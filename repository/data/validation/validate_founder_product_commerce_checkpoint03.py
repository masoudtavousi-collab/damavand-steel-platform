#!/usr/bin/env python3
"""Offline validator for the bounded C003-R1 Checkpoint 03 evidence extension."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
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
from validate_founder_product_commerce_discovery import (
    CONTRACT_PATH as BASE_CONTRACT_PATH,
    REGISTRY_PATH as BASE_REGISTRY_PATH,
    load_validator as load_base_validator,
    validate_registry as validate_base_registry,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/founder-product-commerce-checkpoint03.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/founder-product-commerce-checkpoint03.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c003r1/checkpoint03-evidence-and-pilot-readiness.yaml"
C002_CANDIDATE_PATH = ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
C002_ADMIN_PATH = ROOT / "repository/data/registries/extensions/c002/product-administration-policies.yaml"
C002_ADMIN_CONTRACT_PATH = ROOT / "repository/data/contracts/product-administration-policy.contract.yaml"
PRODUCT_ENTITIES_PATH = ROOT / "repository/data/registries/product-entities.yaml"
PD03A_PATH = ROOT / "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml"
PD03B_PATH = ROOT / "repository/data/registries/extensions/pd03b/canonical-pilots.yaml"
CURRENT_STATE_PATH = ROOT / "docs/CURRENT_PROJECT_STATE.md"

# Pinned after independent review of the final semantic objects.
EXPECTED_CONTRACT_DIGEST = "2a3a5dca032ad2327e1f6ac491a7d1741d574310c889edad64bef85367e4557b"
EXPECTED_REGISTRY_DIGEST = "a6c4a3181db06c1292232a1a8f725a5e5be998a064075910a3da65e7a3d04a75"

LEDGER_MAPPING = {
    "FC": ("FOUNDER_CONFIRMED", "CURRENT_INTENT"),
    "FAC": ("FOUNDER_ACCEPTED_CANDIDATE", "CURRENT_INTENT"),
    "AP": ("ARCHITECTURE_PROPOSAL", "CURRENT_INTENT"),
    "HE": ("FOUNDER_CONFIRMED", "HISTORICAL_EXAMPLE_NONCURRENT"),
    "FUT": ("ARCHITECTURE_PROPOSAL", "FUTURE_CONCEPT"),
    "FCF": ("FOUNDER_CONFIRMED", "FUTURE_CONCEPT"),
}
EXPECTED_SOURCE_TIMESTAMPS = {
    "CHECKPOINT_03_PARENT": "1786996639.277979",
    "CHECKPOINT_03_PART_02": "1786996650.231529",
    "CHECKPOINT_03_PART_03": "1786996663.468959",
    "CHECKPOINT_03_PART_04": "1786996677.496709",
}
EXPECTED_SOURCE_MANIFEST = {
    "mission": [
        ("MISSION_PARENT", "1786996740.153019", 1, "MISSION", True),
        ("MISSION_SCOPE", "1786996752.202309", 2, "MISSION", True),
        ("MISSION_GATES", "1786996764.447649", 3, "MISSION", True),
    ],
    "checkpoint03": [
        ("CHECKPOINT_03_PARENT", "1786996639.277979", 1, "CHECKPOINT_03", True),
        ("CHECKPOINT_03_PART_02", "1786996650.231529", 2, "CHECKPOINT_03", True),
        ("CHECKPOINT_03_PART_03", "1786996663.468959", 3, "CHECKPOINT_03", True),
        ("CHECKPOINT_03_PART_04", "1786996677.496709", 4, "CHECKPOINT_03", True),
    ],
    "original_discovery": [
        ("DISCOVERY_PARENT", "1786929259.157699", 1, "ORIGINAL_DISCOVERY", True),
        ("DISCOVERY_PART_01", "1786929271.724929", 2, "ORIGINAL_DISCOVERY", True),
        ("DISCOVERY_PART_02", "1786929285.156489", 3, "ORIGINAL_DISCOVERY", True),
        ("DISCOVERY_PART_03", "1786929298.131999", 4, "ORIGINAL_DISCOVERY", True),
        ("DISCOVERY_PART_04", "1786929308.929669", 5, "ORIGINAL_DISCOVERY", True),
        ("DISCOVERY_PART_05", "1786929322.167819", 6, "ORIGINAL_DISCOVERY", True),
        ("DISCOVERY_PART_06", "1786929332.918159", 7, "ORIGINAL_DISCOVERY", True),
        ("DISCOVERY_PART_07", "1786961959.781219", 8, "ORIGINAL_DISCOVERY", True),
        ("DISCOVERY_CHECKPOINT_02", "1786969560.307449", 9, "ORIGINAL_DISCOVERY", True),
    ],
    "idea_vault": [
        ("IDEA_VAULT_PARENT", "1786970361.696939", 1, "IDEA_VAULT", True),
        ("IDEA_VAULT_PART_02", "1786970380.980809", 2, "IDEA_VAULT", True),
        ("IDEA_VAULT_USAGE", "1786970396.771679", 3, "IDEA_VAULT", True),
        ("IDEA_VAULT_CONTINUITY", "1786981791.500009", 4, "IDEA_VAULT", True),
    ],
}
EXPECTED_BRANDS = ["Sumwin", "Sansco", "Goldsco", "King", "StoneLand", "SUS"]
EXPECTED_THICKNESS_BANK = [f"{value / 100:.2f}" for value in range(35, 201, 5)]
EXPECTED_PILOT_THICKNESSES = [
    "0.45", "0.50", "0.55", "0.60", "0.70", "0.80",
    "0.90", "1.00", "1.10", "1.20", "1.50", "2.00",
]
EXPECTED_CRITERIA = [
    "DEMAND_SIGNAL", "SUPPLY_EVIDENCE", "GROSS_PROFIT_POTENTIAL", "REPEATABILITY",
    "PRODUCT_DATA_COMPLETENESS", "PHOTO_CONTENT_READINESS", "SEO_BUYER_INTENT",
    "OPERATIONAL_COMPLEXITY", "FULFILLMENT_RISK",
]
EXPECTED_CRITERION_STATES = [
    "SUBMITTED", "SUBMITTED", "MISSING", "MISSING", "SUBMITTED",
    "MISSING", "MISSING", "SUBMITTED", "SUBMITTED",
]
EXPECTED_IDEA_DISPOSITIONS = [
    *("USE_NOW_PLANNING_EVIDENCE_ONLY" for _ in range(9)),
    *("PLAN_NOW_IMPLEMENT_LATER" for _ in range(5)),
    *("DEFER" for _ in range(7)),
    *("REJECT_FOR_MISSION" for _ in range(4)),
]
EXPECTED_IDEA_SOURCE_TIMESTAMPS = [
    *("1786970361.696939" for _ in range(10)),
    "1786996663.468959",
    "1786970380.980809",
    "1786996663.468959",
    *("1786970361.696939" for _ in range(7)),
    "1786970380.980809",
    "1786970380.980809",
    "1786970361.696939",
    "1786970380.980809",
    "1786996752.202309",
]
EXPECTED_RECONCILIATION_RELATIONS = [
    "EXTENDS", "EXTENDS", "RESOLVES_EVIDENCE_ONLY", "REFINES",
    "REFINES", "REFINES", "REFINES", "REFINES",
]


def semantic_digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(encoded).hexdigest()


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


def audit_schema(value: Any) -> list[str]:
    issues: list[str] = []

    def walk(node: Any, path: str, depth: int) -> None:
        if depth > 80:
            issues.append(f"[SCHEMA_DEPTH] {path}: schema exceeds depth cap")
            return
        if isinstance(node, dict):
            ref = node.get("$ref")
            if isinstance(ref, str) and not ref.startswith("#/"):
                issues.append(f"[REMOTE_SCHEMA_REF] {path}: only local fragment references are allowed")
            if node.get("type") == "object" or "properties" in node:
                if node.get("additionalProperties") is not False:
                    issues.append(f"[PERMISSIVE_SCHEMA] {path}: every object boundary must be closed")
            for key, child in node.items():
                walk(child, f"{path}/{key}", depth + 1)
        elif isinstance(node, list):
            for index, child in enumerate(node):
                walk(child, f"{path}/{index}", depth + 1)

    walk(value, "<schema>", 0)
    return sorted(set(issues))


def audit_value(value: Any) -> list[str]:
    issues: list[str] = []
    nodes = 0

    def walk(node: Any, path: str, depth: int) -> None:
        nonlocal nodes
        nodes += 1
        if nodes > 40000:
            issues.append("[INPUT_NODE_CAP] input exceeds 40000 nodes")
            return
        if depth > 80:
            issues.append(f"[INPUT_DEPTH] {path}: input exceeds depth cap")
            return
        if isinstance(node, float) and not math.isfinite(node):
            issues.append(f"[NON_FINITE] {path}: non-finite numeric value")
        elif isinstance(node, dict):
            for key, child in node.items():
                walk(child, f"{path}/{key}", depth + 1)
        elif isinstance(node, list):
            for index, child in enumerate(node):
                walk(child, f"{path}/{index}", depth + 1)

    walk(value, "<root>", 0)
    return sorted(set(issues))


def load_validator(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[Any, dict[str, Any]]:
    contract = require_mapping(load_yaml(safe_path(contract_path, "C003-R1 contract")), "C003-R1 contract")
    if EXPECTED_CONTRACT_DIGEST != "TO_BE_FINALIZED" and semantic_digest(contract) != EXPECTED_CONTRACT_DIGEST:
        raise ValidationConfigurationError("C003-R1 contract literal policy differs")
    schema = require_mapping(load_json(safe_path(schema_path, "C003-R1 schema")), "C003-R1 schema")
    schema_issues = audit_schema(schema)
    if schema_issues:
        raise ValidationConfigurationError(schema_issues[0])
    return validate_schema(schema), contract


def validate_live_anchors(add: Any) -> None:
    base_validator, base_contract = load_base_validator()
    base_registry = load_yaml(BASE_REGISTRY_PATH)
    base_issues = validate_base_registry(base_registry, base_validator, base_contract)
    if base_issues:
        add("BASE_C003_REGRESSION", base_issues[0])

    candidates = require_mapping(load_yaml(C002_CANDIDATE_PATH), "C002 candidate registry")
    admin = require_mapping(load_yaml(C002_ADMIN_PATH), "C002 administration registry")
    admin_contract = require_mapping(load_yaml(C002_ADMIN_CONTRACT_PATH), "C002 administration contract")
    if candidates.get("candidates") != []:
        add("C002_CANDIDATE_REGRESSION", "C002 canonical candidate registry must remain empty")
    if not isinstance(admin.get("policies"), list) or len(admin["policies"]) != 8:
        add("C002_POLICY_REGRESSION", "C002 must retain exactly eight policy definitions")
    if admin.get("instances") != []:
        add("C002_INSTANCE_REGRESSION", "C002 policy instances must remain empty")
    commerce = admin_contract.get("invariants", {}).get("commerce_eligibility", {})
    if commerce.get("default_state") != "INQUIRY_ONLY":
        add("COMMERCE_STATE_REGRESSION", "C002 commerce default must remain INQUIRY_ONLY")

    base_entities = load_yaml(PRODUCT_ENTITIES_PATH)
    pd03a = require_mapping(load_yaml(PD03A_PATH), "PD03A registry")
    entities = list(base_entities) if isinstance(base_entities, list) else []
    entities.extend(pd03a.get("entities", []) if isinstance(pd03a.get("entities"), list) else [])
    if any(isinstance(item, dict) and item.get("entity_type") == "SKU" for item in entities):
        add("SKU_REGRESSION", "canonical SKU count must remain zero")

    pd03b = require_mapping(load_yaml(PD03B_PATH), "PD03B registry")
    pilots = pd03b.get("pilots", [])
    if not isinstance(pilots, list) or len(pilots) != 3:
        add("PD03B_COUNT_REGRESSION", "PD03B must retain three seed/reference records")
    elif any(not isinstance(item, dict) or item.get("availability_status") != "MISSING_DATA_VALUE" for item in pilots):
        add("PD03B_AVAILABILITY_REGRESSION", "PD03B Availability must remain MISSING_DATA_VALUE")

    current_state = safe_path(CURRENT_STATE_PATH, "Current Project State").read_text(encoding="utf-8")
    if "FROZEN_AT_PROTECTED_ARCHITECTURE_BOUNDARY" not in current_state:
        add("C1_T03_REGRESSION", "Current Project State must preserve the frozen C1-T03 boundary")


def validate_registry(value: Any, schema_validator: Any, contract: dict[str, Any]) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    for issue in audit_value(value):
        issues.append(issue)
    for error in schema_validator.iter_errors(value):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add("SCHEMA_VALIDATION", f"{location}: {error.message}")
    if not isinstance(value, dict):
        return sorted(set(issues))

    if EXPECTED_REGISTRY_DIGEST != "TO_BE_FINALIZED" and semantic_digest(value) != EXPECTED_REGISTRY_DIGEST:
        add("REGISTRY_DIGEST", "C003-R1 canonical evidence differs from the reviewed package")

    base_pin = value.get("base_c003_pin", {})
    contract_pin = contract.get("base_c003", {})
    expected_pin = {
        "record_count": contract_pin.get("exact_record_count"),
        "contract_semantic_sha256": contract_pin.get("exact_contract_semantic_sha256"),
        "registry_semantic_sha256": contract_pin.get("exact_registry_semantic_sha256"),
        "mutation_allowed": contract_pin.get("mutation_allowed"),
    }
    if base_pin != expected_pin:
        add("BASE_C003_PIN", "extension must pin the exact immutable C003 package")

    source_manifest = value.get("source_manifest", {})
    if isinstance(source_manifest, dict):
        for group, expected in EXPECTED_SOURCE_MANIFEST.items():
            actual_items = source_manifest.get(group, [])
            actual = [
                (item.get("source_id"), item.get("message_ts"), item.get("source_order"), item.get("role"), item.get("complete"))
                for item in actual_items if isinstance(item, dict)
            ] if isinstance(actual_items, list) else []
            if actual != expected:
                add("SOURCE_MANIFEST", f"{group} source manifest must be exact and complete")
        if source_manifest.get("all_threads_complete") is not True or source_manifest.get("pagination_remaining") is not False:
            add("SOURCE_COMPLETENESS", "all source threads must be complete with no remaining pagination")
    else:
        add("SOURCE_MANIFEST", "source manifest must be an object")

    reconciliations = value.get("base_c003_reconciliation", [])
    if not isinstance(reconciliations, list) or len(reconciliations) != 8:
        add("RECONCILIATION_COUNT", "base C003 reconciliation must contain exactly eight entries")
        reconciliations = reconciliations if isinstance(reconciliations, list) else []
    base_registry = require_mapping(load_yaml(BASE_REGISTRY_PATH), "base C003 registry")
    prior_codes = {
        item.get("decision_code") for item in base_registry.get("evidence_records", []) if isinstance(item, dict)
    }
    delta_codes = {
        item.get("decision_code") for item in value.get("evidence_delta", []) if isinstance(item, dict)
    }
    relations: list[Any] = []
    for index, item in enumerate(reconciliations, start=1):
        if not isinstance(item, dict):
            continue
        if item.get("sequence") != index or item.get("reconciliation_id") != f"C003R1-REC-{index:03d}":
            add("RECONCILIATION_ORDER", f"reconciliation {index} identity/order differs")
        if not set(item.get("prior_decision_codes", [])).issubset(prior_codes):
            add("RECONCILIATION_PRIOR_REF", f"reconciliation {index} has an unknown base C003 reference")
        if not set(item.get("delta_decision_codes", [])).issubset(delta_codes):
            add("RECONCILIATION_DELTA_REF", f"reconciliation {index} has an unknown C003-R1 reference")
        if item.get("supersedes_prior") is not False or item.get("canonical_population") is not False:
            add("RECONCILIATION_AUTHORITY", f"reconciliation {index} cannot supersede or populate canonical truth")
        relations.append(item.get("relation"))
    if relations != EXPECTED_RECONCILIATION_RELATIONS:
        add("RECONCILIATION_RELATION", "base-to-delta relations must preserve the exact reviewed order")

    records = value.get("evidence_delta", [])
    model = contract.get("evidence_delta", {})
    expected_count = model.get("exact_record_count")
    if not isinstance(records, list) or len(records) != expected_count:
        add("EVIDENCE_COUNT", f"evidence delta must contain exactly {expected_count} records")
        records = records if isinstance(records, list) else []

    classifications: Counter[Any] = Counter()
    temporal: Counter[Any] = Counter()
    ledger: list[Any] = []
    ids: list[Any] = []
    codes: list[Any] = []
    authority_false = {
        "candidate_population": False, "product_population": False, "sku_assignment": False,
        "availability_or_stock": False, "current_or_public_price": False,
        "commerce_activation": False, "customer_or_order_population": False,
        "payment_activation": False, "wordpress_woocommerce": False,
        "runtime_staging_production": False, "external_write": False,
    }
    ranges = model.get("exact_source_ranges", [])
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            continue
        classifications[record.get("evidence_classification")] += 1
        temporal[record.get("temporal_role")] += 1
        ledger.append(record.get("ledger_class"))
        ids.append(record.get("evidence_id"))
        codes.append(record.get("decision_code"))
        if record.get("sequence") != index:
            add("SOURCE_ORDER", f"record {index} sequence is not exact")
        if record.get("evidence_id") != f"c003r1ev:{index:012x}":
            add("EVIDENCE_ID", f"record {index} evidence_id is not deterministic")
        if record.get("decision_code") != f"C003R1-CP03-{index:03d}":
            add("DECISION_CODE", f"record {index} decision_code is not deterministic")
        pair = LEDGER_MAPPING.get(record.get("ledger_class"))
        actual_pair = (record.get("evidence_classification"), record.get("temporal_role"))
        if pair != actual_pair:
            add("CLASS_TEMPORAL_BINDING", f"record {index} ledger class does not match independent class/temporal values")
        if record.get("source_ts") != EXPECTED_SOURCE_TIMESTAMPS.get(record.get("source_id")):
            add("SOURCE_LOCATOR", f"record {index} source locator is not exact")
        expected_source = None
        for source_range in ranges if isinstance(ranges, list) else []:
            if source_range.get("first_record", 0) <= index <= source_range.get("last_record", -1):
                expected_source = source_range.get("source_id")
                break
        if record.get("source_id") != expected_source:
            add("SOURCE_RANGE", f"record {index} is outside its exact source range")
        if record.get("authority_effects") != authority_false:
            add("AUTHORITY_EFFECT", f"record {index} must have all authority effects false")

    exact_pilot_owners = {
        17: "C002_COMMERCIAL_PILOT_CANDIDATE",
        26: "C002_PRODUCT_BUILDER_ADD_VALUE",
        27: "C002_BRAND_PROVENANCE",
        28: "PRODUCT_HIERARCHY_VARIANT_RULES",
        29: "C002_COMMERCIAL_PILOT_CANDIDATE",
        30: "PRODUCT_HIERARCHY_VARIANT_RULES",
        31: "PRODUCT_HIERARCHY_VARIANT_RULES",
    }
    for sequence, owner in exact_pilot_owners.items():
        if sequence <= len(records) and isinstance(records[sequence - 1], dict) and records[sequence - 1].get("canonical_owner") != owner:
            add("PILOT_OWNER_RECONCILIATION", f"record {sequence} must reuse canonical owner {owner}")

    if len(ids) != len(set(ids)) or len(codes) != len(set(codes)):
        add("IDENTITY_COLLISION", "evidence IDs and decision codes must be unique")
    expected_classes = model.get("classifications", {})
    actual_classes = {key: classifications.get(key, 0) for key in expected_classes}
    if actual_classes != expected_classes:
        add("CLASSIFICATION_COUNTS", f"expected {expected_classes}, got {actual_classes}")
    expected_temporal = model.get("temporal_roles", {})
    actual_temporal = {key: temporal.get(key, 0) for key in expected_temporal}
    if actual_temporal != expected_temporal:
        add("TEMPORAL_COUNTS", f"expected {expected_temporal}, got {actual_temporal}")
    if ledger != model.get("exact_ledger_class_order"):
        add("LEDGER_ORDER", "evidence ledger class order differs from contract")

    ideas = value.get("idea_vault_dispositions", [])
    expected_idea_count = contract.get("idea_vault_disposition", {}).get("exact_entry_count")
    if not isinstance(ideas, list) or len(ideas) != expected_idea_count:
        add("IDEA_COUNT", f"idea disposition must contain exactly {expected_idea_count} entries")
        ideas = ideas if isinstance(ideas, list) else []
    idea_dispositions: list[Any] = []
    idea_sources: list[Any] = []
    for index, item in enumerate(ideas, start=1):
        if not isinstance(item, dict):
            continue
        if item.get("sequence") != index or item.get("idea_id") != f"C003R1-IDEA-{index:03d}":
            add("IDEA_ORDER", f"idea {index} order or identity differs")
        if item.get("disposition_source_ts") != "1786996752.202309":
            add("IDEA_DISPOSITION_SOURCE", f"idea {index} must cite the Mission disposition source")
        if item.get("implementation_authority") is not False:
            add("IDEA_AUTHORITY", f"idea {index} cannot create implementation authority")
        idea_dispositions.append(item.get("disposition"))
        idea_sources.append(item.get("idea_source_ts"))
    if idea_dispositions != EXPECTED_IDEA_DISPOSITIONS:
        add("IDEA_DISPOSITION_ORDER", "idea dispositions must preserve the Mission 9/5/7/4 order")
    if idea_sources != EXPECTED_IDEA_SOURCE_TIMESTAMPS:
        add("IDEA_ORIGIN_SOURCE", "idea origins must cite Vault, Checkpoint or Mission without false attribution")

    pilot = value.get("pilot_readiness_packet", {})
    if isinstance(pilot, dict):
        if pilot.get("brands") != EXPECTED_BRANDS:
            add("PILOT_BRANDS", "201/51 Pilot brand order and membership must be exact")
        if pilot.get("stainless_thickness_value_bank_mm") != EXPECTED_THICKNESS_BANK:
            add("THICKNESS_BANK", "thickness candidate bank must be 0.35..2.00 by exact 0.05 increments")
        if pilot.get("founder_confirmed_pilot_thicknesses_mm") != EXPECTED_PILOT_THICKNESSES:
            add("PILOT_THICKNESSES", "201/51 Founder-confirmed thickness evidence must be exact")
        combination = pilot.get("combination_evidence", {})
        if combination != {
            "evidence_backed_valid_tuples": [], "tuple_count": 0,
            "unknown_tuple_space_preserved": True, "cartesian_generation": False,
            "value_bank_membership_implies_valid_tuple": False,
        }:
            add("CARTESIAN_BOUNDARY", "Pilot packet must preserve unknown tuple space and zero inferred tuples")
        mass = pilot.get("mass_observation_policy", {})
        if not isinstance(mass, dict) or mass.get("observations") != [] or mass.get("variant_identity") is not False:
            add("MASS_BOUNDARY", "mass must remain empty batch observation history and not Variant identity")
        readiness = pilot.get("c002_readiness", {})
        criteria = readiness.get("criteria", []) if isinstance(readiness, dict) else []
        criterion_codes = [item.get("criterion_code") for item in criteria if isinstance(item, dict)]
        if criterion_codes != EXPECTED_CRITERIA or readiness.get("criterion_order") != EXPECTED_CRITERIA:
            add("READINESS_CRITERIA", "C002 nine-criterion order must be exact")
        criterion_states = [item.get("evidence_state") for item in criteria if isinstance(item, dict)]
        if criterion_states != EXPECTED_CRITERION_STATES:
            add("READINESS_STATES", "C002 evidence states must preserve the exact fail-closed Mission assessment")
        if any(item.get("resolved") is not False for item in criteria if isinstance(item, dict)):
            add("READINESS_PROMOTION", "Checkpoint evidence cannot resolve any C002 selection criterion")
        known_readiness_refs = prior_codes | delta_codes
        for item in criteria if isinstance(criteria, list) else []:
            if not isinstance(item, dict):
                continue
            refs = item.get("evidence_record_refs", [])
            if not set(refs).issubset(known_readiness_refs):
                add("READINESS_EVIDENCE_REF", f"{item.get('criterion_code')} contains an unknown C003/C003-R1 evidence reference")
            if item.get("evidence_state") == "MISSING" and refs:
                add("READINESS_STATE_REF", f"{item.get('criterion_code')} is MISSING and must have no evidence references")
            if item.get("evidence_state") == "SUBMITTED" and not refs:
                add("READINESS_STATE_REF", f"{item.get('criterion_code')} is SUBMITTED and must have at least one evidence reference")
        if readiness.get("resolved_count") != 0 or readiness.get("unresolved_count") != 9:
            add("READINESS_COUNTS", "Pilot readiness must remain 0 resolved / 9 unresolved")
        effects = pilot.get("selection_effects", {})
        expected_effects = {
            "candidate_registry_population": False, "product_state": "NOT_CREATED",
            "sku_state": "NOT_ASSIGNED", "availability_state": "NOT_ASSERTED",
            "price_state": "NO_CURRENT_OR_PUBLIC_PRICE_FACT", "commerce_state": "INQUIRY_ONLY",
            "runtime_state": "NONE", "production_state": "NONE",
        }
        if effects != expected_effects:
            add("SELECTION_EFFECT", "Pilot packet must preserve all fail-closed selection effects")

    if value.get("authority_effects") != authority_false:
        add("ROOT_AUTHORITY_EFFECT", "root authority effects must all remain false")

    validate_live_anchors(add)
    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    args = parser.parse_args()
    try:
        schema_validator, contract = load_validator()
        registry_path = safe_path(Path(args.registry), "C003-R1 registry")
        registry = load_yaml(registry_path)
        issues = validate_registry(registry, schema_validator, contract)
    except (ValidationConfigurationError, ValueError, TypeError) as exc:
        print(f"[CONFIGURATION] {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print("C003-R1 Checkpoint 03 evidence and 201/51 readiness validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
