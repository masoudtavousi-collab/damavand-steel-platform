#!/usr/bin/env python3
"""Fail-closed offline validator for the C008-R1 delta-only evidence closure."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path
import sys
from typing import Any

from validate_c005_founder_evidence_readiness import (
    ROOT,
    ValidationConfigurationError,
    audit_schema,
    audit_value,
    load_json,
    load_yaml,
    require_mapping,
    safe_path,
    semantic_digest,
    validate_schema,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/c008-r1-remaining-real-world-evidence-closure.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/c008-r1-remaining-real-world-evidence-closure.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c008r1/201-51-remaining-real-world-evidence-closure.yaml"
SYNTHETIC_PATH = ROOT / "tests/fixtures/c008-r1-remaining-real-world-evidence-closure/valid-synthetic.yaml"
C002_CONTRACT_PATH = ROOT / "repository/data/contracts/commercial-pilot-candidate.contract.yaml"
C002_SCHEMA_PATH = ROOT / "repository/data/schemas/commercial-pilot-candidate.schema.json"
C002_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
C008_CONTRACT_PATH = ROOT / "repository/data/contracts/c008-c002-readiness-evidence-closure.contract.yaml"
C008_SCHEMA_PATH = ROOT / "repository/data/schemas/c008-c002-readiness-evidence-closure.schema.json"
C008_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c008/201-51-readiness-evidence-closure.yaml"

# Replaced only after a stable-tree independent review.
EXPECTED_CONTRACT_DIGEST = "a95adb501f5441b3a1657a43a6355518706f7da0ff3ae6af867c50316cb7401c"
EXPECTED_SCHEMA_DIGEST = "25543ea5c5237ef3eb002f33b1fd5c0744684b93859718dab3fb974836efcef9"
EXPECTED_REGISTRY_DIGEST = "7643ae4b868d1ea04e8c239cbf2a4a2a8900be32713c0218a507ca241dd9c5de"
EXPECTED_SYNTHETIC_REGISTRY_DIGEST = "e721a12836503f7f11487a3c7f86a78d892da55311afdb483632fe82fb0629d2"
EXPECTED_SOURCE_MANIFEST_DIGEST = "ecaddd36da0055f6bc8922c938393ad2130d0b8276e7d3d8650d27a5ce9b87e5"
EXPECTED_SEARCH_SCOPE_DIGEST = "7b9a9e922eb35cb63b04304d72148dcb6964643b864e07d8de2ea25a09f47e73"
EXPECTED_BLOCKER_DIGESTS = [
    "ed4b52202ef1afa295b1f959896e269b0c88db121d9cf7a48e45338360022313",
    "eec55bae55f9197f450cea9978d86c3fa3c07124340abab9363340e5e57b93cb",
    "b139de0d4e32087b925bca53e20c2b904374e6541e45c93ff19c3cc5328baed9",
]
EXPECTED_REQUEST_DIGESTS = [
    "dabe8800d0d982b7b1e796f0a08ecf11d3d5699c5cf2368c8b942bb837ad9b52",
    "1cc91e8f67e00117dacb5a7c2111120e8cfc26d9ec5dbb5aa944774aaa335344",
]

EXPECTED_MAIN = "fbe3d9eb78566dc7b006fc43b0939d124a81cec6"
EXPECTED_BLOCKERS = ["SUPPLY_EVIDENCE", "PHOTO_CONTENT_READINESS", "FULFILLMENT_RISK"]
EXPECTED_TERMINAL = ["SUBMITTED_REVIEW_INCOMPLETE", "MISSING_EVIDENCE", "SUBMITTED_REVIEW_INCOMPLETE"]
EXPECTED_MAPPED = ["SUBMITTED", "MISSING", "SUBMITTED"]
EXPECTED_INHERITED = ["C008-EVID-002", "C008-EVID-006", "C008-EVID-009"]
EXPECTED_LANES = ["LANE_A_SUPPLY", "LANE_C_RIGHTS_SAFE_MEDIA", "LANE_B_FULFILLMENT"]
EXPECTED_TOTALS = {
    "criterion_count": 9,
    "verified_count": 6,
    "not_applicable_approved_count": 0,
    "submitted_review_incomplete_count": 2,
    "missing_evidence_count": 1,
    "conflicting_evidence_count": 0,
    "expired_or_stale_evidence_count": 0,
    "resolved_count": 6,
    "unresolved_count": 3,
    "open_blocking_count": 3,
    "readiness": "NOT_READY",
    "founder_selection_ready": False,
    "candidate_registry_count": 0,
    "reopened_verified_criteria_count": 0,
}
EXPECTED_G1 = {
    "result": "HOLD_NOT_READY_6_OF_9",
    "resolved_criteria_count": 6,
    "unresolved_criteria": EXPECTED_BLOCKERS,
    "real_world_evidence_required": True,
    "founder_selection_ready": False,
    "m4_promotion_candidate": None,
    "recommendation_is_selection": False,
    "founder_business_decision_required": False,
    "founder_evidence_input_required": True,
    "c009_authorized": False,
    "m4_authorized": False,
}
EXPECTED_PINS = {
    "c002_candidate_contract_semantic_sha256": "923731cb080b0ecc05abb21b1189bfdd0df94297780cce364bb791479f7f47e3",
    "c002_candidate_schema_semantic_sha256": "1e1b1977f369ab7e5961d4e69111682d1117bc6eeedf666a9e568f0115952741",
    "c002_candidate_registry_semantic_sha256": "deb0215d2b5f4b5ec0061f937aec9c3e37cf97c94432a23737bf5756cef9587e",
    "c008_contract_semantic_sha256": "bf450358e11c82df7ae41a7777bd2889f2c4b7cffe64a5f2ee21f3303cbd2f5c",
    "c008_schema_semantic_sha256": "82f8dbfb93233b6d40603a56bdb7661ee4d477003ba13b97c59d80bb0c8a27af",
    "c008_registry_semantic_sha256": "bd06e76da52750b9b54c09ccba88421ae82778dce84a4afa15475a88297081d9",
}
EXPECTED_CONTRACT_AUTHORITY = {
    "mission_id": "C008-R1", "packet_id": "DS-P1-M3-C008-R1-PACKET-01", "packet_version": "1.0",
    "evidence_intake_and_normalization_allowed": True, "blocker_review_allowed": True,
    "founder_evidence_request_packet_allowed": True, "g1_decision_surface_allowed": True,
    "repository_docs_contract_schema_validator_test_work_allowed": True, "branch_commit_push_pr_allowed": True,
    "candidate_population_allowed": False, "product_population_allowed": False,
    "controlled_value_promotion_allowed": False, "valid_tuple_promotion_allowed": False,
    "sku_assignment_allowed": False, "mass_population_allowed": False,
    "supply_truth_population_allowed": False, "availability_or_stock_claim_allowed": False,
    "price_or_pricing_authority_allowed": False, "commerce_eligibility_population_allowed": False,
    "customer_lead_order_payment_population_allowed": False, "media_asset_or_rights_population_allowed": False,
    "media_publication_allowed": False, "wordpress_woocommerce_mutation_allowed": False,
    "runtime_staging_production_allowed": False, "deployment_import_hosting_database_allowed": False,
    "workflow_secret_repository_settings_mutation_allowed": False, "c009_or_m4_start_allowed": False,
    "successor_mission_allowed": False, "auto_merge_allowed": False, "merge_allowed": False,
}
EXPECTED_SOURCE_POLICY = {
    "slack_channel_id": "C0BNHRRTE9F", "founder_user_id": "U0BNFS43TBL",
    "execution_authorization_parent_ts": "1787390606.427149", "packet_reply_ts": "1787390614.653749",
    "slack_file_id": "F0BRVVCN9C5",
    "packet_zip_sha256": "b6f134d78fd309e16ea9fcda22180b235a7a82580b304deeaf6a6b0d4a49715f",
    "complete_thread_required": True, "exact_reply_count": 1, "packet_internal_manifest_required": True,
    "packet_planning_status_is_superseded_only_by_exact_execution_authorization": True,
    "public_channel_evidence_search_required": True, "public_channel_evidence_search_found_new_items": False,
}
EXPECTED_EVIDENCE_POLICY = {
    "exact_new_evidence_item_count": 0, "exact_blocker_count": 3, "blocker_order": EXPECTED_BLOCKERS,
    "terminal_states": ["VERIFIED", "NOT_APPLICABLE_APPROVED", "SUBMITTED_REVIEW_INCOMPLETE", "MISSING_EVIDENCE", "CONFLICTING_EVIDENCE", "EXPIRED_OR_STALE_EVIDENCE"],
    "resolved_terminal_states": ["VERIFIED", "NOT_APPLICABLE_APPROVED"], "exact_terminal_vector": EXPECTED_TERMINAL,
    "missing_evidence_cannot_be_inferred": True, "missing_evidence_cannot_support_claims": True,
    "supplier_specific_evidence_required_for_supply_and_fulfillment": True,
    "rights_safe_media_evidence_required_for_photo_content": True,
    "protected_locators_may_replace_sensitive_values": True, "protected_values_must_not_be_copied": True,
    "owner_and_reviewer_must_differ": True, "conflicts_or_expiry_cannot_resolve": True,
    "competitor_or_internet_editing_cannot_create_rights": True,
    "supplier_evidence_cannot_imply_stock_availability_price_guaranteed_eta_or_permanent_relationship": True,
}
EXPECTED_READINESS_POLICY = {
    "predecessor_resolved_count": 6, "criterion_count": 9, "exact_resolved_count": 6,
    "exact_unresolved_count": 3, "exact_open_blocking_count": 3, "exact_readiness": "NOT_READY",
    "founder_selection_ready": False, "candidate_registry_count": 0, "readiness_is_selection": False,
    "weighted_scoring_allowed": False,
}
EXPECTED_G1_POLICY = {
    "decision_surface_only": True, "exact_result": "HOLD_NOT_READY_6_OF_9",
    "recommendation_is_selection": False, "exact_m4_candidate": None,
    "founder_decision_required": "PROVIDE_SOURCE_BOUND_SUPPLY_FULFILLMENT_AND_RIGHTS_SAFE_MEDIA_EVIDENCE",
    "c009_authorized": False, "m4_authorized": False,
}
EXPECTED_REQUEST_POLICY = {
    "request_count": 2,
    "request_order": ["SUPPLIER_SUPPLY_FULFILLMENT_PACKET", "RIGHTS_SAFE_MEDIA_PACKET"],
    "request_is_founder_decision": False, "sensitive_values_may_be_redacted": True,
    "locator_and_scope_must_remain_reviewable": True,
}
PIN_PATHS = {
    "c002_candidate_contract_semantic_sha256": C002_CONTRACT_PATH,
    "c002_candidate_schema_semantic_sha256": C002_SCHEMA_PATH,
    "c002_candidate_registry_semantic_sha256": C002_REGISTRY_PATH,
    "c008_contract_semantic_sha256": C008_CONTRACT_PATH,
    "c008_schema_semantic_sha256": C008_SCHEMA_PATH,
    "c008_registry_semantic_sha256": C008_REGISTRY_PATH,
}
ALLOWED_TRUE_AUTHORITY = {
    "evidence_intake_and_normalization",
    "blocker_review",
    "founder_evidence_request_packet",
    "g1_decision_surface",
}
FORBIDDEN_KEYS = {
    "products", "product_values", "skus", "persisted_tuples", "mass_observations",
    "availability_records", "stock_records", "prices", "supplier_facts", "media_assets",
    "rights_grants", "runtime_objects", "candidate_records",
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
    contract = require_mapping(load_yaml(CONTRACT_PATH), "C008-R1 contract")
    schema = require_mapping(load_json(SCHEMA_PATH), "C008-R1 schema")
    schema_issues = audit_schema(schema)
    if schema_issues:
        raise ValidationConfigurationError("; ".join(schema_issues))
    return validate_schema(schema), contract


def validate_dependency_pins(add: Any, contract: dict[str, Any]) -> None:
    pins = contract.get("base_pins")
    if pins != EXPECTED_PINS:
        add("DEPENDENCY_PIN_REGRESSION", "contract predecessor pins differ from the exact C002/C008 set")
    for key, path in PIN_PATHS.items():
        try:
            value = load_json(path) if path.suffix == ".json" else load_yaml(path)
            actual = semantic_digest(value)
        except Exception as exc:  # fail closed on any protected-owner read failure
            add("DEPENDENCY_PIN_REGRESSION", f"could not read {key}: {exc}")
            continue
        if actual != EXPECTED_PINS[key]:
            add("DEPENDENCY_PIN_REGRESSION", f"{key} live digest differs")
    try:
        c002 = require_mapping(load_yaml(C002_REGISTRY_PATH), "C002 registry")
        if c002.get("candidates") != []:
            add("C002_CANDIDATE_REGRESSION", "canonical candidate registry must remain empty")
    except Exception as exc:
        add("C002_CANDIDATE_REGRESSION", str(exc))
    try:
        c008 = require_mapping(load_yaml(C008_REGISTRY_PATH), "C008 registry")
        if c008.get("readiness_result", {}).get("resolved_count") != 6 or c008.get("g1_decision_surface", {}).get("result") != "HOLD_NOT_READY_6_OF_9":
            add("C008_PREDECESSOR_REGRESSION", "C008 must remain the exact 6/9 HOLD predecessor")
    except Exception as exc:
        add("C008_PREDECESSOR_REGRESSION", str(exc))


def validate_registry(
    value: dict[str, Any], schema_validator: Any, contract: dict[str, Any], *, synthetic_mode: bool = False
) -> list[str]:
    issues: list[str] = []
    add = lambda code, message: _issue(issues, code, message)
    for item in audit_value(value):
        issues.append(item)
    for error in sorted(schema_validator.iter_errors(value), key=lambda item: list(item.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path) or "$"
        add("SCHEMA", f"{location}: {error.message}")

    expected_mode = "SYNTHETIC" if synthetic_mode else "CANONICAL"
    if value.get("fixture_mode") != expected_mode:
        add("FIXTURE_MODE", f"expected {expected_mode}")
    if value.get("mission_id") != "C008-R1" or value.get("starting_main_sha") != EXPECTED_MAIN:
        add("MISSION_ANCHOR", "mission identity or starting main differs")

    packet = value.get("packet", {})
    expected_packet = {
        "packet_id": "DS-P1-M3-C008-R1-PACKET-01", "packet_version": "1.0",
        "slack_channel_id": "C0BNHRRTE9F", "authorization_parent_ts": "1787390606.427149",
        "packet_reply_ts": "1787390614.653749", "slack_file_id": "F0BRVVCN9C5",
        "packet_zip_sha256": "b6f134d78fd309e16ea9fcda22180b235a7a82580b304deeaf6a6b0d4a49715f",
        "packet_document_sha256": "f3ae526f4034bd4cc381100472f9eb54e21dec097cefbaeb24b35274dd2364a1",
        "checklist_sha256": "d1e1396f09e28a556c8dfe06df53198f79a68a9461d5e12c490147916d981a1c",
        "readme_sha256": "cee437b6367850e1ddfa14a55cfd423884e673c6572dc09fb2b2738c0d13e73c",
        "manifest_sha256": "c63b35b91848199719215cb2f545c02100665fc262fe3fcbbb68941c606baac1",
        "thread_complete": True, "reply_count": 1,
    }
    if packet != expected_packet:
        add("PACKET_EXACTNESS", "Packet/Slack/hash binding differs")

    source_manifest = value.get("source_manifest", {})
    source_ids = [item.get("source_id") for item in source_manifest.get("sources", []) if isinstance(item, dict)]
    if source_manifest.get("source_count") != 2 or source_ids != ["C008R1-SOURCE-001", "C008R1-SOURCE-002"]:
        add("SOURCE_MANIFEST", "exact two-source authorization/Packet manifest required")
    if semantic_digest(source_manifest) != EXPECTED_SOURCE_MANIFEST_DIGEST:
        add("SOURCE_MANIFEST_EXACTNESS", "source roles, locators, timestamps, titles, authors or completeness differ")

    auth = value.get("authority_effects", {})
    if any(auth.get(key) is not True for key in ALLOWED_TRUE_AUTHORITY) or any(
        flag is not False for key, flag in auth.items() if key not in ALLOWED_TRUE_AUTHORITY
    ):
        add("AUTHORITY_BOUNDARY", "only four bounded evidence/review surfaces may be true")

    intake = value.get("evidence_intake", {})
    zero_fields = ["new_evidence_items_total", "admitted_count", "rejected_count", "protected_count", "conflicting_count", "stale_count"]
    if any(intake.get(key) != 0 for key in zero_fields) or intake.get("admitted_evidence_items") != []:
        add("ZERO_EVIDENCE_INTAKE", "no new admissible/rejected/protected/conflicting/stale item exists")
    if intake.get("by_class") != {
        "SUPPLIER_SPECIFIC_EVIDENCE": 0, "RIGHTS_SAFE_MEDIA_EVIDENCE": 0,
        "PROTECTED_COMMERCIAL_EVIDENCE": 0, "CONFLICTING_EVIDENCE": 0,
        "EXPIRED_OR_STALE_EVIDENCE": 0,
    } or intake.get("finding") != "NO_NEW_ADMISSIBLE_REAL_WORLD_EVIDENCE":
        add("ZERO_EVIDENCE_COUNTS", "class counts/finding must remain exact and zero")
    if semantic_digest(intake.get("search_scope")) != EXPECTED_SEARCH_SCOPE_DIGEST:
        add("SEARCH_SCOPE_EXACTNESS", "evidence-search scope cannot add claims or omit required source coverage")

    reviews = value.get("blocker_reviews", [])
    if len(reviews) != 3:
        add("BLOCKER_COUNT", "exactly three ordered blocker reviews required")
    else:
        if [item.get("criterion_code") for item in reviews] != EXPECTED_BLOCKERS:
            add("BLOCKER_ORDER", "blocker order differs")
        if [item.get("sequence") for item in reviews] != [1, 2, 3]:
            add("BLOCKER_ORDER", "blocker sequence differs")
        if [item.get("lane") for item in reviews] != EXPECTED_LANES:
            add("BLOCKER_LANE", "lane binding differs")
        if [item.get("prior_terminal_state") for item in reviews] != EXPECTED_TERMINAL or [item.get("final_terminal_state") for item in reviews] != EXPECTED_TERMINAL:
            add("BLOCKER_TERMINAL_STATE", "no blocker may be force-resolved or reclassified")
        if [item.get("c002_mapped_state") for item in reviews] != EXPECTED_MAPPED:
            add("BLOCKER_C002_MAPPING", "C002 mapped states differ")
        if [item.get("inherited_evidence_ref") for item in reviews] != EXPECTED_INHERITED:
            add("BLOCKER_EVIDENCE_BINDING", "inherited C008 evidence refs differ")
        for item in reviews:
            if item.get("owner") == item.get("reviewer"):
                add("REVIEWER_INDEPENDENCE", f"{item.get('criterion_code')} reviewer equals owner")
            if item.get("supported_claims") != [] or item.get("new_evidence_item_ids") != []:
                add("NO_SUPPORTED_CLAIMS", f"{item.get('criterion_code')} cannot gain claims without evidence")
            if not item.get("missing_fields") or not item.get("remaining_requirement"):
                add("MISSING_REQUIREMENT", f"{item.get('criterion_code')} must preserve exact evidence gap")
            if item.get("conflicts") != [] or item.get("resolved") is not False or item.get("blocking") is not True:
                add("BLOCKER_RESOLUTION", f"{item.get('criterion_code')} must remain conflict-free/open-blocking")
            if item.get("promotion_effect") is not False or item.get("implementation_authority") is not False:
                add("BLOCKER_PROMOTION", f"{item.get('criterion_code')} cannot grant promotion/implementation")
            if item.get("disposition") != "NO_NEW_ADMISSIBLE_EVIDENCE":
                add("BLOCKER_DISPOSITION", f"{item.get('criterion_code')} disposition differs")
        if [semantic_digest(item) for item in reviews] != EXPECTED_BLOCKER_DIGESTS:
            add("BLOCKER_TEXT_EXACTNESS", "blocker gaps, non-claims, requirements or safe behavior differ")

    if value.get("readiness_result") != EXPECTED_TOTALS:
        add("READINESS_RESULT", "C002 readiness must remain exact 6/9 NOT_READY")
    if value.get("g1_decision_surface") != EXPECTED_G1:
        add("G1_BOUNDARY", "G1 must remain HOLD 6/9 with evidence input—not a business decision—required")

    requests = value.get("founder_evidence_requests", {})
    request_rows = requests.get("requests", []) if isinstance(requests, dict) else []
    request_bindings = [(item.get("request_id"), item.get("request_type"), item.get("criteria")) for item in request_rows]
    expected_request_bindings = [
        ("C008R1-REQUEST-001", "SUPPLIER_SUPPLY_FULFILLMENT_PACKET", ["SUPPLY_EVIDENCE", "FULFILLMENT_RISK"]),
        ("C008R1-REQUEST-002", "RIGHTS_SAFE_MEDIA_PACKET", ["PHOTO_CONTENT_READINESS"]),
    ]
    if requests.get("request_count") != 2 or request_bindings != expected_request_bindings:
        add("FOUNDER_REQUESTS", "exact two evidence requests required")
    if requests.get("request_is_founder_decision") is not False:
        add("FOUNDER_DECISION_BOUNDARY", "evidence request must not be recast as a business decision")
    if [semantic_digest(item) for item in request_rows] != EXPECTED_REQUEST_DIGESTS:
        add("FOUNDER_REQUEST_TEXT_EXACTNESS", "required fields, acceptable sources, redaction or review effect differ")

    expected_regression = contract.get("regression_anchors")
    if value.get("regression_snapshot") != expected_regression:
        add("REGRESSION_SNAPSHOT", "canonical Product/C002/runtime regression snapshot differs")

    for key, path in _walk_keys(value):
        if key in FORBIDDEN_KEYS:
            add("FORBIDDEN_POPULATION_KEY", f"forbidden populated domain at {path}")

    if contract.get("authority") != EXPECTED_CONTRACT_AUTHORITY:
        add("CONTRACT_AUTHORITY", "contract authority map differs from the exact bounded map")
    if contract.get("source_policy") != EXPECTED_SOURCE_POLICY:
        add("CONTRACT_SOURCE_POLICY", "contract source/zero-find policy differs")
    if contract.get("evidence_policy") != EXPECTED_EVIDENCE_POLICY:
        add("CONTRACT_EVIDENCE_POLICY", "contract evidence/terminal policy differs")
    if contract.get("readiness_policy") != EXPECTED_READINESS_POLICY:
        add("CONTRACT_READINESS_POLICY", "contract readiness policy differs")
    if contract.get("g1_policy") != EXPECTED_G1_POLICY:
        add("CONTRACT_G1_POLICY", "contract G1/evidence-input boundary differs")
    if contract.get("founder_request_policy") != EXPECTED_REQUEST_POLICY:
        add("CONTRACT_REQUEST_POLICY", "contract request order/decision boundary differs")
    validate_dependency_pins(add, contract)

    return sorted(set(issues))


def validate_package(*, registry_path: Path = REGISTRY_PATH, synthetic_mode: bool = False, allow_unpinned: bool = False) -> list[str]:
    issues: list[str] = []
    try:
        safe_path(CONTRACT_PATH, "C008-R1 contract")
        safe_path(SCHEMA_PATH, "C008-R1 schema")
        safe_path(registry_path, "C008-R1 registry")
        contract = require_mapping(load_yaml(CONTRACT_PATH), "C008-R1 contract")
        schema = require_mapping(load_json(SCHEMA_PATH), "C008-R1 schema")
        registry = require_mapping(load_yaml(registry_path), "C008-R1 registry")
        for item in audit_schema(schema):
            issues.append(item)
        validator = validate_schema(schema)
        issues.extend(validate_registry(registry, validator, contract, synthetic_mode=synthetic_mode))
        digests = [
            ("CONTRACT_DIGEST", EXPECTED_CONTRACT_DIGEST, semantic_digest(contract)),
            ("SCHEMA_DIGEST", EXPECTED_SCHEMA_DIGEST, semantic_digest(schema)),
            (("SYNTHETIC_DIGEST" if synthetic_mode else "REGISTRY_DIGEST"),
             (EXPECTED_SYNTHETIC_REGISTRY_DIGEST if synthetic_mode else EXPECTED_REGISTRY_DIGEST), semantic_digest(registry)),
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
    issues = validate_package(registry_path=args.registry, synthetic_mode=args.synthetic, allow_unpinned=args.allow_unpinned)
    if issues:
        print("\n".join(issues))
        return 1
    print("C008-R1 remaining real-world evidence closure validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
