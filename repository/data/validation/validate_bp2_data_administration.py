#!/usr/bin/env python3
"""Deterministic offline validation for the BP2 data administration contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, NoReturn, Sequence

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = (
    ROOT / "repository/data/contracts/bp2-data-administration-v1.0.json"
)
SCHEMA_PATH = (
    ROOT / "repository/data/schemas/bp2-data-administration-v1.0.schema.json"
)
SOURCE_PATH = ROOT / "repository/data/contracts/bp2-pipe-data-blueprint-v0.1.json"

EXPECTED_SCHEMA_DRAFT = "https://json-schema.org/draft/2020-12/schema"
EXPECTED_SCHEMA_ID = "urn:damavand-steel:schema:bp2-data-administration:1.0.0"
EXPECTED_SOURCE_PATH = (
    "repository/data/contracts/bp2-pipe-data-blueprint-v0.1.json"
)
EXPECTED_HIERARCHY = [
    "CATALOG",
    "PLATFORM",
    "FAMILY",
    "SERIES",
    "VARIANT_RULE_SET",
    "SKU",
]
EXPECTED_STATUSES = [
    "APPROVED",
    "CANDIDATE_UNVERIFIED",
    "MISSING_DATA_VALUE",
    "FOUNDER_INPUT_REQUIRED",
    "DEFERRED",
    "NOT_APPLICABLE",
    "INVALID",
]
EXPECTED_REGISTRIES = [
    "MATERIAL",
    "GRADE",
    "DIAMETER_SIZE",
    "THICKNESS",
    "COLOR_FINISH",
    "SURFACE_DESIGN",
    "BRANCH_LENGTH",
    "SALES_CALCULATION_UNITS",
    "SUPPLY_STATUS",
    "VALID_COMBINATION_RULES",
    "PILOT_COMBINATIONS",
    "PROVENANCE_EVIDENCE",
]
EXPECTED_ACTIONS = ["ADD", "EDIT", "DELETE_OR_ARCHIVE"]
EXPECTED_AUDIT_FIELDS = [
    "actor",
    "occurred_at",
    "reason",
    "before_snapshot",
    "after_snapshot",
    "evidence_reference",
]
EXPECTED_INQUIRY_SEQUENCE = [
    "FAMILY",
    "MATERIAL",
    "GRADE",
    "DIAMETER_SIZE",
    "VALID_THICKNESS",
    "COLOR_FINISH",
    "SURFACE_DESIGN",
    "LENGTH",
]
EXPECTED_ADMIN_COMPONENTS = [
    "REGISTRY_COUNTS",
    "STATUS_FILTERS",
    "SEARCH",
    "ADD_EDIT_ARCHIVE",
    "DEPENDENCY_PREVIEW",
    "COMBINATION_PREVIEW",
    "AUDIT_LOG",
    "FOUNDER_APPROVAL_QUEUE",
]
EXPECTED_STOP_CONDITIONS = [
    "ADMIN_UI_IMPLEMENTATION",
    "PRODUCT_OR_SKU_MUTATION",
    "WORDPRESS_OR_WOOCOMMERCE_CHANGE",
    "DATA_IMPORT",
    "PUBLICATION",
    "DEPLOYMENT",
    "CANDIDATE_PROMOTION",
    "SCOPE_EXPANSION",
]
EXPECTED_SOURCE_GRADES = {
    "201": "APPROVED",
    "304": "APPROVED",
    "316": "CANDIDATE_UNVERIFIED",
    "430": "CANDIDATE_UNVERIFIED",
}
EXPECTED_SOURCE_LENGTHS = {3: "APPROVED", 6: "APPROVED"}
EXPECTED_SOURCE_PILOTS = {
    (
        "PIPE-COMB-0001",
        "GOLD-PIPE-201-16-035-6M",
        False,
        "201",
        "SILVER",
        16,
        0.35,
        6,
        "SUPPLY_AFTER_INQUIRY",
        "APPROVED",
    ),
    (
        "PIPE-COMB-0016",
        "GOLD-PIPE-201-38-050-6M",
        False,
        "201",
        "SILVER",
        38,
        0.5,
        6,
        "SUPPLY_AFTER_INQUIRY",
        "APPROVED",
    ),
    (
        "PIPE-COMB-0023",
        "GOLD-PIPE-201-51-050-6M",
        False,
        "201",
        "SILVER",
        51,
        0.5,
        6,
        "SUPPLY_AFTER_INQUIRY",
        "APPROVED",
    ),
}
LIFECYCLE_DECISION_ID = "FD-BP2-ADM-001"
LIFECYCLE_REVIEW_RECORD_ID = "BP2-ADM-REVIEW-001"
LIFECYCLE_REVIEWERS = [
    "CHIEF_ARCHITECT_PRODUCT_OWNER_QA",
    "REPOSITORY_GUARDIAN",
]
LIFECYCLE_EVIDENCE_REFERENCE = (
    "docs/17_FOUNDER_DECISION_LOG.md"
    "#bp2-data-administration-lifecycle-decision"
)
EXPECTED_LIFECYCLE_HISTORY = [
    {
        "from": "DRAFT",
        "to": "REVIEW",
        "decided_by": "FOUNDER",
        "decided_on": "2026-07-28",
        "decision_id": LIFECYCLE_DECISION_ID,
        "evidence_reference": LIFECYCLE_EVIDENCE_REFERENCE,
    }
]

ROOT_FIELDS = {
    "contract_id",
    "contract_version",
    "lifecycle",
    "scope",
    "source_contract",
    "canonical_hierarchy",
    "status_vocabulary",
    "registries",
    "registry_capabilities",
    "governance",
    "smart_inquiry_sequence",
    "pipe_family_policy",
    "selection_policy",
    "future_admin_experience",
    "stop_conditions",
    "provenance",
}
OBJECT_FIELDS = {
    ("lifecycle",): {
        "status",
        "approval_authority",
        "implementation_authority",
        "decision_id",
        "review_record_id",
        "review_outcome",
        "reviewers",
        "transition_history",
    },
    ("scope",): {
        "phase",
        "documentation_only",
        "implements_admin_ui",
        "creates_products",
        "creates_skus",
        "changes_wordpress",
        "allows_import",
        "allows_publication",
        "allows_deployment",
    },
    ("source_contract",): {"path", "version"},
    ("registry_capabilities",): {
        "actions",
        "default_delete_mode",
        "dependency_check_required",
        "audit_required",
    },
    ("governance",): {
        "preserve_history",
        "cascade_delete",
        "approved_record_delete_requires_founder",
        "archive_is_governance_status",
        "physical_delete_policy",
        "audit_fields",
    },
    ("pipe_family_policy",): {
        "family_key",
        "administered_grades",
        "excluded_grades",
        "base_lengths_m",
        "custom_length",
        "sales_and_inquiry_unit",
        "calculation_unit",
        "thickness_in_product_name",
        "thickness_in_category",
        "cartesian_generation_forbidden",
        "approved_pilot_count",
        "candidate_count",
        "aluminum_and_iron_thickness",
        "sheet_administration",
    },
    ("selection_policy",): {
        "approved_combination_selectable",
        "candidate_selectable",
        "candidate_auto_promotion",
        "free_text_inquiry_allowed",
        "auto_creates_master_data",
        "auto_creates_product",
        "auto_creates_sku",
    },
    ("future_admin_experience",): {
        "locale",
        "direction",
        "mobile_first",
        "components",
        "implementation_authority",
    },
    ("provenance",): {
        "source_type",
        "source_reference",
        "captured_by",
        "captured_at",
        "evidence_status",
    },
}
EXPECTED_SCHEMA_CONSTS: dict[tuple[str, ...], Any] = {
    ("contract_id",): "bp2-data-administration",
    ("contract_version",): "1.0.0",
    ("lifecycle", "status"): "REVIEW",
    ("lifecycle", "approval_authority"): "FOUNDER",
    ("lifecycle", "implementation_authority"): False,
    ("lifecycle", "decision_id"): LIFECYCLE_DECISION_ID,
    ("lifecycle", "review_record_id"): LIFECYCLE_REVIEW_RECORD_ID,
    ("lifecycle", "review_outcome"): "IN_PROGRESS",
    ("lifecycle", "reviewers"): LIFECYCLE_REVIEWERS,
    ("lifecycle", "transition_history"): EXPECTED_LIFECYCLE_HISTORY,
    ("scope", "phase"): "BP2",
    ("scope", "documentation_only"): True,
    ("scope", "implements_admin_ui"): False,
    ("scope", "creates_products"): False,
    ("scope", "creates_skus"): False,
    ("scope", "changes_wordpress"): False,
    ("scope", "allows_import"): False,
    ("scope", "allows_publication"): False,
    ("scope", "allows_deployment"): False,
    ("source_contract", "path"): EXPECTED_SOURCE_PATH,
    ("source_contract", "version"): "0.1.0",
    ("canonical_hierarchy",): EXPECTED_HIERARCHY,
    ("status_vocabulary",): EXPECTED_STATUSES,
    ("registries",): EXPECTED_REGISTRIES,
    ("registry_capabilities", "actions"): EXPECTED_ACTIONS,
    ("registry_capabilities", "default_delete_mode"): "SOFT_DELETE",
    ("registry_capabilities", "dependency_check_required"): True,
    ("registry_capabilities", "audit_required"): True,
    ("governance", "preserve_history"): True,
    ("governance", "cascade_delete"): False,
    ("governance", "approved_record_delete_requires_founder"): True,
    ("governance", "archive_is_governance_status"): False,
    (
        "governance",
        "physical_delete_policy",
    ): "UNUSED_ERRONEOUS_DRAFT_WITH_AUDIT_ONLY",
    ("governance", "audit_fields"): EXPECTED_AUDIT_FIELDS,
    ("smart_inquiry_sequence",): EXPECTED_INQUIRY_SEQUENCE,
    ("pipe_family_policy", "family_key"): "decorative_stainless_steel_pipe",
    ("pipe_family_policy", "administered_grades"): ["201", "304", "316"],
    (
        "pipe_family_policy",
        "excluded_grades",
    ): [{"code": "430", "disposition": "DEFERRED"}],
    ("pipe_family_policy", "base_lengths_m"): [3, 6],
    ("pipe_family_policy", "custom_length"): "INQUIRY_ONLY",
    ("pipe_family_policy", "sales_and_inquiry_unit"): "BRANCH",
    ("pipe_family_policy", "calculation_unit"): "METER",
    ("pipe_family_policy", "thickness_in_product_name"): False,
    ("pipe_family_policy", "thickness_in_category"): False,
    ("pipe_family_policy", "cartesian_generation_forbidden"): True,
    ("pipe_family_policy", "approved_pilot_count"): 3,
    ("pipe_family_policy", "candidate_count"): 879,
    ("pipe_family_policy", "aluminum_and_iron_thickness"): "NOT_APPLICABLE",
    ("pipe_family_policy", "sheet_administration"): "DEFERRED",
    ("selection_policy", "approved_combination_selectable"): True,
    ("selection_policy", "candidate_selectable"): False,
    ("selection_policy", "candidate_auto_promotion"): False,
    ("selection_policy", "free_text_inquiry_allowed"): True,
    ("selection_policy", "auto_creates_master_data"): False,
    ("selection_policy", "auto_creates_product"): False,
    ("selection_policy", "auto_creates_sku"): False,
    ("future_admin_experience", "locale"): "fa-IR",
    ("future_admin_experience", "direction"): "RTL",
    ("future_admin_experience", "mobile_first"): True,
    ("future_admin_experience", "components"): EXPECTED_ADMIN_COMPONENTS,
    ("future_admin_experience", "implementation_authority"): False,
    ("stop_conditions",): EXPECTED_STOP_CONDITIONS,
    ("provenance", "source_type"): "FOUNDER_DECISIONS",
    (
        "provenance",
        "source_reference",
    ): "BP2 Data Administration Scope v1.0 authorization",
    ("provenance", "captured_by"): "role:project-governance",
    ("provenance", "captured_at"): "2026-07-23T00:00:00Z",
    ("provenance", "evidence_status"): "APPROVED",
}


class ValidationFailure(Exception):
    """Expected validation failure with a stable machine-readable code."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


class DuplicateKeyError(ValueError):
    """Raised when strict JSON loading encounters a duplicate object key."""


def fail(code: str, message: str) -> NoReturn:
    raise ValidationFailure(code, message)


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail("FILE_MISSING", f"{label}: {path}")
    except UnicodeDecodeError as exc:
        fail(
            "JSON_INVALID",
            f"{label}: {path.name}: invalid UTF-8 at byte {exc.start}",
        )
    except OSError as exc:
        fail("FILE_READ_ERROR", f"{label}: {path}: {exc}")
    try:
        value = json.loads(text, object_pairs_hook=strict_object)
    except DuplicateKeyError as exc:
        fail("JSON_DUPLICATE_KEY", f"{label}: duplicate key {exc}")
    except json.JSONDecodeError as exc:
        fail(
            "JSON_INVALID",
            f"{label}: {path.name}:{exc.lineno}:{exc.colno}: {exc.msg}",
        )
    except RecursionError:
        fail("JSON_INVALID", f"{label}: JSON nesting exceeds the safe parser limit")
    if not isinstance(value, dict):
        fail("ROOT_TYPE", f"{label}: root must be an object")
    return value


def require_mapping(value: Any, label: str, code: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(code, f"{label} must be an object")
    return value


def require_list(value: Any, label: str, code: str) -> list[Any]:
    if not isinstance(value, list):
        fail(code, f"{label} must be an array")
    return value


def exact_name_set(value: Any, expected: set[str]) -> bool:
    return (
        isinstance(value, list)
        and len(value) == len(expected)
        and set(value) == expected
    )


def json_exact(actual: Any, expected: Any) -> bool:
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, dict):
        return (
            set(actual) == set(expected)
            and all(json_exact(actual[key], item) for key, item in expected.items())
        )
    if isinstance(expected, list):
        return len(actual) == len(expected) and all(
            json_exact(actual_item, expected_item)
            for actual_item, expected_item in zip(actual, expected)
        )
    return actual == expected


def schema_type_for_const(value: Any) -> str:
    if type(value) is bool:
        return "boolean"
    if type(value) is int:
        return "integer"
    if type(value) is float:
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    fail(
        "SCHEMA_CONTRACT_WEAKENED",
        f"unsupported governed const type: {type(value).__name__}",
    )


def property_schema(schema: dict[str, Any], path: tuple[str, ...]) -> dict[str, Any]:
    node = schema
    for name in path:
        properties = node.get("properties")
        if not isinstance(properties, dict) or name not in properties:
            fail(
                "SCHEMA_CONTRACT_WEAKENED",
                f"schema property {'/'.join(path)} is missing",
            )
        node = require_mapping(
            properties[name],
            f"schema property {'/'.join(path)}",
            "SCHEMA_CONTRACT_WEAKENED",
        )
    return node


def reject_schema_references(value: Any, path: str = "#") -> None:
    if isinstance(value, dict):
        if "$ref" in value:
            fail(
                "SCHEMA_CONTRACT_WEAKENED",
                f"schema references are forbidden for offline validation: {path}/$ref",
            )
        for key, item in value.items():
            reject_schema_references(item, f"{path}/{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            reject_schema_references(item, f"{path}/{index}")


def validate_closed_object_schema(
    node: dict[str, Any],
    label: str,
    expected_fields: set[str],
) -> None:
    properties = node.get("properties")
    if (
        node.get("type") != "object"
        or node.get("additionalProperties") is not False
        or not exact_name_set(node.get("required"), expected_fields)
        or not isinstance(properties, dict)
        or set(properties) != expected_fields
    ):
        fail(
            "SCHEMA_CONTRACT_WEAKENED",
            f"{label} must be a closed object with the exact required fields",
        )


def validate_schema_definition(schema: dict[str, Any]) -> None:
    reject_schema_references(schema)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        fail("SCHEMA_INVALID", exc.message)

    if schema.get("$schema") != EXPECTED_SCHEMA_DRAFT:
        fail("SCHEMA_CONTRACT_WEAKENED", "unexpected JSON Schema draft")
    if schema.get("$id") != EXPECTED_SCHEMA_ID:
        fail("SCHEMA_CONTRACT_WEAKENED", "unexpected schema identity")
    validate_closed_object_schema(schema, "schema root", ROOT_FIELDS)

    for path, fields in OBJECT_FIELDS.items():
        validate_closed_object_schema(
            property_schema(schema, path),
            f"schema object {'/'.join(path)}",
            fields,
        )

    excluded_grades = property_schema(
        schema, ("pipe_family_policy", "excluded_grades")
    )
    excluded_item = require_mapping(
        excluded_grades.get("items"),
        "excluded grade item schema",
        "SCHEMA_CONTRACT_WEAKENED",
    )
    validate_closed_object_schema(
        excluded_item,
        "excluded grade item schema",
        {"code", "disposition"},
    )

    for path, expected in EXPECTED_SCHEMA_CONSTS.items():
        node = property_schema(schema, path)
        if (
            "const" not in node
            or not json_exact(node["const"], expected)
            or node.get("type") != schema_type_for_const(expected)
        ):
            fail(
                "SCHEMA_CONTRACT_WEAKENED",
                f"schema const or type {'/'.join(path)} differs from the governed contract",
            )

    captured_at = property_schema(schema, ("provenance", "captured_at"))
    if captured_at.get("format") != "date-time":
        fail(
            "SCHEMA_CONTRACT_WEAKENED",
            "provenance/captured_at must enforce date-time format",
        )


def format_error_path(error: Any) -> str:
    parts = [
        str(part).replace("~", "~0").replace("/", "~1")
        for part in error.absolute_path
    ]
    return "/" + "/".join(parts) if parts else "/"


def validate_contract_instance(
    contract: dict[str, Any],
    schema: dict[str, Any],
) -> None:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(contract),
        key=lambda item: (
            tuple(str(part) for part in item.absolute_path),
            item.message,
        ),
    )
    if errors:
        error = errors[0]
        fail(
            "SCHEMA_INSTANCE_INVALID",
            f"{format_error_path(error)}: {error.message}",
        )


def validate_lifecycle_history(contract: dict[str, Any]) -> None:
    lifecycle = require_mapping(
        contract.get("lifecycle"),
        "lifecycle",
        "LIFECYCLE_TRANSITION",
    )
    history = require_list(
        lifecycle.get("transition_history"),
        "lifecycle transition_history",
        "LIFECYCLE_TRANSITION",
    )
    current_status = "DRAFT"
    expected_fields = {
        "from",
        "to",
        "decided_by",
        "decided_on",
        "decision_id",
        "evidence_reference",
    }
    allowed_transitions = {
        ("DRAFT", "REVIEW"),
        ("REVIEW", "APPROVED"),
    }

    for index, transition_value in enumerate(history):
        transition = require_mapping(
            transition_value,
            f"lifecycle transition {index}",
            "LIFECYCLE_TRANSITION",
        )
        if set(transition) != expected_fields:
            fail(
                "LIFECYCLE_TRANSITION",
                f"lifecycle transition {index} must contain exact evidence fields",
            )
        edge = (transition.get("from"), transition.get("to"))
        if edge not in allowed_transitions or edge[0] != current_status:
            fail(
                "LIFECYCLE_TRANSITION",
                f"illegal or non-linear lifecycle transition at index {index}",
            )
        if (
            transition.get("decided_by") != "FOUNDER"
            or transition.get("decided_on") != "2026-07-28"
            or transition.get("decision_id") != LIFECYCLE_DECISION_ID
            or transition.get("evidence_reference")
            != LIFECYCLE_EVIDENCE_REFERENCE
        ):
            fail(
                "LIFECYCLE_TRANSITION",
                f"invalid lifecycle authority evidence at index {index}",
            )
        current_status = transition["to"]

    if current_status != lifecycle.get("status"):
        fail(
            "LIFECYCLE_TRANSITION",
            "lifecycle history does not terminate at the current status",
        )
    if (
        lifecycle.get("decision_id") != LIFECYCLE_DECISION_ID
        or lifecycle.get("review_record_id") != LIFECYCLE_REVIEW_RECORD_ID
        or lifecycle.get("reviewers") != LIFECYCLE_REVIEWERS
        or "FOUNDER" in lifecycle.get("reviewers", [])
    ):
        fail(
            "LIFECYCLE_TRANSITION",
            "lifecycle decision or independent review evidence differs",
        )
    expected_outcome = (
        "PASS" if lifecycle.get("status") == "APPROVED" else "IN_PROGRESS"
    )
    if lifecycle.get("review_outcome") != expected_outcome:
        fail(
            "LIFECYCLE_TRANSITION",
            "review outcome is inconsistent with lifecycle status",
        )


def validate_source_relationship(
    contract: dict[str, Any],
    source: dict[str, Any],
) -> None:
    source_contract = require_mapping(
        contract.get("source_contract"),
        "source_contract",
        "SOURCE_CONTRACT",
    )
    if (
        source_contract.get("path") != EXPECTED_SOURCE_PATH
        or source_contract.get("version") != "0.1.0"
    ):
        fail("SOURCE_CONTRACT", "unexpected source contract reference")
    if (
        source.get("blueprint_id") != "bp2-pipe-data-blueprint"
        or source.get("blueprint_version") != source_contract["version"]
    ):
        fail("SOURCE_IDENTITY", "source blueprint identity or version differs")
    if source.get("hierarchy") != contract.get("canonical_hierarchy"):
        fail("SOURCE_RELATION", "canonical hierarchy differs from the source")
    if source.get("governance_statuses") != contract.get("status_vocabulary"):
        fail("SOURCE_RELATION", "status vocabulary differs from the source")

    source_family = require_mapping(
        source.get("family"),
        "source family",
        "SOURCE_RELATION",
    )
    policy = require_mapping(
        contract.get("pipe_family_policy"),
        "pipe_family_policy",
        "SOURCE_RELATION",
    )
    if source_family.get("family_key") != policy.get("family_key"):
        fail("SOURCE_RELATION", "family_key differs from the source")

    controlled_values = require_mapping(
        source.get("controlled_values"),
        "source controlled_values",
        "SOURCE_RELATION",
    )
    source_grades = require_list(
        controlled_values.get("grades"),
        "source grades",
        "SOURCE_RELATION",
    )
    grade_statuses: dict[str, str] = {}
    for index, entry_value in enumerate(source_grades):
        entry = require_mapping(
            entry_value,
            f"source grade {index}",
            "SOURCE_RELATION",
        )
        code = entry.get("code")
        status = entry.get("status")
        if not isinstance(code, str) or not isinstance(status, str):
            fail("SOURCE_RELATION", f"source grade {index} is malformed")
        if code in grade_statuses:
            fail("SOURCE_RELATION", f"source grade {code} is duplicated")
        grade_statuses[code] = status
    if grade_statuses != EXPECTED_SOURCE_GRADES:
        fail("SOURCE_RELATION", "source grade statuses differ")

    administered = set(
        require_list(
            policy.get("administered_grades"),
            "administered_grades",
            "SOURCE_RELATION",
        )
    )
    excluded_entries = require_list(
        policy.get("excluded_grades"),
        "excluded_grades",
        "SOURCE_RELATION",
    )
    excluded = {
        require_mapping(item, "excluded grade", "SOURCE_RELATION").get("code")
        for item in excluded_entries
    }
    if (
        administered & excluded
        or administered | excluded != set(EXPECTED_SOURCE_GRADES)
    ):
        fail(
            "SOURCE_RELATION",
            "administered and excluded grades must partition source grades",
        )

    source_lengths = require_list(
        controlled_values.get("lengths_m"),
        "source lengths",
        "SOURCE_RELATION",
    )
    length_statuses: dict[int, str] = {}
    for index, entry_value in enumerate(source_lengths):
        entry = require_mapping(
            entry_value,
            f"source length {index}",
            "SOURCE_RELATION",
        )
        value = entry.get("value")
        status = entry.get("status")
        if type(value) is not int or not isinstance(status, str):
            fail("SOURCE_RELATION", f"source length {index} is malformed")
        if value in length_statuses:
            fail("SOURCE_RELATION", f"source length {value} is duplicated")
        length_statuses[value] = status
    if (
        length_statuses != EXPECTED_SOURCE_LENGTHS
        or policy.get("base_lengths_m") != list(EXPECTED_SOURCE_LENGTHS)
    ):
        fail("SOURCE_RELATION", "base lengths differ from the source")

    measurement = require_mapping(
        source.get("measurement_policy"),
        "source measurement_policy",
        "SOURCE_RELATION",
    )
    if (
        policy.get("custom_length") != measurement.get("custom_length")
        or policy.get("sales_and_inquiry_unit")
        != measurement.get("sales_and_inquiry_unit")
        or policy.get("calculation_unit") != measurement.get("calculation_unit")
    ):
        fail("SOURCE_RELATION", "measurement policy differs from the source")

    source_pilots = require_list(
        source.get("approved_pilot_combinations"),
        "source approved pilots",
        "SOURCE_RELATION",
    )
    actual_pilots: set[tuple[Any, ...]] = set()
    for index, pilot_value in enumerate(source_pilots):
        pilot = require_mapping(
            pilot_value,
            f"source pilot {index}",
            "SOURCE_RELATION",
        )
        actual_pilots.add(
            (
                pilot.get("combination_id"),
                pilot.get("reference_code"),
                pilot.get("reference_is_final_sku"),
                pilot.get("grade"),
                pilot.get("color"),
                pilot.get("diameter_mm"),
                pilot.get("thickness_mm"),
                pilot.get("length_m"),
                pilot.get("supply_status"),
                pilot.get("status"),
            )
        )
    historical = require_mapping(
        source.get("historical_matrix"),
        "source historical_matrix",
        "SOURCE_RELATION",
    )
    if (
        len(source_pilots) != 3
        or actual_pilots != EXPECTED_SOURCE_PILOTS
        or historical.get("total_rows") != 882
        or historical.get("approved_pilot_rows") != len(source_pilots)
        or historical.get("candidate_rows") != 879
        or historical.get("cartesian_generation_forbidden") is not True
        or policy.get("approved_pilot_count") != len(source_pilots)
        or policy.get("candidate_count") != historical.get("candidate_rows")
        or policy.get("cartesian_generation_forbidden")
        != historical.get("cartesian_generation_forbidden")
    ):
        fail("SOURCE_RELATION", "pilot or historical counts differ from the source")

    selection = require_mapping(
        contract.get("selection_policy"),
        "selection_policy",
        "SOURCE_RELATION",
    )
    source_inquiry = require_mapping(
        source.get("custom_inquiry"),
        "source custom_inquiry",
        "SOURCE_RELATION",
    )
    if (
        selection.get("approved_combination_selectable")
        != source_inquiry.get("approved_combination_selectable")
        or selection.get("free_text_inquiry_allowed")
        != source_inquiry.get("other_free_text_allowed")
        or selection.get("auto_creates_master_data")
        != source_inquiry.get("auto_creates_master_data")
        or selection.get("auto_creates_product")
        != source_inquiry.get("auto_creates_product")
        or selection.get("auto_creates_sku")
        != source_inquiry.get("auto_creates_variation")
    ):
        fail("SOURCE_RELATION", "selection policy differs from the source")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the BP2 data administration contract offline."
    )
    parser.add_argument("--contract", type=Path, default=CONTRACT_PATH)
    parser.add_argument("--schema", type=Path, default=SCHEMA_PATH)
    parser.add_argument("--source", type=Path, default=SOURCE_PATH)
    return parser.parse_args(argv)


def run(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    contract = load_json(args.contract, "contract")
    schema = load_json(args.schema, "schema")
    source = load_json(args.source, "source")
    validate_schema_definition(schema)
    validate_contract_instance(contract, schema)
    validate_lifecycle_history(contract)
    validate_source_relationship(contract, source)
    print(
        "BP2 DATA ADMINISTRATION VALIDATION PASSED: "
        "Draft 2020-12 schema enforced offline; all nested objects closed; "
        "DRAFT -> REVIEW lifecycle evidence verified; "
        "12 governed registries; add/edit/soft-delete; 3 approved pilots preserved; "
        "879 candidates not promoted; no admin UI, Product, SKU, WordPress, import, "
        "publication, or deployment authority."
    )


def main(argv: Sequence[str] | None = None) -> int:
    try:
        run(argv)
    except ValidationFailure as exc:
        print(f"[{exc.code}] {exc.message}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
