"""Repeat acceptance and regression checks for the two deliverable commands."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from zipfile import ZipFile

from pptx import Presentation
from pptx.util import Inches


WORK = Path(__file__).resolve().parent


class DeliverableChecks(unittest.TestCase):
    def run_check(self, command, *args):
        result = subprocess.run(
            [sys.executable, str(WORK / command), *map(str, args)],
            capture_output=True,
            text=True,
        )
        return result.returncode, result.stdout + result.stderr

    def test_performance_profiles_and_regression(self):
        report = {
            "requestedUrl": "https://example.test/",
            "finalDisplayedUrl": "https://example.test/",
            "lighthouseVersion": "13.6.0",
            "configSettings": {
                "formFactor": "mobile", "throttlingMethod": "simulate",
                "throttling": {}, "screenEmulation": {},
            },
            "audits": {
                "largest-contentful-paint": {"numericValue": 900, "numericUnit": "millisecond"},
                "cumulative-layout-shift": {"numericValue": 0.05, "numericUnit": "unitless"},
                "total-blocking-time": {"numericValue": 80, "numericUnit": "millisecond"},
            },
        }
        with TemporaryDirectory() as folder:
            baseline = Path(folder) / "baseline.json"
            baseline.write_text(json.dumps(report))
            candidate = Path(folder) / "candidate.json"
            cases = (
                ("same", 0, ()),
                ("regression", 1, ()),
                ("regression", 0, ("--allow-time-ms", "100")),
                ("redirect", 2, ()),
                ("missing", 2, ()),
                ("different profile", 2, ()),
            )
            for case, expected, flags in cases:
                current = deepcopy(report)
                if case == "regression":
                    current["audits"]["largest-contentful-paint"]["numericValue"] = 1000
                if case == "redirect":
                    current["finalDisplayedUrl"] = "https://example.test/login"
                if case == "missing":
                    del current["audits"]["total-blocking-time"]
                if case == "different profile":
                    current["configSettings"]["formFactor"] = "desktop"
                candidate.write_text(json.dumps(current))
                self.assertEqual(self.run_check("check_performance.py", baseline, candidate, *flags)[0], expected, case)

    def test_presentation_count_native_text_and_damaged_xml(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            deck = Presentation()
            slide = deck.slides.add_slide(deck.slide_layouts[6])
            blank = root / "blank.pptx"
            deck.save(blank)
            slide.shapes.add_textbox(Inches(1), Inches(1), Inches(3), Inches(1)).text = "Editable"
            editable = root / "editable.pptx"
            deck.save(editable)
            corrupt = root / "corrupt.pptx"
            with ZipFile(editable) as source, ZipFile(corrupt, "w") as target:
                for item in source.infolist():
                    payload = b"<broken" if item.filename == "ppt/slides/slide1.xml" else source.read(item)
                    target.writestr(item, payload)
            for path, count, expected in ((editable, 1, 0), (editable, 2, 1), (blank, 1, 1), (corrupt, 1, 2)):
                code, output = self.run_check("check_presentation.py", path, "--slides", count)
                self.assertEqual(code, expected, output)
                self.assertNotIn("Traceback", output)


if __name__ == "__main__":
    unittest.main()
