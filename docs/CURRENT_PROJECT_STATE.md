# Current Project State

- **Current date:** 2026-07-26
- **Canonical repository:** `masoudtavousi-collab/damavand-steel-platform`
- **Verified `main` baseline:** `0fb51e5ab2c57ba7ef0f48a12d1fb56f7c2c624f`
- **Last completed repository integration:** BP2 Machine-Readable Data Blueprint, merged by PR #11
- **Current phase:** Claude Recovery and Repository Consolidation
- **Current authorized branch:** `codex/claude-recovery-consolidation`
- **Current authorization:** recovery audit and reconciliation are committed and pushed in Draft PR #13; validation and CI review are authorized, while Ready for Review, merge, and any additional scope remain unauthorized
- **Merge:** NO-GO; PR #13 remains Draft pending validation and CI review, while PR #12 remains Draft and separately blocked pending contract/schema/validator hardening
- **Runtime / WordPress / WooCommerce mutation:** NO-GO
- **Import / publishing / deployment / product creation / bulk SKU generation:** NO-GO

This file is the only operational current-state pointer. Other documents may preserve dated evidence, but must link here instead of repeating a mutable SHA, active branch, or next action.

## Completed Repository Foundations

| Foundation | Evidence | Current meaning |
| --- | --- | --- |
| Wave 2A — Product Core | PR #5; `product-core` contract, schema, entity-type/status registries, validator, and fixtures | Platform-independent structural foundation exists; no Product, Golden, SKU, commercial, import, or runtime record was created |
| Wave 2B — Product Attributes | PR #6; `product-attribute` contract, schema, controlled supporting registries, validator, and fixtures | Attribute-definition foundation exists; canonical Product Attribute registry remains empty and no business values were approved |
| Wave 2C — Measurements | PR #7; measurement contract/schema, two candidate dimensions, four candidate units, validator, and fixtures | Measurement infrastructure exists; entries are `CANDIDATE_UNVERIFIED` and do not assert Product values, weight, availability, pricing, or runtime mappings |
| K-01 — Governance and Knowledge Reconciliation | PR #9; current-state ownership, Knowledge Archive Standard, Atlas disposition, and unified local/CI validation | Governance reconciliation is integrated; merge does not promote Atlas rows, Product facts, or lifecycle approval |
| BP1 — Visible Local Prototype | PR #10; Persian RTL local prototype, inquiry-first preview, local design tokens, and safety validator | Local review evidence only; it is not a WordPress implementation, production site, or Product truth source |
| BP2 — Machine-Readable Data Blueprint | PR #11; controlled Pipe blueprint, schema, offline validator, three approved pilot decisions, and 879 historical candidates | Data-administration design input exists; it creates no final SKU, import, publication, WordPress, WooCommerce, or production authority |
| Atlas planning registry | 173 pending document records across 21 domains | Intake inventory only; no Atlas row is canonical merely because it is registered |

Repository validators are active in CI and unified under `make test`. PR #12 adds a proposed BP2 administration scope, but remains Draft and `NO-GO` for merge until its schema, validator, and positive/negative/adversarial tests are hardened.

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
- PR #12 must close nested schema objects against unknown fields, validate the contract offline against JSON Schema Draft 2020-12, add positive and negative/adversarial tests, and wire all tests into `make test`.
- The recovered Claude export and file packages are historical/private evidence only; raw exports, credentials, Mac inventory reports, legacy runtime code, and superseded repository snapshots are prohibited from repository integration.

## Approved Next Action

On branch `codex/claude-recovery-consolidation`, keep Draft PR #13 limited to the recovery audit and the ten authorized status/navigation documents. Correct this current-state pointer, rerun repository validation, push the exact one-file correction, and inspect the resulting GitHub Actions and PR checks.

Then stop. Ready for Review and merge require separate explicit authorization. PR #12 hardening remains a separate scope. Do not begin Product/Knowledge population, WordPress work, runtime work, import, publishing, deployment, or production mutation.

## Current References

- [Project Baseline](PROJECT_BASELINE.md)
- [Implementation Readiness](IMPLEMENTATION_READINESS.md)
- [Knowledge Archive Standard](KNOWLEDGE_ARCHIVE_STANDARD.md)
- [K-01 Audit](AUDIT_REPORT_K01.md)
- [Claude Recovery and Repository Consolidation Audit](AUDIT_REPORT_CLAUDE_RECOVERY_2026-07-26.md)
- [Project Execution Roadmap](PROJECT_EXECUTION_ROADMAP.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
- [Open Questions](18_OPEN_QUESTIONS.md)
