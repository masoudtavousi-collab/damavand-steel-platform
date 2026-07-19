# Codex Sprint Protocol

## Current Wave 1 Execution Boundary

The Founder authorization dated 2026-07-19 permits Class B Wave 1 only: controlled reconciliation and integration of the exact 19 approved governance paths on `codex/class-b-wave-01-governance`, one commit, push of only that branch, and one Draft PR. Mixed-tree work outside the allowlist must remain unstaged and preserved. PR #1 must remain unchanged. Merge, Wave 2–10, runtime, workflow execution or activation, WordPress, product, content, publication, deployment, production, repository-setting, and default-branch changes remain `NO-GO`.

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
