#!/usr/bin/env python3
"""Fail-closed offline validator for C008 C002 readiness evidence closure."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import re
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


CONTRACT_PATH = ROOT / "repository/data/contracts/c008-c002-readiness-evidence-closure.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/c008-c002-readiness-evidence-closure.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c008/201-51-readiness-evidence-closure.yaml"
C002_CANDIDATE_CONTRACT_PATH = ROOT / "repository/data/contracts/commercial-pilot-candidate.contract.yaml"
C002_CANDIDATE_SCHEMA_PATH = ROOT / "repository/data/schemas/commercial-pilot-candidate.schema.json"
C002_CANDIDATE_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
C002_ADMIN_CONTRACT_PATH = ROOT / "repository/data/contracts/product-administration-policy.contract.yaml"
C002_ADMIN_SCHEMA_PATH = ROOT / "repository/data/schemas/product-administration-policy.schema.json"
C002_ADMIN_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c002/product-administration-policies.yaml"
C005_CONTRACT_PATH = ROOT / "repository/data/contracts/c005-founder-evidence-readiness.contract.yaml"
C005_SCHEMA_PATH = ROOT / "repository/data/schemas/c005-founder-evidence-readiness.schema.json"
C005_REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c005/201-51-founder-evidence-readiness.yaml"
PRODUCT_ENTITIES_PATH = ROOT / "repository/data/registries/product-entities.yaml"

# Pinned only after independent review of the final semantic objects.
EXPECTED_CONTRACT_DIGEST = "555b72cb245a8cd190aa8fe240b6003a3fa4d5210eca843356aaad496d052a2e"
EXPECTED_SCHEMA_DIGEST = "d309d179fb2626d41f7736b034e02eab9a5ff8a3d3e98bb8811ce8b9d24209da"
EXPECTED_REGISTRY_DIGEST = "4f15c0c423f29820e78a4fc09cfb020818ef2ca7af35f758c09723353de566e9"
EXPECTED_SYNTHETIC_REGISTRY_DIGEST = "d31147ac3ce4a36772b7cffc3bd783bf4c1076962df8a3fdcb9a618fa7212f1c"

EXPECTED_MAIN = "5a6fcbf368f817e88fca070a111fecbe65c4511a"
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
EXPECTED_SIX = [
    "DEMAND_SIGNAL",
    "GROSS_PROFIT_POTENTIAL",
    "REPEATABILITY",
    "PRODUCT_DATA_COMPLETENESS",
    "SEO_BUYER_INTENT",
    "OPERATIONAL_COMPLEXITY",
]
EXPECTED_TERMINAL = [
    "VERIFIED",
    "SUBMITTED_REVIEW_INCOMPLETE",
    "VERIFIED",
    "VERIFIED",
    "SUBMITTED_REVIEW_INCOMPLETE",
    "MISSING_EVIDENCE",
    "SUBMITTED_REVIEW_INCOMPLETE",
    "VERIFIED",
    "SUBMITTED_REVIEW_INCOMPLETE",
]
EXPECTED_C002_MAPPED = ["VERIFIED", "SUBMITTED", "VERIFIED", "VERIFIED", "SUBMITTED", "MISSING", "SUBMITTED", "VERIFIED", "SUBMITTED"]
EXPECTED_C005_STATES = ["SUBMITTED", "SUBMITTED", "SUBMITTED", "SUBMITTED", "SUBMITTED", "MISSING", "SUBMITTED", "SUBMITTED", "SUBMITTED"]
EXPECTED_LANES = [
    "LANE_A_INDEPENDENT_REVIEW",
    "LANE_B_SUPPLY_FULFILLMENT",
    "LANE_A_INDEPENDENT_REVIEW",
    "LANE_A_INDEPENDENT_REVIEW",
    "LANE_A_INDEPENDENT_REVIEW",
    "LANE_C_RIGHTS_SAFE_MEDIA",
    "LANE_D_CONDITIONAL_SEO",
    "LANE_A_INDEPENDENT_REVIEW",
    "LANE_B_SUPPLY_FULFILLMENT",
]
EXPECTED_EVIDENCE_CLASSES = [
    "REPOSITORY_CANONICAL_EVIDENCE",
    "MISSING_EVIDENCE",
    "FOUNDER_CONFIRMED_EVIDENCE",
    "FOUNDER_CONFIRMED_EVIDENCE",
    "REPOSITORY_CANONICAL_EVIDENCE",
    "MISSING_EVIDENCE",
    "REPOSITORY_CANONICAL_EVIDENCE",
    "REPOSITORY_CANONICAL_EVIDENCE",
    "MISSING_EVIDENCE",
]
EXPECTED_SOURCE_LOCATORS = [
    "slack:C0BNHRRTE9F:1787343117.499159",
    "slack-file:F0BRTDC1LH3:sha256:4298addbde0c12cc6f4c4653ab5a33b3f6f17c69c485dd01a7581c98981591e5",
]
EXPECTED_SOURCES = [
    {
        "source_id": "C008-SOURCE-001",
        "source_role": "EXECUTION_AUTHORIZATION",
        "source_locator": EXPECTED_SOURCE_LOCATORS[0],
        "captured_at": "2026-08-21T23:41:57.499159+03:30",
        "title": "DS-P1-M3-PACKET-01 — FOUNDER EXECUTION AUTHORIZATION — C008 — 2026-08-21",
        "author_id": "U0BNFS43TBL",
        "thread_complete": True,
    },
    {
        "source_id": "C008-SOURCE-002",
        "source_role": "PACKET",
        "source_locator": EXPECTED_SOURCE_LOCATORS[1],
        "captured_at": "2026-08-21T23:42:06.534289+03:30",
        "title": "DAMAVAND_M3_C008_FOUNDER_REVIEW_PACKAGE_v1.0.zip",
        "author_id": "U0BNFS43TBL",
        "thread_complete": True,
    },
]
EXPECTED_SOURCE_POLICY = {
    "slack_channel_id": "C0BNHRRTE9F",
    "founder_user_id": "U0BNFS43TBL",
    "execution_authorization_parent_ts": "1787343117.499159",
    "packet_reply_ts": "1787343126.534289",
    "slack_file_id": "F0BRTDC1LH3",
    "packet_zip_sha256": "4298addbde0c12cc6f4c4653ab5a33b3f6f17c69c485dd01a7581c98981591e5",
    "complete_thread_required": True,
    "exact_reply_count": 1,
    "packet_internal_manifest_required": True,
    "packet_planning_status_is_superseded_only_by_exact_execution_authorization": True,
    "public_research_is_supplementary_only": True,
    "public_research_can_prove_query_volume_or_buyer_demand": False,
    "public_research_requires_prior_insufficiency_review": True,
    "conditional_public_research_triggered": False,
    "public_research_record_count": 0,
}
EXPECTED_EVIDENCE_SOURCE_LOCATORS = [
    ["repository:repository/data/registries/extensions/c005/201-51-founder-evidence-readiness.yaml"],
    ["repository:docs/C005_201_51_READINESS_REEVALUATION_PACKET_V1.0.md#criterion-contract"],
    ["slack:C0BNHRRTE9F:1787056479.144299"],
    ["slack:C0BNHRRTE9F:1787056479.144299", "slack:C0BNHRRTE9F:1787080149.589239"],
    ["repository:repository/data/registries/extensions/c003r2/201-51-founder-evidence-completion.yaml"],
    ["repository:docs/C005_201_51_READINESS_REEVALUATION_PACKET_V1.0.md#founder-evidence-boundaries"],
    [
        "repository:repository/data/registries/extensions/c005/201-51-founder-evidence-readiness.yaml",
        "repository:docs/201_51_PILOT_COMPETITIVE_EXPERIENCE_BLUEPRINT_V1.0.md",
    ],
    ["repository:repository/data/registries/extensions/c005/201-51-founder-evidence-readiness.yaml"],
    ["repository:docs/C005_201_51_READINESS_REEVALUATION_PACKET_V1.0.md#criterion-contract"],
]
EXPECTED_BASE_REFS = [
    ["C003-DISC-011", "C003-DISC-017", "C003-DISC-018", "C005-EVID-002", "C005-EVID-006"],
    ["C003R1-CP03-001", "C003R1-CP03-002", "C003R1-CP03-003", "C005-EVID-003"],
    ["C005-EVID-001"],
    ["C005-EVID-002", "C005-EVID-006"],
    ["C003R1-CP03-026", "C003R1-CP03-027", "C003R1-CP03-028", "C003R1-CP03-030", "C003R1-CP03-031", "C003R3-ANSWER-001", "C005-EVID-006"],
    ["C005-EVID-004", "C005-EVID-005"],
    ["C005-EVID-005", "C005-EVID-006", "docs/201_51_PILOT_COMPETITIVE_EXPERIENCE_BLUEPRINT_V1.0.md"],
    ["C003R1-CP03-032", "C003R1-CP03-034", "C003R1-CP03-041", "C003R1-CP03-053", "C005-EVID-007", "C005-EVID-008", "C005-EVID-009", "C005-EVID-010", "C005-EVID-011", "C005-EVID-013", "C005-EVID-014"],
    ["C003R1-CP03-007", "C003R1-CP03-008", "C003R1-CP03-041", "C003R1-CP03-042", "C003R1-CP03-043", "C005-EVID-003", "C005-EVID-013"],
]
EXPECTED_SUPPORTED_CLAIMS = [
    [
        "Founder evidence supports recurring/core 201/51 demand and bounded buyer/application context.",
        "Demand priority does not create Product, bundle, stock, Availability or price truth.",
    ],
    [],
    [
        "Founder evidence supports normal positive gross-profit potential with operator discretion.",
        "Exceptional breakeven or loss cases prevent inference of a mandatory margin floor.",
    ],
    [
        "Founder evidence directly classifies 201/51 demand as recurring and core.",
        "Bounded audience, application and high-demand configuration context supports repeatability review.",
    ],
    [
        "All 216 bounded review positions have Founder-confirmed valid evidence.",
        "Evidence completeness is sufficient for review but not canonical promotion.",
    ],
    [],
    [
        "Existing Founder evidence identifies bounded buyer/application context.",
        "Governed C004 planning describes a future research approach but is non-verifying.",
    ],
    [
        "Canonical evidence identifies the operator workflow, exception and future-capability complexity boundaries.",
        "Inquiry-First Pilot-critical complexity is reviewable without implementing deferred features.",
    ],
    [],
]
EXPECTED_UNSUPPORTED_CLAIMS = [
    ["No public stock, sales-volume quantity or universal market-share claim is supported."],
    [
        "General sourcing history does not establish a current supplier commitment.",
        "No stock, Availability, quantity, price or guaranteed lead time may be inferred.",
    ],
    ["No cost, margin, revenue, threshold or pricing authority is established."],
    ["The 51/38/16 pattern is not a mandatory bundle, quantity rule, SKU or Availability fact."],
    ["No Product, controlled value, persisted tuple, Variant Rule, SKU or Availability is created."],
    [
        "Editing, cropping, cleaning, recoloring or background removal cannot create media rights.",
        "Internet or competitor media is not production-safe by default.",
    ],
    [
        "Existing application evidence does not prove query demand, search volume, conversion, ranking or market share.",
        "No additional public research was admitted because the prerequisite insufficiency trigger was not durably recorded before research.",
    ],
    [
        "Public pricing, cart, checkout, payment, VIP, Loyalty, AI, FX, marketplace and full catalog are not Pilot-critical requirements.",
        "Verification creates no workflow, customer, order, pricing or Runtime implementation.",
    ],
    [
        "Typical same-day or next-day sourcing is not a commitment or guaranteed ETA.",
        "No stock, Availability, shipping implementation or customer promise is established.",
    ],
]
EXPECTED_G1_MISSING_EVIDENCE = [
    "Supplier-specific Supply evidence with scope, timestamp, validity and independent reviewer.",
    "Current fulfillment commitment and exception evidence without stock or lead-time inference.",
    "Owned or licensed production-ready 201/51 media with rights and applicability review.",
    "Independent bounded buyer-intent evidence beyond existing Founder/application and planning evidence.",
    "Separately authorized canonical Product and Variant Rules promotion after evidence review.",
]
EXPECTED_TOTALS = {
    "criterion_count": 9,
    "verified_count": 4,
    "not_applicable_approved_count": 0,
    "submitted_review_incomplete_count": 4,
    "missing_evidence_count": 1,
    "conflicting_evidence_count": 0,
    "expired_or_stale_evidence_count": 0,
    "resolved_count": 4,
    "unresolved_count": 5,
    "open_blocking_count": 5,
    "readiness": "NOT_READY",
    "founder_selection_ready": False,
    "candidate_registry_count": 0,
}
EXPECTED_CLASS_COUNTS = {
    "REPOSITORY_CANONICAL_EVIDENCE": 4,
    "FOUNDER_CONFIRMED_EVIDENCE": 2,
    "SUPPLIER_SPECIFIC_EVIDENCE": 0,
    "RIGHTS_SAFE_MEDIA_EVIDENCE": 0,
    "PUBLIC_RESEARCH_EVIDENCE": 0,
    "PROTECTED_COMMERCIAL_EVIDENCE": 0,
    "MISSING_EVIDENCE": 3,
    "CONFLICTING_EVIDENCE": 0,
}
EXPECTED_BASE_PINS = {
    "c002_candidate_contract_semantic_sha256": "923731cb080b0ecc05abb21b1189bfdd0df94297780cce364bb791479f7f47e3",
    "c002_candidate_schema_semantic_sha256": "1e1b1977f369ab7e5961d4e69111682d1117bc6eeedf666a9e568f0115952741",
    "c002_candidate_registry_semantic_sha256": "deb0215d2b5f4b5ec0061f937aec9c3e37cf97c94432a23737bf5756cef9587e",
    "c002_product_administration_contract_semantic_sha256": "75b608e67b6ca3c870e6bf0b533310fbb131a75fa576a79e75c4a936659c33ff",
    "c002_product_administration_schema_semantic_sha256": "a24d0e5118c371078cad05f20952ca6d27f95e11a9d37cc1b91f0ea6e9a368ac",
    "c002_product_administration_registry_semantic_sha256": "796d2dfc424a75f998b309f04e88443d0ffb7450bd457bddf86b574535624fe7",
    "c005_contract_semantic_sha256": "e10707317a3a7c455e3205fed0e058d61c616fd2db126c4862c7f318757e03fa",
    "c005_schema_semantic_sha256": "77e392a4d0f39dc3bb8851837e5b49ffb62e302de0c262055d351821549a3bb4",
    "c005_registry_semantic_sha256": "553da985f1a4e655ff34b0d85cc56bb078365c4cd3ec86f3e270e8cadf416e8b",
}
EXPECTED_REGRESSION = {
    "c002_candidate_count": 0,
    "c002_policy_count": 8,
    "c002_policy_instance_count": 0,
    "c005_source_count": 5,
    "c005_evidence_record_count": 17,
    "c005_submitted_count": 8,
    "c005_missing_count": 1,
    "c005_reviewable_count": 6,
    "c005_resolved_count": 0,
    "c005_open_blocking_count": 9,
    "c003_r3_confirmed_valid_evidence_count": 216,
    "canonical_product_entity_count": 3,
    "canonical_sku_count": 0,
    "current_numeric_mass_observation_count": 0,
    "current_supply_intake_record_count": 0,
    "current_price_value_count": 0,
    "customer_object_count": 0,
    "order_object_count": 0,
    "active_vip_entitlement_count": 0,
    "active_loyalty_ledger_count": 0,
    "commerce_state": "INQUIRY_ONLY",
    "runtime_authority": "NONE",
    "production_authority": "NONE",
    "c1_t03_state": "FROZEN_AT_PROTECTED_ARCHITECTURE_BOUNDARY",
}


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def load_validator(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[Any, dict[str, Any]]:
    contract = require_mapping(load_yaml(safe_path(contract_path, "C008 contract")), "C008 contract")
    schema = require_mapping(load_json(safe_path(schema_path, "C008 schema")), "C008 schema")
    schema_issues = audit_schema(schema)
    if schema_issues:
        raise ValidationConfigurationError(schema_issues[0])
    if EXPECTED_CONTRACT_DIGEST in {"", "TO_BE_FINALIZED", None}:
        raise ValidationConfigurationError("C008 contract digest is not pinned")
    if EXPECTED_SCHEMA_DIGEST in {"", "TO_BE_FINALIZED", None}:
        raise ValidationConfigurationError("C008 schema digest is not pinned")
    if EXPECTED_SYNTHETIC_REGISTRY_DIGEST in {"", "TO_BE_FINALIZED", None}:
        raise ValidationConfigurationError("C008 synthetic registry digest is not pinned")
    if semantic_digest(contract) != EXPECTED_CONTRACT_DIGEST:
        raise ValidationConfigurationError("C008 contract literal policy differs")
    if semantic_digest(schema) != EXPECTED_SCHEMA_DIGEST:
        raise ValidationConfigurationError("C008 schema literal policy differs")
    return validate_schema(schema), contract


def validate_dependency_pins(add: Any, contract: dict[str, Any]) -> None:
    paths = {
        "c002_candidate_contract_semantic_sha256": C002_CANDIDATE_CONTRACT_PATH,
        "c002_candidate_schema_semantic_sha256": C002_CANDIDATE_SCHEMA_PATH,
        "c002_candidate_registry_semantic_sha256": C002_CANDIDATE_REGISTRY_PATH,
        "c002_product_administration_contract_semantic_sha256": C002_ADMIN_CONTRACT_PATH,
        "c002_product_administration_schema_semantic_sha256": C002_ADMIN_SCHEMA_PATH,
        "c002_product_administration_registry_semantic_sha256": C002_ADMIN_REGISTRY_PATH,
        "c005_contract_semantic_sha256": C005_CONTRACT_PATH,
        "c005_schema_semantic_sha256": C005_SCHEMA_PATH,
        "c005_registry_semantic_sha256": C005_REGISTRY_PATH,
    }
    live: dict[str, str] = {}
    for key, path in paths.items():
        value = load_json(safe_path(path, key)) if path.suffix == ".json" else load_yaml(safe_path(path, key))
        live[key] = semantic_digest(value)
    if contract.get("base_pins") != EXPECTED_BASE_PINS or live != EXPECTED_BASE_PINS:
        add("DEPENDENCY_PIN_REGRESSION", "C002 and C005 owners must match exact semantic pins")

    candidate = require_mapping(load_yaml(safe_path(C002_CANDIDATE_REGISTRY_PATH, "C002 candidate registry")), "C002 candidate registry")
    admin = require_mapping(load_yaml(safe_path(C002_ADMIN_REGISTRY_PATH, "C002 admin registry")), "C002 admin registry")
    c005 = require_mapping(load_yaml(safe_path(C005_REGISTRY_PATH, "C005 registry")), "C005 registry")
    if candidate.get("candidates") != []:
        add("C002_CANDIDATE_REGRESSION", "C002 candidate registry must remain empty")
    if len(admin.get("policies", [])) != 8 or admin.get("instances") != []:
        add("C002_POLICY_REGRESSION", "C002 must remain eight policies and zero instances")
    totals = c005.get("c002_readiness_reevaluation", {}).get("totals")
    if totals != {
        "criterion_count": 9,
        "verified_count": 0,
        "submitted_count": 8,
        "missing_count": 1,
        "reviewable_count": 6,
        "resolved_count": 0,
        "unresolved_count": 9,
        "open_blocking_count": 9,
    }:
        add("C005_READINESS_REGRESSION", "C005 predecessor must remain 0/9 with its exact planning totals")
    if len(c005.get("source_manifest", {}).get("sources", [])) != 5 or len(c005.get("evidence_records", [])) != 17:
        add("C005_EVIDENCE_REGRESSION", "C005 must retain five sources and seventeen evidence records")
    if c005.get("regression_anchors", {}).get("c003_r3_confirmed_valid_evidence_count") != 216:
        add("C003_R3_REGRESSION", "C003-R3 must remain 216 evidence positions")
    product_entities = load_yaml(safe_path(PRODUCT_ENTITIES_PATH, "Product entities"))
    if not isinstance(product_entities, list) or len(product_entities) != 3:
        add("PRODUCT_ENTITY_REGRESSION", "canonical hierarchy entity count must remain three")
    if any(isinstance(item, dict) and item.get("entity_type") == "SKU" for item in product_entities if isinstance(product_entities, list)):
        add("SKU_REGRESSION", "canonical SKU count must remain zero")


def validate_registry(
    value: Any,
    schema_validator: Any,
    contract: dict[str, Any],
    *,
    synthetic_mode: bool = False,
) -> list[str]:
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

    contract_authority = contract.get("authority", {})
    if contract.get("contract_id") != "c008-c002-readiness-evidence-closure" or contract.get("contract_version") != "1.0.0":
        add("CONTRACT_IDENTITY", "C008 contract identity/version must remain exact")
    allowed_true = {
        "evidence_intake_and_normalization_allowed",
        "independent_c002_review_allowed",
        "g1_decision_surface_allowed",
        "repository_docs_contract_schema_validator_test_work_allowed",
        "branch_commit_push_pr_allowed",
    }
    if not isinstance(contract_authority, dict) or any(
        value is not (key in allowed_true)
        for key, value in contract_authority.items()
        if key not in {"mission_id", "packet_id", "packet_version"}
    ):
        add("CONTRACT_AUTHORITY", "C008 contract may grant only five bounded evidence/repository execution capabilities")
    if {key: contract_authority.get(key) for key in ["mission_id", "packet_id", "packet_version"]} != {
        "mission_id": "C008", "packet_id": "DS-P1-M3-PACKET-01", "packet_version": "1.0"
    }:
        add("CONTRACT_AUTHORITY", "C008 contract must bind exact Mission and Packet authority")
    if contract.get("source_policy") != EXPECTED_SOURCE_POLICY:
        add("CONTRACT_SOURCE_POLICY", "conditional public research must require a prior insufficiency review and remain untriggered")
    readiness_policy = contract.get("c002_readiness_policy", {})
    if readiness_policy.get("criterion_order") != EXPECTED_CRITERIA or readiness_policy.get("six_immediate_review_order") != EXPECTED_SIX:
        add("CONTRACT_CRITERIA", "C008 contract must retain exact nine criteria and six-review order")
    if readiness_policy.get("exact_terminal_vector") != EXPECTED_TERMINAL or readiness_policy.get("exact_totals") != {key: value for key, value in EXPECTED_TOTALS.items() if key not in {"readiness", "founder_selection_ready", "candidate_registry_count"}}:
        add("CONTRACT_READINESS", "C008 contract must retain exact terminal vector and 4/9 totals")
    if readiness_policy.get("weighted_scoring_allowed") is not False or readiness_policy.get("founder_selection_ready") is not False or readiness_policy.get("candidate_registry_count") != 0:
        add("CONTRACT_READINESS", "C008 contract forbids weighted scoring, selection readiness and candidate population")
    if contract.get("g1_policy") != {
        "decision_surface_only": True,
        "recommendation_is_selection": False,
        "exact_result": "HOLD_NOT_READY_4_OF_9",
        "exact_m4_candidate": None,
        "founder_decision_required": "HOLD_M4_AND_REQUEST_REMAINING_REAL_WORLD_EVIDENCE",
        "m4_authorized": False,
    }:
        add("CONTRACT_G1", "C008 contract G1 must remain a non-selecting hold with no M4 candidate")
    if contract.get("regression_anchors") != EXPECTED_REGRESSION:
        add("CONTRACT_REGRESSION", "C008 contract regression anchors must remain exact")

    expected_registry_digest = EXPECTED_SYNTHETIC_REGISTRY_DIGEST if synthetic_mode else EXPECTED_REGISTRY_DIGEST
    if expected_registry_digest in {"", "TO_BE_FINALIZED", None}:
        add("SEMANTIC_DIGEST", "C008 registry digest is not pinned")
    elif semantic_digest(value) != expected_registry_digest:
        add("REGISTRY_DIGEST", "C008 registry differs from the independently reviewed package")
    expected_fixture_mode = "SYNTHETIC" if synthetic_mode else "CANONICAL"
    if value.get("fixture_mode") != expected_fixture_mode:
        add("FIXTURE_MODE", f"C008 {expected_fixture_mode.lower()} validation requires exact fixture mode")
    if value.get("mission_id") != "C008" or value.get("starting_main_sha") != EXPECTED_MAIN:
        add("MISSION_ANCHOR", "C008 mission and starting main must remain exact")

    packet = value.get("packet", {})
    expected_packet = {
        "packet_id": "DS-P1-M3-PACKET-01",
        "packet_version": "1.0",
        "slack_channel_id": "C0BNHRRTE9F",
        "authorization_parent_ts": "1787343117.499159",
        "packet_reply_ts": "1787343126.534289",
        "slack_file_id": "F0BRTDC1LH3",
        "packet_zip_sha256": "4298addbde0c12cc6f4c4653ab5a33b3f6f17c69c485dd01a7581c98981591e5",
        "thread_complete": True,
        "reply_count": 1,
    }
    if packet != expected_packet:
        add("AUTHORIZATION_SOURCE", "C008 must bind the exact complete Slack authorization and packet")
    expected_authority = {
        "evidence_intake_and_normalization": True,
        "independent_c002_review": True,
        "g1_decision_surface": True,
        "candidate_population": False,
        "product_population": False,
        "controlled_value_promotion": False,
        "valid_tuple_promotion": False,
        "sku_assignment": False,
        "mass_population": False,
        "supply_truth_population": False,
        "availability_or_stock_claim": False,
        "price_or_pricing_authority": False,
        "commerce_eligibility_population": False,
        "customer_lead_order_payment_population": False,
        "media_publication": False,
        "seo_publication": False,
        "wordpress_woocommerce_mutation": False,
        "runtime_staging_production": False,
        "deployment_import_hosting_database": False,
        "workflow_secret_repository_settings_mutation": False,
        "m4_start": False,
        "successor_mission": False,
        "auto_merge": False,
        "merge": False,
    }
    if value.get("authority_effects") != expected_authority:
        add("AUTHORITY_EFFECT", "C008 grants only evidence normalization, independent review and a G1 surface")

    sources = value.get("source_manifest", {}).get("sources", [])
    if [item.get("source_id") for item in sources if isinstance(item, dict)] != [f"C008-SOURCE-{index:03d}" for index in range(1, 3)]:
        add("SOURCE_ORDER", "C008 source IDs/order must be exact")
    expected_source_roles = ["EXECUTION_AUTHORIZATION", "PACKET"]
    if [item.get("source_role") for item in sources if isinstance(item, dict)] != expected_source_roles:
        add("SOURCE_ROLE", "C008 source roles must distinguish authorization, packet and public research")
    if [item.get("source_locator") for item in sources if isinstance(item, dict)] != EXPECTED_SOURCE_LOCATORS:
        add("SOURCE_LOCATOR", "C008 source locators must remain exact and attributable")
    if sources != EXPECTED_SOURCES:
        add("SOURCE_OBJECT_EXACTNESS", "every C008 source field must remain exactly bound to its attributable source")
    if len(sources) != 2 or value.get("source_manifest", {}).get("source_count") != 2:
        add("SOURCE_COUNT", "C008 source manifest must contain exactly authorization and Packet sources")
    if any(item.get("source_role") == "PUBLIC_RESEARCH" for item in sources if isinstance(item, dict)):
        add("CONDITIONAL_RESEARCH_GATE", "public research cannot be admitted without a durable prior insufficiency-review trigger")

    evidence = value.get("evidence_items", [])
    evidence_ids = [item.get("evidence_id") for item in evidence if isinstance(item, dict)]
    if evidence_ids != [f"C008-EVID-{index:03d}" for index in range(1, 10)]:
        add("EVIDENCE_ORDER", "C008 evidence IDs/order must be exact")
    if [item.get("sequence") for item in evidence if isinstance(item, dict)] != list(range(1, 10)):
        add("EVIDENCE_SEQUENCE", "C008 evidence sequence must be exact")
    if [item.get("criterion_code") for item in evidence if isinstance(item, dict)] != EXPECTED_CRITERIA:
        add("EVIDENCE_CRITERION_BINDING", "each criterion must have exactly one ordered C008 evidence item")
    if [item.get("evidence_class") for item in evidence if isinstance(item, dict)] != EXPECTED_EVIDENCE_CLASSES:
        add("EVIDENCE_CLASS", "C008 evidence classes must match the reviewed closure result")
    if [item.get("source_locators") for item in evidence if isinstance(item, dict)] != EXPECTED_EVIDENCE_SOURCE_LOCATORS:
        add("EVIDENCE_SOURCE_BINDING", "every C008 evidence item must retain exact source locators")
    if [item.get("base_evidence_refs") for item in evidence if isinstance(item, dict)] != EXPECTED_BASE_REFS:
        add("EVIDENCE_BASE_BINDING", "every C008 evidence item must retain exact canonical predecessor refs")
    if [item.get("supported_claims") for item in evidence if isinstance(item, dict)] != EXPECTED_SUPPORTED_CLAIMS:
        add("EVIDENCE_CLAIM_BINDING", "supported claims must remain exactly bounded to reviewed source evidence")
    if [item.get("unsupported_claims") for item in evidence if isinstance(item, dict)] != EXPECTED_UNSUPPORTED_CLAIMS:
        add("EVIDENCE_CLAIM_BINDING", "unsupported-claim guardrails must remain exact and fail closed")
    if any(item.get("evidence_class") == "PUBLIC_RESEARCH_EVIDENCE" for item in evidence if isinstance(item, dict)):
        add("CONDITIONAL_RESEARCH_GATE", "C008 recorded no admissible public research because the prerequisite trigger was absent")
    evaluation = parse_time(value.get("evaluation_as_of"))
    for item in evidence:
        if not isinstance(item, dict):
            continue
        evidence_id = item.get("evidence_id")
        captured = parse_time(item.get("captured_at"))
        valid_from = parse_time(item.get("valid_from"))
        valid_until = parse_time(item.get("valid_until")) if item.get("valid_until") is not None else None
        if evaluation is None or captured is None or valid_from is None or captured > evaluation or valid_from > evaluation:
            add("EVIDENCE_TIME", f"{evidence_id} must be captured and valid by evaluation time")
        if valid_until is not None and (valid_from is None or valid_until < valid_from or evaluation > valid_until):
            add("FRESHNESS_FAIL_CLOSED", f"{evidence_id} cannot be expired at evaluation")
        if item.get("evidence_class") == "PUBLIC_RESEARCH_EVIDENCE" and valid_until is None:
            add("PUBLIC_RESEARCH_FRESHNESS", f"{evidence_id} public research requires a bounded validity window")
        if item.get("owner") == item.get("reviewer"):
            add("REVIEW_INDEPENDENCE", f"{evidence_id} reviewer must be independent from owner")
        if item.get("conflicts"):
            add("CONFLICT_FAIL_CLOSED", f"{evidence_id} conflict set must be empty for the current outcome")
        if item.get("evidence_class") == "MISSING_EVIDENCE":
            if item.get("freshness_status") != "MISSING" or item.get("supported_claims"):
                add("MISSING_EVIDENCE_SEMANTICS", f"{evidence_id} missing evidence cannot support claims")
        elif item.get("freshness_status") != "CURRENT":
            add("FRESHNESS_FAIL_CLOSED", f"{evidence_id} non-missing evidence must be current")
        protected_locator = item.get("protected_locator")
        if item.get("evidence_class") != "PROTECTED_COMMERCIAL_EVIDENCE" and protected_locator is not None:
            add("PROTECTED_LOCATOR_BOUNDARY", f"{evidence_id} non-protected evidence cannot carry a protected locator")
        if item.get("evidence_class") == "PROTECTED_COMMERCIAL_EVIDENCE":
            if not isinstance(protected_locator, str) or not re.fullmatch(r"protected-evidence:[A-Za-z0-9._:/-]+", protected_locator):
                add("PROTECTED_LOCATOR_BOUNDARY", f"{evidence_id} protected evidence requires an opaque durable locator")
        if isinstance(protected_locator, str) and re.search(r"(?i)(cost|margin|price|secret|value|amount)\s*[=:]", protected_locator):
            add("PROTECTED_VALUE_LEAK", f"{evidence_id} protected locator must not embed commercial values")
        if item.get("promotion_effect") is not False or item.get("implementation_authority") is not False:
            add("EVIDENCE_PROMOTION", f"{evidence_id} must remain evidence-only")

    counts = Counter(item.get("evidence_class") for item in evidence if isinstance(item, dict))
    summary = value.get("evidence_summary", {})
    if summary.get("total") != 9 or summary.get("by_class") != {key: counts.get(key, 0) for key in EXPECTED_CLASS_COUNTS}:
        add("EVIDENCE_SUMMARY", "evidence summary must derive exactly from nine items")
    if summary.get("by_class") != EXPECTED_CLASS_COUNTS:
        add("EVIDENCE_CLASS_COUNTS", "C008 exact evidence-class counts must remain fixed")
    if any(summary.get(key) != 0 for key in ["protected_count", "conflicting_count", "stale_count", "supplier_specific_count", "rights_safe_media_count"]):
        add("REAL_WORLD_EVIDENCE_BOUNDARY", "no supplier-specific, rights-safe, protected, conflicting or stale item was supplied")

    reviews = value.get("criterion_reviews", [])
    if [item.get("criterion_code") for item in reviews if isinstance(item, dict)] != EXPECTED_CRITERIA:
        add("CRITERION_ORDER", "all nine criteria must be classified in exact order")
    if [item.get("sequence") for item in reviews if isinstance(item, dict)] != list(range(1, 10)):
        add("CRITERION_SEQUENCE", "criterion review sequence must be exact")
    if [item.get("terminal_state") for item in reviews if isinstance(item, dict)] != EXPECTED_TERMINAL:
        add("TERMINAL_STATE_VECTOR", "C008 terminal-state vector must remain exact")
    if [item.get("c002_mapped_state") for item in reviews if isinstance(item, dict)] != EXPECTED_C002_MAPPED:
        add("C002_STATE_MAPPING", "terminal states must map to C002 states without rewriting C002")
    if [item.get("c005_state") for item in reviews if isinstance(item, dict)] != EXPECTED_C005_STATES:
        add("C005_STATE_BINDING", "C005 predecessor states must remain exact")
    if [item.get("review_lane") for item in reviews if isinstance(item, dict)] != EXPECTED_LANES:
        add("REVIEW_LANE", "review and evidence lanes must remain exact")
    if [item.get("evidence_ids") for item in reviews if isinstance(item, dict)] != [[f"C008-EVID-{index:03d}"] for index in range(1, 10)]:
        add("REVIEW_EVIDENCE_BINDING", "each criterion must bind its exact one C008 evidence item")
    if [item.get("base_evidence_refs") for item in reviews if isinstance(item, dict)] != EXPECTED_BASE_REFS:
        add("REVIEW_BASE_BINDING", "criterion reviews must preserve exact predecessor evidence refs")
    reviewed_six = [item.get("criterion_code") for item in reviews if isinstance(item, dict) and item.get("review_lane") in {"LANE_A_INDEPENDENT_REVIEW", "LANE_D_CONDITIONAL_SEO"}]
    if reviewed_six != EXPECTED_SIX:
        add("SIX_REVIEW_SCOPE", "exactly the six C005 reviewable criteria must receive independent review")
    evidence_id_set = set(evidence_ids)
    for item in reviews:
        if not isinstance(item, dict):
            continue
        code = item.get("criterion_code")
        state = item.get("terminal_state")
        resolved = state in {"VERIFIED", "NOT_APPLICABLE_APPROVED"}
        if item.get("resolved") is not resolved or item.get("blocking") is resolved:
            add("RESOLUTION_SEMANTICS", f"{code} resolved/blocking flags must derive from terminal state")
        if resolved and item.get("remaining_requirement") is not None:
            add("RESOLUTION_REQUIREMENT", f"{code} resolved review cannot retain a blocker")
        if not resolved and not item.get("remaining_requirement"):
            add("UNRESOLVED_REQUIREMENT", f"{code} unresolved review requires an exact remaining requirement")
        if item.get("independent_reviewer") in {item.get("submitter"), item.get("evidence_owner")}:
            add("REVIEW_INDEPENDENCE", f"{code} reviewer must be independent")
        reviewed_at = parse_time(item.get("reviewed_at"))
        item_evidence = next((record for record in evidence if isinstance(record, dict) and record.get("evidence_id") in item.get("evidence_ids", [])), None)
        captured_at = parse_time(item_evidence.get("captured_at")) if isinstance(item_evidence, dict) else None
        if reviewed_at is None or evaluation is None or captured_at is None or reviewed_at < captured_at or reviewed_at > evaluation:
            add("REVIEW_TEMPORAL_ORDER", f"{code} review must occur after capture and by evaluation time")
        if any(ref not in evidence_id_set for ref in item.get("evidence_ids", [])):
            add("REVIEW_EVIDENCE_REF", f"{code} references unknown C008 evidence")
        if item.get("promotion_effect") is not False:
            add("CRITERION_PROMOTION", f"{code} cannot promote Product or C002 state")
    seo = next((item for item in reviews if isinstance(item, dict) and item.get("criterion_code") == "SEO_BUYER_INTENT"), {})
    if seo.get("terminal_state") == "VERIFIED":
        add("SEO_EVIDENCE_NOT_VERIFIER", "existing Founder/application evidence and planning cannot independently verify buyer intent")
    product = next((item for item in reviews if isinstance(item, dict) and item.get("criterion_code") == "PRODUCT_DATA_COMPLETENESS"), {})
    if product.get("terminal_state") == "VERIFIED":
        add("PRODUCT_PROMOTION_BOUNDARY", "Product Data Completeness cannot verify before separately authorized canonical promotion")

    totals = value.get("readiness_result", {})
    calculated = Counter(item.get("terminal_state") for item in reviews if isinstance(item, dict))
    derived = {
        "criterion_count": len(reviews),
        "verified_count": calculated.get("VERIFIED", 0),
        "not_applicable_approved_count": calculated.get("NOT_APPLICABLE_APPROVED", 0),
        "submitted_review_incomplete_count": calculated.get("SUBMITTED_REVIEW_INCOMPLETE", 0),
        "missing_evidence_count": calculated.get("MISSING_EVIDENCE", 0),
        "conflicting_evidence_count": calculated.get("CONFLICTING_EVIDENCE", 0),
        "expired_or_stale_evidence_count": calculated.get("EXPIRED_OR_STALE_EVIDENCE", 0),
        "resolved_count": calculated.get("VERIFIED", 0) + calculated.get("NOT_APPLICABLE_APPROVED", 0),
        "unresolved_count": len(reviews) - calculated.get("VERIFIED", 0) - calculated.get("NOT_APPLICABLE_APPROVED", 0),
        "open_blocking_count": sum(item.get("blocking") is True for item in reviews if isinstance(item, dict)),
        "readiness": "NOT_READY",
        "founder_selection_ready": False,
        "candidate_registry_count": 0,
    }
    if totals != derived or totals != EXPECTED_TOTALS:
        add("READINESS_TOTALS", "readiness must derive as 4/9 NOT_READY with five blockers")

    g1 = value.get("g1_decision_surface", {})
    expected_resolved = [code for code, state in zip(EXPECTED_CRITERIA, EXPECTED_TERMINAL) if state in {"VERIFIED", "NOT_APPLICABLE_APPROVED"}]
    expected_unresolved = [code for code, state in zip(EXPECTED_CRITERIA, EXPECTED_TERMINAL) if state not in {"VERIFIED", "NOT_APPLICABLE_APPROVED"}]
    if g1.get("result") != "HOLD_NOT_READY_4_OF_9" or g1.get("resolved_criteria") != expected_resolved or g1.get("unresolved_criteria") != expected_unresolved:
        add("G1_RESULT", "G1 must report exact 4/9 resolved and five unresolved criteria")
    if g1.get("founder_selection_ready") is not False or g1.get("m4_promotion_candidate") is not None or g1.get("m4_authorized") is not False:
        add("M4_SUCCESSOR_BOUNDARY", "G1 cannot select a candidate or authorize M4")
    if g1.get("recommendation_is_selection") is not False or g1.get("founder_decision_required") != "HOLD_M4_AND_REQUEST_REMAINING_REAL_WORLD_EVIDENCE":
        add("FOUNDER_DECISION_BOUNDARY", "G1 is a hold recommendation, never a Founder selection")
    if g1.get("missing_evidence") != EXPECTED_G1_MISSING_EVIDENCE or g1.get("conflicts") != []:
        add("G1_EVIDENCE_SURFACE", "G1 must expose five exact missing requirements and zero hidden conflicts")

    if value.get("regression_snapshot") != EXPECTED_REGRESSION:
        add("REGRESSION_SNAPSHOT", "C002-C007 no-go and zero-population anchors must remain exact")

    forbidden_keys = {
        "weighted_score", "score", "weights", "products", "product_values", "skus", "persisted_tuples",
        "mass_observations", "supply_records", "availability_records", "stock_records", "prices", "customers",
        "leads", "orders", "payments", "commerce_eligibility_instances", "runtime_objects", "wordpress_objects",
        "woocommerce_objects", "deployment_objects",
    }

    def scan(node: Any, path: str) -> None:
        if isinstance(node, dict):
            for key, child in node.items():
                if key in forbidden_keys:
                    add("FORBIDDEN_KEY", f"{path}/{key} is prohibited in C008")
                scan(child, f"{path}/{key}")
        elif isinstance(node, list):
            for index, child in enumerate(node):
                scan(child, f"{path}/{index}")

    scan(value, "<root>")
    validate_dependency_pins(add, contract)
    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--allow-unpinned", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        if args.allow_unpinned:
            contract = require_mapping(load_yaml(safe_path(CONTRACT_PATH, "C008 contract")), "C008 contract")
            schema = require_mapping(load_json(safe_path(SCHEMA_PATH, "C008 schema")), "C008 schema")
            schema_issues = audit_schema(schema)
            if schema_issues:
                raise ValidationConfigurationError(schema_issues[0])
            schema_validator = validate_schema(schema)
        else:
            schema_validator, contract = load_validator()
        registry = load_yaml(safe_path(Path(args.registry), "C008 registry"))
        issues = validate_registry(registry, schema_validator, contract, synthetic_mode=args.synthetic)
        if args.allow_unpinned:
            issues = [item for item in issues if not item.startswith("[SEMANTIC_DIGEST]")]
    except (ValidationConfigurationError, ValueError, TypeError) as exc:
        print(f"[CONFIGURATION] {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print("C008 C002 readiness evidence closure validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
