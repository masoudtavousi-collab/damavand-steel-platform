# Claude Recovery and Repository Consolidation Audit

## Document Control

- **Date:** 2026-07-26
- **Status:** Draft evidence report; not canonical until Founder-approved repository integration
- **Scope:** Recovered Claude export, recovered Damavand Steel file packages, and comparison with current GitHub `main`
- **Canonical repository:** `masoudtavousi-collab/damavand-steel-platform`
- **Verified current `main`:** `0fb51e5ab2c57ba7ef0f48a12d1fb56f7c2c624f`
- **Runtime impact:** None
- **WordPress / WooCommerce / production impact:** None

## Executive Conclusion

The recovered sources are useful as historical evidence, but none may be copied wholesale into the canonical repository.

The 324-file recovered repository snapshot contains no path that is absent from current `main`. Twenty-four shared files differ because current `main` is newer, and current `main` contains eleven additional paths or path groups. The recovered snapshot must never replace current `main`.

The raw Claude export confirms that the major project ideas are already represented by current canonical documents, current proposal documents, controlled Atlas intake, or explicit future references. Legacy identifiers and embedded status labels do not create current authority.

The material gap is operational-state drift inside the repository: several current-orientation documents still describe K-01 and PR #7 even though PR #9, PR #8, PR #10, and PR #11 were subsequently merged. PR #12 remains Draft and is `NO-GO` for merge pending hardening.

## Source Inventory

| Source | Size | SHA-256 | Finding |
| --- | ---: | --- | --- |
| `DAMAVAND_STEEL_CONTENT_REVIEW.zip` | 1,396,799 bytes | `195d19dd5478d39945ecfb0864475ac0a48c85674942f23d05bab142eb970eea` | 469 ZIP entries; 386 substantive-source entries across several generations plus macOS metadata |
| `DAMAVAND_STEEL_AUDIT_REPORT.zip` | 2,673,570 bytes | `ded010acaaee15a59213f15dcf84358ce89219d023996e073536f52dbec801b7` | Seven local-machine inventory reports; evidence only, not project knowledge |
| Claude export batch ZIP | 2,529,477 bytes | `497e4414666aafa36f428c7ed685154dc1db55c33cc5b7fbbd0b5ea7254669de` | 18 conversations, 743 messages, five Claude projects, and 71 Project Knowledge documents in the primary Damavand project |

## Security Incident and Closure

One plaintext file in the recovered content package contained four real-looking Damavand/CentralSteel WordPress and database credentials:

`new site/7672122527827369730centrals_dam (2)g.txt`

The credential values are intentionally omitted from this report. The Founder confirmed on 2026-07-26 that all four credentials were changed or disabled.

The same credential context also appeared inside the Claude conversation export. Raw conversation exports, `users.json`, local-machine inventory reports, and the plaintext credential file are prohibited from repository integration.

Security disposition:

- Exclude the plaintext credential file from every sanitized package.
- Do not commit raw Claude exports or local-machine inventory reports.
- Do not copy secrets into audit evidence, prompts, logs, patches, commits, or pull requests.
- Keep only the closure statement that the four credentials were changed or disabled.

## Method

1. Validated ZIP integrity.
2. Extracted each source into an isolated audit workspace.
3. Excluded macOS metadata and the known plaintext credential file from eligible content.
4. Scanned text sources for credential-related patterns without reproducing matched values.
5. Cloned current public GitHub `main` and verified commit `0fb51e5`.
6. Compared the recovered repository snapshot path-by-path with current `main`.
7. Compared standalone Atlas and n8n packages with their current repository owners.
8. Parsed Claude conversation metadata, human chronology, project definitions, and 71 Project Knowledge documents.
9. Distinguished explicit Founder statements from pasted AI proposals and embedded labels.
10. Ran `make test` on current `main`.

## Recovered Package Disposition

| Source group | Files | Disposition | Reason |
| --- | ---: | --- | --- |
| `damavand steel/` | 324 | `SUPERSEDED_SNAPSHOT / DO_NOT_COPY` | No recovered-only path; current `main` is newer |
| `DAMAVAND_STEEL_ATLAS_MASTER_MANIFEST/` | 8 | `LEGACY_CONTROLLED_INTAKE` | Current `atlas/` includes K-01 disposition and stronger validation; standalone validator/report are superseded or generated evidence |
| `DAMAVAND_STEEL_N8N_ATLAS_PIPELINE_v1.0/` | 11 | `SUPERSEDED_AUTOMATION_REFERENCE` | Current `n8n/` has the safety model, OFFLINE default, write gates, and reconciled workflows |
| `damavand-enterprise-repository/` | 27 | `QUARANTINED_ARCHITECTURE_RESEARCH` | Already classified by repository governance; conceptual factory/generator research is non-authoritative and not implementation-ready |
| `site-selected/` | 14 | `REJECT_DIRECT_INTEGRATION / ARCHIVE_REFERENCE` | Contains custom runtime code and retail/public-pricing, cart/payment, caching, or implementation assumptions that conflict with current rules |
| `site 2/*.patch` | 1 | `ALREADY_ABSORBED / DO_NOT_REAPPLY` | K-01 governance reconciliation scope was integrated through PR #9 |
| `new site/*credential*.txt` | 1 | `SECURITY_EXCLUDE` | Plaintext credentials; rotated/disabled and prohibited from any clean package |
| `DAMAVAND_STEEL_AUDIT_REPORT.zip` reports | 7 | `LOCAL_MACHINE_EVIDENCE_ONLY` | Inventory, sizes, hashes, repositories, archives, and path reports do not own project truth |
| Raw Claude export | 7 export files | `PRIVATE_SOURCE_EVIDENCE_ONLY` | Contains account metadata, unrelated conversations, duplication, and sensitive context; never repository content |
| Claude Project Knowledge | 71 | `LEGACY_PROMPT/KNOWLEDGE_REFERENCE` | Mostly small prompts, governance fragments, and proposed architecture; current repository owners are stronger and traceable |

## Claude Chronology Rules

### Explicitly voided product input

In `Build Engine Damavand Steel`, the Founder supplied early fitting/product drafts and later explicitly stated:

> تمام این اطلاعات رو عوض کردم یجور دیگه برات میفرستم پس اینا هیچی

Therefore, the early product drafts preceding that correction are invalid as Product/Master Data evidence. They must not populate registries, variants, Product records, or SKUs.

### Embedded labels do not establish authority

Recovered text frequently contains labels such as `APPROVED`, `LOCKED`, `FROZEN`, `ACTIVE`, `Permanent`, or `Canonical`. Many occur inside prompts, generated proposals, or text pasted for review. Those labels do not prove Founder approval.

Only current authoritative repository decisions, explicit Founder decisions with traceable chronology, and current task authorization may govern.

### Legacy identifiers

The Claude material uses legacy identifier families including:

- `AD-*` and `ADR-*`
- `BR-001` through `BR-020`
- `DS-*`, including a proposed `DS-041` through `DS-100` expansion
- `MD-001` through `MD-020`
- `PP-001` through `PP-017`
- `PK-001` through `PK-010`

These identifiers must not be inserted into current decision or canonical-data registries unchanged. Their concepts are mapped to current owners; their legacy status and chronology remain evidence.

## Concept Coverage Mapping

| Claude concept group | Current owner or controlled destination | Disposition |
| --- | --- | --- |
| Repository-first, platform-independent knowledge ownership | `AGENTS.md`, `docs/00_PROJECT_BIBLE.md`, `docs/01_PROJECT_CONSTITUTION.md`, `docs/KNOWLEDGE_ARCHIVE_STANDARD.md` | Covered |
| Product hierarchy and Variable Parent boundary | `docs/19_PRODUCT_DATA_MODEL.md`, `repository/platform/`, `repository/data/`, Founder decisions `FD-W2G-*` | Covered; current hierarchy overrides legacy Product Family-only models |
| Master Data libraries and reusable attributes | `repository/data/attributes/`, registries, contracts, schemas, and Atlas Product intake | Covered structurally; business values remain evidence-gated |
| Product Patterns and family-specific modeling | `repository/engine/product/`, `repository/data/products/`, Atlas Product rows | Covered as architecture/intake; only approved data may populate |
| Product Knowledge, Knowledge Blocks, content, SEO, and publishing consumers | `docs/29_CONTENT_ARCHITECTURE.md`, `docs/34_SEO_ENTITY_MODEL.md`, `repository/knowledge/` future references, content/SEO Atlas rows | Covered as proposal/intake; Knowledge implementation remains gated |
| Inquiry, Quotation, CRM, Representative, Commission, Project, Supplier, and Service concepts | `docs/23_INQUIRY_DATA_MODEL.md`, `docs/42_INQUIRY_WORKFLOW.md`, `repository/business/` future references, Sprint 07A traceability | Covered as governed proposals; no records or runtime created |
| Pricing, Formula, Currency, Inventory, Purchase, Shipping, Bundle, Cross-sell, Up-sell, Alternative, Campaign, and Analytics | Business/commerce future references and Atlas intake | Preserve as future concepts; no formula, price, stock, availability, commission, or commercial fact is approved through Claude text |
| WordPress, WooCommerce, Blocksy Pro, Elementor Pro, Admin manageability | `docs/35_WORDPRESS_BLUEPRINT.md` through `docs/44_PLUGIN_RESPONSIBILITY_MATRIX.md` and current permanent rules | Covered; `site-selected` code is not reusable |
| Deployment, environments, release, monitoring, performance, logging, incidents, maintenance, backup, rollback, and cPanel risks | `docs/operations/`, `docs/security/`, `repository/config/`, remediation and execution-gate documents | Covered as architecture/evidence; runtime remains `NO-GO` |
| CentralSteel ecosystem, Representatives, Installers, Referrals, and Project/Portfolio concepts | enterprise architecture, business entity/lifecycle references, Traceability Matrix | Covered conceptually; no CentralSteel runtime or public entity is authorized |
| AI governance, retrieval, evaluation, memory, agents, and future AI consumers | Knowledge/AI readiness proposals and Atlas intake | Future-only; Phase 1 AI remains prohibited |

## Repository Snapshot Comparison

Comparison of recovered `damavand steel/` with current `main` found:

- Recovered-only paths: `0`
- Current-only paths/path groups: `11`
- Shared files with different content: `24`
- Current repository test result: `PASS`
- Current Atlas rows: `173`
- Current Atlas domains: `21`
- Secret detection on current `main`: `0`
- Active n8n workflows on current `main`: `0`

The recovered repository snapshot is fully superseded as a repository source.

## Confirmed Current-State Drift

Current `main` is `0fb51e5`, but several orientation files still describe the earlier K-01 / PR #7 state. This is an actual repository gap, not a reason to restore old files.

Required scoped reconciliation:

| Path | Required action |
| --- | --- |
| `docs/CURRENT_PROJECT_STATE.md` | Replace stale mutable state with PR #11 merged baseline, completed BP1/BP2 evidence, Claude recovery audit state, and PR #12 Draft `NO-GO` blockers |
| `docs/PROJECT_BASELINE.md` | Remove stale K-01 active-phase/next-action claims and defer mutable details to Current Project State |
| `docs/08_DOCUMENTATION_INDEX.md` | Update orientation banner and index this audit |
| `docs/09_NAVIGATION_MAP.md` | Replace stale K-01 current path with current reading path |
| `docs/PROJECT_EXECUTION_ROADMAP.md` | Update active-phase and next-action language without rewriting historical phases |
| `docs/IMPLEMENTATION_READINESS.md` | Replace K-01 exit action with current BP2/admin-hardening and recovery-consolidation gates |
| `docs/READING_ORDER.md` | Replace K-01-specific current reading instructions with the current controlled path |
| `docs/REPOSITORY_RELATIONSHIP_MAP.md` | Replace stale active K-01 state while retaining historical relationships |
| `docs/KNOWLEDGE_ARCHIVE_STANDARD.md` | Clarify that K-01 was integrated while lifecycle approval remains separately recorded; do not infer approval from merge alone |
| `docs/14_CHANGELOG.md` | Append the recovery/consolidation evidence entry |

Historical K-01 audit records, commit edges, and dated baseline evidence must remain unchanged.

## PR #12 Boundary

PR #12 is open, Draft, and mergeable at GitHub, but project governance keeps it `NO-GO` for merge until:

- nested JSON Schema objects are closed against unknown fields;
- the contract is truly validated against JSON Schema Draft 2020-12 offline;
- positive validation tests exist;
- negative and adversarial tests exist;
- every test is wired into `make test`;
- no WordPress, WooCommerce, Product/SKU, publication, deployment, or production scope is added.

Recovery consolidation and PR #12 hardening must remain separate scopes.

## Recommended Integration Plan

1. Obtain Founder approval for a dedicated branch such as `codex/claude-recovery-consolidation`.
2. Add this report as evidence only.
3. Apply the targeted current-state reconciliation above without rewriting historical audit evidence.
4. Add no raw Claude export, machine-inventory report, credential file, legacy code, old repository snapshot, or standalone legacy workflow.
5. Run secret scanning, repository validators, `make test`, JSON validation, link checks, and `git diff --check`.
6. Present the exact diff before staging, commit, push, or Draft PR.
7. After consolidation is reviewed, return to PR #12 hardening as an independent task.

## GO / NO-GO

**GO**

- Preserve the original sources outside the repository.
- Keep a sanitized recovery package without the plaintext credential file or macOS metadata.
- Prepare a scoped repository reconciliation diff on a dedicated branch after Founder approval.
- Keep this report evidence-only until integrated through the approved Git process.

**NO-GO**

- Copying the recovered repository over current `main`.
- Reapplying the old patch.
- Importing `site-selected` code.
- Treating embedded legacy status labels as Founder approval.
- Importing voided product drafts.
- Committing raw Claude exports, user/account metadata, Mac inventory reports, or credentials.
- Merging PR #12.
- WordPress, WooCommerce, Product/SKU, import, publishing, deployment, or production mutation.
