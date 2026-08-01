#!/usr/bin/env python3
"""Validate the immutable PD-03A pilot-prerequisite extension offline."""

from __future__ import annotations

import json
import math
from pathlib import Path
import re
import sys
import unicodedata
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError
import yaml


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repository/data/contracts/pd03a-pilot-prerequisite.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/pd03a-pilot-prerequisite.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml"
BASE_PATHS = (
    ROOT / "repository/data/registries/product-entities.yaml",
    ROOT / "repository/data/registries/product-attributes.yaml",
    ROOT / "repository/data/registries/product-attribute-value-registries.yaml",
    ROOT / "repository/data/registries/product-attribute-profiles.yaml",
    ROOT / "repository/data/registries/product-data-localized-labels.yaml",
    ROOT / "repository/data/registries/product-data-approval-evidence.yaml",
)
MEASUREMENT_CONTRACT = ROOT / "repository/data/contracts/measurement.contract.yaml"
DIMENSIONS_PATH = ROOT / "repository/data/registries/measurement-dimensions.yaml"
UNITS_PATH = ROOT / "repository/data/registries/attribute-units.yaml"
HEX_SUFFIX = re.compile(r":([0-9a-f]{12})$")
FORBIDDEN_KEYS = {
    "product_id", "sku", "commercial_sku", "slug", "stock", "inventory",
    "availability", "availability_value", "supply_status", "price", "pricing",
    "offer", "wordpress_id", "woocommerce_id", "import", "publication",
    "deployment", "production", "golden_package", "master_data",
}
EXPECTED_PROVENANCE = {
    "source_type": "FOUNDER_DECISION",
    "source_reference": "task:019fa05e-1889-79b3-8e83-9477cd1648c6",
    "captured_by": "role:product-data-steward",
    "captured_at": "2026-08-01T00:00:00Z",
    "evidence_status": "FOUNDER_CONFIRMED_NO_CLAIM_SCOPE",
}
EXPECTED_OWNER = {"role": "product-data-steward"}
EXPECTED_REVIEWER = {"role": "repository-guardian"}
EXPECTED_NON_LIFECYCLE_CONTRACT = {
    "contract_id": "pd03a-pilot-prerequisite",
    "contract_version": "1.0.0",
    "record_kind": "canonical-product-data-extension",
    "schema": {
        "path": "repository/data/schemas/pd03a-pilot-prerequisite.schema.json",
        "draft": "https://json-schema.org/draft/2020-12/schema",
    },
    "registry": {
        "path": "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml",
    },
    "baseline": {
        "repository": "masoudtavousi-collab/damavand-steel-platform",
        "main_sha": "dd4d4e9dde59ce652edb5b99d2df3e84b56b8031",
        "immutable_base_decision": "FD-PD02B-001",
    },
    "extension_policy": {
        "immutable_base_registries": True,
        "base_registries": {
            "entities": "repository/data/registries/product-entities.yaml",
            "attributes": "repository/data/registries/product-attributes.yaml",
            "values": "repository/data/registries/product-attribute-value-registries.yaml",
            "profiles": "repository/data/registries/product-attribute-profiles.yaml",
            "labels": "repository/data/registries/product-data-localized-labels.yaml",
        },
        "collision_check_across_base_and_extension": True,
        "labels_slugs_skus_are_not_identity": True,
        "stable_id_allocation": "CSPRNG_12_HEX_WITH_COLLISION_CHECK",
    },
    "exact_extension": {
        "entity_count": 2,
        "entity_types": ["SERIES", "VARIANT_RULE_SET"],
        "attribute_count": 4,
        "attribute_keys": ["finish", "diameter", "thickness", "length"],
        "value_registry_count": 1,
        "value_registry_key": "finish_values",
        "controlled_term_count": 1,
        "controlled_term_code": "silver",
        "profile_count": 1,
        "profile_rule_count": 6,
        "localized_label_count": 11,
        "approval_evidence_count": 1,
    },
    "series_policy": {
        "canonical_label": "لوله استیل دکوراتیو",
        "parent_family_id": "prd:family:a10c6d8ceabc",
        "official_locales": ["fa-IR"],
        "english_official_label_forbidden": True,
    },
    "attribute_policy": {
        "finish": {
            "category": "SECONDARY", "data_type": "CONTROLLED_TERM",
            "canonical_label": "Finish", "persian_label": "رنگ و پوشش",
            "term_code": "silver", "term_label_en": "Silver",
            "term_label_fa": "نقره‌ای", "claim_boundary": "APPEARANCE_DESIGNATION_ONLY",
        },
        "diameter": {
            "category": "PRIMARY", "data_type": "DECIMAL",
            "unit_id": "unit:000000000002", "precision": 0,
        },
        "thickness": {
            "category": "PRIMARY", "data_type": "DECIMAL",
            "unit_id": "unit:000000000002", "precision": 2,
        },
        "length": {
            "category": "PRIMARY", "data_type": "DECIMAL",
            "unit_id": "unit:000000000001", "precision": 0,
        },
    },
    "profile_policy": {
        "scope_entity_type": "SERIES",
        "required_rules": ["material", "grade", "finish", "diameter", "thickness", "length"],
        "variation_axes": ["grade", "finish", "diameter", "thickness", "length"],
        "fixed_non_axis": ["material"],
        "public_visibility": "INTERNAL", "filtering": False,
        "inquiry_use": "NOT_USED", "seo_use": "PROHIBITED",
        "cartesian_generation_forbidden": True,
    },
    "measurement_promotion": {
        "dimension_ids": ["dimension:000000000001"],
        "unit_ids": ["unit:000000000001", "unit:000000000002"],
        "status_by_lifecycle": {
            "DRAFT": "CANDIDATE_UNVERIFIED",
            "REVIEW": "CANDIDATE_UNVERIFIED",
            "APPROVED": "APPROVED",
        },
    },
    "evidence_policy": {
        "founder_decision_required": True,
        "founder_scope_reference": "task:019fa05e-1889-79b3-8e83-9477cd1648c6",
        "no_claim_domain_basis_allowed": True,
        "failed_human_reviews_are_not_pass": True,
        "independent_technical_review_required_before_review": True,
        "technical_review_exact_head_and_base_binding_required": True,
        "technical_review_artifact_digest_required": True,
        "dataset_hashes_required": True,
        "anti_replay_required": True,
        "anti_replay_binding_and_consumption_history_required": True,
    },
    "roles": {
        "decision_authority": "Founder پروژه Damavand Steel",
        "data_steward": "product-data-steward",
        "executor": "codex-build-engine",
        "technical_reviewer": "repository-guardian-independent",
        "ai_domain_authority": False,
    },
    "prohibited": [
        "canonical_pilot_record", "product", "sku", "slug", "actual_availability",
        "supply_promise", "master_data", "golden_package", "wordpress", "woocommerce",
        "import", "runtime", "deploy", "production", "branch_deletion",
        "technical_standard_claim", "tolerance_claim", "quality_claim",
        "application_claim", "cartesian_generation", "grade_430", "pvd", "length_3m",
    ],
}


class ValidationConfigurationError(ValueError):
    """Raised when a contract, schema, or parser boundary is unsafe."""


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that fails on duplicate mapping keys."""


def _construct_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValidationConfigurationError(f"duplicate YAML key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


def load_yaml(path: Path) -> Any:
    try:
        return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    except (OSError, UnicodeError, yaml.YAMLError, ValidationConfigurationError) as exc:
        raise ValidationConfigurationError(f"cannot load {path}: {exc}") from exc


def _json_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValidationConfigurationError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValidationConfigurationError(f"non-finite JSON number is prohibited: {value}")


def load_json(path: Path) -> Any:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_json_pairs,
            parse_constant=_reject_constant,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValidationConfigurationError) as exc:
        raise ValidationConfigurationError(f"cannot load {path}: {exc}") from exc


def require_mapping(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationConfigurationError(f"{name} must be a mapping")
    return value


def walk(value: Any):
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def _audit_schema_node(node: Any, path: str = "<root>") -> None:
    """Reject permissive JSON-Schema branches, including implicit true schemas."""
    if isinstance(node, bool):
        if node:
            raise ValidationConfigurationError(f"permissive true schema: {path}")
        return
    if not isinstance(node, dict) or not node:
        raise ValidationConfigurationError(f"empty or malformed schema node: {path}")
    ref = node.get("$ref")
    if isinstance(ref, str) and not ref.startswith("#/"):
        raise ValidationConfigurationError(f"non-local schema reference: {ref}")
    node_type = node.get("type")
    object_typed = node_type == "object" or (
        isinstance(node_type, list) and "object" in node_type
    )
    if object_typed and node.get("additionalProperties") is not False:
        raise ValidationConfigurationError(f"every object schema must be closed: {path}")
    if "properties" in node and not object_typed:
        raise ValidationConfigurationError(f"properties require an explicit closed object: {path}")
    if node.get("additionalProperties") is True or node.get("unevaluatedProperties") is True:
        raise ValidationConfigurationError(f"permissive object boundary: {path}")

    properties = node.get("properties", {})
    if isinstance(properties, dict):
        for key, child in properties.items():
            _audit_schema_node(child, f"{path}/properties/{key}")
    definitions = node.get("$defs", {})
    if isinstance(definitions, dict):
        for key, child in definitions.items():
            _audit_schema_node(child, f"{path}/$defs/{key}")
    for keyword in ("items", "contains", "propertyNames", "if", "then", "else", "not"):
        if keyword in node:
            _audit_schema_node(node[keyword], f"{path}/{keyword}")
    for keyword in ("prefixItems", "allOf", "anyOf", "oneOf"):
        children = node.get(keyword, [])
        if isinstance(children, list):
            for index, child in enumerate(children):
                _audit_schema_node(child, f"{path}/{keyword}/{index}")
    for keyword in ("patternProperties", "dependentSchemas"):
        children = node.get(keyword, {})
        if isinstance(children, dict):
            for key, child in children.items():
                _audit_schema_node(child, f"{path}/{keyword}/{key}")
    additional = node.get("additionalProperties")
    if isinstance(additional, dict):
        _audit_schema_node(additional, f"{path}/additionalProperties")


def validate_schema(schema: dict[str, Any]) -> Draft202012Validator:
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ValidationConfigurationError("schema must use Draft 2020-12")
    _audit_schema_node(schema)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise ValidationConfigurationError(f"invalid schema: {exc.message}") from exc
    return Draft202012Validator(schema, format_checker=FormatChecker())


def lifecycle_status(contract: dict[str, Any]) -> str:
    lifecycle = require_mapping(contract.get("lifecycle"), "lifecycle")
    history = {
        "DRAFT": [],
        "REVIEW": [{"from": "DRAFT", "to": "REVIEW", "evidence_reference": "PD03A-TECH-REVIEW-001"}],
        "APPROVED": [
            {"from": "DRAFT", "to": "REVIEW", "evidence_reference": "PD03A-TECH-REVIEW-001"},
            {"from": "REVIEW", "to": "APPROVED", "evidence_reference": "FD-PD03A-001"},
        ],
    }
    status = lifecycle.get("current_status")
    if (
        set(lifecycle) != {
            "decision_id", "current_status", "allowed_transition_sequence",
            "transition_history", "direct_draft_to_approved_forbidden",
            "approval_evidence_required", "technical_reviewed_sha",
            "technical_review_artifact_sha256",
        }
        or lifecycle.get("approval_evidence_required") is not True
        or lifecycle.get("decision_id") != "FD-PD03A-001"
        or lifecycle.get("allowed_transition_sequence") != ["DRAFT", "REVIEW", "APPROVED"]
        or lifecycle.get("direct_draft_to_approved_forbidden") is not True
        or status not in history
        or lifecycle.get("transition_history") != history[status]
        or (
            status == "DRAFT"
            and (
                lifecycle.get("technical_reviewed_sha") is not None
                or lifecycle.get("technical_review_artifact_sha256") is not None
            )
        )
        or (
            status in {"REVIEW", "APPROVED"}
            and (
                re.fullmatch(r"[0-9a-f]{40}", str(lifecycle.get("technical_reviewed_sha"))) is None
                or re.fullmatch(r"[0-9a-f]{64}", str(lifecycle.get("technical_review_artifact_sha256"))) is None
            )
        )
    ):
        raise ValidationConfigurationError("PD-03A lifecycle is invalid")
    return str(status)


def validate_contract(contract: dict[str, Any]) -> str:
    expected_keys = set(EXPECTED_NON_LIFECYCLE_CONTRACT) | {"lifecycle"}
    if set(contract) != expected_keys:
        raise ValidationConfigurationError("PD-03A contract keys differ")
    for key, expected in EXPECTED_NON_LIFECYCLE_CONTRACT.items():
        if contract.get(key) != expected:
            raise ValidationConfigurationError(f"PD-03A contract section differs: {key}")
    return lifecycle_status(contract)


def collect_ids(value: Any) -> set[str]:
    ids: set[str] = set()
    id_keys = {
        "entity_id", "attribute_id", "value_registry_id", "value_id", "profile_id",
        "label_id", "approval_evidence_id", "extension_id",
    }
    for node in walk(value):
        if isinstance(node, dict):
            for key in id_keys:
                item = node.get(key)
                if isinstance(item, str) and HEX_SUFFIX.search(item):
                    ids.add(item)
    return ids


def collect_extension_allocations(bundle: dict[str, Any]) -> set[str]:
    allocated: set[str] = set()
    extension_id = bundle.get("extension_id")
    if isinstance(extension_id, str):
        allocated.add(extension_id)
    for section, key in (
        ("entities", "entity_id"),
        ("attributes", "attribute_id"),
        ("profiles", "profile_id"),
        ("localized_labels", "label_id"),
    ):
        for item in bundle.get(section, []):
            if isinstance(item, dict) and isinstance(item.get(key), str):
                allocated.add(item[key])
    for registry in bundle.get("value_registries", []):
        if not isinstance(registry, dict):
            continue
        if isinstance(registry.get("value_registry_id"), str):
            allocated.add(registry["value_registry_id"])
        for term in registry.get("values", []):
            if isinstance(term, dict) and isinstance(term.get("value_id"), str):
                allocated.add(term["value_id"])
    return allocated


def validate_bundle(bundle: Any, contract: dict[str, Any], lifecycle: str) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    if not isinstance(bundle, dict):
        return ["[BUNDLE_TYPE] extension must be a mapping"]
    expected_status = "APPROVED" if lifecycle == "APPROVED" else "CANDIDATE_UNVERIFIED"
    expected_root = {
        "contract_version": "1.0.0",
        "extension_id": "pdext:ad46d9948af1",
        "data_classification": "CANONICAL_PD03A_EXTENSION",
        "baseline_sha": "dd4d4e9dde59ce652edb5b99d2df3e84b56b8031",
        "status": expected_status,
    }
    for key, expected in expected_root.items():
        if bundle.get(key) != expected:
            add("BUNDLE_IDENTITY", f"exact root field differs: {key}")
    if bundle.get("status") != expected_status:
        add("LIFECYCLE_STATUS", "extension status differs from lifecycle")

    expected_entities = {
        "SERIES": {
            "contract_version": "1.0.0", "entity_id": "prd:series:e1657d35ac35",
            "entity_type": "SERIES", "parent_entity_id": "prd:family:a10c6d8ceabc",
            "parent_entity_type": "FAMILY", "canonical_label": "لوله استیل دکوراتیو",
            "status": expected_status, "owner": EXPECTED_OWNER,
            "provenance": EXPECTED_PROVENANCE, "record_version": "1.0.0",
        },
        "VARIANT_RULE_SET": {
            "contract_version": "1.0.0", "entity_id": "prd:variant-rule-set:eb255662accc",
            "entity_type": "VARIANT_RULE_SET", "parent_entity_id": "prd:series:e1657d35ac35",
            "parent_entity_type": "SERIES", "canonical_label": "PD-03 Pipe Pilot Variant Rules",
            "status": expected_status, "owner": EXPECTED_OWNER,
            "provenance": EXPECTED_PROVENANCE, "record_version": "1.0.0",
        },
    }
    entities = bundle.get("entities", [])
    by_type = {item.get("entity_type"): item for item in entities if isinstance(item, dict)}
    if set(by_type) != set(expected_entities):
        add("ENTITY_TYPES", "exact SERIES and VARIANT_RULE_SET records are required")
    for entity_type, expected in expected_entities.items():
        item = by_type.get(entity_type, {})
        if item != expected:
            add("ENTITY_EXACT_RECORD", f"{entity_type} exact identity, relationship, role, provenance, or status differs")

    expected_attributes = {
        "finish": {
            "contract_version": "2.0.0", "attribute_id": "attr:1926e2ad4629",
            "attribute_key": "finish", "canonical_label": "Finish",
            "description": "Internal appearance designation for the bounded pilot prerequisite; it asserts no coating, PVD, material, quality, or standard.",
            "category": "SECONDARY", "data_type": "CONTROLLED_TERM",
            "unit_policy": {"mode": "FORBIDDEN", "allowed_unit_ids": []},
            "validation": {"nullable": False, "multiple_values": False, "constraints": {"value_registry_reference": "vreg:3d37a24e09ea"}},
            "status": expected_status, "owner": EXPECTED_OWNER,
            "provenance": EXPECTED_PROVENANCE, "record_version": "1.0.0",
        },
        "diameter": {
            "contract_version": "2.0.0", "attribute_id": "attr:252ab175be12",
            "attribute_key": "diameter", "canonical_label": "Diameter",
            "description": "Internal decimal diameter value with an explicit millimetre reference; no tolerance or standard is asserted.",
            "category": "PRIMARY", "data_type": "DECIMAL",
            "unit_policy": {"mode": "REQUIRED", "allowed_unit_ids": ["unit:000000000002"]},
            "validation": {"nullable": False, "multiple_values": False, "constraints": {"decimal_places": 0, "minimum": 0}},
            "status": expected_status, "owner": EXPECTED_OWNER,
            "provenance": EXPECTED_PROVENANCE, "record_version": "1.0.0",
        },
        "thickness": {
            "contract_version": "2.0.0", "attribute_id": "attr:d1890e85f84c",
            "attribute_key": "thickness", "canonical_label": "Thickness",
            "description": "Internal decimal thickness value with an explicit millimetre reference; no tolerance or standard is asserted.",
            "category": "PRIMARY", "data_type": "DECIMAL",
            "unit_policy": {"mode": "REQUIRED", "allowed_unit_ids": ["unit:000000000002"]},
            "validation": {"nullable": False, "multiple_values": False, "constraints": {"decimal_places": 2, "minimum": 0}},
            "status": expected_status, "owner": EXPECTED_OWNER,
            "provenance": EXPECTED_PROVENANCE, "record_version": "1.0.0",
        },
        "length": {
            "contract_version": "2.0.0", "attribute_id": "attr:d782d47eae7f",
            "attribute_key": "length", "canonical_label": "Length",
            "description": "Internal decimal length value with an explicit metre reference; no supply-length or availability claim is asserted.",
            "category": "PRIMARY", "data_type": "DECIMAL",
            "unit_policy": {"mode": "REQUIRED", "allowed_unit_ids": ["unit:000000000001"]},
            "validation": {"nullable": False, "multiple_values": False, "constraints": {"decimal_places": 0, "minimum": 0}},
            "status": expected_status, "owner": EXPECTED_OWNER,
            "provenance": EXPECTED_PROVENANCE, "record_version": "1.0.0",
        },
    }
    attributes = bundle.get("attributes", [])
    by_key = {item.get("attribute_key"): item for item in attributes if isinstance(item, dict)}
    if set(by_key) != set(expected_attributes):
        add("ATTRIBUTE_KEYS", "exact finish, diameter, thickness, and length Attributes are required")
    for key, expected in expected_attributes.items():
        item = by_key.get(key, {})
        if item != expected:
            add("ATTRIBUTE_EXACT_RECORD", f"{key} exact semantics, role, provenance, or status differs")
    finish_description = str(by_key.get("finish", {}).get("description", "")).casefold()
    if not all(token in finish_description for token in ("appearance", "no coating", "pvd", "quality", "standard")):
        add("FINISH_CLAIM_BOUNDARY", "Finish must state its no-claim appearance boundary")

    registries = bundle.get("value_registries", [])
    registry = registries[0] if isinstance(registries, list) and len(registries) == 1 and isinstance(registries[0], dict) else {}
    terms = registry.get("values", [])
    term = terms[0] if isinstance(terms, list) and len(terms) == 1 and isinstance(terms[0], dict) else {}
    expected_term = {
        "value_id": "vterm:1df9a5493546", "value_code": "silver",
        "canonical_label": "Silver", "aliases": [], "status": expected_status,
        "provenance": EXPECTED_PROVENANCE, "record_version": "1.0.0",
    }
    expected_registry = {
        "contract_version": "1.0.0", "value_registry_id": "vreg:3d37a24e09ea",
        "registry_key": "finish_values", "attribute_id": "attr:1926e2ad4629",
        "canonical_label": "Finish Values", "values": [expected_term],
        "status": expected_status, "owner": EXPECTED_OWNER, "reviewer": EXPECTED_REVIEWER,
        "provenance": EXPECTED_PROVENANCE, "record_version": "1.0.0",
    }
    if term != expected_term or registry != expected_registry:
        add("FINISH_EXACT_RECORD", "exact no-alias Silver registry, role, provenance, and relationship are required")

    profiles = bundle.get("profiles", [])
    profile = profiles[0] if isinstance(profiles, list) and len(profiles) == 1 and isinstance(profiles[0], dict) else {}
    rules = profile.get("attribute_rules", [])
    rule_by_id = {item.get("attribute_id"): item for item in rules if isinstance(item, dict)}
    def profile_rule(
        attribute_id: str, variation_axis: bool, value_source: str,
        value_registry_id: str | None, allowed_unit_ids: list[str], precision: int | None,
    ) -> dict[str, Any]:
        return {
            "attribute_id": attribute_id, "requirement_level": "REQUIRED",
            "condition_reference": None, "public_visibility": "INTERNAL",
            "variation_axis": variation_axis, "filtering": False,
            "inquiry_use": "NOT_USED", "seo_use": "PROHIBITED",
            "value_source": value_source, "value_registry_id": value_registry_id,
            "allowed_unit_ids": allowed_unit_ids, "precision": precision,
        }

    expected_rules = {
        "attr:dbf5365ee1e5": profile_rule("attr:dbf5365ee1e5", False, "CONTROLLED_REGISTRY", "vreg:302188e2fc8a", [], None),
        "attr:28565665c910": profile_rule("attr:28565665c910", True, "CONTROLLED_REGISTRY", "vreg:e1b9dd333df8", [], None),
        "attr:1926e2ad4629": profile_rule("attr:1926e2ad4629", True, "CONTROLLED_REGISTRY", "vreg:3d37a24e09ea", [], None),
        "attr:252ab175be12": profile_rule("attr:252ab175be12", True, "TYPED_VALIDATION", None, ["unit:000000000002"], 0),
        "attr:d1890e85f84c": profile_rule("attr:d1890e85f84c", True, "TYPED_VALIDATION", None, ["unit:000000000002"], 2),
        "attr:d782d47eae7f": profile_rule("attr:d782d47eae7f", True, "TYPED_VALIDATION", None, ["unit:000000000001"], 0),
    }
    if profile.get("profile_id") != "pprof:4c556c63c1a9" or profile.get("scope_entity_id") != "prd:series:e1657d35ac35":
        add("PROFILE_IDENTITY", "Series Profile identity or scope differs")
    if set(rule_by_id) != set(expected_rules):
        add("PROFILE_RULES", "exact six Profile rules are required")
    for attribute_id, expected in expected_rules.items():
        rule = rule_by_id.get(attribute_id, {})
        if rule != expected:
            add("PROFILE_EXACT_RULE", f"Profile rule differs: {attribute_id}")
    expected_profile = {
        "contract_version": "1.0.0", "profile_id": "pprof:4c556c63c1a9",
        "scope_entity_id": "prd:series:e1657d35ac35", "scope_entity_type": "SERIES",
        "attribute_rules": [expected_rules[key] for key in expected_rules],
        "status": expected_status, "owner": EXPECTED_OWNER, "reviewer": EXPECTED_REVIEWER,
        "provenance": EXPECTED_PROVENANCE, "record_version": "1.0.0",
    }
    if profile != expected_profile:
        add("PROFILE_EXACT_RECORD", "Series Profile metadata, rules, roles, provenance, or status differ")

    labels = bundle.get("localized_labels", [])
    expected_labels = {
        ("prd:series:e1657d35ac35", "fa-IR"): ("plabel:b95d5211b63b", "PRODUCT_ENTITY", "لوله استیل دکوراتیو"),
        ("attr:1926e2ad4629", "fa-IR"): ("plabel:5024b061b393", "PRODUCT_ATTRIBUTE", "رنگ و پوشش"),
        ("attr:1926e2ad4629", "en"): ("plabel:8a9b60f9e03c", "PRODUCT_ATTRIBUTE", "Finish"),
        ("attr:252ab175be12", "fa-IR"): ("plabel:c762e6ae0573", "PRODUCT_ATTRIBUTE", "قطر"),
        ("attr:252ab175be12", "en"): ("plabel:6315b25f82f6", "PRODUCT_ATTRIBUTE", "Diameter"),
        ("attr:d1890e85f84c", "fa-IR"): ("plabel:0dc557363e77", "PRODUCT_ATTRIBUTE", "ضخامت"),
        ("attr:d1890e85f84c", "en"): ("plabel:b4ed88686bc7", "PRODUCT_ATTRIBUTE", "Thickness"),
        ("attr:d782d47eae7f", "fa-IR"): ("plabel:888caa01bfcc", "PRODUCT_ATTRIBUTE", "طول"),
        ("attr:d782d47eae7f", "en"): ("plabel:cb0e64f1f322", "PRODUCT_ATTRIBUTE", "Length"),
        ("vterm:1df9a5493546", "fa-IR"): ("plabel:53ad45e25cc5", "CONTROLLED_TERM", "نقره‌ای"),
        ("vterm:1df9a5493546", "en"): ("plabel:685397bd1e7b", "CONTROLLED_TERM", "Silver"),
    }
    actual_labels: dict[tuple[str, str], tuple[str, str, str]] = {}
    label_ids: set[str] = set()
    for item in labels if isinstance(labels, list) else []:
        if not isinstance(item, dict):
            continue
        key = (str(item.get("subject_id")), str(item.get("locale")))
        if key in actual_labels:
            add("DUPLICATE_SUBJECT_LOCALE", f"duplicate label pair: {key}")
        actual_labels[key] = (
            str(item.get("label_id")), str(item.get("subject_kind")), str(item.get("label")),
        )
        label_id = item.get("label_id")
        if label_id in label_ids:
            add("DUPLICATE_LABEL_ID", f"duplicate label id: {label_id}")
        if isinstance(label_id, str):
            label_ids.add(label_id)
        label = item.get("label")
        if isinstance(label, str):
            if unicodedata.normalize("NFC", label) != label:
                add("UNICODE_NOT_NFC", f"label is not NFC: {label_id}")
            if item.get("locale") == "en" and not label.isascii():
                add("UNICODE_CONFUSABLE_LABEL", f"English label is not ASCII: {label_id}")
        expected = expected_labels.get(key)
        expected_record = {
            "contract_version": "1.0.0", "label_id": expected[0] if expected else None,
            "subject_id": key[0], "subject_kind": expected[1] if expected else None,
            "locale": key[1], "label": expected[2] if expected else None,
            "aliases": [], "status": expected_status, "provenance": EXPECTED_PROVENANCE,
            "record_version": "1.0.0",
        }
        if item != expected_record:
            add("LABEL_EXACT_RECORD", f"label identity, kind, aliases, role, provenance, or status differs: {label_id}")
    if actual_labels != expected_labels:
        add("EXACT_LOCALIZED_LABELS", "exact 11 labels differ; Series English label is forbidden")

    for node in walk(bundle):
        if isinstance(node, dict):
            overlap = FORBIDDEN_KEYS.intersection(node)
            if overlap:
                add("PROHIBITED_FIELD", f"prohibited field(s): {sorted(overlap)}")
        if isinstance(node, float) and not math.isfinite(node):
            add("NON_FINITE_NUMBER", "NaN or Infinity is prohibited")

    extension_ids = collect_extension_allocations(bundle)
    suffixes = [HEX_SUFFIX.search(item).group(1) for item in extension_ids if HEX_SUFFIX.search(item)]
    if len(suffixes) != len(set(suffixes)):
        add("EXTENSION_ID_COLLISION", "12-hex suffixes collide inside the extension")
    base_ids: set[str] = set()
    for path in BASE_PATHS:
        base_ids.update(collect_ids(load_yaml(path)))
    if extension_ids.intersection(base_ids):
        add("BASE_EXTENSION_ID_COLLISION", f"extension IDs collide with immutable base: {sorted(extension_ids.intersection(base_ids))}")

    measurement_contract = require_mapping(load_yaml(MEASUREMENT_CONTRACT), "measurement contract")
    measurement_extension = require_mapping(measurement_contract.get("pd03a_extension"), "measurement pd03a_extension")
    if measurement_extension.get("current_status") != lifecycle:
        add("MEASUREMENT_LIFECYCLE", "measurement lifecycle differs from PD-03A")
    dimensions = require_mapping(load_yaml(DIMENSIONS_PATH), "dimensions").get("dimensions", [])
    units = require_mapping(load_yaml(UNITS_PATH), "units").get("units", [])
    dimension_by_id = {item.get("dimension_id"): item for item in dimensions if isinstance(item, dict)}
    unit_by_id = {item.get("unit_id"): item for item in units if isinstance(item, dict)}
    if dimension_by_id.get("dimension:000000000001", {}).get("status") != expected_status:
        add("DIMENSION_STATUS", "Length dimension status differs")
    for unit_id in ("unit:000000000001", "unit:000000000002"):
        if unit_by_id.get(unit_id, {}).get("status") != expected_status:
            add("UNIT_STATUS", f"Unit status differs: {unit_id}")
    if unit_by_id.get("unit:000000000001", {}).get("symbol") != "m" or unit_by_id.get("unit:000000000002", {}).get("symbol") != "mm":
        add("UNIT_IDENTITY", "metre/millimetre identity differs")

    return sorted(set(issues))


def main() -> int:
    try:
        contract = require_mapping(load_yaml(CONTRACT_PATH), "PD-03A contract")
        lifecycle = validate_contract(contract)
        schema = require_mapping(load_json(SCHEMA_PATH), "PD-03A schema")
        validator = validate_schema(schema)
        bundle = load_yaml(REGISTRY_PATH)
        issues = [
            f"[SCHEMA_VALIDATION] {'/'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
            for error in validator.iter_errors(bundle)
        ]
        issues.extend(validate_bundle(bundle, contract, lifecycle))
    except (ValidationConfigurationError, OSError, TypeError, ValueError) as exc:
        print(f"PD03A_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        for issue in sorted(set(issues)):
            print(issue, file=sys.stderr)
        return 1
    print(
        "PD-03A prerequisite validation PASS: immutable PD-02B base; "
        "2 entities, 4 attributes, 1 registry/term, 1 six-rule INTERNAL profile, "
        f"11 labels; lifecycle={lifecycle}; network, runtime, side effects=false."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
