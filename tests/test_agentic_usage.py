from __future__ import annotations

import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate_agentic_usage.py"
SPEC = importlib.util.spec_from_file_location("agentic_usage_validator", SCRIPT)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class AgenticUsageTests(unittest.TestCase):
    def valid_mission(self) -> dict:
        metric = {"value": 0, "observability": "OBSERVED"}
        metrics = {key: copy.deepcopy(metric) for key in validator.ACTIVITY_KEYS}
        return {
            "cycle_id": "2026-c01", "mission_id": "AUTF-001", "task_id": None,
            "started_at": "2026-08-09T09:35:00Z", "finished_at": "2026-08-09T09:35:30Z",
            "elapsed_seconds": 30.0, "model_used": None, "model_observability": "UNKNOWN",
            "reasoning_level": None, "reasoning_observability": "NOT_OBSERVABLE",
            "execution_surface": "Codex", "activity_metrics": metrics, "task_result": "PASS",
            "blocker_reason_code": "NONE", "notes": None,
            "usage_summary": {
                "cycle_id": "2026-c01", "mission_id": "AUTF-001", "task_id": None,
                "task_result": "PASS", "elapsed_seconds": 30.0,
                "activity_metric_refs": copy.deepcopy(metrics), "blocker_reason_code": "NONE",
                "test_ci_refs": {key: copy.deepcopy(metrics[key]) for key in validator.TEST_CI_KEYS},
                "forecast": {
                    "status": "INSUFFICIENT_DATA", "reason_code": "FEWER_THAN_TWO_REAL_CYCLES",
                    "source_snapshot_ids": [], "source_cycle_ids": [], "meter_id": None,
                    "usage_window_instance_id": None, "observed_delta_percent": None,
                    "elapsed_days": None, "rate_percent_per_day": None, "uncertainty_code": "NONE",
                },
            },
        }

    def test_canonical_cycle_is_valid(self) -> None:
        validator.validate_cycle(validator.load_yaml(validator.CYCLE_PATH))

    def test_duplicate_yaml_key_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text("a: 1\na: 2\n", encoding="utf-8")
            with self.assertRaises(validator.ValidationError):
                validator.load_yaml(path)

    def test_unobserved_metric_requires_null(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        cycle["usage_snapshots"][0]["weekly_usage_remaining_percent"] = {
            "value": 100,
            "observability": "NOT_OBSERVABLE",
        }
        with self.assertRaises(validator.ValidationError):
            validator.validate_cycle(cycle)

    def test_out_of_range_percent_is_rejected(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        cycle["usage_snapshots"][0]["weekly_usage_remaining_percent"]["value"] = 101
        with self.assertRaises(validator.ValidationError):
            validator.validate_cycle(cycle)

    def test_complete_mission_record_is_valid(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        cycle["mission_records"].append(self.valid_mission())
        validator.validate_cycle(cycle)

    def test_unknown_mission_key_is_rejected(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        mission = self.valid_mission()
        mission["invented"] = "forbidden"
        cycle["mission_records"].append(mission)
        with self.assertRaises(validator.ValidationError):
            validator.validate_cycle(cycle)

    def test_summary_must_be_derived_from_mission(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        mission = self.valid_mission()
        mission["usage_summary"]["elapsed_seconds"] = 31
        cycle["mission_records"].append(mission)
        with self.assertRaises(validator.ValidationError):
            validator.validate_cycle(cycle)

    def test_summary_test_ci_refs_must_match_activity_metrics(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        mission = self.valid_mission()
        mission["usage_summary"]["test_ci_refs"]["ci_runs"]["value"] = 1
        cycle["mission_records"].append(mission)
        with self.assertRaisesRegex(validator.ValidationError, "SUMMARY_DERIVATION:test_ci_refs"):
            validator.validate_cycle(cycle)

    def test_raw_notes_are_rejected_and_redacted_codes_are_allowed(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        mission = self.valid_mission()
        mission["notes"] = "FOUNDER_REPORTED;NO_EXTERNAL_CALLS"
        cycle["mission_records"].append(mission)
        validator.validate_cycle(cycle)
        mission["notes"] = "curl https://example.invalid token=secret"
        with self.assertRaisesRegex(validator.ValidationError, "REDACTION:mission.notes"):
            validator.validate_cycle(cycle)

    def test_uppercase_pii_and_credential_shaped_notes_are_rejected(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        for note in ("MASOUD_TAVOUSI", "AKIAIOSFODNN7EXAMPLE"):
            mission = self.valid_mission()
            mission["notes"] = note
            cycle["mission_records"] = [mission]
            with self.assertRaisesRegex(validator.ValidationError, "REDACTION:mission.notes"):
                validator.validate_cycle(cycle)

    def test_notes_over_280_characters_are_rejected(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        mission = self.valid_mission()
        mission["notes"] = "A" * 281
        cycle["mission_records"].append(mission)
        with self.assertRaisesRegex(validator.ValidationError, "REDACTION:mission.notes"):
            validator.validate_cycle(cycle)

    def test_reason_codes_must_use_closed_enums(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        mission = self.valid_mission()
        mission["blocker_reason_code"] = "ARBITRARY_INPUT"
        cycle["mission_records"].append(mission)
        with self.assertRaisesRegex(validator.ValidationError, "BLOCKER_REASON_CODE"):
            validator.validate_cycle(cycle)
        mission = self.valid_mission()
        mission["usage_summary"]["forecast"]["reason_code"] = "ARBITRARY_INPUT"
        cycle["mission_records"] = [mission]
        with self.assertRaisesRegex(validator.ValidationError, "FORECAST_REASON_CODE"):
            validator.validate_cycle(cycle)
        mission["usage_summary"]["forecast"]["reason_code"] = "FEWER_THAN_TWO_REAL_CYCLES"
        mission["usage_summary"]["forecast"]["uncertainty_code"] = "ARBITRARY_INPUT"
        with self.assertRaisesRegex(validator.ValidationError, "FORECAST_UNCERTAINTY_CODE"):
            validator.validate_cycle(cycle)

    def test_forecast_requires_two_real_cycles(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        mission = self.valid_mission()
        forecast = mission["usage_summary"]["forecast"]
        forecast.update({
            "status": "ESTIMATE", "source_snapshot_ids": ["US-2026-001", "US-2026-002"],
            "source_cycle_ids": ["2026-c01"], "meter_id": "weekly-agentic-usage",
            "usage_window_instance_id": "window-1", "observed_delta_percent": 10,
            "elapsed_days": 7, "rate_percent_per_day": 1.42,
        })
        cycle["mission_records"].append(mission)
        with self.assertRaises(validator.ValidationError):
            validator.validate_cycle(cycle)

    def test_estimate_is_fail_closed_even_with_forged_observed_inputs(self) -> None:
        cycle = validator.load_yaml(validator.CYCLE_PATH)
        mission = self.valid_mission()
        forecast = mission["usage_summary"]["forecast"]
        forecast.update({
            "status": "ESTIMATE", "source_snapshot_ids": ["US-2026-001", "US-2026-999"],
            "source_cycle_ids": ["2026-c01", "2026-c02"], "meter_id": "weekly-agentic-usage",
            "usage_window_instance_id": "window-1", "observed_delta_percent": 10,
            "elapsed_days": 7, "rate_percent_per_day": 1.42,
        })
        cycle["mission_records"].append(mission)
        with self.assertRaisesRegex(validator.ValidationError, "FORECAST_ESTIMATE_UNAVAILABLE"):
            validator.validate_cycle(cycle)

    def test_schema_contract_drift_is_rejected(self) -> None:
        schema = validator.load_yaml(validator.SCHEMA_PATH)
        schema["task_result_values"].append("MAYBE")
        with self.assertRaises(validator.ValidationError):
            validator.validate_schema(schema)


if __name__ == "__main__":
    unittest.main()
