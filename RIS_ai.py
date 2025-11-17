#!/usr/bin/env python3
"""
Exportar RIS por DOI: lee data/papers.json y crea un .ris por cada DOI en data/RIS.
- No crea otros archivos.
- Usa content-negotiation via doi.org (Accept: application/x-research-info-systems).
- Manejo básico de reintentos y backoff.
"""
import os
import re
import json
import time
import requests
from urllib.parse import quote_plus

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
PAPERS_JSON = os.path.join(DATA_DIR, "papers.json")
OUT_DIR = os.path.join(DATA_DIR, "RIS")

HEADERS = {
    "User-Agent": "export_ris_from_json/1.0 (mailto:your-email@example.com)",
    "Accept": "application/x-research-info-systems"
}

def normalize_doi(doi_raw: str) -> str:
    if not doi_raw:
        return ""
    doi_raw = doi_raw.strip()
    m = re.search(r'(10\.\d{4,9}/[^\s"\'<>]+)', doi_raw)
    if m:
        return m.group(1)
    if doi_raw.lower().startswith("doi:"):
        return doi_raw[4:].strip()
    if doi_raw.startswith("10."):
        return doi_raw
    return ""

def safe_filename(doi: str) -> str:
    s = doi.strip().lower()
    s = re.sub(r'[^0-9a-z._-]', '_', s)
    return s + ".ris"

def fetch_ris(doi: str, tries: int = 3, timeout: int = 20) -> str:
    if not doi:
        return ""
    url = f"https://doi.org/{quote_plus(doi)}"
    for attempt in range(1, tries + 1):
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout)
            if r.status_code == 200:
                text = r.text.strip()
                if text and ("TY  -" in text or text.startswith("TY  -") or text.startswith("TY -")):
                    return text
                # if server responded but not RIS, assume not available
                return ""
            if r.status_code in (429, 503):
                wait = int(r.headers.get("Retry-After", 5))
                time.sleep(wait)
            else:
                return ""
        except requests.RequestException:
            time.sleep(2 ** attempt)
    return ""

def main():
    if not os.path.exists(PAPERS_JSON):
        print(f"No encontrado: {PAPERS_JSON}")
        return
    try:
        with open(PAPERS_JSON, "r", encoding="utf-8") as fd:
            papers = json.load(fd)
    except Exception as e:
        print(f"Error leyendo JSON: {e}")
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    fetched = 0
    failed = 0
    seen = set()
    for p in papers:
        doi_raw = p.get("doi", "") or p.get("DOI", "")
        doi = normalize_doi(doi_raw)
        if not doi or doi in seen:
            continue
        seen.add(doi)
        ris_text = fetch_ris(doi)
        if not ris_text:
            failed += 1
            continue
        fname = os.path.join(OUT_DIR, safe_filename(doi))
        try:
            with open(fname, "w", encoding="utf-8") as f:
                f.write(ris_text + "\n")
            fetched += 1
        except Exception:
            failed += 1
        time.sleep(1)  # cortesía entre peticiones

    print(f"RIS creados: {fetched}, fallados: {failed}, guardados en: {OUT_DIR}")

if __name__ == "__main__":
    main()