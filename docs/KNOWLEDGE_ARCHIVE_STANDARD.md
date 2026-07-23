# Knowledge Archive Standard

## Document Control

- **Document ID:** `docs/KNOWLEDGE_ARCHIVE_STANDARD.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-23
- **Lifecycle:** Review
- **Source of Truth:** Current repository evidence, accepted governing rules, explicit Founder decisions, and K-01 reconciliation
- **Approval:** Pending Founder review of the K-01 Draft PR

## Purpose

Define one non-duplicative archive structure for decisions, architecture, Product/Knowledge truth, delivery evidence, Atlas intake, and historical records. This standard changes no runtime system and does not promote Draft, Review, candidate, or archived material.

## Archive Layers

| Layer | Canonical purpose | Current locations | May govern? |
| --- | --- | --- | --- |
| 1. Control | Current state, source priority, decisions, open questions, accepted ADRs, execution gates | `docs/CURRENT_PROJECT_STATE.md`, `docs/PROJECT_BASELINE.md`, `docs/10_DECISION_LOG.md`, `docs/17_FOUNDER_DECISION_LOG.md`, `docs/18_OPEN_QUESTIONS.md`, `docs/adr/` | Yes, only within recorded status and authority |
| 2. Architecture | Business, enterprise, Product, Knowledge, WordPress, UX, SEO, content, security, and operations models | Governing/review documents under `docs/` and approved standards under `repository/` | Only when approved within exact scope |
| 3. Canonical Data | Machine-readable contracts, schemas, registries, validation, future Master Data, and Golden references | `repository/data/` | Contracts govern structure; records govern facts only after approval |
| 4. Delivery | Implementation assets, adapters, configuration, tests, and CI | `repository/implementation-assets/`, `repository/wordpress/`, `config/`, `scripts/`, `tests/`, `.github/workflows/` | Derived implementation only; never owns Product/Knowledge truth |
| 5. Controlled Intake | Planned Atlas documents and adoption decisions | `atlas/` | No; intake is noncanonical until mapped, reviewed, and approved |
| 6. Evidence Archive | Audits, snapshots, reports, historical prompts, and superseded records | `docs/AUDIT_REPORT_*`, dated reports, and explicitly marked archive references | No; evidence only |

Physical relocation or deletion is a separate destructive-change decision. K-01 classifies material but does not move or delete historical files.

## One Owner Per Kind of Truth

| Truth kind | Canonical owner | Duplication rule |
| --- | --- | --- |
| Mutable operational state | `docs/CURRENT_PROJECT_STATE.md` | Other documents link here; do not copy current SHA, branch, or next action |
| Concise project orientation | `docs/PROJECT_BASELINE.md` | Summarizes and links; does not replace detailed decisions |
| Decision index | `docs/10_DECISION_LOG.md` | Indexes decisions; never creates or reinterprets them |
| Founder decisions | `docs/17_FOUNDER_DECISION_LOG.md` | Only explicit Founder decisions are recorded as such |
| Unresolved decisions | `docs/18_OPEN_QUESTIONS.md` | Missing operational data is not automatically a Founder question |
| Architecture | The most specific approved architecture document | A broader document links to the owner instead of restating it |
| Product structure | `repository/data/contracts/`, `schemas/`, and `registries/` | WordPress/WooCommerce mappings are downstream |
| Product facts | Future approved `repository/data/master-data/` | Candidate matrices, audits, and Atlas plans cannot override it |
| Golden reference | Future approved `repository/data/golden-reference/` | Pilot prose and legacy matrices remain evidence until packaged and approved |
| Knowledge instances | Future approved `repository/knowledge/` | Atlas plans and generated documents cannot self-promote |
| Historical evidence | Original dated record | Preserve chronology; add a current-status banner or link rather than rewriting history |

## Status Vocabularies

The following vocabularies must remain separate:

| Vocabulary | Applies to | Examples |
| --- | --- | --- |
| Document lifecycle | Documents | `Draft`, `Review`, `Approved`, `Deprecated`, `Archived` |
| Product/Master Data status | Product facts and governed values | `APPROVED`, `CANDIDATE_UNVERIFIED`, `MISSING_DATA_VALUE`, `FOUNDER_INPUT_REQUIRED`, `DEFERRED`, `NOT_APPLICABLE`, `INVALID` |
| Execution readiness | Actions and environments | `GO`, `CONDITIONAL_GO`, `NO-GO`, `BLOCKED` |
| Atlas adoption disposition | Planned documents | `MAP_TO_EXISTING`, `ADOPT`, `MERGE`, `DEFER`, `REJECT`, `ARCHIVE_REFERENCE` |

No status in one vocabulary implies a status in another. For example, a valid contract may still contain no approved Product facts, and a merged PR does not itself prove the originating Founder authorization.

## Conflict Resolution

When two records conflict:

1. Check authority and exact scope, not filename or recency alone.
2. Prefer explicit accepted governing decisions over proposals and evidence.
3. Prefer the current-state pointer for mutable operational facts.
4. Preserve dated evidence without allowing it to control the present.
5. Record the conflict in the decision/open-question system when authority is unresolved.
6. Stop before implementation if the conflict affects Product truth, customer-facing behavior, security, runtime, import, publishing, or production.

## Atlas Adoption Rules

Every Atlas row must have one disposition in `atlas/ATLAS_ADOPTION_MATRIX.csv`.

- `MAP_TO_EXISTING`: an existing canonical owner already covers the purpose; do not generate a duplicate.
- `ADOPT`: no adequate owner exists; create only after exact Founder approval.
- `MERGE`: useful unique content should be merged into a named owner after review.
- `DEFER`: retain as planned intake; no generation or authority.
- `REJECT`: concept conflicts with controlling rules or has no project value.
- `ARCHIVE_REFERENCE`: preserve only as historical/reference material.

All 173 current Atlas registry rows begin as controlled intake. K-01 may map obvious duplicates, but no `pending` row becomes canonical through this matrix alone.

## Legacy Library Atlas Rule

Legacy files with identifiers such as `ATLAS-000`, `ATLAS-006`, `ATLAS-008`, or `ATLAS-020` use an older namespace and may contain stale product hierarchy, lifecycle, or authority claims. They are classified `ARCHIVE_REFERENCE / NONCANONICAL` unless a later path-level adoption decision maps specific content into Repository A.

They must not:

- override `GOV-*`, `FND-*`, or other current Atlas registry IDs;
- override the canonical Product hierarchy;
- call themselves canonical for Repository A;
- create Product, Knowledge, WordPress, runtime, publication, or AI authority.

## Review Cadence

Review this standard whenever a current-state owner, decision register, canonical path, Atlas disposition, archive policy, or status vocabulary changes. Validation should detect duplicate current-state claims and ensure all Atlas rows have a disposition.

## Navigation

- [Current Project State](CURRENT_PROJECT_STATE.md)
- [Project Baseline](PROJECT_BASELINE.md)
- [Decision Log](10_DECISION_LOG.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
- [Open Questions](18_OPEN_QUESTIONS.md)
- [Repository Reading Order](READING_ORDER.md)
- [Atlas Legacy Disposition](../atlas/LEGACY_ATLAS_DISPOSITION.md)
