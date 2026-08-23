#!/usr/bin/env python3
"""Offline, fail-closed validation for FT-RB-01 media readiness."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import socket
import subprocess
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "repository/data/contracts/ft-rb-01-rights-safe-media-readiness.contract.yaml"
SCHEMA = ROOT / "repository/data/schemas/ft-rb-01-rights-safe-media-readiness.schema.json"
REGISTRY = ROOT / "repository/data/registries/extensions/ftrb01/rights-safe-media-readiness.yaml"
SYNTHETIC = ROOT / "tests/fixtures/ft-rb-01-rights-safe-media-readiness/valid-synthetic.yaml"
C009 = ROOT / "repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml"
MAX_BYTES, MAX_DEPTH, MAX_NODES = 2 * 1024 * 1024, 100, 50_000

ALLOWLIST = [
    "docs/FT_RB_01_RIGHTS_SAFE_MEDIA_READINESS_SCOPE_V1.0.md",
    "repository/data/contracts/ft-rb-01-rights-safe-media-readiness.contract.yaml",
    "repository/data/registries/extensions/ftrb01/rights-safe-media-readiness.yaml",
    "repository/data/schemas/ft-rb-01-rights-safe-media-readiness.schema.json",
    "repository/data/validation/validate_ft_rb_01_rights_safe_media_readiness.py",
    "scripts/test.sh",
    "tests/fixtures/ft-rb-01-rights-safe-media-readiness/README.md",
    "tests/fixtures/ft-rb-01-rights-safe-media-readiness/adversarial-duplicate-keys.json",
    "tests/fixtures/ft-rb-01-rights-safe-media-readiness/adversarial-duplicate-keys.yaml",
    "tests/fixtures/ft-rb-01-rights-safe-media-readiness/adversarial-permissive-schema.json",
    "tests/fixtures/ft-rb-01-rights-safe-media-readiness/adversarial-remote-ref-schema.json",
    "tests/fixtures/ft-rb-01-rights-safe-media-readiness/mutation-cases.json",
    "tests/fixtures/ft-rb-01-rights-safe-media-readiness/valid-synthetic.yaml",
    "tests/test_ft_rb_01_rights_safe_media_readiness.py",
]
DEPENDENCIES = {
    "c002_contract": "repository/data/contracts/commercial-pilot-candidate.contract.yaml",
    "c002_schema": "repository/data/schemas/commercial-pilot-candidate.schema.json",
    "c002_registry": "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml",
    "c006_contract": "repository/data/contracts/pipe-product-experience-architecture.contract.yaml",
    "c006_schema": "repository/data/schemas/pipe-product-experience-architecture.schema.json",
    "c006_registry": "repository/data/registries/extensions/c006/pipe-product-experience-architecture.yaml",
    "c008_contract": "repository/data/contracts/c008-c002-readiness-evidence-closure.contract.yaml",
    "c008_schema": "repository/data/schemas/c008-c002-readiness-evidence-closure.schema.json",
    "c008_registry": "repository/data/registries/extensions/c008/201-51-readiness-evidence-closure.yaml",
    "c008_r1_contract": "repository/data/contracts/c008-r1-remaining-real-world-evidence-closure.contract.yaml",
    "c008_r1_schema": "repository/data/schemas/c008-r1-remaining-real-world-evidence-closure.schema.json",
    "c008_r1_registry": "repository/data/registries/extensions/c008r1/201-51-remaining-real-world-evidence-closure.yaml",
    "c008_ft1_contract": "repository/data/contracts/c008-ft1-fast-track-inquiry-launch-gate.contract.yaml",
    "c008_ft1_schema": "repository/data/schemas/c008-ft1-fast-track-inquiry-launch-gate.schema.json",
    "c008_ft1_registry": "repository/data/registries/extensions/c008ft1/fast-track-inquiry-launch-gate.yaml",
    "c009_contract": "repository/data/contracts/c009-first-commercial-slice-canonical-leaf-promotion.contract.yaml",
    "c009_schema": "repository/data/schemas/c009-first-commercial-slice-canonical-leaf-promotion.schema.json",
    "c009_registry": "repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml",
    "c009_ft2_contract": "repository/data/contracts/c009-ft2-post-c009-fast-track-gate-reevaluation.contract.yaml",
    "c009_ft2_schema": "repository/data/schemas/c009-ft2-post-c009-fast-track-gate-reevaluation.schema.json",
    "c009_ft2_registry": "repository/data/registries/extensions/c009ft2/post-c009-fast-track-gate-reevaluation.yaml",
    "ft_rb_00_contract": "repository/data/contracts/ft-rb-campaign-status.contract.yaml",
    "ft_rb_00_schema": "repository/data/schemas/ft-rb-campaign-status.schema.json",
    "ft_rb_00_registry": "repository/data/registries/extensions/ftrb/campaign-status.yaml",
}
PINS = {
    "c002_contract":"923731cb080b0ecc05abb21b1189bfdd0df94297780cce364bb791479f7f47e3",
    "c002_schema":"1e1b1977f369ab7e5961d4e69111682d1117bc6eeedf666a9e568f0115952741",
    "c002_registry":"deb0215d2b5f4b5ec0061f937aec9c3e37cf97c94432a23737bf5756cef9587e",
    "c006_contract":"131b2c79a3d017c65bac896e95e7a638164a77b821546e5217266f6d3829dcc0",
    "c006_schema":"9a9009c4431c097c062dcef81fad03fae51784ff466bb8cc5db6ed14237f79e3",
    "c006_registry":"5b5510af1b521daa7b2539007cab0681885f2bbc3eff4a75dde67cb38857ad8b",
    "c008_contract":"bf450358e11c82df7ae41a7777bd2889f2c4b7cffe64a5f2ee21f3303cbd2f5c",
    "c008_schema":"82f8dbfb93233b6d40603a56bdb7661ee4d477003ba13b97c59d80bb0c8a27af",
    "c008_registry":"bd06e76da52750b9b54c09ccba88421ae82778dce84a4afa15475a88297081d9",
    "c008_r1_contract":"da5a70f0e7330df8afab52e931f664bda453266740646a4d4183d25370ea75d7",
    "c008_r1_schema":"fea342c3210dca9e5c2e98030bf8b5e64464cdd550cbb3b5675109c49673b904",
    "c008_r1_registry":"9dcf2cc7cc10ab01a9b97ab40ac896debd12e6f25ad5b7e700921a6c782fb87b",
    "c008_ft1_contract":"4c940eed75fe433bc8adbc85cb45954068b233cc1de6d80b40bc28eb71466fb5",
    "c008_ft1_schema":"8eb3c93a37932e6676e8a3d1c22e0c35d3f6a4d0f47f7467ea718f466ceabd80",
    "c008_ft1_registry":"799dad2f7fdf9f6ffb5a9fe37c707f222f6f92f1cc6b1e251bd3f366dd2e9cf3",
    "c009_contract":"a1179a6ef97735431f89ef075e7d40c9dd6973b5eacbeca6599d9666bc7674d3",
    "c009_schema":"aea8a6dd7b521a83576bbd00ce686d3bc2477552bc4a2f3642a80b648b6e31e2",
    "c009_registry":"1b50d28ddded3a818afb82d19759713bd6c2f2b058b4020510d8b5f74a7f6a3f",
    "c009_ft2_contract":"0200e474df33fcd8b74308c678107d53dbc9f9999b84fa753db97fc1f1ced5e8",
    "c009_ft2_schema":"558153f5f3bba6206215be46454f6add6c8fdabc414b0105c141327a12903e82",
    "c009_ft2_registry":"51d9298e2e63b44986a921d72eabc069db5b46dfda0c614ee70d4d7e2e434d08",
    "ft_rb_00_contract":"0abac587eff448770493e9afd9dc908503f40f519525b160b8e30d1cb0f59aca",
    "ft_rb_00_schema":"9ccc2f734ca766a52a10811d1b03c2c78cf1f1c0c8db525477ec16727bf86a0d",
    "ft_rb_00_registry":"242df96bf329950e80830a90b1e5a5cd202b89418113347fbbf705b69c8419b1",
}
DIGESTS = {
    "contract":"b615c55751a3d5efd6d7f395f849ac5e7e992e890f13130a348f783491d0468f",
    "schema":"676f1f0180ee2a47d69dc68f2f170a5008ec00126b3540be9a771674f16dec84",
    "canonical":"c89067202e5d2f93953e05bf74b5d47cab5f6db7aa8944afcf2715b047828547",
    "synthetic":"d6da3e1a659cc1055226ce8175f64baddc4ae483f569533fec42491bb5300652",
}

EXPECTED_AUTHORITY = {"mission_id":"FT-RB-01","repository_archaeology_intake_checklist_validator_test_allowed":True,"asset_or_right_creation_allowed":False,"media_publication_allowed":False,"product_combination_sku_mutation_allowed":False,"price_stock_availability_eta_sla_claim_allowed":False,"runtime_staging_production_mutation_allowed":False,"merge_or_successor_mission_allowed":False}
EXPECTED_SOURCE_POLICY = {"slack_channel_id":"C0BNHRRTE9F","founder_user_id":"U0BNFS43TBL","campaign_authorization_ts":"1787485976.633809","campaign_authorization_thread_complete":True,"campaign_authorization_reply_count":0,"fast_track_parent_ts":"1787398697.475999","execution_command_sha256":"f49f01222adc1b1389e61a99f1a07db13c07d01b2d36522a2469975a2015f839","command_hash_bound_by_slack":False,"campaign_authorized_starting_main":"310d0ac3f6f9da67a975a32beb0b55361aa176d5","mission_base_main":"a6fa08ba8bda06fba4e92aa58945fd01c7497dcf","router_merge_authorization_ts":"1787491529.752109","router_post_main_ci_run":32642489715,"router_post_main_ci_result":"PASS","contextual_founder_media_direction_ts":"1787400933.711809"}
EXPECTED_OWNER_POLICY = {"media_owner":"FUTURE_MEDIA_REPOSITORY","product_truth_owner":"PRODUCT_CORE","protected_predecessor_owners_immutable":True,"c009_identity_validated_from_owner_not_persisted_here":True,"append_only_lane_evidence_package":True}
EXPECTED_VALIDATION = {"exact_changed_path_count":14,"exact_changed_paths":ALLOWLIST,"offline_only":True,"side_effects_allowed":False,"closed_schema_required":True,"local_refs_only":True,"duplicate_keys_rejected":True,"non_finite_numbers_rejected":True,"path_caps_enforced":True,"deterministic_sorted_errors":True,"dependency_pins_required":True,"semantic_digest_pinning_required":True}
EXPECTED_SOURCE = {"source_id":"FTRB01-SOURCE-001","locator":"slack:C0BNHRRTE9F:1787485976.633809","author_id":"U0BNFS43TBL","thread_complete":True,"reply_count":0,"parent_ts":"1787398697.475999","command_sha256":"f49f01222adc1b1389e61a99f1a07db13c07d01b2d36522a2469975a2015f839","command_hash_bound_by_slack":False}
EXPECTED_PREDECESSORS = {"c002_readiness":"6/9 / NOT_READY","founder_selection_ready":False,"candidate_count":0,"supply_evidence":"SUBMITTED_REVIEW_INCOMPLETE","photo_content_readiness":"MISSING_EVIDENCE","fulfillment_risk":"SUBMITTED_REVIEW_INCOMPLETE","ft_rb_00_router":"INTEGRATED_ARCHIVE_ONLY","c009_owner_reference":"repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml"}
TREE_MANIFEST = [
    {"path":"assets","git_tree_oid":"e6b345856a8c7df305ebfcb96efd7319ec7862e6","tracked_file_count":6,"media_asset_count":0,"state":"PLACEHOLDER_ONLY"},
    {"path":"assets/images","git_tree_oid":"f4497262ed0c58bc08a892aeaf67df6803afd737","tracked_file_count":2,"media_asset_count":0,"state":"PLACEHOLDER_ONLY"},
    {"path":"assets/images/source","git_tree_oid":"e4b69924ca8a57ac596c60062b2cfed530b15167","tracked_file_count":1,"media_asset_count":0,"state":"PLACEHOLDER_ONLY"},
    {"path":"assets/images/optimized","git_tree_oid":"5bfad2b3f8e483b6b173d8aaff19597e84626f15","tracked_file_count":1,"media_asset_count":0,"state":"PLACEHOLDER_ONLY"},
    {"path":"repository/assets","git_tree_oid":"5bfad2b3f8e483b6b173d8aaff19597e84626f15","tracked_file_count":1,"media_asset_count":0,"state":"PLACEHOLDER_ONLY"},
    {"path":"public/wp-content/uploads","git_tree_oid":"5bfad2b3f8e483b6b173d8aaff19597e84626f15","tracked_file_count":1,"media_asset_count":0,"state":"PLACEHOLDER_ONLY"},
    {"path":"repository/content","git_tree_oid":None,"tracked_file_count":0,"media_asset_count":0,"state":"ABSENT"},
    {"path":"repository/knowledge","git_tree_oid":None,"tracked_file_count":0,"media_asset_count":0,"state":"ABSENT"},
    {"path":"repository/implementation-assets","git_tree_oid":None,"tracked_file_count":0,"media_asset_count":0,"state":"ABSENT"},
]
FILE_MANIFEST = [
    {"path":"assets/README.md","git_blob_oid":"0368fdb1bf625f75aca249ec629688ac2b94044b","classification":"PLACEHOLDER_NOT_ASSET"},
    {"path":"assets/brand/README.md","git_blob_oid":"0ccf467022fb6fdc2edb2b8d409104cbc0ddbe2d","classification":"PLACEHOLDER_NOT_ASSET"},
    {"path":"assets/documents/README.md","git_blob_oid":"ab0e95dd59cacda676acf94ad08e01ef2ef7f5b7","classification":"PLACEHOLDER_NOT_ASSET"},
    {"path":"assets/fonts/README.md","git_blob_oid":"6cb28293ccd62a14dd3d828e16060fab0ca33096","classification":"PLACEHOLDER_NOT_ASSET"},
    {"path":"assets/images/optimized/.gitkeep","git_blob_oid":"8b137891791fe96927ad78e64b0aad7bded08bdc","classification":"PLACEHOLDER_NOT_ASSET"},
    {"path":"assets/images/source/README.md","git_blob_oid":"abbe7f9585ffdf8c73408bfb49a6daa8f01ac66b","classification":"PLACEHOLDER_NOT_ASSET"},
    {"path":"public/wp-content/uploads/.gitkeep","git_blob_oid":"8b137891791fe96927ad78e64b0aad7bded08bdc","classification":"PLACEHOLDER_NOT_ASSET"},
    {"path":"repository/assets/.gitkeep","git_blob_oid":"8b137891791fe96927ad78e64b0aad7bded08bdc","classification":"PLACEHOLDER_NOT_ASSET"},
]
EXPECTED_ARCHAEOLOGY = {"scope":["assets/**","repository/assets/**","public/wp-content/uploads/**","repository/content","repository/knowledge","repository/implementation-assets"],"asset_record_count":0,"rights_evidence_count":0,"publication_eligible_count":0,"result":"NO_ADMISSIBLE_RIGHTS_SAFE_ASSET","tree_manifest":TREE_MANIFEST,"file_manifest":FILE_MANIFEST}
EXPECTED_DIMENSIONS = [
    {"dimension":"asset_exists","current_state":"MISSING","evidence_refs":[],"eligible":False},
    {"dimension":"technical_quality","current_state":"NOT_REVIEWED","evidence_refs":[],"eligible":False},
    {"dimension":"ownership_source","current_state":"MISSING","evidence_refs":[],"eligible":False},
    {"dimension":"usage_right","current_state":"MISSING","evidence_refs":[],"eligible":False},
    {"dimension":"modification_right","current_state":"MISSING","evidence_refs":[],"eligible":False},
    {"dimension":"publication_right","current_state":"MISSING","evidence_refs":[],"eligible":False},
    {"dimension":"product_binding","current_state":"MISSING","evidence_refs":[],"eligible":False},
    {"dimension":"image_to_product_truth","current_state":"NOT_REVIEWED","evidence_refs":[],"eligible":False},
    {"dimension":"rights_evidence","current_state":"MISSING","evidence_refs":[],"eligible":False},
    {"dimension":"review_status","current_state":"NOT_REVIEWED","evidence_refs":[],"eligible":False},
    {"dimension":"publication_eligibility","current_state":"FALSE","evidence_refs":[],"eligible":False},
]
REQUIRED_FIELDS = ["asset_external_reference","asset_type_and_role","master_file_locator_and_sha256","mime_type_and_byte_size","dimensions_orientation_color_profile","creator_and_asset_owner","rights_holder","rights_basis_license_or_permission","rights_evidence_durable_locator","commercial_website_use_allowed","usage_modification_publication_rights","territory_channel_use_constraints","valid_from_and_expiry_or_perpetual","attribution_restrictions_and_revocation","source_or_capture_date","original_master_and_derivative_relationship","checksum_integrity_and_replacement_history","access_class_and_confidentiality","product_family_appearance_applicability","related_entity_references","exact_or_representative_and_visual_truth_limits","language_locale_and_embedded_text","caption_alt_and_transcript_state","accessibility_review","production_ready_derivative_status","lifecycle_state_review_trigger_and_version","retention_and_deletion_authority","evidence_owner","independent_reviewer_and_reviewed_at","publication_context_and_eligibility"]
EXPECTED_INTAKE = {"intake_state":"AWAITING_EXTERNAL_EVIDENCE","required_fields":REQUIRED_FIELDS,"acceptable_source_classes":["DAMAVAND_OWNED_ORIGINAL_201_51","COMMISSIONED_DURABLE_COMMERCIAL_RIGHTS","SUPPLIER_MANUFACTURER_EXPLICIT_WRITTEN_DAMAVAND_COMMERCIAL_SITE_PERMISSION"],"redaction_allowed":True,"verification_effect":"EVIDENCE_REVIEW_ONLY_NO_AUTOMATIC_VERIFICATION","evidence_owner_must_differ_from_reviewer":True,"reject_if_any_state":["MISSING","CONFLICTING","EXPIRED","RESTRICTED","UNREVIEWED"],"acceptance_rule":"ALL_FIELDS_CURRENT_CONSISTENT_AND_INDEPENDENTLY_REVIEWED"}
EXPECTED_NAMING = {"policy_state":"REVIEW_PENDING_FOUNDER_APPROVAL","filename_is_not_identity":True,"public_safe_only":True,"forbidden_content":["PII","CONFIDENTIAL","PRICE","TEMPORARY","PRESENTATION_ONLY"],"logical_pattern":"{entity-type}-{stable-public-safe-reference}-{asset-role}-{view-or-sequence}-{locale}-{revision}.{extension}","logical_pattern_approved_for_use":False,"literal_vocabulary_approved":False,"maximum_length_approved":False,"namespace_and_collision_policy_approved":False,"migration_behavior_approved":False,"rename_folder_format_dimension_optimization_approved":False,"asset_id_minted":False}
STATE_RULES = [
    {"state":"received","public_use_allowed":False,"meaning":"INTAKE_ONLY"},
    {"state":"rights_review","public_use_allowed":False,"meaning":"RIGHTS_REVIEW_IN_PROGRESS"},
    {"state":"content_review","public_use_allowed":False,"meaning":"APPLICABILITY_ACCESSIBILITY_TECHNICAL_REVIEW"},
    {"state":"approved","public_use_allowed":False,"meaning":"CONTEXT_SPECIFIC_APPROVAL_PENDING_SEPARATE_PUBLICATION"},
    {"state":"published","public_use_allowed":True,"meaning":"SEPARATELY_AUTHORIZED_APPROVED_CONTEXT_ONLY"},
    {"state":"restricted","public_use_allowed":False,"meaning":"PUBLIC_USE_PROHIBITED"},
    {"state":"expired","public_use_allowed":False,"meaning":"PUBLIC_USE_PROHIBITED"},
    {"state":"archived","public_use_allowed":False,"meaning":"INTERNAL_OR_PROTECTED_ONLY"},
]
EXPECTED_LIFECYCLE = {"allowed_states":[row["state"] for row in STATE_RULES],"state_rules":STATE_RULES,"direct_received_to_approved_or_published_allowed":False,"automatic_transition_allowed":False,"records":[],"progression_performed":False}
EXPECTED_CHECKLIST = {"required_checks":["asset_exists_and_integrity_valid","technical_quality_pass","ownership_and_source_verified","current_usage_modification_publication_rights_verified","rights_expiry_and_restrictions_valid","public_access_class_approved","exact_product_family_appearance_applicability_verified","visual_truth_limits_reviewed","localization_and_embedded_text_reviewed","accessibility_metadata_ready","production_derivative_and_master_integrity_verified","evidence_owner_differs_from_independent_reviewer","independent_review_pass","context_specific_publication_approval"],"all_checks_passed":False,"publication_authorized":False}
EXPECTED_STATUS = {"repository_package_state":"REPOSITORY_READY","workflow_status":"BLOCKED_EXTERNAL_INPUT","readiness_classification":"BLOCKED_EXTERNAL_EVIDENCE","prerequisite":"UNMET","founder_action_required":"PROVIDE_RIGHTS_SAFE_MEDIA_PACKET"}
EXPECTED_GATE = {"eligible":False,"met_count":5,"unmet_count":7,"total":12,"transition_recorded":False}
EXPECTED_NO_GO = {"commerce_state":"INQUIRY_ONLY","availability":"MISSING_DATA_VALUE","brand":"ABSENT_NOT_PROMOTED","color":"ABSENT_NOT_PROMOTED","price":"ABSENT","stock":"ABSENT","eta_sla":"ABSENT","supplier_truth":"ABSENT","asset_or_right_created":False,"asset_creation_upload_copy_transform_optimize_derivative_or_naming":False,"competitor_or_internet_media_reuse":False,"generated_or_synthetic_media":False,"publication":False,"product_combination_sku_mutation":False,"c002_mutation":False,"gate_transition":False,"wordpress_woocommerce":False,"runtime":False,"staging":False,"production":False,"deploy":False,"merge":False,"auto_merge":False,"branch_deletion":False,"m4_or_successor_mission":False}

class StrictLoader(yaml.SafeLoader):
    pass

def _mapping(loader: StrictLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)

def _json_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result

def bounded(value: Any, depth: int = 0, nodes: list[int] | None = None) -> int:
    if nodes is None:
        nodes = [0]
    if depth > MAX_DEPTH:
        raise ValueError("depth cap exceeded")
    nodes[0] += 1
    if nodes[0] > MAX_NODES:
        raise ValueError("node cap exceeded")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("nonfinite value")
    if isinstance(value, dict):
        for key, item in value.items():
            bounded(key, depth + 1, nodes); bounded(item, depth + 1, nodes)
    elif isinstance(value, list):
        for item in value:
            bounded(item, depth + 1, nodes)
    return nodes[0]

def load(path: Path) -> Any:
    candidate = path if path.is_absolute() else ROOT / path
    if candidate.is_symlink() or any(parent.is_symlink() for parent in candidate.parents if parent.exists()):
        raise ValueError("symlink paths are forbidden")
    resolved = candidate.resolve(strict=True)
    resolved.relative_to(ROOT.resolve())
    if not resolved.is_file() or resolved.stat().st_size > MAX_BYTES:
        raise ValueError("regular-file/byte-cap violation")
    raw = resolved.read_text(encoding="utf-8")
    if resolved.suffix == ".json":
        value = json.loads(raw, object_pairs_hook=_json_pairs, parse_constant=lambda item: (_ for _ in ()).throw(ValueError(f"nonfinite JSON: {item}")))
    else:
        value = yaml.load(raw, Loader=StrictLoader)
    bounded(value)
    return value

def digest(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()

def git_blob_oid(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def schema_issues(schema: Any) -> list[str]:
    issues: list[str] = []
    forbidden = {"allOf","anyOf","oneOf","not","if","then","else","contains","patternProperties","unevaluatedProperties","unevaluatedItems","prefixItems","dependentSchemas","dependentRequired","propertyNames","contentSchema","contentEncoding","contentMediaType"}
    object_keys = {"properties","required","additionalProperties","minProperties","maxProperties"}
    array_keys = {"items","minItems","maxItems","uniqueItems"}
    string_keys = {"minLength","maxLength","pattern","format"}
    numeric_keys = {"minimum","maximum","exclusiveMinimum","exclusiveMaximum","multipleOf"}

    def visit(node: Any, path: str) -> None:
        if node is True or node == {}:
            issues.append(f"PERMISSIVE_SCHEMA:{path}"); return
        if node is False:
            return
        if not isinstance(node, dict):
            issues.append(f"SCHEMA_NODE_TYPE:{path}"); return
        if forbidden.intersection(node):
            issues.append(f"UNSUPPORTED_SCHEMA_KEYWORD:{path}")
        ref = node.get("$ref")
        if isinstance(ref, str):
            if not ref.startswith("#/"):
                issues.append(f"REMOTE_SCHEMA_REF:{path}")
            if set(node) != {"$ref"}:
                issues.append(f"REF_SIBLING:{path}")
            return
        kind = node.get("type")
        if isinstance(kind, list):
            issues.append(f"TYPE_UNION:{path}")
        if not any(key in node for key in ("type","const","enum")):
            issues.append(f"NON_ASSERTIVE_SCHEMA:{path}")
        if object_keys.intersection(node) and kind != "object":
            issues.append(f"WRONG_INSTANCE_OBJECT:{path}")
        if array_keys.intersection(node) and kind != "array":
            issues.append(f"WRONG_INSTANCE_ARRAY:{path}")
        if string_keys.intersection(node) and kind != "string":
            issues.append(f"WRONG_INSTANCE_STRING:{path}")
        if numeric_keys.intersection(node) and kind not in {"integer","number"}:
            issues.append(f"WRONG_INSTANCE_NUMBER:{path}")
        if kind == "object" and node.get("additionalProperties") is not False:
            issues.append(f"OPEN_SCHEMA:{path}")
        if kind == "array" and ("items" not in node or node.get("items") is True):
            issues.append(f"OPEN_ARRAY:{path}")
        for container in ("properties", "$defs"):
            value = node.get(container)
            if value is not None:
                if not isinstance(value, dict):
                    issues.append(f"SCHEMA_CONTAINER:{path}/{container}")
                else:
                    for name, child in value.items():
                        visit(child, f"{path}/{container}/{name}")
        if "items" in node:
            visit(node["items"], f"{path}/items")
        if isinstance(node.get("additionalProperties"), dict):
            visit(node["additionalProperties"], f"{path}/additionalProperties")

    visit(schema, "#")
    if issues:
        return sorted(set(issues))
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        return [f"SCHEMA_META:{type(exc).__name__}"]
    return []

def changed_paths() -> list[str]:
    changed = subprocess.run(["git","diff","--name-only","HEAD"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.splitlines()
    untracked = subprocess.run(["git","ls-files","--others","--exclude-standard"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.splitlines()
    return sorted(set(changed + untracked))

def archaeology_issues(root: Path = ROOT) -> list[str]:
    issues: list[str] = []
    expected_files = {row["path"]: row["git_blob_oid"] for row in FILE_MANIFEST}
    expected_dirs = {"assets","assets/brand","assets/documents","assets/fonts","assets/images","assets/images/optimized","assets/images/source","repository/assets","public/wp-content/uploads"}
    scan_roots = [root / "assets", root / "repository/assets", root / "public/wp-content/uploads"]
    actual_files: set[str] = set()
    actual_dirs: set[str] = set()
    for scan_root in scan_roots:
        if scan_root.is_symlink() or not scan_root.is_dir():
            issues.append(f"ARCHAEOLOGY_LIVE:root:{scan_root.relative_to(root)}"); continue
        actual_dirs.add(scan_root.relative_to(root).as_posix())
        for path in scan_root.rglob("*"):
            rel = path.relative_to(root).as_posix()
            if path.is_symlink():
                issues.append(f"ARCHAEOLOGY_LIVE:symlink:{rel}")
            elif path.is_dir():
                actual_dirs.add(rel)
            elif path.is_file():
                actual_files.add(rel)
            else:
                issues.append(f"ARCHAEOLOGY_LIVE:special:{rel}")
    if actual_files != set(expected_files):
        issues.append("ARCHAEOLOGY_LIVE:file_set")
    if actual_dirs != expected_dirs:
        issues.append("ARCHAEOLOGY_LIVE:directory_set")
    for rel, oid in expected_files.items():
        path = root / rel
        if not path.is_file() or path.is_symlink() or git_blob_oid(path) != oid:
            issues.append(f"ARCHAEOLOGY_LIVE:blob:{rel}")
    for row in TREE_MANIFEST:
        rel = row["path"]
        if row["state"] == "ABSENT":
            if (root / rel).exists() or (root / rel).is_symlink():
                issues.append(f"ARCHAEOLOGY_LIVE:absent:{rel}")
        else:
            result = subprocess.run(["git","rev-parse",f"HEAD:{rel}"], cwd=root, capture_output=True, text=True)
            if result.returncode or result.stdout.strip() != row["git_tree_oid"]:
                issues.append(f"ARCHAEOLOGY_LIVE:tree:{rel}")
    return sorted(set(issues))

def validate(contract: Any, schema: Any, registry: Any, *, synthetic: bool, allow_unpinned: bool, check_worktree: bool = True) -> list[str]:
    issues = schema_issues(schema)
    contract_keys = ["contract_id","contract_version","record_kind","schema","registry","authority","dependencies","dependency_pins","source_policy","owner_policy","validation"]
    expected_contract = {
        "contract_id":"ft-rb-01-rights-safe-media-readiness","contract_version":"1.0.0","record_kind":"rights-safe-media-readiness",
        "schema":{"path":"repository/data/schemas/ft-rb-01-rights-safe-media-readiness.schema.json","draft":"https://json-schema.org/draft/2020-12/schema"},
        "registry":{"path":"repository/data/registries/extensions/ftrb01/rights-safe-media-readiness.yaml"},
        "authority":EXPECTED_AUTHORITY,"dependencies":DEPENDENCIES,"dependency_pins":PINS,"source_policy":EXPECTED_SOURCE_POLICY,"owner_policy":EXPECTED_OWNER_POLICY,"validation":EXPECTED_VALIDATION,
    }
    if not isinstance(contract, dict) or list(contract) != contract_keys or contract != expected_contract:
        issues.append("CONTRACT_EXACTNESS")
    if not isinstance(registry, dict):
        return sorted(set(issues + ["REGISTRY_TYPE"]))
    expected_keys = ["registry_id","registry_version","mission_id","fixture_mode","fixture_identity","campaign_authorized_starting_main","mission_base_main","status_as_of","source","exact_changed_paths","predecessors","repository_archaeology","readiness_dimensions","intake_contract","naming_specification","owner_lifecycle","publication_checklist","lane_status","gate_snapshot","no_claim_boundaries"]
    if list(registry) != expected_keys or registry.get("registry_id") != "ftrb01:rights-safe-media-readiness" or registry.get("registry_version") != "1.0.0" or registry.get("mission_id") != "FT-RB-01" or registry.get("campaign_authorized_starting_main") != "310d0ac3f6f9da67a975a32beb0b55361aa176d5" or registry.get("mission_base_main") != "a6fa08ba8bda06fba4e92aa58945fd01c7497dcf":
        issues.append("REGISTRY_EXACTNESS")
    expected_mode = "SYNTHETIC" if synthetic else "CANONICAL"
    expected_identity = "SYNTHETIC_FTRB01_MEDIA" if synthetic else "CANONICAL_FTRB01_MEDIA"
    expected_time = "2026-08-23T17:00:01+03:30" if synthetic else "2026-08-23T17:00:00+03:30"
    if registry.get("fixture_mode") != expected_mode or registry.get("fixture_identity") != expected_identity or registry.get("status_as_of") != expected_time:
        issues.append("MODE_OR_CHRONOLOGY")
    sections = {
        "source":EXPECTED_SOURCE,"exact_changed_paths":ALLOWLIST,"predecessors":EXPECTED_PREDECESSORS,
        "repository_archaeology":EXPECTED_ARCHAEOLOGY,"readiness_dimensions":EXPECTED_DIMENSIONS,
        "intake_contract":EXPECTED_INTAKE,"naming_specification":EXPECTED_NAMING,"owner_lifecycle":EXPECTED_LIFECYCLE,
        "publication_checklist":EXPECTED_CHECKLIST,"lane_status":EXPECTED_STATUS,"gate_snapshot":EXPECTED_GATE,"no_claim_boundaries":EXPECTED_NO_GO,
    }
    for name, expected in sections.items():
        if registry.get(name) != expected:
            issues.append(f"{name.upper()}_EXACTNESS")
    if not issues:
        try:
            for error in Draft202012Validator(schema).iter_errors(registry):
                issues.append(f"SCHEMA_VALIDATION:{error.json_path}")
        except Exception as exc:
            issues.append(f"SCHEMA_VALIDATION_EXCEPTION:{type(exc).__name__}")
    if check_worktree:
        try:
            if changed_paths() != ALLOWLIST:
                issues.append("ALLOWLIST_ACTUAL_DIFF")
        except Exception as exc:
            issues.append(f"ALLOWLIST_ACTUAL_DIFF:{type(exc).__name__}")
        issues.extend(archaeology_issues())
        runner = ROOT / "scripts/test.sh"
        try:
            text = runner.read_text(encoding="utf-8")
            if text.count('ft_rb_01_media_validator="repository/data/validation/validate_ft_rb_01_rights_safe_media_readiness.py"') != 1 or text.count('ft_rb_campaign_status_validator="repository/data/validation/validate_ft_rb_campaign_status.py"') != 1:
                issues.append("RUNNER_DISPATCH")
        except Exception as exc:
            issues.append(f"RUNNER_DISPATCH:{type(exc).__name__}")
    for key, path in DEPENDENCIES.items():
        try:
            if digest(load(ROOT / path)) != PINS[key]:
                issues.append(f"DEPENDENCY_PIN:{key}")
        except Exception as exc:
            issues.append(f"DEPENDENCY_PIN:{key}:{type(exc).__name__}")
    try:
        c009 = load(C009)
        leaf = c009.get("promotion", {}).get("canonical_leaf", {}) if isinstance(c009, dict) else {}
        owner_ids = [leaf.get("source_pilot_id"), leaf.get("canonical_combination_id"), leaf.get("entity", {}).get("entity_id")]
        if not isinstance(leaf, dict) or not all(isinstance(item, str) and item for item in owner_ids) or len(set(owner_ids)) != 3:
            issues.append("C009_OWNER_SEMANTICS")
    except Exception as exc:
        issues.append(f"C009_OWNER_SEMANTICS:{type(exc).__name__}")
    live = {"contract":digest(contract),"schema":digest(schema),("synthetic" if synthetic else "canonical"):digest(registry)}
    for key, value in live.items():
        if (DIGESTS[key] == "TO_BE_FINALIZED" and not allow_unpinned) or (DIGESTS[key] != "TO_BE_FINALIZED" and DIGESTS[key] != value):
            issues.append(f"SEMANTIC_DIGEST:{key}")
    return sorted(set(issues))

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default=str(REGISTRY))
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--allow-unpinned", action="store_true")
    args = parser.parse_args(argv)
    try:
        contract, schema, registry = load(CONTRACT), load(SCHEMA), load(Path(args.registry))
    except Exception as exc:
        print(f"LOAD_ERROR:{type(exc).__name__}:{exc}"); return 1
    original_socket = socket.socket
    socket.socket = lambda *a, **kw: (_ for _ in ()).throw(RuntimeError("network disabled"))
    try:
        issues = validate(contract, schema, registry, synthetic=args.synthetic, allow_unpinned=args.allow_unpinned)
    finally:
        socket.socket = original_socket
    if issues:
        print("\n".join(issues)); return 1
    print("FT-RB-01 rights-safe media readiness validation PASS"); return 0

if __name__ == "__main__":
    raise SystemExit(main())
