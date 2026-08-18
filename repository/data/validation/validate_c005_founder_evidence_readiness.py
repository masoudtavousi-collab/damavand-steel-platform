#!/usr/bin/env python3
"""Deterministic offline validator for C005 Founder evidence/readiness reconciliation."""

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


CONTRACT_PATH = ROOT / "repository/data/contracts/c005-founder-evidence-readiness.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/c005-founder-evidence-readiness.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c005/201-51-founder-evidence-readiness.yaml"
C002_CANDIDATE_CONTRACT_PATH = ROOT / "repository/data/contracts/commercial-pilot-candidate.contract.yaml"
C002_CANDIDATE_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
C002_ADMIN_CONTRACT_PATH = ROOT / "repository/data/contracts/product-administration-policy.contract.yaml"
C002_ADMIN_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c002/product-administration-policies.yaml"
C003_R3_CONTRACT_PATH = ROOT / "repository/data/contracts/valid-combination-evidence-matrix.contract.yaml"
C003_R3_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c003r2/201-51-founder-evidence-completion.yaml"
C004_CONTRACT_PATH = ROOT / "repository/data/contracts/competitive-intelligence.contract.yaml"
C004_ADVANTAGE_PATH = ROOT / "repository/data/registries/extensions/c004/damavand-advantages.yaml"
C003_BASE_CONTRACT_PATH = ROOT / "repository/data/contracts/founder-product-commerce-discovery.contract.yaml"
C003_BASE_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c003/founder-product-commerce-discovery-session-01.yaml"
C003_R1_CONTRACT_PATH = ROOT / "repository/data/contracts/founder-product-commerce-checkpoint03.contract.yaml"
C003_R1_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c003r1/checkpoint03-evidence-and-pilot-readiness.yaml"
PRODUCT_ENTITIES_PATH = ROOT / "repository/data/registries/product-entities.yaml"
PD03A_PATH = ROOT / "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml"

# Pinned after independent review of the final semantic objects.
EXPECTED_CONTRACT_DIGEST = "e10707317a3a7c455e3205fed0e058d61c616fd2db126c4862c7f318757e03fa"
EXPECTED_SCHEMA_DIGEST = "77e392a4d0f39dc3bb8851837e5b49ffb62e302de0c262055d351821549a3bb4"
EXPECTED_REGISTRY_DIGEST = "553da985f1a4e655ff34b0d85cc56bb078365c4cd3ec86f3e270e8cadf416e8b"

EXPECTED_MAIN = "ebe105279eea04bb0ed880c8a32750ddef3eb9dd"
EXPECTED_SOURCE_IDS = [
    "C005_PLANNING_CHECKPOINT",
    "C005_FOUNDER_EVIDENCE_A",
    "C005_FOUNDER_EVIDENCE_B",
    "C005_FOUNDER_EVIDENCE_C",
    "C005_FOUNDER_EVIDENCE_D",
]
EXPECTED_SOURCE_TS = [
    "1787080262.415499",
    "1787056479.144299",
    "1787080149.589239",
    "1787080165.322449",
    "1787080178.569909",
]
EXPECTED_SOURCES = [
    {
        "source_id": "C005_PLANNING_CHECKPOINT", "message_ts": "1787080262.415499",
        "source_locator": "slack:C0BNHRRTE9F:1787080262.415499",
        "captured_at": "2026-08-18T22:41:02.415499+03:30", "source_role": "PLANNING_CHECKPOINT",
        "evidence_classification": "ARCHITECTURE_PROPOSAL", "temporal_role": "PLANNING_ONLY",
        "title": "C005 PLANNING CHECKPOINT — 201/51 FOUNDER EVIDENCE RECONCILIATION & READINESS RE-EVALUATION",
        "thread_complete": True, "reply_count": 0,
    },
    {
        "source_id": "C005_FOUNDER_EVIDENCE_A", "message_ts": "1787056479.144299",
        "source_locator": "slack:C0BNHRRTE9F:1787056479.144299",
        "captured_at": "2026-08-18T16:04:39.144299+03:30", "source_role": "FOUNDER_EVIDENCE",
        "evidence_classification": "FOUNDER_CONFIRMED", "temporal_role": "CURRENT_INTENT",
        "title": "FOUNDER EVIDENCE — C003-R3 POST-MERGE PARALLEL READINESS DISCOVERY",
        "thread_complete": True, "reply_count": 0,
    },
    {
        "source_id": "C005_FOUNDER_EVIDENCE_B", "message_ts": "1787080149.589239",
        "source_locator": "slack:C0BNHRRTE9F:1787080149.589239",
        "captured_at": "2026-08-18T22:39:09.589239+03:30", "source_role": "FOUNDER_EVIDENCE",
        "evidence_classification": "FOUNDER_CONFIRMED", "temporal_role": "CURRENT_INTENT",
        "title": "FOUNDER EVIDENCE — 201/51 BUSINESS & COMMERCE DISCOVERY — PART A",
        "thread_complete": True, "reply_count": 0,
    },
    {
        "source_id": "C005_FOUNDER_EVIDENCE_C", "message_ts": "1787080165.322449",
        "source_locator": "slack:C0BNHRRTE9F:1787080165.322449",
        "captured_at": "2026-08-18T22:39:25.322449+03:30", "source_role": "FOUNDER_EVIDENCE",
        "evidence_classification": "FOUNDER_CONFIRMED", "temporal_role": "CURRENT_INTENT",
        "title": "FOUNDER EVIDENCE — 201/51 BUSINESS & COMMERCE DISCOVERY — PART B",
        "thread_complete": True, "reply_count": 0,
    },
    {
        "source_id": "C005_FOUNDER_EVIDENCE_D", "message_ts": "1787080178.569909",
        "source_locator": "slack:C0BNHRRTE9F:1787080178.569909",
        "captured_at": "2026-08-18T22:39:38.569909+03:30", "source_role": "FOUNDER_EVIDENCE",
        "evidence_classification": "FOUNDER_CONFIRMED", "temporal_role": "CURRENT_INTENT",
        "title": "FOUNDER EVIDENCE — 201/51 BUSINESS & COMMERCE DISCOVERY — PART C",
        "thread_complete": True, "reply_count": 0,
    },
]
EXPECTED_CRITERIA = [
    "DEMAND_SIGNAL",
    "SUPPLY_EVIDENCE",
    "GROSS_PROFIT_POTENTIAL",
    "REPEATABILITY",
    "PRODUCT_DATA_COMPLETENESS",
    "PHOTO_CONTENT_READINESS",
    "SEO_BUYER_INTENT",
    "OPERATIONAL_COMPLEXITY",
    "FULFILLMENT_RISK",
]
EXPECTED_PREVIOUS_STATES = [
    "SUBMITTED", "SUBMITTED", "MISSING", "MISSING", "SUBMITTED",
    "MISSING", "MISSING", "SUBMITTED", "SUBMITTED",
]
EXPECTED_NEW_STATES = [
    "SUBMITTED", "SUBMITTED", "SUBMITTED", "SUBMITTED", "SUBMITTED",
    "MISSING", "SUBMITTED", "SUBMITTED", "SUBMITTED",
]
EXPECTED_REVIEWABLE = [True, False, True, True, True, False, True, True, False]
EXPECTED_EVIDENCE_REFS = {
    "DEMAND_SIGNAL": ["C003-DISC-011", "C003-DISC-017", "C003-DISC-018", "C005-EVID-002", "C005-EVID-006"],
    "SUPPLY_EVIDENCE": ["C003R1-CP03-001", "C003R1-CP03-002", "C003R1-CP03-003", "C005-EVID-003"],
    "GROSS_PROFIT_POTENTIAL": ["C005-EVID-001"],
    "REPEATABILITY": ["C005-EVID-002", "C005-EVID-006"],
    "PRODUCT_DATA_COMPLETENESS": ["C003R1-CP03-026", "C003R1-CP03-027", "C003R1-CP03-028", "C003R1-CP03-030", "C003R1-CP03-031", "C003R3-ANSWER-001", "C005-EVID-006"],
    "PHOTO_CONTENT_READINESS": [],
    "SEO_BUYER_INTENT": ["C005-EVID-005", "C005-EVID-006"],
    "OPERATIONAL_COMPLEXITY": ["C003R1-CP03-032", "C003R1-CP03-034", "C003R1-CP03-041", "C003R1-CP03-053", "C005-EVID-007", "C005-EVID-008", "C005-EVID-009", "C005-EVID-010", "C005-EVID-011", "C005-EVID-013", "C005-EVID-014"],
    "FULFILLMENT_RISK": ["C003R1-CP03-007", "C003R1-CP03-008", "C003R1-CP03-041", "C003R1-CP03-042", "C003R1-CP03-043", "C005-EVID-003", "C005-EVID-013"],
}
EXPECTED_GAP_REFS = {criterion: [] for criterion in EXPECTED_CRITERIA}
EXPECTED_GAP_REFS["PHOTO_CONTENT_READINESS"] = ["C005-EVID-004"]
EXPECTED_SUPPLEMENTARY_REFS = {criterion: [] for criterion in EXPECTED_CRITERIA}
EXPECTED_SUPPLEMENTARY_REFS["SEO_BUYER_INTENT"] = ["docs/201_51_PILOT_COMPETITIVE_EXPERIENCE_BLUEPRINT_V1.0.md"]
EXPECTED_COMPONENT_STATES = {criterion: [] for criterion in EXPECTED_CRITERIA}
EXPECTED_COMPONENT_STATES["PHOTO_CONTENT_READINESS"] = [
    {"component_code": "PHOTO_ASSET", "evidence_state": "MISSING", "evidence_record_refs": [], "reviewable": False},
    {"component_code": "TEXT_CONTENT_STRATEGY", "evidence_state": "SUBMITTED", "evidence_record_refs": ["C005-EVID-005"], "reviewable": True},
]
EXPECTED_CLASSIFICATIONS = ["FOUNDER_CONFIRMED"] * 14 + ["ARCHITECTURE_PROPOSAL"] * 3
EXPECTED_TEMPORAL = ["CURRENT_INTENT"] * 11 + ["FUTURE_CAPABILITY", "CURRENT_INTENT", "CURRENT_INTENT"] + ["PLANNING_ONLY"] * 3
EXPECTED_RECORD_BINDINGS = [
    ("C005_FOUNDER_EVIDENCE_A", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "GROSS_PROFIT", "DISCOVERY_BACKLOG_ONLY", "EVIDENCE_ONLY"),
    ("C005_FOUNDER_EVIDENCE_A", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "DEMAND_REPEATABILITY", "C002_INVENTORY_HARMONY", "EVIDENCE_ONLY"),
    ("C005_FOUNDER_EVIDENCE_A", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "SUPPLY_FULFILLMENT", "DISCOVERY_BACKLOG_ONLY", "EVIDENCE_ONLY"),
    ("C005_FOUNDER_EVIDENCE_A", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "PHOTO_CONTENT", "PRODUCT_CONTENT_FUTURE", "EVIDENCE_ONLY"),
    ("C005_FOUNDER_EVIDENCE_A", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "PRODUCT_CONTENT", "PRODUCT_CONTENT_FUTURE", "FUTURE_CONTRACT_INPUT"),
    ("C005_FOUNDER_EVIDENCE_B", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "PRODUCT_DEMAND", "PRODUCT_HIERARCHY_VARIANT_RULES", "EVIDENCE_ONLY"),
    ("C005_FOUNDER_EVIDENCE_B", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "MASS_LIFECYCLE", "C002_MASS_PROVENANCE", "EVIDENCE_ONLY"),
    ("C005_FOUNDER_EVIDENCE_B", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "PRICING_CONTEXT", "DISCOVERY_BACKLOG_ONLY", "FUTURE_CONTRACT_INPUT"),
    ("C005_FOUNDER_EVIDENCE_C", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "PRICING_CHANGE_CONTROL", "DISCOVERY_BACKLOG_ONLY", "FUTURE_CONTRACT_INPUT"),
    ("C005_FOUNDER_EVIDENCE_C", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "PRIVATE_PRICING", "INQUIRY_CUSTOMER_MODEL", "FUTURE_CONTRACT_INPUT"),
    ("C005_FOUNDER_EVIDENCE_D", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "VIP_LOYALTY", "INQUIRY_CUSTOMER_MODEL", "FUTURE_CONTRACT_INPUT"),
    ("C005_FOUNDER_EVIDENCE_D", "FOUNDER_CONFIRMED", "FUTURE_CAPABILITY", "VIP_LOYALTY_FUTURE", "INQUIRY_CUSTOMER_MODEL", "FUTURE_CONTRACT_INPUT"),
    ("C005_FOUNDER_EVIDENCE_D", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "ORDER_CUT_SHIPPING", "DISCOVERY_BACKLOG_ONLY", "FUTURE_CONTRACT_INPUT"),
    ("C005_FOUNDER_EVIDENCE_D", "FOUNDER_CONFIRMED", "CURRENT_INTENT", "ORDER_WORKFLOW", "INQUIRY_CUSTOMER_MODEL", "FUTURE_CONTRACT_INPUT"),
    ("C005_FOUNDER_EVIDENCE_B", "ARCHITECTURE_PROPOSAL", "PLANNING_ONLY", "IMPLEMENTATION_MECHANICS", "DISCOVERY_BACKLOG_ONLY", "ARCHITECTURE_PROPOSAL_ONLY"),
    ("C005_FOUNDER_EVIDENCE_C", "ARCHITECTURE_PROPOSAL", "PLANNING_ONLY", "IMPLEMENTATION_MECHANICS", "DISCOVERY_BACKLOG_ONLY", "ARCHITECTURE_PROPOSAL_ONLY"),
    ("C005_FOUNDER_EVIDENCE_D", "ARCHITECTURE_PROPOSAL", "PLANNING_ONLY", "IMPLEMENTATION_MECHANICS", "DISCOVERY_BACKLOG_ONLY", "ARCHITECTURE_PROPOSAL_ONLY"),
]
EXPECTED_AUTHORITY = {
    "evidence_reconciliation": True,
    "c002_readiness_reevaluation": True,
    "candidate_population": False,
    "product_population": False,
    "controlled_value_promotion": False,
    "valid_tuple_promotion": False,
    "sku_assignment": False,
    "mass_population": False,
    "supply_population": False,
    "availability_or_stock_claim": False,
    "current_or_public_price": False,
    "price_engine": False,
    "customer_or_order_population": False,
    "vip_or_loyalty_activation": False,
    "commerce_activation": False,
    "payment_activation": False,
    "wordpress_woocommerce_mutation": False,
    "hosting_mutation": False,
    "content_or_media_publication": False,
    "reservation_engine": False,
    "quotation_engine": False,
    "cutting_service_implementation": False,
    "shipping_implementation": False,
    "runtime_staging_production": False,
    "deployment": False,
    "c1_t03_repair": False,
    "c003_a_start": False,
    "c003_b_start": False,
    "merge": False,
    "successor_mission": False,
}
EXPECTED_BASE_PINS = {
    "c003_base_contract_semantic_sha256": "eff0b6d1546c67c7e5f33f7c39e387bb97fc7398f5190b3c578247db4daf9bf9",
    "c003_base_registry_semantic_sha256": "6531464375953bb117515e4665a679bcf90f15388f0e7513a7268f3787714cf8",
    "c003_r1_contract_semantic_sha256": "2a3a5dca032ad2327e1f6ac491a7d1741d574310c889edad64bef85367e4557b",
    "c003_r1_registry_semantic_sha256": "a6c4a3181db06c1292232a1a8f725a5e5be998a064075910a3da65e7a3d04a75",
    "c002_candidate_contract_semantic_sha256": "923731cb080b0ecc05abb21b1189bfdd0df94297780cce364bb791479f7f47e3",
    "c002_candidate_registry_semantic_sha256": "deb0215d2b5f4b5ec0061f937aec9c3e37cf97c94432a23737bf5756cef9587e",
    "c002_product_administration_contract_semantic_sha256": "75b608e67b6ca3c870e6bf0b533310fbb131a75fa576a79e75c4a936659c33ff",
    "c002_product_administration_registry_semantic_sha256": "796d2dfc424a75f998b309f04e88443d0ffb7450bd457bddf86b574535624fe7",
    "c003_r3_contract_semantic_sha256": "f6e9cc81ef18ded5506714d8316835ff0c0919a38af5a1f1508b93b10297f973",
    "c003_r3_registry_semantic_sha256": "22bf396a7b92b6fe03bce069e889a87dd063174e0f1b7abfd3e51fc349de8172",
    "c004_contract_semantic_sha256": "e4652271d81587d78b8d1fadf6395ef13ca87d7bae7450db346a25e62c7feacc",
    "c004_advantage_registry_semantic_sha256": "eb14e53a04f60250b3125dc3d0422a62e53a0d01fb3f15741182f4a04327c8c1",
}
EXPECTED_TOTALS = {
    "criterion_count": 9,
    "verified_count": 0,
    "submitted_count": 8,
    "missing_count": 1,
    "reviewable_count": 6,
    "resolved_count": 0,
    "unresolved_count": 9,
    "open_blocking_count": 9,
}


def semantic_digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def safe_path(path: Path, label: str) -> Path:
    absolute = path if path.is_absolute() else ROOT / path
    try:
        resolved = absolute.resolve(strict=True)
    except FileNotFoundError as exc:
        raise ValidationConfigurationError(f"missing {label}: {path}") from exc
    if resolved != ROOT and ROOT not in resolved.parents:
        raise ValidationConfigurationError(f"{label} must remain inside the repository")
    current = absolute.absolute()
    while current != ROOT and current != current.parent:
        if current.is_symlink():
            raise ValidationConfigurationError(f"{label} path must not contain a symbolic link")
        current = current.parent
    if absolute.stat().st_size > 2_000_000:
        raise ValidationConfigurationError(f"{label} exceeds 2 MB byte cap")
    return resolved


def audit_schema(value: Any) -> list[str]:
    issues: list[str] = []

    def walk(node: Any, path: str, depth: int) -> None:
        if depth > 100:
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
        if nodes > 50000:
            issues.append("[INPUT_NODE_CAP] input exceeds 50000 nodes")
            return
        if depth > 100:
            issues.append(f"[INPUT_DEPTH] {path}: input exceeds depth cap")
            return
        if isinstance(node, float) and not math.isfinite(node):
            issues.append(f"[NON_FINITE] {path}: non-finite number")
        elif isinstance(node, dict):
            for key, child in node.items():
                walk(child, f"{path}/{key}", depth + 1)
        elif isinstance(node, list):
            for index, child in enumerate(node):
                walk(child, f"{path}/{index}", depth + 1)

    walk(value, "<root>", 0)
    return sorted(set(issues))


def load_validator(contract_path: Path = CONTRACT_PATH, schema_path: Path = SCHEMA_PATH) -> tuple[Any, dict[str, Any]]:
    contract = require_mapping(load_yaml(safe_path(contract_path, "C005 contract")), "C005 contract")
    schema = require_mapping(load_json(safe_path(schema_path, "C005 schema")), "C005 schema")
    schema_issues = audit_schema(schema)
    if schema_issues:
        raise ValidationConfigurationError(schema_issues[0])
    if EXPECTED_CONTRACT_DIGEST != "TO_BE_FINALIZED" and semantic_digest(contract) != EXPECTED_CONTRACT_DIGEST:
        raise ValidationConfigurationError("C005 contract literal policy differs")
    if EXPECTED_SCHEMA_DIGEST != "TO_BE_FINALIZED" and semantic_digest(schema) != EXPECTED_SCHEMA_DIGEST:
        raise ValidationConfigurationError("C005 schema literal policy differs")
    return validate_schema(schema), contract


def known_evidence_codes() -> set[str]:
    base_registry = require_mapping(load_yaml(safe_path(C003_BASE_REGISTRY_PATH, "C003 base registry")), "C003 base registry")
    r1_registry = require_mapping(load_yaml(safe_path(C003_R1_REGISTRY_PATH, "C003-R1 registry")), "C003-R1 registry")
    codes = {
        item.get("decision_code")
        for item in base_registry.get("evidence_records", [])
        if isinstance(item, dict) and isinstance(item.get("decision_code"), str)
    }
    codes.update(
        item.get("decision_code")
        for item in r1_registry.get("evidence_delta", [])
        if isinstance(item, dict) and isinstance(item.get("decision_code"), str)
    )
    codes.add("C003R3-ANSWER-001")
    return codes


def validate_dependency_pins(add: Any, contract: dict[str, Any]) -> None:
    paths = {
        "c003_base_contract_semantic_sha256": C003_BASE_CONTRACT_PATH,
        "c003_base_registry_semantic_sha256": C003_BASE_REGISTRY_PATH,
        "c003_r1_contract_semantic_sha256": C003_R1_CONTRACT_PATH,
        "c003_r1_registry_semantic_sha256": C003_R1_REGISTRY_PATH,
        "c002_candidate_contract_semantic_sha256": C002_CANDIDATE_CONTRACT_PATH,
        "c002_candidate_registry_semantic_sha256": C002_CANDIDATE_REGISTRY_PATH,
        "c002_product_administration_contract_semantic_sha256": C002_ADMIN_CONTRACT_PATH,
        "c002_product_administration_registry_semantic_sha256": C002_ADMIN_REGISTRY_PATH,
        "c003_r3_contract_semantic_sha256": C003_R3_CONTRACT_PATH,
        "c003_r3_registry_semantic_sha256": C003_R3_REGISTRY_PATH,
        "c004_contract_semantic_sha256": C004_CONTRACT_PATH,
        "c004_advantage_registry_semantic_sha256": C004_ADVANTAGE_PATH,
    }
    live = {
        key: semantic_digest(require_mapping(load_yaml(safe_path(path, key)), key))
        for key, path in paths.items()
    }
    if contract.get("base_pins") != EXPECTED_BASE_PINS or live != EXPECTED_BASE_PINS:
        add("BASE_PIN_REGRESSION", "C002/C003/C003-R1/C003-R3/C004 canonical owners must match exact semantic pins")

    candidate_contract = require_mapping(load_yaml(safe_path(C002_CANDIDATE_CONTRACT_PATH, "C002 candidate contract")), "C002 candidate contract")
    candidate_registry = require_mapping(load_yaml(safe_path(C002_CANDIDATE_REGISTRY_PATH, "C002 candidate registry")), "C002 candidate registry")
    admin_contract = require_mapping(load_yaml(safe_path(C002_ADMIN_CONTRACT_PATH, "C002 admin contract")), "C002 admin contract")
    admin_registry = require_mapping(load_yaml(safe_path(C002_ADMIN_REGISTRY_PATH, "C002 admin registry")), "C002 admin registry")
    c003_r3 = require_mapping(load_yaml(safe_path(C003_R3_REGISTRY_PATH, "C003-R3 registry")), "C003-R3 registry")
    if candidate_registry.get("candidates") != []:
        add("C002_CANDIDATE_REGRESSION", "C002 candidate registry must remain empty")
    if len(admin_registry.get("policies", [])) != 8 or admin_registry.get("instances") != []:
        add("C002_ADMIN_REGRESSION", "C002 must remain eight policies and zero instances")
    if admin_contract.get("invariants", {}).get("mass_provenance", {}).get("methods") != ["MANUFACTURER_STATED", "MEASURED", "CALCULATED"]:
        add("C002_MASS_METHOD_REGRESSION", "C002 Mass methods must remain exact and SUPPLIER_STATED must not be promoted")
    if candidate_contract.get("founder_evidence_packet", {}).get("criterion_order") != EXPECTED_CRITERIA:
        add("C002_CRITERIA_REGRESSION", "C002 nine criteria/order must remain exact")
    matrix = c003_r3.get("valid_combination_evidence_matrix", {})
    if matrix.get("confirmed_valid_count") != 216 or matrix.get("persisted_expanded_tuple_rows") is not False:
        add("C003_R3_REGRESSION", "C003-R3 must remain 216 evidence positions without persisted Cartesian rows")

    entities = load_yaml(safe_path(PRODUCT_ENTITIES_PATH, "Product entities"))
    pd03a = require_mapping(load_yaml(safe_path(PD03A_PATH, "PD03A registry")), "PD03A registry")
    rows = list(entities) if isinstance(entities, list) else []
    rows.extend(pd03a.get("entities", []) if isinstance(pd03a.get("entities"), list) else [])
    if any(isinstance(row, dict) and row.get("entity_type") == "SKU" for row in rows):
        add("SKU_REGRESSION", "canonical SKU count must remain zero")


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
        add("REGISTRY_DIGEST", "C005 registry differs from the independently reviewed package")
    if value.get("starting_main_sha") != EXPECTED_MAIN or value.get("mission_id") != "C005":
        add("MISSION_ANCHOR", "C005 mission and starting main must remain exact")

    manifest = value.get("source_manifest", {})
    sources = manifest.get("sources", []) if isinstance(manifest, dict) else []
    if manifest.get("channel_id") != "C0BNHRRTE9F" or manifest.get("founder_user_id") != "U0BNFS43TBL" or manifest.get("source_count") != 5:
        add("SOURCE_MANIFEST", "C005 source manifest must bind exact channel, Founder and five messages")
    if [item.get("source_id") for item in sources if isinstance(item, dict)] != EXPECTED_SOURCE_IDS:
        add("SOURCE_ORDER", "C005 sources must retain exact order")
    if [item.get("message_ts") for item in sources if isinstance(item, dict)] != EXPECTED_SOURCE_TS:
        add("SOURCE_TIMESTAMP", "C005 sources must bind exact Slack timestamps")
    if sources != EXPECTED_SOURCES:
        add("SOURCE_OBJECT_EXACTNESS", "every source must bind its exact locator, role, capture time, class, temporal role and title")
    if any(item.get("thread_complete") is not True or item.get("reply_count") != 0 for item in sources if isinstance(item, dict)):
        add("SOURCE_COMPLETENESS", "every C005 Slack source must be complete with zero replies")
    if any(item.get("evidence_classification") != "FOUNDER_CONFIRMED" for item in sources[1:] if isinstance(item, dict)):
        add("SOURCE_CLASSIFICATION", "all four evidence sources must remain Founder-confirmed")

    if value.get("authority_effects") != EXPECTED_AUTHORITY:
        add("AUTHORITY_EFFECT", "C005 grants only evidence reconciliation and readiness re-evaluation")

    records = value.get("evidence_records", [])
    record_ids = [item.get("evidence_id") for item in records if isinstance(item, dict)]
    if record_ids != [f"C005-EVID-{index:03d}" for index in range(1, 18)]:
        add("EVIDENCE_ORDER", "C005 evidence IDs and sequence must be exact")
    if [item.get("sequence") for item in records if isinstance(item, dict)] != list(range(1, 18)):
        add("EVIDENCE_SEQUENCE", "C005 evidence sequence must be exact")
    if [item.get("evidence_classification") for item in records if isinstance(item, dict)] != EXPECTED_CLASSIFICATIONS:
        add("EVIDENCE_CLASSIFICATION", "C005 evidence classification order must be 14 Founder-confirmed and three proposals")
    if [item.get("temporal_role") for item in records if isinstance(item, dict)] != EXPECTED_TEMPORAL:
        add("EVIDENCE_TEMPORAL", "C005 current/future temporal classification must remain exact")
    source_ids = set(EXPECTED_SOURCE_IDS[1:])
    if any(item.get("source_id") not in source_ids for item in records if isinstance(item, dict)):
        add("EVIDENCE_SOURCE_BINDING", "evidence records may bind only exact Founder evidence sources")
    bindings = [
        (item.get("source_id"), item.get("evidence_classification"), item.get("temporal_role"), item.get("domain"), item.get("canonical_owner"), item.get("disposition"))
        for item in records if isinstance(item, dict)
    ]
    if bindings != EXPECTED_RECORD_BINDINGS:
        add("EVIDENCE_RECORD_BINDING", "each evidence record must retain exact source, class, temporal role, domain, owner and disposition")
    if any(item.get("promotion_effect") is not False or item.get("implementation_authority") is not False for item in records if isinstance(item, dict)):
        add("EVIDENCE_PROMOTION", "every C005 evidence record must remain evidence-only")
    counts = Counter(item.get("evidence_classification") for item in records if isinstance(item, dict))
    temporal_counts = Counter(item.get("temporal_role") for item in records if isinstance(item, dict))
    summary = value.get("classification_summary", {})
    if summary != {
        "total_record_count": 17,
        "founder_confirmed_count": counts.get("FOUNDER_CONFIRMED", 0),
        "architecture_proposal_count": counts.get("ARCHITECTURE_PROPOSAL", 0),
        "external_observation_count": counts.get("EXTERNAL_OBSERVATION", 0),
        "current_intent_count": temporal_counts.get("CURRENT_INTENT", 0),
        "future_capability_count": temporal_counts.get("FUTURE_CAPABILITY", 0),
        "planning_only_count": temporal_counts.get("PLANNING_ONLY", 0),
        "historical_noncurrent_count": temporal_counts.get("HISTORICAL_NONCURRENT", 0),
    }:
        add("CLASSIFICATION_SUMMARY", "classification summary must be derived exactly from 17 records")

    text_by_id = {item.get("evidence_id"): str(item.get("statement", "")) for item in records if isinstance(item, dict)}
    required_phrases = {
        "C005-EVID-001": ["no hard mandatory margin floor"],
        "C005-EVID-002": ["never a bundle", "Availability fact"],
        "C005-EVID-003": ["not a supplier commitment", "Availability assertion"],
        "C005-EVID-004": ["rights", "remains missing"],
        "C005-EVID-006": ["0.45, 0.50, 0.55 and 0.60", "natural is mainly 6 m", "gold mainly 3 m"],
        "C005-EVID-007": ["source channel", "no automatic"],
        "C005-EVID-009": ["fixed and percentage", "arbitrary rounding step", "without second approval", "editable/cancellable"],
        "C005-EVID-010": ["ordinary, reseller/partner, wholesale and special/private", "«قیمت برای شما»", "percentage/savings badge", "creates no customer record"],
        "C005-EVID-011": ["multi-tier-ready", "promote/demote", "extend/cancel"],
        "C005-EVID-012": ["purchases, referrals, on-time payment", "permanent, annual", "in-account plus SMS", "No Phase-1 activation"],
        "C005-EVID-013": ["load and distance", "Reservation duration is operator-defined", "update price before payment"],
        "C005-EVID-014": ["before/after history", "revised, cancelled or converted", "create no Customer or Order objects"],
    }
    for record_id, phrases in required_phrases.items():
        if any(phrase not in text_by_id.get(record_id, "") for phrase in phrases):
            add("EVIDENCE_GUARDRAIL", f"{record_id} must preserve its fail-closed guardrail wording")

    readiness = value.get("c002_readiness_reevaluation", {})
    previous = readiness.get("previous", {}) if isinstance(readiness, dict) else {}
    criteria = readiness.get("criteria", []) if isinstance(readiness, dict) else []
    if previous.get("state_vector") != EXPECTED_PREVIOUS_STATES or previous.get("readiness") != "NOT_READY" or previous.get("resolved_count") != 0:
        add("PREVIOUS_READINESS", "C003-R3 previous 0/9 readiness must remain exact")
    if [item.get("criterion_code") for item in criteria if isinstance(item, dict)] != EXPECTED_CRITERIA:
        add("CRITERION_ORDER", "all nine C002 criteria must be re-evaluated in canonical order")
    if [item.get("previous_state") for item in criteria if isinstance(item, dict)] != EXPECTED_PREVIOUS_STATES:
        add("CRITERION_PREVIOUS_STATE", "each criterion must preserve its exact previous state")
    if [item.get("evidence_state") for item in criteria if isinstance(item, dict)] != EXPECTED_NEW_STATES:
        add("CRITERION_NEW_STATE", "C005 new C002 evidence-state vector must remain exact")
    if [item.get("reviewable") for item in criteria if isinstance(item, dict)] != EXPECTED_REVIEWABLE:
        add("CRITERION_REVIEWABLE", "reviewable is a separate exact six-item planning view, not a C002 evidence state")
    known = known_evidence_codes() | set(record_ids)
    for index, item in enumerate(criteria, start=1):
        if not isinstance(item, dict):
            continue
        code = item.get("criterion_code")
        refs = item.get("evidence_record_refs", [])
        gaps = item.get("gap_record_refs", [])
        supplementary = item.get("supplementary_planning_refs", [])
        components = item.get("component_states", [])
        if item.get("sequence") != index or item.get("status") != "OPEN_BLOCKING" or item.get("blocking") is not True:
            add("CRITERION_STATUS", f"criterion {index} must remain ordered and OPEN_BLOCKING")
        if item.get("promotion_effect") is not False:
            add("CRITERION_PROMOTION", f"{code} cannot create a promotion effect")
        if refs != EXPECTED_EVIDENCE_REFS.get(code) or gaps != EXPECTED_GAP_REFS.get(code):
            add("CRITERION_SOURCE_BINDING", f"{code} must retain exact evidence and gap references")
        if supplementary != EXPECTED_SUPPLEMENTARY_REFS.get(code):
            add("SUPPLEMENTARY_PLANNING_REF", f"{code} must retain exact non-verifying planning references")
        if components != EXPECTED_COMPONENT_STATES.get(code):
            add("PHOTO_COMPONENT_STATE", f"{code} must retain exact Photo Asset versus Text Content Strategy substates")
        for ref in supplementary:
            try:
                safe_path(Path(ref), f"{code} supplementary planning reference")
            except ValidationConfigurationError:
                add("SUPPLEMENTARY_PLANNING_REF", f"{code} supplementary planning reference is unsafe or missing")
        if any(ref not in known for ref in refs + gaps):
            add("CRITERION_UNKNOWN_REF", f"{code} references unknown evidence")
        if item.get("evidence_state") == "MISSING" and refs:
            add("MISSING_STATE_REF", f"{code} cannot cite submitted evidence while MISSING")
        if item.get("evidence_state") == "SUBMITTED" and not refs:
            add("SUBMITTED_STATE_REF", f"{code} requires submitted evidence references")
    if readiness.get("totals") != EXPECTED_TOTALS or readiness.get("readiness") != "NOT_READY" or readiness.get("candidate_registry_count") != 0:
        add("READINESS_TOTALS", "C005 must remain 0/9 NOT_READY with 8 SUBMITTED, 1 MISSING and 9 OPEN_BLOCKING")

    mass = value.get("mass_and_supply_reconciliation", {})
    expected_mass = {
        "canonical_mass_owner": "C002_MASS_PROVENANCE",
        "current_numeric_mass_observation_count": 0,
        "current_supply_intake_record_count": 0,
        "mass_lifecycle_states": ["CURRENT", "NEXT_PENDING", "HISTORICAL"],
        "allowed_transition": "NEXT_PENDING_TO_CURRENT_BY_OPERATOR_AND_PRIOR_CURRENT_TO_HISTORICAL",
        "supplier_statement_is_source_channel_only": True,
        "approved_c002_mass_methods": ["MANUFACTURER_STATED", "MEASURED", "CALCULATED"],
        "supplier_stated_method_extension_allowed": False,
        "operator_promotion_required": True,
        "automatic_mass_switch_allowed": False,
        "no_numeric_mass_value_recorded": True,
        "supply_business_intent_creates_availability": False,
    }
    if mass != expected_mass:
        add("MASS_SUPPLY_BOUNDARY", "Mass/Supply must remain zero-population evidence-only under the C002 owner")

    commercial = value.get("commercial_requirements_reconciliation", {})
    if any(commercial.get(key) != 0 for key in ["current_price_value_count", "customer_object_count", "order_object_count", "active_vip_entitlement_count", "active_loyalty_ledger_count"]):
        add("COMMERCIAL_OBJECT_POPULATION", "C005 cannot create price/customer/order/VIP/loyalty objects")
    if commercial.get("price_engine_created") is not False or commercial.get("implementation_created") is not False:
        add("COMMERCIAL_IMPLEMENTATION", "C005 records requirements only and cannot create implementation")

    path = value.get("shortest_remaining_evidence_path", [])
    if [item.get("priority") for item in path if isinstance(item, dict)] != [1, 2, 3, 4, 5, 6]:
        add("EVIDENCE_PATH_ORDER", "shortest remaining evidence path must be deterministically ranked")
    expected_rankings = [
        ("TWO_CRITERIA", "MEDIUM", "LOW", "SHORT", []),
        ("SIX_CRITERIA", "LOW", "NONE", "SHORT", []),
        ("ONE_CRITERION", "MEDIUM", "LOW", "MEDIUM", []),
        ("ONE_CRITERION", "MEDIUM", "MEDIUM", "MEDIUM", ["Independent C002 Product Data Completeness review"]),
        ("CONDITIONAL", "MEDIUM", "LOW", "MEDIUM", ["Independent SEO and Buyer Intent review remains blocking"]),
        ("NON_CRITERION_FUTURE_INPUT", "MEDIUM", "LOW", "MEDIUM", []),
    ]
    actual_rankings = [
        (item.get("blocking_impact"), item.get("evidence_cost"), item.get("founder_effort"), item.get("estimated_time"), item.get("dependencies"))
        for item in path if isinstance(item, dict)
    ]
    if actual_rankings != expected_rankings:
        add("EVIDENCE_PATH_RANKING", "remaining evidence path must preserve exact impact, cost, Founder effort, time and dependencies")
    if len(path) != 6 or "canonical Product and Variant Rules promotion" not in str(path[3].get("evidence_action", "")):
        add("EVIDENCE_PATH_PROMOTION_GATE", "Product Data Completeness requires a separately authorized canonical Product/Variant promotion gate")
    if any(item.get("authority_created") is not False for item in path if isinstance(item, dict)):
        add("EVIDENCE_PATH_AUTHORITY", "remaining evidence actions create no authority")

    anchors = value.get("regression_anchors", {})
    if anchors.get("commerce_state") != "INQUIRY_ONLY" or anchors.get("runtime_authority") != "NONE" or anchors.get("production_authority") != "NONE":
        add("RUNTIME_COMMERCE_REGRESSION", "Commerce must remain INQUIRY_ONLY with no Runtime/Production authority")
    if anchors.get("c1_t03_state") != "FROZEN_AT_PROTECTED_ARCHITECTURE_BOUNDARY":
        add("C1_T03_REGRESSION", "C1-T03 must remain frozen")

    forbidden_keys = {
        "products", "skus", "availability_records", "stock_records", "price_values", "mass_observations",
        "supply_records", "customers", "orders", "vip_entitlements", "loyalty_ledgers", "runtime_objects",
    }

    def scan(node: Any, path_label: str) -> None:
        if isinstance(node, dict):
            for key, child in node.items():
                if key in forbidden_keys:
                    add("FORBIDDEN_POPULATION_KEY", f"{path_label}/{key} is prohibited in C005")
                scan(child, f"{path_label}/{key}")
        elif isinstance(node, list):
            for index, child in enumerate(node):
                scan(child, f"{path_label}/{index}")

    scan(value, "<root>")
    validate_dependency_pins(add, contract)
    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    args = parser.parse_args()
    try:
        schema_validator, contract = load_validator()
        registry = load_yaml(safe_path(Path(args.registry), "C005 registry"))
        issues = validate_registry(registry, schema_validator, contract)
    except (ValidationConfigurationError, ValueError, TypeError) as exc:
        print(f"[CONFIGURATION] {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print("C005 Founder evidence and C002 readiness re-evaluation validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
