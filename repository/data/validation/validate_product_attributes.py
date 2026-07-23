#!/usr/bin/env python3
"""Deterministic offline validation for the Wave 2B Attribute foundation."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repository/data/contracts/product-attribute.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/product-attribute.schema.json"
ATTRIBUTES_PATH = ROOT / "repository/data/registries/product-attributes.yaml"
DATA_TYPES_PATH = ROOT / "repository/data/registries/attribute-data-types.yaml"
CATEGORIES_PATH = ROOT / "repository/data/registries/attribute-categories.yaml"
UNITS_PATH = ROOT / "repository/data/registries/attribute-units.yaml"
REQUIREMENTS_PATH = ROOT / "repository/data/registries/attribute-requirement-levels.yaml"
STATUSES_PATH = ROOT / "repository/data/registries/product-statuses.yaml"

SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
MACHINE_CODE_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]*$")
OWNER_ROLE_PATTERN = re.compile(r"^[a-z][a-z0-9-]{2,63}$")
CAPTURED_BY_PATTERN = re.compile(r"^role:[a-z][a-z0-9-]{2,63}$")

EXPECTED_DATA_TYPES = {
    "TEXT": ("string", False, True, "NONE"),
    "INTEGER": ("integer", True, True, "NONE"),
    "DECIMAL": ("number", True, True, "NONE"),
    "BOOLEAN": ("boolean", False, False, "NONE"),
    "CONTROLLED_TERM": ("string", False, True, "VALUE_REGISTRY_REFERENCE"),
    "ENTITY_REFERENCE": ("string", False, True, "TARGET_REGISTRY_REFERENCE"),
}
EXPECTED_CATEGORIES = {
    "PRIMARY",
    "SECONDARY",
    "COMMERCIAL",
    "OPERATIONAL_INTERNAL",
}
EXPECTED_REQUIREMENT_LEVELS = {
    "REQUIRED": (True, False, True),
    "OPTIONAL": (False, False, True),
    "CONDITIONAL": (False, True, True),
    "PROHIBITED": (False, False, False),
}
EXPECTED_STATUSES = {
    "APPROVED",
    "CANDIDATE_UNVERIFIED",
    "MISSING_DATA_VALUE",
    "FOUNDER_INPUT_REQUIRED",
    "DEFERRED",
    "NOT_APPLICABLE",
    "INVALID",
}
DATA_TYPE_FIELDS = {
    "code",
    "json_value_type",
    "supports_units",
    "supports_multiple_values",
    "required_constraint",
    "description",
}
CATEGORY_FIELDS = {
    "code",
    "contains_business_data",
    "grants_publication_authority",
    "description",
}
REQUIREMENT_FIELDS = {
    "code",
    "requires_value",
    "requires_condition_reference",
    "permits_value",
    "description",
}
CONSTRAINT_FIELDS = {
    "min_length",
    "max_length",
    "minimum",
    "maximum",
    "decimal_places",
    "pattern",
    "value_registry_reference",
    "target_registry_reference",
}
CONSTRAINTS_BY_TYPE = {
    "TEXT": {"min_length", "max_length", "pattern"},
    "INTEGER": {"minimum", "maximum"},
    "DECIMAL": {"minimum", "maximum", "decimal_places"},
    "BOOLEAN": set(),
    "CONTROLLED_TERM": {"value_registry_reference"},
    "ENTITY_REFERENCE": {"target_registry_reference"},
}


class DefinitionError(ValueError):
    """Raised when foundation definitions are missing or inconsistent."""


@dataclass(frozen=True)
class ValidationIssue:
    source: str
    attribute: str
    code: str
    message: str

    def render(self) -> str:
        return f"{self.source}: attribute {self.attribute}: [{self.code}] {self.message}"


@dataclass(frozen=True)
class Definitions:
    contract_version: str
    attribute_id_pattern: re.Pattern[str]
    attribute_key_pattern: re.Pattern[str]
    unit_id_pattern: re.Pattern[str]
    required_fields: set[str]
    prohibited_fields: set[str]
    data_types: dict[str, dict[str, Any]]
    categories: set[str]
    statuses: set[str]
    unit_ids: set[str]
    parser_sources: tuple[str, ...]


def read_text(path: Path, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise DefinitionError(f"missing {label}: {path.relative_to(ROOT)}") from exc


def parse_yaml(raw: str, label: str) -> tuple[Any, str]:
    try:
        import yaml  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        command = [
            "ruby",
            "-ryaml",
            "-rjson",
            "-e",
            (
                "value=YAML.safe_load(STDIN.read, [], [], false); "
                "STDOUT.write(JSON.generate(value))"
            ),
        ]
        try:
            result = subprocess.run(
                command,
                input=raw,
                text=True,
                capture_output=True,
                check=False,
            )
        except FileNotFoundError as exc:
            raise DefinitionError(
                "YAML validation requires approved PyYAML or Ruby Psych; neither is available"
            ) from exc
        if result.returncode != 0:
            raise DefinitionError(
                f"invalid YAML in {label} via Ruby Psych: {result.stderr.strip()}"
            )
        try:
            return json.loads(result.stdout), "Ruby Psych fallback"
        except json.JSONDecodeError as exc:
            raise DefinitionError(f"Ruby Psych returned invalid JSON for {label}") from exc

    try:
        return yaml.safe_load(raw), f"PyYAML {yaml.__version__}"
    except yaml.YAMLError as exc:  # type: ignore[attr-defined]
        raise DefinitionError(f"invalid YAML in {label}: {exc}") from exc


def load_yaml(path: Path, label: str) -> tuple[Any, str]:
    return parse_yaml(read_text(path, label), label)


def load_json(path: Path, label: str) -> Any:
    try:
        return json.loads(read_text(path, label))
    except json.JSONDecodeError as exc:
        raise DefinitionError(
            f"invalid JSON in {label} at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise DefinitionError(f"{label} must be a mapping")
    return value


def require_exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        raise DefinitionError(
            f"{label} keys differ; missing={sorted(expected - set(value))}, "
            f"extra={sorted(set(value) - expected)}"
        )


def require_semver(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SEMVER_PATTERN.fullmatch(value):
        raise DefinitionError(f"{label} must use semantic-version core")
    return value


def validate_data_types(value: Any) -> dict[str, dict[str, Any]]:
    registry = require_mapping(value, "Attribute data-type registry")
    if registry.get("registry_id") != "attribute-data-types":
        raise DefinitionError("data-type registry_id must be attribute-data-types")
    require_semver(registry.get("registry_version"), "data-type registry_version")
    entries = registry.get("data_types")
    if not isinstance(entries, list):
        raise DefinitionError("data_types must be a list")
    by_code: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(entries):
        entry = require_mapping(item, f"data_types[{index}]")
        require_exact_keys(entry, DATA_TYPE_FIELDS, f"data_types[{index}]")
        code = entry.get("code")
        if not isinstance(code, str) or code in by_code:
            raise DefinitionError(f"data_types[{index}] has an invalid or duplicate code")
        if not isinstance(entry.get("description"), str) or not entry["description"].strip():
            raise DefinitionError(f"data type {code} requires a description")
        by_code[code] = entry
    if set(by_code) != set(EXPECTED_DATA_TYPES):
        raise DefinitionError("data-type registry differs from the exact infrastructure set")
    for code, expected in EXPECTED_DATA_TYPES.items():
        entry = by_code[code]
        actual = (
            entry["json_value_type"],
            entry["supports_units"],
            entry["supports_multiple_values"],
            entry["required_constraint"],
        )
        if actual != expected:
            raise DefinitionError(f"data-type semantics differ for {code}")
    return by_code


def validate_categories(value: Any) -> set[str]:
    registry = require_mapping(value, "Attribute category registry")
    if registry.get("registry_id") != "attribute-categories":
        raise DefinitionError("category registry_id must be attribute-categories")
    require_semver(registry.get("registry_version"), "category registry_version")
    entries = registry.get("categories")
    if not isinstance(entries, list):
        raise DefinitionError("categories must be a list")
    codes: set[str] = set()
    for index, item in enumerate(entries):
        entry = require_mapping(item, f"categories[{index}]")
        require_exact_keys(entry, CATEGORY_FIELDS, f"categories[{index}]")
        code = entry.get("code")
        if not isinstance(code, str) or code in codes:
            raise DefinitionError(f"categories[{index}] has an invalid or duplicate code")
        if entry["contains_business_data"] is not False:
            raise DefinitionError(f"category {code} must remain data-free")
        if entry["grants_publication_authority"] is not False:
            raise DefinitionError(f"category {code} must not grant publication authority")
        if not isinstance(entry.get("description"), str) or not entry["description"].strip():
            raise DefinitionError(f"category {code} requires a description")
        codes.add(code)
    if codes != EXPECTED_CATEGORIES:
        raise DefinitionError("category registry differs from the exact infrastructure set")
    return codes


def validate_requirement_levels(value: Any) -> None:
    registry = require_mapping(value, "Attribute requirement-level registry")
    if registry.get("registry_id") != "attribute-requirement-levels":
        raise DefinitionError(
            "requirement-level registry_id must be attribute-requirement-levels"
        )
    require_semver(registry.get("registry_version"), "requirement registry_version")
    entries = registry.get("requirement_levels")
    if not isinstance(entries, list):
        raise DefinitionError("requirement_levels must be a list")
    by_code: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(entries):
        entry = require_mapping(item, f"requirement_levels[{index}]")
        require_exact_keys(entry, REQUIREMENT_FIELDS, f"requirement_levels[{index}]")
        code = entry.get("code")
        if not isinstance(code, str) or code in by_code:
            raise DefinitionError(
                f"requirement_levels[{index}] has an invalid or duplicate code"
            )
        if not isinstance(entry.get("description"), str) or not entry["description"].strip():
            raise DefinitionError(f"requirement level {code} requires a description")
        by_code[code] = entry
    if set(by_code) != set(EXPECTED_REQUIREMENT_LEVELS):
        raise DefinitionError("requirement-level registry differs from the exact set")
    for code, expected in EXPECTED_REQUIREMENT_LEVELS.items():
        entry = by_code[code]
        actual = (
            entry["requires_value"],
            entry["requires_condition_reference"],
            entry["permits_value"],
        )
        if actual != expected or not all(isinstance(item, bool) for item in actual):
            raise DefinitionError(f"requirement-level semantics differ for {code}")


def validate_statuses(value: Any) -> set[str]:
    registry = require_mapping(value, "Product status registry")
    entries = registry.get("statuses")
    if not isinstance(entries, list):
        raise DefinitionError("Product statuses must be a list")
    codes = {
        item.get("code")
        for item in entries
        if isinstance(item, dict) and isinstance(item.get("code"), str)
    }
    if codes != EXPECTED_STATUSES or len(entries) != len(EXPECTED_STATUSES):
        raise DefinitionError("Product status registry differs from the approved seven statuses")
    return codes


def validate_empty_registries(
    attributes_value: Any, units_value: Any, contract_version: str
) -> set[str]:
    attributes = require_mapping(attributes_value, "Product Attribute registry")
    require_exact_keys(
        attributes,
        {"registry_id", "registry_version", "contract_version", "attributes"},
        "Product Attribute registry",
    )
    if attributes["registry_id"] != "product-attributes":
        raise DefinitionError("Attribute registry_id must be product-attributes")
    require_semver(attributes["registry_version"], "Attribute registry_version")
    if attributes["contract_version"] != contract_version:
        raise DefinitionError("Attribute registry contract_version is incompatible")
    if attributes["attributes"] != []:
        raise DefinitionError("Wave 2B Product Attribute registry must contain zero entries")

    units = require_mapping(units_value, "Attribute Unit registry")
    require_exact_keys(units, {"registry_id", "registry_version", "units"}, "Unit registry")
    if units["registry_id"] != "attribute-units":
        raise DefinitionError("Unit registry_id must be attribute-units")
    require_semver(units["registry_version"], "Unit registry_version")
    if units["units"] != []:
        raise DefinitionError("Wave 2B Unit registry must contain zero entries")
    return set()


def validate_contract_schema(
    contract_value: Any,
    schema_value: Any,
    data_types: dict[str, dict[str, Any]],
    categories: set[str],
    statuses: set[str],
) -> tuple[str, re.Pattern[str], re.Pattern[str], re.Pattern[str], set[str], set[str]]:
    contract = require_mapping(contract_value, "Product Attribute contract")
    if contract.get("contract_id") != "product-attribute":
        raise DefinitionError("contract_id must be product-attribute")
    contract_version = require_semver(contract.get("contract_version"), "contract_version")
    required_fields = set(contract.get("always_required_attribute_fields", []))
    expected_required = {
        "contract_version",
        "attribute_id",
        "attribute_key",
        "canonical_label",
        "description",
        "category",
        "data_type",
        "unit_policy",
        "validation",
        "status",
        "owner",
        "provenance",
        "record_version",
    }
    if required_fields != expected_required:
        raise DefinitionError("contract required fields differ from the exact foundation set")
    naming = require_mapping(contract.get("canonical_naming"), "canonical_naming")
    try:
        attribute_id_pattern = re.compile(str(naming["attribute_id"]["pattern"]))
        attribute_key_pattern = re.compile(str(naming["attribute_key"]["pattern"]))
        unit_id_pattern = re.compile(str(naming["unit_id"]["pattern"]))
    except (KeyError, TypeError, re.error) as exc:
        raise DefinitionError("canonical naming patterns are missing or invalid") from exc
    prohibited = contract.get("prohibited_fields")
    if not isinstance(prohibited, list) or not prohibited:
        raise DefinitionError("prohibited_fields must be a non-empty list")
    prohibited_fields = {str(item) for item in prohibited}
    boundary = require_mapping(contract.get("data_boundary"), "data_boundary")
    if any(boundary.values()):
        raise DefinitionError("Wave 2B data and runtime boundaries must all remain false")

    schema = require_mapping(schema_value, "Product Attribute JSON Schema")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise DefinitionError("JSON Schema must declare draft 2020-12")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise DefinitionError("JSON Schema must be a closed object schema")
    if set(schema.get("required", [])) != required_fields:
        raise DefinitionError("JSON Schema required fields differ from the contract")
    properties = require_mapping(schema.get("properties"), "JSON Schema properties")
    if set(properties) != required_fields:
        raise DefinitionError("JSON Schema properties differ from the contract")
    if properties.get("contract_version", {}).get("const") != contract_version:
        raise DefinitionError("JSON Schema contract_version differs from the contract")
    if properties.get("attribute_id", {}).get("pattern") != naming["attribute_id"]["pattern"]:
        raise DefinitionError("JSON Schema attribute_id pattern differs from the contract")
    if properties.get("attribute_key", {}).get("pattern") != naming["attribute_key"]["pattern"]:
        raise DefinitionError("JSON Schema attribute_key pattern differs from the contract")
    if set(properties.get("data_type", {}).get("enum", [])) != set(data_types):
        raise DefinitionError("JSON Schema data types differ from the registry")
    if set(properties.get("category", {}).get("enum", [])) != categories:
        raise DefinitionError("JSON Schema categories differ from the registry")
    if set(properties.get("status", {}).get("enum", [])) != statuses:
        raise DefinitionError("JSON Schema statuses differ from the approved registry")
    return (
        contract_version,
        attribute_id_pattern,
        attribute_key_pattern,
        unit_id_pattern,
        required_fields,
        prohibited_fields,
    )


def load_definitions() -> Definitions:
    contract, contract_parser = load_yaml(CONTRACT_PATH, "Product Attribute contract")
    data_type_registry, type_parser = load_yaml(DATA_TYPES_PATH, "Attribute data types")
    category_registry, category_parser = load_yaml(CATEGORIES_PATH, "Attribute categories")
    requirement_registry, requirement_parser = load_yaml(
        REQUIREMENTS_PATH, "Attribute requirement levels"
    )
    status_registry, status_parser = load_yaml(STATUSES_PATH, "Product statuses")
    attributes_registry, attribute_parser = load_yaml(ATTRIBUTES_PATH, "Product Attributes")
    units_registry, unit_parser = load_yaml(UNITS_PATH, "Attribute Units")
    schema = load_json(SCHEMA_PATH, "Product Attribute JSON Schema")

    data_types = validate_data_types(data_type_registry)
    categories = validate_categories(category_registry)
    validate_requirement_levels(requirement_registry)
    statuses = validate_statuses(status_registry)
    (
        contract_version,
        attribute_id_pattern,
        attribute_key_pattern,
        unit_id_pattern,
        required_fields,
        prohibited_fields,
    ) = validate_contract_schema(contract, schema, data_types, categories, statuses)
    unit_ids = validate_empty_registries(
        attributes_registry, units_registry, contract_version
    )
    return Definitions(
        contract_version=contract_version,
        attribute_id_pattern=attribute_id_pattern,
        attribute_key_pattern=attribute_key_pattern,
        unit_id_pattern=unit_id_pattern,
        required_fields=required_fields,
        prohibited_fields=prohibited_fields,
        data_types=data_types,
        categories=categories,
        statuses=statuses,
        unit_ids=unit_ids,
        parser_sources=(
            contract_parser,
            type_parser,
            category_parser,
            requirement_parser,
            status_parser,
            attribute_parser,
            unit_parser,
        ),
    )


def nonempty_string(value: Any, maximum: int | None = None) -> bool:
    return (
        isinstance(value, str)
        and bool(value.strip())
        and (maximum is None or len(value) <= maximum)
    )


def rfc3339_utc(value: Any) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return parsed.tzinfo is not None


def iter_keys(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            if isinstance(key, str):
                yield key
            yield from iter_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_keys(child)


def validate_owner_provenance(
    record: dict[str, Any], source: str, attribute: str
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    def add(code: str, message: str) -> None:
        issues.append(ValidationIssue(source, attribute, code, message))

    owner = record.get("owner")
    if owner is not None:
        if not isinstance(owner, dict) or set(owner) != {"role"}:
            add("OWNER_STRUCTURE", "owner must contain only a role field")
        elif not isinstance(owner["role"], str) or not OWNER_ROLE_PATTERN.fullmatch(
            owner["role"]
        ):
            add("OWNER_ROLE", "owner.role must be a stable machine role")

    provenance = record.get("provenance")
    expected = {
        "source_type",
        "source_reference",
        "captured_by",
        "captured_at",
        "evidence_status",
    }
    if provenance is not None:
        if not isinstance(provenance, dict) or not provenance:
            add("PROVENANCE_STRUCTURE", "provenance must be a non-empty mapping")
        else:
            for field in sorted(expected - set(provenance)):
                add("MISSING_PROVENANCE", f"missing provenance field: {field}")
            for field in sorted(set(provenance) - expected):
                add("PROVENANCE_STRUCTURE", f"unexpected provenance field: {field}")
            source_type = provenance.get("source_type")
            if source_type is not None and (
                not isinstance(source_type, str)
                or not MACHINE_CODE_PATTERN.fullmatch(source_type)
            ):
                add("PROVENANCE_SOURCE_TYPE", "source_type must be a machine code")
            if "source_reference" in provenance and not nonempty_string(
                provenance.get("source_reference"), 500
            ):
                add(
                    "PROVENANCE_SOURCE_REFERENCE",
                    "source_reference must be 1-500 non-blank characters",
                )
            captured_by = provenance.get("captured_by")
            if captured_by is not None and (
                not isinstance(captured_by, str)
                or not CAPTURED_BY_PATTERN.fullmatch(captured_by)
            ):
                add("PROVENANCE_CAPTURED_BY", "captured_by must identify a role")
            if "captured_at" in provenance and not rfc3339_utc(
                provenance.get("captured_at")
            ):
                add("PROVENANCE_CAPTURED_AT", "captured_at must be RFC 3339 UTC")
            evidence_status = provenance.get("evidence_status")
            if evidence_status is not None and (
                not isinstance(evidence_status, str)
                or not MACHINE_CODE_PATTERN.fullmatch(evidence_status)
            ):
                add("PROVENANCE_EVIDENCE_STATUS", "evidence_status must be a machine code")
    return issues


def validate_constraints(
    validation: dict[str, Any], data_type: str, source: str, attribute: str
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    def add(code: str, message: str) -> None:
        issues.append(ValidationIssue(source, attribute, code, message))

    if set(validation) != {"nullable", "multiple_values", "constraints"}:
        add("VALIDATION_STRUCTURE", "validation fields must be nullable, multiple_values, constraints")
        return issues
    if not isinstance(validation.get("nullable"), bool):
        add("VALIDATION_NULLABLE", "nullable must be boolean")
    if not isinstance(validation.get("multiple_values"), bool):
        add("VALIDATION_MULTIPLE", "multiple_values must be boolean")
    constraints = validation.get("constraints")
    if not isinstance(constraints, dict):
        add("CONSTRAINT_STRUCTURE", "constraints must be a mapping")
        return issues
    unknown = set(constraints) - CONSTRAINT_FIELDS
    for field in sorted(unknown):
        add("UNKNOWN_CONSTRAINT", f"unknown constraint field: {field}")
    allowed = CONSTRAINTS_BY_TYPE.get(data_type)
    if allowed is not None:
        for field in sorted(set(constraints) - allowed):
            add("CONSTRAINT_TYPE_MISMATCH", f"{field} is not valid for {data_type}")

    for field in ("min_length", "max_length"):
        if field in constraints and (
            not isinstance(constraints[field], int)
            or isinstance(constraints[field], bool)
            or constraints[field] < 0
        ):
            add("LENGTH_CONSTRAINT", f"{field} must be a non-negative integer")
    if isinstance(constraints.get("min_length"), int) and isinstance(
        constraints.get("max_length"), int
    ) and constraints["min_length"] > constraints["max_length"]:
        add("LENGTH_RANGE", "min_length must not exceed max_length")

    for field in ("minimum", "maximum"):
        if field in constraints and (
            not isinstance(constraints[field], (int, float))
            or isinstance(constraints[field], bool)
        ):
            add("NUMERIC_CONSTRAINT", f"{field} must be numeric")
    if isinstance(constraints.get("minimum"), (int, float)) and isinstance(
        constraints.get("maximum"), (int, float)
    ) and constraints["minimum"] > constraints["maximum"]:
        add("NUMERIC_RANGE", "minimum must not exceed maximum")
    if "decimal_places" in constraints and (
        not isinstance(constraints["decimal_places"], int)
        or isinstance(constraints["decimal_places"], bool)
        or not 0 <= constraints["decimal_places"] <= 12
    ):
        add("DECIMAL_PLACES", "decimal_places must be an integer from 0 through 12")
    if "pattern" in constraints:
        if not nonempty_string(constraints["pattern"]):
            add("PATTERN_CONSTRAINT", "pattern must be a non-empty string")
        else:
            try:
                re.compile(constraints["pattern"])
            except re.error as exc:
                add("PATTERN_CONSTRAINT", f"pattern does not compile: {exc}")
    for field in ("value_registry_reference", "target_registry_reference"):
        if field in constraints and not nonempty_string(constraints[field], 500):
            add("REGISTRY_REFERENCE", f"{field} must be a non-empty reference")
    if data_type == "CONTROLLED_TERM" and "value_registry_reference" not in constraints:
        add("VALUE_REGISTRY_REQUIRED", "CONTROLLED_TERM requires value_registry_reference")
    if data_type == "ENTITY_REFERENCE" and "target_registry_reference" not in constraints:
        add("TARGET_REGISTRY_REQUIRED", "ENTITY_REFERENCE requires target_registry_reference")
    return issues


def validate_fixture(
    value: Any, source: str, definitions: Definitions
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    def add(attribute: str, code: str, message: str) -> None:
        issues.append(ValidationIssue(source, attribute, code, message))

    if not isinstance(value, list):
        add("<fixture>", "FIXTURE_TYPE", "fixture must contain a YAML sequence")
        return issues
    if not value:
        add("<fixture>", "EMPTY_FIXTURE", "fixture must contain a synthetic definition")
        return issues

    ids: set[str] = set()
    keys: set[str] = set()
    for index, raw in enumerate(value, start=1):
        attribute = (
            raw.get("attribute_id")
            if isinstance(raw, dict) and nonempty_string(raw.get("attribute_id"))
            else f"<record:{index}>"
        )
        if not isinstance(raw, dict):
            add(str(attribute), "RECORD_TYPE", "attribute definition must be a mapping")
            continue
        record = raw
        string_keys = {key for key in record if isinstance(key, str)}
        for key in record:
            if not isinstance(key, str):
                add(str(attribute), "FIELD_NAME_TYPE", f"field name must be string: {key!r}")
        for field in sorted(string_keys - definitions.required_fields):
            add(str(attribute), "UNEXPECTED_FIELD", f"unexpected field: {field}")
        for field in sorted(definitions.required_fields - string_keys):
            code = "MISSING_PROVENANCE" if field == "provenance" else "MISSING_REQUIRED_FIELD"
            add(str(attribute), code, f"missing required field: {field}")
        for field in sorted(definitions.required_fields & string_keys):
            if record[field] is None:
                add(
                    str(attribute),
                    "NULL_REQUIRED_FIELD",
                    f"required field must not be null: {field}",
                )
        for field in sorted(
            {key for key in iter_keys(record) if key in definitions.prohibited_fields}
        ):
            add(str(attribute), "PROHIBITED_FIELD", f"prohibited business or adapter field: {field}")

        contract_version = record.get("contract_version")
        if contract_version is not None:
            if not isinstance(contract_version, str) or not SEMVER_PATTERN.fullmatch(
                contract_version
            ):
                add(str(attribute), "CONTRACT_VERSION_FORMAT", "contract_version must use X.Y.Z")
            elif contract_version != definitions.contract_version:
                add(
                    str(attribute),
                    "CONTRACT_VERSION_INCOMPATIBLE",
                    f"contract_version must be {definitions.contract_version}",
                )
        record_version = record.get("record_version")
        if record_version is not None and (
            not isinstance(record_version, str)
            or not SEMVER_PATTERN.fullmatch(record_version)
        ):
            add(str(attribute), "RECORD_VERSION_FORMAT", "record_version must use X.Y.Z")

        attribute_id = record.get("attribute_id")
        if attribute_id is not None:
            if not isinstance(attribute_id, str) or not definitions.attribute_id_pattern.fullmatch(
                attribute_id
            ):
                add(str(attribute), "ATTRIBUTE_ID_FORMAT", "attribute_id violates canonical format")
            elif attribute_id in ids:
                add(str(attribute), "DUPLICATE_ATTRIBUTE_ID", f"duplicate attribute_id: {attribute_id}")
            else:
                ids.add(attribute_id)
        attribute_key = record.get("attribute_key")
        if attribute_key is not None:
            if not isinstance(attribute_key, str) or not definitions.attribute_key_pattern.fullmatch(
                attribute_key
            ):
                add(str(attribute), "ATTRIBUTE_KEY_FORMAT", "attribute_key must use lower_snake_case")
            elif attribute_key in keys:
                add(str(attribute), "DUPLICATE_ATTRIBUTE_KEY", f"duplicate attribute_key: {attribute_key}")
            else:
                keys.add(attribute_key)

        if "canonical_label" in record and not nonempty_string(
            record.get("canonical_label"), 200
        ):
            add(str(attribute), "CANONICAL_LABEL", "canonical_label must be 1-200 characters")
        if "description" in record and not nonempty_string(record.get("description"), 500):
            add(str(attribute), "DESCRIPTION", "description must be 1-500 characters")

        category = record.get("category")
        if category is not None and (
            not isinstance(category, str) or category not in definitions.categories
        ):
            add(str(attribute), "UNKNOWN_CATEGORY", f"unknown category: {category}")
        data_type = record.get("data_type")
        if data_type is not None and (
            not isinstance(data_type, str) or data_type not in definitions.data_types
        ):
            add(str(attribute), "UNKNOWN_DATA_TYPE", f"unknown data_type: {data_type}")
        status = record.get("status")
        if status is not None and (
            not isinstance(status, str) or status not in definitions.statuses
        ):
            add(str(attribute), "UNKNOWN_STATUS", f"unknown status: {status}")
        elif status == "INVALID":
            add(str(attribute), "INVALID_STATUS_BLOCK", "INVALID status blocks processing")

        unit_policy = record.get("unit_policy")
        if unit_policy is not None:
            if not isinstance(unit_policy, dict) or set(unit_policy) != {
                "mode",
                "allowed_unit_ids",
            }:
                add(
                    str(attribute),
                    "UNIT_POLICY_STRUCTURE",
                    "unit_policy must contain mode and allowed_unit_ids",
                )
            else:
                mode = unit_policy.get("mode")
                unit_ids = unit_policy.get("allowed_unit_ids")
                if mode not in {"FORBIDDEN", "OPTIONAL", "REQUIRED"}:
                    add(str(attribute), "UNIT_POLICY_MODE", f"unknown unit mode: {mode}")
                if not isinstance(unit_ids, list):
                    add(str(attribute), "UNIT_ID_LIST", "allowed_unit_ids must be a list")
                    unit_ids = []
                else:
                    if len(unit_ids) != len(set(str(item) for item in unit_ids)):
                        add(str(attribute), "DUPLICATE_UNIT_ID", "allowed_unit_ids must be unique")
                    for unit_id in unit_ids:
                        if not isinstance(unit_id, str) or not definitions.unit_id_pattern.fullmatch(
                            unit_id
                        ):
                            add(str(attribute), "UNIT_ID_FORMAT", f"invalid unit ID: {unit_id}")
                        elif unit_id not in definitions.unit_ids:
                            add(str(attribute), "UNKNOWN_UNIT", f"unknown unit ID: {unit_id}")
                if mode == "FORBIDDEN" and unit_ids:
                    add(str(attribute), "UNIT_FORBIDDEN", "FORBIDDEN mode requires zero unit IDs")
                if mode == "REQUIRED" and not unit_ids:
                    add(str(attribute), "UNIT_REQUIRED", "REQUIRED mode needs at least one unit ID")
                if isinstance(data_type, str) and data_type in definitions.data_types:
                    supports_units = definitions.data_types[data_type]["supports_units"]
                    if not supports_units and mode != "FORBIDDEN":
                        add(
                            str(attribute),
                            "UNIT_TYPE_MISMATCH",
                            f"{data_type} does not support units",
                        )

        validation = record.get("validation")
        if validation is not None:
            if not isinstance(validation, dict):
                add(str(attribute), "VALIDATION_STRUCTURE", "validation must be a mapping")
            elif isinstance(data_type, str) and data_type in definitions.data_types:
                issues.extend(
                    validate_constraints(validation, data_type, source, str(attribute))
                )
                multiple = validation.get("multiple_values")
                if multiple is True and not definitions.data_types[data_type][
                    "supports_multiple_values"
                ]:
                    add(
                        str(attribute),
                        "MULTIPLE_VALUES_UNSUPPORTED",
                        f"{data_type} does not support multiple values",
                    )

        issues.extend(validate_owner_provenance(record, source, str(attribute)))
    return issues


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate synthetic Product Attribute definition fixtures."
    )
    parser.add_argument("source", help="YAML fixture path, or '-' for stdin")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        definitions = load_definitions()
        if args.source == "-":
            source = "<stdin>"
            value, fixture_parser = parse_yaml(sys.stdin.read(), source)
        else:
            source = args.source
            value, fixture_parser = load_yaml(Path(args.source), source)
        issues = validate_fixture(value, source, definitions)
    except (DefinitionError, OSError, TypeError, ValueError) as exc:
        print(f"VALIDATION CONFIGURATION FAILED: {exc}", file=sys.stderr)
        return 2

    if issues:
        print(f"VALIDATION FAILED: {len(issues)} issue(s)", file=sys.stderr)
        for issue in issues:
            print(issue.render(), file=sys.stderr)
        return 1

    parsers = sorted(set(definitions.parser_sources + (fixture_parser,)))
    print(
        f"VALIDATION PASSED: {source} ({len(value)} synthetic definitions; "
        f"parser={'; '.join(parsers)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
