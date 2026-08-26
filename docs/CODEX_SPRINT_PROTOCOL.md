# Codex Sprint Protocol

## Current-State Boundary

[Current Project State](CURRENT_PROJECT_STATE.md) is the sole source for the semantic phase, authorization, next action, and GO/NO-GO boundary. The live `main` SHA is not stored as permanent current state: resolve GitHub `refs/heads/main` at dispatch time and record the exact starting SHA in the Sprint Scope/Approval Packet. Historical sprint permissions and fixed SHAs remain dated evidence within their original exact scope and must not be presented as current authority.

For K-01, the Founder authorized governance/current-state reconciliation, Atlas disposition, unified tests, one scoped commit, push of only `codex/k-01-governance-knowledge-reconciliation`, and one Draft PR against `main`. Autonomous merge, Wave 2D, Product/Knowledge population, workflow execution or activation, runtime, WordPress, import, publication, deployment, production mutation, and repository-setting changes remain `NO-GO`.

For `GOV-XD-00`, the Founder authorized only the eleven-path governance allowlist recorded in `FD-GOV-XD-00`, one scoped Branch/Commit/Push/Draft-PR cycle, independent review, conditional Merge Commit, and post-merge `main` CI. This authorization ends when that cycle closes and grants no `PD-01`, Product Data, BP2 implementation, Knowledge, WordPress/WooCommerce, import, runtime, deployment, production, or branch-deletion authority.

## Pre-Mutation Context Gate

Conversation, memory, and handoffs are not Project authority. Before any mutation, Codex must independently resolve live GitHub `main`, inspect the local branch and working-tree state, determine live active writer Missions/open pull requests, classify ownership, verify `MAX_ACTIVE_WIP = 3`, check path collisions, load the [Context Router](CONTEXT_ROUTER.md) route, establish its bounded role, and record a complete Task Context Envelope:

```text
authority
live_main_sha
objective
role
allowed_paths_and_systems
explicit_no_go
dependencies
required_sources
stop_conditions
validation
return_contract
active_writer_wip_verification
material_artifact_custody_plan
checkpoint_triggers
authority_boundary
```

Every field must be resolved from the applicable Repository sources and active Mission. If material authority, state, source ownership, scope, custody, checkpoint handling, or a required field remains unresolved, Codex must return `STOP — CONTEXT_NOT_ESTABLISHED` and perform no Repository mutation. A handoff that says “approved” does not pass this gate.

Before starting a new writer Mission, enumerate active writers live rather than copying PR numbers into stable files. If no WIP slot exists, return `STOP — WIP_LIMIT_REACHED`. An already-authorized active lane may continue without consuming a new slot only if ownership remains exact and its paths do not collide with another active writer.

## Baseline and Approval Packet

Every dispatched Sprint must record:

- the exact GitHub `main` starting SHA resolved at dispatch time;
- one objective and exact path/system allowlist;
- role, required sources, exclusions, stop conditions, and expected evidence;
- named executor, independent reviewer, Founder approval boundary, and rollback owner where applicable;
- live active-writer ownership, WIP count/limit, and path-collision result;
- the material-artifact custody plan and checkpoint triggers;
- a Sprint-specific Test Contract covering positive, negative, boundary, adversarial, cross-file, and fail-closed behavior in proportion to risk; and
- explicit Git, data, runtime, and production permissions as separate gates.

Changing the live Git tip alone does not trigger a Current Project State update. A state-document change is required only when semantic phase, authorization, next action, gate state, or GO/NO-GO changes.

## Artifact Custody and WIP Checkpoints

The Repository is the Project/Product source of truth only for approved structured truth, governance, stable identities, and repository-admissible manifests or references. Raw source artifacts and private, sensitive, commercial, verifier, and recovery/checkpoint artifacts belong in approved durable external custody. Custody location never creates authority.

Every material artifact and checkpoint follows:

```text
Generate → Hash → Classify → Manifest → Preserve → Read Back → Report
```

A checkpoint is required at a phase boundary, planned pause, handoff, session-loss exposure, or major integration. If durable custody cannot be preserved and read back, report `PENDING_EXTERNAL_ARCHIVE`. A checkpoint does not approve work, grant Merge authority, promote Product truth, or authorize a successor Mission.

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
- Completion, a recommendation, a handoff, or an instruction to “continue” does not authorize the next Mission; stop unless it is separately authorized.
- A checkpoint, artifact hash, archive locator, review result, or available WIP slot does not authorize the next Mission.
- Separate executor, independent reviewer, and Founder approval authority; no self-review or self-approval.
- Codex preserves approved architecture during implementation. A potentially better architecture is reported as a separate proposal and is not applied without approval.
- Claude research, UX/design review, red-team review, and specification critique are proposals or review evidence until the authorized project process reconciles them.
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
