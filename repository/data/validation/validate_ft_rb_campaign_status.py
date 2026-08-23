#!/usr/bin/env python3
"""Offline, fail-closed validation for the FT-RB campaign status router."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import socket
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "repository/data/contracts/ft-rb-campaign-status.contract.yaml"
SCHEMA = ROOT / "repository/data/schemas/ft-rb-campaign-status.schema.json"
REGISTRY = ROOT / "repository/data/registries/extensions/ftrb/campaign-status.yaml"
MAX_BYTES, MAX_DEPTH, MAX_NODES = 2 * 1024 * 1024, 100, 50_000
EXPECTED_BLOCKERS = ["RIGHTS_SAFE_MEDIA_READY", "INQUIRY_CRM_FLOW_READY", "SECURITY_PRIVACY_GATE_READY", "SEO_INDEXING_GATE_READY", "MOBILE_PERFORMANCE_GATE_READY", "STAGING_ACCEPTANCE_PASS", "PRODUCTION_FOUNDER_GO"]
EXPECTED_MISSIONS = [f"FT-RB-0{number}" for number in range(1, 9)]
EXPECTED_PINS = {
    "c006_contract": "131b2c79a3d017c65bac896e95e7a638164a77b821546e5217266f6d3829dcc0",
    "c006_schema": "9a9009c4431c097c062dcef81fad03fae51784ff466bb8cc5db6ed14237f79e3",
    "c006_registry": "5b5510af1b521daa7b2539007cab0681885f2bbc3eff4a75dde67cb38857ad8b",
    "c002_contract": "923731cb080b0ecc05abb21b1189bfdd0df94297780cce364bb791479f7f47e3",
    "c008_contract": "bf450358e11c82df7ae41a7777bd2889f2c4b7cffe64a5f2ee21f3303cbd2f5c",
    "c008_r1_contract": "da5a70f0e7330df8afab52e931f664bda453266740646a4d4183d25370ea75d7",
    "c008_ft1_contract": "4c940eed75fe433bc8adbc85cb45954068b233cc1de6d80b40bc28eb71466fb5",
    "c009_contract": "a1179a6ef97735431f89ef075e7d40c9dd6973b5eacbeca6599d9666bc7674d3",
    "c009_ft2_contract": "0200e474df33fcd8b74308c678107d53dbc9f9999b84fa753db97fc1f1ced5e8",
}
DEPENDENCIES = {
    "c006_contract": "repository/data/contracts/pipe-product-experience-architecture.contract.yaml",
    "c006_schema": "repository/data/schemas/pipe-product-experience-architecture.schema.json",
    "c006_registry": "repository/data/registries/extensions/c006/pipe-product-experience-architecture.yaml",
    "c002_contract": "repository/data/contracts/commercial-pilot-candidate.contract.yaml",
    "c008_contract": "repository/data/contracts/c008-c002-readiness-evidence-closure.contract.yaml",
    "c008_r1_contract": "repository/data/contracts/c008-r1-remaining-real-world-evidence-closure.contract.yaml",
    "c008_ft1_contract": "repository/data/contracts/c008-ft1-fast-track-inquiry-launch-gate.contract.yaml",
    "c009_contract": "repository/data/contracts/c009-first-commercial-slice-canonical-leaf-promotion.contract.yaml",
    "c009_ft2_contract": "repository/data/contracts/c009-ft2-post-c009-fast-track-gate-reevaluation.contract.yaml",
}
C009_REGISTRY = ROOT / "repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml"
EXPECTED_DIGESTS = {
    "contract": "0abac587eff448770493e9afd9dc908503f40f519525b160b8e30d1cb0f59aca",
    "schema": "9ccc2f734ca766a52a10811d1b03c2c78cf1f1c0c8db525477ec16727bf86a0d",
    "canonical": "242df96bf329950e80830a90b1e5a5cd202b89418113347fbbf705b69c8419b1",
    "synthetic": "4ace489dfb86b80f27d090842f864ef0ff8a18518abff6a9376ec1f545d112ad",
}
EXPECTED_AUTHORITY = {"mission_id":"FT-RB-00","campaign_status_router_allowed":True,"documentation_contract_schema_registry_validator_test_allowed":True,"branch_commit_push_one_pr_allowed":True,"lane_execution_claim_allowed":False,"gate_transition_allowed":False,"c002_mutation_allowed":False,"product_combination_sku_mutation_allowed":False,"price_stock_availability_eta_sla_claim_allowed":False,"media_asset_or_right_creation_allowed":False,"runtime_staging_production_mutation_allowed":False,"deployment_publication_merge_auto_merge_branch_deletion_allowed":False}
EXPECTED_SOURCE_POLICY = {"repository":"masoudtavousi-collab/damavand-steel-platform","slack_channel_id":"C0BNHRRTE9F","founder_user_id":"U0BNFS43TBL","campaign_authorization_ts":"1787485976.633809","campaign_authorization_thread_complete":True,"campaign_authorization_reply_count":0,"fast_track_parent_ts":"1787398697.475999","execution_command_sha256":"f49f01222adc1b1389e61a99f1a07db13c07d01b2d36522a2469975a2015f839","execution_command_role":"CURRENT_FOUNDER_TASK_INSTRUCTION","command_hash_bound_by_slack":False,"authorized_starting_main":"310d0ac3f6f9da67a975a32beb0b55361aa176d5","predecessor_post_merge_ci_run":32637163057,"predecessor_post_merge_ci_result":"PASS"}
EXPECTED_OWNER_POLICY = {"model":"APPEND_ONLY_CAMPAIGN_STATUS_ROUTER","historical_c008_ft1_owner_immutable":True,"c009_ft2_effective_delta_immutable":True,"campaign_router_creates_gate_authority":False,"baseline_immutable":True,"lane_local_deltas_append_only":True,"effective_resolution_requires_integrated_evidence":True,"lane_status_is_not_gate_transition":True,"readiness_classification_is_not_gate_met":True,"product_truth_owner":"PRODUCT_CORE","media_owner":"FUTURE_MEDIA_REPOSITORY","inquiry_context_owner":"INQUIRY_DATA_MODEL","seo_intent_owner":"SEO_INTENT_OWNER","woocommerce_owner":"WOOCOMMERCE_ADAPTER"}
EXPECTED_VALIDATION = {"offline_only":True,"network_allowed":False,"side_effects_allowed":False,"closed_schema_required":True,"local_refs_only":True,"duplicate_yaml_and_json_keys_rejected":True,"non_finite_numbers_rejected":True,"deterministic_sorted_errors":True,"path_escape_symlink_byte_depth_node_caps_enforced":True,"exact_order_counts_dependencies_statuses_and_no_go_required":True,"exact_allowlist_and_dag_required":True,"no_stacking_wip_and_pre_merge_stop_required":True,"predecessor_semantic_pins_required":True,"semantic_digest_pinning_required":True,"mutation_manifest_dispatch_required":True}
EXPECTED_SOURCE = {"source_id":"FTRB-SOURCE-001","source_class":"FOUNDER_CAMPAIGN_AUTHORIZATION","locator":"slack:C0BNHRRTE9F:1787485976.633809","channel_id":"C0BNHRRTE9F","message_ts":"1787485976.633809","author_id":"U0BNFS43TBL","thread_complete":True,"reply_count":0,"fast_track_parent_ts":"1787398697.475999","execution_command_sha256":"f49f01222adc1b1389e61a99f1a07db13c07d01b2d36522a2469975a2015f839","command_hash_bound_by_slack":False}
EXPECTED_PREDECESSORS = {"c002_readiness":"6/9 / NOT_READY", "founder_selection_ready":False, "c002_candidate_count":0, "supply_evidence":"SUBMITTED_REVIEW_INCOMPLETE", "photo_content_readiness":"MISSING_EVIDENCE", "fulfillment_risk":"SUBMITTED_REVIEW_INCOMPLETE", "c008_ft1_historical_gate":"FALSE / 4/12", "c009_status":"COMPLETED_ARCHIVE_ONLY", "c009_merge_commit":"432a72ee0a22069dc33cc4cbb2a5b78e63705b74", "c009_ft2_status":"COMPLETED_ARCHIVE_ONLY", "c009_ft2_merge_commit":"310d0ac3f6f9da67a975a32beb0b55361aa176d5", "c009_ft2_post_merge_ci_run":32637163057, "c009_ft2_post_merge_ci_result":"PASS"}
EXPECTED_NO_GO = {"commerce_state":"INQUIRY_ONLY","availability":"MISSING_DATA_VALUE","brand":"ABSENT_NOT_PROMOTED","color":"ABSENT_NOT_PROMOTED","price":"ABSENT","stock":"ABSENT","eta_sla":"ABSENT","supplier_truth":"ABSENT","product_scope_changed":False,"runtime_mutation":False,"staging_mutation":False,"production_mutation":False,"publication_mutation":False,"merge_performed":False,"successor_mission_started":False}
EXPECTED_CONTROLS = {"baseline_immutable":True,"lane_local_deltas_append_only":True,"effective_resolution_requires_integrated_evidence":True,"one_writer_worktree_branch_per_mission":True,"no_cross_mission_unreviewed_stacking":True,"resolve_live_main_before_each_mission":True,"maximum_active_wip":3,"wip_shape":"1_COMMERCIAL_PLUS_1_CORE_PLUS_1_ENABLER","one_non_draft_pr_per_mission":True,"changed_head_invalidates_review_and_ci":True,"pre_merge_stop_required":True}
EXPECTED_ALLOWLIST = ["docs/08_DOCUMENTATION_INDEX.md","docs/14_CHANGELOG.md","docs/18_OPEN_QUESTIONS.md","docs/CURRENT_PROJECT_STATE.md","docs/FT_RB_00_FAST_TRACK_REMAINING_BLOCKERS_CAMPAIGN_STATUS_V1.0.md","docs/PROJECT_EXECUTION_ROADMAP.md","docs/TRACEABILITY_MATRIX.md","repository/data/contracts/ft-rb-campaign-status.contract.yaml","repository/data/registries/extensions/ftrb/campaign-status.yaml","repository/data/schemas/ft-rb-campaign-status.schema.json","repository/data/validation/validate_ft_rb_campaign_status.py","scripts/test.sh","tests/fixtures/ft-rb-campaign-status/README.md","tests/fixtures/ft-rb-campaign-status/adversarial-duplicate-keys.json","tests/fixtures/ft-rb-campaign-status/adversarial-duplicate-keys.yaml","tests/fixtures/ft-rb-campaign-status/adversarial-permissive-schema.json","tests/fixtures/ft-rb-campaign-status/adversarial-remote-ref-schema.json","tests/fixtures/ft-rb-campaign-status/mutation-cases.json","tests/fixtures/ft-rb-campaign-status/valid-synthetic.yaml","tests/test_ft_rb_campaign_status.py"]
EXPECTED_LANES = [
    ("FT-RB-01","RIGHTS_SAFE_MEDIA_READY","FUTURE_MEDIA_REPOSITORY",["C009_FT2_INTEGRATED"],"BLOCKED_EXTERNAL_EVIDENCE","No rights-safe asset admitted; intake and publication checklist required.","UNMET","Create bounded media intake/readiness package."),
    ("FT-RB-02","INQUIRY_CRM_FLOW_READY","INQUIRY_DATA_MODEL",["C009_FT2_INTEGRATED"],"NOT_REVIEWED","Repository package may define no-price inquiry handoff only.","UNMET","Create bounded inquiry/CRM repository package."),
    ("FT-RB-03","SECURITY_PRIVACY_GATE_READY","SECURITY_PRIVACY",["C009_FT2_INTEGRATED"],"NOT_REVIEWED","Repository hardening package is not environment security PASS.","UNMET","Create bounded security/privacy repository package."),
    ("FT-RB-04","SEO_INDEXING_GATE_READY","SEO_INTENT_OWNER",["C009_FT2_INTEGRATED"],"NOT_REVIEWED","Repository package cannot claim indexing or publish Product facts.","UNMET","Create bounded SEO/indexing repository package."),
    ("FT-RB-05","MOBILE_PERFORMANCE_GATE_READY","PRODUCT_EXPERIENCE_ENGINE",["C009_FT2_INTEGRATED"],"NOT_REVIEWED","Static controls are not Iran-network or Staging measurement evidence.","UNMET","Create bounded mobile/performance configuration package."),
    ("FT-RB-06","WORDPRESS_WOOCOMMERCE_PROJECTION_ENABLER","WOOCOMMERCE_ADAPTER",["FT_RB_01_TO_05_INTEGRATED"],"NOT_REVIEWED","Projection is downstream only and needs no runtime mutation.","NOT_A_GATE_PREREQUISITE","Wait for required integrated repository packages."),
    ("FT-RB-07","INTEGRATED_RELEASE_CANDIDATE","RELEASE_GOVERNANCE",["FT_RB_02_TO_06_INTEGRATED"],"NOT_REVIEWED","Release candidate is not Staging acceptance or Production authorization.","NOT_A_GATE_PREREQUISITE","Wait for required integrated repository packages."),
    ("FT-RB-08","STAGING_ACCEPTANCE_PASS","RELEASE_GOVERNANCE",["FT_RB_07_INTEGRATED"],"NOT_REVIEWED","First Staging mutation requires separate Founder authorization.","UNMET","Prepare only; stop at STAGING_MUTATION_FOUNDER_GATE_REQUIRED."),
]
EXPECTED_BLOCKER_STATUSES = [
    {"blocker":"RIGHTS_SAFE_MEDIA_READY","owner":"FUTURE_MEDIA_REPOSITORY","dependencies":["C009_FT2_INTEGRATED"],"workflow_status":"NOT_STARTED","readiness_classification":"BLOCKED_EXTERNAL_EVIDENCE","evidence":"No rights-safe asset admitted.","gate_state":"UNMET","next_action":"Await rights-safe media evidence."},
    {"blocker":"INQUIRY_CRM_FLOW_READY","owner":"INQUIRY_DATA_MODEL","dependencies":["C009_FT2_INTEGRATED"],"workflow_status":"NOT_STARTED","readiness_classification":"NOT_REVIEWED","evidence":"No repository package reviewed.","gate_state":"UNMET","next_action":"Create bounded inquiry/CRM package."},
    {"blocker":"SECURITY_PRIVACY_GATE_READY","owner":"SECURITY_PRIVACY","dependencies":["C009_FT2_INTEGRATED"],"workflow_status":"NOT_STARTED","readiness_classification":"NOT_REVIEWED","evidence":"No repository package reviewed.","gate_state":"UNMET","next_action":"Create bounded security/privacy package."},
    {"blocker":"SEO_INDEXING_GATE_READY","owner":"SEO_INTENT_OWNER","dependencies":["C009_FT2_INTEGRATED"],"workflow_status":"NOT_STARTED","readiness_classification":"NOT_REVIEWED","evidence":"No repository package reviewed.","gate_state":"UNMET","next_action":"Create bounded SEO/indexing package."},
    {"blocker":"MOBILE_PERFORMANCE_GATE_READY","owner":"PRODUCT_EXPERIENCE_ENGINE","dependencies":["C009_FT2_INTEGRATED"],"workflow_status":"NOT_STARTED","readiness_classification":"NOT_REVIEWED","evidence":"No configuration package reviewed.","gate_state":"UNMET","next_action":"Create bounded mobile/performance package."},
    {"blocker":"STAGING_ACCEPTANCE_PASS","owner":"RELEASE_GOVERNANCE","dependencies":["FT_RB_07_INTEGRATED"],"workflow_status":"NOT_STARTED","readiness_classification":"NOT_REVIEWED","evidence":"No Staging run exists.","gate_state":"UNMET","next_action":"Prepare only; wait for Staging Founder gate."},
    {"blocker":"PRODUCTION_FOUNDER_GO","owner":"FOUNDER_PROJECT_COMMANDER","dependencies":["STAGING_ACCEPTANCE_PASS"],"workflow_status":"NOT_STARTED","readiness_classification":"NOT_GRANTED","evidence":"No Founder Production GO exists.","gate_state":"UNMET","next_action":"Wait for explicit Founder GO."},
]

class StrictLoader(yaml.SafeLoader):
    pass

def mapping(loader: StrictLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result
StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)

def json_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out

def load(path: Path) -> Any:
    if path.is_symlink() or any(parent.is_symlink() for parent in [path, *path.parents] if parent.exists()):
        raise ValueError("symlink paths are forbidden")
    resolved = path.resolve(strict=True)
    resolved.relative_to(ROOT.resolve())
    if not resolved.is_file() or resolved.stat().st_size > MAX_BYTES:
        raise ValueError("regular-file/byte-cap violation")
    raw = resolved.read_text(encoding="utf-8")
    value = json.loads(raw, object_pairs_hook=json_pairs, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"nonfinite JSON: {value}"))) if resolved.suffix == ".json" else yaml.load(raw, Loader=StrictLoader)
    bounded(value)
    return value

def bounded(value: Any, depth: int = 0) -> int:
    if depth > MAX_DEPTH:
        raise ValueError("depth cap exceeded")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("nonfinite value")
    if isinstance(value, dict):
        count = 1 + sum(bounded(key, depth + 1) + bounded(child, depth + 1) for key, child in value.items())
    elif isinstance(value, list):
        count = 1 + sum(bounded(child, depth + 1) for child in value)
    else:
        count = 1
    if count > MAX_NODES:
        raise ValueError("node cap exceeded")
    return count

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()

def schema_issues(schema: Any) -> list[str]:
    issues: list[str] = []
    forbidden = {"allOf", "anyOf", "oneOf", "not", "if", "then", "else", "dependentSchemas", "contains", "patternProperties", "propertyNames", "unevaluatedProperties", "unevaluatedItems", "dependentRequired", "contentSchema"}
    def visit(node: Any, path: str) -> None:
        if node is True or node == {}:
            issues.append(f"PERMISSIVE_SCHEMA:{path}"); return
        if node is False:
            return
        if not isinstance(node, dict):
            issues.append(f"SCHEMA_NODE_TYPE:{path}"); return
        if forbidden.intersection(node): issues.append(f"PERMISSIVE_APPLICATOR:{path}")
        ref = node.get("$ref")
        if isinstance(ref, str) and not ref.startswith("#/"): issues.append(f"REMOTE_SCHEMA_REF:{path}")
        if isinstance(ref, str) and set(node) != {"$ref"}: issues.append(f"REF_SIBLING:{path}")
        node_type = node.get("type")
        if isinstance(node_type, list): issues.append(f"TYPE_UNION:{path}")
        if not isinstance(ref, str) and not any(key in node for key in ("type", "const", "enum")): issues.append(f"NON_ASSERTIVE_SCHEMA:{path}")
        object_keywords = {"properties", "required", "additionalProperties", "patternProperties", "propertyNames", "minProperties", "maxProperties"}
        array_keywords = {"items", "prefixItems", "minItems", "maxItems", "uniqueItems", "contains"}
        if object_keywords.intersection(node) and node_type != "object": issues.append(f"WRONG_INSTANCE_OBJECT_KEYWORD:{path}")
        if array_keywords.intersection(node) and node_type != "array": issues.append(f"WRONG_INSTANCE_ARRAY_KEYWORD:{path}")
        if node_type == "object" and node.get("additionalProperties") is not False: issues.append(f"OPEN_SCHEMA:{path}")
        if node_type == "array" and "items" not in node: issues.append(f"ARRAY_ITEMS_REQUIRED:{path}")
        if node_type == "array" and node.get("items") is True: issues.append(f"PERMISSIVE_SCHEMA:{path}/items")
        if "prefixItems" in node: issues.append(f"PREFIX_ITEMS_FORBIDDEN:{path}")
        for key in ("properties", "$defs"):
            container = node.get(key)
            if isinstance(container, dict):
                for name, child in container.items(): visit(child, f"{path}/{key}/{name}")
            elif key in node: issues.append(f"SCHEMA_CONTAINER_TYPE:{path}/{key}")
        for key in ("items", "additionalProperties"):
            if isinstance(node.get(key), (dict, bool)): visit(node[key], f"{path}/{key}")
        if "prefixItems" in node and not isinstance(node.get("prefixItems"), list): issues.append(f"SCHEMA_CONTAINER_TYPE:{path}/prefixItems")
    visit(schema, "#")
    if issues:
        return sorted(set(issues))
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        return [f"SCHEMA_META:{exc}"]
    return issues

def validate(contract: Any, schema: Any, registry: Any, *, synthetic: bool, allow_unpinned: bool) -> list[str]:
    issues = schema_issues(schema)
    if not isinstance(contract, dict) or list(contract) != ["contract_id", "contract_version", "record_kind", "schema", "registry", "authority", "dependencies", "dependency_pins", "source_policy", "owner_policy", "validation"]:
        issues.append("CONTRACT_EXACTNESS")
    elif (contract.get("contract_id") != "ft-rb-campaign-status" or contract.get("contract_version") != "1.0.0" or contract.get("record_kind") != "fast-track-remaining-blockers-campaign-status" or contract.get("schema") != {"path":"repository/data/schemas/ft-rb-campaign-status.schema.json","draft":"https://json-schema.org/draft/2020-12/schema"} or contract.get("registry") != {"path":"repository/data/registries/extensions/ftrb/campaign-status.yaml"} or contract.get("authority") != EXPECTED_AUTHORITY or contract.get("dependencies") != DEPENDENCIES or contract.get("dependency_pins") != EXPECTED_PINS or contract.get("source_policy") != EXPECTED_SOURCE_POLICY or contract.get("owner_policy") != EXPECTED_OWNER_POLICY or contract.get("validation") != EXPECTED_VALIDATION):
        issues.append("CONTRACT_EXACTNESS")
    if not isinstance(registry, dict): return sorted(set(issues + ["REGISTRY_TYPE"]))
    expected_keys = ["registry_id", "registry_version", "mission_id", "fixture_mode", "fixture_identity", "authorized_starting_main", "status_as_of", "source", "predecessors", "effective_gate", "campaign_controls", "no_claim_boundaries", "allowlist", "blocker_statuses", "lanes"]
    if list(registry) != expected_keys or registry.get("registry_id") != "ftrb:campaign-status" or registry.get("mission_id") != "FT-RB-00" or registry.get("authorized_starting_main") != "310d0ac3f6f9da67a975a32beb0b55361aa176d5": issues.append("REGISTRY_EXACTNESS")
    if registry.get("fixture_mode") != ("SYNTHETIC" if synthetic else "CANONICAL") or registry.get("fixture_identity") != ("SYNTHETIC_FTRB_CAMPAIGN_STATUS" if synthetic else "CANONICAL_FTRB_CAMPAIGN_STATUS") or registry.get("status_as_of") != ("2026-08-23T16:00:01+03:30" if synthetic else "2026-08-23T16:00:00+03:30"): issues.append("CHRONOLOGY_OR_MODE")
    if not issues:
        for error in Draft202012Validator(schema).iter_errors(registry): issues.append(f"SCHEMA_VALIDATION:{error.message}")
    source = registry.get("source") if isinstance(registry.get("source"), dict) else {}
    if source != EXPECTED_SOURCE: issues.append("SOURCE_EXACTNESS")
    pre = registry.get("predecessors") if isinstance(registry.get("predecessors"), dict) else {}
    if pre != EXPECTED_PREDECESSORS: issues.append("PREDECESSOR_REGRESSION")
    gate = registry.get("effective_gate") if isinstance(registry.get("effective_gate"), dict) else {}
    if gate.get("eligible") is not False or (gate.get("met_count"), gate.get("unmet_count"), gate.get("total_prerequisites")) != (5,7,12) or gate.get("blockers") != EXPECTED_BLOCKERS or gate.get("transition_recorded") is not False: issues.append("GATE_AGGREGATION")
    if registry.get("campaign_controls") != EXPECTED_CONTROLS: issues.append("CAMPAIGN_CONTROLS")
    allowlist = registry.get("allowlist") if isinstance(registry.get("allowlist"), list) else []
    if allowlist != EXPECTED_ALLOWLIST or allowlist != sorted(allowlist): issues.append("ALLOWLIST")
    no_go = registry.get("no_claim_boundaries") if isinstance(registry.get("no_claim_boundaries"), dict) else {}
    if no_go != EXPECTED_NO_GO: issues.append("NO_GO_BOUNDARY")
    blockers = registry.get("blocker_statuses") if isinstance(registry.get("blocker_statuses"), list) else []
    if blockers != EXPECTED_BLOCKER_STATUSES: issues.append("BLOCKER_STATUS_EXACTNESS")
    lanes = registry.get("lanes") if isinstance(registry.get("lanes"), list) else []
    if [lane.get("mission") for lane in lanes if isinstance(lane, dict)] != EXPECTED_MISSIONS: issues.append("LANE_ORDER")
    expected_rows = [{"mission": mission, "blocker": blocker, "owner": owner, "dependencies": dependencies, "workflow_status":"NOT_STARTED", "readiness_classification": readiness, "pr":None, "head_sha":None, "ci":None, "merged":False, "evidence":evidence, "gate_state":gate_state, "next_action":next_action} for mission, blocker, owner, dependencies, readiness, evidence, gate_state, next_action in EXPECTED_LANES]
    if lanes != expected_rows: issues.append("LANE_EXACTNESS")
    try:
        c009 = load(C009_REGISTRY)
        promotion = c009.get("promotion") if isinstance(c009, dict) else None
        canonical_leaf = promotion.get("canonical_leaf") if isinstance(promotion, dict) else None
        if not isinstance(canonical_leaf, dict) or canonical_leaf.get("source_pilot_id") != "pilot:f5922666261e" or canonical_leaf.get("canonical_combination_id") != "pcomb:829e387ccdcb" or canonical_leaf.get("entity", {}).get("entity_id") != "prd:sku:66ebd0510693":
            issues.append("C009_OWNER_SEMANTICS")
    except Exception as exc:
        issues.append(f"C009_OWNER_SEMANTICS:{exc}")
    for key, path in DEPENDENCIES.items():
        try:
            observed = digest(load(ROOT / path))
            expected = EXPECTED_PINS[key]
            if observed != expected: issues.append(f"DEPENDENCY_PIN:{key}")
        except Exception as exc: issues.append(f"DEPENDENCY_PIN:{key}:{exc}")
    values = {"contract": digest(contract), "schema": digest(schema), "synthetic" if synthetic else "canonical": digest(registry)}
    for key, observed in values.items():
        expected = EXPECTED_DIGESTS[key]
        if (expected == "TO_BE_FINALIZED" and not allow_unpinned) or (expected != "TO_BE_FINALIZED" and expected != observed): issues.append(f"SEMANTIC_DIGEST:{key}")
    return sorted(set(issues))

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default=str(REGISTRY)); parser.add_argument("--synthetic", action="store_true"); parser.add_argument("--allow-unpinned", action="store_true")
    args = parser.parse_args(argv)
    try: contract, schema, registry = load(CONTRACT), load(SCHEMA), load(Path(args.registry))
    except Exception as exc: print(f"LOAD_ERROR:{exc}"); return 1
    old = socket.socket; socket.socket = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("network disabled"))
    try: issues = validate(contract, schema, registry, synthetic=args.synthetic, allow_unpinned=args.allow_unpinned)
    finally: socket.socket = old
    if issues:
        print("\n".join(issues)); return 1
    print("FT-RB campaign status validation PASS"); return 0
if __name__ == "__main__": raise SystemExit(main())
