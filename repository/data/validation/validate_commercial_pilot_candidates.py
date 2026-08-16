#!/usr/bin/env python3
"""Fail-closed offline validation for C002 Commercial Pilot Candidate intake."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
import re
import sys
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repository/data/contracts/commercial-pilot-candidate.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/commercial-pilot-candidate.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
PD03B_SEEDS_PATH = ROOT / "repository/data/registries/extensions/pd03b/canonical-pilots.yaml"
REGISTRY_ROOT = ROOT / "repository/data/registries"
MAX_INPUT_BYTES = 2_000_000
MAX_NESTING_DEPTH = 64
MAX_STRUCTURE_NODES = 20_000
CRITERIA = (
    "DEMAND_SIGNAL",
    "SUPPLY_EVIDENCE",
    "GROSS_PROFIT_POTENTIAL",
    "REPEATABILITY",
    "PRODUCT_DATA_COMPLETENESS",
    "PHOTO_CONTENT_READINESS",
    "SEO_BUYER_INTENT",
    "OPERATIONAL_COMPLEXITY",
    "FULFILLMENT_RISK",
)
EVIDENCE_STATES = (
    "MISSING",
    "SUBMITTED",
    "VERIFIED",
    "CONFLICTING",
    "EXPIRED",
    "NOT_APPLICABLE_APPROVED",
)
RESOLVED_STATE_ORDER = ("VERIFIED", "NOT_APPLICABLE_APPROVED")
RESOLVED_STATES = frozenset(RESOLVED_STATE_ORDER)
BOUNDARY = {
    "candidate_population_authority": False,
    "product_population_authority": False,
    "sku_assignment_authority": False,
    "availability_claim_authority": False,
    "runtime_authority": False,
    "commerce_activation_authority": False,
}
PROHIBITED_FIELD_ORDER = (
    "product_id", "sku", "commercial_sku", "availability_value", "supply_status",
    "stock", "inventory", "price", "pricing", "cost", "margin",
    "gross_profit_value", "discount", "coupon", "offer", "cart", "checkout",
    "payment", "wordpress_id", "woocommerce_id", "import", "publication",
    "deployment", "production",
)
PROHIBITED_FIELDS = frozenset(PROHIBITED_FIELD_ORDER)
CONTRACT_ROOT_KEYS = {
    "contract_id", "contract_version", "record_kind", "schema", "registry",
    "dependencies", "authority", "data_classifications", "provenance_policy", "stable_identity",
    "seed_reference_policy", "founder_evidence_packet",
    "minimum_founder_data_packet", "readiness_policy", "selection_state_policy",
    "scope_policy", "validation", "prohibited_fields",
}
EXPECTED_DEPENDENCIES = {
    "product_core": "repository/data/contracts/product-core.contract.yaml",
    "pd03b_seed_evidence": "repository/data/contracts/pd03b-canonical-pilot.contract.yaml",
}
EXPECTED_CLASSIFICATIONS = {
    "canonical": "C002_CONTRACT_FOUNDATION",
    "fixture": "SYNTHETIC_FIXTURE",
    "founder_intake": "FOUNDER_INTAKE_PROTECTED",
}
EXPECTED_PROVENANCE_POLICY = {
    "synthetic_fixture": {
        "source_type": "SYNTHETIC_FIXTURE",
        "captured_by": "role:automated-validation",
        "evidence_status": "SYNTHETIC_TEST_EVIDENCE",
        "allowed_classification": "SYNTHETIC_FIXTURE",
    },
    "founder_intake_protected": {
        "source_type": "FOUNDER_EVIDENCE_PACKET",
        "captured_by": "role:founder-or-authorized-steward",
        "evidence_status": "PROTECTED_FOUNDER_EVIDENCE",
        "allowed_classification": "FOUNDER_INTAKE_PROTECTED",
        "canonical_population_authority": False,
    },
}
EXPECTED_STABLE_IDENTITY = {
    "candidate_id_pattern": r"^cpcand:[0-9a-f]{12}$",
    "founder_packet_id_pattern": r"^cpfep:[0-9a-f]{12}$",
    "evidence_source_id_pattern": r"^cpevd:[0-9a-f]{12}$",
    "allocation_policy": "CSPRNG_12_HEX_WITH_GLOBAL_COLLISION_CHECK",
    "independent_from": ["pilot_id", "product_id", "sku", "label", "slug"],
}
EXPECTED_SEED_POLICY = {
    "evidence_role": "SEED_REFERENCE_ONLY",
    "references_are_identity": False,
    "seed_count_is_scope_ceiling": False,
    "selection_may_extend_beyond_seeds": True,
    "seed_reference_must_resolve": True,
    "automatic_candidate_promotion": False,
}
EXPECTED_DETERMINISTIC_EVALUATION = {
    "evaluation_as_of_required": True,
    "temporal_order": "submitted_at<=reviewed_at<=expires_at",
    "expiry_boundary": "expires_at<=evaluation_as_of_is_expired",
    "expired_and_conflicting_are_unresolved": True,
    "reviewer_must_differ_from": ["every_source_submitter", "packet_owner"],
}
MINIMUM_PACKET_SECTIONS = (
    "bounded_commercial_context", "protected_commercial_evidence",
    "operations_fulfillment", "parties", "mass", "appearance",
    "content_photo_rights", "seo", "inventory_harmony", "commerce_intent",
    "damavand_central_boundary", "information_governance",
    "conflicts_exclusions_blockers", "owner_role", "reviewer_role",
)
EXPECTED_MINIMUM_PACKET_POLICY = {
    "required_sections": list(MINIMUM_PACKET_SECTIONS),
    "unresolved_marker": "UNRESOLVED",
    "packet_states": ["INCOMPLETE", "COMPLETE"],
    "canonical_and_proposal_references_are_separate": True,
    "commercial_values_forbidden_protected_locators_only": True,
    "gross_profit_locator_source": "FOUNDER_SUPPLIED",
    "ready_requires": {
        "packet_state": "COMPLETE", "unresolved_marker_count": 0,
        "conflicts": 0, "blockers": 0, "owner_reviewer_independent": True,
    },
    "founder_decision_vocabulary": {
        "current_instance_state": "PENDING_FOUNDER_SELECTION",
        "current_instance_reference": None,
        "future_vocabulary_only": ["FOUNDER_DECISION_RECORDED"],
    },
}
EXPECTED_READINESS_POLICY = {
    "states": ["NOT_READY", "FOUNDER_SELECTION_READY"],
    "founder_selection_ready_requires": {
        "resolved_count": 9, "unresolved_count": 0, "blocker_count": 0,
    },
    "readiness_is_selection": False,
    "readiness_creates_product": False,
    "readiness_creates_sku": False,
    "readiness_asserts_availability": False,
}
EXPECTED_SELECTION_STATE_POLICY = {
    "product_state": "NOT_CREATED",
    "sku_state": "NOT_ASSIGNED",
    "availability_state": "NOT_ASSERTED",
    "projection_state": "NOT_AUTHORIZED",
    "commerce_state": "INQUIRY_ONLY",
}
EXPECTED_SCOPE_POLICY = {
    "allowed_entity_reference_types": ["FAMILY", "SERIES", "VARIANT_RULE_SET"],
    "per_intake_maximum_is_not_program_ceiling": True,
    "cartesian_generation_forbidden": True,
    "exact_candidate_tuple_population_forbidden": True,
}
EXPECTED_VALIDATION_POLICY = {
    "offline_only": True,
    "network_allowed": False,
    "side_effects_allowed": False,
    "canonical_candidate_count": 0,
    "duplicate_yaml_and_json_keys_rejected": True,
    "non_finite_numbers_rejected": True,
    "remote_or_permissive_schema_rejected": True,
    "deterministic_sorted_errors": True,
    "mutation_manifest_dispatch_required": True,
}
EXPECTED_SELECTION_EFFECTS = {
    "founder_selection_recorded": False,
    **EXPECTED_SELECTION_STATE_POLICY,
    "creates_product": False,
    "creates_sku": False,
    "asserts_availability": False,
    "authorizes_runtime": False,
    "authorizes_commerce": False,
    "limits_future_scope_to_seed_count": False,
}
REFERENCE_ID = re.compile(
    r"^(?:prd:(?:catalog|platform|family|series|variant-rule-set|sku)|"
    r"pilot|unit|dimension|attr|vreg|vterm|cpcand|cpfep|cpevd):[0-9a-f]{12}$"
)


class ConfigurationError(ValueError):
    """Raised when a protected validation dependency is invalid."""


class DuplicateKeyError(ConfigurationError):
    """Raised when strict loading finds a duplicate object key."""


@dataclass(frozen=True)
class Issue:
    source: str
    path: str
    code: str
    message: str

    def render(self) -> str:
        return f"{self.source}: {self.path}: [{self.code}] {self.message}"


@dataclass(frozen=True)
class Definitions:
    contract: dict[str, Any]
    schema_validator: Draft202012Validator
    known_registry_ids: frozenset[str]
    known_seed_ids: frozenset[str]


def safe_path(path: Path, label: str) -> Path:
    try:
        if path.is_symlink():
            raise ConfigurationError(f"[{label.upper()}_SYMLINK] {label} must not be a symbolic link")
        resolved = path.resolve(strict=True)
    except FileNotFoundError as exc:
        raise ConfigurationError(f"[{label.upper()}_MISSING] missing {label}: {path}") from exc
    if resolved != ROOT and ROOT not in resolved.parents:
        raise ConfigurationError(f"[{label.upper()}_PATH] {label} must remain inside the repository")
    return resolved


def read_text(path: Path, label: str) -> str:
    resolved = safe_path(path, label)
    if resolved.stat().st_size > MAX_INPUT_BYTES:
        raise ConfigurationError(f"[INPUT_SIZE] {label} exceeds {MAX_INPUT_BYTES} bytes")
    try:
        return resolved.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ConfigurationError(f"[UTF8] {label} must be valid UTF-8") from exc


def bounded(value: Any, label: str) -> Any:
    stack: list[tuple[Any, int]] = [(value, 0)]
    nodes = 0
    while stack:
        item, depth = stack.pop()
        nodes += 1
        if nodes > MAX_STRUCTURE_NODES:
            raise ConfigurationError(f"[STRUCTURE_SIZE] {label} exceeds the node cap")
        if depth > MAX_NESTING_DEPTH:
            raise ConfigurationError(f"[STRUCTURE_DEPTH] {label} exceeds the nesting cap")
        if isinstance(item, dict):
            stack.extend((child, depth + 1) for child in item.values())
        elif isinstance(item, list):
            stack.extend((child, depth + 1) for child in item)
    return value


def strict_json(raw: str, label: str) -> Any:
    def pairs_hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise DuplicateKeyError(f"[DUPLICATE_KEY] {label}: duplicate JSON key {key!r}")
            result[key] = value
        return result

    def reject_constant(value: str) -> None:
        raise ConfigurationError(f"[NON_FINITE_NUMBER] {label}: {value} is forbidden")

    try:
        return bounded(
            json.loads(raw, object_pairs_hook=pairs_hook, parse_constant=reject_constant),
            label,
        )
    except (DuplicateKeyError, ConfigurationError):
        raise
    except json.JSONDecodeError as exc:
        raise ConfigurationError(
            f"[INVALID_JSON] {label}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    except RecursionError as exc:
        raise ConfigurationError(f"[STRUCTURE_DEPTH] {label}: unsafe JSON nesting") from exc


def strict_yaml(raw: str, label: str) -> Any:
    try:
        import yaml  # type: ignore[import-not-found]
    except ModuleNotFoundError as exc:
        raise ConfigurationError("[YAML_DEPENDENCY] approved PyYAML is required") from exc

    class UniqueKeyLoader(yaml.SafeLoader):  # type: ignore[attr-defined]
        pass

    def construct_mapping(loader: Any, node: Any, deep: bool = False) -> dict[Any, Any]:
        result: dict[Any, Any] = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            try:
                if key in result:
                    raise DuplicateKeyError(f"[DUPLICATE_KEY] {label}: duplicate YAML key {key!r}")
            except TypeError as exc:
                raise ConfigurationError(f"[YAML_KEY] {label}: unhashable key") from exc
            result[key] = loader.construct_object(value_node, deep=deep)
        return result

    UniqueKeyLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,  # type: ignore[attr-defined]
        construct_mapping,
    )
    try:
        return bounded(yaml.load(raw, Loader=UniqueKeyLoader), label)
    except (DuplicateKeyError, ConfigurationError):
        raise
    except yaml.YAMLError as exc:  # type: ignore[attr-defined]
        raise ConfigurationError(f"[INVALID_YAML] {label}: {exc}") from exc
    except RecursionError as exc:
        raise ConfigurationError(f"[STRUCTURE_DEPTH] {label}: unsafe YAML nesting") from exc


def load_json(path: Path, label: str) -> Any:
    return strict_json(read_text(path, label), label)


def load_yaml(path: Path, label: str) -> Any:
    return strict_yaml(read_text(path, label), label)


def mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ConfigurationError(f"[{label.upper()}_TYPE] {label} must be a mapping")
    return value


def audit_schema(node: Any, path: str = "#") -> None:
    if isinstance(node, dict):
        ref = node.get("$ref")
        if "$ref" in node and (not isinstance(ref, str) or not ref.startswith("#/")):
            raise ConfigurationError(f"[REMOTE_SCHEMA_REF] non-local $ref at {path}")
        if node.get("type") == "object":
            if node.get("additionalProperties") is not False:
                raise ConfigurationError(f"[PERMISSIVE_SCHEMA] object is not closed at {path}")
            properties = node.get("properties")
            required = node.get("required")
            has_composition = any(key in node for key in ("allOf", "anyOf", "oneOf"))
            if not has_composition and (
                not isinstance(properties, dict)
                or not isinstance(required, list)
                or set(required) != set(properties)
            ):
                raise ConfigurationError(
                    f"[INCOMPLETE_OBJECT_SCHEMA] object fields are not all required at {path}"
                )
        for key, value in node.items():
            audit_schema(value, f"{path}/{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            audit_schema(value, f"{path}/{index}")


def iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from iter_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_strings(item)


def iter_keys(value: Any, path: str = "<root>") -> Iterable[tuple[str, str]]:
    if isinstance(value, dict):
        for key, item in value.items():
            child = f"{path}/{key}"
            if isinstance(key, str):
                yield key, child
            yield from iter_keys(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from iter_keys(item, f"{path}/{index}")


def collect_registry_ids() -> frozenset[str]:
    ids: set[str] = set()
    for path in sorted(REGISTRY_ROOT.rglob("*.yaml")):
        if path == REGISTRY_PATH:
            continue
        value = load_yaml(path, f"registry dependency {path.relative_to(ROOT)}")
        ids.update(item for item in iter_strings(value) if REFERENCE_ID.fullmatch(item))
    return frozenset(ids)


def validate_contract(contract: dict[str, Any]) -> None:
    if set(contract) != CONTRACT_ROOT_KEYS:
        raise ConfigurationError("[CONTRACT_ROOT] contract keys differ")
    if (
        contract.get("contract_id") != "commercial-pilot-candidate"
        or contract.get("contract_version") != "1.0.0"
        or contract.get("record_kind") != "commercial-pilot-candidate-registry"
    ):
        raise ConfigurationError("[CONTRACT_IDENTITY] contract identity differs")
    schema = mapping(contract.get("schema"), "schema")
    if schema != {
        "path": "repository/data/schemas/commercial-pilot-candidate.schema.json",
        "draft": "https://json-schema.org/draft/2020-12/schema",
    }:
        raise ConfigurationError("[CONTRACT_SCHEMA] schema declaration differs")
    if contract.get("registry") != {
        "path": "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
    }:
        raise ConfigurationError("[CONTRACT_REGISTRY] registry declaration differs")
    if contract.get("dependencies") != EXPECTED_DEPENDENCIES:
        raise ConfigurationError("[CONTRACT_DEPENDENCIES] dependency declarations differ")
    authority = mapping(contract.get("authority"), "authority")
    expected_authority = {"mission_id": "C002", "contract_schema_validator_test_work": True, **BOUNDARY}
    if authority != expected_authority:
        raise ConfigurationError("[CONTRACT_AUTHORITY] C002 authority boundary differs")
    if contract.get("data_classifications") != EXPECTED_CLASSIFICATIONS:
        raise ConfigurationError("[CONTRACT_CLASSIFICATIONS] classifications differ")
    if contract.get("provenance_policy") != EXPECTED_PROVENANCE_POLICY:
        raise ConfigurationError("[CONTRACT_PROVENANCE] provenance policy differs")
    if contract.get("stable_identity") != EXPECTED_STABLE_IDENTITY:
        raise ConfigurationError("[CONTRACT_STABLE_IDENTITY] stable identity policy differs")
    if contract.get("seed_reference_policy") != EXPECTED_SEED_POLICY:
        raise ConfigurationError("[CONTRACT_SEED_POLICY] seed reference policy differs")
    packet = mapping(contract.get("founder_evidence_packet"), "founder_evidence_packet")
    if packet.get("criterion_count") != 9 or tuple(packet.get("criterion_order", ())) != CRITERIA:
        raise ConfigurationError("[CRITERION_CONTRACT] exact nine criteria differ")
    if tuple(packet.get("evidence_states", ())) != EVIDENCE_STATES:
        raise ConfigurationError("[EVIDENCE_STATE_CONTRACT] evidence states differ")
    if tuple(packet.get("resolved_states", ())) != RESOLVED_STATE_ORDER:
        raise ConfigurationError("[RESOLUTION_CONTRACT] resolved states differ")
    if packet.get("coverage_formula") != "resolved_count/9":
        raise ConfigurationError("[COVERAGE_CONTRACT] coverage formula differs")
    if packet.get("weights_allowed") is not False or packet.get("thresholds_allowed") is not False:
        raise ConfigurationError("[COVERAGE_CONTRACT] weights and thresholds must be forbidden")
    if packet.get("gross_profit_fact_source") != "FOUNDER_SUPPLIED":
        raise ConfigurationError("[GROSS_PROFIT_CONTRACT] Founder source is required")
    if packet.get("deterministic_evaluation") != EXPECTED_DETERMINISTIC_EVALUATION:
        raise ConfigurationError("[CONTRACT_EVIDENCE_EVALUATION] evidence evaluation differs")
    if set(packet) != {
        "criterion_count", "criterion_order", "evidence_states", "resolved_states",
        "coverage_formula", "weights_allowed", "thresholds_allowed",
        "gross_profit_fact_source", "deterministic_evaluation",
    }:
        raise ConfigurationError("[CONTRACT_EVIDENCE_PACKET] evidence packet policy keys differ")
    if contract.get("minimum_founder_data_packet") != EXPECTED_MINIMUM_PACKET_POLICY:
        raise ConfigurationError("[CONTRACT_MINIMUM_PACKET] minimum Founder packet policy differs")
    if contract.get("readiness_policy") != EXPECTED_READINESS_POLICY:
        raise ConfigurationError("[CONTRACT_READINESS] readiness policy differs")
    if contract.get("selection_state_policy") != EXPECTED_SELECTION_STATE_POLICY:
        raise ConfigurationError("[CONTRACT_SELECTION_STATES] selection state policy differs")
    if contract.get("scope_policy") != EXPECTED_SCOPE_POLICY:
        raise ConfigurationError("[CONTRACT_SCOPE] scope policy differs")
    if contract.get("validation") != EXPECTED_VALIDATION_POLICY:
        raise ConfigurationError("[CONTRACT_VALIDATION] validation policy differs")
    if contract.get("prohibited_fields") != list(PROHIBITED_FIELD_ORDER):
        raise ConfigurationError("[PROHIBITED_CONTRACT] prohibited fields differ")


def load_definitions(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> Definitions:
    contract = mapping(load_yaml(contract_path, "contract"), "contract")
    validate_contract(contract)
    schema = mapping(load_json(schema_path, "schema"), "schema")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ConfigurationError("[SCHEMA_DRAFT] schema must declare Draft 2020-12")
    audit_schema(schema)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise ConfigurationError(f"[SCHEMA_INVALID] {exc.message}") from exc
    seeds = mapping(load_yaml(PD03B_SEEDS_PATH, "PD03B seeds"), "PD03B seeds")
    seed_ids = frozenset(
        item.get("pilot_id")
        for item in seeds.get("pilots", [])
        if isinstance(item, dict) and isinstance(item.get("pilot_id"), str)
    )
    return Definitions(
        contract=contract,
        schema_validator=Draft202012Validator(schema, format_checker=FormatChecker()),
        known_registry_ids=collect_registry_ids(),
        known_seed_ids=seed_ids,
    )


def review_complete(review: Any) -> bool:
    return isinstance(review, dict) and all(
        isinstance(review.get(field), str) and bool(review[field].strip())
        for field in ("reviewed_by", "reviewed_at", "evidence_reference")
    )


def review_empty(review: Any) -> bool:
    return isinstance(review, dict) and all(
        review.get(field) is None
        for field in ("reviewed_by", "reviewed_at", "evidence_reference")
    )


def parse_timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None


def marker_paths(value: Any, marker: str, path: str = "") -> list[str]:
    found: list[str] = []
    if value == marker:
        found.append(path or "<root>")
    elif isinstance(value, dict):
        for key, item in value.items():
            found.extend(marker_paths(item, marker, f"{path}/{key}" if path else str(key)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(marker_paths(item, marker, f"{path}/{index}" if path else str(index)))
    return found


def evidence_shape_is_valid(state: Any, sources: list[Any], review: Any) -> bool:
    if state == "MISSING":
        return not sources and review_empty(review)
    if state == "SUBMITTED":
        return bool(sources) and review_empty(review)
    if state == "VERIFIED":
        return bool(sources) and review_complete(review)
    if state == "CONFLICTING":
        return len(sources) >= 2 and review_complete(review)
    if state == "EXPIRED":
        return bool(sources) and any(
            isinstance(source, dict) and isinstance(source.get("expires_at"), str)
            for source in sources
        ) and review_complete(review)
    if state == "NOT_APPLICABLE_APPROVED":
        return bool(sources) and review_complete(review)
    return False


def validate_registry(value: Any, source: str, definitions: Definitions) -> list[Issue]:
    issues: list[Issue] = []

    def add(path: str, code: str, message: str) -> None:
        issues.append(Issue(source, path, code, message))

    if not isinstance(value, dict):
        add("<root>", "REGISTRY_TYPE", "registry must be a mapping")
        return issues

    schema_errors = sorted(
        definitions.schema_validator.iter_errors(value),
        key=lambda item: (tuple(str(part) for part in item.absolute_path), item.message),
    )
    for error in schema_errors:
        path = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add(path, "SCHEMA_VALIDATION", error.message)

    for key, path in iter_keys(value):
        if key in PROHIBITED_FIELDS:
            add(path, "PROHIBITED_FIELD", f"field {key!r} is outside C002 authority")

    if value.get("registry_id") != "commercial-pilot-candidates":
        add("registry_id", "REGISTRY_IDENTITY", "registry_id differs")
    if value.get("registry_version") != "1.0.0" or value.get("contract_version") != "1.0.0":
        add("registry_version", "REGISTRY_VERSION", "registry and contract versions must remain 1.0.0")
    if value.get("boundary") != BOUNDARY:
        add("boundary", "AUTHORITY_BOUNDARY", "C002 authority boundary differs")

    candidates = value.get("candidates") if isinstance(value.get("candidates"), list) else []
    classification = value.get("data_classification")
    if classification == "C002_CONTRACT_FOUNDATION" and candidates:
        add("candidates", "CANONICAL_POPULATION", "canonical C002 candidate registry must remain empty")
    if classification == "SYNTHETIC_FIXTURE" and not candidates:
        add("candidates", "SYNTHETIC_POPULATION", "synthetic classification requires test-only candidate evidence")
    if classification == "FOUNDER_INTAKE_PROTECTED" and not candidates:
        add("candidates", "FOUNDER_INTAKE_POPULATION", "protected Founder intake requires at least one noncanonical intake record")

    candidate_ids: set[str] = set()
    packet_ids: set[str] = set()
    evidence_source_ids: set[str] = set()
    for candidate_index, candidate in enumerate(candidates):
        path = f"candidates/{candidate_index}"
        if not isinstance(candidate, dict):
            continue
        candidate_id = candidate.get("candidate_id")
        if isinstance(candidate_id, str):
            if candidate_id in candidate_ids:
                add(f"{path}/candidate_id", "DUPLICATE_CANDIDATE_ID", candidate_id)
            candidate_ids.add(candidate_id)
            if candidate_id in definitions.known_registry_ids:
                add(f"{path}/candidate_id", "GLOBAL_ID_COLLISION", candidate_id)

        provenance = candidate.get("provenance")
        if isinstance(provenance, dict):
            provenance_type = provenance.get("source_type")
            if classification == "SYNTHETIC_FIXTURE" and provenance_type != "SYNTHETIC_FIXTURE":
                add(
                    f"{path}/provenance/source_type",
                    "CLASSIFICATION_PROVENANCE",
                    "synthetic classification requires synthetic provenance",
                )
            elif classification == "FOUNDER_INTAKE_PROTECTED" and provenance_type != "FOUNDER_EVIDENCE_PACKET":
                add(
                    f"{path}/provenance/source_type",
                    "CLASSIFICATION_PROVENANCE",
                    "protected Founder intake classification requires protected Founder provenance",
                )
            elif classification not in {"SYNTHETIC_FIXTURE", "FOUNDER_INTAKE_PROTECTED"}:
                add(
                    f"{path}/provenance/source_type",
                    "CLASSIFICATION_PROVENANCE",
                    "candidate provenance is allowed only in a noncanonical input classification",
                )

        scope = candidate.get("commercial_scope")
        if isinstance(scope, dict):
            for ref_index, reference in enumerate(scope.get("entity_references", [])):
                if isinstance(reference, str) and reference not in definitions.known_registry_ids:
                    add(
                        f"{path}/commercial_scope/entity_references/{ref_index}",
                        "UNKNOWN_ENTITY_REFERENCE",
                        reference,
                    )

        for seed_index, seed in enumerate(candidate.get("seed_references", [])):
            if not isinstance(seed, dict):
                continue
            pilot_id = seed.get("pilot_id")
            if isinstance(pilot_id, str) and pilot_id not in definitions.known_seed_ids:
                add(
                    f"{path}/seed_references/{seed_index}/pilot_id",
                    "UNKNOWN_SEED_REFERENCE",
                    pilot_id,
                )

        packet = candidate.get("founder_evidence_packet")
        if not isinstance(packet, dict):
            continue
        evaluation_as_of = parse_timestamp(packet.get("evaluation_as_of"))
        packet_id = packet.get("packet_id")
        if isinstance(packet_id, str):
            if packet_id in packet_ids:
                add(f"{path}/founder_evidence_packet/packet_id", "DUPLICATE_PACKET_ID", packet_id)
            packet_ids.add(packet_id)
            if packet_id in definitions.known_registry_ids:
                add(f"{path}/founder_evidence_packet/packet_id", "GLOBAL_ID_COLLISION", packet_id)

        minimum = packet.get("minimum_data_packet")
        minimum_prefix = (
            "candidates", candidate_index, "founder_evidence_packet", "minimum_data_packet",
        )
        minimum_has_schema_error = any(
            tuple(error.absolute_path)[: len(minimum_prefix)] == minimum_prefix
            for error in schema_errors
        )
        minimum_valid = (
            isinstance(minimum, dict)
            and set(minimum) == {"packet_state", *MINIMUM_PACKET_SECTIONS}
            and not minimum_has_schema_error
        )
        if not minimum_valid:
            add(
                f"{path}/founder_evidence_packet/minimum_data_packet",
                "MINIMUM_PACKET_STRUCTURE",
                "minimum Founder packet must contain every required section exactly once",
            )
        unresolved_paths = marker_paths(minimum, "UNRESOLVED") if isinstance(minimum, dict) else []
        governance = (
            minimum.get("conflicts_exclusions_blockers")
            if isinstance(minimum, dict) and isinstance(minimum.get("conflicts_exclusions_blockers"), dict)
            else {}
        )
        packet_conflicts = governance.get("conflicts") if isinstance(governance.get("conflicts"), list) else []
        packet_blockers = governance.get("blockers") if isinstance(governance.get("blockers"), list) else []
        owner_role = minimum.get("owner_role") if isinstance(minimum, dict) else None
        reviewer_role = minimum.get("reviewer_role") if isinstance(minimum, dict) else None
        if owner_role == reviewer_role and isinstance(owner_role, str):
            minimum_valid = False
            add(
                f"{path}/founder_evidence_packet/minimum_data_packet/reviewer_role",
                "PACKET_REVIEW_INDEPENDENCE",
                "minimum packet owner and reviewer must be independent",
            )
        bounded_context = (
            minimum.get("bounded_commercial_context")
            if isinstance(minimum, dict) and isinstance(minimum.get("bounded_commercial_context"), dict)
            else {}
        )
        for ref_index, reference in enumerate(bounded_context.get("canonical_references", [])):
            if (
                isinstance(reference, str)
                and reference != "UNRESOLVED"
                and reference not in definitions.known_registry_ids
            ):
                minimum_valid = False
                add(
                    f"{path}/founder_evidence_packet/minimum_data_packet/bounded_commercial_context/canonical_references/{ref_index}",
                    "UNKNOWN_PACKET_CANONICAL_REFERENCE",
                    reference,
                )
        mass_context = (
            minimum.get("mass")
            if isinstance(minimum, dict) and isinstance(minimum.get("mass"), dict)
            else {}
        )
        mass_unit = mass_context.get("unit_reference")
        if (
            isinstance(mass_unit, str)
            and mass_unit != "UNRESOLVED"
            and mass_unit not in definitions.known_registry_ids
        ):
            minimum_valid = False
            add(
                f"{path}/founder_evidence_packet/minimum_data_packet/mass/unit_reference",
                "UNKNOWN_MASS_UNIT_REFERENCE",
                mass_unit,
            )
        complete_facts = (
            minimum_valid
            and not unresolved_paths
            and not packet_conflicts
            and not packet_blockers
            and isinstance(owner_role, str)
            and isinstance(reviewer_role, str)
            and owner_role != reviewer_role
        )
        expected_packet_state = "COMPLETE" if complete_facts else "INCOMPLETE"
        if isinstance(minimum, dict) and minimum.get("packet_state") != expected_packet_state:
            add(
                f"{path}/founder_evidence_packet/minimum_data_packet/packet_state",
                "MINIMUM_PACKET_STATE",
                f"expected {expected_packet_state}; unresolved={len(unresolved_paths)}, conflicts={len(packet_conflicts)}, blockers={len(packet_blockers)}",
            )
        minimum_complete = complete_facts and minimum.get("packet_state") == "COMPLETE"

        decision_state = packet.get("decision_state")
        decision_reference = packet.get("decision_reference")
        if decision_state != "PENDING_FOUNDER_SELECTION" or decision_reference is not None:
            add(
                f"{path}/founder_evidence_packet/decision_reference",
                "FOUNDER_DECISION_STATE",
                "C002 instances are pending-only with null decision reference; recorded is vocabulary-only",
            )

        criteria = packet.get("criteria") if isinstance(packet.get("criteria"), list) else []
        actual_order = tuple(
            item.get("criterion_code") if isinstance(item, dict) else None
            for item in criteria
        )
        if len(actual_order) == 9 and actual_order != CRITERIA:
            add(f"{path}/founder_evidence_packet/criteria", "CRITERION_ORDER", "criteria must use the exact Mission order")

        criterion_validity: dict[str, bool] = {}
        for criterion_index, criterion in enumerate(criteria):
            if not isinstance(criterion, dict):
                continue
            criterion_path = f"{path}/founder_evidence_packet/criteria/{criterion_index}"
            criterion_code = criterion.get("criterion_code")
            criterion_prefix = (
                "candidates", candidate_index, "founder_evidence_packet", "criteria", criterion_index,
            )
            criterion_valid = not any(
                tuple(error.absolute_path)[: len(criterion_prefix)] == criterion_prefix
                for error in schema_errors
            )
            sources = criterion.get("sources") if isinstance(criterion.get("sources"), list) else []
            review = criterion.get("review")
            if not evidence_shape_is_valid(criterion.get("state"), sources, review):
                criterion_valid = False
                add(criterion_path, "EVIDENCE_STATE_SHAPE", "state, sources, and review are inconsistent")
            review_time = parse_timestamp(review.get("reviewed_at")) if isinstance(review, dict) else None
            reviewed_by = review.get("reviewed_by") if isinstance(review, dict) else None
            complete_review = review_complete(review)
            if complete_review:
                if reviewed_by != reviewer_role:
                    criterion_valid = False
                    add(
                        f"{criterion_path}/review/reviewed_by",
                        "REVIEW_ROLE_MISMATCH",
                        "criterion review must use the packet's independent reviewer",
                    )
                if reviewed_by == owner_role:
                    criterion_valid = False
                    add(
                        f"{criterion_path}/review/reviewed_by",
                        "REVIEW_INDEPENDENCE",
                        "reviewer must differ from packet owner",
                    )
                if evaluation_as_of is not None and review_time is not None and review_time > evaluation_as_of:
                    criterion_valid = False
                    add(
                        f"{criterion_path}/review/reviewed_at",
                        "EVIDENCE_AFTER_AS_OF",
                        "reviewed_at cannot follow evaluation_as_of",
                    )
            expiry_times: list[datetime] = []
            for source_index, evidence in enumerate(sources):
                if not isinstance(evidence, dict):
                    continue
                source_path = f"{criterion_path}/sources/{source_index}"
                evidence_id = evidence.get("evidence_source_id")
                if isinstance(evidence_id, str):
                    if evidence_id in evidence_source_ids:
                        criterion_valid = False
                        add(
                            f"{source_path}/evidence_source_id",
                            "DUPLICATE_EVIDENCE_SOURCE_ID",
                            evidence_id,
                        )
                    evidence_source_ids.add(evidence_id)
                    if evidence_id in definitions.known_registry_ids:
                        criterion_valid = False
                        add(
                            f"{source_path}/evidence_source_id",
                            "GLOBAL_ID_COLLISION",
                            evidence_id,
                        )
                submitted_at = parse_timestamp(evidence.get("submitted_at"))
                expires_at = parse_timestamp(evidence.get("expires_at"))
                if expires_at is not None:
                    expiry_times.append(expires_at)
                if evaluation_as_of is not None and submitted_at is not None and submitted_at > evaluation_as_of:
                    criterion_valid = False
                    add(
                        f"{source_path}/submitted_at",
                        "EVIDENCE_AFTER_AS_OF",
                        "submitted_at cannot follow evaluation_as_of",
                    )
                if submitted_at is not None and expires_at is not None and submitted_at > expires_at:
                    criterion_valid = False
                    add(
                        f"{source_path}/expires_at",
                        "EVIDENCE_TEMPORAL_ORDER",
                        "submitted_at cannot follow expires_at",
                    )
                if complete_review and submitted_at is not None and review_time is not None:
                    if submitted_at > review_time or (expires_at is not None and review_time > expires_at):
                        criterion_valid = False
                        add(
                            f"{source_path}/submitted_at",
                            "EVIDENCE_TEMPORAL_ORDER",
                            "required order is submitted_at <= reviewed_at <= expires_at",
                        )
                if complete_review and reviewed_by == evidence.get("submitted_by"):
                    criterion_valid = False
                    add(
                        f"{criterion_path}/review/reviewed_by",
                        "REVIEW_INDEPENDENCE",
                        "reviewer must differ from every evidence submitter",
                    )
                if criterion.get("criterion_code") == "GROSS_PROFIT_POTENTIAL" and evidence.get("source_type") != "FOUNDER_SUPPLIED":
                    criterion_valid = False
                    add(
                        f"{source_path}/source_type",
                        "GROSS_PROFIT_SOURCE",
                        "gross-profit facts must be Founder-supplied",
                    )
            expired_as_of = bool(
                evaluation_as_of is not None
                and any(expires_at <= evaluation_as_of for expires_at in expiry_times)
            )
            state = criterion.get("state")
            if (state == "EXPIRED") != expired_as_of:
                criterion_valid = False
                add(
                    f"{criterion_path}/state",
                    "EVIDENCE_STATE_AS_OF",
                    "EXPIRED must match deterministic expiry at evaluation_as_of",
                )
            if isinstance(criterion_code, str):
                criterion_validity[criterion_code] = criterion_valid

        states_by_code = {
            criterion.get("criterion_code"): criterion.get("state")
            for criterion in criteria
            if isinstance(criterion, dict) and isinstance(criterion.get("criterion_code"), str)
        }
        resolved = [
            code for code in CRITERIA
            if states_by_code.get(code) in RESOLVED_STATES and criterion_validity.get(code) is True
        ]
        unresolved = [code for code in CRITERIA if code not in resolved]
        coverage = packet.get("coverage")
        if isinstance(coverage, dict) and (
            coverage.get("resolved_count") != len(resolved)
            or coverage.get("unresolved_criteria") != unresolved
        ):
            add(
                f"{path}/founder_evidence_packet/coverage",
                "COVERAGE_MISMATCH",
                f"expected resolved_count={len(resolved)} and exact unresolved list",
            )

        readiness = candidate.get("readiness")
        if isinstance(readiness, dict):
            blockers = readiness.get("blockers") if isinstance(readiness.get("blockers"), list) else []
            expected_state = (
                "FOUNDER_SELECTION_READY"
                if len(resolved) == 9 and minimum_complete and not blockers
                else "NOT_READY"
            )
            if readiness.get("state") != expected_state:
                add(
                    f"{path}/readiness/state",
                    "READINESS_MISMATCH",
                    f"expected {expected_state} from 9/9 coverage and blocker state",
                )

        if candidate.get("selection_effects") != EXPECTED_SELECTION_EFFECTS:
            add(
                f"{path}/selection_effects",
                "SELECTION_STATE_BOUNDARY",
                "Product, SKU, Availability, projection, and commerce states must remain separately fail-closed",
            )

    return sorted(issues, key=lambda item: (item.path, item.code, item.message))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", type=Path, default=REGISTRY_PATH)
    parser.add_argument("--contract", type=Path, default=CONTRACT_PATH)
    parser.add_argument("--schema", type=Path, default=SCHEMA_PATH)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        definitions = load_definitions(args.contract, args.schema)
        value = load_yaml(args.registry, "candidate registry")
        issues = validate_registry(value, str(args.registry), definitions)
    except ConfigurationError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except (OSError, ValueError, TypeError) as exc:
        print(f"[VALIDATION_CONFIGURATION] {exc}", file=sys.stderr)
        return 2
    if issues:
        for issue in issues:
            print(issue.render(), file=sys.stderr)
        return 1
    count = len(value.get("candidates", [])) if isinstance(value, dict) else 0
    classification = value.get("data_classification") if isinstance(value, dict) else None
    print(
        "C002 Commercial Pilot Candidate validation PASS: "
        f"classification={classification}; candidates={count}; "
        "coverage=resolved_count/9; no Product/SKU/Availability/projection/commerce authority."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
