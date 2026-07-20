#!/usr/bin/env python3
"""Validate the Damavand Steel Atlas bootstrap and fail-closed workflow contracts."""

from __future__ import annotations

import csv
import json
import posixpath
import re
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
ATLAS_MANIFEST = ROOT / "atlas" / "ATLAS_MASTER_MANIFEST.yaml"
N8N_YAML_MIRROR = ROOT / "n8n" / "config" / "ATLAS_MASTER_MANIFEST.yaml"
JSON_MIRROR = ROOT / "n8n" / "config" / "ATLAS_MASTER_MANIFEST.json"
SCHEMA_PATH = ROOT / "atlas" / "DOCUMENT_OUTPUT_SCHEMA.json"
TEMPLATE_PATH = ROOT / "atlas" / "DOCUMENT_TEMPLATE.md"
REGISTRY_PATH = ROOT / "atlas" / "DOCUMENT_REGISTRY.csv"
WORKFLOW_DIR = ROOT / "n8n" / "workflows"
CI_PATH = ROOT / ".github" / "workflows" / "ci.yml"

EXPECTED_DOMAIN_COUNT = 21
EXPECTED_DOCUMENT_COUNT = 173
EXPECTED_SCHEMA_VERSION = "1.0.0"
EXPECTED_WORKFLOWS = (
    "WF-01_ATLAS_MASTER_CONTROLLER.json",
    "WF-02_DOCUMENT_GENERATOR.json",
    "WF-03_REPAIR_LOOP.json",
)
EXECUTION_MODES = ("OFFLINE", "VALIDATE", "DRY_RUN", "LIVE")
REMOTE_WRITE_METHODS = {"POST", "PUT", "PATCH", "DELETE"}
DOCUMENT_ID_PATTERN = re.compile(r"^[A-Z]{2,3}-\d{3}$")
VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
REGISTRY_FIELDS = (
    "id",
    "title",
    "domain",
    "path",
    "status",
    "minimum_words",
    "dependencies",
)
EXPECTED_SECTIONS = (
    "purpose",
    "scope",
    "context",
    "definitions",
    "architecture",
    "entities",
    "fields",
    "relationships",
    "business_rules",
    "workflows",
    "validation",
    "permissions",
    "integrations",
    "failure_scenarios",
    "security",
    "seo_impact",
    "ai_usage",
    "wordpress_mapping",
    "examples",
    "acceptance_criteria",
    "dependencies_used",
    "related_documents",
    "open_questions",
    "change_history",
)
REQUIRED_GOVERNANCE_FILES = (
    "docs/PROJECT_BASELINE.md",
    "docs/CURRENT_PROJECT_STATE.md",
    "docs/PROJECT_EXECUTION_ROADMAP.md",
    "docs/CODEX_SPRINT_PROTOCOL.md",
    "docs/SOURCE_OF_TRUTH_PRIORITY.md",
    "docs/REPOSITORY_RELATIONSHIP_MAP.md",
)
REQUIRED_RUNTIME_CONTEXT = (
    "PROJECT_BIBLE.md",
    "AGENTS.md",
    *REQUIRED_GOVERNANCE_FILES,
)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)


class ValidationError(RuntimeError):
    """Raised when the bootstrap violates its repository contract."""


def read_text(path: Path, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ValidationError(f"Missing {label}: {path.relative_to(ROOT)}") from exc


def load_json(path: Path, label: str) -> Any:
    try:
        return json.loads(read_text(path, label))
    except json.JSONDecodeError as exc:
        raise ValidationError(
            f"Invalid {label} at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def load_yaml(path: Path, label: str) -> tuple[Any, str]:
    raw = read_text(path, label)
    try:
        import yaml  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        command = [
            "ruby",
            "-ryaml",
            "-rjson",
            "-e",
            "value=YAML.safe_load(STDIN.read, [], [], true); STDOUT.write(JSON.generate(value))",
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
            raise ValidationError(
                "YAML validation requires PyYAML or Ruby Psych; neither is available"
            ) from exc
        if result.returncode != 0:
            raise ValidationError(
                f"Invalid {label} via Ruby Psych: {result.stderr.strip()}"
            )
        try:
            return json.loads(result.stdout), "Ruby Psych fallback"
        except json.JSONDecodeError as exc:
            raise ValidationError(f"Ruby Psych returned invalid JSON for {label}") from exc

    try:
        return yaml.safe_load(raw), f"PyYAML {yaml.__version__}"
    except yaml.YAMLError as exc:  # type: ignore[attr-defined]
        raise ValidationError(f"Invalid {label}: {exc}") from exc


def load_manifests() -> tuple[dict[str, Any], str]:
    atlas_yaml, parser = load_yaml(ATLAS_MANIFEST, "Atlas YAML manifest")
    n8n_yaml, n8n_parser = load_yaml(N8N_YAML_MIRROR, "n8n YAML manifest mirror")
    json_mirror = load_json(JSON_MIRROR, "Atlas JSON mirror")
    if not isinstance(atlas_yaml, dict):
        raise ValidationError("Atlas YAML manifest must contain an object")
    if atlas_yaml != n8n_yaml or atlas_yaml != json_mirror:
        raise ValidationError("Atlas YAML copies and JSON mirror are not semantically equal")
    return atlas_yaml, f"{parser}; mirror={n8n_parser}"


def normalized_dependencies(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[|,]", value) if item.strip()]


def safe_repository_path(value: Any) -> bool:
    if not isinstance(value, str) or not value or value.startswith("/"):
        return False
    if "\\" in value or "\x00" in value:
        return False
    parts = value.split("/")
    return all(part not in {"", ".", ".."} for part in parts)


def dependency_cycles(documents: list[dict[str, Any]]) -> list[list[str]]:
    by_id = {document["id"]: document for document in documents}
    state: dict[str, str] = {}
    stack: list[str] = []
    cycles: list[list[str]] = []

    def visit(document_id: str) -> None:
        if state.get(document_id) == "done":
            return
        if state.get(document_id) == "visiting":
            start = stack.index(document_id)
            cycles.append(stack[start:] + [document_id])
            return
        state[document_id] = "visiting"
        stack.append(document_id)
        for dependency in by_id[document_id].get("dependencies", []):
            visit(dependency)
        stack.pop()
        state[document_id] = "done"

    for document_id in by_id:
        visit(document_id)
    return cycles


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
    document_paths = [document.get("path") for document in documents]
    if len(document_ids) != len(set(document_ids)):
        errors.append("Duplicate document IDs")
    if len(document_paths) != len(set(document_paths)):
        errors.append("Duplicate document paths")
    known_ids = set(document_ids)
    domain_id_set = set(domain_ids)

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
        if document.get("domain") not in domain_id_set:
            errors.append(f"{document_id} references an unknown domain")
        dependencies = document.get("dependencies", [])
        if not isinstance(dependencies, list):
            errors.append(f"{document_id} dependencies must be an array")
            continue
        if len(dependencies) != len(set(dependencies)):
            errors.append(f"{document_id} has duplicate dependencies")
        for dependency in dependencies:
            if dependency not in known_ids:
                errors.append(f"{document_id} missing dependency {dependency}")
        if document.get("minimum_words", 0) < 3000:
            errors.append(f"{document_id} minimum_words too low")
        if tuple(document.get("required_sections", ())) != EXPECTED_SECTIONS:
            errors.append(f"{document_id} required_sections mismatch")
        if not safe_repository_path(document.get("path")):
            errors.append(f"{document_id} has unsafe path {document.get('path')!r}")

    cycles = dependency_cycles(documents)
    if cycles:
        errors.extend("Dependency cycle: " + " -> ".join(cycle) for cycle in cycles)

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
    seen: set[str] = set()
    errors: list[str] = []
    for row in rows:
        row_id = row["id"]
        if row_id in seen:
            errors.append(f"Duplicate registry ID: {row_id}")
            continue
        seen.add(row_id)
        document = by_id.get(row_id)
        if document is None:
            errors.append(f"Registry ID missing from manifest: {row_id}")
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
                errors.append(f"{row_id} registry mismatch: {field}")

    missing = sorted(set(by_id) - seen)
    if missing:
        errors.append("Manifest IDs missing from registry: " + ", ".join(missing))
    if errors:
        raise ValidationError("; ".join(errors))
    return 0


def validate_schema_structure(schema: Any) -> dict[str, Any]:
    if not isinstance(schema, dict):
        raise ValidationError("Document output schema must contain an object")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ValidationError("Document output schema must use JSON Schema 2020-12")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise ValidationError("Document output schema root must be a closed object")
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        raise ValidationError("Document output schema properties are missing")
    version = properties.get("schema_version", {})
    if version.get("const") != EXPECTED_SCHEMA_VERSION:
        raise ValidationError("Document output schema version mismatch")
    required = schema.get("required", [])
    if "schema_version" not in required or "sections" not in required:
        raise ValidationError("Document output schema required properties are incomplete")
    sections = properties.get("sections")
    if not isinstance(sections, dict) or sections.get("type") != "object":
        raise ValidationError("Document sections schema is malformed")
    if sections.get("additionalProperties") is not False:
        raise ValidationError("Document sections schema must reject undeclared sections")
    if tuple(sections.get("required", ())) != EXPECTED_SECTIONS:
        raise ValidationError("Document sections required list does not match the template")
    section_properties = sections.get("properties")
    if not isinstance(section_properties, dict):
        raise ValidationError("Document section property definitions are missing")
    if tuple(section_properties) != EXPECTED_SECTIONS:
        raise ValidationError("Document section property order or identity mismatch")
    for key, definition in section_properties.items():
        if definition.get("type") != "string" or definition.get("minLength") != 1:
            raise ValidationError(f"Section {key} must be a non-empty string")
    return schema


def validate_output(
    output: Any,
    schema: dict[str, Any],
    *,
    expected_id: str | None = None,
    expected_title: str | None = None,
    declared_dependencies: list[str] | None = None,
) -> list[str]:
    errors: list[str] = []
    if not isinstance(output, dict):
        return ["output must be an object"]

    properties = schema["properties"]
    required = schema["required"]
    for key in required:
        if key not in output:
            errors.append(f"missing required property: {key}")
    for key in output:
        if key not in properties:
            errors.append(f"undeclared property: {key}")

    if output.get("schema_version") != EXPECTED_SCHEMA_VERSION:
        errors.append("schema version mismatch")
    document_id = output.get("document_id")
    if not isinstance(document_id, str) or not DOCUMENT_ID_PATTERN.fullmatch(document_id):
        errors.append("invalid document identity")
    if expected_id is not None and document_id != expected_id:
        errors.append("document identity mismatch")
    title = output.get("title")
    if not isinstance(title, str) or not title.strip():
        errors.append("empty title")
    if expected_title is not None and title != expected_title:
        errors.append("document title mismatch")
    if output.get("status") not in properties["status"]["enum"]:
        errors.append("invalid status")
    version = output.get("version")
    if not isinstance(version, str) or not VERSION_PATTERN.fullmatch(version):
        errors.append("invalid version")

    sections = output.get("sections")
    if not isinstance(sections, dict):
        errors.append("malformed sections")
    else:
        for key in EXPECTED_SECTIONS:
            value = sections.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"empty required content: {key}")
        for key in sections:
            if key not in EXPECTED_SECTIONS:
                errors.append(f"undeclared section: {key}")

    for key in (
        "dependencies_used",
        "entities_referenced",
        "rules_referenced",
        "open_questions",
        "acceptance_criteria",
    ):
        if key in output and (
            not isinstance(output[key], list)
            or any(not isinstance(value, str) for value in output[key])
        ):
            errors.append(f"malformed array: {key}")

    if declared_dependencies is not None:
        used = output.get("dependencies_used")
        if (
            not isinstance(used, list)
            or len(used) != len(set(used))
            or sorted(used) != sorted(declared_dependencies)
        ):
            errors.append("dependencies_used mismatch")
    return errors


def valid_output_fixture() -> dict[str, Any]:
    return {
        "schema_version": EXPECTED_SCHEMA_VERSION,
        "document_id": "GOV-001",
        "title": "Enterprise Governance Constitution",
        "status": "draft",
        "version": "0.1.0",
        "sections": {key: f"Governed content for {key}." for key in EXPECTED_SECTIONS},
        "dependencies_used": [],
        "entities_referenced": [],
        "rules_referenced": [],
        "open_questions": [],
        "acceptance_criteria": [],
    }


def validate_output_fixtures(schema: dict[str, Any]) -> int:
    cases: list[tuple[str, dict[str, Any], bool]] = []
    valid = valid_output_fixture()
    cases.append(("valid", valid, True))

    missing_sections = deepcopy(valid)
    missing_sections.pop("sections")
    cases.append(("missing_sections", missing_sections, False))

    undeclared_markdown = deepcopy(valid)
    undeclared_markdown["markdown"] = "# Invalid alternate contract"
    cases.append(("undeclared_markdown", undeclared_markdown, False))

    malformed_sections = deepcopy(valid)
    malformed_sections["sections"] = []
    cases.append(("malformed_sections", malformed_sections, False))

    empty_content = deepcopy(valid)
    empty_content["sections"]["purpose"] = " "
    cases.append(("empty_required_content", empty_content, False))

    bad_version = deepcopy(valid)
    bad_version["schema_version"] = "0.9.0"
    cases.append(("schema_version_mismatch", bad_version, False))

    for name, fixture, should_pass in cases:
        passed = not validate_output(
            fixture,
            schema,
            expected_id="GOV-001",
            expected_title="Enterprise Governance Constitution",
            declared_dependencies=[],
        )
        if passed != should_pass:
            raise ValidationError(f"Output-contract fixture failed expectation: {name}")
    return len(cases)


def heading_for(section: str) -> str:
    special = {
        "seo_impact": "SEO Impact",
        "ai_usage": "AI Usage",
        "wordpress_mapping": "WordPress Mapping",
    }
    return special.get(section, " ".join(word.capitalize() for word in section.split("_")))


def validate_template() -> None:
    template = read_text(TEMPLATE_PATH, "canonical document template")
    tokens = (
        "{{DOCUMENT_ID}}",
        "{{TITLE}}",
        "{{DOMAIN}}",
        "{{OWNER}}",
        "{{DEPENDENCIES}}",
        "{{MINIMUM_WORDS}}",
    )
    for token in tokens:
        if token not in template:
            raise ValidationError(f"Document template is missing token {token}")
    for section in EXPECTED_SECTIONS:
        marker = f"## {heading_for(section)}"
        if template.count(marker) != 1:
            raise ValidationError(f"Document template heading mismatch: {marker}")


def git_tracked_paths() -> set[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError as exc:
        raise ValidationError("Git is required for repository validation") from exc
    if result.returncode != 0:
        raise ValidationError("Unable to enumerate tracked repository files")
    paths = {line for line in result.stdout.splitlines() if line}
    for required in REQUIRED_GOVERNANCE_FILES:
        if (ROOT / required).is_file():
            paths.add(required)
    return paths


def github_heading_slugs(text: str) -> set[str]:
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = re.sub(r"<[^>]*>", "", match.group(1))
        heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        heading = heading.replace(chr(96), "")
        heading = re.sub(r"[*_~]", "", heading)
        slug = heading.lower()
        slug = re.sub(r"[^\w\s-]", "", slug, flags=re.UNICODE).strip()
        slug = re.sub(r"\s", "-", slug)
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        slugs.add(slug if count == 0 else f"{slug}-{count}")
    return slugs


def validate_markdown_links(paths: set[str]) -> int:
    known_files = set(paths)
    known_dirs: set[str] = set()
    for path in known_files:
        parent = posixpath.dirname(path)
        while parent and parent != ".":
            known_dirs.add(parent)
            parent = posixpath.dirname(parent)

    markdown_files = sorted(path for path in known_files if path.lower().endswith(".md"))
    cache: dict[str, str] = {}
    slug_cache: dict[str, set[str]] = {}
    issues: list[str] = []
    checked = 0

    def content(path: str) -> str:
        if path not in cache:
            cache[path] = read_text(ROOT / path, f"Markdown file {path}")
        return cache[path]

    for source in markdown_files:
        text = content(source)
        references = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text)
        references.extend(
            re.findall(r"^\s*\[[^\]]+\]:\s*(\S+)", text, flags=re.MULTILINE)
        )
        for raw in references:
            destination = raw.strip()
            if destination.startswith("<") and destination.endswith(">"):
                destination = destination[1:-1]
            if not destination or re.match(
                r"^(?:https?:|mailto:|tel:|data:)", destination, flags=re.IGNORECASE
            ):
                continue
            checked += 1
            file_part, marker, anchor = destination.partition("#")
            file_part = unquote(file_part)
            if not file_part:
                target = source
            elif file_part.startswith("/"):
                target = posixpath.normpath(file_part.lstrip("/"))
            else:
                target = posixpath.normpath(
                    posixpath.join(posixpath.dirname(source), file_part)
                )
            if target not in known_files and target not in known_dirs:
                issues.append(f"{source}: missing local target {destination} -> {target}")
                continue
            if marker and anchor and target.lower().endswith(".md"):
                normalized_anchor = unquote(anchor).lower()
                if target not in slug_cache:
                    slug_cache[target] = github_heading_slugs(content(target))
                if normalized_anchor not in slug_cache[target]:
                    issues.append(
                        f"{source}: missing anchor {destination} in {target}"
                    )

    if issues:
        raise ValidationError(
            "Markdown link validation failed: " + "; ".join(issues[:40])
        )
    return checked


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
                for edge in output:
                    if isinstance(edge, dict) and edge.get("node") == target:
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


def ancestor_names(
    connections: dict[str, Any], target: str, depth: int = 4
) -> set[str]:
    found: set[str] = set()
    frontier = {target}
    for _ in range(depth):
        next_frontier: set[str] = set()
        for name in frontier:
            for source in incoming_sources(connections, name):
                if source not in found:
                    found.add(source)
                    next_frontier.add(source)
        frontier = next_frontier
    return found


def validate_workflows() -> dict[str, int]:
    metrics = {
        "workflow_json_files": 0,
        "workflow_parse_errors": 0,
        "active_workflows": 0,
        "ungated_external_write_nodes": 0,
        "offline_validate_network_violations": 0,
        "execution_mode_policy_errors": 0,
        "required_context_policy_errors": 0,
        "output_contract_policy_errors": 0,
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

        if any(node.get("credentials") for node in nodes):
            raise ValidationError(f"{filename} contains embedded credential bindings")
        if "REPLACE_ME" in json.dumps(workflow):
            raise ValidationError(f"{filename} contains an unsafe REPLACE_ME placeholder")

        by_name = {node["name"]: node for node in nodes}
        for node in nodes:
            parameters = node.get("parameters", {})
            if not isinstance(parameters, dict):
                continue
            serialized = json.dumps(parameters)
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

            if is_external_write(node):
                node_name = str(node["name"])
                sources = incoming_sources(connections, node_name)
                guarded = len(sources) == 1
                if guarded:
                    gate_name = next(iter(sources))
                    gate = by_name[gate_name]
                    gate_text = json.dumps(gate.get("parameters", {}))
                    blocked_targets = connection_targets(connections, gate_name, 1)
                    blocked_text = json.dumps(
                        [by_name[name] for name in blocked_targets]
                    ).replace(" ", "")
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
                continue

            if not is_external_api_node(node):
                continue
            node_name = str(node["name"])
            ancestors = ancestor_names(connections, node_name)
            gate_names = [
                name
                for name in ancestors
                if by_name[name].get("type") == "n8n-nodes-base.if"
                and "execution_mode === 'DRY_RUN'"
                in json.dumps(by_name[name].get("parameters", {}))
                and "execution_mode === 'LIVE'"
                in json.dumps(by_name[name].get("parameters", {}))
            ]
            if not gate_names:
                metrics["offline_validate_network_violations"] += 1
                continue
            safe_block = False
            for gate_name in gate_names:
                blocked = connection_targets(connections, gate_name, 1)
                blocked_text = json.dumps([by_name[name] for name in blocked]).replace(
                    " ", ""
                )
                if (
                    "offline_local_only" in blocked_text
                    and "validate_local_only" in blocked_text
                    and "network_performed:false" in blocked_text
                ):
                    safe_block = True
            if not safe_block:
                metrics["offline_validate_network_violations"] += 1

        if re.search(
            r"https?://(?:www\.)?(?:damavandsteel|centralsteel)\.",
            json.dumps(workflow),
            re.IGNORECASE,
        ):
            raise ValidationError(f"{filename} contains a production-site URL")

    wf1 = loaded[EXPECTED_WORKFLOWS[0]]
    config = next(
        node for node in wf1["nodes"] if node.get("name") == "Pipeline Configuration"
    )
    assignments = config["parameters"]["assignments"]["assignments"]
    defaults = {
        item.get("name"): item.get("value")
        for item in assignments
        if isinstance(item, dict)
    }
    expected_defaults = {
        "dry_run": True,
        "founder_write_approved": False,
        "credentials_configured": False,
        "execution_mode": "OFFLINE",
        "manifest_path": "n8n/config/ATLAS_MASTER_MANIFEST.json",
        "schema_path": "atlas/DOCUMENT_OUTPUT_SCHEMA.json",
        "template_path": "atlas/DOCUMENT_TEMPLATE.md",
    }
    for name, expected in expected_defaults.items():
        if defaults.get(name) != expected:
            raise ValidationError(f"WF-01 default mismatch: {name}")
    if tuple(defaults.get("required_governance_paths", ())) != REQUIRED_RUNTIME_CONTEXT:
        raise ValidationError("WF-01 mandatory governance context list mismatch")

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
        resolver_code = str((resolver or {}).get("parameters", {}).get("jsCode", ""))
        if (
            resolver is None
            or any(f"'{mode}'" not in resolver_code for mode in EXECUTION_MODES)
            or "? requested : 'OFFLINE'" not in resolver_code
            or "dry_run" not in resolver_code
            or "founder_write_approved" not in resolver_code
            or "credentials_configured" not in resolver_code
            or "Resolve Execution Mode"
            not in connection_targets(workflow["connections"], source, 0)
        ):
            metrics["execution_mode_policy_errors"] += 1

    wf2_nodes = {node["name"]: node for node in loaded[EXPECTED_WORKFLOWS[1]]["nodes"]}
    context_code = str(
        wf2_nodes.get("Build Repository Context", {})
        .get("parameters", {})
        .get("jsCode", "")
    )
    required_context_tokens = (
        "Required context read failed",
        "Repository identity mismatch",
        "Branch identity mismatch",
        "Manifest path mismatch",
        "Unknown document ID",
        "Duplicate manifest document ID",
        "Duplicate manifest document path",
        "Unknown dependency ID",
        "Wrong file identity for dependency",
        "Required context is empty",
        "atlas/DOCUMENT_OUTPUT_SCHEMA.json",
        "atlas/DOCUMENT_TEMPLATE.md",
    )
    if any(token not in context_code for token in required_context_tokens):
        metrics["required_context_policy_errors"] += 1
    if "return ''" in context_code or "return \"\"" in context_code:
        metrics["required_context_policy_errors"] += 1

    structural_code = str(
        wf2_nodes.get("Structural Validator", {})
        .get("parameters", {})
        .get("jsCode", "")
    )
    render_code = str(
        wf2_nodes.get("Render Canonical Markdown", {})
        .get("parameters", {})
        .get("jsCode", "")
    )
    contract_tokens = (
        "schema version mismatch",
        "undeclared property",
        "malformed sections",
        "empty required content",
        "invalid document identity",
        "dependencies_used mismatch",
    )
    if any(token not in structural_code for token in contract_tokens):
        metrics["output_contract_policy_errors"] += 1
    if (
        "canonical output is invalid" not in render_code
        or "Template heading missing or duplicated" not in render_code
    ):
        metrics["output_contract_policy_errors"] += 1

    wf2_connections = loaded[EXPECTED_WORKFLOWS[1]]["connections"]
    if (
        "Render Canonical Markdown"
        not in connection_targets(wf2_connections, "Validation Passed?", 0)
        or "LIVE Remote Write Safety Gate"
        not in connection_targets(wf2_connections, "Render Canonical Markdown", 0)
    ):
        metrics["output_contract_policy_errors"] += 1

    wf3_nodes = {node["name"]: node for node in loaded[EXPECTED_WORKFLOWS[2]]["nodes"]}
    guard_code = str(
        wf3_nodes.get("Repair Attempt Guard", {})
        .get("parameters", {})
        .get("jsCode", "")
    )
    for token in (
        "typeof rawAttempt === 'number'",
        "Number.isFinite",
        "Number.isInteger",
        "rawAttempt >= 1",
        "rawAttempt <= 3",
    ):
        if token not in guard_code:
            raise ValidationError("WF-03 repair attempt guard is not fail-closed")
    repair_code = str(
        wf3_nodes.get("Validate Repair", {}).get("parameters", {}).get("jsCode", "")
    )
    if any(token not in repair_code for token in contract_tokens):
        metrics["output_contract_policy_errors"] += 1

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

    for metric in (
        "ungated_external_write_nodes",
        "offline_validate_network_violations",
        "execution_mode_policy_errors",
        "required_context_policy_errors",
        "output_contract_policy_errors",
    ):
        if metrics[metric]:
            raise ValidationError(f"{metric.replace('_', ' ')}: {metrics[metric]}")
    return metrics


def validate_required_context_fixture(fixture: dict[str, Any]) -> None:
    repository = fixture.get("repository")
    expected_repository = fixture.get("expected_repository")
    branch = fixture.get("branch")
    expected_branch = fixture.get("expected_branch")
    if repository != expected_repository:
        raise ValidationError("repository mismatch")
    if branch != expected_branch:
        raise ValidationError("branch mismatch")

    reads = fixture.get("reads")
    if not isinstance(reads, dict):
        raise ValidationError("required reads missing")
    for path in REQUIRED_RUNTIME_CONTEXT:
        value = reads.get(path)
        if not isinstance(value, dict):
            raise ValidationError(f"missing required context: {path}")
        if value.get("ok") is not True:
            raise ValidationError(f"failed repository read: {path}")
        if value.get("path") != path:
            raise ValidationError(f"wrong context path: {path}")
        if not isinstance(value.get("content"), str) or not value["content"].strip():
            raise ValidationError(f"empty required context: {path}")

    manifest = fixture.get("manifest")
    if not isinstance(manifest, dict) or not isinstance(manifest.get("documents"), list):
        raise ValidationError("missing manifest")
    documents = {item.get("id"): item for item in manifest["documents"]}
    document = fixture.get("document")
    if not isinstance(document, dict) or document.get("id") not in documents:
        raise ValidationError("unknown document")
    registered = documents[document["id"]]
    if registered.get("path") != document.get("path"):
        raise ValidationError("wrong document path")
    dependency_files = fixture.get("dependency_files")
    if not isinstance(dependency_files, dict):
        raise ValidationError("dependency files missing")
    for dependency in registered.get("dependencies", []):
        if dependency not in documents or dependency not in dependency_files:
            raise ValidationError(f"missing dependency: {dependency}")
        value = dependency_files[dependency]
        if (
            value.get("ok") is not True
            or value.get("path") != documents[dependency].get("path")
            or dependency not in value.get("content", "")
        ):
            raise ValidationError(f"failed dependency resolution: {dependency}")


def valid_context_fixture() -> dict[str, Any]:
    reads = {
        path: {"ok": True, "path": path, "content": f"Governed content for {path}"}
        for path in REQUIRED_RUNTIME_CONTEXT
    }
    dependency = {
        "id": "GOV-001",
        "path": "00_GOVERNANCE/GOV-001_ENTERPRISE_GOVERNANCE_CONSTITUTION.md",
        "dependencies": [],
    }
    target = {
        "id": "GOV-002",
        "path": "00_GOVERNANCE/GOV-002_FOUNDER_CONTROL_MODEL.md",
        "dependencies": ["GOV-001"],
    }
    return {
        "repository": "owner/repository",
        "expected_repository": "owner/repository",
        "branch": "atlas-drafts",
        "expected_branch": "atlas-drafts",
        "reads": reads,
        "manifest": {"documents": [dependency, target]},
        "document": deepcopy(target),
        "dependency_files": {
            "GOV-001": {
                "ok": True,
                "path": dependency["path"],
                "content": "# GOV-001 — Enterprise Governance Constitution",
            }
        },
    }


def validate_context_fixtures() -> int:
    cases: list[tuple[str, dict[str, Any], bool]] = []
    valid = valid_context_fixture()
    cases.append(("valid", valid, True))

    missing_agents = deepcopy(valid)
    missing_agents["reads"].pop("AGENTS.md")
    cases.append(("missing_agents", missing_agents, False))

    missing_bible = deepcopy(valid)
    missing_bible["reads"].pop("PROJECT_BIBLE.md")
    cases.append(("missing_project_bible", missing_bible, False))

    missing_manifest = deepcopy(valid)
    missing_manifest["manifest"] = None
    cases.append(("missing_manifest", missing_manifest, False))

    missing_dependency = deepcopy(valid)
    missing_dependency["dependency_files"].pop("GOV-001")
    cases.append(("missing_dependency", missing_dependency, False))

    failed_read = deepcopy(valid)
    failed_read["reads"]["AGENTS.md"]["ok"] = False
    cases.append(("failed_repository_read", failed_read, False))

    empty_context = deepcopy(valid)
    empty_context["reads"]["PROJECT_BIBLE.md"]["content"] = " "
    cases.append(("empty_required_context", empty_context, False))

    wrong_path = deepcopy(valid)
    wrong_path["document"]["path"] = "wrong/path.md"
    cases.append(("wrong_document_path", wrong_path, False))

    repository_mismatch = deepcopy(valid)
    repository_mismatch["repository"] = "wrong/repository"
    cases.append(("repository_mismatch", repository_mismatch, False))

    branch_mismatch = deepcopy(valid)
    branch_mismatch["branch"] = "wrong-branch"
    cases.append(("branch_mismatch", branch_mismatch, False))

    for name, fixture, should_pass in cases:
        try:
            validate_required_context_fixture(fixture)
        except ValidationError:
            passed = False
        else:
            passed = True
        if passed != should_pass:
            raise ValidationError(f"Required-context fixture failed expectation: {name}")
    return len(cases)


def valid_repair_attempt(value: Any) -> bool:
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and 1 <= value <= 3
    )


def validate_repair_attempt_fixtures() -> int:
    cases = (
        ("valid_attempt", 1, True),
        ("maximum_attempt", 3, True),
        ("excessive_attempt", 4, False),
        ("nonnumeric_attempt", "two", False),
        ("negative_attempt", -1, False),
        ("null_attempt", None, False),
    )
    for name, value, expected in cases:
        if valid_repair_attempt(value) != expected:
            raise ValidationError(f"Repair-attempt fixture failed expectation: {name}")
    return len(cases)


def scan_for_secrets(paths: set[str]) -> int:
    matches = 0
    for relative in sorted(paths):
        path = ROOT / relative
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        matches += sum(len(pattern.findall(content)) for pattern in SECRET_PATTERNS)
    return matches


def validate_case_collisions(paths: set[str]) -> int:
    by_case: dict[str, list[str]] = {}
    for path in paths:
        by_case.setdefault(path.casefold(), []).append(path)
    collisions = [values for values in by_case.values() if len(set(values)) > 1]
    if collisions:
        raise ValidationError(
            "Case-colliding paths: "
            + "; ".join(" | ".join(sorted(values)) for values in collisions)
        )
    return 0


def validate_ci_configuration() -> None:
    content = read_text(CI_PATH, "GitHub CI workflow")
    parsed, _ = load_yaml(CI_PATH, "GitHub CI workflow")
    if not isinstance(parsed, dict):
        raise ValidationError("GitHub CI workflow must contain a YAML object")
    required = (
        "permissions:",
        "contents: read",
        "PyYAML==6.0.2",
        "python3 scripts/validate_manifest.py",
        "./scripts/validate.sh",
    )
    missing = [token for token in required if token not in content]
    if missing:
        raise ValidationError("CI configuration missing: " + ", ".join(missing))


def main() -> int:
    try:
        manifest, parser_source = load_manifests()
        documents = validate_manifest(manifest)
        registry_mismatches = validate_registry(documents)
        schema = validate_schema_structure(
            load_json(SCHEMA_PATH, "document output schema")
        )
        validate_template()
        output_fixtures = validate_output_fixtures(schema)
        context_fixtures = validate_context_fixtures()
        repair_fixtures = validate_repair_attempt_fixtures()
        workflow_metrics = validate_workflows()
        tracked_paths = git_tracked_paths()
        markdown_links = validate_markdown_links(tracked_paths)
        case_collisions = validate_case_collisions(tracked_paths)
        detected_secrets = scan_for_secrets(tracked_paths)
        if detected_secrets:
            raise ValidationError(f"detected secret values: {detected_secrets}")
        validate_ci_configuration()
    except (OSError, TypeError, ValueError, ValidationError) as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

    print("VALIDATION PASSED")
    print(f"- Manifest parser source: {parser_source}")
    print(f"- Domains: {len(manifest['domains'])}")
    print(f"- Registered documents: {len(documents)}")
    print(f"- Registry mismatches: {registry_mismatches}")
    print("- Duplicate document IDs: 0")
    print("- Duplicate document paths: 0")
    print("- Unknown dependencies: 0")
    print("- Dependency cycles: 0")
    print(f"- Output-contract fixtures: {output_fixtures}")
    print(f"- Required-context fixtures: {context_fixtures}")
    print(f"- Repair-attempt fixtures: {repair_fixtures}")
    print(f"- Markdown local links and anchors checked: {markdown_links}")
    print(f"- Case-colliding paths: {case_collisions}")
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
    print(
        "- Required-context policy errors: "
        f"{workflow_metrics['required_context_policy_errors']}"
    )
    print(
        "- Output-contract policy errors: "
        f"{workflow_metrics['output_contract_policy_errors']}"
    )
    print("- Production URL violations: 0")
    print("- Publishing/deployment nodes: 0")
    print("- CI configuration: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
