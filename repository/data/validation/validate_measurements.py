#!/usr/bin/env python3
"""Deterministic offline validation for the Wave 2C measurement foundation."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
from math import gcd
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Iterable
import unicodedata


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repository/data/contracts/measurement.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/measurement.schema.json"
DIMENSIONS_PATH = ROOT / "repository/data/registries/measurement-dimensions.yaml"
UNITS_PATH = ROOT / "repository/data/registries/attribute-units.yaml"
DATA_TYPES_PATH = ROOT / "repository/data/registries/attribute-data-types.yaml"
STATUSES_PATH = ROOT / "repository/data/registries/product-statuses.yaml"

SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
MACHINE_CODE_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]*$")
OWNER_ROLE_PATTERN = re.compile(r"^[a-z][a-z0-9-]{2,63}$")
CAPTURED_BY_PATTERN = re.compile(r"^role:[a-z][a-z0-9-]{2,63}$")

EXPECTED_STATUSES = {
    "APPROVED",
    "CANDIDATE_UNVERIFIED",
    "MISSING_DATA_VALUE",
    "FOUNDER_INPUT_REQUIRED",
    "DEFERRED",
    "NOT_APPLICABLE",
    "INVALID",
}
EXPECTED_UNIT_DATA_TYPES = {"INTEGER", "DECIMAL"}
EXPECTED_DIMENSION_FIELDS = {
    "contract_version",
    "dimension_id",
    "dimension_key",
    "canonical_name",
    "description",
    "base_unit_id",
    "status",
    "owner",
    "provenance",
    "record_version",
}
EXPECTED_UNIT_FIELDS = {
    "contract_version",
    "unit_id",
    "unit_key",
    "canonical_name",
    "symbol",
    "dimension_id",
    "is_base_unit",
    "base_unit_id",
    "conversion_to_base",
    "allowed_data_types",
    "precision",
    "status",
    "owner",
    "provenance",
    "record_version",
}


class MeasurementDefinitionError(ValueError):
    """Raised when canonical measurement definitions are inconsistent."""


@dataclass(frozen=True)
class ValidationIssue:
    source: str
    entity: str
    code: str
    message: str

    def render(self) -> str:
        return f"{self.source}: entity {self.entity}: [{self.code}] {self.message}"


@dataclass(frozen=True)
class Definitions:
    contract_version: str
    dimension_id_pattern: re.Pattern[str]
    dimension_key_pattern: re.Pattern[str]
    unit_id_pattern: re.Pattern[str]
    unit_key_pattern: re.Pattern[str]
    symbol_pattern: re.Pattern[str]
    dimension_fields: set[str]
    unit_fields: set[str]
    statuses: set[str]
    data_types: dict[str, dict[str, Any]]
    prohibited_fields: set[str]
    parser_sources: tuple[str, ...]


@dataclass(frozen=True)
class MeasurementFoundation:
    contract_version: str
    dimensions: dict[str, dict[str, Any]]
    units: dict[str, dict[str, Any]]
    parser_sources: tuple[str, ...]


@dataclass(frozen=True)
class BundleResult:
    issues: tuple[ValidationIssue, ...]
    dimensions: dict[str, dict[str, Any]]
    units: dict[str, dict[str, Any]]


def read_text(path: Path, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise MeasurementDefinitionError(
            f"missing {label}: {path.relative_to(ROOT)}"
        ) from exc


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
            raise MeasurementDefinitionError(
                "YAML validation requires approved PyYAML or Ruby Psych; neither is available"
            ) from exc
        if result.returncode != 0:
            raise MeasurementDefinitionError(
                f"invalid YAML in {label} via Ruby Psych: {result.stderr.strip()}"
            )
        try:
            return json.loads(result.stdout), "Ruby Psych fallback"
        except json.JSONDecodeError as exc:
            raise MeasurementDefinitionError(
                f"Ruby Psych returned invalid JSON for {label}"
            ) from exc

    try:
        return yaml.safe_load(raw), f"PyYAML {yaml.__version__}"
    except yaml.YAMLError as exc:  # type: ignore[attr-defined]
        raise MeasurementDefinitionError(f"invalid YAML in {label}: {exc}") from exc


def load_yaml(path: Path, label: str) -> tuple[Any, str]:
    return parse_yaml(read_text(path, label), label)


def load_json(path: Path, label: str) -> Any:
    try:
        return json.loads(read_text(path, label))
    except json.JSONDecodeError as exc:
        raise MeasurementDefinitionError(
            f"invalid JSON in {label} at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise MeasurementDefinitionError(f"{label} must be a mapping")
    return value


def require_exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        raise MeasurementDefinitionError(
            f"{label} keys differ; missing={sorted(expected - set(value))}, "
            f"extra={sorted(set(value) - expected)}"
        )


def require_semver(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SEMVER_PATTERN.fullmatch(value):
        raise MeasurementDefinitionError(f"{label} must use semantic-version core")
    return value


def load_statuses(value: Any) -> set[str]:
    registry = require_mapping(value, "Product status registry")
    entries = registry.get("statuses")
    if not isinstance(entries, list):
        raise MeasurementDefinitionError("Product statuses must be a list")
    statuses = {
        item.get("code")
        for item in entries
        if isinstance(item, dict) and isinstance(item.get("code"), str)
    }
    if statuses != EXPECTED_STATUSES or len(entries) != len(EXPECTED_STATUSES):
        raise MeasurementDefinitionError(
            "Product status registry differs from the approved seven statuses"
        )
    return statuses


def load_data_types(value: Any) -> dict[str, dict[str, Any]]:
    registry = require_mapping(value, "Attribute data-type registry")
    entries = registry.get("data_types")
    if not isinstance(entries, list):
        raise MeasurementDefinitionError("Attribute data_types must be a list")
    by_code: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(entries):
        entry = require_mapping(raw, f"data_types[{index}]")
        code = entry.get("code")
        if not isinstance(code, str) or code in by_code:
            raise MeasurementDefinitionError(
                f"data_types[{index}] has an invalid or duplicate code"
            )
        if not isinstance(entry.get("supports_units"), bool):
            raise MeasurementDefinitionError(
                f"data type {code} must declare boolean supports_units"
            )
        by_code[code] = entry
    unit_capable = {
        code for code, entry in by_code.items() if entry["supports_units"] is True
    }
    if unit_capable != EXPECTED_UNIT_DATA_TYPES:
        raise MeasurementDefinitionError(
            "unit-capable data types must be exactly INTEGER and DECIMAL"
        )
    return by_code


def compile_contract_pattern(
    naming: dict[str, Any], key: str, label: str
) -> re.Pattern[str]:
    try:
        return re.compile(str(naming[key]["pattern"]))
    except (KeyError, TypeError, re.error) as exc:
        raise MeasurementDefinitionError(f"{label} pattern is missing or invalid") from exc


def validate_contract_schema(
    contract_value: Any,
    schema_value: Any,
    statuses: set[str],
    data_types: dict[str, dict[str, Any]],
) -> tuple[
    str,
    re.Pattern[str],
    re.Pattern[str],
    re.Pattern[str],
    re.Pattern[str],
    re.Pattern[str],
    set[str],
    set[str],
    set[str],
]:
    contract = require_mapping(contract_value, "Measurement contract")
    if contract.get("contract_id") != "measurement-foundation":
        raise MeasurementDefinitionError(
            "Measurement contract_id must be measurement-foundation"
        )
    contract_version = require_semver(
        contract.get("contract_version"), "Measurement contract_version"
    )
    dimension_fields = set(contract.get("required_dimension_fields", []))
    unit_fields = set(contract.get("required_unit_fields", []))
    if dimension_fields != EXPECTED_DIMENSION_FIELDS:
        raise MeasurementDefinitionError(
            "Measurement contract dimension fields differ from the exact foundation set"
        )
    if unit_fields != EXPECTED_UNIT_FIELDS:
        raise MeasurementDefinitionError(
            "Measurement contract Unit fields differ from the exact foundation set"
        )

    naming = require_mapping(contract.get("canonical_naming"), "canonical_naming")
    dimension_id_pattern = compile_contract_pattern(
        naming, "dimension_id", "dimension_id"
    )
    dimension_key_pattern = compile_contract_pattern(
        naming, "dimension_key", "dimension_key"
    )
    unit_id_pattern = compile_contract_pattern(naming, "unit_id", "unit_id")
    unit_key_pattern = compile_contract_pattern(naming, "unit_key", "unit_key")
    symbol_pattern = compile_contract_pattern(naming, "symbol", "symbol")

    compatibility = require_mapping(contract.get("compatibility"), "compatibility")
    if set(compatibility.get("unit_capable_data_types", [])) != EXPECTED_UNIT_DATA_TYPES:
        raise MeasurementDefinitionError(
            "Measurement contract compatibility must be INTEGER and DECIMAL"
        )
    if {
        code for code, entry in data_types.items() if entry["supports_units"] is True
    } != EXPECTED_UNIT_DATA_TYPES:
        raise MeasurementDefinitionError(
            "Measurement contract and Attribute data types are incompatible"
        )
    boundary = require_mapping(contract.get("data_boundary"), "data_boundary")
    if any(value is not False for value in boundary.values()):
        raise MeasurementDefinitionError(
            "Measurement data and runtime boundaries must all remain false"
        )
    prohibited = contract.get("prohibited_fields")
    if not isinstance(prohibited, list) or not prohibited:
        raise MeasurementDefinitionError(
            "Measurement prohibited_fields must be a non-empty list"
        )
    prohibited_fields = {str(item) for item in prohibited}

    schema = require_mapping(schema_value, "Measurement JSON Schema")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise MeasurementDefinitionError(
            "Measurement JSON Schema must declare draft 2020-12"
        )
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise MeasurementDefinitionError(
            "Measurement JSON Schema must be a closed object schema"
        )
    expected_top = {"contract_version", "dimensions", "units"}
    if set(schema.get("required", [])) != expected_top:
        raise MeasurementDefinitionError(
            "Measurement JSON Schema required fields differ from the contract"
        )
    properties = require_mapping(
        schema.get("properties"), "Measurement JSON Schema properties"
    )
    if set(properties) != expected_top:
        raise MeasurementDefinitionError(
            "Measurement JSON Schema properties differ from the contract"
        )
    if properties.get("contract_version", {}).get("const") != contract_version:
        raise MeasurementDefinitionError(
            "Measurement JSON Schema contract_version differs from the contract"
        )
    definitions = require_mapping(schema.get("$defs"), "Measurement JSON Schema $defs")
    dimension_schema = require_mapping(
        definitions.get("dimension"), "Measurement dimension schema"
    )
    unit_schema = require_mapping(definitions.get("unit"), "Measurement Unit schema")
    if dimension_schema.get("additionalProperties") is not False or set(
        dimension_schema.get("required", [])
    ) != dimension_fields:
        raise MeasurementDefinitionError(
            "Measurement dimension schema differs from the contract"
        )
    if set(require_mapping(dimension_schema.get("properties"), "dimension properties")) != (
        dimension_fields
    ):
        raise MeasurementDefinitionError(
            "Measurement dimension properties differ from the contract"
        )
    if unit_schema.get("additionalProperties") is not False or set(
        unit_schema.get("required", [])
    ) != unit_fields:
        raise MeasurementDefinitionError(
            "Measurement Unit schema differs from the contract"
        )
    unit_properties = require_mapping(unit_schema.get("properties"), "Unit properties")
    if set(unit_properties) != unit_fields:
        raise MeasurementDefinitionError(
            "Measurement Unit properties differ from the contract"
        )
    if (
        unit_properties.get("unit_id", {}).get("pattern")
        != naming["unit_id"]["pattern"]
        or unit_properties.get("unit_key", {}).get("pattern")
        != naming["unit_key"]["pattern"]
        or unit_properties.get("symbol", {}).get("pattern")
        != naming["symbol"]["pattern"]
    ):
        raise MeasurementDefinitionError(
            "Measurement Unit naming differs between contract and schema"
        )
    if (
        dimension_schema["properties"].get("dimension_id", {}).get("pattern")
        != naming["dimension_id"]["pattern"]
        or dimension_schema["properties"].get("dimension_key", {}).get("pattern")
        != naming["dimension_key"]["pattern"]
    ):
        raise MeasurementDefinitionError(
            "Measurement dimension naming differs between contract and schema"
        )
    if set(
        unit_properties.get("allowed_data_types", {})
        .get("items", {})
        .get("enum", [])
    ) != EXPECTED_UNIT_DATA_TYPES:
        raise MeasurementDefinitionError(
            "Measurement schema data-type compatibility differs from the contract"
        )
    if set(definitions.get("status", {}).get("enum", [])) != statuses:
        raise MeasurementDefinitionError(
            "Measurement schema statuses differ from the approved registry"
        )
    precision_contract = require_mapping(
        contract.get("precision_model"), "precision_model"
    )
    precision_range = require_mapping(
        precision_contract.get("maximum_decimal_places"),
        "precision maximum_decimal_places",
    )
    precision_schema = require_mapping(
        definitions.get("precision"), "Measurement precision schema"
    )
    precision_places = require_mapping(
        precision_schema.get("properties", {}).get("maximum_decimal_places"),
        "Measurement precision range schema",
    )
    if (
        precision_places.get("minimum") != precision_range.get("minimum")
        or precision_places.get("maximum") != precision_range.get("maximum")
    ):
        raise MeasurementDefinitionError(
            "Measurement precision range differs between contract and schema"
        )
    if set(
        precision_schema.get("properties", {})
        .get("rounding_mode", {})
        .get("enum", [])
    ) != set(precision_contract.get("rounding_modes", [])):
        raise MeasurementDefinitionError(
            "Measurement rounding modes differ between contract and schema"
        )
    return (
        contract_version,
        dimension_id_pattern,
        dimension_key_pattern,
        unit_id_pattern,
        unit_key_pattern,
        symbol_pattern,
        dimension_fields,
        unit_fields,
        prohibited_fields,
    )


def load_definitions() -> Definitions:
    contract, contract_parser = load_yaml(CONTRACT_PATH, "Measurement contract")
    statuses_value, statuses_parser = load_yaml(STATUSES_PATH, "Product statuses")
    data_types_value, data_types_parser = load_yaml(
        DATA_TYPES_PATH, "Attribute data types"
    )
    schema = load_json(SCHEMA_PATH, "Measurement JSON Schema")
    statuses = load_statuses(statuses_value)
    data_types = load_data_types(data_types_value)
    (
        contract_version,
        dimension_id_pattern,
        dimension_key_pattern,
        unit_id_pattern,
        unit_key_pattern,
        symbol_pattern,
        dimension_fields,
        unit_fields,
        prohibited_fields,
    ) = validate_contract_schema(contract, schema, statuses, data_types)
    return Definitions(
        contract_version=contract_version,
        dimension_id_pattern=dimension_id_pattern,
        dimension_key_pattern=dimension_key_pattern,
        unit_id_pattern=unit_id_pattern,
        unit_key_pattern=unit_key_pattern,
        symbol_pattern=symbol_pattern,
        dimension_fields=dimension_fields,
        unit_fields=unit_fields,
        statuses=statuses,
        data_types=data_types,
        prohibited_fields=prohibited_fields,
        parser_sources=(contract_parser, statuses_parser, data_types_parser),
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


def normalized_token(value: str) -> str:
    return unicodedata.normalize("NFKC", value).casefold()


def validate_owner_provenance(
    record: dict[str, Any], source: str, entity: str
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    def add(code: str, message: str) -> None:
        issues.append(ValidationIssue(source, entity, code, message))

    owner = record.get("owner")
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
    if not isinstance(provenance, dict) or set(provenance) != expected:
        add(
            "PROVENANCE_STRUCTURE",
            "provenance must contain exactly the five required evidence fields",
        )
        return issues
    if not isinstance(provenance["source_type"], str) or not MACHINE_CODE_PATTERN.fullmatch(
        provenance["source_type"]
    ):
        add("PROVENANCE_SOURCE_TYPE", "source_type must be a machine code")
    if not nonempty_string(provenance["source_reference"], 500):
        add(
            "PROVENANCE_SOURCE_REFERENCE",
            "source_reference must be 1-500 non-blank characters",
        )
    if not isinstance(provenance["captured_by"], str) or not CAPTURED_BY_PATTERN.fullmatch(
        provenance["captured_by"]
    ):
        add("PROVENANCE_CAPTURED_BY", "captured_by must identify a role")
    if not rfc3339_utc(provenance["captured_at"]):
        add("PROVENANCE_CAPTURED_AT", "captured_at must be RFC 3339 UTC")
    if not isinstance(
        provenance["evidence_status"], str
    ) or not MACHINE_CODE_PATTERN.fullmatch(provenance["evidence_status"]):
        add(
            "PROVENANCE_EVIDENCE_STATUS",
            "evidence_status must be a machine code",
        )
    return issues


def validate_common(
    record: dict[str, Any],
    required_fields: set[str],
    source: str,
    entity: str,
    definitions: Definitions,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    def add(code: str, message: str) -> None:
        issues.append(ValidationIssue(source, entity, code, message))

    string_keys = {key for key in record if isinstance(key, str)}
    for key in record:
        if not isinstance(key, str):
            add("FIELD_NAME_TYPE", f"field name must be string: {key!r}")
    for field in sorted(string_keys - required_fields):
        add("UNEXPECTED_FIELD", f"unexpected field: {field}")
    for field in sorted(required_fields - string_keys):
        add("MISSING_REQUIRED_FIELD", f"missing required field: {field}")
    for field in sorted(required_fields & string_keys):
        if record[field] is None:
            add("NULL_REQUIRED_FIELD", f"required field must not be null: {field}")
    for field in sorted(
        {key for key in iter_keys(record) if key in definitions.prohibited_fields}
    ):
        add("PROHIBITED_FIELD", f"prohibited Product or runtime field: {field}")

    contract_version = record.get("contract_version")
    if contract_version is not None:
        if not isinstance(contract_version, str) or not SEMVER_PATTERN.fullmatch(
            contract_version
        ):
            add(
                "CONTRACT_VERSION_FORMAT",
                "contract_version must use semantic-version core",
            )
        elif contract_version != definitions.contract_version:
            add(
                "CONTRACT_VERSION_INCOMPATIBLE",
                f"contract_version must be {definitions.contract_version}",
            )
    record_version = record.get("record_version")
    if record_version is not None and (
        not isinstance(record_version, str)
        or not SEMVER_PATTERN.fullmatch(record_version)
    ):
        add(
            "RECORD_VERSION_FORMAT",
            "record_version must use semantic-version core",
        )
    if "canonical_name" in record and not nonempty_string(
        record.get("canonical_name"), 100
    ):
        add(
            "CANONICAL_NAME",
            "canonical_name must be 1-100 non-blank characters",
        )
    if "description" in record and not nonempty_string(record.get("description"), 500):
        add("DESCRIPTION", "description must be 1-500 non-blank characters")
    status = record.get("status")
    if status is not None and (
        not isinstance(status, str) or status not in definitions.statuses
    ):
        add("UNKNOWN_STATUS", f"unknown status: {status}")
    elif status == "INVALID":
        add("INVALID_STATUS_BLOCK", "INVALID status blocks foundation use")
    issues.extend(validate_owner_provenance(record, source, entity))
    return issues


def rational_tuple(
    value: Any,
    source: str,
    entity: str,
    label: str,
    require_positive_numerator: bool,
) -> tuple[tuple[int, int] | None, list[ValidationIssue]]:
    issues: list[ValidationIssue] = []

    def add(code: str, message: str) -> None:
        issues.append(ValidationIssue(source, entity, code, message))

    if not isinstance(value, dict) or set(value) != {"numerator", "denominator"}:
        add(
            "RATIONAL_STRUCTURE",
            f"{label} must contain numerator and denominator",
        )
        return None, issues
    numerator = value.get("numerator")
    denominator = value.get("denominator")
    if not isinstance(numerator, int) or isinstance(numerator, bool):
        add("RATIONAL_NUMERATOR", f"{label}.numerator must be an integer")
    if (
        not isinstance(denominator, int)
        or isinstance(denominator, bool)
        or denominator <= 0
    ):
        add(
            "RATIONAL_DENOMINATOR",
            f"{label}.denominator must be a positive integer",
        )
    if issues:
        return None, issues
    assert isinstance(numerator, int)
    assert isinstance(denominator, int)
    if require_positive_numerator and numerator <= 0:
        add(
            "NONPOSITIVE_MULTIPLIER",
            f"{label}.numerator must be positive",
        )
    if gcd(abs(numerator), denominator) != 1:
        add(
            "UNNORMALIZED_RATIONAL",
            f"{label} must be reduced to lowest terms",
        )
    return (numerator, denominator), issues


def validate_conversion(
    value: Any, source: str, entity: str
) -> tuple[
    tuple[tuple[int, int], tuple[int, int]] | None,
    list[ValidationIssue],
]:
    issues: list[ValidationIssue] = []
    if not isinstance(value, dict) or set(value) != {"multiplier", "offset"}:
        return None, [
            ValidationIssue(
                source,
                entity,
                "CONVERSION_STRUCTURE",
                "conversion_to_base must contain multiplier and offset",
            )
        ]
    multiplier, multiplier_issues = rational_tuple(
        value.get("multiplier"),
        source,
        entity,
        "multiplier",
        True,
    )
    offset, offset_issues = rational_tuple(
        value.get("offset"),
        source,
        entity,
        "offset",
        False,
    )
    issues.extend(multiplier_issues)
    issues.extend(offset_issues)
    if multiplier is None or offset is None:
        return None, issues
    return (multiplier, offset), issues


def validate_precision(
    value: Any, source: str, entity: str
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if not isinstance(value, dict) or set(value) != {
        "maximum_decimal_places",
        "rounding_mode",
    }:
        return [
            ValidationIssue(
                source,
                entity,
                "PRECISION_STRUCTURE",
                "precision must contain maximum_decimal_places and rounding_mode",
            )
        ]
    places = value.get("maximum_decimal_places")
    if (
        not isinstance(places, int)
        or isinstance(places, bool)
        or not 0 <= places <= 12
    ):
        issues.append(
            ValidationIssue(
                source,
                entity,
                "PRECISION_RANGE",
                "maximum_decimal_places must be an integer from 0 through 12",
            )
        )
    if value.get("rounding_mode") != "HALF_EVEN":
        issues.append(
            ValidationIssue(
                source,
                entity,
                "ROUNDING_MODE",
                "rounding_mode must be HALF_EVEN",
            )
        )
    return issues


def detect_cycles(
    units: dict[str, dict[str, Any]], source: str
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    reported: set[tuple[str, ...]] = set()
    for start in sorted(units):
        path: list[str] = []
        positions: dict[str, int] = {}
        current = start
        while current in units:
            if current in positions:
                cycle = path[positions[current] :]
                if len(cycle) == 1 and units[current].get("is_base_unit") is True:
                    break
                signature = tuple(sorted(cycle))
                if signature not in reported:
                    reported.add(signature)
                    issues.append(
                        ValidationIssue(
                            source,
                            current,
                            "UNIT_BASE_CYCLE",
                            f"cyclic base-unit relationship: {' -> '.join(cycle + [current])}",
                        )
                    )
                break
            positions[current] = len(path)
            path.append(current)
            next_unit = units[current].get("base_unit_id")
            if not isinstance(next_unit, str) or next_unit == current:
                break
            current = next_unit
    return issues


def validate_bundle(
    value: Any, source: str, definitions: Definitions
) -> BundleResult:
    issues: list[ValidationIssue] = []

    def add(entity: str, code: str, message: str) -> None:
        issues.append(ValidationIssue(source, entity, code, message))

    if not isinstance(value, dict) or set(value) != {
        "contract_version",
        "dimensions",
        "units",
    }:
        add(
            "<foundation>",
            "FOUNDATION_STRUCTURE",
            "foundation must contain contract_version, dimensions, and units",
        )
        return BundleResult(tuple(issues), {}, {})
    if value.get("contract_version") != definitions.contract_version:
        add(
            "<foundation>",
            "CONTRACT_VERSION_INCOMPATIBLE",
            f"foundation contract_version must be {definitions.contract_version}",
        )
    dimensions_value = value.get("dimensions")
    units_value = value.get("units")
    if not isinstance(dimensions_value, list) or not dimensions_value:
        add(
            "<foundation>",
            "DIMENSIONS_STRUCTURE",
            "dimensions must be a non-empty list",
        )
        dimensions_value = []
    if not isinstance(units_value, list) or not units_value:
        add("<foundation>", "UNITS_STRUCTURE", "units must be a non-empty list")
        units_value = []

    dimensions: dict[str, dict[str, Any]] = {}
    dimension_keys: set[str] = set()
    dimension_names: set[str] = set()
    for index, raw in enumerate(dimensions_value):
        entity = (
            raw.get("dimension_id")
            if isinstance(raw, dict) and nonempty_string(raw.get("dimension_id"))
            else f"<dimension:{index + 1}>"
        )
        if not isinstance(raw, dict):
            add(str(entity), "DIMENSION_TYPE", "dimension must be a mapping")
            continue
        record = raw
        issues.extend(
            validate_common(
                record,
                definitions.dimension_fields,
                source,
                str(entity),
                definitions,
            )
        )
        dimension_id = record.get("dimension_id")
        if dimension_id is not None:
            if not isinstance(
                dimension_id, str
            ) or not definitions.dimension_id_pattern.fullmatch(dimension_id):
                add(
                    str(entity),
                    "DIMENSION_ID_FORMAT",
                    "dimension_id violates canonical format",
                )
            elif dimension_id in dimensions:
                add(
                    str(entity),
                    "DUPLICATE_DIMENSION_ID",
                    f"duplicate dimension_id: {dimension_id}",
                )
            else:
                dimensions[dimension_id] = record
        dimension_key = record.get("dimension_key")
        if dimension_key is not None:
            if not isinstance(
                dimension_key, str
            ) or not definitions.dimension_key_pattern.fullmatch(dimension_key):
                add(
                    str(entity),
                    "DIMENSION_KEY_FORMAT",
                    "dimension_key must use lower_snake_case",
                )
            elif dimension_key in dimension_keys:
                add(
                    str(entity),
                    "DUPLICATE_DIMENSION_KEY",
                    f"duplicate dimension_key: {dimension_key}",
                )
            else:
                dimension_keys.add(dimension_key)
        name = record.get("canonical_name")
        if isinstance(name, str) and name.strip():
            normalized = normalized_token(name)
            if normalized in dimension_names:
                add(
                    str(entity),
                    "DUPLICATE_DIMENSION_NAME",
                    f"ambiguous canonical dimension name: {name}",
                )
            else:
                dimension_names.add(normalized)
        base_unit_id = record.get("base_unit_id")
        if base_unit_id is not None and (
            not isinstance(base_unit_id, str)
            or not definitions.unit_id_pattern.fullmatch(base_unit_id)
        ):
            add(
                str(entity),
                "BASE_UNIT_ID_FORMAT",
                "base_unit_id violates canonical Unit ID format",
            )

    units: dict[str, dict[str, Any]] = {}
    unit_keys: set[str] = set()
    unit_names: set[str] = set()
    symbols: set[str] = set()
    conversions: dict[
        str, tuple[tuple[int, int], tuple[int, int]] | None
    ] = {}
    for index, raw in enumerate(units_value):
        entity = (
            raw.get("unit_id")
            if isinstance(raw, dict) and nonempty_string(raw.get("unit_id"))
            else f"<unit:{index + 1}>"
        )
        if not isinstance(raw, dict):
            add(str(entity), "UNIT_TYPE", "Unit must be a mapping")
            continue
        record = raw
        issues.extend(
            validate_common(
                record,
                definitions.unit_fields,
                source,
                str(entity),
                definitions,
            )
        )
        unit_id = record.get("unit_id")
        if unit_id is not None:
            if not isinstance(
                unit_id, str
            ) or not definitions.unit_id_pattern.fullmatch(unit_id):
                add(str(entity), "UNIT_ID_FORMAT", "unit_id violates canonical format")
            elif unit_id in units:
                add(
                    str(entity),
                    "DUPLICATE_UNIT_ID",
                    f"duplicate unit_id: {unit_id}",
                )
            else:
                units[unit_id] = record
        unit_key = record.get("unit_key")
        if unit_key is not None:
            if not isinstance(
                unit_key, str
            ) or not definitions.unit_key_pattern.fullmatch(unit_key):
                add(
                    str(entity),
                    "UNIT_KEY_FORMAT",
                    "unit_key must use lower_snake_case",
                )
            elif unit_key in unit_keys:
                add(
                    str(entity),
                    "DUPLICATE_UNIT_KEY",
                    f"duplicate unit_key: {unit_key}",
                )
            else:
                unit_keys.add(unit_key)
        name = record.get("canonical_name")
        if isinstance(name, str) and name.strip():
            normalized = normalized_token(name)
            if normalized in unit_names:
                add(
                    str(entity),
                    "DUPLICATE_UNIT_NAME",
                    f"ambiguous canonical Unit name: {name}",
                )
            else:
                unit_names.add(normalized)
        symbol = record.get("symbol")
        if symbol is not None:
            if not isinstance(symbol, str) or not definitions.symbol_pattern.fullmatch(
                symbol
            ):
                add(
                    str(entity),
                    "UNIT_SYMBOL_FORMAT",
                    "symbol must be one non-whitespace token of 1-16 characters",
                )
            else:
                normalized_symbol = normalized_token(symbol)
                if normalized_symbol in symbols:
                    add(
                        str(entity),
                        "DUPLICATE_UNIT_SYMBOL",
                        f"ambiguous canonical Unit symbol: {symbol}",
                    )
                else:
                    symbols.add(normalized_symbol)
        dimension_id = record.get("dimension_id")
        if dimension_id is not None and (
            not isinstance(dimension_id, str)
            or not definitions.dimension_id_pattern.fullmatch(dimension_id)
        ):
            add(
                str(entity),
                "DIMENSION_ID_FORMAT",
                "dimension_id violates canonical format",
            )
        if "is_base_unit" in record and not isinstance(
            record.get("is_base_unit"), bool
        ):
            add(str(entity), "BASE_UNIT_FLAG", "is_base_unit must be boolean")
        base_unit_id = record.get("base_unit_id")
        if base_unit_id is not None and (
            not isinstance(base_unit_id, str)
            or not definitions.unit_id_pattern.fullmatch(base_unit_id)
        ):
            add(
                str(entity),
                "BASE_UNIT_ID_FORMAT",
                "base_unit_id violates canonical Unit ID format",
            )
        conversion, conversion_issues = validate_conversion(
            record.get("conversion_to_base"), source, str(entity)
        )
        issues.extend(conversion_issues)
        if isinstance(unit_id, str):
            conversions[unit_id] = conversion
        allowed = record.get("allowed_data_types")
        if not isinstance(allowed, list) or not allowed:
            add(
                str(entity),
                "UNIT_DATA_TYPES",
                "allowed_data_types must be a non-empty list",
            )
        else:
            if len(allowed) != len(set(str(item) for item in allowed)):
                add(
                    str(entity),
                    "DUPLICATE_UNIT_DATA_TYPE",
                    "allowed_data_types must be unique",
                )
            for data_type in allowed:
                if not isinstance(data_type, str) or data_type not in definitions.data_types:
                    add(
                        str(entity),
                        "UNKNOWN_UNIT_DATA_TYPE",
                        f"unknown allowed data type: {data_type}",
                    )
                elif definitions.data_types[data_type]["supports_units"] is not True:
                    add(
                        str(entity),
                        "UNIT_DATA_TYPE_UNSUPPORTED",
                        f"{data_type} does not support Units",
                    )
        issues.extend(validate_precision(record.get("precision"), source, str(entity)))

    for dimension_id, dimension in sorted(dimensions.items()):
        base_unit_id = dimension.get("base_unit_id")
        base_unit = units.get(base_unit_id) if isinstance(base_unit_id, str) else None
        if base_unit is None:
            add(
                dimension_id,
                "UNKNOWN_DIMENSION_BASE_UNIT",
                f"dimension base_unit_id does not resolve: {base_unit_id}",
            )
            continue
        if base_unit.get("dimension_id") != dimension_id:
            add(
                dimension_id,
                "CROSS_DIMENSION_BASE_UNIT",
                "dimension base Unit belongs to a different dimension",
            )
        if base_unit.get("is_base_unit") is not True:
            add(
                dimension_id,
                "DIMENSION_BASE_UNIT_NOT_BASE",
                "dimension base_unit_id must identify a base Unit",
            )
        base_count = sum(
            1
            for unit in units.values()
            if unit.get("dimension_id") == dimension_id
            and unit.get("is_base_unit") is True
        )
        if base_count != 1:
            add(
                dimension_id,
                "BASE_UNIT_COUNT",
                f"dimension must have exactly one base Unit; found {base_count}",
            )

    for unit_id, unit in sorted(units.items()):
        dimension_id = unit.get("dimension_id")
        dimension = dimensions.get(dimension_id) if isinstance(dimension_id, str) else None
        if dimension is None:
            add(
                unit_id,
                "UNKNOWN_UNIT_DIMENSION",
                f"Unit dimension_id does not resolve: {dimension_id}",
            )
        base_unit_id = unit.get("base_unit_id")
        base_unit = units.get(base_unit_id) if isinstance(base_unit_id, str) else None
        if base_unit is None:
            add(
                unit_id,
                "UNKNOWN_UNIT_BASE",
                f"Unit base_unit_id does not resolve: {base_unit_id}",
            )
            continue
        if base_unit.get("dimension_id") != dimension_id:
            add(
                unit_id,
                "CROSS_DIMENSION_UNIT_BASE",
                "Unit base reference crosses dimensions",
            )
        conversion = conversions.get(unit_id)
        if unit.get("is_base_unit") is True:
            if base_unit_id != unit_id:
                add(
                    unit_id,
                    "BASE_UNIT_SELF_REFERENCE",
                    "base Unit must reference itself",
                )
            if conversion is not None and conversion != ((1, 1), (0, 1)):
                add(
                    unit_id,
                    "BASE_CONVERSION_IDENTITY",
                    "base Unit conversion must be identity",
                )
        else:
            if base_unit_id == unit_id:
                add(
                    unit_id,
                    "NON_BASE_SELF_REFERENCE",
                    "non-base Unit must not reference itself",
                )
            if base_unit.get("is_base_unit") is not True:
                add(
                    unit_id,
                    "UNIT_BASE_NOT_BASE",
                    "non-base Unit must reference the dimension base Unit directly",
                )
            if dimension is not None and base_unit_id != dimension.get("base_unit_id"):
                add(
                    unit_id,
                    "UNIT_BASE_MISMATCH",
                    "non-base Unit must reference its dimension base Unit",
                )

    issues.extend(detect_cycles(units, source))
    return BundleResult(tuple(issues), dimensions, units)


def load_canonical_foundation() -> MeasurementFoundation:
    definitions = load_definitions()
    dimensions_registry, dimensions_parser = load_yaml(
        DIMENSIONS_PATH, "Measurement dimensions"
    )
    units_registry, units_parser = load_yaml(UNITS_PATH, "Attribute Units")
    dimensions_mapping = require_mapping(
        dimensions_registry, "Measurement dimension registry"
    )
    units_mapping = require_mapping(units_registry, "Attribute Unit registry")
    require_exact_keys(
        dimensions_mapping,
        {"registry_id", "registry_version", "contract_version", "dimensions"},
        "Measurement dimension registry",
    )
    require_exact_keys(
        units_mapping,
        {"registry_id", "registry_version", "contract_version", "units"},
        "Attribute Unit registry",
    )
    if dimensions_mapping["registry_id"] != "measurement-dimensions":
        raise MeasurementDefinitionError(
            "Measurement dimension registry_id must be measurement-dimensions"
        )
    if units_mapping["registry_id"] != "attribute-units":
        raise MeasurementDefinitionError(
            "Attribute Unit registry_id must be attribute-units"
        )
    require_semver(
        dimensions_mapping["registry_version"],
        "Measurement dimension registry_version",
    )
    require_semver(units_mapping["registry_version"], "Attribute Unit registry_version")
    if (
        dimensions_mapping["contract_version"] != definitions.contract_version
        or units_mapping["contract_version"] != definitions.contract_version
    ):
        raise MeasurementDefinitionError(
            "Measurement registry contract_version is incompatible"
        )
    bundle = {
        "contract_version": definitions.contract_version,
        "dimensions": dimensions_mapping["dimensions"],
        "units": units_mapping["units"],
    }
    result = validate_bundle(bundle, "<canonical>", definitions)
    if result.issues:
        rendered = "\n".join(issue.render() for issue in result.issues)
        raise MeasurementDefinitionError(
            f"canonical measurement foundation is invalid:\n{rendered}"
        )
    return MeasurementFoundation(
        contract_version=definitions.contract_version,
        dimensions=result.dimensions,
        units=result.units,
        parser_sources=definitions.parser_sources
        + (dimensions_parser, units_parser),
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate canonical or synthetic measurement foundations."
    )
    parser.add_argument(
        "source",
        nargs="?",
        default="canonical",
        help="YAML fixture path, '-' for stdin, or canonical",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if args.source == "canonical":
            foundation = load_canonical_foundation()
            parsers = sorted(set(foundation.parser_sources))
            print(
                "VALIDATION PASSED: canonical measurement foundation "
                f"({len(foundation.dimensions)} dimensions; {len(foundation.units)} Units; "
                f"parser={'; '.join(parsers)})"
            )
            return 0
        definitions = load_definitions()
        if args.source == "-":
            source = "<stdin>"
            value, fixture_parser = parse_yaml(sys.stdin.read(), source)
        else:
            source = args.source
            value, fixture_parser = load_yaml(Path(args.source), source)
        result = validate_bundle(value, source, definitions)
    except (MeasurementDefinitionError, OSError, TypeError, ValueError) as exc:
        print(f"VALIDATION CONFIGURATION FAILED: {exc}", file=sys.stderr)
        return 2

    if result.issues:
        print(f"VALIDATION FAILED: {len(result.issues)} issue(s)", file=sys.stderr)
        for issue in result.issues:
            print(issue.render(), file=sys.stderr)
        return 1

    parsers = sorted(set(definitions.parser_sources + (fixture_parser,)))
    print(
        f"VALIDATION PASSED: {source} "
        f"({len(result.dimensions)} dimensions; {len(result.units)} Units; "
        f"parser={'; '.join(parsers)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
