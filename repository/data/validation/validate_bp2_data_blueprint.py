#!/usr/bin/env python3
"""Deterministic offline validation for the BP2 pipe data blueprint."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / "repository/data/contracts/bp2-pipe-data-blueprint-v0.1.json"
SCHEMA_PATH = ROOT / "repository/data/schemas/bp2-pipe-data-blueprint-v0.1.schema.json"

EXPECTED_HIERARCHY = [
    "CATALOG",
    "PLATFORM",
    "FAMILY",
    "SERIES",
    "VARIANT_RULE_SET",
    "SKU",
]
EXPECTED_GOVERNANCE_STATUSES = {
    "APPROVED",
    "CANDIDATE_UNVERIFIED",
    "MISSING_DATA_VALUE",
    "FOUNDER_INPUT_REQUIRED",
    "DEFERRED",
    "NOT_APPLICABLE",
    "INVALID",
}
EXPECTED_PILOTS = {
    (
        "PIPE-COMB-0001",
        "GOLD-PIPE-201-16-035-6M",
        "201",
        "SILVER",
        16,
        0.35,
        6,
    ),
    (
        "PIPE-COMB-0016",
        "GOLD-PIPE-201-38-050-6M",
        "201",
        "SILVER",
        38,
        0.5,
        6,
    ),
    (
        "PIPE-COMB-0023",
        "GOLD-PIPE-201-51-050-6M",
        "201",
        "SILVER",
        51,
        0.5,
        6,
    ),
}
EXPECTED_RULES = {(16, 0.35), (38, 0.5), (51, 0.5)}


def fail(code: str, message: str) -> None:
    print(f"[{code}] {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail("FILE_MISSING", str(path.relative_to(ROOT)))
    except json.JSONDecodeError as exc:
        fail("JSON_INVALID", f"{path.name}:{exc.lineno}:{exc.colno}: {exc.msg}")
    if not isinstance(value, dict):
        fail("ROOT_TYPE", f"{path.name} must contain an object")
    return value


def require(condition: bool, code: str, message: str) -> None:
    if not condition:
        fail(code, message)


def main() -> None:
    data = load_json(DATA_PATH)
    schema = load_json(SCHEMA_PATH)

    require(
        schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema",
        "SCHEMA_DRAFT",
        "schema must declare draft 2020-12",
    )
    require(schema.get("additionalProperties") is False, "SCHEMA_OPEN", "schema must be closed")
    require(data.get("blueprint_id") == "bp2-pipe-data-blueprint", "BLUEPRINT_ID", "unexpected blueprint_id")
    require(data.get("blueprint_version") == "0.1.0", "BLUEPRINT_VERSION", "unexpected blueprint version")
    require(data.get("hierarchy") == EXPECTED_HIERARCHY, "HIERARCHY", "canonical hierarchy differs")
    require(
        set(data.get("governance_statuses", [])) == EXPECTED_GOVERNANCE_STATUSES,
        "STATUS_VOCABULARY",
        "governance status vocabulary differs",
    )

    scope = data.get("scope", {})
    for key in (
        "creates_products",
        "creates_skus",
        "changes_wordpress",
        "allows_import",
        "allows_publication",
        "allows_deployment",
    ):
        require(scope.get(key) is False, "SCOPE_BOUNDARY", f"{key} must be false")

    admin = data.get("admin_actions", {})
    require(
        admin.get("registries") == ["ADD", "EDIT", "DELETE_OR_ARCHIVE"],
        "ADMIN_ACTIONS",
        "all registries must support add, edit, and delete/archive",
    )
    require(admin.get("default_delete_mode") == "SOFT_DELETE", "DELETE_MODE", "default deletion must be soft")
    require(admin.get("audit_required") is True, "DELETE_AUDIT", "audit must be required")
    require(admin.get("cascade_delete") is False, "CASCADE_DELETE", "cascade deletion must be forbidden")

    rules = {
        (item.get("diameter_mm"), item.get("thickness_mm"))
        for item in data.get("approved_diameter_thickness_rules", [])
        if isinstance(item, dict)
    }
    require(rules == EXPECTED_RULES, "APPROVED_RULES", "approved diameter/thickness rules differ")

    pilots = data.get("approved_pilot_combinations", [])
    require(len(pilots) == 3, "PILOT_COUNT", "exactly three pilot combinations are required")
    actual_pilots = set()
    for pilot in pilots:
        require(isinstance(pilot, dict), "PILOT_TYPE", "pilot entries must be objects")
        actual_pilots.add(
            (
                pilot.get("combination_id"),
                pilot.get("reference_code"),
                pilot.get("grade"),
                pilot.get("color"),
                pilot.get("diameter_mm"),
                pilot.get("thickness_mm"),
                pilot.get("length_m"),
            )
        )
        require(pilot.get("reference_is_final_sku") is False, "FINAL_SKU", "pilot reference cannot be a final SKU")
        require(pilot.get("status") == "APPROVED", "PILOT_STATUS", "pilot status must be APPROVED")
        require(
            pilot.get("supply_status") == "SUPPLY_AFTER_INQUIRY",
            "SUPPLY_STATUS",
            "approved pilots must use SUPPLY_AFTER_INQUIRY",
        )
    require(actual_pilots == EXPECTED_PILOTS, "PILOT_VALUES", "approved pilot combinations differ")

    matrix = data.get("historical_matrix", {})
    require(matrix.get("total_rows") == 882, "MATRIX_TOTAL", "historical total must be 882")
    require(matrix.get("approved_pilot_rows") == 3, "MATRIX_APPROVED", "approved pilot count must be 3")
    require(matrix.get("candidate_rows") == 879, "MATRIX_CANDIDATE", "candidate row count must be 879")
    require(matrix.get("cartesian_generation_forbidden") is True, "CARTESIAN", "Cartesian generation must be forbidden")

    inquiry = data.get("custom_inquiry", {})
    for key in ("auto_creates_master_data", "auto_creates_product", "auto_creates_variation"):
        require(inquiry.get(key) is False, "AUTO_CREATE", f"{key} must be false")

    print(
        "BP2 DATA BLUEPRINT VALIDATION PASSED: "
        "3 approved pilot decisions; 879 candidates; add/edit/delete governance; "
        "no Product, SKU, WordPress, import, publication, or deployment authority."
    )


if __name__ == "__main__":
    main()
