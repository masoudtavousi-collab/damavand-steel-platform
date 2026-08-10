#!/usr/bin/env python3
"""Fail-closed validation for the local Agentic Usage Register."""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CYCLE_PATH = ROOT / "docs/operations/agentic-usage/cycles/2026-c01.yaml"
SCHEMA_PATH = ROOT / "docs/operations/agentic-usage/agentic_usage.schema.yaml"
METRIC_KEYS = {"value", "observability"}
ACTIVITY_KEYS = {"files_read", "files_changed", "commands_run", "tests_run", "ci_runs", "commits_created", "prs_created_or_updated"}
TEST_CI_KEYS = {"tests_run", "ci_runs"}
REDACTED_NOTE_CODES = {"FOUNDER_REPORTED", "NO_EXTERNAL_CALLS", "LOCAL_VALIDATION", "APPROVAL_RECORDED", "SCOPE_REVIEWED", "NO_GIT_MUTATION", "BLOCKED_BY_SCOPE"}
BLOCKER_REASON_CODES = {"NONE", "VALIDATION_FAILED", "SCOPE_BLOCKED", "DEPENDENCY_UNAVAILABLE", "EXTERNAL_APPROVAL_REQUIRED"}
FORECAST_REASON_CODES = {"FEWER_THAN_TWO_REAL_CYCLES", "REGISTER_WIDE_RESOLVER_UNAVAILABLE"}
FORECAST_UNCERTAINTY_CODES = {"NONE", "USER_REPORTED_SNAPSHOT", "REGISTER_WIDE_RESOLVER_UNAVAILABLE"}


class ValidationError(ValueError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def load_yaml(path: Path) -> Any:
    raw = path.read_text(encoding="utf-8")

    class UniqueKeyLoader(yaml.SafeLoader):
        pass

    def construct_mapping(loader: yaml.SafeLoader, node: yaml.Node, deep: bool = False) -> dict[str, Any]:
        mapping: dict[str, Any] = {}
        for key_node, value_node in node.value:  # type: ignore[attr-defined]
            key = loader.construct_object(key_node, deep=deep)
            if key in mapping:
                fail(f"DUPLICATE_KEY:{key}")
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)
    try:
        return yaml.load(raw, Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        fail(f"MALFORMED_YAML:{exc}")


def exact_keys(value: Any, allowed: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"TYPE:{label}")
    extra, missing = set(value) - allowed, allowed - set(value)
    if extra or missing:
        fail(f"KEYS:{label}:missing={sorted(missing)}:extra={sorted(extra)}")
    return value


def utc_timestamp(value: Any, label: str) -> dt.datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        fail(f"TIMESTAMP:{label}")
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        fail(f"TIMESTAMP:{label}")


def text_or_null(value: Any, label: str, required: bool = False) -> None:
    if required:
        if not isinstance(value, str) or not value:
            fail(f"TEXT:{label}")
    elif value is not None and (not isinstance(value, str) or not value):
        fail(f"TEXT:{label}")


def redacted_note(value: Any, label: str) -> None:
    if value is not None and (not isinstance(value, str) or len(value) > 280 or not value or any(code not in REDACTED_NOTE_CODES for code in value.split(";"))):
        fail(f"REDACTION:{label}")


def number_or_null(value: Any, label: str, nonnegative: bool = True) -> None:
    if value is not None and (not isinstance(value, (int, float)) or isinstance(value, bool) or (nonnegative and value < 0)):
        fail(f"NUMBER:{label}")


def validate_metric(value: Any, label: str, percent: bool = False) -> None:
    metric = exact_keys(value, METRIC_KEYS, label)
    observed, number = metric["observability"], metric["value"]
    if observed == "OBSERVED":
        number_or_null(number, label)
        if number is None or (percent and (not isinstance(number, int) or number > 100)):
            fail(f"METRIC_VALUE:{label}")
    elif observed == "NOT_OBSERVABLE":
        if number is not None:
            fail(f"METRIC_NULL:{label}")
    else:
        fail(f"METRIC_OBSERVABILITY:{label}")


def validate_snapshot(snapshot: Any) -> None:
    keys = {"snapshot_id", "snapshot_at", "weekly_usage_remaining_percent", "purchased_credits_remaining", "source", "reported_by", "plan_label", "meter_id", "usage_window_instance_id", "observed_input_local", "notes"}
    item = exact_keys(snapshot, keys, "snapshot")
    if not isinstance(item["snapshot_id"], str) or not re.fullmatch(r"US-\d{4}-\d{3}", item["snapshot_id"]):
        fail("SNAPSHOT_ID")
    utc_timestamp(item["snapshot_at"], "snapshot")
    validate_metric(item["weekly_usage_remaining_percent"], "weekly_usage_remaining_percent", percent=True)
    validate_metric(item["purchased_credits_remaining"], "purchased_credits_remaining")
    if item["source"] != "ChatGPT Usage and limits" or item["reported_by"] != "USER_REPORTED":
        fail("SNAPSHOT_PROVENANCE")
    for field in ("plan_label", "meter_id", "observed_input_local"):
        text_or_null(item[field], f"snapshot.{field}", required=True)
    text_or_null(item["usage_window_instance_id"], "snapshot.usage_window_instance_id")
    redacted_note(item["notes"], "snapshot.notes")


def validate_observable_text(item: dict[str, Any], value_key: str, observability_key: str, label: str) -> None:
    observed, value = item[observability_key], item[value_key]
    if observed == "OBSERVED":
        text_or_null(value, label, required=True)
    elif observed in {"UNKNOWN", "NOT_OBSERVABLE"}:
        if value is not None:
            fail(f"OBSERVABILITY_NULL:{label}")
    else:
        fail(f"OBSERVABILITY:{label}")


def validate_forecast(value: Any) -> None:
    keys = {"status", "reason_code", "source_snapshot_ids", "source_cycle_ids", "meter_id", "usage_window_instance_id", "observed_delta_percent", "elapsed_days", "rate_percent_per_day", "uncertainty_code"}
    item = exact_keys(value, keys, "forecast")
    if item["status"] not in {"ESTIMATE", "INSUFFICIENT_DATA"}:
        fail("FORECAST_STATUS")
    if item["reason_code"] not in FORECAST_REASON_CODES:
        fail("FORECAST_REASON_CODE")
    if item["uncertainty_code"] not in FORECAST_UNCERTAINTY_CODES:
        fail("FORECAST_UNCERTAINTY_CODE")
    snapshots, cycles = item["source_snapshot_ids"], item["source_cycle_ids"]
    if not isinstance(snapshots, list) or not all(isinstance(v, str) and v for v in snapshots):
        fail("FORECAST_SNAPSHOTS")
    if not isinstance(cycles, list) or not all(re.fullmatch(r"\d{4}-c\d{2}", v) for v in cycles if isinstance(v, str)) or not all(isinstance(v, str) for v in cycles):
        fail("FORECAST_CYCLES")
    numeric = ("observed_delta_percent", "elapsed_days", "rate_percent_per_day")
    for key in numeric:
        number_or_null(item[key], f"forecast.{key}")
    if item["status"] == "ESTIMATE":
        # This one-cycle register cannot resolve source IDs across real cycles.
        # Reject estimates until a separately approved register-wide resolver and
        # arithmetic contract exist; accepting caller-supplied values is unsafe.
        fail("FORECAST_ESTIMATE_UNAVAILABLE")
    elif snapshots or cycles or item["meter_id"] is not None or item["usage_window_instance_id"] is not None or any(item[key] is not None for key in numeric):
        fail("FORECAST_INSUFFICIENT_DATA")


def validate_mission(mission: Any, cycle_id: str) -> None:
    keys = {"cycle_id", "mission_id", "task_id", "started_at", "finished_at", "elapsed_seconds", "model_used", "model_observability", "reasoning_level", "reasoning_observability", "execution_surface", "activity_metrics", "task_result", "blocker_reason_code", "notes", "usage_summary"}
    item = exact_keys(mission, keys, "mission")
    if item["cycle_id"] != cycle_id or not isinstance(item["mission_id"], str) or not item["mission_id"]:
        fail("MISSION_ID")
    text_or_null(item["task_id"], "mission.task_id")
    started, finished = utc_timestamp(item["started_at"], "mission.started_at"), utc_timestamp(item["finished_at"], "mission.finished_at")
    number_or_null(item["elapsed_seconds"], "mission.elapsed_seconds")
    if item["elapsed_seconds"] is None or started > finished or item["elapsed_seconds"] != (finished - started).total_seconds():
        fail("MISSION_ELAPSED")
    validate_observable_text(item, "model_used", "model_observability", "mission.model_used")
    validate_observable_text(item, "reasoning_level", "reasoning_observability", "mission.reasoning_level")
    if item["execution_surface"] not in {"Work", "Codex", "other"}:
        fail("EXECUTION_SURFACE")
    metrics = exact_keys(item["activity_metrics"], ACTIVITY_KEYS, "activity_metrics")
    for key in ACTIVITY_KEYS:
        validate_metric(metrics[key], f"activity_metrics.{key}")
    if item["task_result"] not in {"PASS", "PARTIAL", "BLOCKED", "FAIL"}:
        fail("TASK_RESULT")
    if item["blocker_reason_code"] not in BLOCKER_REASON_CODES:
        fail("BLOCKER_REASON_CODE")
    if (item["task_result"] == "PASS") != (item["blocker_reason_code"] == "NONE"):
        fail("BLOCKER_REASON")
    redacted_note(item["notes"], "mission.notes")
    validate_usage_summary(item["usage_summary"], item)


def validate_usage_summary(summary: Any, mission: dict[str, Any]) -> None:
    keys = {"cycle_id", "mission_id", "task_id", "task_result", "elapsed_seconds", "activity_metric_refs", "test_ci_refs", "blocker_reason_code", "forecast"}
    item = exact_keys(summary, keys, "usage_summary")
    for key in ("cycle_id", "mission_id", "task_id", "task_result", "elapsed_seconds", "blocker_reason_code"):
        if item[key] != mission[key]:
            fail(f"SUMMARY_DERIVATION:{key}")
    if item["activity_metric_refs"] != mission["activity_metrics"]:
        fail("SUMMARY_DERIVATION:activity_metrics")
    if exact_keys(item["test_ci_refs"], TEST_CI_KEYS, "test_ci_refs") != {key: mission["activity_metrics"][key] for key in TEST_CI_KEYS}:
        fail("SUMMARY_DERIVATION:test_ci_refs")
    validate_forecast(item["forecast"])


def validate_cycle(cycle: Any) -> None:
    item = exact_keys(cycle, {"schema_version", "cycle_id", "usage_snapshots", "mission_records"}, "cycle")
    if item["schema_version"] != 1 or not isinstance(item["cycle_id"], str) or not re.fullmatch(r"\d{4}-c\d{2}", item["cycle_id"]):
        fail("CYCLE_ID")
    if not isinstance(item["usage_snapshots"], list) or not isinstance(item["mission_records"], list):
        fail("CYCLE_ARRAY")
    snapshot_ids, mission_ids = set(), set()
    for snapshot in item["usage_snapshots"]:
        validate_snapshot(snapshot)
        if snapshot["snapshot_id"] in snapshot_ids:
            fail("DUPLICATE_SNAPSHOT_ID")
        snapshot_ids.add(snapshot["snapshot_id"])
    for mission in item["mission_records"]:
        validate_mission(mission, item["cycle_id"])
        if mission["mission_id"] in mission_ids:
            fail("DUPLICATE_MISSION_ID")
        mission_ids.add(mission["mission_id"])


def validate_schema(schema: Any) -> None:
    keys = {
        "schema_version", "contract", "top_level_cycle_keys", "snapshot_required_keys",
        "metric_keys", "observability_values", "model_observability_values",
        "mission_required_keys", "activity_metric_keys", "usage_summary_required_keys",
        "forecast_required_keys", "task_result_values", "execution_surface_values",
        "forecast_status_values", "blocker_reason_code_values", "forecast_reason_code_values",
        "forecast_uncertainty_code_values", "redacted_note_code_values", "rules",
    }
    item = exact_keys(schema, keys, "schema")
    expected = {
        "top_level_cycle_keys": {"schema_version", "cycle_id", "usage_snapshots", "mission_records"},
        "snapshot_required_keys": {"snapshot_id", "snapshot_at", "weekly_usage_remaining_percent", "purchased_credits_remaining", "source", "reported_by", "plan_label", "meter_id", "usage_window_instance_id", "observed_input_local", "notes"},
        "metric_keys": METRIC_KEYS,
        "observability_values": {"OBSERVED", "NOT_OBSERVABLE"},
        "model_observability_values": {"OBSERVED", "UNKNOWN", "NOT_OBSERVABLE"},
        "mission_required_keys": {"cycle_id", "mission_id", "task_id", "started_at", "finished_at", "elapsed_seconds", "model_used", "model_observability", "reasoning_level", "reasoning_observability", "execution_surface", "activity_metrics", "task_result", "blocker_reason_code", "notes", "usage_summary"},
        "activity_metric_keys": ACTIVITY_KEYS,
        "usage_summary_required_keys": {"cycle_id", "mission_id", "task_id", "task_result", "elapsed_seconds", "activity_metric_refs", "test_ci_refs", "blocker_reason_code", "forecast"},
        "forecast_required_keys": {"status", "reason_code", "source_snapshot_ids", "source_cycle_ids", "meter_id", "usage_window_instance_id", "observed_delta_percent", "elapsed_days", "rate_percent_per_day", "uncertainty_code"},
        "task_result_values": {"PASS", "PARTIAL", "BLOCKED", "FAIL"},
        "execution_surface_values": {"Work", "Codex", "other"},
        "forecast_status_values": {"ESTIMATE", "INSUFFICIENT_DATA"},
        "blocker_reason_code_values": BLOCKER_REASON_CODES,
        "forecast_reason_code_values": FORECAST_REASON_CODES,
        "forecast_uncertainty_code_values": FORECAST_UNCERTAINTY_CODES,
        "redacted_note_code_values": REDACTED_NOTE_CODES,
    }
    if item["schema_version"] != 1 or item["contract"] != "agentic_usage_register":
        fail("SCHEMA_VERSION")
    for key, required in expected.items():
        if not isinstance(item[key], list) or set(item[key]) != required or len(item[key]) != len(required):
            fail(f"SCHEMA_CONTRACT:{key}")
    if not isinstance(item["rules"], list) or not item["rules"] or not all(isinstance(v, str) and v for v in item["rules"]):
        fail("SCHEMA_CONTRACT:rules")


def main() -> int:
    schema = load_yaml(SCHEMA_PATH)
    validate_schema(schema)
    validate_cycle(load_yaml(CYCLE_PATH))
    print(f"AGENTIC_USAGE_VALIDATION_PASS: {CYCLE_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"AGENTIC_USAGE_VALIDATION_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
