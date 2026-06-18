import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


class ScriptTests(unittest.TestCase):
    def test_build_report_outline_prints_research_markdown(self):
        script = ROOT / "scripts" / "build_report_outline.py"

        result = subprocess.run(
            [
                PYTHON,
                str(script),
                "--company",
                "Sample Dairy Co",
                "--ticker",
                "1234.HK",
                "--industry",
                "Consumer Staples",
                "--region",
                "Hong Kong",
                "--report-type",
                "initiation",
            ],
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("# Sample Dairy Co (1234.HK) Equity Research Outline", result.stdout)
        self.assertIn("## Company And Business Overview", result.stdout)
        self.assertIn("## Valuation Framework", result.stdout)
        self.assertIn("DCF", result.stdout)
        self.assertIn("Not investment advice", result.stdout)
        self.assertNotIn("\n        ##", result.stdout)
        self.assertNotIn("\n        -", result.stdout)

    def test_quick_validate_inputs_accepts_complete_json(self):
        script = ROOT / "scripts" / "quick_validate_inputs.py"
        payload = {
            "company": "Sample Dairy Co",
            "ticker": "1234.HK",
            "region": "Hong Kong",
            "industry": "Consumer Staples",
            "currency": "HKD",
            "financials": [{"year": 2025, "revenue": 1000}],
            "share_count": 500,
            "sources": ["annual report"],
        }

        with tempfile.TemporaryDirectory() as tmp:
            input_path = Path(tmp) / "complete.json"
            input_path.write_text(json.dumps(payload), encoding="utf-8")

            result = subprocess.run(
                [PYTHON, str(script), str(input_path)],
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("usable", result.stdout.lower())
        self.assertIn("optional", result.stdout.lower())

    def test_quick_validate_inputs_rejects_missing_required_fields(self):
        script = ROOT / "scripts" / "quick_validate_inputs.py"
        payload = {
            "company": "Sample Dairy Co",
            "ticker": "1234.HK",
            "sources": ["annual report"],
        }

        with tempfile.TemporaryDirectory() as tmp:
            input_path = Path(tmp) / "incomplete.json"
            input_path.write_text(json.dumps(payload), encoding="utf-8")

            result = subprocess.run(
                [PYTHON, str(script), str(input_path)],
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("missing critical fields", result.stdout.lower())
        self.assertIn("industry", result.stdout)
        self.assertIn("financials", result.stdout)


if __name__ == "__main__":
    unittest.main()
