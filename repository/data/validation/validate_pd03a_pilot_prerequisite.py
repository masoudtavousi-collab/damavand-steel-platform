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


def validate_schema(schema: dict[str, Any]) -> Draft202012Validator:
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ValidationConfigurationError("schema must use Draft 2020-12")
    for node in walk(schema):
        if isinstance(node, dict):
            ref = node.get("$ref")
            if isinstance(ref, str) and not ref.startswith("#/"):
                raise ValidationConfigurationError(f"non-local schema reference: {ref}")
            if node.get("type") == "object" and node.get("additionalProperties") is not False:
                raise ValidationConfigurationError("every object schema must be closed")
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
        lifecycle.get("decision_id") != "FD-PD03A-001"
        or lifecycle.get("allowed_transition_sequence") != ["DRAFT", "REVIEW", "APPROVED"]
        or lifecycle.get("direct_draft_to_approved_forbidden") is not True
        or status not in history
        or lifecycle.get("transition_history") != history[status]
    ):
        raise ValidationConfigurationError("PD-03A lifecycle is invalid")
    return str(status)


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
    if bundle.get("status") != expected_status:
        add("LIFECYCLE_STATUS", "extension status differs from lifecycle")

    expected_entities = {
        "SERIES": ("prd:series:e1657d35ac35", "prd:family:a10c6d8ceabc", "لوله استیل دکوراتیو"),
        "VARIANT_RULE_SET": ("prd:variant-rule-set:eb255662accc", "prd:series:e1657d35ac35", "PD-03 Pipe Pilot Variant Rules"),
    }
    entities = bundle.get("entities", [])
    by_type = {item.get("entity_type"): item for item in entities if isinstance(item, dict)}
    if set(by_type) != set(expected_entities):
        add("ENTITY_TYPES", "exact SERIES and VARIANT_RULE_SET records are required")
    for entity_type, (entity_id, parent_id, label) in expected_entities.items():
        item = by_type.get(entity_type, {})
        if (item.get("entity_id"), item.get("parent_entity_id"), item.get("canonical_label")) != (entity_id, parent_id, label):
            add("ENTITY_IDENTITY", f"{entity_type} identity, parent, or label differs")
        if item.get("status") != expected_status:
            add("ENTITY_STATUS", f"{entity_type} status differs")

    expected_attributes = {
        "finish": ("attr:1926e2ad4629", "CONTROLLED_TERM", "FORBIDDEN", [], None, "vreg:3d37a24e09ea"),
        "diameter": ("attr:252ab175be12", "DECIMAL", "REQUIRED", ["unit:000000000002"], 0, None),
        "thickness": ("attr:d1890e85f84c", "DECIMAL", "REQUIRED", ["unit:000000000002"], 2, None),
        "length": ("attr:d782d47eae7f", "DECIMAL", "REQUIRED", ["unit:000000000001"], 0, None),
    }
    attributes = bundle.get("attributes", [])
    by_key = {item.get("attribute_key"): item for item in attributes if isinstance(item, dict)}
    if set(by_key) != set(expected_attributes):
        add("ATTRIBUTE_KEYS", "exact finish, diameter, thickness, and length Attributes are required")
    for key, expected in expected_attributes.items():
        item = by_key.get(key, {})
        constraints = item.get("validation", {}).get("constraints", {})
        actual = (
            item.get("attribute_id"), item.get("data_type"),
            item.get("unit_policy", {}).get("mode"), item.get("unit_policy", {}).get("allowed_unit_ids"),
            constraints.get("decimal_places"), constraints.get("value_registry_reference"),
        )
        if actual != expected:
            add("ATTRIBUTE_POLICY", f"{key} type, Unit, precision, or registry differs")
        if item.get("status") != expected_status:
            add("ATTRIBUTE_STATUS", f"{key} status differs")
    finish_description = str(by_key.get("finish", {}).get("description", "")).casefold()
    if not all(token in finish_description for token in ("appearance", "no coating", "pvd", "quality", "standard")):
        add("FINISH_CLAIM_BOUNDARY", "Finish must state its no-claim appearance boundary")

    registries = bundle.get("value_registries", [])
    registry = registries[0] if isinstance(registries, list) and len(registries) == 1 and isinstance(registries[0], dict) else {}
    terms = registry.get("values", [])
    term = terms[0] if isinstance(terms, list) and len(terms) == 1 and isinstance(terms[0], dict) else {}
    if (
        registry.get("value_registry_id") != "vreg:3d37a24e09ea"
        or registry.get("attribute_id") != "attr:1926e2ad4629"
        or term.get("value_id") != "vterm:1df9a5493546"
        or term.get("value_code") != "silver"
        or term.get("canonical_label") != "Silver"
        or term.get("aliases") != []
    ):
        add("FINISH_REGISTRY", "exact no-alias Silver registry is required")
    for item in (registry, term):
        if item.get("status") != expected_status:
            add("FINISH_STATUS", "Finish registry/term status differs")

    profiles = bundle.get("profiles", [])
    profile = profiles[0] if isinstance(profiles, list) and len(profiles) == 1 and isinstance(profiles[0], dict) else {}
    rules = profile.get("attribute_rules", [])
    rule_by_id = {item.get("attribute_id"): item for item in rules if isinstance(item, dict)}
    expected_rules = {
        "attr:dbf5365ee1e5": (False, "CONTROLLED_REGISTRY", "vreg:302188e2fc8a", [], None),
        "attr:28565665c910": (True, "CONTROLLED_REGISTRY", "vreg:e1b9dd333df8", [], None),
        "attr:1926e2ad4629": (True, "CONTROLLED_REGISTRY", "vreg:3d37a24e09ea", [], None),
        "attr:252ab175be12": (True, "TYPED_VALIDATION", None, ["unit:000000000002"], 0),
        "attr:d1890e85f84c": (True, "TYPED_VALIDATION", None, ["unit:000000000002"], 2),
        "attr:d782d47eae7f": (True, "TYPED_VALIDATION", None, ["unit:000000000001"], 0),
    }
    if profile.get("profile_id") != "pprof:4c556c63c1a9" or profile.get("scope_entity_id") != "prd:series:e1657d35ac35":
        add("PROFILE_IDENTITY", "Series Profile identity or scope differs")
    if set(rule_by_id) != set(expected_rules):
        add("PROFILE_RULES", "exact six Profile rules are required")
    for attribute_id, expected in expected_rules.items():
        rule = rule_by_id.get(attribute_id, {})
        actual = (rule.get("variation_axis"), rule.get("value_source"), rule.get("value_registry_id"), rule.get("allowed_unit_ids"), rule.get("precision"))
        if actual != expected:
            add("PROFILE_AXIS", f"Profile rule differs: {attribute_id}")
        if any((rule.get("requirement_level") != "REQUIRED", rule.get("public_visibility") != "INTERNAL", rule.get("filtering") is not False, rule.get("inquiry_use") != "NOT_USED", rule.get("seo_use") != "PROHIBITED")):
            add("PROFILE_BOUNDARY", f"Profile rule exceeds INTERNAL-only authority: {attribute_id}")
    if profile.get("status") != expected_status:
        add("PROFILE_STATUS", "Series Profile status differs")

    labels = bundle.get("localized_labels", [])
    expected_labels = {
        ("prd:series:e1657d35ac35", "fa-IR"): "لوله استیل دکوراتیو",
        ("attr:1926e2ad4629", "fa-IR"): "رنگ و پوشش",
        ("attr:1926e2ad4629", "en"): "Finish",
        ("attr:252ab175be12", "fa-IR"): "قطر",
        ("attr:252ab175be12", "en"): "Diameter",
        ("attr:d1890e85f84c", "fa-IR"): "ضخامت",
        ("attr:d1890e85f84c", "en"): "Thickness",
        ("attr:d782d47eae7f", "fa-IR"): "طول",
        ("attr:d782d47eae7f", "en"): "Length",
        ("vterm:1df9a5493546", "fa-IR"): "نقره‌ای",
        ("vterm:1df9a5493546", "en"): "Silver",
    }
    actual_labels: dict[tuple[str, str], str] = {}
    label_ids: set[str] = set()
    for item in labels if isinstance(labels, list) else []:
        if not isinstance(item, dict):
            continue
        key = (str(item.get("subject_id")), str(item.get("locale")))
        if key in actual_labels:
            add("DUPLICATE_SUBJECT_LOCALE", f"duplicate label pair: {key}")
        actual_labels[key] = str(item.get("label"))
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
        if item.get("status") != expected_status:
            add("LABEL_STATUS", f"label status differs: {label_id}")
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
        lifecycle = lifecycle_status(contract)
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
