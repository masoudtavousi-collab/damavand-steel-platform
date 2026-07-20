#!/usr/bin/env python3
"""Deterministic offline validation for Wave 2A Product core records."""

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
CONTRACT_PATH = ROOT / "repository/data/contracts/product-core.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/product-core.schema.json"
ENTITY_TYPES_PATH = ROOT / "repository/data/registries/product-entity-types.yaml"
STATUSES_PATH = ROOT / "repository/data/registries/product-statuses.yaml"

SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
MACHINE_CODE_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]*$")
OWNER_ROLE_PATTERN = re.compile(r"^[a-z][a-z0-9-]{2,63}$")
CAPTURED_BY_PATTERN = re.compile(r"^role:[a-z][a-z0-9-]{2,63}$")

EXPECTED_ENTITY_TYPES = {
    "CATALOG": (1, None, "PLATFORM", True, False),
    "PLATFORM": (2, "CATALOG", "FAMILY", False, False),
    "FAMILY": (3, "PLATFORM", "SERIES", False, False),
    "SERIES": (4, "FAMILY", "VARIANT_RULE_SET", False, False),
    "VARIANT_RULE_SET": (5, "SERIES", "SKU", False, False),
    "SKU": (6, "VARIANT_RULE_SET", None, False, True),
}
EXPECTED_STATUSES = {
    "APPROVED": (True, False, False, False, False),
    "CANDIDATE_UNVERIFIED": (False, False, False, False, False),
    "MISSING_DATA_VALUE": (False, False, False, False, False),
    "FOUNDER_INPUT_REQUIRED": (False, False, False, True, False),
    "DEFERRED": (False, False, False, False, False),
    "NOT_APPLICABLE": (False, False, False, False, True),
    "INVALID": (False, False, False, False, True),
}
ENTITY_REGISTRY_FIELDS = {
    "code",
    "hierarchy_position",
    "allowed_parent_type",
    "allowed_child_type",
    "may_be_hierarchy_root",
    "derived",
    "description",
}
STATUS_REGISTRY_FIELDS = {
    "code",
    "meaning",
    "allowed_use",
    "represents_approved_factual_data",
    "may_be_published_by_status_alone",
    "may_be_imported_by_status_alone",
    "founder_action_required",
    "terminal",
}


class DefinitionError(ValueError):
    """Raised when a core contract definition is missing or inconsistent."""


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
    entity_types: dict[str, dict[str, Any]]
    statuses: set[str]
    entity_id_pattern: re.Pattern[str]
    required_fields: set[str]
    parent_fields: set[str]
    prohibited_fields: set[str]
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


def load_yaml_file(path: Path, label: str) -> tuple[Any, str]:
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
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise DefinitionError(f"{label} keys differ; missing={missing}, extra={extra}")


def validate_entity_registry(value: Any) -> dict[str, dict[str, Any]]:
    registry = require_mapping(value, "entity-type registry")
    if registry.get("registry_id") != "product-entity-types":
        raise DefinitionError("entity-type registry_id must be product-entity-types")
    if not SEMVER_PATTERN.fullmatch(str(registry.get("registry_version", ""))):
        raise DefinitionError("entity-type registry_version must use semantic-version core")
    entries = registry.get("entity_types")
    if not isinstance(entries, list):
        raise DefinitionError("entity_types must be a list")
    by_code: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(entries):
        entry = require_mapping(item, f"entity_types[{index}]")
        require_exact_keys(entry, ENTITY_REGISTRY_FIELDS, f"entity_types[{index}]")
        code = entry.get("code")
        if not isinstance(code, str) or code in by_code:
            raise DefinitionError(f"entity_types[{index}] has an invalid or duplicate code")
        if not isinstance(entry.get("description"), str) or not entry["description"].strip():
            raise DefinitionError(f"entity type {code} requires a description")
        by_code[code] = entry
    if set(by_code) != set(EXPECTED_ENTITY_TYPES):
        raise DefinitionError(
            "entity registry must contain exactly: "
            + ", ".join(EXPECTED_ENTITY_TYPES)
        )
    for code, expected in EXPECTED_ENTITY_TYPES.items():
        entry = by_code[code]
        actual = (
            entry["hierarchy_position"],
            entry["allowed_parent_type"],
            entry["allowed_child_type"],
            entry["may_be_hierarchy_root"],
            entry["derived"],
        )
        if actual != expected:
            raise DefinitionError(f"entity registry semantics differ for {code}")
    return by_code


def validate_status_registry(value: Any) -> set[str]:
    registry = require_mapping(value, "status registry")
    if registry.get("registry_id") != "product-statuses":
        raise DefinitionError("status registry_id must be product-statuses")
    if not SEMVER_PATTERN.fullmatch(str(registry.get("registry_version", ""))):
        raise DefinitionError("status registry_version must use semantic-version core")
    entries = registry.get("statuses")
    if not isinstance(entries, list):
        raise DefinitionError("statuses must be a list")
    by_code: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(entries):
        entry = require_mapping(item, f"statuses[{index}]")
        require_exact_keys(entry, STATUS_REGISTRY_FIELDS, f"statuses[{index}]")
        code = entry.get("code")
        if not isinstance(code, str) or code in by_code:
            raise DefinitionError(f"statuses[{index}] has an invalid or duplicate code")
        if not isinstance(entry.get("meaning"), str) or not entry["meaning"].strip():
            raise DefinitionError(f"status {code} requires a meaning")
        if not isinstance(entry.get("allowed_use"), str) or not entry["allowed_use"].strip():
            raise DefinitionError(f"status {code} requires allowed_use guidance")
        by_code[code] = entry
    if set(by_code) != set(EXPECTED_STATUSES):
        raise DefinitionError(
            "status registry must contain exactly: " + ", ".join(EXPECTED_STATUSES)
        )
    for code, expected in EXPECTED_STATUSES.items():
        entry = by_code[code]
        actual = (
            entry["represents_approved_factual_data"],
            entry["may_be_published_by_status_alone"],
            entry["may_be_imported_by_status_alone"],
            entry["founder_action_required"],
            entry["terminal"],
        )
        if actual != expected or not all(isinstance(item, bool) for item in actual):
            raise DefinitionError(f"status registry semantics differ for {code}")
    return set(by_code)


def validate_contract_and_schema(
    contract_value: Any,
    schema_value: Any,
    entity_types: dict[str, dict[str, Any]],
    statuses: set[str],
) -> tuple[str, re.Pattern[str], set[str], set[str], set[str]]:
    contract = require_mapping(contract_value, "Product core contract")
    if contract.get("contract_id") != "product-core":
        raise DefinitionError("contract_id must be product-core")
    contract_version = contract.get("contract_version")
    if not isinstance(contract_version, str) or not SEMVER_PATTERN.fullmatch(contract_version):
        raise DefinitionError("contract_version must use semantic-version core")
    required_fields = set(contract.get("always_required_record_fields", []))
    expected_required = {
        "contract_version",
        "entity_id",
        "entity_type",
        "canonical_label",
        "status",
        "owner",
        "provenance",
        "record_version",
    }
    if required_fields != expected_required:
        raise DefinitionError("contract always-required fields differ from the approved set")
    parent_fields = set(contract.get("conditional_parent_fields", []))
    if parent_fields != {"parent_entity_id", "parent_entity_type"}:
        raise DefinitionError("contract conditional parent fields differ from the approved set")
    identity = require_mapping(contract.get("stable_identity"), "stable_identity")
    try:
        entity_id_pattern = re.compile(str(identity["pattern"]))
    except (KeyError, re.error) as exc:
        raise DefinitionError("stable_identity pattern is missing or invalid") from exc
    prohibited = contract.get("prohibited_fact_fields")
    if not isinstance(prohibited, list) or not prohibited:
        raise DefinitionError("prohibited_fact_fields must be a non-empty list")
    prohibited_fields = {str(item) for item in prohibited}

    hierarchy = contract.get("hierarchy")
    if not isinstance(hierarchy, list) or len(hierarchy) != len(EXPECTED_ENTITY_TYPES):
        raise DefinitionError("contract hierarchy must contain exactly six entries")
    hierarchy_by_type = {
        item.get("entity_type"): item
        for item in hierarchy
        if isinstance(item, dict) and isinstance(item.get("entity_type"), str)
    }
    if set(hierarchy_by_type) != set(EXPECTED_ENTITY_TYPES):
        raise DefinitionError("contract hierarchy entity types differ from the approved set")
    for code, registry_entry in entity_types.items():
        item = hierarchy_by_type[code]
        actual = (
            item.get("position"),
            item.get("parent_type"),
            item.get("child_type"),
            item.get("hierarchy_root"),
            item.get("derived"),
        )
        expected = (
            registry_entry["hierarchy_position"],
            registry_entry["allowed_parent_type"],
            registry_entry["allowed_child_type"],
            registry_entry["may_be_hierarchy_root"],
            registry_entry["derived"],
        )
        if actual != expected:
            raise DefinitionError(f"contract hierarchy differs from the registry for {code}")

    schema = require_mapping(schema_value, "Product core JSON Schema")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise DefinitionError("JSON Schema must declare draft 2020-12")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise DefinitionError("JSON Schema must be a closed object schema")
    if set(schema.get("required", [])) != required_fields:
        raise DefinitionError("JSON Schema required fields differ from the contract")
    properties = require_mapping(schema.get("properties"), "JSON Schema properties")
    if set(properties) != required_fields | parent_fields:
        raise DefinitionError("JSON Schema properties differ from the approved field set")
    if properties.get("contract_version", {}).get("const") != contract_version:
        raise DefinitionError("JSON Schema contract_version differs from the contract")
    if properties.get("entity_id", {}).get("pattern") != identity.get("pattern"):
        raise DefinitionError("JSON Schema entity_id pattern differs from the contract")
    if set(properties.get("entity_type", {}).get("enum", [])) != set(entity_types):
        raise DefinitionError("JSON Schema entity types differ from the registry")
    if set(properties.get("status", {}).get("enum", [])) != statuses:
        raise DefinitionError("JSON Schema statuses differ from the registry")
    if not isinstance(schema.get("allOf"), list) or len(schema["allOf"]) != 7:
        raise DefinitionError("JSON Schema must encode root and parent-field conditions")
    return (
        contract_version,
        entity_id_pattern,
        required_fields,
        parent_fields,
        prohibited_fields,
    )


def load_definitions() -> Definitions:
    contract, contract_parser = load_yaml_file(CONTRACT_PATH, "Product core contract")
    entity_registry, entity_parser = load_yaml_file(
        ENTITY_TYPES_PATH, "Product entity-type registry"
    )
    status_registry, status_parser = load_yaml_file(
        STATUSES_PATH, "Product status registry"
    )
    schema = load_json(SCHEMA_PATH, "Product core JSON Schema")
    entity_types = validate_entity_registry(entity_registry)
    statuses = validate_status_registry(status_registry)
    (
        contract_version,
        entity_id_pattern,
        required_fields,
        parent_fields,
        prohibited_fields,
    ) = validate_contract_and_schema(contract, schema, entity_types, statuses)
    return Definitions(
        contract_version=contract_version,
        entity_types=entity_types,
        statuses=statuses,
        entity_id_pattern=entity_id_pattern,
        required_fields=required_fields,
        parent_fields=parent_fields,
        prohibited_fields=prohibited_fields,
        parser_sources=(contract_parser, entity_parser, status_parser),
    )


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_rfc3339_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return parsed.tzinfo is not None


def iter_mapping_keys(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            if isinstance(key, str):
                yield key
            yield from iter_mapping_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_mapping_keys(child)


def entity_label(record: Any, index: int) -> str:
    if isinstance(record, dict) and is_nonempty_string(record.get("entity_id")):
        return str(record["entity_id"])
    return f"<record:{index}>"


def validate_dataset(
    value: Any, source: str, definitions: Definitions
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    def add(entity: str, code: str, message: str) -> None:
        issues.append(ValidationIssue(source, entity, code, message))

    if not isinstance(value, list):
        add("<dataset>", "DATASET_TYPE", "fixture must contain a YAML sequence of records")
        return issues
    if not value:
        add("<dataset>", "EMPTY_DATASET", "fixture must contain at least one record")
        return issues

    allowed_fields = definitions.required_fields | definitions.parent_fields
    records_by_id: dict[str, dict[str, Any]] = {}
    record_order: list[tuple[str, dict[str, Any]]] = []

    for index, raw_record in enumerate(value, start=1):
        entity = entity_label(raw_record, index)
        if not isinstance(raw_record, dict):
            add(entity, "RECORD_TYPE", "record must be a mapping")
            continue
        record = raw_record

        non_string_keys = [key for key in record if not isinstance(key, str)]
        for key in non_string_keys:
            add(entity, "FIELD_NAME_TYPE", f"field name must be a string: {key!r}")
        for key in sorted({key for key in record if isinstance(key, str)} - allowed_fields):
            add(entity, "UNEXPECTED_FIELD", f"unexpected top-level field: {key}")
        prohibited_found = sorted(
            {key for key in iter_mapping_keys(record) if key in definitions.prohibited_fields}
        )
        for key in prohibited_found:
            add(entity, "PROHIBITED_FIELD", f"prohibited Product or adapter field: {key}")

        for field in sorted(definitions.required_fields):
            if field not in record:
                code = "MISSING_PROVENANCE" if field == "provenance" else "MISSING_REQUIRED_FIELD"
                add(entity, code, f"missing required field: {field}")

        contract_version = record.get("contract_version")
        if contract_version is not None:
            if not isinstance(contract_version, str) or not SEMVER_PATTERN.fullmatch(
                contract_version
            ):
                add(entity, "CONTRACT_VERSION_FORMAT", "contract_version must use X.Y.Z")
            elif contract_version != definitions.contract_version:
                add(
                    entity,
                    "CONTRACT_VERSION_INCOMPATIBLE",
                    f"contract_version must be {definitions.contract_version}",
                )

        record_version = record.get("record_version")
        if record_version is not None and (
            not isinstance(record_version, str)
            or not SEMVER_PATTERN.fullmatch(record_version)
        ):
            add(entity, "RECORD_VERSION_FORMAT", "record_version must use X.Y.Z")

        entity_id = record.get("entity_id")
        entity_type = record.get("entity_type")
        if entity_id is not None:
            if not isinstance(entity_id, str) or not definitions.entity_id_pattern.fullmatch(
                entity_id
            ):
                add(entity, "ENTITY_ID_FORMAT", "entity_id does not match the stable ID format")
            elif isinstance(entity_type, str) and entity_type in definitions.entity_types:
                expected_segment = entity_type.lower().replace("_", "-")
                if entity_id.split(":", 2)[1] != expected_segment:
                    add(
                        entity,
                        "ENTITY_ID_TYPE_MISMATCH",
                        "entity_id type segment does not match entity_type",
                    )
            if isinstance(entity_id, str):
                if entity_id in records_by_id:
                    add(entity, "DUPLICATE_ENTITY_ID", f"duplicate entity_id: {entity_id}")
                else:
                    records_by_id[entity_id] = record
                    record_order.append((entity_id, record))

        if entity_type is not None and (
            not isinstance(entity_type, str)
            or entity_type not in definitions.entity_types
        ):
            add(entity, "UNKNOWN_ENTITY_TYPE", f"unknown entity_type: {entity_type}")

        status = record.get("status")
        if status is not None and (
            not isinstance(status, str) or status not in definitions.statuses
        ):
            add(entity, "UNKNOWN_STATUS", f"unknown status: {status}")
        elif status == "INVALID":
            add(
                entity,
                "INVALID_STATUS_BLOCK",
                "INVALID status blocks further processing until correction and revalidation",
            )

        label = record.get("canonical_label")
        if label is not None and (
            not is_nonempty_string(label) or len(str(label)) > 200
        ):
            add(entity, "CANONICAL_LABEL", "canonical_label must be 1-200 non-blank characters")

        owner = record.get("owner")
        if owner is not None:
            if not isinstance(owner, dict) or not owner:
                add(entity, "OWNER_STRUCTURE", "owner must be a non-empty mapping")
            else:
                if set(owner) != {"role"}:
                    add(entity, "OWNER_STRUCTURE", "owner must contain only the role field")
                role = owner.get("role")
                if not isinstance(role, str) or not OWNER_ROLE_PATTERN.fullmatch(role):
                    add(entity, "OWNER_ROLE", "owner.role must be a stable machine role")

        provenance = record.get("provenance")
        provenance_fields = {
            "source_type",
            "source_reference",
            "captured_by",
            "captured_at",
            "evidence_status",
        }
        if provenance is not None:
            if not isinstance(provenance, dict) or not provenance:
                add(entity, "EMPTY_PROVENANCE", "provenance must be a non-empty mapping")
            else:
                missing = sorted(provenance_fields - set(provenance))
                extra = sorted(set(provenance) - provenance_fields)
                for field in missing:
                    add(entity, "MISSING_PROVENANCE", f"missing provenance field: {field}")
                for field in extra:
                    add(entity, "PROVENANCE_STRUCTURE", f"unexpected provenance field: {field}")
                source_type = provenance.get("source_type")
                if source_type is not None and (
                    not isinstance(source_type, str)
                    or not MACHINE_CODE_PATTERN.fullmatch(source_type)
                ):
                    add(entity, "PROVENANCE_SOURCE_TYPE", "source_type must be a machine code")
                if "source_reference" in provenance:
                    source_reference = provenance.get("source_reference")
                    if not is_nonempty_string(source_reference) or len(
                        str(source_reference)
                    ) > 500:
                        add(
                            entity,
                            "PROVENANCE_SOURCE_REFERENCE",
                            "source_reference must be 1-500 non-blank characters",
                        )
                captured_by = provenance.get("captured_by")
                if captured_by is not None and (
                    not isinstance(captured_by, str)
                    or not CAPTURED_BY_PATTERN.fullmatch(captured_by)
                ):
                    add(entity, "PROVENANCE_CAPTURED_BY", "captured_by must identify a role")
                if "captured_at" in provenance and not is_rfc3339_datetime(
                    provenance.get("captured_at")
                ):
                    add(entity, "PROVENANCE_CAPTURED_AT", "captured_at must be RFC 3339 UTC")
                evidence_status = provenance.get("evidence_status")
                if evidence_status is not None and (
                    not isinstance(evidence_status, str)
                    or not MACHINE_CODE_PATTERN.fullmatch(evidence_status)
                ):
                    add(
                        entity,
                        "PROVENANCE_EVIDENCE_STATUS",
                        "evidence_status must be a machine code distinct from lifecycle status",
                    )

        if entity_type in definitions.entity_types:
            expected_parent = definitions.entity_types[entity_type]["allowed_parent_type"]
            has_parent_id = "parent_entity_id" in record
            has_parent_type = "parent_entity_type" in record
            if expected_parent is None:
                if has_parent_id or has_parent_type:
                    add(entity, "ROOT_RULE", "CATALOG must not declare a parent")
            else:
                if not has_parent_id:
                    add(entity, "MISSING_PARENT", "non-root entity requires parent_entity_id")
                if not has_parent_type:
                    add(entity, "MISSING_PARENT", "non-root entity requires parent_entity_type")
                declared_parent_type = record.get("parent_entity_type")
                if declared_parent_type is not None and declared_parent_type != expected_parent:
                    add(
                        entity,
                        "PARENT_TYPE_MISMATCH",
                        f"parent_entity_type must be {expected_parent} for {entity_type}",
                    )
                    if declared_parent_type in definitions.entity_types:
                        parent_position = definitions.entity_types[declared_parent_type][
                            "hierarchy_position"
                        ]
                        child_position = definitions.entity_types[entity_type][
                            "hierarchy_position"
                        ]
                        if child_position - parent_position > 1:
                            add(
                                entity,
                                "SKIPPED_HIERARCHY_LEVEL",
                                f"{declared_parent_type} cannot directly parent {entity_type}",
                            )

        parent_id = record.get("parent_entity_id")
        parent_type = record.get("parent_entity_type")
        if parent_id is not None and (
            not isinstance(parent_id, str)
            or not definitions.entity_id_pattern.fullmatch(parent_id)
        ):
            add(entity, "PARENT_ID_FORMAT", "parent_entity_id does not match the stable ID format")
        if parent_type is not None and (
            not isinstance(parent_type, str)
            or parent_type not in definitions.entity_types
        ):
            add(entity, "UNKNOWN_PARENT_TYPE", f"unknown parent_entity_type: {parent_type}")

    for entity_id, record in record_order:
        parent_id = record.get("parent_entity_id")
        if not isinstance(parent_id, str):
            continue
        if parent_id == entity_id:
            add(entity_id, "SELF_REFERENCE", "entity cannot reference itself as parent")
            continue
        parent = records_by_id.get(parent_id)
        if parent is None:
            add(entity_id, "UNKNOWN_PARENT", f"parent_entity_id does not exist: {parent_id}")
            continue
        declared_parent_type = record.get("parent_entity_type")
        actual_parent_type = parent.get("entity_type")
        if declared_parent_type != actual_parent_type:
            add(
                entity_id,
                "PARENT_REFERENCE_TYPE_MISMATCH",
                f"parent record is {actual_parent_type}, not {declared_parent_type}",
            )

    parent_by_id = {
        entity_id: record.get("parent_entity_id")
        for entity_id, record in record_order
        if isinstance(record.get("parent_entity_id"), str)
        and record.get("parent_entity_id") in records_by_id
    }
    state: dict[str, int] = {entity_id: 0 for entity_id in records_by_id}
    stack: list[str] = []
    reported_cycles: set[tuple[str, ...]] = set()

    def visit(entity_id: str) -> None:
        state[entity_id] = 1
        stack.append(entity_id)
        parent_id = parent_by_id.get(entity_id)
        if isinstance(parent_id, str):
            if state[parent_id] == 0:
                visit(parent_id)
            elif state[parent_id] == 1:
                start = stack.index(parent_id)
                cycle_nodes = stack[start:]
                cycle_key = tuple(sorted(cycle_nodes))
                if cycle_key not in reported_cycles:
                    reported_cycles.add(cycle_key)
                    cycle_path = " -> ".join(cycle_nodes + [parent_id])
                    add(entity_id, "ANCESTRY_CYCLE", f"ancestry cycle detected: {cycle_path}")
        stack.pop()
        state[entity_id] = 2

    for entity_id in records_by_id:
        if state[entity_id] == 0:
            visit(entity_id)

    return issues


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a YAML sequence of canonical Product core entity records."
    )
    parser.add_argument("source", help="YAML fixture path, or '-' to read YAML from stdin")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        definitions = load_definitions()
        if args.source == "-":
            source = "<stdin>"
            raw = sys.stdin.read()
            value, fixture_parser = parse_yaml(raw, source)
        else:
            source_path = Path(args.source)
            source = str(source_path)
            value, fixture_parser = load_yaml_file(source_path, source)
        issues = validate_dataset(value, source, definitions)
    except (DefinitionError, OSError, TypeError, ValueError) as exc:
        print(f"VALIDATION CONFIGURATION FAILED: {exc}", file=sys.stderr)
        return 2

    if issues:
        print(f"VALIDATION FAILED: {len(issues)} issue(s)", file=sys.stderr)
        for issue in issues:
            print(issue.render(), file=sys.stderr)
        return 1

    parser_sources = sorted(set(definitions.parser_sources + (fixture_parser,)))
    print(
        f"VALIDATION PASSED: {source} ({len(value)} records; "
        f"parser={'; '.join(parser_sources)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
