"""Validate a JSON input package for an equity research workflow."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "company",
    "ticker",
    "region",
    "industry",
    "currency",
    "financials",
    "share_count",
    "sources",
]

OPTIONAL_FIELDS = [
    "market_cap",
    "net_debt",
    "peer_set",
    "management_guidance",
    "transcripts",
    "segment_data",
    "valuation_assumptions",
]


def has_value(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def validate_payload(payload: dict[str, Any]) -> tuple[list[str], list[str]]:
    missing_required = [field for field in REQUIRED_FIELDS if not has_value(payload.get(field))]
    missing_optional = [field for field in OPTIONAL_FIELDS if not has_value(payload.get(field))]
    return missing_required, missing_optional


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate equity research JSON inputs.")
    parser.add_argument("input_json", help="Path to a JSON file with company research inputs")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("Input JSON must contain an object at the top level.")
    return payload


def main() -> int:
    args = parse_args()
    path = Path(args.input_json)

    try:
        payload = load_json(path)
    except FileNotFoundError:
        print(f"Missing file: {path}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}")
        return 1
    except ValueError as exc:
        print(str(exc))
        return 1

    missing_required, missing_optional = validate_payload(payload)

    if missing_required:
        print("Input is not usable: missing critical fields.")
        for field in missing_required:
            print(f"- {field}")
        if missing_optional:
            print("\nOptional fields that would improve the workflow:")
            for field in missing_optional:
                print(f"- {field}")
        return 1

    print("Input is usable for a first-pass equity research workflow.")
    if missing_optional:
        print("Optional fields that would improve the workflow:")
        for field in missing_optional:
            print(f"- {field}")
    else:
        print("Optional fields are complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
