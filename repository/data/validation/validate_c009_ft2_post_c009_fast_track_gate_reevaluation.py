#!/usr/bin/env python3
"""Offline fail-closed validation for the C009-FT2 gate re-evaluation delta."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import socket
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repository/data/contracts/c009-ft2-post-c009-fast-track-gate-reevaluation.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/c009-ft2-post-c009-fast-track-gate-reevaluation.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c009ft2/post-c009-fast-track-gate-reevaluation.yaml"
MAX_BYTES = 2 * 1024 * 1024
MAX_DEPTH = 100
MAX_NODES = 50_000

EXPECTED_CONTRACT_DIGEST = "0200e474df33fcd8b74308c678107d53dbc9f9999b84fa753db97fc1f1ced5e8"
EXPECTED_SCHEMA_DIGEST = "558153f5f3bba6206215be46454f6add6c8fdabc414b0105c141327a12903e82"
EXPECTED_REGISTRY_DIGEST = "51d9298e2e63b44986a921d72eabc069db5b46dfda0c614ee70d4d7e2e434d08"
EXPECTED_SYNTHETIC_DIGEST = "cd4e8b06367e3ec98f277b814e1d9397e2cfdd80e7afef1045dac64cd8c4fc57"

EXPECTED_SCHEMA_BINDING = {
    "path": "repository/data/schemas/c009-ft2-post-c009-fast-track-gate-reevaluation.schema.json",
    "draft": "https://json-schema.org/draft/2020-12/schema",
}
EXPECTED_REGISTRY_BINDING = {
    "path": "repository/data/registries/extensions/c009ft2/post-c009-fast-track-gate-reevaluation.yaml"
}
EXPECTED_AUTHORITY = {
    "mission_id": "C009-FT2",
    "append_only_gate_reevaluation_delta_allowed": True,
    "exact_single_prerequisite_transition_allowed": True,
    "docs_contract_schema_registry_validator_tests_allowed": True,
    "branch_commit_push_one_pr_allowed": True,
    "c008_ft1_owner_mutation_allowed": False,
    "c009_owner_mutation_allowed": False,
    "authority_transfer_allowed": False,
    "second_prerequisite_transition_allowed": False,
    "gate_true_or_launch_authority_allowed": False,
    "c002_mutation_allowed": False,
    "candidate_population_allowed": False,
    "additional_product_combination_or_sku_population_allowed": False,
    "brand_color_or_mass_population_allowed": False,
    "availability_price_stock_eta_sla_supplier_claim_allowed": False,
    "media_right_or_asset_creation_allowed": False,
    "inquiry_crm_security_seo_performance_implementation_allowed": False,
    "wordpress_woocommerce_mutation_allowed": False,
    "runtime_staging_production_mutation_allowed": False,
    "deployment_or_publication_allowed": False,
    "m4_or_successor_mission_allowed": False,
    "auto_merge_or_merge_allowed": False,
    "branch_deletion_allowed": False,
}
EXPECTED_DEPENDENCIES = {
    "c002_contract": "repository/data/contracts/commercial-pilot-candidate.contract.yaml",
    "c002_schema": "repository/data/schemas/commercial-pilot-candidate.schema.json",
    "c002_registry": "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml",
    "c008_ft1_contract": "repository/data/contracts/c008-ft1-fast-track-inquiry-launch-gate.contract.yaml",
    "c008_ft1_schema": "repository/data/schemas/c008-ft1-fast-track-inquiry-launch-gate.schema.json",
    "c008_ft1_registry": "repository/data/registries/extensions/c008ft1/fast-track-inquiry-launch-gate.yaml",
    "c009_contract": "repository/data/contracts/c009-first-commercial-slice-canonical-leaf-promotion.contract.yaml",
    "c009_schema": "repository/data/schemas/c009-first-commercial-slice-canonical-leaf-promotion.schema.json",
    "c009_registry": "repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml",
}
EXPECTED_PINS = {
    "c002_contract": "923731cb080b0ecc05abb21b1189bfdd0df94297780cce364bb791479f7f47e3",
    "c002_schema": "1e1b1977f369ab7e5961d4e69111682d1117bc6eeedf666a9e568f0115952741",
    "c002_registry": "deb0215d2b5f4b5ec0061f937aec9c3e37cf97c94432a23737bf5756cef9587e",
    "c008_ft1_contract": "4c940eed75fe433bc8adbc85cb45954068b233cc1de6d80b40bc28eb71466fb5",
    "c008_ft1_schema": "8eb3c93a37932e6676e8a3d1c22e0c35d3f6a4d0f47f7467ea718f466ceabd80",
    "c008_ft1_registry": "799dad2f7fdf9f6ffb5a9fe37c707f222f6f92f1cc6b1e251bd3f366dd2e9cf3",
    "c009_contract": "a1179a6ef97735431f89ef075e7d40c9dd6973b5eacbeca6599d9666bc7674d3",
    "c009_schema": "aea8a6dd7b521a83576bbd00ce686d3bc2477552bc4a2f3642a80b648b6e31e2",
    "c009_registry": "1b50d28ddded3a818afb82d19759713bd6c2f2b058b4020510d8b5f74a7f6a3f",
}
EXPECTED_SOURCE_POLICY = {
    "repository": "masoudtavousi-collab/damavand-steel-platform",
    "slack_channel_id": "C0BNHRRTE9F", "founder_user_id": "U0BNFS43TBL",
    "authorization_ts": "1787478181.812239",
    "authorization_title": "FOUNDER / PROJECT COMMANDER EXECUTION AUTHORIZATION — POST-C009 FAST-TRACK GATE RE-EVALUATION — 2026-08-23",
    "authorization_thread_reply_count": 0,
    "execution_command_sha256": "243e330b51b7e89cc0a4b5faadafa880c4cf5a0376eb190644c7950e90bb46fd",
    "authorized_starting_main": "432a72ee0a22069dc33cc4cbb2a5b78e63705b74",
    "predecessor_post_merge_ci_run": 32631411970, "predecessor_post_merge_ci_result": "PASS",
    "authorized_branch": "codex/c009-ft2-post-c009-fast-track-gate-reevaluation",
    "exact_source_count": 2,
}
EXPECTED_OWNER_POLICY = {
    "model": "APPEND_ONLY_POST_C009_GATE_REEVALUATION_DELTA",
    "historical_gate_owner": "C008_FT1_FAST_TRACK_GATE", "product_identity_owner": "PRODUCT_CORE",
    "combination_validity_owner": "VARIANT_RULE_SET", "pilot_evidence_owner": "PD03B_CANONICAL_PILOT",
    "c009_role": "PERSISTENCE_AND_IMMUTABLE_BINDING_EXTENSION_ONLY",
    "c009_ft2_role": "EFFECTIVE_GATE_STATE_DELTA_ONLY",
    "c008_ft1_historical_truth_immutable": True, "c009_truth_immutable": True, "authority_transfer": False,
}
EXPECTED_TRANSITION_POLICY = {
    "gate_id": "FAST_TRACK_INQUIRY_LAUNCH_ELIGIBLE", "baseline_met_count": 4,
    "baseline_unmet_count": 8, "total_prerequisites": 12, "changed_prerequisites_count": 1,
    "changed_prerequisite_id": "CANONICAL_PRODUCT_PROMOTION_COMPLETE", "previous_state": "NOT_AUTHORIZED",
    "new_state": "MET", "effective_gate_state": False, "effective_met_count": 5,
    "effective_unmet_count": 7, "exact_evidence_binding_required": True,
    "all_other_prerequisites_unchanged": True,
}
EXPECTED_C002_POLICY = {
    "readiness": "NOT_READY", "resolved_count": 6, "unresolved_count": 3,
    "founder_selection_ready": False, "candidate_count": 0,
    "supply_evidence": "SUBMITTED_REVIEW_INCOMPLETE", "photo_content_readiness": "MISSING_EVIDENCE",
    "fulfillment_risk": "SUBMITTED_REVIEW_INCOMPLETE", "mutation_allowed": False,
}
EXPECTED_NO_CLAIM_POLICY = {
    "availability": "MISSING_DATA_VALUE", "brand": "ABSENT_NOT_PROMOTED",
    "color": "ABSENT_NOT_PROMOTED", "price": "ABSENT", "stock": "ABSENT",
    "eta_sla": "ABSENT", "supplier_truth": "ABSENT",
    "gate_reevaluation_creates_commercial_or_runtime_truth": False,
}
EXPECTED_VALIDATION = {
    "offline_only": True, "network_allowed": False, "side_effects_allowed": False,
    "closed_schema_required": True, "local_refs_only": True,
    "duplicate_yaml_and_json_keys_rejected": True, "non_finite_numbers_rejected": True,
    "deterministic_sorted_errors": True, "path_escape_symlink_byte_depth_node_caps_enforced": True,
    "exact_order_counts_and_bindings_required": True, "predecessor_semantic_pins_required": True,
    "semantic_digest_pinning_required": True, "mutation_manifest_dispatch_required": True,
}
EXPECTED_SOURCE = {
    "source_id": "C009FT2-SOURCE-001", "source_class": "FOUNDER_EXECUTION_AUTHORIZATION",
    "bound_source_count": 2, "locator": "slack:C0BNHRRTE9F:1787478181.812239",
    "channel_id": "C0BNHRRTE9F", "message_ts": "1787478181.812239",
    "author_id": "U0BNFS43TBL",
    "title": "FOUNDER / PROJECT COMMANDER EXECUTION AUTHORIZATION — POST-C009 FAST-TRACK GATE RE-EVALUATION — 2026-08-23",
    "authored_at": "2026-08-23T13:13:01.812239+03:30", "thread_complete": True, "reply_count": 0,
    "execution_command_sha256": "243e330b51b7e89cc0a4b5faadafa880c4cf5a0376eb190644c7950e90bb46fd",
    "execution_command_role": "CURRENT_FOUNDER_TASK_INSTRUCTION",
    "authorized_branch": "codex/c009-ft2-post-c009-fast-track-gate-reevaluation",
}
EXPECTED_OWNER = {
    "model": "APPEND_ONLY_POST_C009_GATE_REEVALUATION_DELTA",
    "historical_gate_owner": "C008_FT1_FAST_TRACK_GATE", "product_identity_owner": "PRODUCT_CORE",
    "combination_validity_owner": "VARIANT_RULE_SET", "pilot_evidence_owner": "PD03B_CANONICAL_PILOT",
    "c009_role": "PERSISTENCE_AND_IMMUTABLE_BINDING_EXTENSION_ONLY",
    "c009_ft2_role": "EFFECTIVE_GATE_STATE_DELTA_ONLY", "c008_ft1_owner_mutated": False,
    "c009_owner_mutated": False, "authority_transfer": False,
}
EXPECTED_EVIDENCE_REFS = [
    "git:main:432a72ee0a22069dc33cc4cbb2a5b78e63705b74", "ci:32631411970",
    "registry:c009:pilot:f5922666261e", "registry:c009:pcomb:829e387ccdcb",
    "registry:c009:prd:sku:66ebd0510693",
]
EXPECTED_BLOCKERS = [
    "RIGHTS_SAFE_MEDIA_READY", "INQUIRY_CRM_FLOW_READY", "SECURITY_PRIVACY_GATE_READY",
    "SEO_INDEXING_GATE_READY", "MOBILE_PERFORMANCE_GATE_READY", "STAGING_ACCEPTANCE_PASS",
    "PRODUCTION_FOUNDER_GO",
]
EXPECTED_C002 = {
    "relationship": "INDEPENDENT_SIBLING_NOT_ALIAS", "readiness": "NOT_READY",
    "resolved_count": 6, "unresolved_count": 3, "founder_selection_ready": False,
    "candidate_registry_count": 0, "supply_evidence": "SUBMITTED_REVIEW_INCOMPLETE",
    "photo_content_readiness": "MISSING_EVIDENCE", "fulfillment_risk": "SUBMITTED_REVIEW_INCOMPLETE",
    "state_mutation_effect": False,
}


@dataclass(frozen=True)
class Issue:
    code: str
    message: str


class StrictLoader(yaml.SafeLoader):
    pass


def _construct_mapping(loader: StrictLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


def _json_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _bounded_tree(value: Any, depth: int = 0) -> int:
    if depth > MAX_DEPTH:
        raise ValueError("document exceeds maximum depth")
    if isinstance(value, dict):
        total = 1 + sum(_bounded_tree(k, depth + 1) + _bounded_tree(v, depth + 1) for k, v in value.items())
    elif isinstance(value, list):
        total = 1 + sum(_bounded_tree(v, depth + 1) for v in value)
    else:
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("non-finite number")
        total = 1
    if total > MAX_NODES:
        raise ValueError("document exceeds maximum node count")
    return total


def safe_path(path: Path, label: str) -> Path:
    if path.is_symlink() or any(parent.is_symlink() for parent in [path, *path.parents] if parent.exists()):
        raise ValueError(f"{label}: symlink paths are forbidden")
    resolved = path.resolve(strict=True)
    resolved.relative_to(ROOT.resolve())
    if not resolved.is_file() or resolved.stat().st_size > MAX_BYTES:
        raise ValueError(f"{label}: invalid regular file or byte cap exceeded")
    return resolved


def load_document(path: Path, label: str) -> Any:
    resolved = safe_path(path, label)
    text = resolved.read_text(encoding="utf-8")
    if resolved.suffix == ".json":
        value = json.loads(text, object_pairs_hook=_json_pairs,
                           parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"non-finite JSON token: {token}")))
    else:
        value = yaml.load(text, Loader=StrictLoader)
    _bounded_tree(value)
    return value


def semantic_digest(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def add(issues: list[Issue], code: str, message: str) -> None:
    issues.append(Issue(code, message))


def audit_schema(schema: Any) -> list[Issue]:
    issues: list[Issue] = []
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        return [Issue("SCHEMA_META", str(exc))]

    forbidden = {"allOf", "anyOf", "oneOf", "not", "if", "then", "else", "dependentSchemas",
                 "contains", "patternProperties", "propertyNames", "unevaluatedProperties", "unevaluatedItems"}

    def visit(node: Any, path: str) -> None:
        if node is True:
            add(issues, "PERMISSIVE_SCHEMA", f"true schema forbidden at {path}")
            return
        if node is False:
            return
        if not isinstance(node, dict):
            return
        if not node:
            add(issues, "PERMISSIVE_SCHEMA", f"empty schema forbidden at {path}")
            return
        present = sorted(forbidden.intersection(node))
        if present:
            add(issues, "PERMISSIVE_APPLICATOR", f"unsupported applicators at {path}: {present}")
        if not any(key in node for key in ("$ref", "const", "enum", "type")):
            add(issues, "NON_ASSERTIVE_SCHEMA", f"non-assertive schema at {path}")
        ref = node.get("$ref")
        if isinstance(ref, str) and not ref.startswith("#/"):
            add(issues, "REMOTE_SCHEMA_REF", f"non-local ref at {path}")
        if isinstance(ref, str) and set(node) != {"$ref"}:
            add(issues, "REF_SIBLING", f"$ref siblings forbidden at {path}")
        node_type = node.get("type")
        if isinstance(node_type, list) and "object" in node_type:
            add(issues, "OBJECT_UNION_SCHEMA", f"object union forbidden at {path}")
        if node_type == "object" and node.get("additionalProperties") is not False:
            add(issues, "OPEN_SCHEMA", f"object is not closed at {path}")
        for key in ("properties", "$defs"):
            container = node.get(key)
            if isinstance(container, dict):
                for name, child in container.items():
                    visit(child, f"{path}/{key}/{name}")
        items = node.get("items")
        if isinstance(items, dict):
            visit(items, f"{path}/items")

    visit(schema, "#")
    return sorted(set(issues), key=lambda item: (item.code, item.message))


def validate_contract(contract: Any) -> list[Issue]:
    issues: list[Issue] = []
    if not isinstance(contract, dict):
        return [Issue("CONTRACT_TYPE", "contract must be an object")]
    expected_keys = ["contract_id", "contract_version", "record_kind", "schema", "registry", "authority",
                     "dependencies", "dependency_pins", "source_policy", "owner_policy", "transition_policy",
                     "c002_policy", "no_claim_policy", "validation"]
    if list(contract) != expected_keys or contract.get("contract_id") != "c009-ft2-post-c009-fast-track-gate-reevaluation" or contract.get("contract_version") != "1.0.0" or contract.get("record_kind") != "c009ft2-post-c009-fast-track-gate-reevaluation":
        add(issues, "CONTRACT_EXACTNESS", "contract identity/order drift")
    exact_sections = {
        "schema": EXPECTED_SCHEMA_BINDING, "registry": EXPECTED_REGISTRY_BINDING,
        "authority": EXPECTED_AUTHORITY, "dependencies": EXPECTED_DEPENDENCIES,
        "dependency_pins": EXPECTED_PINS, "source_policy": EXPECTED_SOURCE_POLICY,
        "owner_policy": EXPECTED_OWNER_POLICY, "transition_policy": EXPECTED_TRANSITION_POLICY,
        "c002_policy": EXPECTED_C002_POLICY, "no_claim_policy": EXPECTED_NO_CLAIM_POLICY,
        "validation": EXPECTED_VALIDATION,
    }
    for key, expected in exact_sections.items():
        if contract.get(key) != expected:
            add(issues, "CONTRACT_EXACTNESS", f"contract section drift: {key}")
    return sorted(set(issues), key=lambda item: (item.code, item.message))


def validate_dependencies(contract: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    for key, relative in EXPECTED_DEPENDENCIES.items():
        try:
            document = load_document(ROOT / relative, f"dependency {key}")
            if semantic_digest(document) != EXPECTED_PINS[key]:
                add(issues, "DEPENDENCY_PIN", f"semantic drift: {key}")
        except Exception as exc:
            add(issues, "DEPENDENCY_PIN", f"{key}: {exc}")
    return sorted(set(issues), key=lambda item: (item.code, item.message))


def _expected_registry_sections() -> dict[str, Any]:
    return {
        "source": EXPECTED_SOURCE,
        "owner_model": EXPECTED_OWNER,
        "predecessors": {
            "c008_ft1": {"status": "COMPLETED_ARCHIVE_ONLY", "gate_id": "FAST_TRACK_INQUIRY_LAUNCH_ELIGIBLE",
                          "gate_state": False, "met_count": 4, "unmet_count": 8, "total_prerequisites": 12,
                          "changed_prerequisite_previous_state": "NOT_AUTHORIZED", "historical_record_immutable": True},
            "c009": {"status": "COMPLETED_ARCHIVE_ONLY", "merge_commit": "432a72ee0a22069dc33cc4cbb2a5b78e63705b74",
                     "post_merge_ci_run": 32631411970, "post_merge_ci_result": "PASS", "tree_integrated": True,
                     "target_pilot_id": "pilot:f5922666261e", "canonical_combination_id": "pcomb:829e387ccdcb",
                     "canonical_leaf_id": "prd:sku:66ebd0510693"},
        },
        "c009_evidence": {
            "evidence_class": "INTEGRATED_CANONICAL_PRODUCT_PROMOTION", "evidence_refs": EXPECTED_EVIDENCE_REFS,
            "target_pilot_id": "pilot:f5922666261e", "canonical_combination_id": "pcomb:829e387ccdcb",
            "canonical_leaf_id": "prd:sku:66ebd0510693", "material": "Stainless Steel", "grade": "201",
            "finish": "Silver", "diameter": "51 mm", "thickness": "0.50 mm", "length": "6 m",
            "availability": "MISSING_DATA_VALUE", "brand": "ABSENT_NOT_PROMOTED", "color": "ABSENT_NOT_PROMOTED",
            "price": "ABSENT", "stock": "ABSENT", "eta_sla": "ABSENT", "supplier_truth": "ABSENT",
            "additional_product_combination_or_sku_created": False, "runtime_or_publication_created": False,
        },
        "transition": {
            "changed_prerequisites_count": 1, "prerequisite_id": "CANONICAL_PRODUCT_PROMOTION_COMPLETE",
            "previous": {"state": "NOT_AUTHORIZED", "met": False, "evidence_class": "FUTURE_AUTHORIZATION_REQUIRED", "owner": "PRODUCT_CORE"},
            "effective": {"state": "MET", "met": True, "evidence_class": "INTEGRATED_CANONICAL_PRODUCT_PROMOTION", "owner": "PRODUCT_CORE"},
            "evidence_refs": EXPECTED_EVIDENCE_REFS, "promotion_effect": False,
        },
        "effective_gate": {
            "gate_id": "FAST_TRACK_INQUIRY_LAUNCH_ELIGIBLE", "gate_kind": "SIBLING_GOVERNANCE_GATE",
            "eligible": False, "aggregate_rule": "ALL_12_PREREQUISITES_MET", "prerequisite_count": 12,
            "met_count": 5, "unmet_count": 7, "blockers": EXPECTED_BLOCKERS,
            "all_other_prerequisites_unchanged": True, "launch_authority_created": False,
        },
        "c002_snapshot": EXPECTED_C002,
        "no_claim_boundaries": {
            "availability": "MISSING_DATA_VALUE", "brand": "ABSENT_NOT_PROMOTED", "color": "ABSENT_NOT_PROMOTED",
            "price": "ABSENT", "stock": "ABSENT", "eta_sla": "ABSENT", "supplier_truth": "ABSENT",
            "rights_safe_media_ready": False, "inquiry_crm_flow_ready": False,
            "security_privacy_gate_ready": False, "seo_indexing_gate_ready": False,
            "mobile_performance_gate_ready": False, "staging_acceptance_pass": False,
            "production_founder_go": False,
        },
        "authority_effects": {
            "gate_reevaluation_delta_recorded": True, "exact_single_prerequisite_transition_recorded": True,
            "docs_contract_schema_registry_validator_tests": True, "branch_commit_push_one_pr": True,
            "c008_ft1_owner_mutation": False, "c009_owner_mutation": False, "authority_transfer": False,
            "second_prerequisite_transition": False, "gate_true_or_launch_authority": False,
            "c002_mutation": False, "candidate_population": False,
            "additional_product_combination_or_sku_population": False, "brand_color_or_mass_population": False,
            "availability_price_stock_eta_sla_supplier_claim": False, "media_right_or_asset_creation": False,
            "inquiry_crm_security_seo_performance_implementation": False, "wordpress_woocommerce_mutation": False,
            "runtime_mutation": False, "staging_mutation": False, "production_mutation": False,
            "deployment_or_publication": False, "m4_or_successor_mission": False,
            "auto_merge_or_merge": False, "branch_deletion": False,
        },
        "regression_anchors": {
            "c008_ft1_historical_gate_state": False, "c008_ft1_historical_met_count": 4,
            "c008_ft1_historical_unmet_count": 8, "c009_combination_count": 1, "c009_leaf_count": 1,
            "effective_gate_state": False, "effective_met_count": 5, "effective_unmet_count": 7,
            "c002_resolved_count": 6, "c002_unresolved_count": 3, "c002_readiness": "NOT_READY",
            "c002_candidate_count": 0, "commerce_state": "INQUIRY_ONLY", "runtime_state": "NONE",
            "staging_state": "NONE", "production_state": "NONE", "m4_authorized": False,
            "successor_mission_started": False,
        },
    }


def _validate_live_predecessor_semantics(issues: list[Issue]) -> None:
    try:
        ft1 = load_document(ROOT / EXPECTED_DEPENDENCIES["c008_ft1_registry"], "C008-FT1 registry")
        gate = ft1.get("gate", {})
        if gate.get("eligible") is not False or gate.get("met_count") != 4 or gate.get("unmet_count") != 8 or gate.get("prerequisite_count") != 12:
            add(issues, "C008_FT1_BASELINE", "historical gate must remain false 4/12")
        rows = gate.get("prerequisites", [])
        product = [row for row in rows if row.get("id") == "CANONICAL_PRODUCT_PROMOTION_COMPLETE"]
        if len(product) != 1 or product[0].get("state") != "NOT_AUTHORIZED" or product[0].get("met") is not False or product[0].get("owner") != "PRODUCT_CORE":
            add(issues, "C008_FT1_BASELINE", "historical Product prerequisite drift")
        if [row.get("id") for row in rows if not row.get("met")][1:] != EXPECTED_BLOCKERS:
            add(issues, "BLOCKER_TRANSFORMATION", "effective blockers must remove only Product promotion")
    except Exception as exc:
        add(issues, "C008_FT1_BASELINE", str(exc))
    try:
        c009 = load_document(ROOT / EXPECTED_DEPENDENCIES["c009_registry"], "C009 registry")
        promotion = c009.get("promotion", {})
        if promotion.get("canonical_combination", {}).get("combination_id") != "pcomb:829e387ccdcb" or promotion.get("canonical_leaf", {}).get("entity", {}).get("entity_id") != "prd:sku:66ebd0510693" or promotion.get("canonical_combination", {}).get("source_pilot_id") != "pilot:f5922666261e":
            add(issues, "C009_EVIDENCE", "exact Pilot/combination/leaf evidence drift")
        expected_boundaries = {"brand": "ABSENT_NOT_PROMOTED", "color": "ABSENT_NOT_PROMOTED", "availability": "MISSING_DATA_VALUE", "price": "ABSENT", "stock": "ABSENT", "eta_sla": "ABSENT", "supplier_truth": "ABSENT", "mass": "ABSENT", "inquiry_only": True, "approved_status_does_not_imply_import_publication_or_runtime": True}
        if c009.get("commercial_boundaries") != expected_boundaries:
            add(issues, "C009_EVIDENCE", "C009 commercial/no-claim boundaries drift")
    except Exception as exc:
        add(issues, "C009_EVIDENCE", str(exc))


def validate_registry(registry: Any, schema: dict[str, Any], *, synthetic: bool) -> list[Issue]:
    issues: list[Issue] = []
    if not isinstance(registry, dict):
        return [Issue("REGISTRY_TYPE", "registry must be an object")]
    for error in Draft202012Validator(schema).iter_errors(registry):
        add(issues, "SCHEMA_VALIDATION", error.message)
    expected_keys = ["registry_id", "registry_version", "mission_id", "fixture_mode", "authorized_starting_main",
                     "evaluation_as_of", "source", "owner_model", "predecessors", "c009_evidence", "transition",
                     "effective_gate", "c002_snapshot", "no_claim_boundaries", "authority_effects", "regression_anchors"]
    if list(registry) != expected_keys or registry.get("registry_id") != "c009ft2:post-c009-fast-track-gate-reevaluation" or registry.get("registry_version") != "1.0.0" or registry.get("mission_id") != "C009-FT2" or registry.get("authorized_starting_main") != "432a72ee0a22069dc33cc4cbb2a5b78e63705b74":
        add(issues, "REGISTRY_EXACTNESS", "registry identity/order/start drift")
    expected_mode = "SYNTHETIC" if synthetic else "CANONICAL"
    expected_time = "2026-08-23T13:25:29+03:30" if synthetic else "2026-08-23T13:20:29+03:30"
    if registry.get("fixture_mode") != expected_mode:
        add(issues, "FIXTURE_MODE", "canonical/synthetic mode mismatch")
    if registry.get("evaluation_as_of") != expected_time:
        add(issues, "CHRONOLOGY", "evaluation timestamp drift")
    for key, expected in _expected_registry_sections().items():
        if registry.get(key) != expected:
            code = {
                "source": "SOURCE_EXACTNESS", "owner_model": "OWNER_MODEL", "predecessors": "PREDECESSOR_EXACTNESS",
                "c009_evidence": "C009_EVIDENCE", "transition": "SINGLE_TRANSITION",
                "effective_gate": "GATE_AGGREGATION", "c002_snapshot": "C002_REGRESSION",
                "no_claim_boundaries": "NO_CLAIM_BOUNDARY", "authority_effects": "AUTHORITY_BOUNDARY",
                "regression_anchors": "REGRESSION_ANCHOR",
            }[key]
            add(issues, code, f"exact section drift: {key}")
    transition = registry.get("transition", {})
    gate = registry.get("effective_gate", {})
    if transition.get("changed_prerequisites_count") != 1 or transition.get("prerequisite_id") != "CANONICAL_PRODUCT_PROMOTION_COMPLETE":
        add(issues, "SINGLE_TRANSITION", "exactly one Product prerequisite transition required")
    if transition.get("effective", {}).get("met") is not True or transition.get("previous", {}).get("met") is not False:
        add(issues, "SINGLE_TRANSITION", "transition must be false/NOT_AUTHORIZED to true/MET")
    if transition.get("evidence_refs") != EXPECTED_EVIDENCE_REFS or registry.get("c009_evidence", {}).get("evidence_refs") != EXPECTED_EVIDENCE_REFS:
        add(issues, "EVIDENCE_BINDING", "exact C009 merge/CI/Pilot/combination/leaf binding required")
    if gate.get("eligible") is not False or (gate.get("met_count"), gate.get("unmet_count"), gate.get("prerequisite_count")) != (5, 7, 12) or gate.get("blockers") != EXPECTED_BLOCKERS:
        add(issues, "GATE_AGGREGATION", "effective gate must remain false 5/12 with exact blockers")
    _validate_live_predecessor_semantics(issues)
    forbidden = {"products", "product_values", "skus", "persisted_tuples", "mass_observations", "availability_records", "stock_records", "prices", "supplier_facts", "media_assets", "seo_pages", "runtime_objects", "customers", "orders", "quotes", "payments"}
    def scan(value: Any, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in forbidden:
                    add(issues, "FORBIDDEN_POPULATION", f"forbidden key {key} at {path}")
                scan(child, f"{path}/{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                scan(child, f"{path}/{index}")
    scan(registry, "#")
    return sorted(set(issues), key=lambda item: (item.code, item.message))


def validate_all(contract: Any, schema: Any, registry: Any, *, synthetic: bool, allow_unpinned: bool) -> list[Issue]:
    issues = validate_contract(contract) + audit_schema(schema)
    if isinstance(contract, dict):
        issues += validate_dependencies(contract)
    if isinstance(schema, dict):
        issues += validate_registry(registry, schema, synthetic=synthetic)
    else:
        issues.append(Issue("SCHEMA_TYPE", "schema must be an object"))
    expected = [EXPECTED_CONTRACT_DIGEST, EXPECTED_SCHEMA_DIGEST, EXPECTED_SYNTHETIC_DIGEST if synthetic else EXPECTED_REGISTRY_DIGEST]
    actual = [semantic_digest(contract), semantic_digest(schema), semantic_digest(registry)]
    if not allow_unpinned:
        for label, pin, observed in zip(("contract", "schema", "registry"), expected, actual):
            if pin in ("", "TO_BE_FINALIZED", None) or pin != observed:
                issues.append(Issue("SEMANTIC_DIGEST", f"{label} semantic digest is unpinned or drifted"))
    return sorted(set(issues), key=lambda item: (item.code, item.message))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default=str(REGISTRY_PATH))
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--allow-unpinned", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        contract = load_document(CONTRACT_PATH, "C009-FT2 contract")
        schema = load_document(SCHEMA_PATH, "C009-FT2 schema")
        registry = load_document(Path(args.registry), "C009-FT2 registry")
    except Exception as exc:
        print(f"LOAD_ERROR: {exc}")
        return 1
    original_socket = socket.socket
    socket.socket = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("network disabled"))  # type: ignore[assignment]
    try:
        issues = validate_all(contract, schema, registry, synthetic=args.synthetic, allow_unpinned=args.allow_unpinned)
    finally:
        socket.socket = original_socket
    if issues:
        for issue in issues:
            print(f"{issue.code}: {issue.message}")
        return 1
    print("C009-FT2 post-C009 Fast-Track gate re-evaluation validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
