#!/usr/bin/env python3
"""Unit tests for mention and citation detection. No network and no API key."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from detect import (
    analyze_answer,
    cited_urls_for_domains,
    extract_urls,
    matched_names,
    summarize_run,
)

BRAND = {
    "name": "WireReady",
    "aliases": ["Wire Ready", "Wire-Ready"],
    "domains": ["wireready-pilot.netlify.app"],
}
COMPETITORS = [
    {"name": "GCATS", "aliases": ["GCATS Power Solutions"], "domains": ["gcats.com"]},
    {"name": "FSG", "aliases": ["FSG Dallas"], "domains": ["fsg.com"]},
    {
        "name": "PowerBoy Electrical Services",
        "aliases": ["PowerBoy", "Power Boy"],
        "domains": ["powerboy.us"],
    },
]


class MentionTests(unittest.TestCase):
    def test_brand_plain_and_possessive(self):
        text = "WireReady's intake form is public."
        self.assertEqual(matched_names(text, ["WireReady"]), ["WireReady"])

    def test_alias_with_space_and_hyphen(self):
        self.assertEqual(matched_names("Try Wire Ready today.", ["Wire Ready"]), ["Wire Ready"])
        self.assertEqual(matched_names("See Wire-Ready online.", ["Wire-Ready"]), ["Wire-Ready"])

    def test_no_false_positive_on_partial_words(self):
        text = "The crew is ready after the wire pull is wired correctly."
        self.assertEqual(matched_names(text, ["WireReady", "Wire Ready", "Wire-Ready"]), [])

    def test_short_competitor_token_uses_boundaries(self):
        self.assertTrue(matched_names("FSG Dallas does commercial work.", ["FSG", "FSG Dallas"]))
        self.assertEqual(matched_names("The fsgx tool is unrelated.", ["FSG"]), [])

    def test_gcats_match(self):
        self.assertEqual(matched_names("I would call GCATS first.", ["GCATS"]), ["GCATS"])


class CitationTests(unittest.TestCase):
    def test_extracts_and_strips_punctuation(self):
        text = "See https://wireready-pilot.netlify.app/contact."
        self.assertEqual(extract_urls(text), ["https://wireready-pilot.netlify.app/contact"])

    def test_brand_domain_match_ignores_www(self):
        text = "Source: https://www.gcats.com/data-centers"
        self.assertEqual(
            cited_urls_for_domains(text, ["gcats.com"]),
            ["https://www.gcats.com/data-centers"],
        )

    def test_unrelated_url_is_recorded_but_not_a_brand_citation(self):
        text = "Also see https://example.com/guide"
        self.assertEqual(extract_urls(text), ["https://example.com/guide"])
        self.assertEqual(cited_urls_for_domains(text, ["wireready-pilot.netlify.app"]), [])


class AnalyzeAndSummaryTests(unittest.TestCase):
    def test_analyze_answer_flags_brand_and_competitor(self):
        text = (
            "Ask WireReady (https://wireready-pilot.netlify.app) or compare with "
            "GCATS at https://www.gcats.com/."
        )
        result = analyze_answer(text, BRAND, COMPETITORS)
        self.assertTrue(result["brand_mentioned"])
        self.assertEqual(result["brand_cited_urls"], ["https://wireready-pilot.netlify.app"])
        gcats = next(item for item in result["competitors"] if item["name"] == "GCATS")
        self.assertTrue(gcats["mentioned"])
        self.assertTrue(gcats["cited_urls"])
        fsg = next(item for item in result["competitors"] if item["name"] == "FSG")
        self.assertFalse(fsg["mentioned"])

    def test_empty_answer(self):
        result = analyze_answer("", BRAND, COMPETITORS)
        self.assertFalse(result["brand_mentioned"])
        self.assertEqual(result["urls"], [])
        self.assertTrue(all(not item["mentioned"] for item in result["competitors"]))

    def test_summarize_run_rates(self):
        rows = [
            {
                "brand_mentioned": True,
                "brand_cited_urls": ["https://wireready-pilot.netlify.app"],
                "competitors": [
                    {"name": "GCATS", "mentioned": True, "cited_urls": ["https://www.gcats.com/"]},
                    {"name": "FSG", "mentioned": False, "cited_urls": []},
                ],
            },
            {
                "brand_mentioned": False,
                "brand_cited_urls": [],
                "competitors": [
                    {"name": "GCATS", "mentioned": False, "cited_urls": []},
                    {"name": "FSG", "mentioned": True, "cited_urls": []},
                ],
            },
        ]
        summary = summarize_run(rows, COMPETITORS)
        self.assertEqual(summary["questions"], 2)
        self.assertEqual(summary["brand_mention_count"], 1)
        self.assertEqual(summary["brand_mention_rate"], 0.5)
        self.assertEqual(summary["brand_citation_count"], 1)
        self.assertEqual(summary["competitor_mention_counts"]["GCATS"], 1)
        self.assertEqual(summary["competitor_mention_counts"]["FSG"], 1)
        self.assertEqual(summary["competitor_citation_counts"]["GCATS"], 1)
        self.assertEqual(summary["competitor_citation_counts"]["FSG"], 0)

    def test_config_file_is_valid_and_has_ten_questions(self):
        path = Path(__file__).resolve().parent / "config.wireready.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["brand"]["name"], "WireReady")
        self.assertEqual(len(data["questions"]), 10)
        self.assertGreaterEqual(len(data["competitors"]), 3)
        ids = [item["id"] for item in data["questions"]]
        self.assertEqual(len(ids), len(set(ids)))


class CsvShapeTests(unittest.TestCase):
    def test_flatten_helper_columns(self):
        from measure import flatten_row

        row = {
            "question_id": "Q01",
            "category": "discovery",
            "question": "Who?",
            "ok": True,
            "http_status": 200,
            "latency_s": 1.2,
            "returned_model": "mistral-Nemo-Instruct-2407",
            "brand_mentioned": True,
            "brand_matched_names": ["WireReady"],
            "brand_cited_urls": [],
            "competitors": [
                {"name": "GCATS", "mentioned": True, "cited_urls": ["https://www.gcats.com/"]}
            ],
            "urls": ["https://www.gcats.com/"],
            "error": None,
            "answer": "GCATS and maybe others.",
        }
        flat = flatten_row(row)
        self.assertEqual(flat["competitors_mentioned"], "GCATS")
        self.assertIn("question_id", flat)
        self.assertIn("answer", flat)


if __name__ == "__main__":
    unittest.main()
