#!/usr/bin/env python3
"""Validate synthetic PD-03 pilot-combination fixtures offline."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

from validate_pd03a_pilot_prerequisite import (
    ROOT,
    ValidationConfigurationError,
    load_json,
    load_yaml,
    require_mapping,
    validate_schema,
    walk,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/product-pilot-combination.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/product-pilot-combination.schema.json"
DEFAULT_FIXTURE = ROOT / "tests/fixtures/pd03a/valid-synthetic-pilot-combinations.yaml"
EXPECTED_AXES = ["grade", "finish", "diameter", "thickness", "length"]
EXPECTED_TUPLES = {
    ("PIPE-COMB-0001", "201", "silver", "16", "0.35", "6"),
    ("PIPE-COMB-0016", "201", "silver", "38", "0.50", "6"),
    ("PIPE-COMB-0023", "201", "silver", "51", "0.50", "6"),
}
PROHIBITED_FIELDS = {
    "product_id", "sku", "commercial_sku", "slug", "stock", "inventory",
    "availability_value", "supply_status", "price", "pricing", "offer",
    "wordpress_id", "woocommerce_id", "import", "publication", "deployment",
    "production", "golden_ready_value",
}


def load_validator(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[Draft202012Validator, dict[str, Any]]:
    contract = require_mapping(load_yaml(contract_path), "pilot-combination contract")
    if (
        contract.get("contract_id") != "product-pilot-combination"
        or contract.get("contract_version") != "1.0.0"
        or contract.get("authority", {}).get("canonical_population_authority") is not False
        or contract.get("authority", {}).get("fixtures_only") is not True
    ):
        raise ValidationConfigurationError("pilot-combination contract authority differs")
    schema = require_mapping(load_json(schema_path), "pilot-combination schema")
    return validate_schema(schema), contract


def validate_fixture(value: Any, source: str, validator: Draft202012Validator) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"{source}: [{code}] {message}")

    for error in validator.iter_errors(value):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add("SCHEMA_VALIDATION", f"{location}: {error.message}")
    if not isinstance(value, dict):
        return sorted(issues)
    if value.get("axes") != EXPECTED_AXES:
        add("AXIS_ORDER", "exact five-axis order is required")
    combinations = value.get("combinations", [])
    actual: set[tuple[str, str, str, str, str, str]] = set()
    ids: set[str] = set()
    for item in combinations if isinstance(combinations, list) else []:
        if not isinstance(item, dict):
            continue
        combination_id = item.get("combination_id")
        if combination_id in ids:
            add("DUPLICATE_COMBINATION_ID", str(combination_id))
        if isinstance(combination_id, str):
            ids.add(combination_id)
        actual.add((
            str(item.get("historical_reference")),
            "201" if item.get("grade_term_id") == "vterm:a891bfdfdd6b" else "invalid",
            "silver" if item.get("finish_term_id") == "vterm:1df9a5493546" else "invalid",
            str(item.get("diameter", {}).get("decimal_lexeme")),
            str(item.get("thickness", {}).get("decimal_lexeme")),
            str(item.get("length", {}).get("decimal_lexeme")),
        ))
        if item.get("diameter", {}).get("unit_id") != "unit:000000000002":
            add("DIAMETER_UNIT", "Diameter requires millimetre")
        if item.get("thickness", {}).get("unit_id") != "unit:000000000002":
            add("THICKNESS_UNIT", "Thickness requires millimetre")
        if item.get("length", {}).get("unit_id") != "unit:000000000001":
            add("LENGTH_UNIT", "Length requires metre")
    if actual != EXPECTED_TUPLES:
        add("EXACT_SYNTHETIC_TUPLES", "exact three bounded synthetic tuples are required")
    for node in walk(value):
        if isinstance(node, dict):
            overlap = PROHIBITED_FIELDS.intersection(node)
            if overlap:
                add("PROHIBITED_FIELD", f"prohibited field(s): {sorted(overlap)}")
    readiness = value.get("readiness", {})
    if readiness != {"import_ready": False, "runtime_ready": False, "golden_ready": False}:
        add("READINESS", "all readiness flags must be false")
    return sorted(set(issues))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", default=str(DEFAULT_FIXTURE))
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        validator, _ = load_validator()
        value = load_yaml(Path(args.fixture))
        issues = validate_fixture(value, str(args.fixture), validator)
    except (ValidationConfigurationError, OSError, TypeError, ValueError) as exc:
        print(f"PD03A_PILOT_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print("PD-03 synthetic pilot-combination validation PASS: 3 tuples; readiness=false; no canonical, SKU, availability, import, or runtime authority.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
