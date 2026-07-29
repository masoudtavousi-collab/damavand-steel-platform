#!/usr/bin/env python3
"""Fail-closed offline validation for PD-01 synthetic Product Master Data."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, InvalidOperation
import json
import math
from pathlib import Path
import re
import sys
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

from validate_product_attributes import (
    DefinitionError as AttributeDefinitionError,
    load_definitions as load_attribute_definitions,
    validate_fixture as validate_attribute_fixture,
)
from validate_product_core import (
    DefinitionError as ProductDefinitionError,
    load_definitions as load_product_definitions,
    validate_dataset as validate_product_dataset,
)


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repository/data/contracts/product-master-data.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/product-master-data.schema.json"
DEFAULT_ENTITIES = ROOT / "tests/fixtures/product-core/valid-minimal.yaml"
DEFAULT_ATTRIBUTES = (
    ROOT / "tests/fixtures/product-attributes/valid-measured-attribute.yaml"
)
DEFAULT_BUNDLE = (
    ROOT / "tests/fixtures/product-master-data/valid-synthetic-minimal.yaml"
)
MAX_INPUT_BYTES = 2_000_000
MAX_NESTING_DEPTH = 64
MAX_STRUCTURE_NODES = 20_000
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
PROHIBITED_FIELDS = {
    "sku",
    "commercial_sku",
    "slug",
    "canonical_slug",
    "availability",
    "supply_status",
    "stock",
    "inventory",
    "price",
    "pricing",
    "cost",
    "margin",
    "offer",
    "cart",
    "checkout",
    "payment",
    "wordpress_id",
    "woocommerce_id",
    "parent_product_id",
    "variation_id",
    "import",
    "publication",
    "deployment",
    "production",
}


class ConfigurationError(ValueError):
    """Raised when a contract, schema, or approved input boundary is invalid."""


class DuplicateKeyError(ValueError):
    """Raised when strict JSON or YAML loading finds a duplicate object key."""


@dataclass(frozen=True)
class Issue:
    source: str
    entity: str
    code: str
    message: str

    def render(self) -> str:
        return f"{self.source}: entity {self.entity}: [{self.code}] {self.message}"


@dataclass(frozen=True)
class Definitions:
    contract: dict[str, Any]
    schema_validator: Any
    prohibited_fields: set[str]


def safe_path(path: Path, label: str) -> Path:
    try:
        if path.is_symlink():
            raise ConfigurationError(f"{label} must not be a symbolic link")
        resolved = path.resolve(strict=True)
    except FileNotFoundError as exc:
        raise ConfigurationError(f"missing {label}: {path}") from exc
    if resolved != ROOT and ROOT not in resolved.parents:
        raise ConfigurationError(f"{label} must remain inside the repository")
    return resolved


def read_text(path: Path, label: str) -> str:
    resolved = safe_path(path, label)
    if resolved.stat().st_size > MAX_INPUT_BYTES:
        raise ConfigurationError(f"{label} exceeds the {MAX_INPUT_BYTES}-byte limit")
    try:
        return resolved.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ConfigurationError(f"{label} must be valid UTF-8") from exc


def ensure_bounded_structure(value: Any, label: str) -> Any:
    stack: list[tuple[Any, int]] = [(value, 0)]
    nodes = 0
    while stack:
        item, depth = stack.pop()
        nodes += 1
        if nodes > MAX_STRUCTURE_NODES:
            raise ConfigurationError(
                f"{label}: structure exceeds the {MAX_STRUCTURE_NODES}-node limit"
            )
        if depth > MAX_NESTING_DEPTH:
            raise ConfigurationError(
                f"{label}: nesting exceeds the {MAX_NESTING_DEPTH}-level limit"
            )
        if isinstance(item, dict):
            stack.extend((child, depth + 1) for child in item.values())
        elif isinstance(item, list):
            stack.extend((child, depth + 1) for child in item)
    return value


def strict_json(raw: str, label: str) -> Any:
    def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise DuplicateKeyError(f"{label}: duplicate JSON key {key!r}")
            result[key] = value
        return result

    def reject_constant(value: str) -> None:
        raise ConfigurationError(f"{label}: non-finite JSON number {value} is forbidden")

    try:
        return ensure_bounded_structure(
            json.loads(
                raw,
                object_pairs_hook=strict_object,
                parse_constant=reject_constant,
            ),
            label,
        )
    except DuplicateKeyError:
        raise
    except json.JSONDecodeError as exc:
        raise ConfigurationError(
            f"{label}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    except RecursionError as exc:
        raise ConfigurationError(f"{label}: JSON nesting is unsafe") from exc


def strict_yaml(raw: str, label: str) -> tuple[Any, str]:
    try:
        import yaml  # type: ignore[import-not-found]
    except ModuleNotFoundError as exc:
        raise ConfigurationError("strict YAML validation requires approved PyYAML") from exc

    class UniqueKeyLoader(yaml.SafeLoader):  # type: ignore[attr-defined]
        pass

    def construct_mapping(loader: Any, node: Any, deep: bool = False) -> dict[Any, Any]:
        mapping: dict[Any, Any] = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            try:
                if key in mapping:
                    raise DuplicateKeyError(f"{label}: duplicate YAML key {key!r}")
            except TypeError as exc:
                raise ConfigurationError(f"{label}: unhashable YAML key {key!r}") from exc
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    UniqueKeyLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,  # type: ignore[attr-defined]
        construct_mapping,
    )
    try:
        return (
            ensure_bounded_structure(
                yaml.load(raw, Loader=UniqueKeyLoader),
                label,
            ),
            f"PyYAML {yaml.__version__} strict",
        )
    except DuplicateKeyError:
        raise
    except yaml.YAMLError as exc:  # type: ignore[attr-defined]
        raise ConfigurationError(f"{label}: invalid YAML: {exc}") from exc
    except RecursionError as exc:
        raise ConfigurationError(f"{label}: YAML nesting is unsafe") from exc


def load_yaml(path: Path, label: str) -> tuple[Any, str]:
    return strict_yaml(read_text(path, label), label)


def load_json(path: Path, label: str) -> Any:
    return strict_json(read_text(path, label), label)


def require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ConfigurationError(f"{label} must be a mapping")
    return value


def reject_nonlocal_refs(value: Any, path: str = "#") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            child = f"{path}/{key}"
            if key == "$ref" and (
                not isinstance(item, str) or not item.startswith("#/")
            ):
                raise ConfigurationError(
                    f"non-local schema reference is forbidden: {child}"
                )
            reject_nonlocal_refs(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            reject_nonlocal_refs(item, f"{path}/{index}")


def validate_lifecycle(contract: dict[str, Any]) -> None:
    lifecycle = require_mapping(contract.get("pd01_lifecycle"), "pd01_lifecycle")
    if lifecycle.get("decision_id") != "FD-PD01-001":
        raise ConfigurationError("PD-01 decision_id must be FD-PD01-001")
    if lifecycle.get("allowed_transition_sequence") != [
        "DRAFT",
        "REVIEW",
        "APPROVED",
    ]:
        raise ConfigurationError("PD-01 lifecycle must be DRAFT -> REVIEW -> APPROVED")
    expected = {
        "DRAFT": [],
        "REVIEW": [
            {
                "from": "DRAFT",
                "to": "REVIEW",
                "evidence_reference": "PD01-REVIEW-001",
            }
        ],
        "APPROVED": [
            {
                "from": "DRAFT",
                "to": "REVIEW",
                "evidence_reference": "PD01-REVIEW-001",
            },
            {
                "from": "REVIEW",
                "to": "APPROVED",
                "evidence_reference": "FD-PD01-001",
            },
        ],
    }
    status = lifecycle.get("current_status")
    if status not in expected or lifecycle.get("transition_history") != expected[status]:
        raise ConfigurationError("PD-01 lifecycle history is invalid or skips REVIEW")
    if lifecycle.get("direct_draft_to_approved_forbidden") is not True:
        raise ConfigurationError("direct DRAFT -> APPROVED must remain forbidden")


def load_definitions(contract_path: Path, schema_path: Path) -> Definitions:
    contract_value, _ = load_yaml(contract_path, "Product Master Data contract")
    contract = require_mapping(contract_value, "Product Master Data contract")
    if contract.get("contract_id") != "product-master-data":
        raise ConfigurationError("contract_id must be product-master-data")
    if contract.get("contract_version") != "1.0.0":
        raise ConfigurationError("Product Master Data contract_version must be 1.0.0")
    validate_lifecycle(contract)
    boundary = require_mapping(contract.get("data_boundary"), "data_boundary")
    expected_boundary = {
        "validation_mode": "SYNTHETIC_ONLY",
        "canonical_population_authority": False,
        "product_creation_authority": False,
        "sku_authority": False,
        "golden_package_authority": False,
        "import_ready": False,
        "runtime_ready": False,
        "network_allowed": False,
    }
    if boundary != expected_boundary:
        raise ConfigurationError("PD-01 data boundary differs from the approved boundary")
    contract_prohibited = contract.get("prohibited_fields")
    if not isinstance(contract_prohibited, list) or set(contract_prohibited) != PROHIBITED_FIELDS:
        raise ConfigurationError("PD-01 prohibited fields differ from the approved set")

    schema = require_mapping(
        load_json(schema_path, "Product Master Data JSON Schema"),
        "Product Master Data JSON Schema",
    )
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ConfigurationError("Product Master Data schema must declare Draft 2020-12")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise ConfigurationError("Product Master Data schema root must be closed")
    reject_nonlocal_refs(schema)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise ConfigurationError(f"invalid Product Master Data schema: {exc.message}") from exc
    return Definitions(
        contract=contract,
        schema_validator=Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ),
        prohibited_fields=set(contract_prohibited),
    )


def iter_keys(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(key, str):
                yield key
            yield from iter_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_keys(item)


def list_items(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def decimals(value: Any) -> int | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    if isinstance(value, float) and not math.isfinite(value):
        return None
    try:
        decimal_value = Decimal(str(value))
    except InvalidOperation:
        return None
    return max(0, -decimal_value.as_tuple().exponent)


def valid_utc_timestamp(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return False
    return True


def validate_bundle(
    bundle: Any,
    source: str,
    definitions: Definitions,
    entities_value: Any,
    attributes_value: Any,
) -> list[Issue]:
    issues: list[Issue] = []

    def add(entity: str, code: str, message: str) -> None:
        issues.append(Issue(source, entity, code, message))

    if not isinstance(bundle, dict):
        add("<bundle>", "BUNDLE_TYPE", "bundle must be a mapping")
        return issues

    for error in sorted(
        definitions.schema_validator.iter_errors(bundle),
        key=lambda item: (
            tuple(str(part) for part in item.absolute_path),
            item.message,
        ),
    ):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add("<bundle>", "SCHEMA_VALIDATION", f"{location}: {error.message}")

    for field in sorted(set(iter_keys(bundle)) & definitions.prohibited_fields):
        add("<bundle>", "PROHIBITED_FIELD", f"prohibited Product/runtime field: {field}")
    provenances = [bundle.get("provenance")]
    provenances.extend(
        assignment.get("provenance")
        for assignment in list_items(bundle.get("value_assignments"))
        if isinstance(assignment, dict)
    )
    for index, provenance in enumerate(provenances):
        if isinstance(provenance, dict) and not valid_utc_timestamp(
            provenance.get("captured_at")
        ):
            add(
                f"<provenance:{index}>",
                "TIMESTAMP_INVALID",
                "captured_at must be a real UTC timestamp in YYYY-MM-DDTHH:MM:SSZ",
            )

    entity_definitions = load_product_definitions()
    product_issues = validate_product_dataset(
        entities_value,
        "<synthetic-product-core>",
        entity_definitions,
    )
    for issue in product_issues:
        add(issue.entity, f"PRODUCT_CORE_{issue.code}", issue.message)
    attribute_definitions = load_attribute_definitions()
    attribute_issues = validate_attribute_fixture(
        attributes_value,
        "<synthetic-product-attributes>",
        attribute_definitions,
    )
    for issue in attribute_issues:
        add(issue.attribute, f"PRODUCT_ATTRIBUTE_{issue.code}", issue.message)
    if product_issues or attribute_issues:
        return sorted(issues, key=lambda item: (item.entity, item.code, item.message))

    entities = {
        item["entity_id"]: item
        for item in entities_value
        if isinstance(item, dict) and isinstance(item.get("entity_id"), str)
    }
    attributes = {
        item["attribute_id"]: item
        for item in attributes_value
        if isinstance(item, dict) and isinstance(item.get("attribute_id"), str)
    }

    profiles: dict[str, dict[str, Any]] = {}
    for index, profile in enumerate(
        list_items(bundle.get("attribute_profiles")),
        start=1,
    ):
        if not isinstance(profile, dict):
            continue
        profile_id = profile.get("profile_id")
        label = str(profile_id or f"<profile:{index}>")
        if profile_id in profiles:
            add(label, "DUPLICATE_PROFILE_ID", f"duplicate profile_id: {profile_id}")
        elif isinstance(profile_id, str):
            profiles[profile_id] = profile
        scope_id = profile.get("scope_entity_id")
        scope = entities.get(scope_id)
        if scope is None:
            add(label, "UNKNOWN_SCOPE_ENTITY", f"unknown scope entity: {scope_id}")
        elif scope.get("entity_type") != profile.get("scope_entity_type"):
            add(label, "SCOPE_ENTITY_TYPE", "scope entity type does not match Product Core")
        seen_rules: set[str] = set()
        for rule in list_items(profile.get("attribute_rules")):
            if not isinstance(rule, dict):
                continue
            attribute_id = rule.get("attribute_id")
            if attribute_id in seen_rules:
                add(label, "DUPLICATE_PROFILE_ATTRIBUTE", f"duplicate rule: {attribute_id}")
            elif isinstance(attribute_id, str):
                seen_rules.add(attribute_id)
            if attribute_id not in attributes:
                add(label, "UNKNOWN_ATTRIBUTE", f"unknown profile attribute: {attribute_id}")
            conditional = rule.get("requirement_level") == "CONDITIONAL"
            condition = rule.get("condition_reference")
            if conditional != isinstance(condition, str):
                add(
                    label,
                    "CONDITION_REFERENCE",
                    "only CONDITIONAL rules require condition_reference",
                )
            if rule.get("requirement_level") == "PROHIBITED" and (
                rule.get("variation_axis") is True or rule.get("filtering") is True
            ):
                add(label, "PROHIBITED_RULE_USE", "PROHIBITED rule cannot vary or filter")

    assignments: dict[str, dict[str, Any]] = {}
    for index, assignment in enumerate(
        list_items(bundle.get("value_assignments")),
        start=1,
    ):
        if not isinstance(assignment, dict):
            continue
        assignment_id = assignment.get("assignment_id")
        label = str(assignment_id or f"<assignment:{index}>")
        if assignment_id in assignments:
            add(label, "DUPLICATE_ASSIGNMENT_ID", f"duplicate assignment_id: {assignment_id}")
        elif isinstance(assignment_id, str):
            assignments[assignment_id] = assignment
        entity_id = assignment.get("entity_id")
        if entity_id not in entities:
            add(label, "UNKNOWN_ENTITY", f"unknown assignment entity: {entity_id}")
        attribute_id = assignment.get("attribute_id")
        attribute = attributes.get(attribute_id)
        if attribute is None:
            add(label, "UNKNOWN_ATTRIBUTE", f"unknown assignment attribute: {attribute_id}")
            continue
        value = assignment.get("value")
        if not isinstance(value, dict) or len(value) != 1:
            add(label, "VALUE_SHAPE", "value must contain exactly one typed field")
            continue
        value_key, scalar = next(iter(value.items()))
        expected_key = {
            "TEXT": "text",
            "INTEGER": "integer",
            "DECIMAL": "decimal",
            "BOOLEAN": "boolean",
            "CONTROLLED_TERM": "term_id",
            "ENTITY_REFERENCE": "entity_reference",
        }.get(attribute.get("data_type"))
        if value_key != expected_key:
            add(
                label,
                "VALUE_TYPE",
                f"{attribute.get('data_type')} requires value.{expected_key}",
            )
        if isinstance(scalar, float) and not math.isfinite(scalar):
            add(label, "NON_FINITE_NUMBER", "NaN and Infinity are forbidden")
        constraints = attribute.get("validation", {}).get("constraints", {})
        if expected_key in {"integer", "decimal"} and isinstance(scalar, (int, float)) and not isinstance(scalar, bool):
            if "minimum" in constraints and scalar < constraints["minimum"]:
                add(label, "VALUE_MINIMUM", "numeric value is below the approved minimum")
            if "maximum" in constraints and scalar > constraints["maximum"]:
                add(label, "VALUE_MAXIMUM", "numeric value exceeds the approved maximum")
            if expected_key == "decimal" and "decimal_places" in constraints:
                places = decimals(scalar)
                if places is None or places > constraints["decimal_places"]:
                    add(label, "VALUE_PRECISION", "decimal value exceeds approved precision")
        unit_policy = attribute.get("unit_policy", {})
        unit_id = assignment.get("unit_id")
        mode = unit_policy.get("mode")
        allowed_units = unit_policy.get("allowed_unit_ids", [])
        if mode == "FORBIDDEN" and unit_id is not None:
            add(label, "UNIT_FORBIDDEN", "attribute forbids a Unit")
        if mode == "REQUIRED" and unit_id is None:
            add(label, "UNIT_REQUIRED", "attribute requires a Unit")
        if unit_id is not None and unit_id not in allowed_units:
            add(label, "UNIT_NOT_ALLOWED", f"Unit is not allowed by attribute: {unit_id}")

    assignment_pairs = {
        (assignment.get("entity_id"), assignment.get("attribute_id"))
        for assignment in assignments.values()
    }
    for profile_id, profile in profiles.items():
        scope_id = profile.get("scope_entity_id")
        for rule in list_items(profile.get("attribute_rules")):
            if not isinstance(rule, dict):
                continue
            pair = (scope_id, rule.get("attribute_id"))
            if rule.get("requirement_level") == "REQUIRED" and pair not in assignment_pairs:
                add(
                    profile_id,
                    "REQUIRED_ASSIGNMENT_MISSING",
                    f"required synthetic assignment is missing: {rule.get('attribute_id')}",
                )
            if rule.get("requirement_level") == "PROHIBITED" and pair in assignment_pairs:
                add(
                    profile_id,
                    "PROHIBITED_ASSIGNMENT",
                    f"PROHIBITED rule has a synthetic assignment: {rule.get('attribute_id')}",
                )

    combinations: set[str] = set()
    for index, rule_set in enumerate(
        list_items(bundle.get("variant_rule_sets")),
        start=1,
    ):
        if not isinstance(rule_set, dict):
            continue
        rule_set_id = rule_set.get("rule_set_entity_id")
        label = str(rule_set_id or f"<rule-set:{index}>")
        entity = entities.get(rule_set_id)
        if entity is None or entity.get("entity_type") != "VARIANT_RULE_SET":
            add(label, "RULE_SET_ENTITY", "rule_set_entity_id must resolve to VARIANT_RULE_SET")
        profile = profiles.get(rule_set.get("profile_id"))
        if profile is None:
            add(label, "UNKNOWN_PROFILE", f"unknown profile: {rule_set.get('profile_id')}")
            profile_rules: dict[str, dict[str, Any]] = {}
        else:
            profile_rules = {
                rule.get("attribute_id"): rule
                for rule in list_items(profile.get("attribute_rules"))
                if isinstance(rule, dict)
            }
            scope_id = profile.get("scope_entity_id")
            if entity is not None and entity.get("parent_entity_id") != scope_id:
                add(label, "RULE_SET_SCOPE", "Variant Rule Set must be a child of profile scope")
        axes = list_items(rule_set.get("axes"))
        for axis in axes:
            rule = profile_rules.get(axis)
            if rule is None:
                add(label, "AXIS_NOT_IN_PROFILE", f"axis is not in profile: {axis}")
            elif rule.get("variation_axis") is not True:
                add(label, "AXIS_NOT_ENABLED", f"profile does not enable axis: {axis}")
        for combination in list_items(rule_set.get("allowed_combinations")):
            if not isinstance(combination, dict):
                continue
            combination_id = combination.get("combination_id")
            if combination_id in combinations:
                add(label, "DUPLICATE_COMBINATION_ID", f"duplicate combination: {combination_id}")
            elif isinstance(combination_id, str):
                combinations.add(combination_id)
            assignment_ids = list_items(combination.get("assignment_ids"))
            referenced_attributes: set[str] = set()
            for assignment_id in assignment_ids:
                assignment = assignments.get(assignment_id)
                if assignment is None:
                    add(label, "UNKNOWN_ASSIGNMENT", f"unknown assignment: {assignment_id}")
                    continue
                referenced_attributes.add(str(assignment.get("attribute_id")))
                if profile is not None and assignment.get("entity_id") != profile.get(
                    "scope_entity_id"
                ):
                    add(
                        label,
                        "ASSIGNMENT_SCOPE",
                        f"assignment is outside profile scope: {assignment_id}",
                    )
            if set(axes) != referenced_attributes:
                add(
                    label,
                    "COMBINATION_AXIS_COVERAGE",
                    "combination assignments must cover every axis exactly",
                )
        if rule_set.get("cartesian_generation_forbidden") is not True:
            add(label, "CARTESIAN_FORBIDDEN", "Cartesian generation must remain forbidden")

    return sorted(issues, key=lambda item: (item.entity, item.code, item.message))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate PD-01 synthetic Product Master Data bundles offline."
    )
    parser.add_argument("source", nargs="?", default=str(DEFAULT_BUNDLE))
    parser.add_argument("--entities", default=str(DEFAULT_ENTITIES))
    parser.add_argument("--attributes", default=str(DEFAULT_ATTRIBUTES))
    parser.add_argument("--contract", default=str(CONTRACT_PATH))
    parser.add_argument("--schema", default=str(SCHEMA_PATH))
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        definitions = load_definitions(Path(args.contract), Path(args.schema))
        entities, entity_parser = load_yaml(Path(args.entities), "Product Core fixture")
        attributes, attribute_parser = load_yaml(
            Path(args.attributes),
            "Product Attribute fixture",
        )
        bundle, bundle_parser = load_yaml(Path(args.source), "Product Master Data fixture")
        issues = validate_bundle(
            bundle,
            args.source,
            definitions,
            entities,
            attributes,
        )
    except DuplicateKeyError as exc:
        print(f"VALIDATION CONFIGURATION FAILED: [DUPLICATE_KEY] {exc}", file=sys.stderr)
        return 2
    except (
        ConfigurationError,
        AttributeDefinitionError,
        ProductDefinitionError,
        OSError,
        TypeError,
        ValueError,
    ) as exc:
        print(f"VALIDATION CONFIGURATION FAILED: {exc}", file=sys.stderr)
        return 2

    if issues:
        print(f"VALIDATION FAILED: {len(issues)} issue(s)", file=sys.stderr)
        for issue in issues:
            print(issue.render(), file=sys.stderr)
        return 1

    print(
        "PD-01 PRODUCT MASTER DATA VALIDATION PASSED: "
        f"{len(bundle['attribute_profiles'])} synthetic profile(s); "
        f"{len(bundle['value_assignments'])} synthetic assignment(s); "
        f"{len(bundle['variant_rule_sets'])} synthetic rule set(s); "
        f"parser={'; '.join(sorted({entity_parser, attribute_parser, bundle_parser}))}; "
        "canonical population, SKU, Golden, import, runtime, and network authority=false."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
