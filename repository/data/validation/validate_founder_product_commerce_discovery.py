#!/usr/bin/env python3
"""Validate the bounded C003 Founder Discovery evidence package offline."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any

from validate_pd03a_pilot_prerequisite import (
    ROOT,
    ValidationConfigurationError,
    load_json,
    load_yaml,
    require_mapping,
    validate_schema,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/founder-product-commerce-discovery.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/founder-product-commerce-discovery.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c003/founder-product-commerce-discovery-session-01.yaml"
C002_CANDIDATE_PATH = ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
C002_ADMIN_PATH = ROOT / "repository/data/registries/extensions/c002/product-administration-policies.yaml"
C002_ADMIN_CONTRACT_PATH = ROOT / "repository/data/contracts/product-administration-policy.contract.yaml"
PRODUCT_ENTITIES_PATH = ROOT / "repository/data/registries/product-entities.yaml"
PD03A_PATH = ROOT / "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml"
PD03B_PATH = ROOT / "repository/data/registries/extensions/pd03b/canonical-pilots.yaml"

# Updated only when the versioned C003 contract is intentionally revised.
EXPECTED_CONTRACT_DIGEST = "b5b54fa515fac492494f3a95ceccb62f7d5bfa3dcf58a27e95a026a1216c28a2"
EXPECTED_REGISTRY_DIGEST = "c99a80ea52def8146c48410dab667843162a7aabab58b143b160bd41119e4888"
EXPECTED_C002_MASS_METHODS = ["MANUFACTURER_STATED", "MEASURED", "CALCULATED"]
EXPECTED_AVAILABILITY_ORDER_RECORDS = {61, 77, 79, 80, 81, 82, 83, 84, 85, 86}
EXPECTED_DEAL_POLICY_RECORDS = {88, 90}

EXPECTED_MISSION_SOURCES = [
    ("MISSION_PARENT", "1786969720.051019", 1, "MISSION_PARENT", True),
    ("MISSION_BOUNDARY", "1786969736.626679", 2, "MISSION_BOUNDARY", True),
    ("MISSION_STOP_REPORT", "1786969749.649289", 3, "MISSION_STOP_REPORT", True),
]
EXPECTED_DISCOVERY_SOURCES = [
    ("DISCOVERY_PARENT", "1786929259.157699", 1, "DISCOVERY_PARENT", True),
    ("PART_01", "1786929271.724929", 2, "PART_01", True),
    ("PART_02", "1786929285.156489", 3, "PART_02", True),
    ("PART_03", "1786929298.131999", 4, "PART_03", True),
    ("PART_04", "1786929308.929669", 5, "PART_04", True),
    ("PART_05", "1786929322.167819", 6, "PART_05", True),
    ("PART_06", "1786929332.918159", 7, "PART_06_CORROBORATION", False),
    ("PART_07", "1786961959.781219", 8, "PART_07", True),
    ("CHECKPOINT_02", "1786969560.307449", 9, "CHECKPOINT_02", True),
]

EXPECTED_CLASSIFICATION_COUNTS = {
    "FOUNDER_CONFIRMED": 70,
    "FOUNDER_ACCEPTED_CANDIDATE": 3,
    "ARCHITECTURE_PROPOSAL": 42,
}
EXPECTED_TEMPORAL_COUNTS = {
    "CURRENT_INTENT": 86,
    "HISTORICAL_EXAMPLE_NONCURRENT": 4,
    "FUTURE_CONCEPT": 25,
}
LEDGER_MAPPING = {
    "FC": ("FOUNDER_CONFIRMED", "CURRENT_INTENT"),
    "FAC": ("FOUNDER_ACCEPTED_CANDIDATE", "CURRENT_INTENT"),
    "AP": ("ARCHITECTURE_PROPOSAL", "CURRENT_INTENT"),
    "HE": ("FOUNDER_CONFIRMED", "HISTORICAL_EXAMPLE_NONCURRENT"),
    "FUT": ("ARCHITECTURE_PROPOSAL", "FUTURE_CONCEPT"),
    "FCF": ("FOUNDER_CONFIRMED", "FUTURE_CONCEPT"),
    "FACF": ("FOUNDER_ACCEPTED_CANDIDATE", "FUTURE_CONCEPT"),
}
REQUIRED_TOPICS = {
    "PRODUCT_GROUP", "VALID_COMBINATIONS", "CONTENT_INHERITANCE", "PRODUCT_ADMIN",
    "BRAND_SOURCE", "DIMENSIONS_GRADE", "APPEARANCE", "CUTTING_LENGTH",
    "MASS_PROVENANCE", "SMART_HISTORY", "PRICING_FX", "MARKETPLACE_DEALS",
    "CUSTOMER_CONTEXT", "FULFILLMENT", "AVAILABILITY_RESERVATION",
    "PAYMENT_DOCUMENTS", "CRM_IDENTITY", "LOYALTY_REFERRAL", "RETURNS_DAMAGE",
    "RBAC_TAX",
}
PROTECTED_PRICE_DIGESTS = {
    "a603a710592d8752fdad886dc905dcae85d0c3d5ee5f001c623ebe332b4cf030",
    "9437e07b40d98d95f90b65522b3b1f34a0c6ca51818d918f135e94894391a5e4",
}


def _semantic_digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def _contains_protected_price_value(value: str) -> bool:
    normalized = value.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789"))
    candidates = re.findall(r"(?<!\d)(?:\d[\s,._-]*){5}\d(?!\d)", normalized)
    for candidate in candidates:
        digits = re.sub(r"\D", "", candidate)
        if hashlib.sha256(digits.encode()).hexdigest() in PROTECTED_PRICE_DIGESTS:
            return True
    return False


def safe_path(path: Path, label: str) -> Path:
    try:
        if path.is_symlink():
            raise ValidationConfigurationError(f"{label} must not be a symbolic link")
        resolved = path.resolve(strict=True)
    except FileNotFoundError as exc:
        raise ValidationConfigurationError(f"missing {label}: {path}") from exc
    if resolved != ROOT and ROOT not in resolved.parents:
        raise ValidationConfigurationError(f"{label} must remain inside the repository")
    return resolved


def load_validator(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[Any, dict[str, Any]]:
    contract = require_mapping(load_yaml(safe_path(contract_path, "C003 discovery contract")), "C003 discovery contract")
    digest = _semantic_digest(contract)
    if EXPECTED_CONTRACT_DIGEST != "TO_BE_FINALIZED" and digest != EXPECTED_CONTRACT_DIGEST:
        raise ValidationConfigurationError("C003 discovery contract literal policy differs")
    schema = require_mapping(load_json(safe_path(schema_path, "C003 discovery schema")), "C003 discovery schema")
    return validate_schema(schema), contract


def _render_sources(items: Any) -> list[tuple[Any, Any, Any, Any, Any]]:
    if not isinstance(items, list):
        return []
    return [
        (
            item.get("source_id"), item.get("timestamp"), item.get("source_order"),
            item.get("source_role"), item.get("contributes_new_records"),
        )
        for item in items if isinstance(item, dict)
    ]


def _source_order_for(sequence: int, ranges: list[dict[str, Any]]) -> int | None:
    for source_order, item in enumerate(ranges, start=1):
        first = item.get("first_record")
        last = item.get("last_record")
        if isinstance(first, int) and isinstance(last, int) and first <= sequence <= last:
            return source_order
    return None


def _validate_live_regression_anchors(add: Any) -> None:
    candidates = require_mapping(load_yaml(C002_CANDIDATE_PATH), "C002 candidate registry")
    admin = require_mapping(load_yaml(C002_ADMIN_PATH), "C002 administration registry")
    admin_contract = require_mapping(load_yaml(C002_ADMIN_CONTRACT_PATH), "C002 administration contract")
    pd03b = require_mapping(load_yaml(PD03B_PATH), "PD03B registry")
    pd03a = require_mapping(load_yaml(PD03A_PATH), "PD03A extension")
    base_entities = load_yaml(PRODUCT_ENTITIES_PATH)

    if candidates.get("candidates") != []:
        add("REGRESSION_C002_CANDIDATES", "C002 candidate registry must remain empty")
    if not isinstance(admin.get("policies"), list) or len(admin["policies"]) != 8:
        add("REGRESSION_C002_POLICIES", "C002 must retain exactly eight policy definitions")
    if admin.get("instances") != []:
        add("REGRESSION_C002_INSTANCES", "C002 policy-instance registry must remain empty")
    methods = admin_contract.get("invariants", {}).get("mass_provenance", {}).get("methods")
    if methods != EXPECTED_C002_MASS_METHODS:
        add("SUPPLIER_STATED_PROMOTION", "SUPPLIER_STATED must not be added to the approved C002 method enum by C003")
    pilots = pd03b.get("pilots", [])
    if not isinstance(pilots, list) or len(pilots) != 3:
        add("REGRESSION_PD03B_COUNT", "PD03B must retain exactly three seed/reference Pilot records")
    elif any(item.get("availability_status") != "MISSING_DATA_VALUE" for item in pilots if isinstance(item, dict)):
        add("REGRESSION_PD03B_AVAILABILITY", "all PD03B Availability must remain MISSING_DATA_VALUE")
    entities = list(base_entities) if isinstance(base_entities, list) else []
    entities.extend(pd03a.get("entities", []) if isinstance(pd03a.get("entities"), list) else [])
    if any(isinstance(item, dict) and item.get("entity_type") == "SKU" for item in entities):
        add("REGRESSION_SKU_POPULATION", "C003 cannot populate canonical SKU entities")


def validate_registry(value: Any, validator: Any, contract: dict[str, Any]) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    for error in validator.iter_errors(value):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add("SCHEMA_VALIDATION", f"{location}: {error.message}")
    if not isinstance(value, dict):
        return sorted(set(issues))

    if value.get("data_classification") != "C003_FOUNDER_DISCOVERY_EVIDENCE":
        add("DATA_CLASSIFICATION", "canonical C003 registry must remain Founder Discovery evidence")
    if EXPECTED_REGISTRY_DIGEST != "TO_BE_FINALIZED" and _semantic_digest(value) != EXPECTED_REGISTRY_DIGEST:
        add("REGISTRY_DIGEST", "C003 canonical discovery evidence differs from the independently reviewed package")

    if _render_sources(value.get("mission_sources")) != EXPECTED_MISSION_SOURCES:
        add("MISSION_SOURCE_MANIFEST", "Mission source manifest must be exact and complete (3/3)")
    if _render_sources(value.get("discovery_sources")) != EXPECTED_DISCOVERY_SOURCES:
        add("DISCOVERY_SOURCE_MANIFEST", "Discovery source manifest must be exact and complete (9/9)")
    if value.get("source_complete") is not True:
        add("SOURCE_COMPLETENESS", "source_complete must be true")

    model = require_mapping(contract.get("evidence_model"), "evidence model")
    expected_ledger = model.get("exact_ledger_class_order", [])
    source_ranges = model.get("source_ranges", [])
    records = value.get("evidence_records", [])
    if not isinstance(records, list):
        records = []
    if len(records) != 115:
        add("EXACT_RECORD_COUNT", "C003 requires exactly 115 source-order evidence records")

    ids: list[Any] = []
    codes: list[Any] = []
    ledger_classes: list[Any] = []
    classifications: Counter[Any] = Counter()
    temporal_roles: Counter[Any] = Counter()
    topics: set[Any] = set()
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            continue
        ids.append(record.get("evidence_id"))
        codes.append(record.get("decision_code"))
        ledger_class = record.get("ledger_class")
        ledger_classes.append(ledger_class)
        classifications[record.get("evidence_classification")] += 1
        temporal_roles[record.get("temporal_role")] += 1
        topics.add(record.get("topic_code"))
        if record.get("sequence") != index:
            add("SOURCE_SEQUENCE", f"record {index} sequence must equal source order")
        if record.get("evidence_id") != f"fdisc:{index:012x}":
            add("EVIDENCE_ID", f"record {index} stable evidence ID differs")
        if record.get("decision_code") != f"C003-DISC-{index:03d}":
            add("DECISION_CODE", f"record {index} decision code differs")
        expected_source_order = _source_order_for(index, source_ranges)
        if record.get("source_order") != expected_source_order:
            add("RECORD_SOURCE_BINDING", f"record {index} source_order differs")
        expected_pair = LEDGER_MAPPING.get(ledger_class)
        actual_pair = (record.get("evidence_classification"), record.get("temporal_role"))
        if expected_pair != actual_pair:
            add("LEDGER_CLASS_BINDING", f"record {index} class/temporal mapping differs")
        effects = record.get("authority_effects")
        if not isinstance(effects, dict) or not effects or any(item is not False for item in effects.values()):
            add("AUTHORITY_EFFECT", f"record {index} must have only explicit false authority effects")
        if record.get("source_scope") != "COMPLETE_DISCOVERY_THREAD":
            add("SOURCE_SCOPE", f"record {index} must bind the complete Discovery thread")
        if index in EXPECTED_AVAILABILITY_ORDER_RECORDS and record.get("canonical_owner") != "DISCOVERY_BACKLOG_ONLY":
            add("AVAILABILITY_ORDER_OWNER", f"record {index} belongs to future Availability/Order backlog, not C002 eligibility")
        if index in EXPECTED_DEAL_POLICY_RECORDS and record.get("canonical_owner") != "DISCOVERY_BACKLOG_ONLY":
            add("DEAL_POLICY_OWNER", f"record {index} belongs to a future Deals policy, not C002 Inventory Harmony")
        if index == 89 and record.get("canonical_owner") != "C002_INVENTORY_HARMONY":
            add("INVENTORY_HARMONY_OWNER", "record 089 is evidence for the existing C002 Inventory Harmony owner")
        if index == 72:
            if record.get("canonical_owner") != "C002_COMMERCE_ELIGIBILITY":
                add("ELIGIBILITY_OWNER", "record 072 must reconcile through the existing C002 eligibility owner")
            statement = str(record.get("statement"))
            if "per canonical SKU" not in statement or "inheritance is prohibited" not in statement:
                add("ELIGIBILITY_NO_INHERITANCE", "record 072 must preserve per-SKU eligibility and prohibit Product-class inheritance")
        if index == 35:
            expected = {
                "proposed_extension_state": "PROPOSED_EXTENSION_REQUIRING_SEPARATE_REVIEW",
                "requires_separate_contract_version": True,
                "requires_separate_promotion_authority": True,
            }
            if any(record.get(key) != expected_value for key, expected_value in expected.items()):
                add("SUPPLIER_STATED_BOUNDARY", "record 035 must remain a non-promoted proposal requiring separate review")
            if record.get("canonical_owner") != "C002_MASS_PROVENANCE":
                add("SUPPLIER_STATED_OWNER", "record 035 must route to the existing C002 Mass owner")
        elif any(key in record for key in (
            "proposed_extension_state", "requires_separate_contract_version", "requires_separate_promotion_authority",
        )):
            add("PROPOSED_EXTENSION_SCOPE", f"proposal-extension fields are exclusive to record 035, found at {index}")
        if index == 39:
            if record.get("protected_source_locator") != "slack:C0BNHRRTE9F:1786929285.156489:record:039":
                add("PROTECTED_PRICE_LOCATOR", "record 039 requires the exact protected Slack locator")
        elif record.get("protected_source_locator") is not None:
            add("PROTECTED_LOCATOR_SCOPE", f"protected locator is exclusive to record 039, found at {index}")

    if ids and len(ids) != len(set(ids)):
        add("DUPLICATE_EVIDENCE_ID", "evidence IDs must be unique")
    if codes and len(codes) != len(set(codes)):
        add("DUPLICATE_DECISION_CODE", "decision codes must be unique")
    if ledger_classes != expected_ledger:
        add("EXACT_LEDGER_ORDER", "ledger classes must match the exact 115-record source order")
    if dict(classifications) != EXPECTED_CLASSIFICATION_COUNTS:
        add("CLASSIFICATION_COUNTS", f"classification counts differ: {dict(classifications)}")
    if dict(temporal_roles) != EXPECTED_TEMPORAL_COUNTS:
        add("TEMPORAL_COUNTS", f"temporal-role counts differ: {dict(temporal_roles)}")
    if topics != REQUIRED_TOPICS:
        add("TOPIC_COVERAGE", f"exact Mission topic coverage differs: {sorted(topics)}")
    summary = value.get("evidence_summary")
    if isinstance(summary, dict):
        if summary.get("record_count") != len(records):
            add("SUMMARY_RECORD_COUNT", "summary record_count must be derived from evidence_records")
        if summary.get("classification_counts") != EXPECTED_CLASSIFICATION_COUNTS:
            add("SUMMARY_CLASSIFICATION", "summary classification counts differ")
        if summary.get("temporal_role_counts") != EXPECTED_TEMPORAL_COUNTS:
            add("SUMMARY_TEMPORAL", "summary temporal-role counts differ")

    boundary = value.get("boundary")
    if not isinstance(boundary, dict) or not boundary or any(item is not False for item in boundary.values()):
        add("PACKAGE_AUTHORITY", "C003 package must grant no Product/commercial/runtime authority")
    normalized_text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    if _contains_protected_price_value(normalized_text):
        add("PROTECTED_PRICE_VALUE", "protected historical price values must not enter the public repository")

    try:
        _validate_live_regression_anchors(add)
    except (OSError, TypeError, ValueError, ValidationConfigurationError) as exc:
        add("REGRESSION_CONFIGURATION", str(exc))
    return sorted(set(issues))


def validate_file(path: Path = REGISTRY_PATH) -> list[str]:
    validator, contract = load_validator()
    return validate_registry(load_yaml(safe_path(path, "C003 discovery registry")), validator, contract)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    parser.add_argument("--synthetic", action="store_true")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        target = safe_path(Path(args.registry), "C003 registry input")
        if args.synthetic:
            control = require_mapping(load_yaml(target), "C003 synthetic control")
            expected_control = {
                "fixture_id": "c003-founder-discovery-valid-synthetic-control",
                "data_classification": "SYNTHETIC_FIXTURE",
                "subject_path": "repository/data/registries/extensions/c003/founder-product-commerce-discovery-session-01.yaml",
                "expected_record_count": 115,
                "expected_result": "PASS",
                "authority_effect": "NONE",
            }
            if control != expected_control:
                raise ValidationConfigurationError("C003 synthetic control manifest differs")
            target = ROOT / str(control["subject_path"])
        issues = validate_file(target)
    except (OSError, TypeError, ValueError, ValidationConfigurationError) as exc:
        print(f"C003_DISCOVERY_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    mode = "synthetic control" if args.synthetic else "canonical evidence"
    print(f"C003 Founder Discovery validation PASS: {mode}; 115 records; no Product/SKU/Availability/price/runtime authority.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
