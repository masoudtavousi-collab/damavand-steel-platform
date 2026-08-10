# Usage Summary — {{mission_id}}

Render this exact `usage_summary` object from the corresponding mission record;
do not create a second source of truth.

```yaml
cycle_id: "{{cycle_id}}"
mission_id: "{{mission_id}}"
task_id: null
task_result: PASS | PARTIAL | BLOCKED | FAIL
elapsed_seconds: 0
activity_metric_refs:
  files_read: { value: 0, observability: OBSERVED }
  files_changed: { value: 0, observability: OBSERVED }
  commands_run: { value: 0, observability: OBSERVED }
  tests_run: { value: 0, observability: OBSERVED }
  ci_runs: { value: 0, observability: OBSERVED }
  commits_created: { value: 0, observability: OBSERVED }
  prs_created_or_updated: { value: 0, observability: OBSERVED }
test_ci_refs:
  tests_run: { value: 0, observability: OBSERVED }
  ci_runs: { value: 0, observability: OBSERVED }
blocker_reason_code: NONE
forecast:
  status: INSUFFICIENT_DATA
  reason_code: FEWER_THAN_TWO_REAL_CYCLES
  source_snapshot_ids: []
  source_cycle_ids: []
  meter_id: null
  usage_window_instance_id: null
  observed_delta_percent: null
  elapsed_days: null
  rate_percent_per_day: null
  uncertainty_code: NONE
```

This v1 register accepts only `INSUFFICIENT_DATA`. `ESTIMATE` is fail-closed
until a separately approved register-wide resolver can verify real,
user-reported snapshots and reproducible arithmetic. Do not estimate Tokens,
Credits, model, reasoning level, or Usage.
