# Current Project State

- **Current date:** 2026-07-23
- **Canonical repository:** `masoudtavousi-collab/damavand-steel-platform`
- **Verified `main` baseline:** `ed0841bcd46d315dba8c4ecfd64b1eb105048da5`
- **Last completed repository integration:** Wave 2C Measurement Foundation, merged by PR #7
- **Current phase:** K-01 Governance and Knowledge Reconciliation
- **Current authorized branch:** `codex/k-01-governance-knowledge-reconciliation`
- **Current authorization:** reconcile governance/current-state documents, classify Atlas intake, unify repository tests, create one commit, push this branch, and open one Draft PR
- **Merge:** NO-GO pending Founder review
- **Runtime / WordPress / WooCommerce mutation:** NO-GO
- **Import / publishing / deployment / product creation / bulk SKU generation:** NO-GO

This file is the only operational current-state pointer. Other documents may preserve dated evidence, but must link here instead of repeating a mutable SHA, active branch, or next action.

## Completed Repository Foundations

| Foundation | Evidence | Current meaning |
| --- | --- | --- |
| Wave 2A — Product Core | PR #5; `product-core` contract, schema, entity-type/status registries, validator, and fixtures | Platform-independent structural foundation exists; no Product, Golden, SKU, commercial, import, or runtime record was created |
| Wave 2B — Product Attributes | PR #6; `product-attribute` contract, schema, controlled supporting registries, validator, and fixtures | Attribute-definition foundation exists; canonical Product Attribute registry remains empty and no business values were approved |
| Wave 2C — Measurements | PR #7; measurement contract/schema, two candidate dimensions, four candidate units, validator, and fixtures | Measurement infrastructure exists; entries are `CANDIDATE_UNVERIFIED` and do not assert Product values, weight, availability, pricing, or runtime mappings |
| Atlas planning registry | 173 pending document records across 21 domains | Intake inventory only; no Atlas row is canonical merely because it is registered |

All Wave 2A–2C validators are active in CI. The local `make test` entry point is being reconciled in K-01 to run the same foundation checks.

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

## Approved Next Action

Complete K-01 on `codex/k-01-governance-knowledge-reconciliation`, run repository validation and unified tests, create one scoped commit, push only that branch, and open one Draft PR against `main`.

Then stop for Founder review. Do not merge autonomously and do not begin Wave 2D, Product/Knowledge population, WordPress work, runtime work, import, publishing, deployment, or production mutation.

## Current References

- [Project Baseline](PROJECT_BASELINE.md)
- [Implementation Readiness](IMPLEMENTATION_READINESS.md)
- [Knowledge Archive Standard](KNOWLEDGE_ARCHIVE_STANDARD.md)
- [K-01 Audit](AUDIT_REPORT_K01.md)
- [Project Execution Roadmap](PROJECT_EXECUTION_ROADMAP.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
- [Open Questions](18_OPEN_QUESTIONS.md)
