#!/usr/bin/env python3
"""
fetch_plant_disease_papers.py

Retrieve recent (last 5 years) scientific articles about machine learning and deep learning
applied to plant disease detection and classification from public APIs:
- Semantic Scholar
- OpenAlex
- CrossRef

Features:
- Query: ML/DL + plant disease detection + image classification
- Metadata: title, authors, year, DOI, URL, abstract, open_access flag
- Save results to JSON and CSV in review/data folder
- Error handling for rate limits and empty responses
- Prioritize open-access papers
- Remove duplicates by DOI
- Support English and Spanish articles
- Focus on practical/agricultural applications with datasets
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
DATA_DIR = os.path.join(BASE_DIR, "data")  # review/data folder
OUTPUT_JSON = os.path.join(DATA_DIR, "plant_disease_papers.json")
OUTPUT_CSV = os.path.join(DATA_DIR, "plant_disease_papers.csv")

# API endpoints
SEMANTIC_SCHOLAR_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
OPENALEX_WORKS = "https://api.openalex.org/works"
CROSSREF_WORKS = "https://api.crossref.org/works"

# User-Agent (required by some APIs)
DEFAULT_HEADERS = {
    "User-Agent": "plant_disease_research/1.0 (Academic Research - Plant Disease Detection with ML/DL)"
}

# Semantic Scholar API Key (optional, from environment)
SEMANTIC_SCHOLAR_API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
if SEMANTIC_SCHOLAR_API_KEY:
    DEFAULT_HEADERS["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY

# Query - Optimized for plant disease detection with ML/DL comparison
# Based on project.md: Python (TensorFlow/Keras/PyTorch) vs Edge Impulse
# Aligned with Kitchenham methodology PICOC framework
QUERY = '''("machine learning" OR "deep learning" OR "convolutional neural network" OR "CNN" OR "transfer learning" OR "image classification" OR "computer vision") AND ("plant disease" OR "crop disease" OR "leaf disease" OR "plant pathology" OR "disease detection" OR "disease classification" OR "phytopathology") AND ("TensorFlow" OR "Keras" OR "PyTorch" OR "Edge Impulse" OR "MobileNet" OR "ResNet" OR "VGG" OR "EfficientNet" OR "dataset" OR "benchmark" OR "PlantVillage")'''

# Keywords to validate article relevance (must contain at least one)
ML_DL_KEYWORDS = {
    "machine learning", "deep learning", "convolutional neural network", "cnn", "neural network",
    "artificial intelligence", "computer vision", "transfer learning", "image classification",
    "feature extraction", "vgg", "resnet", "inception", "mobilenet", "efficientnet",
    "tensorflow", "keras", "pytorch", "alexnet", "densenet",
    "aprendizaje automático", "aprendizaje profundo", "red neuronal convolucional",
    "red neuronal", "inteligencia artificial", "visión por computadora", "aprendizaje por transferencia",
    "clasificación de imágenes", "extracción de características"
}

# Keywords to EXCLUDE (noise/irrelevant articles)
EXCLUSION_KEYWORDS = {
    "human disease", "medical diagnosis", "cancer", "tumor", "patient", "clinical",
    "animal disease", "veterinary", "livestock", "genomics", "dna sequencing",
    "soil analysis", "weather prediction", "climate modeling",
    "enfermedad humana", "diagnóstico médico", "cáncer", "paciente", "clínico",
    "enfermedad animal", "veterinaria", "ganado", "genómica",
    "conference proceedings", "book of abstracts", "keynote"
}

# Agriculture / practical application keywords (prefer these to ensure real-world relevance)
AGRICULTURE_APPLICATION_KEYWORDS = {
    "agriculture", "farming", "crop", "cultivation", "field", "greenhouse", "agricultural",
    "precision agriculture", "smart farming", "digital agriculture", "agricultura de precisión",
    "case study", "case studies", "real-world", "real world", "empirical", "evaluation",
    "dataset", "benchmark", "experimental", "validation", "field study", "practical application",
    "mobile application", "edge device", "iot", "embedded system", "smartphone",
    "agricultura", "cultivo", "agrícola", "campo", "invernadero",
    "aplicación móvil", "dispositivo", "aplicación práctica", "estudio de campo"
}

# Plant disease detection keywords (reinforce disease detection context)
PLANT_DISEASE_KEYWORDS = {
    "plant disease", "plant pathology", "disease detection", "disease classification", "disease identification",
    "leaf disease", "crop disease", "plant health", "phytopathology", "disease diagnosis",
    "symptoms", "lesion", "infection", "pathogen", "fungi", "bacteria", "virus",
    "image-based detection", "automated detection", "early detection",
    "enfermedad de plantas", "patología vegetal", "detección de enfermedades",
    "clasificación de enfermedades", "identificación de enfermedades", "salud vegetal",
    "síntomas", "lesión", "infección", "patógeno", "hongos", "bacteria", "virus",
    "detección automática", "detección temprana", "diagnóstico"
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
        # Rate limited
        retry_after = int(res.headers.get("Retry-After", 5))
        logger.warning("%s: Rate limited (429). Waiting %d seconds.", provider_name, retry_after)
        time.sleep(retry_after)
        return None
    
    if res.status_code == 503:
        # Service unavailable
        logger.warning("%s: Service temporarily unavailable (503).", provider_name)
        time.sleep(3)
        return None
    
    logger.error("%s: HTTP %d - %s", provider_name, res.status_code, res.text[:200])
    return None


def normalize_authors(author_entries) -> List[str]:
    """
    Convert provider-specific author structures to list of author names.
    
    Handles:
    - Semantic Scholar: list of dicts with 'name'
    - OpenAlex: authorship list with author.display_name
    - CrossRef: list of dicts with 'given' and 'family'
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
                     open_access: bool, source: str, agriculture_relevant: bool=False) -> Dict:
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
        "open_access": bool(open_access),
        "agriculture_relevant": bool(agriculture_relevant),
        "source": source,
        "retrieved_at": datetime.utcnow().isoformat()
    }


def is_relevant_article(record: Dict) -> Dict[str, bool]:
    """
    Validate if article is relevant for ML/DL for plant disease detection.
    
    Returns True if:
    - Contains ML/DL keywords in title or abstract
    - Contains plant disease keywords
    - Does NOT contain exclusion keywords
    - Preferably has agriculture/practical application context
    
    Args:
        record: Paper record dictionary
        
    Returns:
        Dictionary with validation flags
    """
    text_to_check = f"{record.get('title', '')} {record.get('abstract', '')}".lower()
    
    # Check exclusion keywords first
    for exclude_kw in EXCLUSION_KEYWORDS:
        if exclude_kw.lower() in text_to_check:
            return {"ml_dl": False, "plant_disease": False, "agriculture": False, "practical": False, "relevant": False}

    # ML/DL present?
    ml_dl_found = any(ml_kw.lower() in text_to_check for ml_kw in ML_DL_KEYWORDS)

    # Plant disease present?
    plant_disease_found = any(pd_kw.lower() in text_to_check for pd_kw in PLANT_DISEASE_KEYWORDS)

    # Agriculture or practical application presence
    agriculture_found = any(ag_kw.lower() in text_to_check for ag_kw in AGRICULTURE_APPLICATION_KEYWORDS)
    practical_found = any(pr_kw.lower() in text_to_check for pr_kw in {"case study", "case studies", "empirical", "real world", "real-world", "dataset", "benchmark", "evaluation", "experimental", "validation"})

    # Relevant if ML/DL + Plant Disease + (agriculture OR practical)
    is_relevant = ml_dl_found and plant_disease_found and (agriculture_found or practical_found)
    return {"ml_dl": ml_dl_found, "plant_disease": plant_disease_found, "agriculture": agriculture_found, "practical": practical_found, "relevant": is_relevant}


# ============================================================================
# PROVIDER-SPECIFIC FUNCTIONS
# ============================================================================

def get_semantic_scholar(query: str, since_date: str, limit: int = 50, 
                        offset: int = 0, prefer_oa: bool = True) -> List[Dict]:
    """
    Query Semantic Scholar Graph API.
    
    Endpoint: https://api.semanticscholar.org/graph/v1/paper/search
    Fields: title, authors, year, doi, url, abstract, isOpenAccess, openAccessPdf
    """
    provider = "Semantic Scholar"
    logger.info("%s: Querying (OA=%s)...", provider, prefer_oa)
    
    params = {
        "query": query,
        "offset": offset,
        "limit": limit,
        # 'doi' is not a valid field in the Semantic Scholar search API; use externalIds for DOI
        "fields": "title,authors,year,url,abstract,isOpenAccess,openAccessPdf,externalIds"
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
                # Semantic Scholar may provide DOI in externalIds
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
                
                record = make_paper_record(
                    title=item.get("title"),
                    authors=authors,
                    year=year,
                    doi=doi,
                    url=url,
                    abstract=item.get("abstract"),
                    open_access=is_oa,
                    source=provider
                )
                
                # Validate relevance (ML/DL + Plant Disease + (agriculture|practical))
                relevance_flags = is_relevant_article(record)
                if relevance_flags.get("relevant"):
                    # annotate record with agriculture/practical relevance
                    record["agriculture_relevant"] = bool(relevance_flags.get("agriculture") or relevance_flags.get("practical"))
                    results.append(record)
                else:
                    logger.debug("%s: Filtered out non-relevant article: %s", provider, record.get("title", "")[:50])
                
            except Exception as e:
                logger.debug("%s: Error parsing item - %s", provider, str(e))
                continue
        
        logger.info("%s: Successfully retrieved %d papers.", provider, len(results))
        return results
    
    logger.warning("%s: All retry attempts failed.", provider)
    return []


def get_openalex(query: str, since_date: str, per_page: int = 25, 
                 page: int = 1, prefer_oa: bool = True) -> List[Dict]:
    """
    Query OpenAlex works endpoint.
    
    Endpoint: https://api.openalex.org/works
    Supports filtering by publication date and open access status.
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
        # select valid OpenAlex fields only; OA status will still be available in nested 'open_access' object
        "select": "title,authorships,publication_date,doi,ids,abstract_inverted_index"
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
                    # Sort tokens by their first position for readability
                    sorted_tokens = sorted(inv_index.items(), 
                                         key=lambda x: min(x[1]) if x[1] else float('inf'))
                    abstract = " ".join([token for token, _ in sorted_tokens])
                
                authors = normalize_authors(item.get("authorships", []))
                
                # Get URL from OA locations or OpenAlex ID
                url = None
                oa_locations = item.get("open_access", {}).get("oa_locations", [])
                if oa_locations:
                    url = oa_locations[0].get("url") or oa_locations[0].get("url_for_landing_page")
                
                if not url:
                    ids = item.get("ids", {})
                    url = ids.get("openalex") or item.get("id")
                
                if prefer_oa and not is_oa:
                    continue
                
                record = make_paper_record(
                    title=item.get("title"),
                    authors=authors,
                    year=year,
                    doi=doi,
                    url=url,
                    abstract=abstract,
                    open_access=is_oa,
                    source=provider
                )
                
                # Validate relevance (ML/DL + Plant Disease + (agriculture|practical))
                relevance_flags = is_relevant_article(record)
                if relevance_flags.get("relevant"):
                    record["agriculture_relevant"] = bool(relevance_flags.get("agriculture") or relevance_flags.get("practical"))
                    results.append(record)
                else:
                    logger.debug("%s: Filtered out non-relevant article: %s", provider, record.get("title", "")[:50])
                
            except Exception as e:
                logger.debug("%s: Error parsing item - %s", provider, str(e))
                continue
        
        logger.info("%s: Successfully retrieved %d papers.", provider, len(results))
        return results
        
    except requests.RequestException as e:
        logger.error("%s: Request failed - %s", provider, str(e))
        return []


def get_crossref(query: str, since_date: str, rows: int = 20, 
                 offset: int = 0, prefer_oa: bool = True) -> List[Dict]:
    """
    Query CrossRef works endpoint.
    
    Endpoint: https://api.crossref.org/works
    Note: CrossRef doesn't have explicit OA flag; we check for license info.
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
                
                record = make_paper_record(
                    title=title,
                    authors=authors,
                    year=year,
                    doi=doi,
                    url=url,
                    abstract=abstract,
                    open_access=is_oa,
                    source=provider
                )
                
                # Validate relevance (ML/DL + Plant Disease + (agriculture|practical))
                relevance_flags = is_relevant_article(record)
                if relevance_flags.get("relevant"):
                    record["agriculture_relevant"] = bool(relevance_flags.get("agriculture") or relevance_flags.get("practical"))
                    results.append(record)
                else:
                    logger.debug("%s: Filtered out non-relevant article: %s", provider, record.get("title", "")[:50])
                
            except Exception as e:
                logger.debug("%s: Error parsing item - %s", provider, str(e))
                continue
        
        logger.info("%s: Successfully retrieved %d papers.", provider, len(results))
        return results
    
    logger.warning("%s: All retry attempts failed.", provider)
    return []


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def load_existing_records(filepath: str) -> Dict[str, Dict]:
    """
    Load existing records from JSON file to avoid duplicates.
    Returns dict keyed by DOI for fast lookup.
    
    Args:
        filepath: Path to JSON file
        
    Returns:
        Dictionary of existing records keyed by DOI
    """
    existing = {}
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                records = json.load(f)
                for record in records:
                    # Evaluate existing record under new relevance rules; keep only relevant ones
                    flags = is_relevant_article(record)
                    if flags.get("relevant"):
                        # annotate enterprise flag
                        record["enterprise_relevant"] = bool(flags.get("enterprise") or flags.get("empirical"))
                        if record.get("doi"):
                            existing[record["doi"].lower()] = record
                        else:
                            # fallback to title+year key; still include under its DOI key if missing
                            key = (record.get("title",""), str(record.get("year","")))
                            existing_key = "|".join(key)
                            existing[existing_key] = record
            logger.info("Loaded %d existing records from %s", len(existing), filepath)
        except Exception as e:
            logger.warning("Could not load existing records: %s", str(e))
    return existing


def deduplicate_records(records: List[Dict], existing: Optional[Dict] = None) -> List[Dict]:
    """
    Remove duplicate papers by DOI; fallback to (title, year) pair.
    Also avoids duplicates from previous executions.
    
    Args:
        records: List of paper records
        existing: Dictionary of existing records (optional)
        
    Returns:
        Deduplicated list of records
    """
    if existing is None:
        existing = {}
    
    seen = set(existing.keys())  # Start with existing DOIs
    unique = list(existing.values())  # Start with existing records
    
    for record in records:
        # Try DOI first
        key = None
        if record.get("doi"):
            key = record["doi"].lower()
            if key in seen:
                continue
        else:
            # Fallback to title + year
            title_clean = record.get("title", "").strip().lower()
            year = str(record.get("year", ""))
            key = f"{title_clean}___{year}"
            if key in seen:
                continue
        
        seen.add(key)
        unique.append(record)
    
    return unique


def save_json(records: List[Dict], filepath: str):
    """Save records to JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    logger.info("Saved %d records to JSON: %s", len(records), filepath)


def save_csv(records: List[Dict], filepath: str):
    """Save records to CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    fieldnames = ["title", "authors", "year", "doi", "url", "abstract", "open_access", "agriculture_relevant", "source", "retrieved_at"]
    
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        
        for record in records:
            row = record.copy()
            # Convert authors list to semicolon-separated string
            if isinstance(row.get("authors"), list):
                row["authors"] = "; ".join(row["authors"])
            # ensure agriculture_relevant field exists
            if "agriculture_relevant" not in row:
                row["agriculture_relevant"] = False
            writer.writerow(row)
    
    logger.info("Saved %d records to CSV: %s", len(records), filepath)


def print_summary(records: List[Dict]):
    """Print a summary of retrieved papers."""
    print("\n" + "="*100)
    print(f"RETRIEVED {len(records)} SCIENTIFIC ARTICLES")
    print("="*100 + "\n")
    
    oa_count = sum(1 for r in records if r.get("open_access"))
    non_oa_count = len(records) - oa_count
    agriculture_count = sum(1 for r in records if r.get("agriculture_relevant"))
    
    print(f"Summary Statistics:")
    print(f"  Total Papers: {len(records)}")
    print(f"  Open Access: {oa_count}")
    print(f"  Non-OA: {non_oa_count}")
    print(f"  Agriculture/Practical Application: {agriculture_count}")
    print(f"  Query: {QUERY}\n")
    
    # Print detailed list
    for idx, record in enumerate(records, 1):
        doi_str = record.get("doi") or "N/A"
        oa_str = "✓ OA" if record.get("open_access") else "Non-OA"
        year_str = str(record.get("year")) if record.get("year") else "N/A"
        source_str = record.get("source", "Unknown")
        
        print(f"{idx}. [{oa_str}] {record.get('title', 'N/A')[:80]}")
        print(f"   Year: {year_str} | DOI: {doi_str}")
        print(f"   Authors: {', '.join(record.get('authors', [])[:3]) if record.get('authors') else 'N/A'}")
        print(f"   Source: {source_str}")
        print()


# ============================================================================
# MAIN ORCHESTRATION
# ============================================================================

def fetch_papers(target_count: int = 20, since_years: int = 5, 
                providers_priority: Optional[List[str]] = None) -> List[Dict]:
    """
    Orchestrate paper fetching from all providers.
    
    Strategy:
    1. Load existing records from files to avoid duplicates
    2. Fetch OA papers first from all providers
    3. If not enough OA papers, include non-OA papers
    4. Deduplicate and limit to target_count
    
    Args:
        target_count: Minimum number of papers to retrieve
        since_years: How many years back to search
        providers_priority: List of providers to query in order
        
    Returns:
        List of paper records
    """
    if providers_priority is None:
        providers_priority = ["Semantic Scholar", "OpenAlex", "CrossRef"]
    
    since_date = (datetime.utcnow() - timedelta(days=since_years * 365)).strftime("%Y-%m-%d")
    logger.info("Searching for papers since: %s", since_date)
    
    # Load existing records to avoid duplicates
    existing_records = load_existing_records(OUTPUT_JSON)
    logger.info("Found %d existing records.", len(existing_records))
    
    all_records = []
    
    # Phase 1: Fetch OA papers
    logger.info("\n=== PHASE 1: Fetching Open-Access Papers ===")
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
            
            logger.info("%s: Got %d OA papers", provider, len(records))
            all_records.extend(records)
            
            # Deduplicate incrementally (including existing records)
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
                
                logger.info("%s: Got %d additional papers (non-OA included)", provider, len(records))
                
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
    logger.info("Total unique papers retrieved: %d", len(all_records))
    
    return all_records


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Fetch ML/DL papers for plant disease detection from public APIs"
    )
    parser.add_argument("--count", type=int, default=20, 
                       help="Number of papers to retrieve (default: 20)")
    parser.add_argument("--years", type=int, default=5, 
                       help="Years back to search (default: 5)")
    parser.add_argument("--out-json", type=str, default=OUTPUT_JSON,
                       help=f"Output JSON file (default: {OUTPUT_JSON})")
    parser.add_argument("--out-csv", type=str, default=OUTPUT_CSV,
                       help=f"Output CSV file (default: {OUTPUT_CSV})")
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()
    
    logger.info("="*100)
    logger.info("STARTING SCIENTIFIC PAPER RETRIEVAL")
    logger.info("="*100)
    logger.info("Target: %d papers from the last %d years", args.count, args.years)
    
    # Fetch papers
    records = fetch_papers(target_count=args.count, since_years=args.years)
    
    if not records:
        logger.error("No papers retrieved. Check your internet connection and API availability.")
        return
    
    # Save results
    try:
        save_json(records, args.out_json)
        save_csv(records, args.out_csv)
    except Exception as e:
        logger.error("Error saving results: %s", str(e))
        return
    
    # Print summary
    print_summary(records)
    
    logger.info("\n" + "="*100)
    logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    logger.info("="*100)


if __name__ == "__main__":
    main()