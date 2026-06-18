# Equity Research Assistant

A free Codex skill for drafting structured equity research workflows, report outlines, valuation plans, and analyst checklists from user-supplied company materials.

This project helps analysts, students, independent investors, and small research teams turn filings, financials, transcripts, and industry notes into editable Markdown research scaffolds.

## What It Does

- Builds equity research report outlines.
- Selects suitable valuation methods such as DCF, DDM, PE, PB, EV/EBITDA, EV/Sales, and sum-of-the-parts.
- Checks whether a JSON research input package has enough fields to begin.
- Adds source, verification, risk, and disclaimer discipline to investment-research style outputs.
- Keeps claims tied to user-supplied data, sources, or explicit assumptions.

## What It Does Not Do

- It does not provide investment advice.
- It does not fetch live market data.
- It does not include proprietary broker research or licensed datasets.
- It does not guarantee investment outcomes.
- It does not replace professional judgment, compliance review, or regulated financial advice.

## Install As A Codex Skill

Copy this folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\equity-research-assistant "$env:USERPROFILE\.codex\skills\equity-research-assistant"
```

Then ask Codex to use it:

```text
Use $equity-research-assistant to draft an initiation report outline for a consumer staples company using the files I provide.
```

## CLI Helpers

Generate a Markdown research outline:

```powershell
python .\scripts\build_report_outline.py --company "Sample Dairy Co" --ticker "1234.HK" --industry "Consumer Staples" --region "Hong Kong" --report-type "initiation"
```

Validate a JSON input package:

```powershell
python .\scripts\quick_validate_inputs.py .\examples\complete-input.json
```

## Example Input

See:

- `examples/complete-input.json`
- `examples/incomplete-input.json`

## Free And Pro Model

The free version includes the skill workflow, references, and starter scripts.

Potential paid extensions can include:

- Editable Word research report templates.
- Excel valuation model templates.
- PowerPoint stock pitch templates.
- Sector-specific research packs.
- Team workflow and review checklist packages.
- Custom templates for funds, finance classes, or research teams.

See `PRICING.md` for a suggested packaging model.

See `PAYMENT_SETUP.md` for owner-controlled payment setup steps.

## Verification

Run tests:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest discover -s .\tests -v
```

Validate the Codex skill:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
```

## Disclaimer

This project is for research workflow and educational purposes only. It is not investment advice, a recommendation, or a solicitation to buy or sell securities. Verify all company facts, market data, financial figures, valuation inputs, and peer comparisons against primary sources or licensed data providers before relying on any output.
