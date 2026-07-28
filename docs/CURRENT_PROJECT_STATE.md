# Current Project State

- **Current date:** 2026-07-28
- **Canonical repository:** `masoudtavousi-collab/damavand-steel-platform`
- **Reviewed input anchor:** `b391ca1632d4a7d266e33aa5e279e214941901ae`, PR #19 Merge Commit; successful post-merge CI run `30372385447`
- **Live `main` tip:** resolve dynamically from GitHub `refs/heads/main` at task start; do not treat the reviewed input anchor as a permanent live-tip claim
- **Last completed substantive repository integration:** BP2 Data Administration Lifecycle Approval, integrated by PR #18
- **Last completed governance reconciliation:** post-PR18 reconciliation, integrated by PR #19
- **Current phase:** `GOV-XD-00` Cross-Domain Execution Charter complete when the PR carrying this declaration merges; no implementation sprint active
- **Current authorized branch:** no Product, Knowledge, Admin UI, or runtime implementation branch is authorized
- **Current authorization:** read-only preparation of an exact `PD-01` decision package only; `PD-01` execution is not authorized
- **Merge:** no merge after the PR carrying `GOV-XD-00` is authorized without a new exact Founder approval
- **Runtime / WordPress / WooCommerce mutation:** NO-GO
- **Import / publishing / deployment / product creation / bulk SKU generation:** NO-GO

This file is the only semantic operational-state pointer. Other documents may preserve dated evidence, but must link here instead of repeating mutable authorization or next-action claims.

## Git State Resolution Rules

- The state declared in this file becomes effective only when the PR carrying it is merged to GitHub `main`.
- `main` is a symbolic branch reference. Its exact SHA must be resolved from GitHub at the start of every task and recorded in that task's Scope/Approval Packet.
- A SHA stored in repository prose is a dated `reviewed input anchor` or historical event reference, not the permanent live tip.
- A Merge Commit SHA is a stable content-addressed identifier. PR metadata and post-merge CI are related GitHub evidence, but their mutability and retention follow GitHub and repository policy; evidence requiring long-term preservation must be captured in an approved durable artifact or record.
- A normal Git-tip change does not require a documentation reconciliation. Update this file only when phase, authorization, gate state, next action, or GO/NO-GO changes.
- An annotated baseline tag may be proposed later when immutable baseline naming is needed; tag creation requires separate Founder approval.

## Completed Repository Foundations

| Foundation | Evidence | Current meaning |
| --- | --- | --- |
| Wave 2A — Product Core | PR #5; `product-core` contract, schema, entity-type/status registries, validator, and fixtures | Platform-independent structural foundation exists; no Product, Golden, SKU, commercial, import, or runtime record was created |
| Wave 2B — Product Attributes | PR #6; `product-attribute` contract, schema, controlled supporting registries, validator, and fixtures | Attribute-definition foundation exists; canonical Product Attribute registry remains empty and no business values were approved |
| Wave 2C — Measurements | PR #7; measurement contract/schema, two candidate dimensions, four candidate units, validator, and fixtures | Measurement infrastructure exists; entries are `CANDIDATE_UNVERIFIED` and do not assert Product values, weight, availability, pricing, or runtime mappings |
| K-01 — Governance and Knowledge Reconciliation | PR #9; current-state ownership, Knowledge Archive Standard, Atlas disposition, and unified local/CI validation | Governance reconciliation is integrated; merge does not promote Atlas rows, Product facts, or lifecycle approval |
| BP1 — Visible Local Prototype | PR #10; Persian RTL local prototype, inquiry-first preview, local design tokens, and safety validator | Local review evidence only; it is not a WordPress implementation, production site, or Product truth source |
| BP2 — Machine-Readable Data Blueprint | PR #11; controlled Pipe blueprint, schema, offline validator, three approved pilot decisions, and 879 historical candidates | Data-administration design input exists; it creates no final SKU, import, publication, WordPress, WooCommerce, or production authority |
| Claude Recovery and Repository Consolidation | PR #13; recovery audit and reconciliation of current-state and navigation documents | Recovery evidence is classified and governance sources are reconciled; no recovered runtime, credential, Product, publication, deployment, or production authority was introduced |
| Post-Recovery Current State | PR #14; current-state pointer aligned to the completed recovery baseline and the then-open PR #12 review boundary | Historical bridge between PR #13 and PR #12; it granted no Product, runtime, import, publication, deployment, or production authority |
| BP2 — Data Administration Contract Lifecycle | PR #12, `FD-BP2-ADM-001`, `BP2-ADM-REVIEW-001`, and merged PR #18; administration scope, contract, closed Draft 2020-12 schema, deterministic offline validator, and positive/negative/adversarial tests | The contract completed `DRAFT → REVIEW → APPROVED`; it governs only the documentation-only BP2 administration boundary and implementation authority remains false |
| Post-PR12 Governance Reconciliation | PR #15; active state, baseline, readiness, roadmap, index, navigation, health, traceability, changelog, and open-question alignment | Removes obsolete PR #12 merge blockers from active documents while preserving historical audits and all Product/runtime `NO-GO` boundaries |
| BP1 — M1 Accessibility and Local Validation Hardening | PR #16; primary-CTA contrast correction, fail-closed contrast validation, reproducible local setup, and unified local/CI test entry point | Closes the recorded BP1 M1 contrast and validation-tooling gaps; the prototype remains local-only evidence and creates no WordPress, WooCommerce, Product/SKU, import, publication, deployment, or production authority |
| Post-PR16 Governance Reconciliation | PR #17; active state, baseline, roadmap, repository relationship, index, navigation, health, traceability, changelog, and open-question alignment | Records the PR #16 completion and removes its closed blocker while preserving the BP2 `DRAFT` lifecycle and all Product/runtime `NO-GO` boundaries |
| Post-PR18 Governance Reconciliation | PR #19; direct governance and current-state alignment after PR #18 | Closes the BP2 lifecycle integration cycle and returns the project to read-only next-step planning without implementation authority |
| `GOV-XD-00` Cross-Domain Execution Charter | Founder authorization dated 2026-07-28; six-task read-only analysis; independent QA; the PR carrying this declaration | Separates semantic operational state from the dynamic Git tip, records cross-domain dependency order and separation of duties, and selects `PD-01` only as the next decision-package target |
| Atlas planning registry | 173 pending document records across 21 domains | Intake inventory only; no Atlas row is canonical merely because it is registered |

Repository validators are active in CI and unified under `make test`. PR #12 hardening is merged: nested schema objects are closed, JSON Schema Draft 2020-12 is enforced offline, validation output is deterministic, and positive, negative, and adversarial tests are wired into the unified test entry point. `FD-BP2-ADM-001` records the completed legal `DRAFT → REVIEW → APPROVED` sequence; this lifecycle approval does not authorize implementation.

## Current Product and Knowledge Readiness

### Product Repository

- Machine-readable core, attribute, and measurement foundations exist.
- No canonical Product entity rows, Product Attribute definitions, final SKU vocabulary, Master Data package, or Golden reference package exists on `main`.
- Stable structural contracts do not prove commercial truth, availability, import readiness, or runtime readiness.
- Product Data readiness remains **blocked** pending governed records, evidence, approvals, and later exact-scope implementation.

### Knowledge Repository

- Knowledge architecture proposals exist.
- `repository/knowledge/` remains the approved future canonical location.
- No canonical Knowledge contract, content instance, population process, retrieval implementation, or Phase 1 AI capability exists.
- Knowledge implementation depends on stable Product identities and separate authorization.

### Golden Pipe Pilot

- The approved Golden Parent remains `لوله استیل دکوراتیو`.
- Exactly three pilot combinations are approved in Founder decisions and governing prose.
- Their `GOLD-PIPE-*` identifiers are pilot references, not final commercial SKUs.
- The other 879 combinations remain `CANDIDATE_UNVERIFIED`.
- Availability remains `MISSING_DATA_VALUE` for all 882 rows.
- Brand remains approved absent/hidden; weight remains `DEFERRED`.
- No canonical machine-readable Golden or Master Data package exists.

## Canonical Architecture Boundary

The canonical Product hierarchy is:

```text
Catalog → Platform → Family → Series → Variant Rules → SKU
```

WooCommerce is downstream:

```text
Canonical Product model → Variable Parent Product → evidence-backed valid variations
```

A Variable Parent Product is a commerce presentation and never the owner of canonical Product truth.

## Knowledge-Archive Boundary

- Current operational truth: this document.
- Concise orientation: [Project Baseline](PROJECT_BASELINE.md).
- Decisions: [Decision Log](10_DECISION_LOG.md), [Founder Decision Log](17_FOUNDER_DECISION_LOG.md), accepted ADRs, and [Open Questions](18_OPEN_QUESTIONS.md).
- Repository knowledge structure: [Knowledge Archive Standard](KNOWLEDGE_ARCHIVE_STANDARD.md).
- Atlas intake: [Atlas Adoption Matrix](../atlas/ATLAS_ADOPTION_MATRIX.csv).
- Historical audits and superseded snapshots: evidence only; they cannot override current state.
- Legacy Library Atlas files named `ATLAS-*` are archive references, not canonical Repository A documents.

## Current Blockers

- Final Product records, Product Attribute definitions, SKU vocabulary, approved commercial combinations, and availability evidence are incomplete.
- Media files, rights, final content, relations, and compatibility remain incomplete.
- Authenticated WordPress/cPanel evidence, isolated staging, verified backup/restore, rollback ownership, and exact target approval are absent.
- Product-level suppression of public price, Offer schema, cart, and checkout remains unproven.
- Blocksy Pro and Elementor Pro package/license compatibility remains unresolved.
- Atlas rows require controlled adoption decisions before any content generation or promotion.
- Historical authorization evidence for Wave 2A and Wave 2B is not explicitly linked in the current Founder Decision Log; merge history is implementation evidence, not a substitute for the originating authorization record.
- The BP2 Data Administration contract is `APPROVED` only as a documentation-only administration boundary; a separate exact-scope Founder decision is still required before any administration implementation or Product Data sprint.
- Canonical Product records, Product Attribute definitions, Master Data, Golden package, final SKU/slug policy, content/media rights, and availability evidence remain absent or incomplete.
- Product Data, BP2 Administration, Runtime, WordPress/WooCommerce, and Knowledge/Content plans are all blocked from writing until their own exact Founder authorization and domain gates pass.
- The ordering conflict between credential containment and mandatory pre-mutation backup/restore evidence remains unresolved.
- Legacy Review-state Product/Content/SEO documents that describe a Variable Parent Product as canonical owner must be reconciled before Knowledge, SEO, or WooCommerce mapping approval.
- A shared role/separation-of-duties matrix and Sprint-specific Test Contract remain required before implementation.
- The recovered Claude export and file packages are historical/private evidence only; raw exports, credentials, Mac inventory reports, legacy runtime code, and superseded repository snapshots are prohibited from repository integration.

## Approved Next Action

Prepare one exact, read-only `PD-01` decision package for Founder review. It may define objective, proposed allowlist, Contract/Schema/Validator/Test scope, synthetic fixtures, risks, stop conditions, and conditional Git controls. It must not create or modify any Product Data, Contract, Schema, Validator, Test, Branch, PR, or runtime asset.

Do not modify BP1, populate Product/Knowledge data, implement an Admin UI, change WordPress/WooCommerce, run imports, publish, deploy, delete the branch, or mutate production.

## Current References

- [Project Baseline](PROJECT_BASELINE.md)
- [Implementation Readiness](IMPLEMENTATION_READINESS.md)
- [Knowledge Archive Standard](KNOWLEDGE_ARCHIVE_STANDARD.md)
- [K-01 Audit](AUDIT_REPORT_K01.md)
- [Claude Recovery and Repository Consolidation Audit](AUDIT_REPORT_CLAUDE_RECOVERY_2026-07-26.md)
- [BP2 Data Administration Scope v1.0](BP2_DATA_ADMINISTRATION_SCOPE_V1.0.md)
- [Project Execution Roadmap](PROJECT_EXECUTION_ROADMAP.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
- [Open Questions](18_OPEN_QUESTIONS.md)
