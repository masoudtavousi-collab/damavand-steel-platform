# Codex Sprint Protocol

## Current Wave 2 Pre-Implementation Reconciliation Boundary

Bootstrap PR #1, Wave 1 Governance PR #2, and Post-merge Governance Reconciliation PR #3 are merged. Canonical/default `main` is verified at `d702c5217f7caa2f23e56f965f3f993967e3c17d`; main protection and required `repository-validation` are active. Wave 1 and the read-only Wave 2 discovery are complete. Historically, the 2026-07-19 Founder authorization permitted the exact Wave 1 branch/commit/push/Draft-PR sequence while merge remained prohibited; that chronology must remain intact.

The current Founder authorization permits documentation-only Wave 2 pre-implementation reconciliation on `codex/wave-2-preimplementation-reconciliation`, one commit, push of only that branch, and one Draft PR against `main`. Wave 2A is proposed but not authorized or started. The approved next action is Founder review and merge decision for this documentation PR, followed by a separate Wave 2A authorization decision. Autonomous merge, workflow execution or activation, runtime, WordPress, Product/Knowledge Repository implementation, publication, deployment, production mutation, and repository-setting changes remain `NO-GO`.

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
