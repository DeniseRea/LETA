#!/usr/bin/env python3
"""
fetch_plant_disease_reviews.py

Retrieve systematic literature reviews (SLRs), surveys, and mapping studies about 
machine learning and deep learning applied to plant disease detection and classification
from public APIs:
- Semantic Scholar
- OpenAlex
- CrossRef

Features:
- Query: SLR/survey/mapping + ML/DL + plant disease detection
- Metadata: title, authors, year, DOI, URL, abstract, open_access flag, venue, keywords
- Save results to JSON, CSV, and BibTeX in review/data folder
- Error handling for rate limits and empty responses
- Prioritize open-access papers
- Remove duplicates by DOI
- Support English and Spanish articles

Output files:
- data/plant_disease_reviews.json
- data/plant_disease_reviews.csv
- data/plant_disease_reviews.bib (BibTeX format)
- ReviewResearch/*.txt (individual abstract files)
"""

import csv
import json
import os
import time
import argparse
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
REVIEW_RESEARCH_DIR = os.path.join(BASE_DIR, "ReviewResearch")
OUTPUT_JSON = os.path.join(DATA_DIR, "plant_disease_reviews.json")
OUTPUT_CSV = os.path.join(DATA_DIR, "plant_disease_reviews.csv")
OUTPUT_BIB = os.path.join(DATA_DIR, "plant_disease_reviews.bib")

# API endpoints
SEMANTIC_SCHOLAR_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
OPENALEX_WORKS = "https://api.openalex.org/works"
CROSSREF_WORKS = "https://api.crossref.org/works"

# User-Agent (required by some APIs)
DEFAULT_HEADERS = {
    "User-Agent": "plant_disease_slr_research/1.0 (Academic Research - SLRs on Plant Disease Detection with ML/DL)"
}

# Semantic Scholar API Key (optional, from environment)
SEMANTIC_SCHOLAR_API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
if SEMANTIC_SCHOLAR_API_KEY:
    DEFAULT_HEADERS["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY

# Query - Optimized for systematic literature reviews on plant disease detection with ML/DL
# Based on Kitchenham methodology: SLR/survey/mapping + ML/DL + plant disease/agriculture
# Aligned with research questions RQ1-RQ8 from planning phase
QUERY = '''("systematic review" OR "systematic literature review" OR "SLR" OR "survey" OR "state of the art" OR "mapping study" OR "meta-analysis" OR "scoping review") AND ("deep learning" OR "machine learning" OR "CNN" OR "convolutional neural network" OR "computer vision" OR "artificial intelligence" OR "transfer learning") AND ("plant disease" OR "crop disease" OR "agriculture" OR "plant pathology" OR "disease detection" OR "smart farming" OR "precision agriculture")'''

# Keywords to validate article is a literature review (must contain at least one)
REVIEW_TYPE_KEYWORDS = {
    "systematic literature review", "systematic review", "slr", "survey", "mapping study",
    "systematic mapping", "meta-analysis", "scoping review", "literature review",
    "state of the art", "revisión sistemática", "estado del arte", "revisión de literatura",
    "tertiary study", "umbrella review"
}

# Keywords to validate ML/DL relevance (must contain at least one)
ML_DL_KEYWORDS = {
    "machine learning", "deep learning", "convolutional neural network", "cnn", "neural network",
    "artificial intelligence", "computer vision", "transfer learning", "image classification",
    "feature extraction", "vgg", "resnet", "inception", "mobilenet", "efficientnet",
    "tensorflow", "keras", "pytorch", "alexnet", "densenet",
    "aprendizaje automático", "aprendizaje profundo", "red neuronal convolucional",
    "red neuronal", "inteligencia artificial", "visión por computadora", "aprendizaje por transferencia",
    "clasificación de imágenes", "extracción de características"
}

# Plant disease detection keywords (must contain at least one)
PLANT_DISEASE_KEYWORDS = {
    "plant disease", "plant pathology", "disease detection", "disease classification", "disease identification",
    "leaf disease", "crop disease", "plant health", "phytopathology", "disease diagnosis",
    "symptoms", "lesion", "infection", "pathogen", "agricultural", "agriculture", "crop",
    "image-based detection", "automated detection", "early detection",
    "enfermedad de plantas", "patología vegetal", "detección de enfermedades",
    "clasificación de enfermedades", "identificación de enfermedades", "salud vegetal",
    "síntomas", "lesión", "infección", "patógeno", "agricultura", "agrícola", "cultivo",
    "detección automática", "detección temprana", "diagnóstico"
}

# Keywords to EXCLUDE (noise/irrelevant articles)
EXCLUSION_KEYWORDS = {
    "human disease", "medical diagnosis", "cancer", "tumor", "patient", "clinical",
    "animal disease", "veterinary", "livestock", "genomics", "dna sequencing",
    "soil analysis only", "weather prediction", "climate modeling",
    "enfermedad humana", "diagnóstico médico", "cáncer", "paciente", "clínico",
    "enfermedad animal", "veterinaria", "ganado", "genómica"
}


def check_response(res: requests.Response, provider_name: str) -> Optional[Dict]:
    """
    Validate HTTP response and handle rate limiting.
    
    Args:
        res: requests.Response object
        provider_name: Name of the API provider
        
    Returns:
        Parsed JSON on success, None on error
    """
    if res.status_code == 200:
        try:
            return res.json()
        except ValueError as e:
            logger.error("%s: Failed to parse JSON response - %s", provider_name, str(e))
            return None
    
    if res.status_code == 429:
        retry_after = int(res.headers.get("Retry-After", 5))
        logger.warning("%s: Rate limited (429). Waiting %d seconds.", provider_name, retry_after)
        time.sleep(retry_after)
        return None
    
    if res.status_code == 503:
        logger.warning("%s: Service temporarily unavailable (503).", provider_name)
        time.sleep(3)
        return None
    
    logger.error("%s: HTTP %d - %s", provider_name, res.status_code, res.text[:200])
    return None


def normalize_authors(author_entries) -> List[str]:
    """
    Convert provider-specific author structures to list of author names.
    """
    names = []
    if not author_entries:
        return names
    
    if isinstance(author_entries, list):
        for author in author_entries:
            if isinstance(author, dict):
                # OpenAlex authorship
                if "author" in author and isinstance(author["author"], dict):
                    display_name = author["author"].get("display_name")
                    if display_name:
                        names.append(display_name)
                # Semantic Scholar
                elif "name" in author:
                    names.append(author["name"])
                # CrossRef format
                elif "given" in author or "family" in author:
                    given = author.get("given", "")
                    family = author.get("family", "")
                    full_name = f"{given} {family}".strip()
                    if full_name:
                        names.append(full_name)
            elif isinstance(author, str):
                names.append(author)
    
    return names


def make_paper_record(title: str, authors: List[str], year: Optional[int],
                     doi: Optional[str], url: Optional[str], abstract: Optional[str],
                     open_access: bool, source: str, venue: Optional[str] = None,
                     keywords: Optional[List[str]] = None) -> Dict:
    """
    Create a standardized paper record.
    """
    return {
        "title": title or "",
        "authors": authors or [],
        "year": int(year) if year else None,
        "doi": doi.lower().strip() if doi else None,
        "url": url or None,
        "abstract": abstract or None,
        "keywords": keywords or [],
        "venue": venue or None,
        "open_access": bool(open_access),
        "source": source,
        "retrieved_at": datetime.utcnow().isoformat()
    }


def is_literature_review(record: Dict) -> Dict[str, bool]:
    """
    Validate if article is a literature review about ML/DL for plant disease detection.
    
    Returns dict with flags:
    - review_type: Contains review-type keywords
    - ml_dl: Contains ML/DL keywords
    - plant_disease: Contains plant disease keywords
    - relevant: True if all above are True AND no exclusion keywords
    
    Args:
        record: Paper record dictionary
        
    Returns:
        Dictionary with validation flags
    """
    text_to_check = f"{record.get('title', '')} {record.get('abstract', '')}".lower()
    
    # Check exclusion keywords first
    for exclude_kw in EXCLUSION_KEYWORDS:
        if exclude_kw.lower() in text_to_check:
            return {"review_type": False, "ml_dl": False, "plant_disease": False, "relevant": False}
    
    # Review type present?
    review_found = any(review_kw.lower() in text_to_check for review_kw in REVIEW_TYPE_KEYWORDS)
    
    # ML/DL present?
    ml_dl_found = any(ml_kw.lower() in text_to_check for ml_kw in ML_DL_KEYWORDS)
    
    # Plant disease present?
    plant_disease_found = any(pd_kw.lower() in text_to_check for pd_kw in PLANT_DISEASE_KEYWORDS)
    
    # Relevant if review_type + ML/DL + plant_disease
    is_relevant = review_found and ml_dl_found and plant_disease_found
    
    return {
        "review_type": review_found,
        "ml_dl": ml_dl_found,
        "plant_disease": plant_disease_found,
        "relevant": is_relevant
    }


# ============================================================================
# PROVIDER-SPECIFIC FUNCTIONS
# ============================================================================

def get_semantic_scholar(query: str, since_date: str, limit: int = 50,
                        offset: int = 0, prefer_oa: bool = True) -> List[Dict]:
    """
    Query Semantic Scholar Graph API.
    """
    provider = "Semantic Scholar"
    logger.info("%s: Querying (OA=%s)...", provider, prefer_oa)
    
    params = {
        "query": query,
        "offset": offset,
        "limit": limit,
        "fields": "title,authors,year,url,abstract,isOpenAccess,openAccessPdf,externalIds,venue,s2FieldsOfStudy"
    }
    
    headers = DEFAULT_HEADERS.copy()
    
    for attempt in range(3):
        try:
            res = requests.get(SEMANTIC_SCHOLAR_SEARCH, params=params,
                             headers=headers, timeout=15)
        except requests.RequestException as e:
            logger.warning("%s: Request failed (attempt %d/3) - %s", provider, attempt + 1, str(e))
            time.sleep(2 ** attempt)
            continue
        
        data = check_response(res, provider)
        if data is None:
            time.sleep(2 ** attempt)
            continue
        
        results = []
        items = data.get("data", [])
        logger.info("%s: Retrieved %d items from response.", provider, len(items))
        
        for item in items:
            try:
                year = item.get("year")
                
                # Filter by minimum year
                if year and int(year) < int(since_date[:4]):
                    continue
                
                doi = None
                ext = item.get("externalIds") or {}
                doi = ext.get("DOI") or item.get("doi")
                is_oa = item.get("isOpenAccess") or False
                
                # Skip non-OA if prefer_oa is True
                if prefer_oa and not is_oa:
                    continue
                
                authors = normalize_authors(item.get("authors", []))
                
                # Try to get OA PDF URL
                url = None
                if is_oa:
                    oa_pdf = item.get("openAccessPdf")
                    if isinstance(oa_pdf, dict):
                        url = oa_pdf.get("url")
                
                if not url:
                    url = item.get("url")
                
                venue = item.get("venue")
                
                # Extract keywords from Semantic Scholar (if available)
                keywords = []
                if "s2FieldsOfStudy" in item:
                    fields = item.get("s2FieldsOfStudy", [])
                    if isinstance(fields, list):
                        keywords = [f.get("category") for f in fields if isinstance(f, dict) and f.get("category")]
                
                record = make_paper_record(
                    title=item.get("title"),
                    authors=authors,
                    year=year,
                    doi=doi,
                    url=url,
                    abstract=item.get("abstract"),
                    open_access=is_oa,
                    source=provider,
                    venue=venue,
                    keywords=keywords
                )
                
                # Validate it's a literature review
                relevance_flags = is_literature_review(record)
                if relevance_flags.get("relevant"):
                    results.append(record)
                else:
                    logger.debug("%s: Filtered out non-review article: %s", provider, record.get("title", "")[:50])
                
            except Exception as e:
                logger.debug("%s: Error parsing item - %s", provider, str(e))
                continue
        
        logger.info("%s: Successfully retrieved %d literature reviews.", provider, len(results))
        return results
    
    logger.warning("%s: All retry attempts failed.", provider)
    return []


def get_openalex(query: str, since_date: str, per_page: int = 25,
                 page: int = 1, prefer_oa: bool = True) -> List[Dict]:
    """
    Query OpenAlex works endpoint.
    """
    provider = "OpenAlex"
    logger.info("%s: Querying (OA=%s)...", provider, prefer_oa)
    
    filters = f"from_publication_date:{since_date}"
    if prefer_oa:
        filters += ",is_oa:true"
    
    params = {
        "search": query,
        "filter": filters,
        "per-page": per_page,
        "page": page,
        "select": "title,authorships,publication_date,doi,ids,abstract_inverted_index,primary_location,concepts"
    }
    
    headers = DEFAULT_HEADERS.copy()
    results = []
    
    try:
        res = requests.get(OPENALEX_WORKS, params=params, headers=headers, timeout=15)
        data = check_response(res, provider)
        
        if not data:
            logger.warning("%s: No response received.", provider)
            return []
        
        items = data.get("results", [])
        logger.info("%s: Retrieved %d items from response.", provider, len(items))
        
        for item in items:
            try:
                doi = item.get("doi")
                if not doi:
                    doi = item.get("ids", {}).get("doi")
                
                year = None
                pub_date = item.get("publication_date")
                if pub_date:
                    try:
                        year = int(pub_date.split("-")[0])
                    except (ValueError, IndexError):
                        pass
                
                is_oa = bool(item.get("is_oa"))
                
                # Reconstruct abstract from inverted index
                abstract = None
                inv_index = item.get("abstract_inverted_index")
                if isinstance(inv_index, dict) and inv_index:
                    sorted_tokens = sorted(inv_index.items(),
                                         key=lambda x: min(x[1]) if x[1] else float('inf'))
                    abstract = " ".join([token for token, _ in sorted_tokens])
                
                authors = normalize_authors(item.get("authorships", []))
                
                # Get venue from primary_location
                venue = None
                primary_loc = item.get("primary_location")
                if isinstance(primary_loc, dict):
                    source_obj = primary_loc.get("source")
                    if isinstance(source_obj, dict):
                        venue = source_obj.get("display_name")
                
                # Get URL
                url = None
                oa_locations = item.get("open_access", {}).get("oa_locations", [])
                if oa_locations:
                    url = oa_locations[0].get("url") or oa_locations[0].get("url_for_landing_page")
                
                if not url:
                    ids = item.get("ids", {})
                    url = ids.get("openalex") or item.get("id")
                
                if prefer_oa and not is_oa:
                    continue
                
                # Extract keywords from OpenAlex concepts
                keywords = []
                concepts = item.get("concepts", [])
                if isinstance(concepts, list):
                    # Get top 5 concepts by score
                    sorted_concepts = sorted(concepts, key=lambda x: x.get("score", 0), reverse=True)[:5]
                    keywords = [c.get("display_name") for c in sorted_concepts if c.get("display_name")]
                
                record = make_paper_record(
                    title=item.get("title"),
                    authors=authors,
                    year=year,
                    doi=doi,
                    url=url,
                    abstract=abstract,
                    open_access=is_oa,
                    source=provider,
                    venue=venue,
                    keywords=keywords
                )
                
                # Validate it's a literature review
                relevance_flags = is_literature_review(record)
                if relevance_flags.get("relevant"):
                    results.append(record)
                else:
                    logger.debug("%s: Filtered out non-review article: %s", provider, record.get("title", "")[:50])
                
            except Exception as e:
                logger.debug("%s: Error parsing item - %s", provider, str(e))
                continue
        
        logger.info("%s: Successfully retrieved %d literature reviews.", provider, len(results))
        return results
        
    except requests.RequestException as e:
        logger.error("%s: Request failed - %s", provider, str(e))
        return []


def get_crossref(query: str, since_date: str, rows: int = 20,
                 offset: int = 0, prefer_oa: bool = True) -> List[Dict]:
    """
    Query CrossRef works endpoint.
    """
    provider = "CrossRef"
    logger.info("%s: Querying (OA=%s)...", provider, prefer_oa)
    
    params = {
        "query": query,
        "filter": f"from-pub-date:{since_date}",
        "rows": rows,
        "offset": offset
    }
    
    headers = DEFAULT_HEADERS.copy()
    results = []
    
    for attempt in range(2):
        try:
            res = requests.get(CROSSREF_WORKS, params=params, headers=headers, timeout=15)
        except requests.RequestException as e:
            logger.warning("%s: Request failed (attempt %d/2) - %s", provider, attempt + 1, str(e))
            time.sleep(2 ** attempt)
            continue
        
        data = check_response(res, provider)
        if not data:
            time.sleep(2 ** attempt)
            continue
        
        items = data.get("message", {}).get("items", [])
        logger.info("%s: Retrieved %d items from response.", provider, len(items))
        
        for item in items:
            try:
                # Extract title
                title_raw = item.get("title") or []
                title = ""
                if isinstance(title_raw, list) and title_raw:
                    title = title_raw[0]
                elif isinstance(title_raw, str):
                    title = title_raw
                
                if not title:
                    continue
                
                doi = item.get("DOI")
                
                # Extract year
                year = None
                pub_date = item.get("published-print") or item.get("published-online") or item.get("issued")
                if isinstance(pub_date, dict):
                    date_parts = pub_date.get("date-parts", [])
                    if isinstance(date_parts, list) and date_parts:
                        try:
                            year = int(date_parts[0][0])
                        except (ValueError, IndexError, TypeError):
                            pass
                
                # Check for OA via license
                license_arr = item.get("license") or []
                is_oa = bool(license_arr)
                
                if prefer_oa and not is_oa:
                    continue
                
                # Extract URL
                url = item.get("URL")
                if not url:
                    links = item.get("link") or []
                    for link in links:
                        if isinstance(link, dict) and link.get("URL"):
                            url = link.get("URL")
                            break
                
                authors = normalize_authors(item.get("author", []))
                abstract = item.get("abstract")
                
                # Venue
                venue = None
                container_title = item.get("container-title") or []
                if isinstance(container_title, list) and container_title:
                    venue = container_title[0]
                elif isinstance(container_title, str):
                    venue = container_title
                
                # Extract keywords from CrossRef (if available)
                keywords = []
                subject_arr = item.get("subject") or []
                if isinstance(subject_arr, list):
                    keywords = subject_arr[:5]  # Limit to top 5
                
                record = make_paper_record(
                    title=title,
                    authors=authors,
                    year=year,
                    doi=doi,
                    url=url,
                    abstract=abstract,
                    open_access=is_oa,
                    source=provider,
                    venue=venue,
                    keywords=keywords
                )
                
                # Validate it's a literature review
                relevance_flags = is_literature_review(record)
                if relevance_flags.get("relevant"):
                    results.append(record)
                else:
                    logger.debug("%s: Filtered out non-review article: %s", provider, record.get("title", "")[:50])
                
            except Exception as e:
                logger.debug("%s: Error parsing item - %s", provider, str(e))
                continue
        
        logger.info("%s: Successfully retrieved %d literature reviews.", provider, len(results))
        return results
    
    logger.warning("%s: All retry attempts failed.", provider)
    return []


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def load_existing_records(filepath: str) -> Dict[str, Dict]:
    """
    Load existing records from JSON file to avoid duplicates.
    """
    existing = {}
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                records = json.load(f)
                for record in records:
                    # Re-validate under current relevance rules
                    flags = is_literature_review(record)
                    if flags.get("relevant"):
                        if record.get("doi"):
                            existing[record["doi"].lower()] = record
                        else:
                            key = (record.get("title", ""), str(record.get("year", "")))
                            existing_key = "|".join(key)
                            existing[existing_key] = record
            logger.info("Loaded %d existing records from %s", len(existing), filepath)
        except Exception as e:
            logger.warning("Could not load existing records: %s", str(e))
    return existing


def deduplicate_records(records: List[Dict], existing: Optional[Dict] = None) -> List[Dict]:
    """
    Remove duplicate papers by DOI; fallback to (title, year) pair.
    """
    if existing is None:
        existing = {}
    
    seen = set(existing.keys())
    unique = list(existing.values())
    
    for record in records:
        key = None
        if record.get("doi"):
            key = record["doi"].lower()
            if key in seen:
                continue
        else:
            title_clean = record.get("title", "").strip().lower()
            year = str(record.get("year", ""))
            key = f"{title_clean}___{year}"
            if key in seen:
                continue
        
        seen.add(key)
        unique.append(record)
    
    return unique


def generate_bibtex_key(record: Dict, index: int) -> str:
    """
    Generate a BibTeX citation key.
    Format: FirstAuthorLastName{Year}{Index}
    """
    authors = record.get("authors", [])
    year = record.get("year") or "NODATE"
    
    if authors:
        first_author = authors[0].split()[-1]  # Last name of first author
        first_author = "".join(c for c in first_author if c.isalnum())
    else:
        first_author = "Anonymous"
    
    return f"{first_author}{year}_{index:03d}"


def record_to_bibtex(record: Dict, index: int) -> str:
    """
    Convert a paper record to BibTeX format.
    """
    cite_key = generate_bibtex_key(record, index)
    
    # Determine entry type (most SLRs are @article or @inproceedings)
    entry_type = "article"  # Default
    venue = record.get("venue", "")
    if venue and ("conference" in venue.lower() or "proceedings" in venue.lower()):
        entry_type = "inproceedings"
    
    # Escape special characters in title and abstract
    def escape_tex(text):
        if not text:
            return ""
        text = text.replace("&", "\\&")
        text = text.replace("%", "\\%")
        text = text.replace("$", "\\$")
        text = text.replace("#", "\\#")
        text = text.replace("_", "\\_")
        text = text.replace("{", "\\{")
        text = text.replace("}", "\\}")
        return text
    
    title = escape_tex(record.get("title", ""))
    authors_list = record.get("authors", [])
    authors_str = " and ".join(authors_list) if authors_list else "Anonymous"
    year = record.get("year") or ""
    doi = record.get("doi", "")
    url = record.get("url", "")
    abstract = escape_tex(record.get("abstract", ""))
    venue_str = escape_tex(venue)
    
    # Build BibTeX entry
    bib_lines = [f"@{entry_type}{{{cite_key},"]
    bib_lines.append(f"  title = {{{title}}},")
    bib_lines.append(f"  author = {{{authors_str}}},")
    if year:
        bib_lines.append(f"  year = {{{year}}},")
    if venue_str:
        if entry_type == "article":
            bib_lines.append(f"  journal = {{{venue_str}}},")
        else:
            bib_lines.append(f"  booktitle = {{{venue_str}}},")
    if doi:
        bib_lines.append(f"  doi = {{{doi}}},")
    if url:
        bib_lines.append(f"  url = {{{url}}},")
    if abstract:
        bib_lines.append(f"  abstract = {{{abstract}}},")
    bib_lines.append("}")
    
    return "\n".join(bib_lines)


def save_json(records: List[Dict], filepath: str):
    """Save records to JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    logger.info("Saved %d records to JSON: %s", len(records), filepath)


def save_csv(records: List[Dict], filepath: str):
    """Save records to CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    fieldnames = ["title", "authors", "year", "doi", "url", "venue", "keywords", "abstract", "open_access", "source", "retrieved_at"]
    
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for record in records:
            row = record.copy()
            # Convert authors list to semicolon-separated string
            if isinstance(row.get("authors"), list):
                row["authors"] = "; ".join(row["authors"])
            # Convert keywords list to semicolon-separated string
            if isinstance(row.get("keywords"), list):
                row["keywords"] = "; ".join(row["keywords"])
            writer.writerow(row)
    
    logger.info("Saved %d records to CSV: %s", len(records), filepath)


def save_bibtex(records: List[Dict], filepath: str):
    """Save records to BibTeX file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w", encoding="utf-8") as f:
        for idx, record in enumerate(records, 1):
            bibtex_entry = record_to_bibtex(record, idx)
            f.write(bibtex_entry)
            f.write("\n\n")
    
    logger.info("Saved %d records to BibTeX: %s", len(records), filepath)


def sanitize_filename(title: str, max_length: int = 100) -> str:
    """
    Convert article title to a valid filename.
    
    Args:
        title: Article title
        max_length: Maximum filename length
        
    Returns:
        Sanitized filename
    """
    # Remove invalid filename characters
    invalid_chars = '<>:"/\\|?*'
    filename = title
    for char in invalid_chars:
        filename = filename.replace(char, '')
    
    # Replace spaces and special chars with underscores
    filename = filename.replace(' ', '_')
    filename = ''.join(c if c.isalnum() or c in ('_', '-') else '_' for c in filename)
    
    # Remove multiple consecutive underscores
    while '__' in filename:
        filename = filename.replace('__', '_')
    
    # Truncate to max_length
    if len(filename) > max_length:
        filename = filename[:max_length]
    
    # Remove trailing underscores
    filename = filename.rstrip('_')
    
    return filename


def save_abstracts_to_files(records: List[Dict], output_dir: str):
    """
    Save each paper's abstract and keywords to individual text files.
    
    Args:
        records: List of paper records
        output_dir: Directory to save text files
    """
    os.makedirs(output_dir, exist_ok=True)
    
    saved_count = 0
    for idx, record in enumerate(records, 1):
        title = record.get("title", f"paper_{idx}")
        filename = sanitize_filename(title) + ".txt"
        filepath = os.path.join(output_dir, filename)
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                # Write header
                f.write("="*80 + "\n")
                f.write(f"LITERATURE REVIEW #{idx}\n")
                f.write("="*80 + "\n\n")
                
                # Write title
                f.write(f"TITLE:\n{record.get('title', 'N/A')}\n\n")
                
                # Write authors
                authors = record.get("authors", [])
                if authors:
                    f.write(f"AUTHORS:\n{', '.join(authors)}\n\n")
                else:
                    f.write("AUTHORS:\nN/A\n\n")
                
                # Write year and venue
                year = record.get("year", "N/A")
                venue = record.get("venue", "N/A")
                f.write(f"YEAR: {year}\n")
                f.write(f"VENUE: {venue}\n\n")
                
                # Write DOI and URL
                doi = record.get("doi", "N/A")
                url = record.get("url", "N/A")
                f.write(f"DOI: {doi}\n")
                f.write(f"URL: {url}\n\n")
                
                # Write keywords
                keywords = record.get("keywords", [])
                f.write("KEYWORDS:\n")
                if keywords:
                    for kw in keywords:
                        f.write(f"  - {kw}\n")
                else:
                    f.write("  N/A\n")
                f.write("\n")
                
                # Write abstract
                f.write("ABSTRACT:\n")
                f.write("-"*80 + "\n")
                abstract = record.get("abstract")
                if abstract and abstract.strip():
                    f.write(abstract.strip())
                else:
                    f.write("Abstract not available.")
                f.write("\n" + "-"*80 + "\n\n")
                
                # Write metadata
                f.write("METADATA:\n")
                f.write(f"  Source: {record.get('source', 'N/A')}\n")
                f.write(f"  Open Access: {'Yes' if record.get('open_access') else 'No'}\n")
                f.write(f"  Retrieved: {record.get('retrieved_at', 'N/A')}\n")
                
            saved_count += 1
            logger.debug("Saved abstract to: %s", filepath)
            
        except Exception as e:
            logger.warning("Failed to save abstract for '%s': %s", title[:50], str(e))
            continue
    
    logger.info("Saved %d abstracts to directory: %s", saved_count, output_dir)


def print_summary(records: List[Dict]):
    """Print a summary of retrieved papers."""
    print("\n" + "="*100)
    print(f"RETRIEVED {len(records)} LITERATURE REVIEWS (SLRs, Surveys, Mapping Studies)")
    print("="*100 + "\n")
    
    oa_count = sum(1 for r in records if r.get("open_access"))
    non_oa_count = len(records) - oa_count
    
    print(f"Summary Statistics:")
    print(f"  Total Literature Reviews: {len(records)}")
    print(f"  Open Access: {oa_count}")
    print(f"  Non-OA: {non_oa_count}")
    print(f"  Query: {QUERY}\n")
    
    # Print detailed list
    for idx, record in enumerate(records, 1):
        doi_str = record.get("doi") or "N/A"
        oa_str = "✓ OA" if record.get("open_access") else "Non-OA"
        year_str = str(record.get("year")) if record.get("year") else "N/A"
        source_str = record.get("source", "Unknown")
        venue_str = record.get("venue") or "N/A"
        
        print(f"{idx}. [{oa_str}] {record.get('title', 'N/A')[:80]}")
        print(f"   Year: {year_str} | DOI: {doi_str}")
        print(f"   Venue: {venue_str[:60] if venue_str != 'N/A' else 'N/A'}")
        print(f"   Authors: {', '.join(record.get('authors', [])[:3]) if record.get('authors') else 'N/A'}")
        print(f"   Source: {source_str}")
        print()


# ============================================================================
# MAIN ORCHESTRATION
# ============================================================================

def fetch_literature_reviews(target_count: int = 20, since_years: int = 5,
                            providers_priority: Optional[List[str]] = None) -> List[Dict]:
    """
    Orchestrate literature review fetching from all providers.
    """
    if providers_priority is None:
        providers_priority = ["Semantic Scholar", "OpenAlex", "CrossRef"]
    
    since_date = (datetime.utcnow() - timedelta(days=since_years * 365)).strftime("%Y-%m-%d")
    logger.info("Searching for literature reviews since: %s", since_date)
    
    # Load existing records to avoid duplicates
    existing_records = load_existing_records(OUTPUT_JSON)
    logger.info("Found %d existing records.", len(existing_records))
    
    all_records = []
    
    # Phase 1: Fetch OA papers
    logger.info("\n=== PHASE 1: Fetching Open-Access Literature Reviews ===")
    for provider in providers_priority:
        if len(all_records) >= target_count:
            logger.info("Target count reached. Stopping Phase 1.")
            break
        
        try:
            if provider == "Semantic Scholar":
                records = get_semantic_scholar(QUERY, since_date=since_date,
                                             limit=50, offset=0, prefer_oa=True)
            elif provider == "OpenAlex":
                records = get_openalex(QUERY, since_date=since_date,
                                      per_page=25, page=1, prefer_oa=True)
            elif provider == "CrossRef":
                records = get_crossref(QUERY, since_date=since_date,
                                      rows=25, offset=0, prefer_oa=True)
            else:
                records = []
            
            logger.info("%s: Got %d OA literature reviews", provider, len(records))
            all_records.extend(records)
            
            # Deduplicate incrementally
            all_records = deduplicate_records(all_records, existing_records)
            
        except Exception as e:
            logger.error("Error fetching from %s: %s", provider, str(e))
            continue
    
    # Phase 2: If not enough OA papers, fetch non-OA
    if len(all_records) < target_count:
        needed = target_count - len(all_records)
        logger.info("\n=== PHASE 2: Need %d more papers (including non-OA) ===", needed)
        
        for provider in providers_priority:
            if len(all_records) >= target_count:
                logger.info("Target count reached. Stopping Phase 2.")
                break
            
            try:
                if provider == "Semantic Scholar":
                    records = get_semantic_scholar(QUERY, since_date=since_date,
                                                 limit=50, offset=0, prefer_oa=False)
                elif provider == "OpenAlex":
                    records = get_openalex(QUERY, since_date=since_date,
                                          per_page=25, page=1, prefer_oa=False)
                elif provider == "CrossRef":
                    records = get_crossref(QUERY, since_date=since_date,
                                          rows=25, offset=0, prefer_oa=False)
                else:
                    records = []
                
                logger.info("%s: Got %d additional literature reviews (non-OA included)", provider, len(records))
                
                all_records.extend(records)
                all_records = deduplicate_records(all_records, existing_records)
                
            except Exception as e:
                logger.error("Error fetching from %s: %s", provider, str(e))
                continue
    
    # Final cleanup
    all_records = deduplicate_records(all_records, existing_records)
    if len(all_records) > target_count:
        all_records = all_records[:target_count]
    
    logger.info("\n=== FINAL RESULTS ===")
    logger.info("Total unique literature reviews retrieved: %d", len(all_records))
    
    return all_records


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Fetch literature reviews (SLRs, surveys) about ML/DL for plant disease detection"
    )
    parser.add_argument("--count", type=int, default=20,
                       help="Number of literature reviews to retrieve (default: 20)")
    parser.add_argument("--years", type=int, default=5,
                       help="Years back to search (default: 5)")
    parser.add_argument("--out-json", type=str, default=OUTPUT_JSON,
                       help=f"Output JSON file (default: {OUTPUT_JSON})")
    parser.add_argument("--out-csv", type=str, default=OUTPUT_CSV,
                       help=f"Output CSV file (default: {OUTPUT_CSV})")
    parser.add_argument("--out-bib", type=str, default=OUTPUT_BIB,
                       help=f"Output BibTeX file (default: {OUTPUT_BIB})")
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()
    
    logger.info("="*100)
    logger.info("STARTING LITERATURE REVIEW RETRIEVAL")
    logger.info("="*100)
    logger.info("Target: %d literature reviews from the last %d years", args.count, args.years)
    
    # Fetch literature reviews
    records = fetch_literature_reviews(target_count=args.count, since_years=args.years)
    
    if not records:
        logger.error("No literature reviews retrieved. Check your internet connection and API availability.")
        return
    
    # Save results
    try:
        save_json(records, args.out_json)
        save_csv(records, args.out_csv)
        save_bibtex(records, args.out_bib)
        save_abstracts_to_files(records, REVIEW_RESEARCH_DIR)
    except Exception as e:
        logger.error("Error saving results: %s", str(e))
        return
    
    # Print summary
    print_summary(records)
    
    logger.info("\n" + "="*100)
    logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    logger.info("="*100)
    logger.info("Output files:")
    logger.info("  - JSON: %s", args.out_json)
    logger.info("  - CSV: %s", args.out_csv)
    logger.info("  - BibTeX: %s", args.out_bib)
    logger.info("  - Abstracts: %s", REVIEW_RESEARCH_DIR)


if __name__ == "__main__":
    main()