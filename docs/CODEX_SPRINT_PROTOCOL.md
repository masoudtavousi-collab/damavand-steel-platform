# Codex Sprint Protocol

## Current-State Boundary

[Current Project State](CURRENT_PROJECT_STATE.md) is the sole source for the active branch, baseline SHA, authorization, next action, and GO/NO-GO boundary. Historical sprint permissions remain evidence within their original exact scope and must not be presented as current authority.

For K-01, the Founder authorized governance/current-state reconciliation, Atlas disposition, unified tests, one scoped commit, push of only `codex/k-01-governance-knowledge-reconciliation`, and one Draft PR against `main`. Autonomous merge, Wave 2D, Product/Knowledge population, workflow execution or activation, runtime, WordPress, import, publication, deployment, production mutation, and repository-setting changes remain `NO-GO`.

## Standard Prompt Structure

```text
MODE
TASK
OBJECTIVE
SOURCE FILES
CREATE
UPDATE
DO
DO NOT
VALIDATE
OUTPUT
GO / NO-GO
```

## Mandatory Rules

- One objective per sprint; no silent scope expansion or automatic next sprint.
- Do not duplicate architecture. Corrections update files in place; no V2 duplication unless explicitly requested.
- Technically valid does not mean commercially approved.
- Every commercially meaningful row needs provenance and status.
- Every output declares whether it is scaffold, candidate, approved, import-ready, and runtime-ready.
- Large generation requires explicit evidence. Cartesian generation never implies validity.
- Do not disguise missing values as approval. Founder decisions must be genuine decisions, not missing operational values.

## Compact Output Format

```text
Created:
Updated:
Validated:
Resolved:
Unresolved:
Founder Decisions:
GO:
NO-GO:
```

## Correction Sprint Rules

- Modify only affected files and preserve traceability.
- Do not rebuild unrelated assets.
- Recalculate affected quality/readiness scores.
- Create one audit report unless otherwise requested.
- For a mixed working tree, stage only an explicit approved path allowlist and verify exact set equality before commit.

## Asset Sprint Rules

- Produce directly usable implementation assets; prefer YAML/CSV.
- Avoid unnecessary prose and speculative values.
- No runtime unless explicitly authorized.

## Runtime Sprint Rules

Explicit approval, verified backup, documented rollback, minimal reversible scope, and post-change validation are mandatory. Stop on unexpected state.
