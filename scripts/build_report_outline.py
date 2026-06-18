"""Generate a Markdown equity research outline from supplied metadata."""

from __future__ import annotations

import argparse


VALUATION_METHODS_BY_REPORT = {
    "initiation": ["DCF", "PE", "EV/EBITDA", "scenario analysis"],
    "earnings-preview": ["PE", "EV/EBITDA", "near-term scenario analysis"],
    "valuation-memo": ["DCF", "peer multiples", "sensitivity analysis"],
    "stock-pitch": ["primary intrinsic method", "peer multiples", "upside/downside scenario analysis"],
    "tear-sheet": ["PE", "EV/EBITDA", "quick peer cross-check"],
}


def normalize_report_type(report_type: str) -> str:
    return report_type.strip().lower().replace(" ", "-")


def select_methods(report_type: str) -> list[str]:
    normalized = normalize_report_type(report_type)
    return VALUATION_METHODS_BY_REPORT.get(
        normalized,
        ["DCF", "PE", "EV/EBITDA", "scenario analysis"],
    )


def build_outline(company: str, ticker: str, industry: str, region: str, report_type: str) -> str:
    methods = select_methods(report_type)
    lines = [
        f"# {company} ({ticker}) Equity Research Outline",
        "",
        f"**Report type:** {report_type}",
        f"**Industry:** {industry}",
        f"**Region:** {region}",
        "",
        "## Research Question",
        "",
        "Define the central question this report should answer. Examples: whether growth is sustainable, whether margins can recover, whether the current valuation reflects normalized earnings, or what catalysts matter over the next 6-12 months.",
        "",
        "## Company And Business Overview",
        "",
        "- Describe the business model, revenue streams, customer base, and segment mix.",
        "- Identify the most important products, geographies, and profit drivers.",
        "- Required evidence: annual report, segment disclosures, management commentary, and recent filings.",
        "- Suggested charts: revenue by segment, revenue by geography, and margin by segment.",
        "",
        "## Industry And Competitive Position",
        "",
        "- Summarize market size, growth, regulation, pricing, supply/demand, and competitive structure.",
        f"- Compare {company} with relevant listed peers.",
        "- Required evidence: industry reports, company filings, regulator data, and peer disclosures.",
        "- Suggested charts: peer growth and margin comparison, market share, and pricing/volume trend.",
        "",
        "## Financial Analysis",
        "",
        "- Analyze revenue growth, gross margin, operating margin, net margin, cash conversion, leverage, and capital intensity.",
        "- Separate recurring performance from one-off items.",
        "- Required evidence: historical income statement, balance sheet, cash flow statement, and notes.",
        "- Suggested charts: revenue growth, margin bridge, free cash flow conversion, and net debt/cash.",
        "",
        "## Valuation Framework",
        "",
        "Use these methods as a starting point:",
        "",
        *[f"- {method}" for method in methods],
        "",
        "For each method, state the reason it is suitable, the assumptions required, and the sensitivity that matters most. Use ranges and scenarios instead of false precision.",
        "",
        "## Catalysts And Monitoring Items",
        "",
        "- Earnings releases and guidance changes.",
        "- Pricing, volume, cost, or margin inflection points.",
        "- Regulatory, financing, product, or competitive developments.",
        "- Data points that would confirm or weaken the thesis.",
        "",
        "## Risks",
        "",
        "- Business model and execution risk.",
        "- Industry, macro, currency, and regulatory risk.",
        "- Balance sheet, liquidity, and refinancing risk.",
        "- Valuation risk and assumption sensitivity.",
        "- Data quality or source limitations.",
        "",
        "## Source Checklist",
        "",
        "- Primary filings and annual/interim reports.",
        "- Earnings transcripts or management presentations.",
        "- Historical financial model or extracted financial table.",
        "- Peer financials and valuation multiples.",
        "- Industry and macro data sources.",
        "",
        "## Disclaimer",
        "",
        "Not investment advice. This outline is for research workflow and educational purposes only. Verify all facts, market data, financial figures, and assumptions before relying on the output.",
    ]
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a Markdown equity research outline.")
    parser.add_argument("--company", required=True, help="Company name")
    parser.add_argument("--ticker", required=True, help="Ticker or identifier")
    parser.add_argument("--industry", required=True, help="Industry or sector")
    parser.add_argument("--region", required=True, help="Primary market or region")
    parser.add_argument("--report-type", required=True, help="Report type, such as initiation or valuation memo")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print(
        build_outline(
            company=args.company,
            ticker=args.ticker,
            industry=args.industry,
            region=args.region,
            report_type=args.report_type,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
