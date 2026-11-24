"""Mention and URL-citation detectors for the AI Visibility prototype.

These functions only inspect model text. They do not verify that a cited URL
is real or that a claim is accurate.
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

URL_RE = re.compile(r"https?://[^\s\]\)>\"'<>]+", re.I)


def extract_urls(text: str) -> list[str]:
    urls: list[str] = []
    for raw in URL_RE.findall(text or ""):
        cleaned = raw.rstrip(").,;:]'\"")
        if cleaned:
            urls.append(cleaned)
    return urls


def domain_of(url: str) -> str:
    value = url if "://" in url else "https://" + url
    host = (urlparse(value).netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]
    return host


def _term_pattern(term: str) -> re.Pattern[str]:
    escaped = re.escape(term.strip())
    return re.compile(
        rf"(?<![A-Za-z0-9_]){escaped}(?:['’]s)?(?![A-Za-z0-9_])",
        re.I,
    )


def matched_names(text: str, names: list[str]) -> list[str]:
    hits: list[str] = []
    body = text or ""
    for name in names:
        if not name or not name.strip():
            continue
        if _term_pattern(name).search(body) and name not in hits:
            hits.append(name)
    return hits


def cited_urls_for_domains(text: str, domains: list[str]) -> list[str]:
    wanted = []
    for domain in domains or []:
        host = domain.lower().strip()
        if host.startswith("www."):
            host = host[4:]
        if host:
            wanted.append(host)
    hits: list[str] = []
    for url in extract_urls(text):
        host = domain_of(url)
        for domain in wanted:
            if host == domain or host.endswith("." + domain):
                if url not in hits:
                    hits.append(url)
                break
    return hits


def analyze_answer(text: str, brand: dict, competitors: list[dict]) -> dict:
    brand_names = [brand.get("name", "")] + list(brand.get("aliases") or [])
    brand_hits = matched_names(text, brand_names)
    brand_cites = cited_urls_for_domains(text, brand.get("domains") or [])
    competitor_rows = []
    for competitor in competitors:
        names = [competitor.get("name", "")] + list(competitor.get("aliases") or [])
        name_hits = matched_names(text, names)
        competitor_rows.append(
            {
                "name": competitor.get("name", ""),
                "mentioned": bool(name_hits),
                "matched_names": name_hits,
                "cited_urls": cited_urls_for_domains(
                    text, competitor.get("domains") or []
                ),
            }
        )
    return {
        "brand_mentioned": bool(brand_hits),
        "brand_matched_names": brand_hits,
        "brand_cited_urls": brand_cites,
        "urls": extract_urls(text),
        "competitors": competitor_rows,
    }


def summarize_run(rows: list[dict], competitors: list[dict]) -> dict:
    n = len(rows)
    brand_mentions = sum(1 for row in rows if row.get("brand_mentioned"))
    brand_cites = sum(1 for row in rows if row.get("brand_cited_urls"))
    competitor_mentions = {}
    competitor_cites = {}
    for competitor in competitors:
        name = competitor["name"]
        competitor_mentions[name] = sum(
            1
            for row in rows
            for item in row.get("competitors") or []
            if item.get("name") == name and item.get("mentioned")
        )
        competitor_cites[name] = sum(
            1
            for row in rows
            for item in row.get("competitors") or []
            if item.get("name") == name and item.get("cited_urls")
        )
    return {
        "questions": n,
        "brand_mention_count": brand_mentions,
        "brand_mention_rate": (brand_mentions / n) if n else 0.0,
        "brand_citation_count": brand_cites,
        "brand_citation_rate": (brand_cites / n) if n else 0.0,
        "competitor_mention_counts": competitor_mentions,
        "competitor_citation_counts": competitor_cites,
    }
