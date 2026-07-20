# Codex Sprint Protocol

## Current Post-Merge Reconciliation Boundary

Bootstrap PR #1 and Wave 1 Governance PR #2 are merged. Canonical `main` is verified at `4a0f229107716a1b9f7f825f5cd5f16ea78a1b26`, and Wave 1 is complete. Historically, the 2026-07-19 Founder authorization permitted the exact Wave 1 branch/commit/push/Draft-PR sequence while merge remained prohibited; that chronology must remain intact.

The current Founder authorization permits documentation-only post-merge baseline reconciliation on `codex/post-merge-governance-reconciliation`, one commit, push of only that branch, and one Draft PR against `main`. Wave 2 has not started and remains unauthorized. Merge of the reconciliation PR, workflow execution or activation, runtime, WordPress, Product Repository implementation, publication, deployment, production mutation, repository-setting changes, and default-branch changes remain `NO-GO`.

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
