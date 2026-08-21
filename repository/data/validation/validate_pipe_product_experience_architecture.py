#!/usr/bin/env python3
"""Deterministic, offline validator for the C006 architecture-only package."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any, Callable

from validate_pd03a_pilot_prerequisite import (
    ROOT,
    ValidationConfigurationError,
    load_json,
    load_yaml,
    require_mapping,
    validate_schema,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/pipe-product-experience-architecture.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/pipe-product-experience-architecture.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c006/pipe-product-experience-architecture.yaml"

EXPECTED_CONTRACT_DIGEST = "131b2c79a3d017c65bac896e95e7a638164a77b821546e5217266f6d3829dcc0"
EXPECTED_SCHEMA_DIGEST = "9a9009c4431c097c062dcef81fad03fae51784ff466bb8cc5db6ed14237f79e3"
EXPECTED_REGISTRY_DIGEST = "5b5510af1b521daa7b2539007cab0681885f2bbc3eff4a75dde67cb38857ad8b"
EXPECTED_MAIN = "ea616b08ef2f4012afd011684dfe4e5c98cd8fcf"

EXPECTED_SOURCES = [
    ("C006_MOP_PARENT", 1, "1787086720.993949", "1787086720.993949", "THREAD_PARENT",
     "C006 MASTER ORCHESTRATION PLAN — SINGLE-PROMPT CODEX EXECUTION — 2026-08-18",
     "2026-08-19T00:28:40+03:30", 2),
    ("C006_MOP_PART_2", 2, "1787086738.441119", "1787086720.993949", "THREAD_REPLY",
     "C006-MOP-01 — PART 2 — AGENT TOPOLOGY & REASONING BUDGET",
     "2026-08-19T00:28:58+03:30", None),
    ("C006_MOP_PART_3", 3, "1787086759.886949", "1787086720.993949", "THREAD_REPLY",
     "C006-MOP-01 — PART 3 — INTERNAL EPICS, QUALITY GATES & FINAL HANDOFF",
     "2026-08-19T00:29:19+03:30", None),
    ("C006_PIPE_INFORMATION_MODEL", 4, "1787084095.125229", "1787084095.125229", "THREAD_PARENT",
     "PRODUCT DATA ENHANCEMENT CHECKPOINT — PIPE INFORMATION MODEL — 2026-08-18",
     "2026-08-18T23:44:55+03:30", 1),
    ("C006_PRODUCT_PAGE_ADDENDUM_A", 5, "1787084980.103649", "1787084095.125229", "THREAD_REPLY",
     "PRODUCT PAGE INTERACTION MODEL — ADDENDUM A — 2026-08-18",
     "2026-08-18T23:59:40+03:30", None),
]

ALLOWED_AUTHORITY = [
    "semantic_reconciliation", "projection_architecture", "owner_interface_definition",
    "documentation_contract_schema_validator_test", "branch_commit_push_non_draft_pr",
    "attributable_ci_repair",
]
DENIED_AUTHORITY = [
    "product_population", "product_value_population", "variant_population", "valid_tuple_promotion",
    "sku_population", "mass_observation_population", "mass_promotion", "supply_population",
    "availability_population", "stock_or_supplier_truth", "current_or_public_price",
    "pricing_activation", "media_asset_population", "knowledge_content_population",
    "seo_page_creation", "customer_crm_order_quote_population", "cart_checkout_payment",
    "public_pricing", "wordpress_woocommerce_mutation", "import_publication",
    "runtime_staging_production", "deployment", "competitor_asset_reuse", "c1_t03_repair",
    "merge", "branch_deletion", "successor_mission",
]
EXPECTED_DOMAINS = [
    "PRODUCT_IDENTITY", "ATTRIBUTE_DEFINITION", "VARIANT_RULE_SET", "MEASUREMENT",
    "BRAND_IDENTITY", "C002_BRAND_PROVENANCE", "MASS", "AVAILABILITY", "PRICING_AUTHORITY",
    "CUSTOMER_ORDER_UNIT_POLICY", "PRICING_BASIS_POLICY", "MEDIA", "KNOWLEDGE",
    "SERVICE_POLICY", "INQUIRY_CONTEXT", "SEO_INTENT", "WOOCOMMERCE",
]
EXPECTED_OWNERS = [
    "PRODUCT_CORE", "PRODUCT_ATTRIBUTE", "VARIANT_RULE_SET", "MEASUREMENT_FOUNDATION",
    "BRAND_IDENTITY", "C002_BRAND_PROVENANCE", "C002_MASS_PROVENANCE",
    "FUTURE_AVAILABILITY_EVIDENCE_CONTRACT", "PRICING_AUTHORITY", "CUSTOMER_ORDER_UNIT_POLICY",
    "PRICING_BASIS_POLICY", "FUTURE_MEDIA_REPOSITORY", "FUTURE_KNOWLEDGE_REPOSITORY",
    "SERVICE_POLICY", "INQUIRY_DATA_MODEL", "SEO_INTENT_OWNER", "WOOCOMMERCE_ADAPTER",
]
EXPECTED_OWNER_KINDS = (
    ["EXISTING_CANONICAL_OWNER"] * 4
    + ["FUTURE_GATED_OWNER"]
    + ["EXISTING_POLICY_OWNER"] * 2
    + ["FUTURE_GATED_OWNER"] * 7
    + ["EXISTING_ARCHITECTURE_OWNER"] * 2
    + ["PROJECTION_ONLY"]
)
EXPECTED_OWNER_ROLES = (
    ["READ_ONLY_INTERFACE"] * 4
    + ["BOUNDARY_ONLY"]
    + ["READ_ONLY_INTERFACE"] * 2
    + ["BOUNDARY_ONLY"] * 7
    + ["READ_ONLY_PROJECTION"] * 3
)
EXPECTED_TRUTH_CLASSES = [
    "CANONICAL_SELECTION", "DERIVED_TECHNICAL", "DYNAMIC_COMMERCIAL",
    "KNOWLEDGE_CONTENT", "SERVICE_FULFILLMENT", "OPERATOR_INTERNAL",
]
EXPECTED_FIELD_KEYS = [
    "product_family_type", "grade_alloy", "brand", "market_nominal_size", "outside_diameter",
    "inside_diameter", "thickness", "finish", "color", "appearance", "coating_method", "length",
    "production_seam_method", "material_manufacturing_standard", "tolerance", "current_branch_mass",
    "availability", "price", "customer_order_unit", "pricing_basis", "applications_guidance", "cutting",
    "shipping_handling",
]

DEPENDENCY_PATHS = {
    "product_core_contract_semantic_sha256": "product_core_contract",
    "product_entities_registry_semantic_sha256": "product_entities_registry",
    "product_attribute_contract_semantic_sha256": "product_attribute_contract",
    "product_attribute_registry_semantic_sha256": "product_attribute_registry",
    "measurement_contract_semantic_sha256": "measurement_contract",
    "measurement_dimensions_registry_semantic_sha256": "measurement_dimensions_registry",
    "measurement_units_registry_semantic_sha256": "measurement_units_registry",
    "c002_product_administration_contract_semantic_sha256": "c002_product_administration_contract",
    "c002_product_administration_registry_semantic_sha256": "c002_product_administration_registry",
    "c002_candidate_contract_semantic_sha256": "c002_candidate_contract",
    "c002_candidate_registry_semantic_sha256": "c002_candidate_registry",
    "c003_r3_contract_semantic_sha256": "c003_r3_contract",
    "c003_r3_registry_semantic_sha256": "c003_r3_registry",
    "c004_contract_semantic_sha256": "c004_contract",
    "c004_advantage_registry_semantic_sha256": "c004_advantage_registry",
    "c005_contract_semantic_sha256": "c005_contract",
    "c005_registry_semantic_sha256": "c005_registry",
}

FORBIDDEN_POPULATION_KEYS = {
    "products", "product_values", "variants", "valid_tuples", "skus", "mass_observations",
    "supply_records", "availability_records", "stock_records", "price_values", "media_assets",
    "knowledge_articles", "customers", "orders", "quotes", "runtime_configuration",
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
        if nodes > 50_000:
            issues.append("[INPUT_NODE_CAP] input exceeds 50000 nodes")
            return
        if depth > 100:
            issues.append(f"[INPUT_DEPTH] {path}: input exceeds depth cap")
            return
        if isinstance(node, float) and not math.isfinite(node):
            issues.append(f"[NON_FINITE] {path}: non-finite number is forbidden")
        elif isinstance(node, dict):
            for key, child in node.items():
                walk(child, f"{path}/{key}", depth + 1)
        elif isinstance(node, list):
            for index, child in enumerate(node):
                walk(child, f"{path}/{index}", depth + 1)

    walk(value, "<registry>", 0)
    return sorted(set(issues))


def load_validator(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[Any, dict[str, Any]]:
    contract = require_mapping(load_yaml(safe_path(contract_path, "contract")), "contract")
    schema = require_mapping(load_json(safe_path(schema_path, "schema")), "schema")
    schema_issues = audit_schema(schema)
    if schema_issues:
        raise ValidationConfigurationError("; ".join(schema_issues))
    validator = validate_schema(schema)
    return validator, contract


def _actual_source(item: Any) -> tuple[Any, ...]:
    if not isinstance(item, dict):
        return (None,) * 8
    return (
        item.get("source_id"), item.get("sequence"), item.get("message_ts"), item.get("parent_ts"),
        item.get("message_role"), item.get("title"), item.get("captured_at"), item.get("parent_reply_count"),
    )


def validate_dependency_pins(add: Callable[[str, str], None], contract: dict[str, Any]) -> None:
    dependencies = contract.get("dependencies", {})
    pins = contract.get("base_pins", {})
    if set(pins) != set(DEPENDENCY_PATHS):
        add("BASE_PIN_SET", "base pin names must match the complete C002-C005 and canonical dependency set")
    for pin_key, path_key in DEPENDENCY_PATHS.items():
        rel = dependencies.get(path_key) if isinstance(dependencies, dict) else None
        expected = pins.get(pin_key) if isinstance(pins, dict) else None
        if not isinstance(rel, str) or not isinstance(expected, str):
            add("BASE_PIN_CONFIG", f"missing dependency or pin for {pin_key}")
            continue
        try:
            path = safe_path(ROOT / rel, f"dependency {path_key}")
            actual = semantic_digest(load_json(path) if path.suffix == ".json" else load_yaml(path))
        except Exception as exc:
            add("BASE_PIN_CONFIG", f"cannot load {path_key}: {exc}")
            continue
        if actual != expected:
            add("BASE_PIN_REGRESSION", f"{pin_key} expected {expected}, found {actual}")


def validate_contract_policy(add: Callable[[str, str], None], contract: dict[str, Any]) -> None:
    if contract.get("contract_id") != "pipe-product-experience-architecture" or contract.get("contract_version") != "1.0.0":
        add("CONTRACT_POLICY", "contract identity/version must be exact")
    if contract.get("schema") != {
        "path": "repository/data/schemas/pipe-product-experience-architecture.schema.json",
        "draft": "https://json-schema.org/draft/2020-12/schema",
    } or contract.get("registry") != {
        "path": "repository/data/registries/extensions/c006/pipe-product-experience-architecture.yaml"
    }:
        add("CONTRACT_POLICY", "schema and registry paths must be canonical")
    if contract.get("mission") != {
        "mission_id": "C006", "starting_main_sha": EXPECTED_MAIN, "architecture_only": True,
        "implementation_ready_does_not_mean_runtime_ready": True,
        "old_deferred_c006_label_superseded_only": True,
        "pilot_certification_or_production_authority_created": False,
    }:
        add("MISSION_ANCHOR", "contract mission and bounded identity reconciliation must be exact")
    source = contract.get("source_policy", {})
    if source != {
        "channel_id": "C0BNHRRTE9F", "founder_user_id": "U0BNFS43TBL",
        "exact_message_timestamps": [item[2] for item in EXPECTED_SOURCES],
        "exact_parent_reply_counts": {"1787086720.993949": 2, "1787084095.125229": 1},
        "complete_threads_required": True, "planning_direction_does_not_populate_truth": True,
    }:
        add("SOURCE_EXACTNESS", "contract Slack source policy must be exact")
    contract_authority = contract.get("authority", {})
    # These six contract keys intentionally use concise, stable names.
    expected_authority = {
        "semantic_reconciliation_allowed": True,
        "projection_architecture_allowed": True,
        "owner_interface_definition_allowed": True,
        "documentation_contract_schema_validator_test_allowed": True,
        "branch_commit_push_non_draft_pr_allowed": True,
        "attributable_ci_repair_allowed": True,
    } | {f"{key}_allowed": False for key in DENIED_AUTHORITY}
    if contract_authority != expected_authority:
        add("AUTHORITY_EFFECT", "contract authority/no-go map must be complete and exact")

    owner_policy = contract.get("owner_policy", {})
    if owner_policy.get("required_owner_domains") != EXPECTED_DOMAINS:
        add("OWNER_ORDER", "contract required owner domains must be exact")
    if any(owner_policy.get(key) is not True for key in (
        "brand_identity_and_provenance_separate", "service_policy_and_inquiry_context_separate",
        "customer_order_unit_pricing_authority_and_pricing_basis_separate",
    )):
        add("OWNER_BOUNDARY", "contract must preserve separate Brand, Service, order-unit and pricing owners")
    semantic_policy = contract.get("semantic_policy", {})
    if semantic_policy.get("data_classes") != EXPECTED_TRUTH_CLASSES:
        add("TRUTH_CLASS_VOCABULARY", "contract truth-class vocabulary must match Scope exactly")
    if semantic_policy.get("finish_color_appearance_coating_collapse_allowed") is not False:
        add("SEMANTIC_FIELD_COLLAPSE", "Finish, Color, Appearance and Coating Method must remain distinct")
    if contract.get("variant_policy", {}).get("owner") != "VARIANT_RULE_SET":
        add("VARIANT_RULE_OWNER_MISMATCH", "Variant Rules owner literal must be canonical")
    if contract.get("media_knowledge_policy", {}).get("media_precedence") != [
        "VARIANT_OVERRIDE", "APPEARANCE_OR_FINISH_OVERRIDE", "FAMILY_DEFAULT"
    ]:
        add("MEDIA_PRECEDENCE", "contract media precedence must be most-specific to Family fallback")
    if contract.get("commercial_owner_policy") != {
        "price_owner": "PRICING_AUTHORITY", "customer_order_unit_owner": "CUSTOMER_ORDER_UNIT_POLICY",
        "pricing_basis_owner": "PRICING_BASIS_POLICY", "owners_are_future_gated": True,
    }:
        add("COMMERCIAL_OWNER_COLLAPSE", "commercial owner policy must keep its three future-gated owners separate")
    if contract.get("service_policy") != {
        "owner": "SERVICE_POLICY", "owner_is_future_gated": True,
        "inquiry_context_is_not_service_policy_owner": True,
    }:
        add("SERVICE_INQUIRY_OWNER_COLLAPSE", "Service policy owner must remain separate from Inquiry context")


def validate_live_regressions(add: Callable[[str, str], None]) -> None:
    candidate = load_yaml(ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml")
    admin = load_yaml(ROOT / "repository/data/registries/extensions/c002/product-administration-policies.yaml")
    r3 = load_yaml(ROOT / "repository/data/registries/extensions/c003r2/201-51-founder-evidence-completion.yaml")
    advantages = load_yaml(ROOT / "repository/data/registries/extensions/c004/damavand-advantages.yaml")
    c005 = load_yaml(ROOT / "repository/data/registries/extensions/c005/201-51-founder-evidence-readiness.yaml")
    entities = load_yaml(ROOT / "repository/data/registries/product-entities.yaml")
    attributes = load_yaml(ROOT / "repository/data/registries/product-attributes.yaml")
    pd03a = load_yaml(ROOT / "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml")

    if len(candidate.get("candidates", [])) != 0:
        add("REGRESSION_ANCHOR", "C002 candidate registry must remain empty")
    if len(admin.get("policies", [])) != 8 or len(admin.get("instances", [])) != 0:
        add("REGRESSION_ANCHOR", "C002 must remain 8 policies and 0 instances")
    matrix = r3.get("valid_combination_evidence_matrix", {})
    if matrix.get("confirmed_valid_count") != 216 or matrix.get("persisted_expanded_tuple_rows") is not False:
        add("REGRESSION_ANCHOR", "C003-R3 evidence must remain 216 positions without persisted Cartesian rows")
    dispositions = [item.get("recommended_status") for item in advantages.get("advantages", [])]
    if dispositions.count("USE_NOW") != 7 or dispositions.count("PLAN_NOW_IMPLEMENT_LATER") != 3:
        add("REGRESSION_ANCHOR", "C004 advantage counts changed")
    if len(c005.get("evidence_records", [])) != 17 or c005.get("c002_readiness_reevaluation", {}).get("readiness") != "NOT_READY":
        add("REGRESSION_ANCHOR", "C005 evidence/readiness changed")
    if not isinstance(entities, list) or len(entities) != 3:
        add("REGRESSION_ANCHOR", "canonical Product entity count must remain 3")
    if len(attributes.get("attributes", [])) + len(pd03a.get("attributes", [])) != 6:
        add("REGRESSION_ANCHOR", "approved attribute definition count must remain 6")


def validate_registry(value: Any, schema_validator: Any, contract: dict[str, Any]) -> list[str]:
    issues = audit_value(value)

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    if not isinstance(value, dict):
        add("ROOT_TYPE", "registry root must be an object")
        return sorted(set(issues))

    for error in sorted(schema_validator.iter_errors(value), key=lambda item: list(item.absolute_path)):
        path = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add("SCHEMA", f"{path}: {error.message}")

    if value.get("mission_id") != "C006" or value.get("starting_main_sha") != EXPECTED_MAIN:
        add("MISSION_ANCHOR", "mission id and starting live main SHA must be exact")

    manifest = value.get("source_manifest", {})
    sources = manifest.get("sources", []) if isinstance(manifest, dict) else []
    if (manifest.get("channel_id"), manifest.get("author_user_id"), manifest.get("source_count")) != ("C0BNHRRTE9F", "U0BNFS43TBL", 5):
        add("SOURCE_EXACTNESS", "Slack channel, Founder author and source count must be exact")
    if [_actual_source(item) for item in sources] != EXPECTED_SOURCES:
        add("SOURCE_EXACTNESS", "Slack source timestamps, roles, titles, capture times and ordering must be exact")
    if manifest.get("complete_threads_verified") is not True or any(
        not isinstance(item, dict) or item.get("thread_complete") is not True or item.get("promotion_effect") is not False
        or item.get("authority_role") != "FOUNDER_ACCEPTED_PLANNING_DIRECTION" for item in sources
    ):
        add("SOURCE_COMPLETENESS", "all sources must be complete, planning-only and non-promoting")

    authority = value.get("authority_effects", {})
    expected_authority = {key: True for key in ALLOWED_AUTHORITY} | {key: False for key in DENIED_AUTHORITY}
    if authority != expected_authority:
        add("AUTHORITY_EFFECT", "authority map must be complete and exact")
    if value.get("truth_class_vocabulary") != EXPECTED_TRUTH_CLASSES:
        add("TRUTH_CLASS_VOCABULARY", "machine truth-class vocabulary must match Scope exactly")

    owners = value.get("owner_bindings", [])
    if [item.get("domain") for item in owners if isinstance(item, dict)] != EXPECTED_DOMAINS:
        add("OWNER_ORDER", "owner domain order must be exact")
    if [item.get("canonical_owner") for item in owners if isinstance(item, dict)] != EXPECTED_OWNERS:
        add("OWNER_BOUNDARY", "canonical and future-gated owners must be exact")
    if [item.get("owner_kind") for item in owners if isinstance(item, dict)] != EXPECTED_OWNER_KINDS:
        add("OWNER_BOUNDARY", "owner kinds must be exact")
    if [item.get("c006_role") for item in owners if isinstance(item, dict)] != EXPECTED_OWNER_ROLES:
        add("OWNER_BOUNDARY", "C006 owner-interface roles must be exact")
    if [item.get("sequence") for item in owners if isinstance(item, dict)] != list(range(1, 18)):
        add("OWNER_ORDER", "owner sequences must be contiguous and exact")
    if len({item.get("domain") for item in owners if isinstance(item, dict)}) != len(owners):
        add("OWNER_DUPLICATION", "each domain must have one owner binding")
    if any(item.get("writeback_allowed") is not False or item.get("authority_transfer") is not False for item in owners if isinstance(item, dict)):
        add("OWNER_BOUNDARY", "C006 interfaces cannot write back or transfer authority")
    owner_domains = [item.get("domain") for item in owners if isinstance(item, dict)]
    if owner_domains.count("BRAND_IDENTITY") != 1 or owner_domains.count("C002_BRAND_PROVENANCE") != 1:
        add("BRAND_IDENTITY_PROVENANCE_COLLAPSE", "Brand identity and C002 Brand provenance require separate owners")
    if owner_domains.count("SERVICE_POLICY") != 1 or owner_domains.count("INQUIRY_CONTEXT") != 1:
        add("SERVICE_INQUIRY_OWNER_COLLAPSE", "Service policy and Inquiry context require separate owners")
    if any(owner_domains.count(key) != 1 for key in (
        "PRICING_AUTHORITY", "CUSTOMER_ORDER_UNIT_POLICY", "PRICING_BASIS_POLICY"
    )):
        add("COMMERCIAL_OWNER_COLLAPSE", "Price, customer order unit and pricing basis require separate owners")

    fields = value.get("semantic_fields", [])
    if [item.get("field_key") for item in fields if isinstance(item, dict)] != EXPECTED_FIELD_KEYS:
        add("FIELD_ORDER", "semantic field set and order must be exact")
    if len({item.get("field_key") for item in fields if isinstance(item, dict)}) != len(fields):
        add("FIELD_BOUNDARY", "semantic field keys must be unique")
    by_key = {item.get("field_key"): item for item in fields if isinstance(item, dict)}
    raw_field_keys = [item.get("field_key") for item in fields if isinstance(item, dict)]
    semantic_keys = ["finish", "color", "appearance", "coating_method"]
    omission_codes = {
        "finish": "FINISH_OMISSION", "color": "COLOR_OMISSION",
        "appearance": "APPEARANCE_OMISSION", "coating_method": "COATING_METHOD_OMISSION",
    }
    collapse_codes = {
        frozenset(("finish", "color")): "FINISH_COLOR_COLLAPSE",
        frozenset(("finish", "appearance")): "FINISH_APPEARANCE_COLLAPSE",
        frozenset(("finish", "coating_method")): "FINISH_COATING_METHOD_COLLAPSE",
        frozenset(("color", "appearance")): "COLOR_APPEARANCE_COLLAPSE",
        frozenset(("color", "coating_method")): "COLOR_COATING_METHOD_COLLAPSE",
        frozenset(("appearance", "coating_method")): "APPEARANCE_COATING_METHOD_COLLAPSE",
    }
    for missing in semantic_keys:
        if raw_field_keys.count(missing) == 0:
            add(omission_codes[missing], f"{missing} semantic field is required")
            for duplicate in semantic_keys:
                if duplicate != missing and raw_field_keys.count(duplicate) > 1:
                    code = collapse_codes[frozenset((missing, duplicate))]
                    add(code, f"{missing} and {duplicate} must remain separate semantic fields")
    if by_key.get("brand", {}).get("owner_domain") != "BRAND_IDENTITY":
        add("BRAND_OWNER_DUPLICATION", "Brand selection must bind to Brand identity with provenance as a separate gate")
    if by_key.get("brand", {}).get("provenance_owner_domain") != "C002_BRAND_PROVENANCE":
        add("BRAND_PROVENANCE_LINK", "Brand identity must retain an exact machine link to C002 Brand provenance")
    if any(item.get("provenance_owner_domain") is not None for item in fields if isinstance(item, dict) and item.get("field_key") != "brand"):
        add("BRAND_PROVENANCE_LINK", "only Brand may carry the Brand provenance owner link")
    if by_key.get("inside_diameter", {}).get("evidence_mode") != "CALCULATED_NOMINAL" or by_key.get("inside_diameter", {}).get("data_class") != "DERIVED_TECHNICAL":
        add("DERIVED_ID_AS_MEASURED", "inside diameter must remain a calculated nominal value")
    for key in ("current_branch_mass", "availability", "price"):
        if by_key.get(key, {}).get("immutable_product_identity") is not False:
            add("FIELD_BOUNDARY", f"{key} cannot be immutable Product identity")
    if by_key.get("current_branch_mass", {}).get("data_class") == "CANONICAL_SELECTION":
        add("MASS_IN_PRODUCT_IDENTITY", "mass cannot become Product identity")
    if by_key.get("price", {}).get("owner_domain") == "PRODUCT_IDENTITY":
        add("PRICE_IN_PRODUCT_TRUTH", "price cannot move into Product truth")
    if raw_field_keys.count("customer_order_unit") != 1 or raw_field_keys.count("pricing_basis") != 1:
        add("ORDER_UNIT_PRICING_BASIS_COLLAPSE", "order unit and pricing basis must remain distinct")
    if by_key.get("cutting", {}).get("owner_domain") != "SERVICE_POLICY" or by_key.get("shipping_handling", {}).get("owner_domain") != "SERVICE_POLICY":
        add("SERVICE_INQUIRY_OWNER_COLLAPSE", "Service fields must bind to Service policy, never Inquiry context")
    if by_key.get("customer_order_unit", {}).get("owner_domain") != "CUSTOMER_ORDER_UNIT_POLICY":
        add("ORDER_UNIT_PRICING_OWNER_COLLAPSE", "customer order unit requires its own future-gated policy owner")
    if by_key.get("pricing_basis", {}).get("owner_domain") != "PRICING_BASIS_POLICY":
        add("PRICING_BASIS_AUTHORITY_COLLAPSE", "pricing basis requires its own future-gated policy owner")
    if by_key.get("price", {}).get("owner_domain") != "PRICING_AUTHORITY":
        add("PRICE_AUTHORITY_OWNER_MISMATCH", "price must bind only to future-gated Pricing authority")

    derivation = (value.get("derivation_rules") or [{}])[0]
    if not isinstance(derivation, dict) or derivation.get("classification") != "CALCULATED_NOMINAL" or derivation.get("measured_evidence") is not False:
        add("DERIVED_ID_AS_MEASURED", "inside-diameter derivation cannot claim measured evidence")

    variant = value.get("variant_resolution", {})
    if variant.get("owner") != "VARIANT_RULE_SET":
        add("VARIANT_RULE_OWNER_MISMATCH", "Variant Rules owner literal must be canonical")
    if variant.get("cartesian_generation") is not False:
        add("CARTESIAN_VARIANT_GENERATION", "Cartesian Variant generation is forbidden")
    if variant.get("unsupported_option_selectable") is not False:
        add("UNSUPPORTED_SELECTOR_OPTION", "unsupported selector options must not be selectable")
    if variant.get("availability_is_separate") is not True:
        add("VARIANT_AVAILABILITY_COLLAPSE", "valid combination and Availability are separate states")
    if variant.get("unknown_means_out_of_stock") is not False:
        add("UNKNOWN_AS_OUT_OF_STOCK", "UNKNOWN combination/evidence cannot mean out of stock")

    mass = value.get("mass_lifecycle", {})
    if mass.get("promotion_actor") != "OPERATOR" or mass.get("automatic_promotion") is not False:
        add("MASS_UNAUTHORIZED_PROMOTION", "mass lifecycle promotion must be operator-controlled")
    if mass.get("embedded_in_product_identity") is not False or mass.get("numeric_observation_count") != 0:
        add("MASS_IN_PRODUCT_IDENTITY", "C006 may not embed or populate mass")

    availability = value.get("availability_boundary", {})
    if availability.get("supplier_habit_inference") is not False or availability.get("available_requires_current_governed_evidence") is not True:
        add("AVAILABILITY_FROM_SUPPLIER_HABIT", "Availability requires current governed evidence, never supplier habit")
    if availability.get("missing_evidence_means_out_of_stock") is not False:
        add("UNKNOWN_AS_OUT_OF_STOCK", "missing Availability evidence cannot mean out of stock")

    pricing = value.get("pricing_boundary", {})
    if (
        pricing.get("price_owner") != "PRICING_AUTHORITY"
        or pricing.get("customer_order_unit_owner") != "CUSTOMER_ORDER_UNIT_POLICY"
        or pricing.get("pricing_basis_owner") != "PRICING_BASIS_POLICY"
    ):
        add("COMMERCIAL_OWNER_COLLAPSE", "pricing boundary must retain three separate future-gated owners")
    if pricing.get("product_truth_field") is not False or pricing.get("current_price_value_count") != 0:
        add("PRICE_IN_PRODUCT_TRUTH", "C006 cannot own or populate price")
    if pricing.get("customer_order_unit_and_pricing_basis_distinct") is not True:
        add("ORDER_UNIT_PRICING_BASIS_COLLAPSE", "order unit and pricing basis must remain distinct")

    media = value.get("media_knowledge", {})
    if media.get("media_precedence") != ["VARIANT_OVERRIDE", "APPEARANCE_OR_FINISH_OVERRIDE", "FAMILY_DEFAULT"]:
        add("MEDIA_PRECEDENCE", "media precedence must resolve most-specific Variant first, then override, then Family")
    if media.get("false_visual_inheritance_allowed") is not False or media.get("selected_visual_mismatch_blocks_inheritance") is not True:
        add("FALSE_MEDIA_INHERITANCE", "visual inheritance must stop on selected-context mismatch")

    seo = value.get("seo_projection", {})
    if seo.get("page_per_tuple") is not False:
        add("TUPLE_PAGE_EXPLOSION", "page-per-tuple projection is forbidden")
    if seo.get("selector_state_indexed_by_default") is not False or seo.get("query_state_indexed_by_default") is not False:
        add("SELECTOR_STATE_INDEXED", "selector/query state cannot be indexed by default")

    woo = value.get("woocommerce_projection", {})
    if woo.get("canonical_product_truth_owner") is not False or woo.get("canonical_commerce_authority") is not False:
        add("WOOCOMMERCE_AS_CANONICAL_OWNER", "WooCommerce is projection-only")

    cta = value.get("cta_boundary", {})
    if cta.get("purchase_cta_enabled") is not False or any(cta.get(key) is not False for key in ("cart_enabled", "checkout_enabled", "payment_enabled")):
        add("PREMATURE_PURCHASE_CTA", "purchase/cart/checkout/payment must remain disabled")

    service = value.get("service_boundary", {})
    if service.get("owner") != "SERVICE_POLICY":
        add("SERVICE_INQUIRY_OWNER_COLLAPSE", "Service boundary requires the future-gated Service policy owner")
    if service.get("product_attribute") is not False or service.get("immutable_product_identity") is not False:
        add("SERVICE_AS_PRODUCT_ATTRIBUTE", "services are context, not Product attributes or identity")

    for key in FORBIDDEN_POPULATION_KEYS.intersection(value):
        add("FORBIDDEN_POPULATION_KEY", f"architecture registry cannot contain {key}")

    expected_anchors = {
        "c002_candidate_count": 0, "c002_policy_count": 8, "c002_policy_instance_count": 0,
        "c002_mass_methods": ["MANUFACTURER_STATED", "MEASURED", "CALCULATED"],
        "c003_r3_confirmed_evidence_positions": 216, "c003_r3_persisted_cartesian_rows": False,
        "c004_competitor_count": 13, "c004_score_count": 364,
        "c004_advantage_counts": {"USE_NOW": 7, "PLAN_NOW_IMPLEMENT_LATER": 3},
        "c005_evidence_count": 17,
        "c005_readiness": {"SUBMITTED": 8, "MISSING": 1, "REVIEWABLE": 6, "OPEN_BLOCKING": 9, "VERIFIED": 0, "RESOLVED": 0, "REQUIRED": 9, "STATE": "NOT_READY"},
        "canonical_product_entity_count": 3, "canonical_sku_count": 0, "approved_attribute_count": 6,
        "numeric_mass_count": 0, "supply_count": 0, "current_price_count": 0,
        "c1_t03_state": "FROZEN_AT_PROTECTED_ARCHITECTURE_BOUNDARY", "commerce_state": "INQUIRY_ONLY",
        "runtime_authority": "NONE", "production_authority": "NONE",
    }
    if value.get("regression_anchors") != expected_anchors:
        add("REGRESSION_ANCHOR", "C002-C005 and canonical Product boundary anchors must be exact")

    validate_contract_policy(add, contract)
    validate_dependency_pins(add, contract)
    validate_live_regressions(add)
    return sorted(set(issues))


def validate_package(
    registry_path: Path = REGISTRY_PATH,
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> list[str]:
    schema_validator, contract = load_validator(contract_path, schema_path)
    registry = load_yaml(safe_path(registry_path, "registry"))
    issues = validate_registry(registry, schema_validator, contract)
    for label, value, expected in (
        ("contract", contract, EXPECTED_CONTRACT_DIGEST),
        ("schema", load_json(schema_path), EXPECTED_SCHEMA_DIGEST),
        ("registry", registry, EXPECTED_REGISTRY_DIGEST),
    ):
        if expected == "TO_BE_FINALIZED":
            issues.append(f"[SEMANTIC_DIGEST] {label} digest is not pinned")
            continue
        actual = semantic_digest(value)
        if actual != expected:
            issues.append(f"[SEMANTIC_DIGEST] {label} digest pin mismatch")
    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", type=Path, default=REGISTRY_PATH)
    args = parser.parse_args()
    try:
        issues = validate_package(args.registry)
    except (OSError, ValueError, ValidationConfigurationError) as exc:
        print(f"[CONFIGURATION] {exc}", file=sys.stderr)
        return 2
    if issues:
        for issue in issues:
            print(issue, file=sys.stderr)
        return 1
    print("C006 pipe Product/experience architecture validation passed (offline, architecture-only).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
