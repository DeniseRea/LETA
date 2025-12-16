Create a Python script that retrieves at least 20 recent scientific articles (from the last 5 years) about artificial intelligence applied to software development, using only public and legal APIs (NO webscraping).

Requirements:
- Use the Semantic Scholar API, CrossRef API, and/or OpenAlex API.
- The script must send an HTTP request with a query such as:
  "artificial intelligence" AND "software development" OR "software engineering".
- Return metadata including: title, authors, year, DOI, URL, and abstract (if available).
- Save the results in a JSON or CSV file.
- Include error handling (rate limits, empty responses, etc.).
- The code must be clean, commented, and easy to modify.
- Do NOT use scraped HTML; only API endpoints.
- Add a function for each provider (Semantic Scholar, CrossRef, OpenAlex).
- Add a main() function that aggregates all results and removes duplicates by DOI.
- Ensure the final script prints a summary list of all retrieved papers.
- Prioritize open-access (OA) papers: attempt to return OA papers first (semantic_scholar: isOpenAccess, openalex: is_oa, crossref: license info). If fewer than the required number of OA papers are found, include non-OA papers as needed but mark OA status in the results.
