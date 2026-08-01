# Current Project State

- **Current date:** 2026-08-01
- **Canonical repository:** `masoudtavousi-collab/damavand-steel-platform`
- **Reviewed input anchor:** `e72c32bdb041448d34c925c969fe01a2156f9e1d`, merged PR #24 PD-03A baseline; successful main CI `30696801759`
- **Live `main` tip:** resolve dynamically from GitHub `refs/heads/main` at task start; do not treat the reviewed input anchor as a permanent live-tip claim
- **Last completed substantive repository integration:** `PD-03A` through merged PR #24 and successful post-merge main CI
- **Last completed governance reconciliation:** PD-03A direct reconciliation through PR #24
- **Current phase:** `PD-03B` Canonical Pilot Records — `DRAFT`
- **Current authorized branch:** `codex/pd-03b-canonical-pilot-records`
- **Current authorization:** maximum 33-path repository-only scope for exactly three canonical Pilot records, dedicated Contract/Schema/Validator/Test, one Approval Evidence, legal lifecycle, and conditional Git integration
- **Merge:** conditional after independent technical PASS, legal `DRAFT → REVIEW → APPROVED`, exact allowlist, successful tests/CI, no conflict or scope drift, Merge Commit, and successful `main` CI
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
| `PD-01` Product Data Contract Enablement | `FD-PD01-001`; `PD01-REVIEW-001`; [PD-01 Scope v1.0](PD01_PRODUCT_DATA_CONTRACT_SCOPE_V1.0.md); exact 30-path allowlist; starting SHA `6577cd461e88463903b18c11b0e5bdbfa88375e2`; PR #21; DRAFT CI `30390311445`; REVIEW CI `30466264564` | `APPROVED` after legal `DRAFT → REVIEW → APPROVED`; synthetic Contract/Schema/Validator/Test enablement only; canonical Product Attribute registry remains empty; no Product, SKU, Master Data, Golden, import, runtime, or production authority |
| `PD-02A` Controlled Values and Attribute Profiles foundation | `FD-PD02A-001`; `PD02A-REVIEW-001`; [PD-02A Scope v1.0](PD02A_CONTROLLED_VALUES_ATTRIBUTE_PROFILES_SCOPE_V1.0.md); exact 38-path allowlist; merged PR #22; successful post-merge validation | `APPROVED` synthetic foundation; its historical empty-registry boundary is preserved and later canonical population requires PD-02B |
| `PD-02B` Minimum Canonical Slice | `FD-PD02B-001`; `PD02B-TECH-REVIEW-001`; [PD-02B Scope v1.0](PD02B_MINIMUM_CANONICAL_SLICE_SCOPE_V1.0.md); exact 57-path allowlist; starting SHA `6ed6fc89e555b1be3a97d7f9c64c9e2b989af1df`; PASS on `f38eb447…`; CI `30479723615` and REVIEW-stage CI `30480571732`; PR #23 | `APPROVED` after legal `DRAFT → REVIEW → APPROVED`; all 31 bounded records are approved; no broader Product/runtime authority |
| `PD-03A` Pilot Prerequisite Foundation | `FD-PD03A-001`; `PD03A-TECH-REVIEW-001`; [PD-03A Scope v1.0](PD03A_PILOT_PREREQUISITE_FOUNDATION_SCOPE_V1.0.md); starting SHA `dd4d4e9dde59ce652edb5b99d2df3e84b56b8031`; PASS on `cb6c817…`; DRAFT CI `30696083295`; REVIEW CI `30696444576`; PR #24; main CI `30696801759`; immutable extension; 50 dispatched mutation cases | `APPROVED`, merged by Merge Commit `e72c32bdb041448d34c925c969fe01a2156f9e1d`, and validated on `main`; exact extension records and Length/Metre/Millimetre are approved; PD-02B aggregate registries/hashes remain unchanged; no canonical Pilot/Product/SKU/availability or runtime authority |
| `PD-03B` Canonical Pilot Records | `FD-PD03B-001`; [PD-03B Scope v1.0](PD03B_CANONICAL_PILOT_SCOPE_V1.0.md); starting SHA `e72c32bdb041448d34c925c969fe01a2156f9e1d`; exact 33-path allowlist; 43 mutation cases | `DRAFT`; exactly three lifecycle-gated Pilot records only. Technical review, REVIEW, final Founder approval, Merge Commit, and main CI remain conditional. No Product/SKU, availability, Master/Golden, import, or runtime authority |
| Atlas planning registry | 173 pending document records across 21 domains | Intake inventory only; no Atlas row is canonical merely because it is registered |

Repository validators are active in CI and unified under `make test`. PR #12 hardening is merged: nested schema objects are closed, JSON Schema Draft 2020-12 is enforced offline, validation output is deterministic, and positive, negative, and adversarial tests are wired into the unified test entry point. `FD-BP2-ADM-001` records the completed legal BP2 lifecycle without implementation authority. `FD-PD01-001` approves a separate synthetic Product Data contract boundary; it is not canonical Product Data.

## Current Product and Knowledge Readiness

### Product Repository

- Machine-readable core, attribute, and measurement foundations exist.
- PD-02B approves only the exact minimum canonical Catalog/Platform/Family, Material/Grade, controlled-term, INTERNAL Profile, localized-label, and evidence slice.
- No Product/SKU records, final SKU vocabulary, Master Data package, Golden reference package, dimensions, Finish/Color/PVD, availability, import, or runtime mapping is authorized.
- Stable structural contracts do not prove commercial truth, availability, import readiness, or runtime readiness.
- Broader Product Data readiness remains **blocked**; the PD-02B minimum slice does not make pilot, Master/Golden, commerce, import, or runtime data ready.
- PD-03A is an APPROVED prerequisite extension only. Its bounded records and
  Length/Metre/Millimetre are approved, but its synthetic tuples remain test
  evidence, not Pilots. PR #24 integration grants no broader authority.
- PD-03B is DRAFT. Its three stable Pilot identities and exact tuples remain
  `CANDIDATE_UNVERIFIED` until independent technical PASS and legal lifecycle
  approval. A Pilot record is not a Product, SKU, Golden package, or availability.

### Knowledge Repository

- Knowledge architecture proposals exist.
- `repository/knowledge/` remains the approved future canonical location.
- No canonical Knowledge contract, content instance, population process, retrieval implementation, or Phase 1 AI capability exists.
- Knowledge implementation depends on stable Product identities and separate authorization.

### Golden Pipe Pilot

- The approved Golden Parent remains `لوله استیل دکوراتیو`.
- Exactly three pilot combinations are approved in Founder decisions and governing prose.
- PD-03B encodes only these three combinations as lifecycle-gated canonical
  Pilot records; while DRAFT, they are not approved repository records.
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
- The BP2 Data Administration contract is `APPROVED` only as a documentation-only administration boundary; it does not grant authority to PD-01 or any administration engine.
- Canonical Product records, Product Attribute definitions, Master Data, Golden package, final SKU/slug policy, content/media rights, and availability evidence remain absent or incomplete.
- PD-01 permits only the exact synthetic Contract/Schema/Validator/Test and governance allowlist; canonical Product Data, BP2 Administration, Runtime, WordPress/WooCommerce, and Knowledge/Content writes remain blocked.
- The ordering conflict between credential containment and mandatory pre-mutation backup/restore evidence remains unresolved.
- Legacy Review-state Product/Content/SEO documents that describe a Variable Parent Product as canonical owner must be reconciled before Knowledge, SEO, or WooCommerce mapping approval.
- A shared role/separation-of-duties matrix and Sprint-specific Test Contract remain required before implementation.
- The recovered Claude export and file packages are historical/private evidence only; raw exports, credentials, Mac inventory reports, legacy runtime code, and superseded repository snapshots are prohibited from repository integration.

## Approved Next Action

Complete only the authorized PD-03B cycle: exact three-record DRAFT,
independent technical review, legal `DRAFT → REVIEW → APPROVED`, exact
Allowlist, successful tests/CI, no conflict or scope drift, Merge Commit, and
successful post-merge `main` CI.

Do not create a Product, fourth Pilot, 879-row set, Master Data, Golden package,
SKU, Slug, availability value, supply promise, Grade 430, PVD, 3m,
WordPress/WooCommerce mapping, import, publication, runtime, deployment,
production mutation, or branch deletion. PD-04 requires separate approval.

## Current References

- [Project Baseline](PROJECT_BASELINE.md)
- [Implementation Readiness](IMPLEMENTATION_READINESS.md)
- [Knowledge Archive Standard](KNOWLEDGE_ARCHIVE_STANDARD.md)
- [K-01 Audit](AUDIT_REPORT_K01.md)
- [Claude Recovery and Repository Consolidation Audit](AUDIT_REPORT_CLAUDE_RECOVERY_2026-07-26.md)
- [BP2 Data Administration Scope v1.0](BP2_DATA_ADMINISTRATION_SCOPE_V1.0.md)
- [PD-02B Minimum Canonical Slice Scope v1.0](PD02B_MINIMUM_CANONICAL_SLICE_SCOPE_V1.0.md)
- [PD-03B Canonical Pilot Records Scope v1.0](PD03B_CANONICAL_PILOT_SCOPE_V1.0.md)
- [Project Execution Roadmap](PROJECT_EXECUTION_ROADMAP.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
- [Open Questions](18_OPEN_QUESTIONS.md)
