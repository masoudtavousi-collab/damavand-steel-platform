#!/usr/bin/env python3
"""Validate the imported Damavand Steel Atlas v1.0 package."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ATLAS_MANIFEST = ROOT / "atlas" / "ATLAS_MASTER_MANIFEST.yaml"
JSON_MIRROR = ROOT / "n8n" / "config" / "ATLAS_MASTER_MANIFEST.json"
SCHEMA_PATH = ROOT / "atlas" / "DOCUMENT_OUTPUT_SCHEMA.json"
REGISTRY_PATH = ROOT / "atlas" / "DOCUMENT_REGISTRY.csv"
WORKFLOW_DIR = ROOT / "n8n" / "workflows"

EXPECTED_DOMAIN_COUNT = 21
EXPECTED_DOCUMENT_COUNT = 173
EXPECTED_WORKFLOWS = (
    "WF-01_ATLAS_MASTER_CONTROLLER.json",
    "WF-02_DOCUMENT_GENERATOR.json",
    "WF-03_REPAIR_LOOP.json",
)
EXECUTION_MODES = ("OFFLINE", "VALIDATE", "DRY_RUN", "LIVE")
REMOTE_WRITE_METHODS = {"POST", "PUT", "PATCH", "DELETE"}
DOCUMENT_ID_PATTERN = re.compile(r"^[A-Z]{2,3}-\d{3}$")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)
REGISTRY_FIELDS = (
    "id",
    "title",
    "domain",
    "path",
    "status",
    "minimum_words",
    "dependencies",
)


class ValidationError(RuntimeError):
    """Raised when the imported Atlas package violates its contract."""


def load_json(path: Path, label: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"Missing {label}: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(
            f"Invalid {label} at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def load_manifest() -> tuple[dict[str, Any], str]:
    mirror = load_json(JSON_MIRROR, "Atlas JSON mirror")
    if not isinstance(mirror, dict):
        raise ValidationError("Atlas JSON mirror must contain an object")

    try:
        import yaml  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        try:
            raw_yaml = ATLAS_MANIFEST.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise ValidationError("Missing Atlas YAML manifest") from exc
        if "domains:" not in raw_yaml or "documents:" not in raw_yaml:
            raise ValidationError("Atlas YAML manifest lacks domains or documents")
        return mirror, "JSON mirror (PyYAML unavailable)"

    parsed_yaml = yaml.safe_load(ATLAS_MANIFEST.read_text(encoding="utf-8"))
    if parsed_yaml != mirror:
        raise ValidationError("Atlas YAML and JSON mirror are not semantically equal")
    return parsed_yaml, "YAML plus JSON mirror"


def normalized_dependencies(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[|,]", value) if item.strip()]


def validate_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    required = ("atlas", "quality_gates", "domains", "documents")
    missing = [key for key in required if key not in manifest]
    if missing:
        raise ValidationError("Manifest missing keys: " + ", ".join(missing))

    atlas = manifest["atlas"]
    domains = manifest["domains"]
    documents = manifest["documents"]
    if not isinstance(atlas, dict):
        raise ValidationError("atlas must be an object")
    if not isinstance(domains, list) or not isinstance(documents, list):
        raise ValidationError("domains and documents must be arrays")

    errors: list[str] = []
    if len(domains) != EXPECTED_DOMAIN_COUNT:
        errors.append(f"Expected {EXPECTED_DOMAIN_COUNT} domains, found {len(domains)}")
    if len(documents) != EXPECTED_DOCUMENT_COUNT:
        errors.append(
            f"Expected {EXPECTED_DOCUMENT_COUNT} documents, found {len(documents)}"
        )

    domain_ids = [domain.get("id") for domain in domains]
    if len(domain_ids) != len(set(domain_ids)):
        errors.append("Duplicate domain IDs")

    document_ids = [document.get("id") for document in documents]
    if len(document_ids) != len(set(document_ids)):
        errors.append("Duplicate document IDs")
    known_ids = set(document_ids)

    for domain in domains:
        domain_id = domain.get("id")
        actual = sum(1 for document in documents if document.get("domain") == domain_id)
        if domain.get("document_count") != actual:
            errors.append(
                f"{domain_id} document_count={domain.get('document_count')} but found {actual}"
            )

    for document in documents:
        document_id = document.get("id")
        if not isinstance(document_id, str) or not DOCUMENT_ID_PATTERN.fullmatch(
            document_id
        ):
            errors.append(f"Bad document ID: {document_id!r}")
            continue
        if document.get("domain") not in set(domain_ids):
            errors.append(f"{document_id} references an unknown domain")
        for dependency in document.get("dependencies", []):
            if dependency not in known_ids:
                errors.append(f"{document_id} missing dependency {dependency}")
        if document.get("minimum_words", 0) < 3000:
            errors.append(f"{document_id} minimum_words too low")
        if not document.get("required_sections"):
            errors.append(f"{document_id} missing required_sections")
        path = Path(str(document.get("path", "")))
        if path.is_absolute() or ".." in path.parts or not str(path):
            errors.append(f"{document_id} has unsafe path {path}")

    if errors:
        raise ValidationError("; ".join(errors))
    return documents


def validate_registry(documents: list[dict[str, Any]]) -> int:
    try:
        with REGISTRY_PATH.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
    except FileNotFoundError as exc:
        raise ValidationError("Missing Atlas document registry") from exc

    if tuple(reader.fieldnames or ()) != REGISTRY_FIELDS:
        raise ValidationError("Document registry header does not match the source contract")
    if len(rows) != EXPECTED_DOCUMENT_COUNT:
        raise ValidationError(
            f"Expected {EXPECTED_DOCUMENT_COUNT} registry rows, found {len(rows)}"
        )

    by_id = {document["id"]: document for document in documents}
    errors: list[str] = []
    for row in rows:
        document = by_id.get(row["id"])
        if document is None:
            errors.append(f"Registry ID missing from manifest: {row['id']}")
            continue
        comparisons = {
            "title": row["title"],
            "domain": row["domain"],
            "path": row["path"],
            "status": row["status"],
            "minimum_words": int(row["minimum_words"]),
            "dependencies": normalized_dependencies(row["dependencies"]),
        }
        for field, value in comparisons.items():
            if document.get(field, [] if field == "dependencies" else None) != value:
                errors.append(f"{row['id']} registry mismatch: {field}")

    if errors:
        raise ValidationError("; ".join(errors))
    return 0


def validate_schema() -> None:
    schema = load_json(SCHEMA_PATH, "document output schema")
    if not isinstance(schema, dict):
        raise ValidationError("Document output schema must contain an object")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ValidationError("Document output schema must use JSON Schema 2020-12")
    if schema.get("type") != "object":
        raise ValidationError("Document output schema root type must be object")


def connection_targets(
    connections: dict[str, Any], source: str, output_index: int
) -> set[str]:
    outputs = connections.get(source, {}).get("main", [])
    if output_index >= len(outputs) or not isinstance(outputs[output_index], list):
        return set()
    return {
        edge.get("node")
        for edge in outputs[output_index]
        if isinstance(edge, dict) and isinstance(edge.get("node"), str)
    }


def incoming_sources(connections: dict[str, Any], target: str) -> set[str]:
    sources: set[str] = set()
    for source, connection_types in connections.items():
        if not isinstance(connection_types, dict):
            continue
        for outputs in connection_types.values():
            if not isinstance(outputs, list):
                continue
            for output in outputs:
                if not isinstance(output, list):
                    continue
                if any(
                    isinstance(edge, dict) and edge.get("node") == target
                    for edge in output
                ):
                    sources.add(source)
    return sources


def is_external_write(node: dict[str, Any]) -> bool:
    parameters = node.get("parameters", {})
    if not isinstance(parameters, dict):
        return False
    method = str(parameters.get("method", "GET")).upper()
    url = str(parameters.get("url", "")).lower()
    node_type = str(node.get("type", "")).lower()
    if "api.github.com" in url and method in REMOTE_WRITE_METHODS:
        return True
    serialized = json.dumps(parameters).lower()
    if "api.github.com" in serialized and re.search(
        r"method\s*[:=]\s*['\"](?:post|put|patch|delete)['\"]", serialized
    ):
        return True
    if "github" in node_type:
        operation = str(parameters.get("operation", "")).lower()
        return operation not in {"", "get", "getall", "list", "read"}
    return False


def is_external_api_node(node: dict[str, Any]) -> bool:
    if node.get("type") == "n8n-nodes-base.httpRequest":
        return True
    parameters = node.get("parameters", {})
    if not isinstance(parameters, dict):
        return False
    serialized = json.dumps(parameters).lower()
    return "helpers.httprequest" in serialized or "https://" in serialized


def scan_for_secrets() -> int:
    scan_roots = (
        ROOT / "atlas",
        ROOT / "n8n",
        ROOT / "config" / "environment.example",
    )
    files: list[Path] = []
    for path in scan_roots:
        if not path.exists():
            continue
        if path.is_file():
            files.append(path)
        else:
            files.extend(candidate for candidate in path.rglob("*") if candidate.is_file())

    matches = 0
    for path in files:
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        matches += sum(len(pattern.findall(content)) for pattern in SECRET_PATTERNS)
    return matches


def validate_workflows() -> dict[str, int]:
    metrics = {
        "workflow_json_files": 0,
        "workflow_parse_errors": 0,
        "active_workflows": 0,
        "ungated_external_write_nodes": 0,
        "offline_validate_network_violations": 0,
        "execution_mode_policy_errors": 0,
    }
    loaded: dict[str, dict[str, Any]] = {}

    for filename in EXPECTED_WORKFLOWS:
        workflow = load_json(WORKFLOW_DIR / filename, filename)
        metrics["workflow_json_files"] += 1
        if not isinstance(workflow, dict):
            raise ValidationError(f"{filename} must contain an object")
        loaded[filename] = workflow
        nodes = workflow.get("nodes")
        connections = workflow.get("connections")
        if not isinstance(nodes, list) or not nodes:
            raise ValidationError(f"{filename} has no workflow nodes")
        if not isinstance(connections, dict) or not connections:
            raise ValidationError(f"{filename} has no workflow connections")
        if workflow.get("active") is not False:
            metrics["active_workflows"] += 1
            raise ValidationError(f"{filename} must remain inactive")

        names = [node.get("name") for node in nodes]
        ids = [node.get("id") for node in nodes]
        if (
            any(not isinstance(name, str) or not name for name in names)
            or any(not isinstance(node_id, str) or not node_id for node_id in ids)
            or len(names) != len(set(names))
            or len(ids) != len(set(ids))
        ):
            raise ValidationError(f"{filename} has duplicate or missing node names/IDs")
        if any(node.get("credentials") for node in nodes):
            raise ValidationError(f"{filename} contains embedded credential bindings")
        if "REPLACE_ME" in json.dumps(workflow):
            raise ValidationError(f"{filename} contains an unsafe REPLACE_ME placeholder")

        known_names = set(names)
        for source, connection_types in connections.items():
            if source not in known_names:
                raise ValidationError(f"{filename} has unknown source node {source}")
            if not isinstance(connection_types, dict):
                raise ValidationError(f"{filename} has malformed connections for {source}")
            for outputs in connection_types.values():
                if not isinstance(outputs, list):
                    raise ValidationError(f"{filename} has malformed outputs for {source}")
                for output in outputs:
                    if not isinstance(output, list):
                        raise ValidationError(
                            f"{filename} has malformed connection output for {source}"
                        )
                    for edge in output:
                        if not isinstance(edge, dict) or edge.get("node") not in known_names:
                            target = edge.get("node") if isinstance(edge, dict) else edge
                            raise ValidationError(
                                f"{filename} has unknown target node {target}"
                            )

        for node in nodes:
            parameters = node.get("parameters", {})
            if not isinstance(parameters, dict):
                continue
            header_group = parameters.get("headerParameters", {})
            headers = (
                header_group.get("parameters", [])
                if isinstance(header_group, dict)
                else []
            )
            for header in headers if isinstance(headers, list) else []:
                if not isinstance(header, dict):
                    continue
                if str(header.get("name", "")).lower() not in {
                    "authorization",
                    "x-api-key",
                }:
                    continue
                value = header.get("value")
                if not isinstance(value, str) or "$env." not in value:
                    raise ValidationError(
                        f"{filename} / {node.get('name')} embeds a credential value"
                    )

            if re.search(
                r"\b(publish|deploy|release to production)\b",
                str(node.get("name", "")),
                re.IGNORECASE,
            ):
                raise ValidationError(
                    f"{filename} contains deployment-capable node {node.get('name')}"
                )

            if not is_external_write(node):
                if not is_external_api_node(node):
                    continue
                node_name = str(node["name"])
                sources = incoming_sources(connections, node_name)
                mode_guarded = len(sources) == 1
                if mode_guarded:
                    gate_name = next(iter(sources))
                    gate = next(item for item in nodes if item.get("name") == gate_name)
                    gate_text = json.dumps(gate.get("parameters", {}))
                    blocked_targets = connection_targets(connections, gate_name, 1)
                    blocked_nodes = [
                        item for item in nodes if item.get("name") in blocked_targets
                    ]
                    blocked_text = json.dumps(blocked_nodes).replace(" ", "")
                    mode_guarded = (
                        gate.get("type") == "n8n-nodes-base.if"
                        and "execution_mode === 'DRY_RUN'" in gate_text
                        and "execution_mode === 'LIVE'" in gate_text
                        and node_name in connection_targets(connections, gate_name, 0)
                        and "offline_local_only" in blocked_text
                        and "validate_local_only" in blocked_text
                        and "network_performed:false" in blocked_text
                        and "validation_scope" in blocked_text
                        and "manifest" in blocked_text
                        and "registry" in blocked_text
                        and "workflows" in blocked_text
                    )
                if not mode_guarded:
                    metrics["offline_validate_network_violations"] += 1
                continue
            node_name = str(node["name"])
            sources = incoming_sources(connections, node_name)
            guarded = len(sources) == 1
            if guarded:
                gate_name = next(iter(sources))
                gate = next(item for item in nodes if item.get("name") == gate_name)
                gate_text = json.dumps(gate.get("parameters", {}))
                blocked_targets = connection_targets(connections, gate_name, 1)
                blocked_nodes = [
                    item for item in nodes if item.get("name") in blocked_targets
                ]
                blocked_text = json.dumps(blocked_nodes).replace(" ", "")
                guarded = (
                    gate.get("type") == "n8n-nodes-base.if"
                    and "execution_mode === 'LIVE'" in gate_text
                    and "dry_run === false" in gate_text
                    and "founder_write_approved === true" in gate_text
                    and "credentials_configured === true" in gate_text
                    and "$workflow.active === true" in gate_text
                    and node_name in connection_targets(connections, gate_name, 0)
                    and "dry_run_blocked_write" in blocked_text
                    and "write_performed:false" in blocked_text
                )
            if not guarded:
                metrics["ungated_external_write_nodes"] += 1

        if re.search(
            r"https?://(?:www\.)?(?:damavandsteel|centralsteel)\.",
            json.dumps(workflow),
            re.IGNORECASE,
        ):
            raise ValidationError(f"{filename} contains a production-site URL")

    wf1 = loaded[EXPECTED_WORKFLOWS[0]]
    config_node = next(
        (node for node in wf1["nodes"] if node.get("name") == "Pipeline Configuration"),
        None,
    )
    if config_node is None:
        raise ValidationError("WF-01 is missing Pipeline Configuration")
    assignments = config_node.get("parameters", {}).get("assignments", {}).get(
        "assignments", []
    )
    defaults = {
        item.get("name"): item.get("value")
        for item in assignments
        if isinstance(item, dict)
    }
    if defaults.get("dry_run") is not True:
        raise ValidationError("WF-01 dry_run must default to true")
    if defaults.get("founder_write_approved") is not False:
        raise ValidationError("WF-01 founder_write_approved must default to false")
    if defaults.get("credentials_configured") is not False:
        raise ValidationError("WF-01 credentials_configured must default to false")
    if defaults.get("execution_mode") != "OFFLINE":
        raise ValidationError("WF-01 execution_mode must default to OFFLINE")

    expected_resolver_sources = {
        EXPECTED_WORKFLOWS[0]: "Pipeline Configuration",
        EXPECTED_WORKFLOWS[1]: "Execute Workflow Trigger",
        EXPECTED_WORKFLOWS[2]: "Execute Workflow Trigger",
    }
    for filename, source in expected_resolver_sources.items():
        workflow = loaded[filename]
        resolver = next(
            (
                node
                for node in workflow["nodes"]
                if node.get("name") == "Resolve Execution Mode"
            ),
            None,
        )
        if resolver is None:
            metrics["execution_mode_policy_errors"] += 1
            continue
        resolver_code = str(resolver.get("parameters", {}).get("jsCode", ""))
        if (
            any(f"'{mode}'" not in resolver_code for mode in EXECUTION_MODES)
            or "? requested : 'OFFLINE'" not in resolver_code
            or "dry_run" not in resolver_code
            or "founder_write_approved" not in resolver_code
            or "credentials_configured" not in resolver_code
            or "Resolve Execution Mode"
            not in connection_targets(workflow["connections"], source, 0)
        ):
            metrics["execution_mode_policy_errors"] += 1

    expected_terminals = {
        EXPECTED_WORKFLOWS[0]: ("Run Summary", "Return Local Validation Mode"),
        EXPECTED_WORKFLOWS[1]: (
            "Return Blocked Write",
            "Prepare Repair Request",
            "Return Generation Result",
            "Return Local Validation Mode",
        ),
        EXPECTED_WORKFLOWS[2]: (
            "Return Repaired Document",
            "Escalate To Human",
            "Return Local Validation Mode",
        ),
    }
    for filename, terminals in expected_terminals.items():
        connections = loaded[filename]["connections"]
        node_names = {node.get("name") for node in loaded[filename]["nodes"]}
        for terminal in terminals:
            if terminal not in node_names:
                raise ValidationError(f"{filename} is missing terminal node {terminal}")
            if terminal in connections:
                raise ValidationError(f"{filename} unsafe path after {terminal}")

    wf3 = loaded[EXPECTED_WORKFLOWS[2]]
    guard = next(
        (node for node in wf3["nodes"] if node.get("name") == "Repair Attempt Guard"),
        None,
    )
    guard_code = str((guard or {}).get("parameters", {}).get("jsCode", ""))
    if not re.search(r"attempt\s*>\s*3", guard_code):
        raise ValidationError("WF-03 must permit no more than three repair attempts")
    if metrics["ungated_external_write_nodes"]:
        raise ValidationError(
            "ungated external write nodes: "
            + str(metrics["ungated_external_write_nodes"])
        )
    if metrics["offline_validate_network_violations"]:
        raise ValidationError(
            "OFFLINE/VALIDATE network violations: "
            + str(metrics["offline_validate_network_violations"])
        )
    if metrics["execution_mode_policy_errors"]:
        raise ValidationError(
            "execution mode policy errors: "
            + str(metrics["execution_mode_policy_errors"])
        )
    return metrics


def main() -> int:
    try:
        manifest, parser_source = load_manifest()
        documents = validate_manifest(manifest)
        registry_mismatches = validate_registry(documents)
        validate_schema()
        workflow_metrics = validate_workflows()
        detected_secrets = scan_for_secrets()
        if detected_secrets:
            raise ValidationError(f"detected secret values: {detected_secrets}")
    except (OSError, TypeError, ValueError, ValidationError) as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

    print("VALIDATION PASSED")
    print(f"- Manifest parser source: {parser_source}")
    print(f"- Domains: {len(manifest['domains'])}")
    print(f"- Registered documents: {len(documents)}")
    print(f"- Registry mismatches: {registry_mismatches}")
    print(f"- Workflow JSON files: {workflow_metrics['workflow_json_files']}")
    print(f"- Workflow parse errors: {workflow_metrics['workflow_parse_errors']}")
    print(f"- Secrets detected: {detected_secrets}")
    print(f"- Active workflows: {workflow_metrics['active_workflows']}")
    print(
        "- Ungated external write nodes: "
        f"{workflow_metrics['ungated_external_write_nodes']}"
    )
    print("- Default execution mode: OFFLINE")
    print(
        "- OFFLINE/VALIDATE network violations: "
        f"{workflow_metrics['offline_validate_network_violations']}"
    )
    print(
        "- Execution mode policy errors: "
        f"{workflow_metrics['execution_mode_policy_errors']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
