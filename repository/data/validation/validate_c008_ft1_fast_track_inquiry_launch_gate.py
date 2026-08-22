#!/usr/bin/env python3
"""Fail-closed offline validator for the C008-FT1 sibling launch gate."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any

from validate_c005_founder_evidence_readiness import (
    ROOT,
    audit_schema,
    audit_value,
    load_json,
    load_yaml,
    require_mapping,
    safe_path,
    semantic_digest,
    validate_schema,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/c008-ft1-fast-track-inquiry-launch-gate.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/c008-ft1-fast-track-inquiry-launch-gate.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c008ft1/fast-track-inquiry-launch-gate.yaml"
SYNTHETIC_PATH = ROOT / "tests/fixtures/c008-ft1-fast-track-inquiry-launch-gate/valid-synthetic.yaml"

PIN_PATHS = {
    "c002_candidate_contract_semantic_sha256": ROOT / "repository/data/contracts/commercial-pilot-candidate.contract.yaml",
    "c002_candidate_schema_semantic_sha256": ROOT / "repository/data/schemas/commercial-pilot-candidate.schema.json",
    "c002_candidate_registry_semantic_sha256": ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml",
    "c006_contract_semantic_sha256": ROOT / "repository/data/contracts/pipe-product-experience-architecture.contract.yaml",
    "c006_schema_semantic_sha256": ROOT / "repository/data/schemas/pipe-product-experience-architecture.schema.json",
    "c006_registry_semantic_sha256": ROOT / "repository/data/registries/extensions/c006/pipe-product-experience-architecture.yaml",
    "c008_contract_semantic_sha256": ROOT / "repository/data/contracts/c008-c002-readiness-evidence-closure.contract.yaml",
    "c008_schema_semantic_sha256": ROOT / "repository/data/schemas/c008-c002-readiness-evidence-closure.schema.json",
    "c008_registry_semantic_sha256": ROOT / "repository/data/registries/extensions/c008/201-51-readiness-evidence-closure.yaml",
    "c008_r1_contract_semantic_sha256": ROOT / "repository/data/contracts/c008-r1-remaining-real-world-evidence-closure.contract.yaml",
    "c008_r1_schema_semantic_sha256": ROOT / "repository/data/schemas/c008-r1-remaining-real-world-evidence-closure.schema.json",
    "c008_r1_registry_semantic_sha256": ROOT / "repository/data/registries/extensions/c008r1/201-51-remaining-real-world-evidence-closure.yaml",
}

# Replaced only after an independent stable-tree review.
EXPECTED_CONTRACT_DIGEST = "4c940eed75fe433bc8adbc85cb45954068b233cc1de6d80b40bc28eb71466fb5"
EXPECTED_SCHEMA_DIGEST = "8eb3c93a37932e6676e8a3d1c22e0c35d3f6a4d0f47f7467ea718f466ceabd80"
EXPECTED_REGISTRY_DIGEST = "799dad2f7fdf9f6ffb5a9fe37c707f222f6f92f1cc6b1e251bd3f366dd2e9cf3"
EXPECTED_SYNTHETIC_REGISTRY_DIGEST = "40e11db4a2bd2703e9213537e2590624c97d729c258d798974f9915ec575c167"

EXPECTED_MAIN = "324fc66e5ae1c7c4062a36c9deb84dc769352e1e"
EXPECTED_GATE_ID = "FAST_TRACK_INQUIRY_LAUNCH_ELIGIBLE"
EXPECTED_BLOCKERS = [
    "CANONICAL_PRODUCT_PROMOTION_COMPLETE",
    "RIGHTS_SAFE_MEDIA_READY",
    "INQUIRY_CRM_FLOW_READY",
    "SECURITY_PRIVACY_GATE_READY",
    "SEO_INDEXING_GATE_READY",
    "MOBILE_PERFORMANCE_GATE_READY",
    "STAGING_ACCEPTANCE_PASS",
    "PRODUCTION_FOUNDER_GO",
]
EXPECTED_SOURCE = {
    "source_id": "C008FT1-SOURCE-001",
    "source_class": "FOUNDER_EXECUTION_AUTHORIZATION",
    "bound_source_count": 3,
    "locator": "slack:C0BNHRRTE9F:1787435678.814589",
    "channel_id": "C0BNHRRTE9F",
    "message_ts": "1787435678.814589",
    "thread_parent_ts": "1787398697.475999",
    "direction_parent_title": "FOUNDER DECISION — FIRST COMMERCIAL SLICE — 2026-08-22",
    "direction_parent_authored_at": "2026-08-22T15:08:17+03:30",
    "direction_parent_author_id": "U0BNFS43TBL",
    "author_id": "U0BNFS43TBL",
    "title": "FOUNDER / PROJECT COMMANDER EXECUTION AUTHORIZATION — C008-FT1 FAST-TRACK INQUIRY LAUNCH GOVERNANCE AMENDMENT — 2026-08-23",
    "authored_at": "2026-08-23T01:24:38+03:30",
    "thread_complete": True,
    "reply_count": 17,
    "reply_index": 17,
    "execution_command_sha256": "87dbebf5b77f57fc24e1dc9ad9ced7d5725d4bba32112ebdb335adfc67e8a9ed",
    "execution_command_role": "CURRENT_FOUNDER_TASK_INSTRUCTION",
    "authorized_branch": "codex/c008-ft1-fast-track-inquiry-launch-governance",
}
EXPECTED_PREDECESSOR = {
    "mission": "C008-R1",
    "status": "COMPLETED_ARCHIVE_ONLY",
    "merge_commit": EXPECTED_MAIN,
    "post_merge_ci_run": 32600651309,
    "post_merge_ci_result": "PASS",
    "tree_integrated": True,
}
EXPECTED_PREREQUISITES = [
    {"id": "PREDECESSOR_GOVERNANCE_INTEGRATED", "state": "MET", "met": True,
     "evidence_class": "MERGED_GOVERNANCE_EVIDENCE", "owner": "C008_R1",
     "source_refs": [f"git:main:{EXPECTED_MAIN}", "ci:32600651309"], "fail_closed_reason": None},
    {"id": "FAST_TRACK_SLICE_FOUNDER_DIRECTION_EXISTS", "state": "MET", "met": True,
     "evidence_class": "FOUNDER_DIRECTION", "owner": "FOUNDER",
     "source_refs": ["slack:C0BNHRRTE9F:1787398697.475999", "slack:C0BNHRRTE9F:1787435678.814589"], "fail_closed_reason": None},
    {"id": "CANONICAL_PRODUCT_PROMOTION_COMPLETE", "state": "NOT_AUTHORIZED", "met": False,
     "evidence_class": "FUTURE_AUTHORIZATION_REQUIRED", "owner": "PRODUCT_CORE",
     "source_refs": ["repository:AGENTS.md:enterprise-product-architecture"],
     "fail_closed_reason": "No canonical Product, Variant Rule, valid tuple or SKU promotion is authorized or complete."},
    {"id": "VALID_COMBINATION_CONTRACT_READY", "state": "MET", "met": True,
     "evidence_class": "ARCHITECTURE_CONTRACT", "owner": "VARIANT_RULE_SET",
     "source_refs": ["repository:data:contracts:pipe-product-experience-architecture"], "fail_closed_reason": None},
    {"id": "RIGHTS_SAFE_MEDIA_READY", "state": "MISSING_EVIDENCE", "met": False,
     "evidence_class": "MISSING_EVIDENCE", "owner": "FUTURE_MEDIA_REPOSITORY",
     "source_refs": ["registry:C008-R1:RIGHTS_SAFE_MEDIA_PACKET_ONLY"],
     "fail_closed_reason": "No owned, licensed or permission-bound production media has been admitted and independently reviewed."},
    {"id": "INQUIRY_ONLY_COMMERCE_BOUNDARY_READY", "state": "MET", "met": True,
     "evidence_class": "GOVERNANCE_POLICY", "owner": "INQUIRY_DATA_MODEL",
     "source_refs": ["repository:docs:adr:0001-inquiry-first-commerce"], "fail_closed_reason": None},
    {"id": "INQUIRY_CRM_FLOW_READY", "state": "NOT_AUTHORIZED", "met": False,
     "evidence_class": "FUTURE_AUTHORIZATION_REQUIRED", "owner": "INQUIRY_DATA_MODEL",
     "source_refs": ["repository:docs:42_INQUIRY_WORKFLOW"],
     "fail_closed_reason": "No approved or configured inquiry form, consent, routing, CRM or operational workflow exists."},
    {"id": "SECURITY_PRIVACY_GATE_READY", "state": "NOT_AUTHORIZED", "met": False,
     "evidence_class": "FUTURE_AUTHORIZATION_REQUIRED", "owner": "SECURITY_PRIVACY",
     "source_refs": ["repository:docs:10_SECURITY"],
     "fail_closed_reason": "Security and privacy acceptance for a public inquiry flow is not authorized or complete."},
    {"id": "SEO_INDEXING_GATE_READY", "state": "NOT_AUTHORIZED", "met": False,
     "evidence_class": "FUTURE_AUTHORIZATION_REQUIRED", "owner": "SEO_INTENT_OWNER",
     "source_refs": ["repository:docs:34_SEO_ENTITY_MODEL"],
     "fail_closed_reason": "No public URL, indexing, entity or Schema implementation is authorized or accepted."},
    {"id": "MOBILE_PERFORMANCE_GATE_READY", "state": "NOT_AUTHORIZED", "met": False,
     "evidence_class": "FUTURE_AUTHORIZATION_REQUIRED", "owner": "PRODUCT_EXPERIENCE_ENGINE",
     "source_refs": ["repository:enterprise-platform:05_PRODUCT_EXPERIENCE_ENGINE"],
     "fail_closed_reason": "Mobile RTL accessibility and performance acceptance has not been executed on an authorized implementation."},
    {"id": "STAGING_ACCEPTANCE_PASS", "state": "NOT_AUTHORIZED", "met": False,
     "evidence_class": "FUTURE_AUTHORIZATION_REQUIRED", "owner": "RELEASE_GOVERNANCE",
     "source_refs": ["authority:C008-FT1:no-staging"],
     "fail_closed_reason": "Staging mutation and acceptance are not authorized."},
    {"id": "PRODUCTION_FOUNDER_GO", "state": "NOT_AUTHORIZED", "met": False,
     "evidence_class": "FUTURE_AUTHORIZATION_REQUIRED", "owner": "FOUNDER",
     "source_refs": ["authority:C008-FT1:no-production"],
     "fail_closed_reason": "No Founder Production GO exists."},
]
EXPECTED_C002 = {
    "relationship": "INDEPENDENT_SIBLING_NOT_ALIAS", "readiness": "NOT_READY",
    "resolved_count": 6, "unresolved_count": 3, "founder_selection_ready": False,
    "candidate_registry_count": 0, "supply_evidence": "SUBMITTED_REVIEW_INCOMPLETE",
    "photo_content_readiness": "MISSING_EVIDENCE",
    "fulfillment_risk": "SUBMITTED_REVIEW_INCOMPLETE", "state_mutation_effect": False,
}
EXPECTED_SUPPLY = {
    "intake_status": "DEFERRED_TO_BE_COMPLETED_LATER", "deferred_is_waiver": False,
    "deferred_is_verified": False, "deferred_is_not_applicable": False,
    "deferred_is_resolved": False,
    "planning_may_continue_only_under_inquiry_first_no_public_commitment": True,
    "public_safe_wording_fa": "پس از استعلام بررسی می‌شود", "price_claim_allowed": False,
    "stock_claim_allowed": False, "availability_claim_allowed": False,
    "eta_or_sla_claim_allowed": False, "delivery_guarantee_allowed": False,
    "supplier_commitment_claim_allowed": False,
}
EXPECTED_MEDIA = {
    "photo_content_readiness": "MISSING_EVIDENCE", "rights_safe_media_required": True,
    "owned_media_created": False, "licensed_media_created": False,
    "supplier_permission_created": False, "publication_right_created": False,
    "publication_allowed": False,
}
EXPECTED_COMMERCIAL = {
    "classification": "FOUNDER_APPROVED_BUSINESS_DIRECTION_NOT_CANONICAL_PRODUCT_TRUTH",
    "product_direction": "Decorative Stainless Steel Pipe", "material": "Stainless Steel",
    "grade": "201", "primary_diameter": "51 mm", "commerce_state": "INQUIRY_ONLY",
    "public_price": False, "public_stock_or_availability": False, "public_eta_or_sla": False,
    "creates_canonical_product_truth": False, "creates_product_variant_value_tuple_or_sku": False,
}
EXPECTED_SELECTOR = {
    "selector_order_is_family_dependent": True, "global_selector_order_hardcoded": False,
    "finish_and_color_fused": False, "brand_inferred": False,
    "valid_combination_contract_is_valid_tuple": False, "selectable_values_created": False,
}
EXPECTED_AUTHORITY = {
    "governance_model_creation": True,
    "repository_docs_contract_schema_registry_validator_tests": True,
    "branch_commit_push_pr": True,
    "c002_state_mutation": False, "candidate_population": False, "product_population": False,
    "controlled_value_promotion": False, "valid_tuple_promotion": False,
    "sku_assignment": False, "supply_or_fulfillment_truth_population": False,
    "media_asset_or_rights_population": False, "price_stock_availability_eta_sla_claim": False,
    "commerce_eligibility_activation": False, "wordpress_woocommerce_mutation": False,
    "runtime_mutation": False, "staging_mutation": False, "production_mutation": False,
    "publication": False, "c009_or_m4_start": False, "successor_mission": False,
    "auto_merge": False, "merge": False,
}
EXPECTED_REGRESSION = {
    "c002_resolved_count": 6, "c002_unresolved_count": 3, "c002_readiness": "NOT_READY",
    "c002_founder_selection_ready": False, "c002_candidate_count": 0,
    "canonical_product_entity_count": 3, "canonical_sku_count": 0,
    "current_supply_intake_record_count": 0, "current_price_value_count": 0,
    "commerce_state": "INQUIRY_ONLY", "runtime_authority": "NONE",
    "staging_authority": "NONE", "production_authority": "NONE",
    "c009_authorized": False, "m4_authorized": False,
}
EXPECTED_PINS = {
    "c002_candidate_contract_semantic_sha256": "923731cb080b0ecc05abb21b1189bfdd0df94297780cce364bb791479f7f47e3",
    "c002_candidate_schema_semantic_sha256": "1e1b1977f369ab7e5961d4e69111682d1117bc6eeedf666a9e568f0115952741",
    "c002_candidate_registry_semantic_sha256": "deb0215d2b5f4b5ec0061f937aec9c3e37cf97c94432a23737bf5756cef9587e",
    "c006_contract_semantic_sha256": "131b2c79a3d017c65bac896e95e7a638164a77b821546e5217266f6d3829dcc0",
    "c006_schema_semantic_sha256": "9a9009c4431c097c062dcef81fad03fae51784ff466bb8cc5db6ed14237f79e3",
    "c006_registry_semantic_sha256": "5b5510af1b521daa7b2539007cab0681885f2bbc3eff4a75dde67cb38857ad8b",
    "c008_contract_semantic_sha256": "bf450358e11c82df7ae41a7777bd2889f2c4b7cffe64a5f2ee21f3303cbd2f5c",
    "c008_schema_semantic_sha256": "82f8dbfb93233b6d40603a56bdb7661ee4d477003ba13b97c59d80bb0c8a27af",
    "c008_registry_semantic_sha256": "bd06e76da52750b9b54c09ccba88421ae82778dce84a4afa15475a88297081d9",
    "c008_r1_contract_semantic_sha256": "da5a70f0e7330df8afab52e931f664bda453266740646a4d4183d25370ea75d7",
    "c008_r1_schema_semantic_sha256": "fea342c3210dca9e5c2e98030bf8b5e64464cdd550cbb3b5675109c49673b904",
    "c008_r1_registry_semantic_sha256": "9dcf2cc7cc10ab01a9b97ab40ac896debd12e6f25ad5b7e700921a6c782fb87b",
}

EXPECTED_CONTRACT_AUTHORITY = {
    "mission_id": "C008-FT1", "governance_model_creation_allowed": True,
    "repository_docs_contract_schema_registry_validator_test_work_allowed": True,
    "branch_commit_push_pr_allowed": True, "c002_state_mutation_allowed": False,
    "candidate_population_allowed": False, "product_population_allowed": False,
    "controlled_value_promotion_allowed": False, "valid_tuple_promotion_allowed": False,
    "sku_assignment_allowed": False, "supply_or_fulfillment_truth_population_allowed": False,
    "media_asset_or_rights_population_allowed": False,
    "availability_stock_price_eta_sla_claim_allowed": False,
    "commerce_eligibility_activation_allowed": False,
    "wordpress_woocommerce_mutation_allowed": False, "runtime_mutation_allowed": False,
    "staging_mutation_allowed": False, "production_mutation_allowed": False,
    "publication_allowed": False, "c009_or_m4_start_allowed": False,
    "successor_mission_allowed": False, "auto_merge_allowed": False, "merge_allowed": False,
}
EXPECTED_DEPENDENCIES = {
    "c002_candidate_contract": "repository/data/contracts/commercial-pilot-candidate.contract.yaml",
    "c002_candidate_schema": "repository/data/schemas/commercial-pilot-candidate.schema.json",
    "c002_candidate_registry": "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml",
    "c006_contract": "repository/data/contracts/pipe-product-experience-architecture.contract.yaml",
    "c006_schema": "repository/data/schemas/pipe-product-experience-architecture.schema.json",
    "c006_registry": "repository/data/registries/extensions/c006/pipe-product-experience-architecture.yaml",
    "c008_contract": "repository/data/contracts/c008-c002-readiness-evidence-closure.contract.yaml",
    "c008_schema": "repository/data/schemas/c008-c002-readiness-evidence-closure.schema.json",
    "c008_registry": "repository/data/registries/extensions/c008/201-51-readiness-evidence-closure.yaml",
    "c008_r1_contract": "repository/data/contracts/c008-r1-remaining-real-world-evidence-closure.contract.yaml",
    "c008_r1_schema": "repository/data/schemas/c008-r1-remaining-real-world-evidence-closure.schema.json",
    "c008_r1_registry": "repository/data/registries/extensions/c008r1/201-51-remaining-real-world-evidence-closure.yaml",
}
EXPECTED_SCHEMA_BINDING = {
    "path": "repository/data/schemas/c008-ft1-fast-track-inquiry-launch-gate.schema.json",
    "draft": "https://json-schema.org/draft/2020-12/schema",
}
EXPECTED_REGISTRY_BINDING = {
    "path": "repository/data/registries/extensions/c008ft1/fast-track-inquiry-launch-gate.yaml",
}
EXPECTED_SOURCE_POLICY = {
    "slack_channel_id": "C0BNHRRTE9F", "founder_user_id": "U0BNFS43TBL",
    "direction_parent_ts": "1787398697.475999",
    "direction_parent_title": "FOUNDER DECISION — FIRST COMMERCIAL SLICE — 2026-08-22",
    "authorization_ts": "1787435678.814589",
    "authorization_reply_index": 17, "exact_thread_reply_count": 17,
    "authorization_title": EXPECTED_SOURCE["title"], "authorized_starting_main": EXPECTED_MAIN,
    "execution_command_sha256": "87dbebf5b77f57fc24e1dc9ad9ced7d5725d4bba32112ebdb335adfc67e8a9ed",
    "predecessor_merge_commit": EXPECTED_MAIN, "predecessor_post_merge_ci_run": 32600651309,
    "predecessor_post_merge_ci_result": "PASS",
    "authorized_branch": "codex/c008-ft1-fast-track-inquiry-launch-governance",
    "exact_source_count": 3, "complete_source_required": True,
}
EXPECTED_GATE_POLICY = {
    "gate_id": EXPECTED_GATE_ID, "gate_kind": "SIBLING_GOVERNANCE_GATE",
    "initial_state": False, "aggregate_rule": "ALL_12_PREREQUISITES_MET",
    "prerequisite_count": 12, "met_count": 4, "unmet_count": 8,
    "merge_does_not_enable_gate": True,
    "gate_does_not_authorize_runtime_staging_production_or_publication": True,
    "c002_is_not_input_alias_or_output": True, "c009_and_m4_remain_separately_authorized": True,
}
EXPECTED_C002_POLICY = {
    "readiness": "NOT_READY", "resolved_count": 6, "unresolved_count": 3,
    "founder_selection_ready": False, "candidate_registry_count": 0,
    "supply_evidence": "SUBMITTED_REVIEW_INCOMPLETE",
    "photo_content_readiness": "MISSING_EVIDENCE",
    "fulfillment_risk": "SUBMITTED_REVIEW_INCOMPLETE",
    "reinterpretation_or_mutation_allowed": False,
}
EXPECTED_SUPPLY_POLICY = {
    "intake_status": "DEFERRED_TO_BE_COMPLETED_LATER", "deferred_is_waiver": False,
    "deferred_is_verified": False, "deferred_is_not_applicable": False,
    "deferred_is_resolved": False,
    "planning_may_continue_only_under_inquiry_first_no_public_commitment": True,
    "public_price_stock_availability_eta_sla_or_delivery_guarantee_allowed": False,
}
EXPECTED_MEDIA_POLICY = {
    "rights_safe_media_state": "MISSING_EVIDENCE", "media_readiness_inference_allowed": False,
    "publication_without_rights_safe_media_allowed": False,
}
EXPECTED_COMMERCIAL_POLICY = {
    key: value for key, value in EXPECTED_COMMERCIAL.items()
    if key not in {"public_price", "public_stock_or_availability", "public_eta_or_sla", "creates_canonical_product_truth"}
}
EXPECTED_SELECTOR_POLICY = {
    "selector_order_is_family_dependent": True, "global_selector_order_hardcoding_allowed": False,
    "finish_and_color_may_be_fused": False, "brand_may_be_inferred": False,
    "valid_combination_contract_is_valid_tuple": False,
}
EXPECTED_VALIDATION = {
    "offline_only": True, "network_allowed": False, "side_effects_allowed": False,
    "closed_schema_required": True, "local_refs_only": True,
    "duplicate_keys_rejected": True, "non_finite_numbers_rejected": True,
    "deterministic_sorted_errors": True, "path_escape_symlink_and_byte_cap_enforced": True,
    "exact_order_counts_and_bindings_required": True, "semantic_digest_pinning_required": True,
    "mutation_manifest_dispatch_required": True,
}
EXPECTED_CONTRACT_KEYS = {
    "contract_id", "contract_version", "record_kind", "schema", "registry", "authority",
    "dependencies", "base_pins", "source_policy", "gate_policy", "c002_separation_policy",
    "supply_fulfillment_policy", "media_policy", "commercial_direction_policy",
    "selector_policy", "validation",
}
FORBIDDEN_KEYS = {
    "products", "product_values", "variants", "variant_rules", "valid_tuples", "skus",
    "prices", "availability", "stock", "eta", "sla", "media_assets", "rights_grants",
    "runtime_objects", "staging_objects", "production_objects", "candidates",
}


def _issue(issues: list[str], code: str, message: str) -> None:
    issues.append(f"[{code}] {message}")


def _walk_keys(value: Any, path: str = "$") -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            found.append((key, child_path))
            found.extend(_walk_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(_walk_keys(child, f"{path}[{index}]"))
    return found


def load_validator() -> tuple[Any, dict[str, Any]]:
    contract = require_mapping(load_yaml(CONTRACT_PATH), "C008-FT1 contract")
    schema = require_mapping(load_json(SCHEMA_PATH), "C008-FT1 schema")
    schema_issues = audit_schema(schema)
    if schema_issues:
        raise RuntimeError("; ".join(schema_issues))
    return validate_schema(schema), contract


def validate_dependency_pins(add: Any, contract: dict[str, Any]) -> None:
    if contract.get("base_pins") != EXPECTED_PINS:
        add("DEPENDENCY_PIN", "contract predecessor pins differ")
    for key, path in PIN_PATHS.items():
        try:
            value = load_json(path) if path.suffix == ".json" else load_yaml(path)
            if semantic_digest(value) != EXPECTED_PINS[key]:
                add("DEPENDENCY_PIN", f"{key} live semantic digest differs")
        except Exception as exc:
            add("DEPENDENCY_PIN", f"could not validate {key}: {exc}")
    try:
        c002 = require_mapping(load_yaml(PIN_PATHS["c002_candidate_registry_semantic_sha256"]), "C002 registry")
        if c002.get("candidates") != []:
            add("C002_SNAPSHOT_DRIFT", "canonical candidate registry must remain empty")
        c008 = require_mapping(load_yaml(PIN_PATHS["c008_registry_semantic_sha256"]), "C008 registry")
        rr = c008.get("readiness_result", {})
        if rr.get("resolved_count") != 6 or rr.get("readiness") != "NOT_READY":
            add("C002_SNAPSHOT_DRIFT", "C008 predecessor must remain exact 6/9 NOT_READY")
        c008r1 = require_mapping(load_yaml(PIN_PATHS["c008_r1_registry_semantic_sha256"]), "C008-R1 registry")
        if c008r1.get("readiness_result", {}).get("resolved_count") != 6:
            add("C002_SNAPSHOT_DRIFT", "C008-R1 predecessor must preserve 6/9")
    except Exception as exc:
        add("DEPENDENCY_PIN", str(exc))


def validate_registry(
    value: dict[str, Any], schema_validator: Any, contract: dict[str, Any], *, synthetic_mode: bool = False
) -> list[str]:
    issues: list[str] = []
    add = lambda code, message: _issue(issues, code, message)
    issues.extend(audit_value(value))
    for error in sorted(schema_validator.iter_errors(value), key=lambda item: list(item.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path) or "$"
        add("SCHEMA", f"{location}: {error.message}")

    expected_mode = "SYNTHETIC" if synthetic_mode else "CANONICAL"
    expected_id = "c008ft1:fast-track-inquiry-launch-gate:synthetic" if synthetic_mode else "c008ft1:fast-track-inquiry-launch-gate"
    expected_time = "2026-08-23T01:36:56+03:30" if synthetic_mode else "2026-08-23T01:31:56+03:30"
    if value.get("fixture_mode") != expected_mode or value.get("registry_id") != expected_id:
        add("FIXTURE_MODE", f"expected {expected_mode} fixture identity")
    if value.get("mission_id") != "C008-FT1" or value.get("authorized_starting_main") != EXPECTED_MAIN:
        add("MISSION_ANCHOR", "mission identity or starting main differs")
    if value.get("evaluation_as_of") != expected_time:
        add("MISSION_ANCHOR", "evaluation timestamp differs")
    if value.get("source") != EXPECTED_SOURCE:
        add("SOURCE_BINDING", "Founder authorization source differs")
    if value.get("predecessor") != EXPECTED_PREDECESSOR:
        add("PREDECESSOR_BINDING", "C008-R1 predecessor binding differs")

    gate = value.get("gate", {})
    prerequisites = gate.get("prerequisites", []) if isinstance(gate, dict) else []
    if prerequisites != EXPECTED_PREREQUISITES:
        add("PREREQUISITE_SET_EXACTNESS", "ordered prerequisite rows differ")
    met = [row for row in prerequisites if isinstance(row, dict) and row.get("met") is True]
    unmet = [row for row in prerequisites if isinstance(row, dict) and row.get("met") is False]
    expected_gate_scalars = {
        "gate_id": EXPECTED_GATE_ID, "gate_kind": "SIBLING_GOVERNANCE_GATE", "eligible": False,
        "aggregate_rule": "ALL_12_PREREQUISITES_MET", "prerequisite_count": 12,
        "met_count": 4, "unmet_count": 8, "merge_does_not_enable_gate": True,
    }
    if any(gate.get(key) != expected for key, expected in expected_gate_scalars.items()):
        add("GATE_AGGREGATION", "gate identity, state, rule or counts differ")
    if gate.get("blockers") != EXPECTED_BLOCKERS or len(met) != 4 or len(unmet) != 8:
        add("GATE_AGGREGATION", "blocker order or derived prerequisite counts differ")
    if gate.get("eligible") is True and (unmet or gate.get("merge_does_not_enable_gate") is not True):
        add("GATE_AGGREGATION", "gate cannot be eligible with unmet prerequisites")
    if gate.get("merge_does_not_enable_gate") is not True:
        add("MERGE_DOES_NOT_GRANT_ELIGIBILITY", "merge must not enable the sibling gate")
    if gate.get("gate_id") != EXPECTED_GATE_ID or gate.get("gate_kind") != "SIBLING_GOVERNANCE_GATE":
        add("C002_ALIASING", "Fast-Track gate must remain a separate sibling")

    if value.get("c002_snapshot") != EXPECTED_C002:
        add("C002_SNAPSHOT_DRIFT", "C002 snapshot must remain exact 6/9 NOT_READY")
    c002 = value.get("c002_snapshot", {})
    if c002.get("relationship") != "INDEPENDENT_SIBLING_NOT_ALIAS" or c002.get("state_mutation_effect") is not False:
        add("C002_ALIASING", "Fast-Track gate must not alias or mutate C002")
    if value.get("supply_fulfillment_deferral") != EXPECTED_SUPPLY:
        add("SUPPLIER_DEFERRAL_BOUNDARY", "deferred Supply/Fulfillment semantics differ")
    if value.get("media_boundary") != EXPECTED_MEDIA:
        add("MEDIA_RIGHTS_BOUNDARY", "rights-safe media boundary differs")
    if value.get("commercial_direction") != EXPECTED_COMMERCIAL:
        add("PRODUCT_PROMOTION_BOUNDARY", "Founder business direction or Product non-promotion differs")
    commercial = value.get("commercial_direction", {})
    if any(commercial.get(key) is True for key in ("public_price", "public_stock_or_availability", "public_eta_or_sla")):
        add("PUBLIC_COMMERCIAL_CLAIM", "public Price/Availability/ETA claims are forbidden")
    supply = value.get("supply_fulfillment_deferral", {})
    commercial_claim_keys = (
        "price_claim_allowed", "stock_claim_allowed", "availability_claim_allowed",
        "eta_or_sla_claim_allowed", "delivery_guarantee_allowed", "supplier_commitment_claim_allowed",
    )
    if any(supply.get(key) is True for key in commercial_claim_keys):
        add("PUBLIC_COMMERCIAL_CLAIM", "deferred evidence cannot create a public commercial claim")
    if value.get("selector_boundaries") != EXPECTED_SELECTOR:
        add("C006_SEMANTIC_BOUNDARY", "selector/Finish/Color/Brand boundaries differ")
    selector = value.get("selector_boundaries", {})
    if selector.get("global_selector_order_hardcoded") is True:
        add("SELECTOR_OWNER_BOUNDARY", "global selector order is forbidden")
    if selector.get("valid_combination_contract_is_valid_tuple") is True:
        add("READINESS_CLASS_CONFUSION", "architecture contract cannot be treated as a valid tuple")
    if value.get("authority_effects") != EXPECTED_AUTHORITY:
        add("RUNTIME_AUTHORITY_BOUNDARY", "authority effects differ from the bounded governance-only map")
    authority = value.get("authority_effects", {})
    if authority.get("c009_or_m4_start") is True or authority.get("successor_mission") is True:
        add("SUCCESSOR_AUTHORITY_BOUNDARY", "C009/M4/successor authority is forbidden")
    if value.get("regression_anchors") != EXPECTED_REGRESSION:
        add("REGRESSION_ANCHOR", "protected Product/C002/runtime anchors differ")

    for key, path in _walk_keys(value):
        if key in FORBIDDEN_KEYS:
            add("FORBIDDEN_POPULATION_KEY", f"forbidden populated domain at {path}")

    if set(contract) != EXPECTED_CONTRACT_KEYS or contract.get("contract_id") != "c008-ft1-fast-track-inquiry-launch-gate" or contract.get("contract_version") != "1.0.0" or contract.get("record_kind") != "c008ft1-fast-track-inquiry-launch-gate":
        add("CONTRACT_EXACTNESS", "contract identity or top-level keys differ")
    if contract.get("schema") != EXPECTED_SCHEMA_BINDING or contract.get("registry") != EXPECTED_REGISTRY_BINDING:
        add("CONTRACT_EXACTNESS", "contract schema or registry binding differs")
    if contract.get("dependencies") != EXPECTED_DEPENDENCIES:
        add("CONTRACT_EXACTNESS", "contract dependencies differ")
    contract_checks = [
        ("CONTRACT_AUTHORITY", "authority", EXPECTED_CONTRACT_AUTHORITY),
        ("CONTRACT_SOURCE_POLICY", "source_policy", EXPECTED_SOURCE_POLICY),
        ("CONTRACT_GATE_POLICY", "gate_policy", EXPECTED_GATE_POLICY),
        ("CONTRACT_C002_POLICY", "c002_separation_policy", EXPECTED_C002_POLICY),
        ("CONTRACT_SUPPLY_POLICY", "supply_fulfillment_policy", EXPECTED_SUPPLY_POLICY),
        ("CONTRACT_MEDIA_POLICY", "media_policy", EXPECTED_MEDIA_POLICY),
        ("CONTRACT_COMMERCIAL_POLICY", "commercial_direction_policy", EXPECTED_COMMERCIAL_POLICY),
        ("CONTRACT_SELECTOR_POLICY", "selector_policy", EXPECTED_SELECTOR_POLICY),
        ("CONTRACT_VALIDATION_POLICY", "validation", EXPECTED_VALIDATION),
    ]
    for code, key, expected in contract_checks:
        if contract.get(key) != expected:
            add(code, f"contract {key} differs")
    validate_dependency_pins(add, contract)
    return sorted(set(issues))


def validate_package(
    *, registry_path: Path = REGISTRY_PATH, synthetic_mode: bool = False, allow_unpinned: bool = False
) -> list[str]:
    issues: list[str] = []
    try:
        for path, label in ((CONTRACT_PATH, "contract"), (SCHEMA_PATH, "schema"), (registry_path, "registry")):
            safe_path(path, f"C008-FT1 {label}")
        contract = require_mapping(load_yaml(CONTRACT_PATH), "C008-FT1 contract")
        schema = require_mapping(load_json(SCHEMA_PATH), "C008-FT1 schema")
        registry = require_mapping(load_yaml(registry_path), "C008-FT1 registry")
        issues.extend(audit_schema(schema))
        schema_validator = validate_schema(schema)
        issues.extend(validate_registry(registry, schema_validator, contract, synthetic_mode=synthetic_mode))
        digests = [
            ("CONTRACT_DIGEST", EXPECTED_CONTRACT_DIGEST, semantic_digest(contract)),
            ("SCHEMA_DIGEST", EXPECTED_SCHEMA_DIGEST, semantic_digest(schema)),
            (("SYNTHETIC_DIGEST" if synthetic_mode else "REGISTRY_DIGEST"),
             (EXPECTED_SYNTHETIC_REGISTRY_DIGEST if synthetic_mode else EXPECTED_REGISTRY_DIGEST),
             semantic_digest(registry)),
        ]
        for code, expected, actual in digests:
            if expected in {None, "", "TO_BE_FINALIZED"}:
                if not allow_unpinned:
                    _issue(issues, "SEMANTIC_DIGEST", f"{code} is not pinned")
            elif expected != actual:
                _issue(issues, code, f"expected {expected}, got {actual}")
    except Exception as exc:
        _issue(issues, "VALIDATION_CONFIGURATION", str(exc))
    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=REGISTRY_PATH)
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--allow-unpinned", action="store_true")
    args = parser.parse_args()
    issues = validate_package(
        registry_path=args.registry, synthetic_mode=args.synthetic, allow_unpinned=args.allow_unpinned
    )
    if issues:
        print("\n".join(issues))
        return 1
    print("C008-FT1 fast-track inquiry launch gate validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
