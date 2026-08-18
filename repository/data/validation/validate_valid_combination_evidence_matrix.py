#!/usr/bin/env python3
"""Offline validator for C003-R2 Founder evidence completion and tuple review planning."""

from __future__ import annotations

import argparse
from datetime import datetime
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
import validate_founder_product_commerce_checkpoint03 as c003r1


CONTRACT_PATH = ROOT / "repository/data/contracts/valid-combination-evidence-matrix.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/valid-combination-evidence-matrix.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c003r2/201-51-founder-evidence-completion.yaml"
C002_CANDIDATE_CONTRACT_PATH = ROOT / "repository/data/contracts/commercial-pilot-candidate.contract.yaml"
C002_CANDIDATE_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
C002_ADMIN_CONTRACT_PATH = ROOT / "repository/data/contracts/product-administration-policy.contract.yaml"
C002_ADMIN_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c002/product-administration-policies.yaml"
PRODUCT_ENTITIES_PATH = ROOT / "repository/data/registries/product-entities.yaml"
PD03A_PATH = ROOT / "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml"

# Pinned only after independent review of the final semantic objects.
EXPECTED_CONTRACT_DIGEST = "f4d9cddaf1ad94ffe2ac863d61ddcd5cb7babc4b85d20b1424fea4697f41c194"
EXPECTED_REGISTRY_DIGEST = "880afc790a44863ae6a44ba58539b189348d5adb2550fd0d89c63877c78cc24b"

EXPECTED_BRANDS = ["Sumwin", "Sansco", "Goldsco", "King", "StoneLand", "SUS"]
EXPECTED_THICKNESSES = [
    "0.45", "0.50", "0.55", "0.60", "0.70", "0.80",
    "0.90", "1.00", "1.10", "1.20", "1.50", "2.00",
]
EXPECTED_GROUPS = [
    ("STEEL_NATURAL_GLOSSY", "6.00"),
    ("GOLD_GLOSSY", "3.00"),
    ("GOLD_GLOSSY", "6.00"),
]
EXPECTED_CRITERIA = [
    "DEMAND_SIGNAL", "SUPPLY_EVIDENCE", "GROSS_PROFIT_POTENTIAL", "REPEATABILITY",
    "PRODUCT_DATA_COMPLETENESS", "PHOTO_CONTENT_READINESS", "SEO_BUYER_INTENT",
    "OPERATIONAL_COMPLEXITY", "FULFILLMENT_RISK",
]
EXPECTED_STATES = [
    "SUBMITTED", "SUBMITTED", "MISSING", "MISSING", "SUBMITTED",
    "MISSING", "MISSING", "SUBMITTED", "SUBMITTED",
]
EXPECTED_THREADS = [
    ("CHECKPOINT_03", "1786996639.277979", 4),
    ("FOUNDER_DISCOVERY_SESSION_01", "1786929259.157699", 9),
    ("IDEA_VAULT_RELEVANT_DOMAINS", "1786970361.696939", 4),
]
EXPECTED_ROW_SOURCES = [
    "C003R1-CP03-026", "C003R1-CP03-027", "C003R1-CP03-028",
    "C003R1-CP03-029", "C003R1-CP03-030",
]
EXPECTED_KNOWN_SOURCES = [
    "C003R1-CP03-017", "C003R1-CP03-026", "C003R1-CP03-027", "C003R1-CP03-028", "C003R1-CP03-029",
    "C003R1-CP03-030", "C003R1-CP03-032", "C003R1-CP03-033", "C003R1-CP03-034",
    "C003R1-CP03-036", "C003R1-CP03-039",
]
EXPECTED_HISTORICAL_MASS = ["3.500", "3.600", "3.620", "3.650", "3.680", "3.700"]
EXPECTED_C002_MASS_METHODS = ["MANUFACTURER_STATED", "MEASURED", "CALCULATED"]
EXPECTED_EVIDENCE_REFS = {
    "DEMAND_SIGNAL": ["C003-DISC-011", "C003-DISC-017", "C003-DISC-018"],
    "SUPPLY_EVIDENCE": ["C003R1-CP03-001", "C003R1-CP03-002", "C003R1-CP03-003"],
    "GROSS_PROFIT_POTENTIAL": [],
    "REPEATABILITY": [],
    "PRODUCT_DATA_COMPLETENESS": ["C003R1-CP03-026", "C003R1-CP03-027", "C003R1-CP03-028", "C003R1-CP03-030", "C003R1-CP03-031"],
    "PHOTO_CONTENT_READINESS": [],
    "SEO_BUYER_INTENT": [],
    "OPERATIONAL_COMPLEXITY": ["C003R1-CP03-032", "C003R1-CP03-034", "C003R1-CP03-041", "C003R1-CP03-053"],
    "FULFILLMENT_RISK": ["C003R1-CP03-007", "C003R1-CP03-008", "C003R1-CP03-041", "C003R1-CP03-042", "C003R1-CP03-043"],
}
EXPECTED_AUTHORITY = {
    "candidate_population": False,
    "product_population": False,
    "controlled_value_promotion": False,
    "valid_tuple_promotion": False,
    "sku_assignment": False,
    "availability_or_stock_claim": False,
    "current_or_public_price": False,
    "commerce_activation": False,
    "payment_activation": False,
    "wordpress_woocommerce_mutation": False,
    "runtime_staging_production": False,
    "deployment": False,
    "c1_t03_repair": False,
    "c003_a_start": False,
    "c003_b_start": False,
    "merge": False,
    "successor_mission": False,
}
EXPECTED_SELECTION_EFFECTS = {
    "candidate_registry_population": False,
    "product_state": "NOT_CREATED",
    "sku_state": "NOT_ASSIGNED",
    "availability_state": "NOT_ASSERTED",
    "price_state": "NO_CURRENT_OR_PUBLIC_PRICE_FACT",
    "commerce_state": "INQUIRY_ONLY",
    "runtime_state": "NONE",
    "production_state": "NONE",
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


def parse_rfc3339(value: Any, label: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError(f"{label} must be an RFC3339 string")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{label} must be a valid RFC3339 timestamp") from exc


def validate_answer_semantics(group: Any, answer_evidence: Any) -> list[str]:
    """Validate future answer mechanics without granting answer-capture authority."""
    issues: list[str] = []
    if not isinstance(group, dict):
        return ["[QUESTION_SEMANTICS] group must be an object"]
    supported = group.get("supported_thicknesses_mm", [])
    invalid = group.get("invalid_thicknesses_mm", [])
    not_applicable = group.get("not_applicable_thicknesses_mm", [])
    collections = [supported, invalid, not_applicable]
    if not all(isinstance(items, list) for items in collections):
        return ["[QUESTION_SEMANTICS] answer state sets must be arrays"]
    sets = [set(items) for items in collections]
    for items, item_set in zip(collections, sets):
        if items != [thickness for thickness in EXPECTED_THICKNESSES if thickness in item_set]:
            issues.append("[QUESTION_STATE_ORDER] every answer-state set must follow canonical Thickness order")
    if any(sets[left] & sets[right] for left, right in [(0, 1), (0, 2), (1, 2)]):
        issues.append("[QUESTION_STATE_OVERLAP] valid, invalid and not-applicable thickness sets must be disjoint")
    if any(item not in EXPECTED_THICKNESSES for items in collections for item in items):
        issues.append("[QUESTION_UNKNOWN_THICKNESS] answer contains a thickness outside the exact Founder list")

    mode = group.get("answer_mode")
    state = group.get("evidence_state")
    all_values = set(EXPECTED_THICKNESSES)
    union = sets[0] | sets[1] | sets[2]
    evidence_required = mode != "UNANSWERED"
    if mode == "UNANSWERED":
        if union or state != "UNKNOWN" or answer_evidence is not None:
            issues.append("[QUESTION_UNANSWERED_SEMANTICS] unanswered groups must remain empty, UNKNOWN and unbound")
    elif mode == "KEEP_UNKNOWN":
        if union or state != "UNKNOWN":
            issues.append("[QUESTION_KEEP_UNKNOWN_SEMANTICS] KEEP_UNKNOWN cannot resolve any listed thickness")
    elif mode == "ALL_LISTED_CONFIRMED_VALID":
        if supported != EXPECTED_THICKNESSES or invalid or not_applicable or state != "CONFIRMED_VALID":
            issues.append("[QUESTION_ALL_VALID_SEMANTICS] ALL_LISTED_CONFIRMED_VALID must bind every listed thickness only to CONFIRMED_VALID")
    elif mode == "ALL_LISTED_CONFIRMED_INVALID":
        if invalid != EXPECTED_THICKNESSES or supported or not_applicable or state != "CONFIRMED_INVALID":
            issues.append("[QUESTION_ALL_INVALID_SEMANTICS] ALL_LISTED_CONFIRMED_INVALID must bind every listed thickness only to CONFIRMED_INVALID")
    elif mode == "EXPLICIT_STATE_SETS":
        if not union:
            issues.append("[QUESTION_EXPLICIT_EMPTY] EXPLICIT_STATE_SETS must resolve at least one listed thickness")
        if union - all_values:
            issues.append("[QUESTION_UNKNOWN_THICKNESS] explicit state sets contain an unknown thickness")
        expected_summary = (
            "CONFIRMED_VALID" if supported == EXPECTED_THICKNESSES and not invalid and not not_applicable
            else "CONFIRMED_INVALID" if invalid == EXPECTED_THICKNESSES and not supported and not not_applicable
            else "NOT_APPLICABLE" if not_applicable == EXPECTED_THICKNESSES and not supported and not invalid
            else "UNKNOWN"
        )
        if state != expected_summary:
            issues.append("[QUESTION_EXPLICIT_SUMMARY] explicit-set summary must be uniform only when all twelve thicknesses share one state; otherwise it remains UNKNOWN")
        # Every listed thickness omitted from the three sets remains UNKNOWN by definition.
    else:
        issues.append("[QUESTION_MODE] answer mode is not in the closed contract vocabulary")

    if evidence_required:
        if not isinstance(answer_evidence, dict):
            issues.append("[QUESTION_EVIDENCE_BINDING] every recorded Founder answer requires a verified evidence binding")
        else:
            expected_literals = {
                "evidence_classification": "FOUNDER_CONFIRMED",
                "founder_confirmed": True,
                "review_status": "VERIFIED",
                "promotion_effect": False,
            }
            if any(answer_evidence.get(key) != expected for key, expected in expected_literals.items()):
                issues.append("[QUESTION_EVIDENCE_BINDING] answer evidence must be Founder-confirmed, verified and evidence-only")
            try:
                if parse_rfc3339(answer_evidence.get("captured_at"), "captured_at") > parse_rfc3339(answer_evidence.get("reviewed_at"), "reviewed_at"):
                    issues.append("[QUESTION_EVIDENCE_CHRONOLOGY] answer review cannot precede capture")
            except ValueError:
                issues.append("[QUESTION_EVIDENCE_CHRONOLOGY] answer evidence timestamps must be valid")
    return sorted(set(issues))


def validate_future_mass_observation(value: Any) -> list[str]:
    issues: list[str] = []
    if not isinstance(value, dict):
        return ["[MASS_ITEM] mass observation must be an object"]
    context = value.get("variant_context", {})
    missing = set(context.get("missing_context_fields", [])) if isinstance(context, dict) else set()
    for field in ["grade", "diameter_mm", "brand", "thickness_mm", "appearance", "length_m"]:
        is_missing = isinstance(context, dict) and context.get(field) is None
        if is_missing != (field in missing):
            issues.append(f"[MASS_CONTEXT_MISSINGNESS] {field} nullability must match missing_context_fields")
    if value.get("previous_observation_reference") == value.get("observation_id"):
        issues.append("[MASS_HISTORY_SELF_REFERENCE] observation cannot reference itself")
    if value.get("confirmed_by_operator") is True and value.get("operator_reference") is None:
        issues.append("[MASS_OPERATOR_BINDING] confirmed observation requires an operator reference")
    proposed_method = value.get("proposed_c002_mass_method")
    if proposed_method is not None and proposed_method not in EXPECTED_C002_MASS_METHODS:
        issues.append("[MASS_METHOD_OWNER] intake cannot extend C002 Mass Provenance method vocabulary")
    if value.get("source_channel") == "SUPPLIER_COMMUNICATION" and proposed_method is not None:
        issues.append("[MASS_SUPPLIER_METHOD_INFERENCE] supplier communication cannot be inferred as an approved C002 Mass method")
    if value.get("c002_method_validation_state") != "UNVALIDATED_C002_INTAKE_ONLY" or value.get("supplier_stated_method_allowed") is not False:
        issues.append("[MASS_METHOD_BOUNDARY] method mapping remains unvalidated and SUPPLIER_STATED remains separately gated")
    if value.get("canonical_or_variant_effect") is not False:
        issues.append("[MASS_EFFECT] observation cannot create canonical or Variant truth")
    return sorted(set(issues))


def validate_future_supply_record(value: Any) -> list[str]:
    issues: list[str] = []
    if not isinstance(value, dict):
        return ["[SUPPLY_ITEM] supply evidence must be an object"]
    try:
        confirmed = parse_rfc3339(value.get("confirmation_timestamp"), "confirmation_timestamp")
        valid_from = parse_rfc3339(value.get("valid_from"), "valid_from")
        valid_until = parse_rfc3339(value.get("valid_until"), "valid_until")
        reviewed = parse_rfc3339(value.get("reviewed_at"), "reviewed_at")
        if valid_from > valid_until:
            issues.append("[SUPPLY_VALIDITY_WINDOW] valid_from must not follow valid_until")
        if confirmed > reviewed:
            issues.append("[SUPPLY_REVIEW_CHRONOLOGY] review cannot precede confirmation")
    except ValueError:
        issues.append("[SUPPLY_TIMESTAMP] supply timestamps must be valid RFC3339 values")
    if value.get("availability_effect") is not False or value.get("stock_effect") is not False:
        issues.append("[SUPPLY_EFFECT] supply evidence cannot create Availability or stock")
    scope = value.get("tuple_scope", {})
    if not isinstance(scope, dict) or scope.get("representation") != "EXACT_TUPLE_LIST" or scope.get("cartesian_generation_allowed") is not False or scope.get("omitted_tuple_state") != "UNKNOWN":
        issues.append("[SUPPLY_SCOPE] supply evidence must bind an exact tuple list; omitted tuples remain UNKNOWN and Cartesian generation is forbidden")
    tuples = scope.get("tuples", []) if isinstance(scope, dict) else []
    if not isinstance(tuples, list) or not tuples:
        issues.append("[SUPPLY_TUPLE_UNIVERSE] exact supply scope must contain at least one tuple")
    tuple_keys: list[tuple[Any, Any, Any, Any]] = []
    for item in tuples if isinstance(tuples, list) else []:
        if not isinstance(item, dict):
            issues.append("[SUPPLY_TUPLE_UNIVERSE] every supply scope member must be an exact tuple object")
            continue
        key = (item.get("brand"), item.get("thickness_mm"), item.get("appearance"), item.get("length_m"))
        tuple_keys.append(key)
        if key[0] not in EXPECTED_BRANDS or key[1] not in EXPECTED_THICKNESSES or (key[2], key[3]) not in EXPECTED_GROUPS:
            issues.append("[SUPPLY_TUPLE_UNIVERSE] supply scope tuple falls outside the exact 216-tuple Founder review universe")
    if len(tuple_keys) != len(set(tuple_keys)):
        issues.append("[SUPPLY_TUPLE_DUPLICATE] exact supply tuple scope cannot contain duplicates")
    sortable = all(
        brand in EXPECTED_BRANDS and thickness in EXPECTED_THICKNESSES and (appearance, length) in EXPECTED_GROUPS
        for brand, thickness, appearance, length in tuple_keys
    )
    if sortable:
        expected_order = sorted(
            tuple_keys,
            key=lambda item: (
                EXPECTED_BRANDS.index(item[0]),
                EXPECTED_THICKNESSES.index(item[1]),
                EXPECTED_GROUPS.index((item[2], item[3])),
            ),
        )
        if tuple_keys != expected_order:
            issues.append("[SUPPLY_TUPLE_ORDER] exact supply tuples must follow Brand, Thickness, appearance-length group order")
    if not isinstance(value.get("evidence_source_locator"), str) or not value.get("evidence_source_locator"):
        issues.append("[SUPPLY_SOURCE_BINDING] supply evidence requires an inspectable protected source locator")
    if value.get("evidence_classification") not in {"SUPPLIER_DOCUMENT", "OPERATIONS_EVIDENCE"} or value.get("temporal_role") not in {"CURRENT_OBSERVATION", "HISTORICAL_NONCURRENT"}:
        issues.append("[SUPPLY_CLASS_TEMPORAL] supply source classification and temporal role must be explicit")
    return sorted(set(issues))


def load_validator(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[Any, dict[str, Any]]:
    contract = require_mapping(load_yaml(safe_path(contract_path, "C003-R2 contract")), "C003-R2 contract")
    if EXPECTED_CONTRACT_DIGEST != "TO_BE_FINALIZED" and semantic_digest(contract) != EXPECTED_CONTRACT_DIGEST:
        raise ValidationConfigurationError("C003-R2 contract literal policy differs")
    schema = require_mapping(load_json(safe_path(schema_path, "C003-R2 schema")), "C003-R2 schema")
    schema_issues = audit_schema(schema)
    if schema_issues:
        raise ValidationConfigurationError(schema_issues[0])
    return validate_schema(schema), contract


def base_evidence_codes() -> tuple[set[str], set[str]]:
    r1_registry = require_mapping(load_yaml(c003r1.REGISTRY_PATH), "C003-R1 registry")
    r1_codes = {
        item.get("decision_code")
        for item in r1_registry.get("evidence_delta", [])
        if isinstance(item, dict) and isinstance(item.get("decision_code"), str)
    }
    base_registry = require_mapping(load_yaml(c003r1.BASE_REGISTRY_PATH), "C003 base registry")
    base_codes = {
        item.get("decision_code")
        for item in base_registry.get("evidence_records", [])
        if isinstance(item, dict) and isinstance(item.get("decision_code"), str)
    }
    return r1_codes, base_codes


def validate_regression_anchors(add: Any, contract: dict[str, Any], value: dict[str, Any]) -> None:
    r1_validator, r1_contract = c003r1.load_validator()
    r1_registry = require_mapping(load_yaml(c003r1.REGISTRY_PATH), "C003-R1 registry")
    r1_issues = c003r1.validate_registry(r1_registry, r1_validator, r1_contract)
    if r1_issues:
        add("C003_R1_REGRESSION", r1_issues[0])

    pins = contract.get("base_pins", {})
    live_digests = {
        "c003_r1_contract_semantic_sha256": semantic_digest(require_mapping(load_yaml(c003r1.CONTRACT_PATH), "C003-R1 contract")),
        "c003_r1_registry_semantic_sha256": semantic_digest(r1_registry),
        "c002_candidate_contract_semantic_sha256": semantic_digest(require_mapping(load_yaml(C002_CANDIDATE_CONTRACT_PATH), "C002 candidate contract")),
        "c002_candidate_registry_semantic_sha256": semantic_digest(require_mapping(load_yaml(C002_CANDIDATE_REGISTRY_PATH), "C002 candidate registry")),
        "c002_product_administration_contract_semantic_sha256": semantic_digest(require_mapping(load_yaml(C002_ADMIN_CONTRACT_PATH), "C002 administration contract")),
        "c002_product_administration_registry_semantic_sha256": semantic_digest(require_mapping(load_yaml(C002_ADMIN_REGISTRY_PATH), "C002 administration registry")),
    }
    if pins != live_digests:
        add("BASE_PIN_REGRESSION", "C003-R1 and C002 semantic pins must match immutable live owners")

    source_owner = value.get("source_manifest", {}).get("canonical_evidence_owner", {})
    if source_owner.get("contract_semantic_sha256") != live_digests["c003_r1_contract_semantic_sha256"] or source_owner.get("registry_semantic_sha256") != live_digests["c003_r1_registry_semantic_sha256"]:
        add("SOURCE_OWNER_PIN", "C003-R2 source owner must pin the exact C003-R1 package")

    candidate_registry = require_mapping(load_yaml(C002_CANDIDATE_REGISTRY_PATH), "C002 candidate registry")
    admin_contract = require_mapping(load_yaml(C002_ADMIN_CONTRACT_PATH), "C002 administration contract")
    admin_registry = require_mapping(load_yaml(C002_ADMIN_REGISTRY_PATH), "C002 administration registry")
    if candidate_registry.get("candidates") != []:
        add("C002_CANDIDATE_REGRESSION", "C002 canonical candidate registry must remain empty")
    if not isinstance(admin_registry.get("policies"), list) or len(admin_registry["policies"]) != 8:
        add("C002_POLICY_REGRESSION", "C002 must retain exactly eight policy definitions")
    if admin_registry.get("instances") != []:
        add("C002_INSTANCE_REGRESSION", "C002 policy instances must remain empty")
    live_methods = admin_contract.get("invariants", {}).get("mass_provenance", {}).get("methods")
    if live_methods != EXPECTED_C002_MASS_METHODS:
        add("C002_MASS_METHOD_REGRESSION", "C002 Mass Provenance must retain exactly MANUFACTURER_STATED, MEASURED and CALCULATED")
    base_registry = require_mapping(load_yaml(c003r1.BASE_REGISTRY_PATH), "C003 base registry")
    supplier_extension = next(
        (item for item in base_registry.get("evidence_records", []) if isinstance(item, dict) and item.get("decision_code") == "C003-DISC-035"),
        None,
    )
    if not isinstance(supplier_extension, dict) or supplier_extension.get("proposed_extension_state") != "PROPOSED_EXTENSION_REQUIRING_SEPARATE_REVIEW" or supplier_extension.get("requires_separate_contract_version") is not True:
        add("SUPPLIER_STATED_BOUNDARY_REGRESSION", "SUPPLIER_STATED must remain a separately reviewed proposed C002 extension")

    entities = load_yaml(PRODUCT_ENTITIES_PATH)
    pd03a = require_mapping(load_yaml(PD03A_PATH), "PD03A registry")
    all_entities = list(entities) if isinstance(entities, list) else []
    all_entities.extend(pd03a.get("entities", []) if isinstance(pd03a.get("entities"), list) else [])
    if any(isinstance(item, dict) and item.get("entity_type") == "SKU" for item in all_entities):
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
        add("REGISTRY_DIGEST", "C003-R2 registry differs from the independently reviewed package")
    mass_policy = contract.get("mass_evidence", {})
    if (
        mass_policy.get("canonical_owner") != "C002_MASS_PROVENANCE"
        or mass_policy.get("approved_c002_methods") != EXPECTED_C002_MASS_METHODS
        or mass_policy.get("source_channel_is_not_mass_method") is not True
        or mass_policy.get("supplier_stated_method_allowed") is not False
    ):
        add("MASS_CONTRACT_OWNER", "R2 Mass intake must reuse the exact C002 owner/method boundary without SUPPLIER_STATED promotion")

    mission = value.get("mission", {})
    if mission.get("starting_main_sha") != "91bddc43fd521a5548910d5087aad2f9d63e06f5" or mission.get("source_verified") is not True:
        add("MISSION_SOURCE", "Mission source and starting main must be exact")

    manifest = value.get("source_manifest", {})
    threads = manifest.get("verified_threads", []) if isinstance(manifest, dict) else []
    actual_threads = [
        (item.get("source_id"), item.get("parent_ts"), item.get("message_count"))
        for item in threads if isinstance(item, dict)
    ]
    if actual_threads != EXPECTED_THREADS or any(item.get("complete") is not True for item in threads if isinstance(item, dict)):
        add("SOURCE_MANIFEST", "Checkpoint, Discovery and relevant Idea Vault sources must be exact and complete")
    if manifest.get("copied_slack_ledger") is not False or manifest.get("external_market_research_used") is not False:
        add("SOURCE_BOUNDARY", "R2 must reuse C003-R1 and must not use external market research as Founder truth")

    packet = value.get("founder_evidence_completion_packet", {})
    known = packet.get("known_evidence", {}) if isinstance(packet, dict) else {}
    if known.get("brands") != EXPECTED_BRANDS:
        add("KNOWN_BRANDS", "known Founder brand evidence must remain exact")
    if known.get("thicknesses_mm") != EXPECTED_THICKNESSES:
        add("KNOWN_THICKNESSES", "known Founder thickness evidence must remain exact")
    if known.get("appearances") != ["STEEL_NATURAL_GLOSSY", "GOLD_GLOSSY"]:
        add("KNOWN_APPEARANCES", "known appearance evidence must remain exact")
    actual_appearance_lengths = [
        (item.get("appearance"), item.get("lengths_m"))
        for item in known.get("appearance_lengths", []) if isinstance(item, dict)
    ]
    if actual_appearance_lengths != [
        ("STEEL_NATURAL_GLOSSY", ["6.00"]),
        ("GOLD_GLOSSY", ["3.00", "6.00"]),
    ]:
        add("KNOWN_LENGTHS", "known appearance-length evidence must remain exact")
    if known.get("evidence_source_refs") != EXPECTED_KNOWN_SOURCES:
        add("KNOWN_SOURCE_BINDING", "known evidence must bind to exact C003-R1 decisions")
    historical_mass = known.get("historical_mass_examples", {})
    if (
        historical_mass.get("source_ref") != "C003-DISC-031"
        or historical_mass.get("values_kg") != EXPECTED_HISTORICAL_MASS
        or historical_mass.get("evidence_class") != "FOUNDER_CONFIRMED"
        or historical_mass.get("temporal_role") != "HISTORICAL_EXAMPLE_NONCURRENT"
        or historical_mass.get("current_intake_observation") is not False
    ):
        add("HISTORICAL_MASS_RECONCILIATION", "six historical Sumwin/51 mass examples must remain exact, noncurrent and excluded from bounded intake")
    if known.get("brand_appearance_claim_proves_complete_tuple") is not False:
        add("BRAND_APPEARANCE_BOUNDARY", "Brand/appearance evidence cannot prove complete tuples")

    matrix = value.get("valid_combination_evidence_matrix", {})
    rows = matrix.get("rows", []) if isinstance(matrix, dict) else []
    if not isinstance(rows, list) or len(rows) != 3:
        add("MATRIX_ROW_COUNT", "matrix must contain exactly three compressed rows")
        rows = rows if isinstance(rows, list) else []
    expanded: set[tuple[str, str, str, str]] = set()
    row_groups: list[tuple[Any, Any]] = []
    row_ids: list[Any] = []
    r1_codes, base_codes = base_evidence_codes()
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            continue
        row_ids.append(row.get("row_id"))
        if row.get("row_id") != f"c003r2row:{index:012x}":
            add("MATRIX_ROW_ORDER", f"matrix row {index} identity/order differs")
        brand_values = row.get("brand", {}).get("values", [])
        thickness_values = row.get("thickness", {}).get("values_mm", [])
        if brand_values != EXPECTED_BRANDS or thickness_values != EXPECTED_THICKNESSES:
            add("MATRIX_AXES", f"matrix row {index} must reference exact Brand and Thickness evidence")
        group = (row.get("appearance"), row.get("length_m"))
        row_groups.append(group)
        if row.get("evidence_state") != "UNKNOWN":
            add("UNKNOWN_PROMOTION", f"matrix row {index} cannot promote UNKNOWN")
        if row.get("evidence_source_refs") != EXPECTED_ROW_SOURCES or row.get("guardrail_source_refs") != ["C003R1-CP03-031"]:
            add("MATRIX_SOURCE_BINDING", f"matrix row {index} sources must be exact")
        if not set(row.get("evidence_source_refs", []) + row.get("guardrail_source_refs", [])).issubset(r1_codes):
            add("UNKNOWN_EVIDENCE_REF", f"matrix row {index} contains unknown C003-R1 evidence")
        if row.get("evidence_class") != "FOUNDER_CONFIRMED" or row.get("temporal_role") != "CURRENT_INTENT":
            add("CLASS_TEMPORAL_SEPARATION", f"matrix row {index} must preserve source class and temporal role")
        before = len(expanded)
        for brand in brand_values:
            for thickness in thickness_values:
                expanded.add((brand, thickness, str(row.get("appearance")), str(row.get("length_m"))))
        expected_added = len(brand_values) * len(thickness_values)
        if len(expanded) - before != expected_added:
            add("MATRIX_OVERLAP", f"matrix row {index} overlaps another compressed rule")
    if len(row_ids) != len(set(row_ids)):
        add("MATRIX_ID_COLLISION", "matrix row IDs must be unique")
    if row_groups != EXPECTED_GROUPS:
        add("MATRIX_GROUP_ORDER", "compressed matrix appearance-length groups must be exact")
    if len(expanded) != 216:
        add("UNKNOWN_TUPLE_COUNT", f"compressed UNKNOWN review universe must equal 216, got {len(expanded)}")
    expected_counts = {
        "compressed_row_count": 3,
        "expanded_review_universe_count": 216,
        "confirmed_valid_count": 0,
        "confirmed_invalid_count": 0,
        "unknown_count": 216,
        "not_applicable_count": 0,
        "inferred_tuple_count": 0,
    }
    if any(matrix.get(key) != expected for key, expected in expected_counts.items()):
        add("MATRIX_COUNTS", "matrix counts must preserve 216 UNKNOWN and zero inferred/confirmed tuples")
    if matrix.get("cartesian_truth_generation") is not False or matrix.get("persisted_expanded_tuple_rows") is not False:
        add("CARTESIAN_BOUNDARY", "matrix may count UNKNOWN review scope in memory but cannot persist Cartesian truth")

    plan = value.get("founder_question_compression_plan", {})
    review_items = plan.get("review_items", []) if isinstance(plan, dict) else []
    if not isinstance(review_items, list) or len(review_items) != 6:
        add("QUESTION_COUNT", "question plan must contain exactly six Brand-level review items")
        review_items = review_items if isinstance(review_items, list) else []
    question_ids: list[Any] = []
    for index, item in enumerate(review_items, start=1):
        if not isinstance(item, dict):
            continue
        question_ids.append(item.get("review_item_id"))
        if item.get("review_item_id") != f"c003r2question:{index:012x}" or item.get("brand") != EXPECTED_BRANDS[index - 1]:
            add("QUESTION_ORDER", f"Founder review item {index} identity/Brand differs")
        groups = item.get("groups", [])
        actual_groups = [(group.get("appearance"), group.get("length_m")) for group in groups if isinstance(group, dict)]
        if actual_groups != EXPECTED_GROUPS:
            add("QUESTION_GROUPS", f"Founder review item {index} must contain exact three groups")
        for group in groups if isinstance(groups, list) else []:
            if not isinstance(group, dict):
                continue
            for semantic_issue in validate_answer_semantics(group, item.get("answer_evidence")):
                issues.append(semantic_issue)
            if group.get("answer_mode") != "UNANSWERED" or group.get("evidence_state") != "UNKNOWN":
                add("QUESTION_PREANSWERED", f"Founder review item {index} must remain unanswered/UNKNOWN")
            if (
                group.get("supported_thicknesses_mm") != []
                or group.get("invalid_thicknesses_mm") != []
                or group.get("not_applicable_thicknesses_mm") != []
                or group.get("exception_notes") != []
                or item.get("answer_evidence") is not None
            ):
                add("QUESTION_PREPOPULATED", f"Founder review item {index} cannot contain inferred answers or exceptions")
    if len(question_ids) != len(set(question_ids)):
        add("QUESTION_ID_COLLISION", "Founder review item IDs must be unique")
    if plan.get("founder_review_item_count") != 6 or plan.get("maximum_tuple_resolution_per_answer") != 36 or plan.get("total_tuple_review_universe") != 216:
        add("QUESTION_COMPRESSION", "six answers must cover the 216-tuple review universe at up to 36 per Brand")
    if plan.get("answer_capture_authority") is not False or plan.get("unanswered_preserves_unknown") is not True:
        add("QUESTION_AUTHORITY", "worksheet cannot pre-authorize answers and unanswered tuples remain UNKNOWN")

    missing = value.get("missing_evidence_register", {})
    missing_items = missing.get("items", []) if isinstance(missing, dict) else []
    if not isinstance(missing_items, list) or len(missing_items) != 9:
        add("MISSING_EVIDENCE_COUNT", "missing evidence register must map all nine C002 criteria")
        missing_items = missing_items if isinstance(missing_items, list) else []
    actual_criteria = [item.get("criterion_code") for item in missing_items if isinstance(item, dict)]
    actual_states = [item.get("evidence_state") for item in missing_items if isinstance(item, dict)]
    if actual_criteria != EXPECTED_CRITERIA or actual_states != EXPECTED_STATES:
        add("MISSING_EVIDENCE_ORDER", "missing evidence register must preserve exact C002 criterion order/states")
    for index, item in enumerate(missing_items, start=1):
        if not isinstance(item, dict):
            continue
        if item.get("sequence") != index or item.get("status") != "OPEN_BLOCKING":
            add("MISSING_EVIDENCE_STATUS", f"missing evidence item {index} must remain ordered/open/blocking")
        refs = item.get("evidence_source_refs", [])
        if not set(refs).issubset(r1_codes | base_codes):
            add("MISSING_EVIDENCE_REF", f"missing evidence item {index} contains an unknown source")
        if item.get("evidence_state") == "MISSING" and refs:
            add("MISSING_STATE_REF", f"missing evidence item {index} cannot cite submitted evidence")
        if item.get("evidence_state") == "SUBMITTED" and not refs:
            add("SUBMITTED_STATE_REF", f"submitted evidence item {index} needs at least one source")
        if refs != EXPECTED_EVIDENCE_REFS.get(item.get("criterion_code")):
            add("CRITERION_SOURCE_BINDING", f"missing evidence item {index} must retain the exact criterion-specific source list")

    if contract.get("c002_evidence_source_bindings") != EXPECTED_EVIDENCE_REFS:
        add("CONTRACT_CRITERION_BINDING", "contract must pin every criterion to its exact ordered evidence-source list")

    mass = value.get("mass_evidence_intake", {})
    for observation in mass.get("observations", []) if isinstance(mass.get("observations"), list) else []:
        issues.extend(validate_future_mass_observation(observation))
    if mass.get("observations") != [] or mass.get("mass_observation_count") != 0:
        add("MASS_POPULATION", "mass intake must remain prepared and empty")
    if (
        mass.get("variant_identity") is not False
        or mass.get("canonical_mass_value_created") is not False
        or mass.get("population_authority") is not False
        or mass.get("historical_example_refs_excluded_from_current_intake") != ["C003-DISC-031"]
    ):
        add("MASS_BOUNDARY", "mass cannot become Variant identity or canonical value")
    supply = value.get("supply_evidence_intake", {})
    for record in supply.get("records", []) if isinstance(supply.get("records"), list) else []:
        issues.extend(validate_future_supply_record(record))
    if supply.get("records") != [] or supply.get("supply_evidence_record_count") != 0:
        add("SUPPLY_POPULATION", "supply intake must remain prepared and empty")
    if supply.get("creates_availability") is not False or supply.get("creates_stock_claim") is not False or supply.get("population_authority") is not False:
        add("SUPPLY_BOUNDARY", "supply evidence cannot create Availability or stock")

    readiness = value.get("c002_readiness", {})
    if readiness.get("criterion_order") != EXPECTED_CRITERIA or readiness.get("criterion_states") != EXPECTED_STATES:
        add("READINESS_ORDER", "C002 readiness order/states must remain exact")
    if readiness.get("resolved_count") != 0 or readiness.get("unresolved_count") != 9 or readiness.get("coverage") != "0/9" or readiness.get("readiness") != "NOT_READY":
        add("READINESS_PROMOTION", "C003-R2 cannot resolve or promote any C002 readiness criterion")
    if readiness.get("founder_selection_recorded") is not False:
        add("FOUNDER_SELECTION", "C003-R2 cannot record Founder Pilot selection")

    if value.get("selection_effects") != EXPECTED_SELECTION_EFFECTS:
        add("SELECTION_EFFECT", "selection effects must remain fail-closed and inactive")
    if value.get("authority_effects") != EXPECTED_AUTHORITY:
        add("ROOT_AUTHORITY_EFFECT", "all C003-R2 authority effects must remain false")

    validate_regression_anchors(add, contract, value)
    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    args = parser.parse_args()
    try:
        schema_validator, contract = load_validator()
        registry_path = safe_path(Path(args.registry), "C003-R2 registry")
        registry = load_yaml(registry_path)
        issues = validate_registry(registry, schema_validator, contract)
    except (ValidationConfigurationError, ValueError, TypeError) as exc:
        print(f"[CONFIGURATION] {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print("C003-R2 201/51 Founder evidence completion validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
