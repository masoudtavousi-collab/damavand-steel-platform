#!/usr/bin/env python3
"""Offline fail-closed validation for the bounded C009 canonical leaf promotion."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
import re
import socket
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repository/data/contracts/c009-first-commercial-slice-canonical-leaf-promotion.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/c009-first-commercial-slice-canonical-leaf-promotion.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml"
PRODUCT_CORE_SCHEMA_PATH = ROOT / "repository/data/schemas/product-core.schema.json"
MAX_BYTES = 2 * 1024 * 1024
MAX_DEPTH = 100
MAX_NODES = 50_000

EXPECTED_CONTRACT_DIGEST = "a1179a6ef97735431f89ef075e7d40c9dd6973b5eacbeca6599d9666bc7674d3"
EXPECTED_SCHEMA_DIGEST = "aea8a6dd7b521a83576bbd00ce686d3bc2477552bc4a2f3642a80b648b6e31e2"
EXPECTED_REGISTRY_DIGEST = "1b50d28ddded3a818afb82d19759713bd6c2f2b058b4020510d8b5f74a7f6a3f"
EXPECTED_SYNTHETIC_DIGEST = "a31211a48ba9be14637e16f2b02fa692bedfcf3e2800d8e79dde7bbf4bb7bc6a"

EXPECTED_CONTRACT_TOP_KEYS = [
    "contract_id", "contract_version", "record_kind", "schema", "registry", "authority",
    "source_policy", "promotion_policy", "stable_identity_policy", "validation",
    "dependencies", "dependency_pins",
]
EXPECTED_SCHEMA_BINDING = {
    "path": "repository/data/schemas/c009-first-commercial-slice-canonical-leaf-promotion.schema.json",
    "draft": "https://json-schema.org/draft/2020-12/schema",
}
EXPECTED_REGISTRY_BINDING = {
    "path": "repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml"
}
EXPECTED_AUTHORITY = {
    "mission_id": "C009",
    "one_canonical_combination_promotion_allowed": True,
    "one_canonical_sku_leaf_promotion_allowed": True,
    "exact_pilot_binding_allowed": True,
    "package_docs_validator_tests_allowed": True,
    "branch_commit_push_one_pr_allowed": True,
    "existing_product_core_owner_mutation_allowed": False,
    "additional_combination_or_leaf_allowed": False,
    "product_entity_type_invention_allowed": False,
    "product_family_or_series_rename_allowed": False,
    "controlled_value_or_unit_creation_allowed": False,
    "other_pilot_or_candidate_promotion_allowed": False,
    "cartesian_generation_allowed": False,
    "brand_or_color_promotion_allowed": False,
    "mass_population_allowed": False,
    "availability_stock_price_eta_sla_supplier_claim_allowed": False,
    "c002_mutation_allowed": False,
    "c008_ft1_mutation_or_reevaluation_allowed": False,
    "commerce_eligibility_activation_allowed": False,
    "wordpress_woocommerce_mutation_allowed": False,
    "runtime_staging_production_mutation_allowed": False,
    "import_deployment_publication_allowed": False,
    "auto_merge_or_merge_allowed": False,
    "branch_deletion_allowed": False,
    "successor_mission_allowed": False,
}
EXPECTED_SOURCE_POLICY = {
    "repository": "masoudtavousi-collab/damavand-steel-platform",
    "slack_channel_id": "C0BNHRRTE9F", "founder_user_id": "U0BNFS43TBL",
    "direction_parent_ts": "1787398697.475999",
    "direction_parent_title": "FOUNDER DECISION — FIRST COMMERCIAL SLICE — 2026-08-22",
    "direction_thread_reply_count": 21, "authorization_ts": "1787440938.184179",
    "authorization_reply_index": 21, "authorization_direct_thread_reply_count": 0,
    "authorization_title": "FOUNDER / PROJECT COMMANDER EXECUTION AUTHORIZATION — C009 FIRST COMMERCIAL SLICE CANONICAL LEAF PROMOTION — 2026-08-23",
    "execution_command_sha256": "0e0a03ae9f445e6d42c6a45284b2869b007fcd709eb1e442ce30bf1cd4205f16",
    "authorized_starting_main": "f226381622e94a1d0b2d598f5ed933bde37bd7df",
    "predecessor_post_merge_ci_run": 32604542391, "predecessor_post_merge_ci_result": "PASS",
    "authorized_branch": "codex/c009-first-commercial-slice-canonical-leaf-promotion",
    "exact_source_count": 3,
}
EXPECTED_PROMOTION_POLICY = {
    "hierarchy_model": ["CATALOG", "PLATFORM", "FAMILY", "SERIES", "VARIANT_RULE_SET", "SKU"],
    "product_entity_type_exists": False, "target_pilot_id": "pilot:f5922666261e",
    "target_family_id": "prd:family:a10c6d8ceabc", "target_family_label": "Stainless Steel Pipe",
    "target_series_id": "prd:series:e1657d35ac35", "target_series_label": "لوله استیل دکوراتیو",
    "target_variant_rule_set_id": "prd:variant-rule-set:eb255662accc",
    "target_profile_id": "pprof:4c556c63c1a9", "exact_combination_count": 1,
    "exact_leaf_count": 1, "product_identity_semantic_owner": "PRODUCT_CORE",
    "combination_validity_semantic_owner": "VARIANT_RULE_SET",
    "pilot_evidence_semantic_owner": "PD03B_CANONICAL_PILOT",
    "c009_role": "PERSISTENCE_AND_IMMUTABLE_BINDING_EXTENSION_ONLY",
    "authority_transfer": False, "approved_does_not_imply_import_publication_or_runtime": True,
    "availability_remains_missing_data_value": True, "commercial_sku_created": False,
}
EXPECTED_STABLE_POLICY = {
    "allocation": "CSPRNG_12_HEX_WITH_GLOBAL_COLLISION_CHECK",
    "label_slug_wordpress_woocommerce_or_commercial_sku_derived": False,
    "cross_namespace_suffix_collision_forbidden": True,
    "historical_reference_reuse_forbidden": True,
}
EXPECTED_VALIDATION_POLICY = {
    "offline_only": True, "network_allowed": False, "side_effects_allowed": False,
    "closed_schema_required": True, "local_refs_only": True,
    "duplicate_yaml_and_json_keys_rejected": True, "non_finite_numbers_rejected": True,
    "deterministic_sorted_errors": True, "path_escape_symlink_byte_depth_node_caps_enforced": True,
    "exact_order_counts_and_bindings_required": True, "predecessor_semantic_pins_required": True,
    "semantic_digest_pinning_required": True, "mutation_manifest_dispatch_required": True,
}

EXPECTED_DEPENDENCIES = {
    "product_core_contract": "repository/data/contracts/product-core.contract.yaml",
    "product_core_schema": "repository/data/schemas/product-core.schema.json",
    "product_entities_registry": "repository/data/registries/product-entities.yaml",
    "product_entity_types_registry": "repository/data/registries/product-entity-types.yaml",
    "product_statuses_registry": "repository/data/registries/product-statuses.yaml",
    "pd03a_contract": "repository/data/contracts/pd03a-pilot-prerequisite.contract.yaml",
    "pd03a_schema": "repository/data/schemas/pd03a-pilot-prerequisite.schema.json",
    "pd03a_registry": "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml",
    "pd03b_contract": "repository/data/contracts/pd03b-canonical-pilot.contract.yaml",
    "pd03b_schema": "repository/data/schemas/pd03b-canonical-pilot.schema.json",
    "pd03b_registry": "repository/data/registries/extensions/pd03b/canonical-pilots.yaml",
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
}
EXPECTED_DEPENDENCY_PINS = {
    "product_core_contract": "4f297d98e0864fbfad6f872ac75c873f26a8d059bd57ea282b4af892d0e9a5d9",
    "product_core_schema": "1a4ae6ee76089b2ca82e2ecf1753577f0f6c0e558b631ed16238ec24773931da",
    "product_entities_registry": "69ca32a8a0bb5958f8442ab3aaf812fc7e25eb4b89c20ab6d7f7f16bf75c4fca",
    "product_entity_types_registry": "14ebf20c0c6ed5fe0d7ae9e80b3bf3e822edc9c9ace9df97ae409a7126ae74e1",
    "product_statuses_registry": "bba27ebfa858f5bb29ed0005107d420a0ed004a15b0098bc99d55e1098083b0a",
    "pd03a_contract": "eeb45b9171d118e763678f85521749f1d256150e369fe1df910ed9479260f48b",
    "pd03a_schema": "cdbd6176ac890c3f54bc3ea2add6d8661d709c85e566456f3565ab221eff001e",
    "pd03a_registry": "c6ec36726a2417b153836d3c3f2503e993bf7a4d14d84e55ac27b83281492a3b",
    "pd03b_contract": "1d711b2467550ab57153e82a5555863d0bfe2a6aeee469a0f4b18162f990be3a",
    "pd03b_schema": "27ab146e3a93cf102ec7fe2c73c9923dbc20437c731823fdb36e5d650d70638d",
    "pd03b_registry": "ca46b8ec00a4dadfcfc281d52eadf7946609aa21223668d742bcb950f4e7fdac",
    "c002_contract": "923731cb080b0ecc05abb21b1189bfdd0df94297780cce364bb791479f7f47e3",
    "c002_schema": "1e1b1977f369ab7e5961d4e69111682d1117bc6eeedf666a9e568f0115952741",
    "c002_registry": "deb0215d2b5f4b5ec0061f937aec9c3e37cf97c94432a23737bf5756cef9587e",
    "c006_contract": "131b2c79a3d017c65bac896e95e7a638164a77b821546e5217266f6d3829dcc0",
    "c006_schema": "9a9009c4431c097c062dcef81fad03fae51784ff466bb8cc5db6ed14237f79e3",
    "c006_registry": "5b5510af1b521daa7b2539007cab0681885f2bbc3eff4a75dde67cb38857ad8b",
    "c008_contract": "bf450358e11c82df7ae41a7777bd2889f2c4b7cffe64a5f2ee21f3303cbd2f5c",
    "c008_schema": "82f8dbfb93233b6d40603a56bdb7661ee4d477003ba13b97c59d80bb0c8a27af",
    "c008_registry": "bd06e76da52750b9b54c09ccba88421ae82778dce84a4afa15475a88297081d9",
    "c008_r1_contract": "da5a70f0e7330df8afab52e931f664bda453266740646a4d4183d25370ea75d7",
    "c008_r1_schema": "fea342c3210dca9e5c2e98030bf8b5e64464cdd550cbb3b5675109c49673b904",
    "c008_r1_registry": "9dcf2cc7cc10ab01a9b97ab40ac896debd12e6f25ad5b7e700921a6c782fb87b",
    "c008_ft1_contract": "4c940eed75fe433bc8adbc85cb45954068b233cc1de6d80b40bc28eb71466fb5",
    "c008_ft1_schema": "8eb3c93a37932e6676e8a3d1c22e0c35d3f6a4d0f47f7467ea718f466ceabd80",
    "c008_ft1_registry": "799dad2f7fdf9f6ffb5a9fe37c707f222f6f92f1cc6b1e251bd3f366dd2e9cf3",
}

EXPECTED_SOURCE = {
    "source_id": "C009-SOURCE-001", "source_class": "FOUNDER_EXECUTION_AUTHORIZATION",
    "bound_source_count": 3, "channel_id": "C0BNHRRTE9F",
    "direction_parent_locator": "slack:C0BNHRRTE9F:1787398697.475999",
    "direction_parent_ts": "1787398697.475999",
    "direction_parent_title": "FOUNDER DECISION — FIRST COMMERCIAL SLICE — 2026-08-22",
    "direction_parent_authored_at": "2026-08-22T15:08:17.475999+03:30",
    "direction_thread_complete": True, "direction_thread_reply_count": 21,
    "authorization_locator": "slack:C0BNHRRTE9F:1787440938.184179",
    "authorization_ts": "1787440938.184179",
    "authorization_title": "FOUNDER / PROJECT COMMANDER EXECUTION AUTHORIZATION — C009 FIRST COMMERCIAL SLICE CANONICAL LEAF PROMOTION — 2026-08-23",
    "authorization_authored_at": "2026-08-23T02:52:18.184179+03:30",
    "authorization_author_id": "U0BNFS43TBL", "authorization_reply_index": 21,
    "authorization_direct_thread_complete": True, "authorization_direct_thread_reply_count": 0,
    "execution_command_sha256": "0e0a03ae9f445e6d42c6a45284b2869b007fcd709eb1e442ce30bf1cd4205f16",
    "execution_command_role": "CURRENT_FOUNDER_TASK_INSTRUCTION",
    "authorized_branch": "codex/c009-first-commercial-slice-canonical-leaf-promotion",
}
EXPECTED_PREDECESSOR = {
    "mission": "C008-FT1", "status": "COMPLETED_ARCHIVE_ONLY",
    "merge_commit": "f226381622e94a1d0b2d598f5ed933bde37bd7df",
    "post_merge_ci_run": 32604542391, "post_merge_ci_result": "PASS", "tree_integrated": True,
}
EXPECTED_AXES = [
    {"attribute_key": "grade", "attribute_id": "attr:28565665c910", "term_id": "vterm:a891bfdfdd6b", "canonical_value": "201", "unit_id": None},
    {"attribute_key": "finish", "attribute_id": "attr:1926e2ad4629", "term_id": "vterm:1df9a5493546", "canonical_value": "Silver", "unit_id": None},
    {"attribute_key": "diameter", "attribute_id": "attr:252ab175be12", "term_id": None, "canonical_value": "51", "unit_id": "unit:000000000002"},
    {"attribute_key": "thickness", "attribute_id": "attr:d1890e85f84c", "term_id": None, "canonical_value": "0.50", "unit_id": "unit:000000000002"},
    {"attribute_key": "length", "attribute_id": "attr:d782d47eae7f", "term_id": None, "canonical_value": "6", "unit_id": "unit:000000000001"},
]
EXPECTED_C002 = {
    "readiness": "NOT_READY", "resolved_count": 6, "unresolved_count": 3,
    "founder_selection_ready": False, "candidate_registry_count": 0,
    "supply_evidence": "SUBMITTED_REVIEW_INCOMPLETE", "photo_content_readiness": "MISSING_EVIDENCE",
    "fulfillment_risk": "SUBMITTED_REVIEW_INCOMPLETE", "mutation_effect": False,
}
EXPECTED_FT1 = {
    "gate_id": "FAST_TRACK_INQUIRY_LAUNCH_ELIGIBLE", "gate_state": False, "met_count": 4,
    "prerequisite_count": 12, "canonical_product_promotion_prerequisite_state": "NOT_AUTHORIZED",
    "gate_reevaluated": False, "owner_mutated": False,
}

@dataclass(frozen=True)
class Issue:
    code: str
    message: str


class StrictLoader(yaml.SafeLoader):
    pass


def _construct_mapping(loader: StrictLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


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
        total = 1 + sum(_bounded_tree(item, depth + 1) for item in value)
    else:
        total = 1
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("non-finite number")
    if total > MAX_NODES:
        raise ValueError("document exceeds maximum node count")
    return total


def safe_path(path: Path, label: str) -> Path:
    if path.is_symlink() or any(part.is_symlink() for part in [path, *path.parents] if part.exists()):
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
        value = json.loads(text, object_pairs_hook=_json_pairs, parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"non-finite JSON token: {token}")))
    else:
        value = yaml.load(text, Loader=StrictLoader)
    _bounded_tree(value)
    return value


def semantic_digest(value: Any) -> str:
    canonical = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def add(issues: list[Issue], code: str, message: str) -> None:
    issues.append(Issue(code, message))


def audit_schema(schema: Any) -> list[Issue]:
    issues: list[Issue] = []
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        add(issues, "SCHEMA_META", str(exc))
        return issues

    def visit(node: Any, path: str) -> None:
        if node is True:
            add(issues, "PERMISSIVE_SCHEMA", f"permissive true schema forbidden at {path}")
            return
        if node is False:
            return
        if isinstance(node, dict):
            if not node:
                add(issues, "PERMISSIVE_SCHEMA", f"empty permissive schema forbidden at {path}")
                return
            if path.endswith("/properties") or path.endswith("/$defs"):
                for key, child in node.items():
                    visit(child, f"{path}/{key}")
                return
            forbidden_applicators = {
                "allOf", "anyOf", "oneOf", "not", "if", "then", "else",
                "dependentSchemas", "contains", "patternProperties", "propertyNames",
                "unevaluatedProperties", "unevaluatedItems",
            }
            present_applicators = sorted(forbidden_applicators.intersection(node))
            if present_applicators:
                add(issues, "PERMISSIVE_APPLICATOR", f"unsupported schema applicator at {path}: {present_applicators}")
            if not any(key in node for key in ("$ref", "const", "enum", "type")):
                add(issues, "NON_ASSERTIVE_SCHEMA", f"schema has no instance-applicable type/ref/const/enum assertion at {path}")
            ref = node.get("$ref")
            if isinstance(ref, str) and not ref.startswith("#/"):
                add(issues, "REMOTE_SCHEMA_REF", f"non-local ref at {path}: {ref}")
            if isinstance(ref, str) and set(node) != {"$ref"}:
                add(issues, "REF_SIBLING", f"local ref must be the sole schema keyword at {path}")
            if isinstance(node.get("const"), (dict, list)):
                add(issues, "CONTAINER_LITERAL_SCHEMA", f"container-valued const is forbidden at {path}")
            enum_values = node.get("enum")
            if isinstance(enum_values, list) and any(isinstance(value, (dict, list)) for value in enum_values):
                add(issues, "CONTAINER_LITERAL_SCHEMA", f"container-valued enum is forbidden at {path}")
            node_type = node.get("type")
            if isinstance(node_type, list) and "object" in node_type:
                add(issues, "OBJECT_UNION_SCHEMA", f"object type unions are forbidden at {path}")
            object_keywords = {
                "properties", "patternProperties", "required", "dependentRequired",
                "dependentSchemas", "propertyNames", "minProperties", "maxProperties",
                "unevaluatedProperties",
            }
            permits_object = (
                node_type == "object"
                or (isinstance(node_type, list) and "object" in node_type)
                or any(key in node for key in object_keywords)
            )
            if permits_object and node.get("additionalProperties") is not False:
                add(issues, "OPEN_SCHEMA", f"object is not closed at {path}")
            for container_key in ("properties", "$defs"):
                container = node.get(container_key)
                if isinstance(container, dict):
                    visit(container, f"{path}/{container_key}")
            prefix_items = node.get("prefixItems")
            if isinstance(prefix_items, list):
                for index, child in enumerate(prefix_items):
                    visit(child, f"{path}/prefixItems/{index}")
            if "items" in node:
                visit(node["items"], f"{path}/items")

    visit(schema, "#")
    return issues


def validate_contract(contract: Any) -> list[Issue]:
    issues: list[Issue] = []
    if not isinstance(contract, dict) or list(contract) != EXPECTED_CONTRACT_TOP_KEYS:
        add(issues, "CONTRACT_EXACTNESS", "contract top-level keys/order must be exact")
        return issues
    expected_scalars = {
        "contract_id": "c009-first-commercial-slice-canonical-leaf-promotion",
        "contract_version": "1.0.0",
        "record_kind": "canonical-product-leaf-promotion-extension",
    }
    for key, expected in expected_scalars.items():
        if contract.get(key) != expected:
            add(issues, "CONTRACT_EXACTNESS", f"contract {key} drift")
    checks = [
        ("schema", EXPECTED_SCHEMA_BINDING), ("registry", EXPECTED_REGISTRY_BINDING),
        ("authority", EXPECTED_AUTHORITY), ("source_policy", EXPECTED_SOURCE_POLICY),
        ("promotion_policy", EXPECTED_PROMOTION_POLICY), ("stable_identity_policy", EXPECTED_STABLE_POLICY),
        ("validation", EXPECTED_VALIDATION_POLICY), ("dependencies", EXPECTED_DEPENDENCIES),
        ("dependency_pins", EXPECTED_DEPENDENCY_PINS),
    ]
    for key, expected in checks:
        if contract.get(key) != expected:
            add(issues, "CONTRACT_EXACTNESS", f"contract {key} must match exact policy")
    return issues


def validate_dependencies(contract: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    for key, relative in EXPECTED_DEPENDENCIES.items():
        try:
            value = load_document(ROOT / relative, f"dependency {key}")
            if semantic_digest(value) != EXPECTED_DEPENDENCY_PINS[key]:
                add(issues, "DEPENDENCY_PIN", f"semantic drift: {key}")
        except Exception as exc:
            add(issues, "DEPENDENCY_PIN", f"cannot load {key}: {exc}")
    return issues


def _global_id_collision(registry: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    promotion = registry.get("promotion", {})
    combination_id = promotion.get("canonical_combination", {}).get("combination_id")
    sku_id = promotion.get("canonical_leaf", {}).get("entity", {}).get("entity_id")
    suffixes = [str(combination_id).split(":")[-1], str(sku_id).split(":")[-1]]
    if len(suffixes) != len(set(suffixes)):
        add(issues, "STABLE_ID_COLLISION", "new stable-ID suffixes collide with each other")
    roots = [ROOT / "repository/data/registries"]
    for root in roots:
        for path in root.rglob("*.yaml"):
            if "extensions/c009" in path.as_posix():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue
            for suffix in suffixes:
                if suffix in text:
                    add(issues, "STABLE_ID_COLLISION", f"new suffix already exists outside C009: {suffix}")
    return issues


def _forbidden_population_scan(value: Any, path: str, issues: list[Issue]) -> None:
    forbidden = {
        "products", "product_values", "skus", "prices", "stock_records", "availability_records",
        "supplier_records", "mass_observations", "wordpress_objects", "woocommerce_objects",
        "runtime_objects", "staging_objects", "production_objects", "publications", "deployments",
    }
    if isinstance(value, dict):
        for key, child in value.items():
            if key in forbidden:
                add(issues, "FORBIDDEN_POPULATION_KEY", f"forbidden key at {path}/{key}")
            _forbidden_population_scan(child, f"{path}/{key}", issues)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _forbidden_population_scan(child, f"{path}/{index}", issues)


def validate_registry(registry: Any, schema: dict[str, Any], *, synthetic: bool = False) -> list[Issue]:
    issues: list[Issue] = []
    if not isinstance(registry, dict):
        return [Issue("REGISTRY_TYPE", "registry must be an object")]
    for error in Draft202012Validator(schema).iter_errors(registry):
        where = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add(issues, "SCHEMA", f"{where}: {error.message}")

    expected_mode = "SYNTHETIC" if synthetic else "CANONICAL"
    expected_id = "c009:201-51-canonical-leaf-promotion:synthetic" if synthetic else "c009:201-51-canonical-leaf-promotion"
    expected_class = "SYNTHETIC_VALIDATION_ONLY" if synthetic else "CANONICAL_C009_EXACT_SLICE_EXTENSION"
    expected_evaluation = "2026-08-23T03:10:01+03:30" if synthetic else "2026-08-23T03:05:01+03:30"
    expected_combination_id = "pcomb:111111111111" if synthetic else "pcomb:829e387ccdcb"
    expected_leaf_id = "prd:sku:222222222222" if synthetic else "prd:sku:66ebd0510693"
    if registry.get("fixture_mode") != expected_mode or registry.get("registry_id") != expected_id or registry.get("data_classification") != expected_class:
        add(issues, "FIXTURE_MODE", "canonical and synthetic modes must be explicit and isolated")
    if registry.get("mission_id") != "C009" or registry.get("authorized_starting_main") != EXPECTED_SOURCE_POLICY["authorized_starting_main"]:
        add(issues, "MISSION_ANCHOR", "mission identity or starting main drift")
    if registry.get("evaluation_as_of") != expected_evaluation:
        add(issues, "CHRONOLOGY", "canonical/synthetic evaluation timestamp must be exact")
    if registry.get("source") != EXPECTED_SOURCE:
        add(issues, "SOURCE_BINDING", "Founder parent/authorization/command binding must be exact")
    if registry.get("predecessor") != EXPECTED_PREDECESSOR:
        add(issues, "PREDECESSOR_BINDING", "C008-FT1 predecessor must be exact")

    archaeology = registry.get("owner_archaeology", {})
    expected_archaeology = {
        "canonical_hierarchy_model": ["CATALOG", "PLATFORM", "FAMILY", "SERIES", "VARIANT_RULE_SET", "SKU"],
        "product_entity_type_exists": False,
        "product_identity_semantic_owner": "PRODUCT_CORE",
        "combination_validity_semantic_owner": "VARIANT_RULE_SET",
        "pilot_evidence_semantic_owner": "PD03B_CANONICAL_PILOT",
        "persistence_binding_extension": "C009_CANONICAL_PROMOTION_EXTENSION",
        "persistence_binding_extension_path": "repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml",
        "authority_transfer": False,
        "existing_product_core_registry_mutated": False, "product_master_data_is_synthetic_only": True,
        "pd03a_and_pd03b_are_immutable_evidence_dependencies": True,
        "explicit_canonical_combination_required": True,
        "stable_id_allocation": "CSPRNG_12_HEX_WITH_GLOBAL_COLLISION_CHECK", "collision_check_result": "PASS_NO_COLLISION",
    }
    if archaeology != expected_archaeology:
        add(issues, "OWNER_ARCHAEOLOGY", "semantic owners, persistence role and hierarchy result must be exact")

    promotion = registry.get("promotion", {})
    family = promotion.get("family", {})
    series = promotion.get("series", {})
    vrs = promotion.get("variant_rule_set", {})
    if family != {"entity_id": "prd:family:a10c6d8ceabc", "canonical_label": "Stainless Steel Pipe", "status": "APPROVED"}:
        add(issues, "HIERARCHY_BINDING", "Family must stay Stainless Steel Pipe")
    if series != {"entity_id": "prd:series:e1657d35ac35", "parent_entity_id": "prd:family:a10c6d8ceabc", "canonical_label": "لوله استیل دکوراتیو", "status": "APPROVED"}:
        add(issues, "HIERARCHY_BINDING", "Series binding must be exact")
    expected_vrs = {"entity_id": "prd:variant-rule-set:eb255662accc", "parent_entity_id": "prd:series:e1657d35ac35", "profile_id": "pprof:4c556c63c1a9", "status": "APPROVED", "cartesian_generation_forbidden": True}
    if vrs != expected_vrs:
        add(issues, "HIERARCHY_BINDING", "Variant Rule Set/Profile binding must be exact")
    if promotion.get("target_pilot_id") != "pilot:f5922666261e":
        add(issues, "TARGET_PILOT", "only pilot:f5922666261e is authorized")

    combination = promotion.get("canonical_combination", {})
    if combination.get("combination_id") != expected_combination_id:
        add(issues, "CANONICAL_IDENTITY", "canonical/synthetic combination ID must be exact")
    if combination.get("source_pilot_id") != "pilot:f5922666261e" or combination.get("status") != "APPROVED":
        add(issues, "COMBINATION_BINDING", "canonical combination source/status drift")
    if combination.get("variant_rule_set_entity_id") != "prd:variant-rule-set:eb255662accc" or combination.get("profile_id") != "pprof:4c556c63c1a9":
        add(issues, "COMBINATION_BINDING", "combination owner/profile drift")
    if combination.get("material") != {"attribute_id": "attr:dbf5365ee1e5", "term_id": "vterm:5ff9c0ceca39", "canonical_label": "Stainless Steel", "fixed_non_axis": True}:
        add(issues, "EXACT_TUPLE", "Material must be the exact existing Stainless Steel term")
    if combination.get("axes") != EXPECTED_AXES:
        add(issues, "EXACT_TUPLE", "exact Grade/Finish/Diameter/Thickness/Length tuple or order drift")
    expected_availability = {"source_pilot_id": "pilot:f5922666261e", "state": "MISSING_DATA_VALUE", "stored_as_leaf_fact": False, "availability_claim_created": False}
    if combination.get("availability_reference") != expected_availability:
        add(issues, "AVAILABILITY_BOUNDARY", "Availability must remain a missing-data evidence reference")
    if any(combination.get(key) is not None for key in ("brand", "color", "mass")):
        add(issues, "UNAUTHORIZED_DIMENSION", "Brand, Color and Mass must stay absent")
    if combination.get("cartesian_generated") is not False or combination.get("sibling_combinations_created") != 0:
        add(issues, "CARTESIAN_GENERATION", "one explicit combination only; no siblings or Cartesian generation")

    leaf = promotion.get("canonical_leaf", {})
    entity = leaf.get("entity", {})
    expected_entity = {
        "contract_version": "1.0.0",
        "entity_id": expected_leaf_id,
        "entity_type": "SKU",
        "parent_entity_id": "prd:variant-rule-set:eb255662accc",
        "parent_entity_type": "VARIANT_RULE_SET",
        "canonical_label": "Stainless Steel Pipe 201 / Silver / 51 mm / 0.50 mm / 6 m",
        "status": "APPROVED",
        "owner": {"role": "product-data-steward"},
        "provenance": {
            "source_type": "FOUNDER_EXECUTION_AUTHORIZATION",
            "source_reference": "slack:C0BNHRRTE9F:1787440938.184179",
            "captured_by": "role:product-data-steward",
            "captured_at": "2026-08-23T02:52:18.184179+03:30",
            "evidence_status": "FOUNDER_AUTHORIZED_CANONICAL_LEAF",
        },
        "record_version": "1.0.0",
    }
    if entity != expected_entity:
        add(issues, "SKU_EXACTNESS", "canonical/synthetic SKU identity, label, owner and provenance must be exact")
    if entity.get("entity_type") != "SKU" or entity.get("parent_entity_id") != "prd:variant-rule-set:eb255662accc" or entity.get("parent_entity_type") != "VARIANT_RULE_SET":
        add(issues, "SKU_HIERARCHY", "one SKU leaf must be a direct child of the exact Variant Rule Set")
    if entity.get("status") != "APPROVED" or entity.get("owner") != {"role": "product-data-steward"}:
        add(issues, "SKU_LIFECYCLE", "leaf status/owner drift")
    try:
        product_schema = load_document(PRODUCT_CORE_SCHEMA_PATH, "Product Core schema")
        for error in Draft202012Validator(product_schema).iter_errors(entity):
            add(issues, "SKU_PRODUCT_CORE_SCHEMA", error.message)
    except Exception as exc:
        add(issues, "SKU_PRODUCT_CORE_SCHEMA", str(exc))
    if leaf.get("source_pilot_id") != "pilot:f5922666261e" or leaf.get("canonical_combination_id") != combination.get("combination_id"):
        add(issues, "LEAF_COMBINATION_BINDING", "leaf/pilot/combination binding drift")
    if leaf.get("public_commercial_sku_code") is not None or any(leaf.get(key) is not False for key in ("availability_fact_created", "import_ready", "publication_ready", "runtime_ready")):
        add(issues, "SKU_COMMERCIAL_BOUNDARY", "canonical leaf must create no commercial/runtime fact or readiness")
    binding = promotion.get("immutable_binding", {})
    expected_binding = {"pilot_id": "pilot:f5922666261e", "combination_id": combination.get("combination_id"), "sku_entity_id": entity.get("entity_id"), "exact_one_to_one": True, "immutable": True}
    if binding != expected_binding:
        add(issues, "IMMUTABLE_BINDING", "Pilot/combination/SKU binding must be exact and immutable")
    summary = promotion.get("promotion_summary", {})
    expected_summary = {"canonical_combination_count": 1, "canonical_leaf_count": 1, "promoted_leaf_count": 1, "other_pilots_promoted": 0, "candidate_rows_promoted": 0, "cartesian_generation": False, "product_entity_type_created": "SKU", "existing_canonical_owner_records_changed": 0}
    if summary != expected_summary:
        add(issues, "PROMOTION_COUNT", "exact one-leaf promotion summary drift")

    expected_boundaries = {"brand": "ABSENT_NOT_PROMOTED", "color": "ABSENT_NOT_PROMOTED", "availability": "MISSING_DATA_VALUE", "price": "ABSENT", "stock": "ABSENT", "eta_sla": "ABSENT", "supplier_truth": "ABSENT", "mass": "ABSENT", "inquiry_only": True, "approved_status_does_not_imply_import_publication_or_runtime": True}
    if registry.get("commercial_boundaries") != expected_boundaries:
        add(issues, "COMMERCIAL_BOUNDARY", "no-claim commercial boundary drift")
    if registry.get("c002_snapshot") != EXPECTED_C002:
        add(issues, "C002_REGRESSION", "C002 must remain 6/9 NOT_READY with zero candidates")
    if registry.get("c008_ft1_snapshot") != EXPECTED_FT1:
        add(issues, "C008_FT1_REGRESSION", "Fast-Track gate owner/state must remain FALSE 4/12 and unreevaluated")
    authority = registry.get("authority_effects", {})
    expected_true = {"one_canonical_combination_promoted", "one_canonical_sku_leaf_promoted", "exact_pilot_binding_created", "package_docs_validator_tests_created", "branch_commit_push_one_pr"}
    if set(authority) != {
        "one_canonical_combination_promoted", "one_canonical_sku_leaf_promoted", "exact_pilot_binding_created", "package_docs_validator_tests_created", "branch_commit_push_one_pr", "product_core_base_mutation", "additional_product_or_sku_population", "additional_combination_population", "controlled_value_or_unit_population", "c002_mutation", "c008_ft1_mutation_or_gate_reevaluation", "commerce_eligibility_activation", "availability_stock_price_eta_sla_supplier_claim", "wordpress_woocommerce_mutation", "runtime_staging_production_mutation", "import_deployment_publication", "auto_merge_or_merge", "branch_deletion", "successor_mission"
    } or any(authority.get(key) is not True for key in expected_true) or any(authority.get(key) is not False for key in set(authority) - expected_true):
        add(issues, "AUTHORITY_BOUNDARY", "authority effects must allow only the exact C009 package and one promotion")
    regression = registry.get("regression_anchors", {})
    expected_regression = {"base_product_entity_count": 3, "base_canonical_sku_count": 0, "pd03a_extension_entity_count": 2, "pd03b_pilot_count": 3, "c009_canonical_combination_count": 1, "c009_canonical_leaf_count": 1, "total_governed_hierarchy_sku_count_after_c009": 1, "c002_candidate_count": 0, "c002_readiness": "NOT_READY", "c002_resolved_count": 6, "c008_ft1_gate_state": False, "c008_ft1_met_count": 4, "commerce_state": "INQUIRY_ONLY", "runtime_state": "NONE", "production_state": "NONE"}
    if regression != expected_regression:
        add(issues, "REGRESSION_ANCHOR", "exact predecessor/post-promotion counts drift")
    _forbidden_population_scan(registry, "#", issues)
    if not synthetic:
        issues.extend(_global_id_collision(registry))
    return sorted(set(issues), key=lambda item: (item.code, item.message))


def validate_all(contract: Any, schema: Any, registry: Any, *, synthetic: bool, allow_unpinned: bool) -> list[Issue]:
    issues = validate_contract(contract) + audit_schema(schema)
    if isinstance(contract, dict):
        issues += validate_dependencies(contract)
    if isinstance(schema, dict):
        issues += validate_registry(registry, schema, synthetic=synthetic)
    else:
        issues.append(Issue("SCHEMA_TYPE", "schema must be an object"))
    pins = [EXPECTED_CONTRACT_DIGEST, EXPECTED_SCHEMA_DIGEST, EXPECTED_SYNTHETIC_DIGEST if synthetic else EXPECTED_REGISTRY_DIGEST]
    actual = [semantic_digest(contract), semantic_digest(schema), semantic_digest(registry)]
    if not allow_unpinned:
        for label, expected, observed in zip(("contract", "schema", "registry"), pins, actual):
            if expected in ("", "TO_BE_FINALIZED", None) or observed != expected:
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
        contract = load_document(CONTRACT_PATH, "C009 contract")
        schema = load_document(SCHEMA_PATH, "C009 schema")
        registry = load_document(Path(args.registry), "C009 registry")
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
    print("C009 canonical leaf promotion validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
