---
name: equity-research-assistant
description: Build structured equity research, valuation, stock pitch, earnings preview, initiation report, and company tear sheet workflows from user-supplied company filings, financials, transcripts, market data, and industry notes. Use when Codex needs to produce research outlines, analyst checklists, valuation method selection, source-backed report drafts, chart plans, or investment-research style deliverables while avoiding unsupported recommendations.
---

# Equity Research Assistant

## Core Workflow

Use this skill to turn supplied company and market materials into structured equity research outputs. Keep every claim tied to provided evidence, a named source, or an explicit assumption.

1. Identify the output type: initiation report, earnings preview, valuation memo, stock pitch, company tear sheet, or update note.
2. Inventory supplied materials: filings, financials, transcripts, broker notes, industry data, model extracts, and source links.
3. Flag critical gaps before drafting when missing data would make the output misleading.
4. Read `references/report-structure.md` for section structure and evidence expectations.
5. Read `references/valuation-methods.md` before selecting valuation approaches.
6. Read `references/disclaimers.md` when the output resembles investment research, a stock pitch, or valuation conclusion.
7. Draft in Markdown unless the user asks for another format.

## Output Standards

- Separate facts, assumptions, and interpretation.
- Include a source checklist for every major section.
- Prefer ranges, scenarios, and sensitivity framing over single-point certainty.
- Describe what would change the conclusion.
- Include data limitations and verification needs.
- Do not claim real-time prices, consensus estimates, filings, ownership, or news unless the user supplied them or you verified them with a current source.
- Do not provide personalized financial advice or guaranteed return claims.

## Helper Scripts

Use `scripts/build_report_outline.py` to generate a first-pass Markdown outline:

```bash
python scripts/build_report_outline.py --company "Sample Co" --ticker "1234.HK" --industry "Consumer Staples" --region "Hong Kong" --report-type "initiation"
```

Use `scripts/quick_validate_inputs.py` to check whether a JSON input package has enough fields to start:

```bash
python scripts/quick_validate_inputs.py sample-input.json
```

## Missing Data Policy

Ask for more information only when a missing item blocks a credible output. For non-blocking gaps, proceed with a clearly labeled "Needs verification" list.

Critical fields for valuation-oriented work usually include company name, ticker, region, industry, currency, historical financials, share count, and source list.

## Commercial Boundary

This free skill provides workflow, scaffolding, and starter scripts. Do not imply that it includes proprietary data, live market feeds, complete valuation models, or regulated investment advice.
