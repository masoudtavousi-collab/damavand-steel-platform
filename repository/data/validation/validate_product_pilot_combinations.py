#!/usr/bin/env python3
"""Validate synthetic PD-03 pilot-combination fixtures offline."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

from validate_pd03a_pilot_prerequisite import (
    BASE_PATHS,
    REGISTRY_PATH as FOUNDATION_REGISTRY_PATH,
    ROOT,
    ValidationConfigurationError,
    collect_ids,
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
    ("pcomb:17b1e8554038", "PIPE-COMB-0001", "201", "silver", "16", "0.35", "6"),
    ("pcomb:0a1b2c3d4e5f", "PIPE-COMB-0016", "201", "silver", "38", "0.50", "6"),
    ("pcomb:1a2b3c4d5e6f", "PIPE-COMB-0023", "201", "silver", "51", "0.50", "6"),
}
PROHIBITED_FIELDS = {
    "product_id", "sku", "commercial_sku", "slug", "stock", "inventory",
    "availability_value", "supply_status", "price", "pricing", "offer",
    "wordpress_id", "woocommerce_id", "import", "publication", "deployment",
    "production", "golden_ready_value",
}
EXPECTED_CONTRACT = {
    "contract_id": "product-pilot-combination",
    "contract_version": "1.0.0",
    "record_kind": "synthetic-pilot-combination-test-bundle",
    "schema": {
        "path": "repository/data/schemas/product-pilot-combination.schema.json",
        "draft": "https://json-schema.org/draft/2020-12/schema",
    },
    "authority": {
        "decision_id": "FD-PD03A-001", "canonical_population_authority": False,
        "fixtures_only": True, "allowed_data_classification": "SYNTHETIC_FIXTURE",
        "allowed_status": "CANDIDATE_UNVERIFIED",
    },
    "exact_test_model": {
        "combination_count": 3,
        "axes": ["grade", "finish", "diameter", "thickness", "length"],
        "fixed_non_axis": {"material": "stainless_steel"},
        "tuple_lexemes": [
            ["201", "silver", "16", "0.35", "6"],
            ["201", "silver", "38", "0.50", "6"],
            ["201", "silver", "51", "0.50", "6"],
        ],
        "units": {
            "diameter": "unit:000000000002", "thickness": "unit:000000000002",
            "length": "unit:000000000001",
        },
        "availability_status": "MISSING_DATA_VALUE",
        "cartesian_generation_forbidden": True,
        "historical_references_are_non_identity": True,
        "cross_file_reference_resolution_required": True,
    },
    "readiness": {"import_ready": False, "runtime_ready": False, "golden_ready": False},
    "prohibited_fields": [
        "product_id", "sku", "commercial_sku", "slug", "stock", "inventory",
        "availability_value", "supply_status", "price", "offer", "wordpress_id",
        "woocommerce_id", "import", "publication", "deployment", "production",
    ],
    "validation": {
        "network_allowed": False, "side_effects_allowed": False,
        "duplicate_json_or_yaml_keys_rejected": True,
        "non_finite_numbers_rejected": True, "remote_schema_references_rejected": True,
        "exact_contract_validation_required": True,
    },
}


def load_validator(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[Draft202012Validator, dict[str, Any]]:
    contract = require_mapping(load_yaml(contract_path), "pilot-combination contract")
    if contract != EXPECTED_CONTRACT:
        raise ValidationConfigurationError("pilot-combination contract differs from exact fail-closed policy")
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
    expected_top_level = {
        "contract_version": "1.0.0",
        "fixture_id": "ptest:dfa2ea0b6c2e",
        "data_classification": "SYNTHETIC_FIXTURE",
        "series_entity_id": "prd:series:e1657d35ac35",
        "variant_rule_set_entity_id": "prd:variant-rule-set:eb255662accc",
        "profile_id": "pprof:4c556c63c1a9",
        "fixed_material_term_id": "vterm:5ff9c0ceca39",
        "cartesian_generation_forbidden": True,
    }
    for key, expected in expected_top_level.items():
        if value.get(key) != expected:
            add("EXACT_FIXTURE_REFERENCE", f"exact synthetic fixture field differs: {key}")
    available_ids: set[str] = set()
    available_ids.update(collect_ids(load_yaml(FOUNDATION_REGISTRY_PATH)))
    for path in BASE_PATHS:
        available_ids.update(collect_ids(load_yaml(path)))
    referenced_ids = {
        value.get("series_entity_id"), value.get("variant_rule_set_entity_id"),
        value.get("profile_id"), value.get("fixed_material_term_id"),
    }
    if not all(isinstance(item, str) and item in available_ids for item in referenced_ids):
        add("CROSS_FILE_REFERENCE", "Series, rule-set, Profile, and Material IDs must resolve across exact base/extension files")
    if value.get("axes") != EXPECTED_AXES:
        add("AXIS_ORDER", "exact five-axis order is required")
    combinations = value.get("combinations", [])
    actual: set[tuple[str, str, str, str, str, str, str]] = set()
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
            str(item.get("combination_id")),
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
    if value.get("provenance") != {
        "source_type": "SYNTHETIC_FIXTURE",
        "source_reference": "tests/fixtures/pd03a/valid-synthetic-pilot-combinations.yaml",
        "captured_by": "role:codex-build-engine",
        "captured_at": "2026-08-01T00:00:00Z",
        "evidence_status": "SYNTHETIC_TEST_EVIDENCE",
    }:
        add("FIXTURE_PROVENANCE", "exact synthetic provenance is required")
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
