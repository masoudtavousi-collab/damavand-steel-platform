# Founder Decision Log

## Document Control

- **Document ID:** `docs/17_FOUNDER_DECISION_LOG.md` (provisional path identifier)
- **Status:** Draft
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.21.0
- **Last Updated:** 2026-08-18
- **Last Review:** 2026-08-18
- **Review Cycle:** On Founder decision creation, resolution, supersession, or dependency change
- **Lifecycle:** Draft
- **Source of Truth:** Explicit Founder-decision requirements in controlled source documents; this log is an index only
- **Dependencies:** [Decision Log](10_DECISION_LOG.md), [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md)
- **Related Documents:** [Open Questions](18_OPEN_QUESTIONS.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), and [Review Process](15_REVIEW_PROCESS.md)
- **Traceability:** Founder-decision ID, source, status, resulting authority, and resolution evidence
- **AI Compatibility:** AI-readable with gaps until Founder approval
- **Approval:** Pending Founder approval

## Purpose

Index every repository item explicitly marked as requiring a Founder decision. This log does not decide or reinterpret any item.

## Governance Decisions Required

| ID | Decision required | Source | Status |
| --- | --- | --- | --- |
| FD-GOV-001 | Assign approval authority by document category. | [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md) | Resolved: Founder |
| FD-GOV-002 | Approve the documentation versioning rule. | [Document Template](13_DOCUMENT_TEMPLATE.md) and [Git Governance](GIT_GOVERNANCE.md#versioning-strategy) | Pending |
| FD-GOV-003 | Approve repository release versioning and its relationship to document versions. | [Changelog Policy](14_CHANGELOG_POLICY.md) and [Git Governance](GIT_GOVERNANCE.md#versioning-strategy) | Pending |
| FD-GOV-004 | Assign architecture, business, technical, documentation, and final review authorities. | [Review Process](15_REVIEW_PROCESS.md) | Resolved for Batch 02A: Repository Guardian reviews; Founder approves |
| FD-GOV-005 | Approve project steel-industry terminology with a qualified subject-matter expert. | [Glossary](11_GLOSSARY.md) | Pending |
| FD-GOV-006 | Approve, revise, or reject the modular documentation numbering strategy. | [Repository Standards](07_REPOSITORY_GUIDE.md#numbering-scalability-proposal) | Pending |
| FD-GOV-007 | Approve the repository baseline and authorize creation of the first exact baseline commit, manifest, and tag. | [Repository Baseline v1.0](BASELINE_v1.0.md) and [Git Governance](GIT_GOVERNANCE.md#baseline-strategy) | Resolved for the exact local v1.0.0 baseline by Founder task directive dated 2026-07-04; remote/mirror/backup/signing remain unresolved |
| FD-GOV-008 | Determine the disposition of the existing Blocksy child-theme placeholder under CP-007 No Custom Theme. | [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) and [existing placeholder](../public/wp-content/themes/blocksy-child/README.md) | Pending; no theme implementation authorized |
| FD-GOV-009 | Approve, revise, or reject the AI Collaboration Standard. | [AI Collaboration Standard](AI_COLLABORATION.md) | Pending; repository collaboration only |
| FD-GOV-010 | Approve, revise, or reject the Repository Metadata Standard. | [Repository Metadata Standard](REPOSITORY_METADATA.md) | Pending |
| FD-GOV-011 | Approve, revise, or reject the Repository Traceability Matrix as the supporting traceability view. | [Traceability Matrix](TRACEABILITY_MATRIX.md) | Pending |
| FD-GOV-012 | Approve, revise, or reject the role-based Repository Reading Order. | [Reading Order](READING_ORDER.md) | Pending |
| FD-GOV-013 | Approve, revise, or reject the Repository Knowledge Graph relationship vocabulary and authority layers. | [Knowledge Graph](KNOWLEDGE_GRAPH.md) | Pending |
| FD-GOV-014 | Approve, revise, or reject the Decision Classification Framework. | [Decision Classification Framework](10_DECISION_LOG.md#decision-classification-framework) | Pending |
| FD-GOV-015 | Approve, revise, or reject the expanded document lifecycle and repository state-transition model. | [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md) | Pending |
| FD-GOV-016 | Approve, revise, or reject the relationship vocabulary, rule-inheritance hierarchy, and conflict-resolution framework. | [Relationship Metadata](REPOSITORY_METADATA.md#relationship-metadata-model) and [Project Constitution](01_PROJECT_CONSTITUTION.md#governance-rule-inheritance) | Pending |
| FD-GOV-017 | Approve, revise, or reject the Controlled Document Validation Checklist and repository validation gate. | [Documentation Quality Standard](16_QUALITY_STANDARD.md#controlled-document-validation-checklist) | Pending |
| FD-GOV-018 | Approve, revise, or reject the expanded AI change-authority and repository-protection rules. | [AI Collaboration Standard](AI_COLLABORATION.md#ai-change-authority-matrix) | Pending; repository collaboration only |
| FD-GOV-019 | Approve, revise, or reject Git Governance, including branch, merge, tag, commit, release, backup, freeze, validation, remote, mirror, custody, and retention rules. | [Git Governance](GIT_GOVERNANCE.md) | Pending; the proposal grants no Git mutation. `FD-GIT-W1-001` separately authorizes only its exact Wave 1 actions. |

## Architecture Decisions Required

| ID | Decision required | Source | Status |
| --- | --- | --- | --- |
| FD-ARC-001 | Approve, revise, or reject WP-ARC-001 through WP-ARC-012 as the WordPress Enterprise Architecture. | [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#architecture-decision-register) | Pending; no implementation authorized |
| FD-ARC-002 | Resolve or delegate the product, taxonomy, role, inquiry, SEO, media, version, plugin, integration, security, and performance decisions required before configuration. | [Open Architecture Decisions](06_WORDPRESS_ARCHITECTURE.md#open-architecture-decisions) | Pending; domain review required |

## DS Program Charter and Strategic Directive Decision

| ID | Decision | Decision owner / effective date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-DS-PROGRAM-001` | Accept [DS-PC-001 Program Charter](DS_PC_001_PROGRAM_CHARTER.md) as the program execution method (`HOW`) and [DS-SPD-001 Strategic Program Directive](DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md) as the Version 1.0 strategic outcome (`WHAT`). The Founder remains final authority. ChatGPT serves as Project Commander, Chief Architect, Product Owner, and Repository Governor. Codex serves as operational Program Commander and Build Engine only inside exact task gates and cannot self-approve or bypass repository, Git, runtime, production, human-review, Founder-review, or branch-deletion gates. | Founder / effective 2026-08-02 | Canonicalize the two complete source texts using only UTF-8 decoding, CRLF/CR and U+2028/U+2029 to LF, and NFC normalization; update only `AGENTS.md`, the two canonical documents, Source of Truth Priority, Decision Log, Founder Decision Log, Repository Relationship Map, Reading Order, Documentation Index, Traceability Matrix, and Changelog. | DS-PC raw SHA-256 `ee750ca9a3ba47f4f48fd906675714922fc7cbe88904d3f580aee734237a0e0c`; normalized SHA-256 `3e6e9c7a827fc4998bb96b343842b84efe80573febf2c688247a98b9f01e44d4`; canonical path `docs/DS_PC_001_PROGRAM_CHARTER.md`. DS-SPD raw SHA-256 `aa10c18ff06b38d0054908e4267848c8f7432e649b32d2de7b4bf0c55015d40c`; normalized SHA-256 `929b96e17207e93c8b3543241c5db361093f1030f31431d3c5960bf4ea010bf6`; canonical path `docs/DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md`. | `APPROVED` within this exact governance-integration scope. DS-PC and DS-SPD are companions and successor program context; neither silently approves the full Draft Project Bible/Constitution, rewrites `GOV-XD-00` history, auto-supersedes domain roadmaps, or overrides CP-001–CP-010, accepted Founder decisions/ADRs, accepted architecture, source priority, or production controls. PD-04, Campaign 002, Product/SKU, Golden/Master Data, Runtime, Import, Deployment, Production, Git publication, merge, and branch deletion require separate authority. Any supersession must be explicit, scoped, and recorded by a later Founder decision. |

## C000 / Project OS 2.0 Strategic Reconciliation Decision

| ID | Decision | Decision owner / effective date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-C000-OS2-001` | Accept Project OS 2.0 using `PRESERVE → RECONCILE → SIMPLIFY → EXTEND`; preserve Repository/Product Data/Taxonomy/Knowledge authority; freeze C1-T03 at its protected architecture boundary with all 11 findings retained; adopt Tracks A–D with WIP focus `1 Commercial + 1 Core + 1 Enabler`; approve `Inquiry First by default + future SKU-level purchase eligibility` as target architecture only; and classify the three PD-03B records as seed/reference evidence, not Product/SKU/Availability or a ceiling on future bounded scope. | Founder + Project Commander / effective 2026-08-16 | Strategic reconciliation and documentation canonicalization only. Future Product Builder, controlled values, weight provenance, electrostatic appearance, Commerce Eligibility, Inventory Harmony, Damavand/Central BOM, Commercial Pilot, Growth/CRM, Runtime, and Automation require separate Missions and gates. | C000 Slack Mission Packet (parent + 3 replies); C001 Slack Mission Packet (parent + 4 replies); [C000 Decision Package](C000_OS2_STRATEGIC_RECONCILIATION_DECISION_PACKAGE.md); reviewed live-main anchor `dfb5f4f632b0e913c33d303292c320a889a6f63a` | `APPROVED` within exact strategic scope. It grants no Product/SKU/Availability, public pricing/purchase/cart/checkout/payment, Runtime, Staging, Production, C1-T03 repair, Central Steel, n8n/OpenAI, or successor execution authority. |
| `C001-OS2-RECON` | Execute one bounded docs-only Repository reconciliation branch, commit, push, and pull request; run local validation, independent review, and CI; correct only attributable in-scope findings; stop before merge. | Founder + Project Commander / 2026-08-16 | The two required new documents and named state/baseline/roadmap/decision/navigation/traceability files, plus minimal direct-contradiction corrections in `AGENTS.md` and ADR-0001. | C001 Slack Mission Packet; starting `main` SHA `dfb5f4f632b0e913c33d303292c320a889a6f63a`; branch `codex/c001-os2-repository-reconciliation` | `APPROVED` for branch/commit/push/one PR and attributable CI fixes only. Merge, C002, Product/Runtime/Production, and every explicit C001 NO-GO remain unauthorized. |

## C002 Commercial Pilot Truth and Product Administration Contracts

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `C002-CONTRACTS-001` | Execute a bounded repository contract mission for Commercial Pilot candidate intake/readiness, the minimum Founder Evidence/Data Packet, Product Builder and controlled Add Value policy, Brand/Mass/Electrostatic provenance, inactive per-SKU Commerce Eligibility, Inventory Harmony, and the Damavand/Central interface boundary. | Founder + Project Commander / 2026-08-16 | Contracts, closed schemas, empty canonical C002 extension registries, deterministic offline validators, synthetic tests, bounded documentation, one branch/commit/push/PR, attributable CI fixes, and independent review. | C002 Slack Mission Packet (parent + 4 replies); starting `main` SHA `d603322e238d4cf06070da8fb8096cf7050527c2`; [C002 Contract Scope](C002_COMMERCIAL_PILOT_PRODUCT_ADMINISTRATION_CONTRACTS_SCOPE_V1.0.md) | `APPROVED` for the exact C002 mission. No first Pilot selection, Product/SKU/Availability/stock claim, commercial fact or pricing, 879-row population, WordPress/WooCommerce, Runtime/Staging/Production, Central implementation, merge, or successor Mission is authorized. |

## C003 Founder Discovery Reconciliation

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-C003-DISCOVERY-001` | Read the complete C003 Mission and Founder Product & Commerce Discovery Session 01 threads, then integrate the discovery as durable classified evidence, owner mappings, inactive backlog/defer dispositions, and deterministic validation. Preserve exactly `FOUNDER_CONFIRMED`, `FOUNDER_ACCEPTED_CANDIDATE`, and `ARCHITECTURE_PROPOSAL` evidence classes plus independent current/historical/future temporal roles without Product or runtime promotion. | Founder + Project Commander / 2026-08-17 | One bounded branch, documentation, evidence contract/schema/registry/validator/tests, necessary navigation/traceability reconciliation, independent review, local validation, commit/push/one non-draft PR, and attributable CI repair. | C003 Slack Mission parent `1786969720.051019` plus two replies; Founder Discovery parent `1786929259.157699` plus all eight replies (`PART 1`–`PART 7` and `CHECKPOINT 02`); starting `main` `b45e1b592213f8d3d98805cef2681be781d8cff8`; branch `codex/c003-founder-discovery-reconciliation`; [C003 Scope](C003_FOUNDER_DISCOVERY_RECONCILIATION_SCOPE_V1.0.md) | `APPROVED` as Mission and evidence-integration authority only. It is not canonical Product/value/tuple/SKU/Availability/price/stock/customer/order approval; C002 remains zero candidates/eight policies/zero instances; Inquiry First remains effective; no WordPress/WooCommerce, Runtime/Staging/Production, FX automation, marketplace, C1-T03 repair, merge, C003-A, C003-B, or successor Mission is authorized. |
| `FD-C003-R1-CP03-001` | Reconcile the complete Checkpoint 03 source into a deterministic versioned C003 extension, classify relevant Idea Vault concepts without granting implementation authority, and prepare a Founder-ready but fail-closed 201/51 Commercial Pilot evidence packet. | Founder + Project Commander / 2026-08-17 execution completed 2026-08-18 | Documentation, evidence contract/schema/registry/validator/tests, bounded branch/commit/push/one non-draft PR, attributable CI fixes and independent review. | C003-R1 Mission parent `1786996740.153019` plus two replies; Checkpoint 03 parent `1786996639.277979` plus three replies; complete original Discovery and Idea Vault threads; starting `main` `f64b5b481ef66e000c8c87a26794c74f5622418c`; [C003-R1 Scope](C003_R1_CHECKPOINT03_201_51_PILOT_READINESS_SCOPE_V1.0.md) | `APPROVED` for evidence/planning and Git publication only. The prior 115 records remain unchanged; no C002 candidate is populated; Product/SKU/Availability/price/customer/order/payment/Runtime/Production, merge, C003-A/C003-B and successor work remain unauthorized. |

## BP2 Data Administration Lifecycle Decision

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-BP2-ADM-001` | Execute the BP2 Data Administration lifecycle in the ordered sequence `DRAFT → REVIEW → APPROVED`; perform governance-only review and corrections; preserve `implementation_authority: false`; and reject any direct `DRAFT → APPROVED` transition. | Founder / 2026-07-28 | BP2 scope, Contract, Schema, Validator, tests, direct governance reconciliation, scoped Branch/Commit/Push/PR, conditional Merge Commit, and post-merge CI only | Founder authorization recorded in the active Codex task; [BP2 Data Administration Scope](BP2_DATA_ADMINISTRATION_SCOPE_V1.0.md); `BP2-ADM-REVIEW-001`; merged PR #18; successful local, Review-stage, final-PR, and post-merge `main` validation | `APPROVED` on 2026-07-28 after recorded `DRAFT → REVIEW → APPROVED`, completed review, resolved blockers, successful CI, and Merge Commit `180bea23a3f13e3c957f3a323bc215b9d2e4b972`. No Admin UI, Product/SKU, WordPress/WooCommerce, import, publication, deployment, runtime, production, or branch deletion is authorized. |

## Cross-Domain Execution Charter Decision

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-GOV-XD-00` | Execute the documentation-only Cross-Domain Execution Charter; separate semantic operational state from the dynamic Git tip; require per-Sprint starting-SHA resolution, exact Scope/Approval and Test Contracts, executor/reviewer/Founder separation, and ordered dependency gates; select `PD-01` only as the next decision-package target. | Founder / 2026-07-28 | Exactly `AGENTS.md`, `docs/CURRENT_PROJECT_STATE.md`, `docs/PROJECT_BASELINE.md`, `docs/IMPLEMENTATION_READINESS.md`, `docs/PROJECT_EXECUTION_ROADMAP.md`, `docs/CODEX_SPRINT_PROTOCOL.md`, `docs/REPOSITORY_HEALTH.md`, `docs/17_FOUNDER_DECISION_LOG.md`, `docs/18_OPEN_QUESTIONS.md`, `docs/TRACEABILITY_MATRIX.md`, and `docs/14_CHANGELOG.md`; Branch `codex/gov-xd-00-execution-charter`; scoped Commit/Push/Draft PR; independent review; conditional Merge Commit and post-merge `main` CI | Reviewed input anchor `b391ca1632d4a7d266e33aa5e279e214941901ae`; PR #19; CI run `30372385447`; five domain plans; independent QA and self-reference review; Founder authorization recorded in the active Codex task | `APPROVED` and integrated by PR #20. This decision itself granted no Contract, Schema, Validator, Test, Product/Knowledge data, BP2 implementation, Admin UI, WordPress/WooCommerce, import, credential, backup, staging, runtime, deployment, production, branch deletion, or `PD-01` execution; later `FD-PD01-001` is separate. |

## PD-01 Product Data Contract Enablement Decision

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-PD01-001` | Execute PD-01 through the legal sequence `DRAFT → REVIEW → APPROVED` with synthetic fixtures only; require the exact 30-path allowlist, independent `PASS`, successful tests/CI, no conflict or scope drift, and Merge Commit only after every condition passes. | Founder / 2026-07-28; lifecycle approval recorded 2026-07-29 | [PD-01 Scope v1.0](PD01_PRODUCT_DATA_CONTRACT_SCOPE_V1.0.md); Branch `codex/pd-01-product-data-contract-enablement`; scoped Commit/Push/Draft PR; limited in-scope corrections; lifecycle evidence; conditional ready-for-review/Merge Commit; post-merge `main` CI | Founder authorization in the active Codex task; starting `main` SHA `6577cd461e88463903b18c11b0e5bdbfa88375e2`; merged PR #20 and successful required-check run `30376465378`; Draft Commit `4cc1805`; Draft PR #21; DRAFT CI `30390311445`; independent `PD01-REVIEW-001` PASS with zero findings; REVIEW Commit `a3c547a`; REVIEW CI `30466264564` | `APPROVED` on 2026-07-29 after legal `DRAFT → REVIEW → APPROVED`. Approval covers only the synthetic Contract/Schema/Validator/Test boundary. Canonical Product Attribute registry must remain empty. No Product, real Pilot, 879-row data, Master Data, Golden package, SKU, slug, availability, WordPress/WooCommerce, import, runtime, deploy, production, or branch deletion is authorized. |

## PD-02A Controlled Values and Attribute Profiles Foundation Decision

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-PD02A-001` | Execute PD-02A through `DRAFT → REVIEW → APPROVED` for synthetic-only Controlled Value Registry and standalone Attribute Profile Contract/Schema/Validator/Test infrastructure; require all three canonical Product Attribute/value/Profile collections to remain empty; require exact 38-path scope, independent `PASS`, successful local/CI evidence, no conflict or scope drift, and Merge Commit only after all conditions pass. | Founder / 2026-07-29 | [PD-02A Scope v1.0](PD02A_CONTROLLED_VALUES_ATTRIBUTE_PROFILES_SCOPE_V1.0.md); Branch `codex/pd-02a-controlled-values-profile-foundation`; scoped Commit/Push/Draft PR; limited in-scope corrections; conditional ready-for-review/Merge Commit; post-merge `main` CI | Founder authorization in the active Codex task; starting `main` SHA `d8ae556d17ab518970149533d975b7924f3af3e1`; PR #21 integration baseline; DRAFT Commits `a6f7e09` and `23e8ac2`; Draft PR #22; CI runs `30469027782`, `30469883442`, and REVIEW-stage `30470305597`; `PD02A-REVIEW-001` attempt 1 = `REWORK`, attempt 2 = `PASS` with zero findings; later merged PR #22 and main CI `30471480775` | `APPROVED` after legal `DRAFT → REVIEW → APPROVED`; later Git integration completed through PR #22. No canonical Family, Attribute, controlled term, Profile, Product, Pilot, Master Data, Golden package, SKU, slug, availability, WordPress/WooCommerce, import, runtime, deployment, production, or branch deletion is authorized. PD-02B required separate approval. |

## PD-02B Minimum Canonical Slice Decision

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-PD02B-001` | Execute the exact minimum canonical slice through `DRAFT → REVIEW → APPROVED`: 3 Product Entities, 2 Attributes, 2 Value Registries, 4 Terms, 1 INTERNAL Profile, 18 localized labels, and 1 Approval Evidence; require independent technical PASS, successful tests/CI, no conflict or scope drift, and Merge Commit only after every condition passes. | Founder / 2026-07-29; lifecycle approval recorded 2026-07-29 | [PD-02B Scope v1.0](PD02B_MINIMUM_CANONICAL_SLICE_SCOPE_V1.0.md); exact 57 paths after separately approved successor-compatibility corrections to the PD-02A and Product Master Data regression tests; Branch `codex/pd-02b-minimum-canonical-slice`; scoped Commit/Push/Draft PR; allowlisted corrections; conditional ready/Merge Commit/post-merge CI | Founder task `019faec6-5d14-7da2-909a-450fe030b551`; Material PASS `SS-MATERIAL-REVIEWER-02`; Grade PASS `SS-INDEPENDENT-REVIEWER-20Y-01`; starting `main` SHA `6ed6fc89e555b1be3a97d7f9c64c9e2b989af1df`; `PD02B-TECH-REVIEW-001` attempt 2 = `PASS` on `f38eb44721b90f2cf6b451c280e2d8a91c789f55`; CI `30479723615` and REVIEW-stage CI `30480571732` = `PASS`; final approval timestamp `2026-07-29T18:41:26Z`; later merged PR #23 and main CI `30482348480` | `APPROVED` after legal `DRAFT → REVIEW → APPROVED`; all 31 bounded records are approved and later Git integration completed through PR #23. No 430, Finish/Color/PVD, dimensions/Units, Product/Pilot/879-row/Master/Golden/SKU/slug/availability, SEO/filter/variation/inquiry/commerce, WordPress/WooCommerce/import/runtime/deploy/production, or branch deletion is authorized. |

## PD-03A Pilot Prerequisite Foundation Decision

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-PD03A-001` | Build a successor-safe immutable extension for the decorative Pipe Series prerequisite through `DRAFT → REVIEW → APPROVED`; preserve all PD-02B files and hashes; add exactly 2 entities, 4 Attributes, one Silver appearance term, one six-rule INTERNAL Series Profile, 11 labels, controlled Length/Metre/Millimetre promotion, one Approval Evidence, and synthetic-only pilot-combination validation. | Founder / 2026-08-01; lifecycle approval recorded 2026-08-01 | [PD-03A Scope v1.0](PD03A_PILOT_PREREQUISITE_FOUNDATION_SCOPE_V1.0.md); maximum 49 paths; Branch `codex/pd-03a-pilot-prerequisite-foundation`; scoped Commit/Push/Draft PR; independent technical review; legal lifecycle; conditional Merge Commit and post-merge CI | Founder authorization in active task `019fa05e-1889-79b3-8e83-9477cd1648c6`; starting `main` SHA `dd4d4e9dde59ce652edb5b99d2df3e84b56b8031`; two failed human-review attempts preserved as Blocked evidence; no human PASS claimed; `PD03A-TECH-REVIEW-001` attempt 3 zero-finding PASS on `cb6c817…`; CI `30696083295`; REVIEW CI `30696444576`; final approval `2026-08-01T10:50:12Z`; 50-case mutation contract; later merged PR #24 and main CI `30696801759` | `APPROVED` after legal `DRAFT → REVIEW → APPROVED`; exact bounded records and Length/Metre/Millimetre are approved, and later Git integration completed through PR #24. No technical, standard, tolerance, quality, application, commercial, availability, supply, Product/Pilot/SKU/Slug, Master/Golden, WordPress/WooCommerce, import, runtime, deployment, production, or branch-deletion authority. PD-03B required separate approval. |

## PD-03B Canonical Pilot Records Decision

| Decision ID | Decision | Authority / Date | Scope | Evidence | Status / Boundary |
| --- | --- | --- | --- | --- | --- |
| `FD-PD03B-001` | Execute exactly three canonical Pilot records through `DRAFT → REVIEW → APPROVED`, using new stable identities while keeping every `GOLD-PIPE-*` and `PIPE-COMB-*` value as a non-identity historical reference. | Founder / 2026-08-01; lifecycle approval recorded 2026-08-01 | [PD-03B Scope v1.0](PD03B_CANONICAL_PILOT_SCOPE_V1.0.md); exact 33-path Allowlist; Branch `codex/pd-03b-canonical-pilot-records`; dedicated Contract/Schema/Validator/Test and one Approval Evidence; conditional Merge Commit and main CI | Founder authorization in active task `019fa05e-1889-79b3-8e83-9477cd1648c6`; starting `main` SHA `e72c32bdb041448d34c925c969fe01a2156f9e1d`; `FD-PILOT-001`; `FD-PD03A-001`; `PD03B-TECH-REVIEW-001` attempt 1 REWORK and attempt 2 zero-finding PASS on `41849b3…`; DRAFT CI `30698352338`; REVIEW CI `30698582671`; final approval `2026-08-01T11:54:38Z`; merged PR #25; Merge Commit `64511d7caf95d88122847abfef9914e9d0605954`; main CI `30698838847` | `APPROVED` after legal lifecycle and integrated through PR #25; exactly three Pilot records are approved, nonce consumed once, availability remains `MISSING_DATA_VALUE`, and every readiness flag remains false. No Product/SKU, 879 rows, Master/Golden, WordPress/WooCommerce, import, runtime, deployment, production, or branch deletion. |

## Settled Golden Pipe Pilot Decision

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| FD-PILOT-001 | Approve Golden Parent `لوله استیل دکوراتیو` and exactly three limited-pilot Pipe combinations: 201 / Silver / 51 mm / 0.50 mm / 6 m (`GOLD-PIPE-201-51-050-6M`, `PIPE-COMB-0023`); 201 / Silver / 38 mm / 0.50 mm / 6 m (`GOLD-PIPE-201-38-050-6M`, `PIPE-COMB-0016`); and 201 / Silver / 16 mm / 0.35 mm / 6 m (`GOLD-PIPE-201-16-035-6M`, `PIPE-COMB-0001`). The `GOLD-PIPE-*` values are pilot references only, not final commercial SKUs. The remaining 879 combinations remain `CANDIDATE_UNVERIFIED`; market availability is `MISSING_DATA_VALUE` for all 882 rows. Import, runtime, publishing, deployment, product creation, and bulk SKU generation remain `NO-GO`. | Founder / 2026-07-14 | Repository-only Golden Product pilot decision and decision registration; no availability, SKU, import, runtime, or publication approval | [Current Project State](CURRENT_PROJECT_STATE.md), Future Reference: Sprint 11 Audit — `docs/AUDIT_REPORT_SPRINT11.md` (Not yet approved), Future Reference: Golden Variations — `repository/golden-reference/pipe/02_GOLDEN_VARIATIONS.yaml` (Not yet approved), Future Reference: Golden Founder Review — `repository/golden-reference/pipe/15_GOLDEN_FOUNDER_REVIEW.md` (Not yet approved), and Future Reference: Pipe Combination Register — `repository/master-data/pipes/03_PIPE_VALID_COMBINATIONS.csv` (Not yet approved) | `APPROVED` within exact scope; only a later explicit Founder decision with affected scope, evidence, and traceability may amend or supersede it |

## Settled Golden Product Completion Decisions

| ID | Decision | Decision owner / date | Approval scope | Evidence | Status / supersession |
| --- | --- | --- | --- | --- | --- |
| `FD-SPR13-BUS-01` | The Golden Product pilot is Persian-only. No official English product name is required at this stage. English naming is deferred until multilingual or international requirements are formally approved. | Founder / 2026-07-14 | Current Golden Product pilot identity and content scope only | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), Future Reference: Implementation Package — `repository/golden-reference/pipe/GOLDEN_PRODUCT_IMPLEMENTATION_PACKAGE.md` (Not yet approved) | `APPROVED`; English naming remains `DEFERRED` for future scope |
| `FD-SPR13-COM-01` | The Parent remains brand-neutral. Brand is not part of product identity and remains absent/hidden. Brand may be introduced later only as an optional descriptive commercial attribute after evidence and separate Founder approval. | Founder / 2026-07-14 | Current Golden Product pilot public identity and configurator behavior only | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), Future Reference: Completion Matrix — `repository/golden-reference/pipe/GOLDEN_PRODUCT_COMPLETION_MATRIX.md` (Not yet approved) | `APPROVED`; no brand value, availability, or future use is inferred |
| `FD-SPR13-COM-03` | Weight is intentionally deferred. No estimated or inferred value is permitted. Weight may be introduced later only when a validated shipping, warehouse, calculation, or internal-logistics requirement exists and an authoritative source supplies the value. | Founder / 2026-07-14 | Current Golden Product pilot data/content/import-preparation scope only | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), Future Reference: Master Data Governance — `repository/master-data/MASTER_DATA_GOVERNANCE.md` (Not yet approved) | `APPROVED`; weight remains `DEFERRED` and no value is approved |
| `FD-SPR13-BUS-03` | The pilot uses one controlled inquiry path. Each inquiry retains the selected Parent and Variation context. Initial follow-up is by telephone. The accountable role is `Sales Owner`, not a named individual. WhatsApp, email, and other channels are deferred until ownership, security, privacy, traceability, and governance are approved. | Founder / 2026-07-14 | Golden Product pilot inquiry business flow only; no live form, provider, personal-data processing, or runtime authorization | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), Future Reference: Inquiry Payload — `repository/golden-reference/pipe/11_GOLDEN_INQUIRY_PAYLOAD.yaml` (Not yet approved), and [Execution Gate G13](EXECUTION_GATES.md#g13--inquiry-crm-email-and-privacy) | `APPROVED` for business flow; runtime implementation remains blocked by G13 |
| `FD-SPR13-BUS-02` | Target-customer segmentation is intentionally deferred. The Golden Product pilot remains customer-neutral until evidence-based market segmentation is available. | Founder / 2026-07-14 | Current Golden Product pilot content and targeting scope only | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), Future Reference: Implementation Package — `repository/golden-reference/pipe/GOLDEN_PRODUCT_IMPLEMENTATION_PACKAGE.md` (Not yet approved) | `APPROVED`; segmentation and targeted claims remain `DEFERRED` |
| `FD-SPR13-COM-02` | Commercial SKU policy is deferred. The `GOLD-PIPE-*` identifiers remain internal pilot references only. No commercial SKU generation, import, or runtime use is authorized until a separate SKU Architecture is approved. | Founder / 2026-07-14 | Current Golden Product pilot identity and implementation-preparation scope only; no SKU, import, or runtime approval | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), [Project Baseline](PROJECT_BASELINE.md) | `APPROVED` as deferral; Import and Runtime remain `NO-GO` |
| `FD-SPR13-SEO-02` | OpenGraph and Twitter metadata are deferred until the final Hero image, approved media assets, and final SEO content are available. No speculative social metadata may be generated. | Founder / 2026-07-14 | Current Golden Product pilot social metadata scope only | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), Future Reference: Implementation Package — `repository/golden-reference/pipe/GOLDEN_PRODUCT_IMPLEMENTATION_PACKAGE.md` (Not yet approved) | `APPROVED` as deferral; Social Preview and Publishing readiness remain `NO-GO` |
| `FD-SPR13-CNT-01` | No authoritative application evidence is currently available. No product application claim may be published. | Founder / 2026-07-14 | Current Golden Product pilot evidence-handling and content-omission scope only | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), Future Reference: Content Package — `repository/golden-reference/pipe/07_GOLDEN_CONTENT_PACKAGE.yaml` (Not yet approved) | Evidence Option 2 `APPROVED`; no application fact or content is approved |
| `FD-SPR13-CNT-02` | Alloy 201 guidance may be created only after `Qualified Domain Reviewer` reviews authoritative technical sources. Until then, only the approved identifier `201` may appear without technical interpretation. | Founder / 2026-07-14 | Current Golden Product pilot evidence assignment and output restriction only | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), Future Reference: Knowledge Bindings — `repository/golden-reference/pipe/05_GOLDEN_KNOWLEDGE_BINDINGS.yaml` (Not yet approved) | Evidence Option 3 `APPROVED`; guidance remains `MISSING_CONTENT` and unapproved |
| `FD-SPR13-CNT-03` | No authoritative maintenance instructions are currently available. No maintenance recommendation may be published. | Founder / 2026-07-14 | Current Golden Product pilot evidence-handling and content-omission scope only | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), Future Reference: Content Package — `repository/golden-reference/pipe/07_GOLDEN_CONTENT_PACKAGE.yaml` (Not yet approved) | Evidence Option 2 `APPROVED`; no maintenance fact or content is approved |
| `FD-SPR13-RUN-01` | An isolated staging environment has not been proven. Evidence collection is delegated to `Operations Owner`. | Founder / 2026-07-14 | Runtime evidence-status and owner assignment only; no target, staging, access, or runtime approval | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), [Execution Gate G04](EXECUTION_GATES.md#g04--staging-isolation) | Evidence Option 3 `APPROVED`; staging and Runtime remain `NO-GO` |
| `FD-SPR13-RUN-03` | Backup capability exists, but an independent successful restore has not been demonstrated. Runtime changes remain prohibited until restore evidence is verified. | Founder / 2026-07-14 | Backup/restore evidence-status only; no mutation or residual-risk acceptance | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), [Execution Gate G03](EXECUTION_GATES.md#g03--backup-and-restore) | Evidence Option 2 `APPROVED`; G03 remains failed and Runtime remains `NO-GO` |
| `FD-SPR13-RUN-04` | Blocksy Pro and Elementor Pro remain architectural targets, but ownership, licensing, version, and compatibility evidence has not been verified. | Founder / 2026-07-14 | Presentation package evidence-status only; no installation, activation, compatibility, or runtime approval | Future Reference: Founder Checklist — `repository/golden-reference/pipe/FOUNDER_DECISION_CHECKLIST.md` (Not yet approved), [Execution Gate G10](EXECUTION_GATES.md#g10--approved-component-and-license) | Evidence Option 3 `APPROVED`; Presentation Runtime remains `NO-GO` |

## Settled Class B Wave 1 Repository-Control Decision

| ID | Settled decision | Decision source | Exact scope | Resulting status |
| --- | --- | --- | --- | --- |
| `FD-GIT-W1-001` | Execute Class B Wave 1 only through branch `codex/class-b-wave-01-governance`. Reconcile and integrate exactly `.gitattributes`, `README.md`, `docs/08_DOCUMENTATION_INDEX.md`, `docs/09_NAVIGATION_MAP.md`, `docs/10_DECISION_LOG.md`, `docs/17_FOUNDER_DECISION_LOG.md`, `docs/18_OPEN_QUESTIONS.md`, `docs/CODEX_SPRINT_PROTOCOL.md`, `docs/CURRENT_PROJECT_STATE.md`, `docs/GIT_BASELINE_APPROVAL_CHECKLIST.md`, `docs/GIT_FILE_CLASSIFICATION.csv`, `docs/KNOWLEDGE_GRAPH.md`, `docs/PROJECT_BASELINE.md`, `docs/PROJECT_EXECUTION_ROADMAP.md`, `docs/READING_ORDER.md`, `docs/REPOSITORY_HEALTH.md`, `docs/REPOSITORY_RELATIONSHIP_MAP.md`, `docs/SOURCE_OF_TRUTH_PRIORITY.md`, and `docs/TRACEABILITY_MATRIX.md`; create one commit, push only that branch, and open one Draft PR. | Founder / 2026-07-19 | Git and documentation integration for the named 19 paths only. PR #1 must remain unchanged; Waves 2–10 and the six Sprint 1 reports remain excluded. | `APPROVED` within exact scope. Merge, runtime, workflow activation/execution, WordPress, product, content, publication, deployment, production, repository-setting, and default-branch changes remain `NO-GO`. |

## Settled Wave 2 Pre-Implementation Governance Decisions

| ID | Settled decision | Decision source | Exact scope | Resulting status |
| --- | --- | --- | --- | --- |
| `FD-W2G-001` | The canonical Product Repository hierarchy is exactly `Catalog → Platform → Family → Series → Variant Rules → SKU`. Catalog through Variant Rules are canonical repository concepts; SKU is derived only after governed modeling. Product Family, Product Group, Product Type, Parent Product, Variable Parent Product, and Variation may be retained only as legacy, presentation, or commerce-adapter mappings. Labels, slugs, WooCommerce IDs, Parent IDs, Variation IDs, and SKUs are not canonical entity identities. | Founder / 2026-07-20 Wave 2 pre-implementation governance reconciliation approval | Documentation authority for Product hierarchy and identity boundaries only | `APPROVED`; no schema, registry, Product record, SKU, mapping, or implementation is created or authorized |
| `FD-W2G-002` | Canonical path ownership is `repository/data/contracts/`, `repository/data/schemas/`, `repository/data/registries/`, `repository/data/validation/`, `repository/data/master-data/`, `repository/data/golden-reference/`, `repository/knowledge/`, `repository/content/`, `repository/implementation-assets/`, and adapter-only `repository/wordpress/`. WordPress, WooCommerce, imports, page builders, adapters, and runtime consumers never own canonical Product or Knowledge truth. | Founder / 2026-07-20 Wave 2 pre-implementation governance reconciliation approval | Directory ownership and non-duplication rule only | `APPROVED`; path creation and implementation remain separately gated. Older Future Reference paths in historical rows preserve their original chronology and do not designate current ownership |
| `FD-W2G-003` | Record PR #1–#3 merged; Wave 1 and post-merge reconciliation complete; canonical/default `main` at `d702c5217f7caa2f23e56f965f3f993967e3c17d`; `origin/HEAD` at `origin/main`; main protection, administrator enforcement, strict required `repository-validation`, force-push prohibition, and deletion prohibition active; Wave 2 discovery complete; Wave 2 implementation not started; Wave 2A proposed but not authorized. | Founder / 2026-07-20 plus verified GitHub and Git evidence | Current repository-governance documentation only | `APPROVED` for reconciliation; Runtime, Import, Publishing, Deployment, and implementation remain `NO-GO` |
| `FD-W2G-004` | Product and Knowledge architecture proposals exist, but their machine-readable core contracts/instances and Product-domain tests do not. No canonical machine-readable Master Data or Golden package exists on `main`. The approved Golden Parent and exactly three combinations remain decision/prose authority only; 879 remain `CANDIDATE_UNVERIFIED`, availability is `MISSING_DATA_VALUE` across all 882, brand is absent/hidden, and weight is `DEFERRED`. `PIPE_VARIATION_MATRIX.md` is a legacy theoretical scaffold and has no Golden, availability, Master Data, import, SKU, or runtime authority. | Founder / 2026-07-20 Wave 2 pre-implementation governance reconciliation approval | Readiness and evidence classification only | `APPROVED`; Product Repository and Knowledge Repository are `NOT_IMPLEMENTATION_READY`, and no Product/Golden data or implementation is authorized |

## Settled K-01 Governance and Knowledge Reconciliation Decision

| ID | Settled decision | Decision source | Exact scope | Resulting status |
| --- | --- | --- | --- | --- |
| `FD-K01-001` | Execute K-01 through an independent branch with repository edits and one Draft PR. Reconcile current-state and decision records after Wave 2A–2C, define one knowledge-archive ownership model, disposition the 173 current Atlas rows, classify legacy Library Atlas material as noncanonical archive reference, and make `make test` run the repository validators. | Founder / 2026-07-23 selection: “Branch + edits + Draft PR” | `codex/k-01-governance-knowledge-reconciliation`; governance/docs, Atlas classification, tests, one commit, branch push, and one Draft PR only | `APPROVED` within exact scope. Merge, WordPress/WooCommerce/runtime mutation, import, publishing, deployment, production, Product/Knowledge population, Wave 2D, and repository-settings changes remain `NO-GO` |

## Wave 2A–2C Evidence Reconciliation

PR #5, PR #6, and PR #7 verify that Product core, Product Attribute, and measurement structural foundations are present. These are implementation outcomes, not new Founder decisions created by this log. The Wave 2C registries explicitly cite `founder-authorization:wave-2c:2026-07-23`; equivalent originating authorization references for Wave 2A and Wave 2B are not explicit in this log and must not be inferred from merge history. See `EV-W2A-001` through `EV-W2C-001` in the [Decision Log](10_DECISION_LOG.md#wave-2-foundation-implementation-evidence).

## Product Data Decisions Required

| ID | Decision required | Source | Status |
| --- | --- | --- | --- |
| FD-DATA-001 | Approve, revise, or reject PDM-001 through PDM-008. | [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md#data-model-decisions) | Partially resolved: PDM-001 and PDM-002's exclusion of downstream identifiers from canonical identity are settled by `FD-W2G-001`; stable-ID contract/registry design and remaining proposal scope are pending; no product creation authorized |
| FD-DATA-002 | Approve, revise, or reject WCM-001 through WCM-008. | [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md#woocommerce-model-decisions) | Pending; no WooCommerce configuration authorized |
| FD-DATA-003 | Approve, revise, or reject TAX-001 through TAX-008. | [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md#taxonomy-decisions) | Pending; no taxonomy or term creation authorized |
| FD-DATA-004 | Approve, revise, or reject ATT-001 through ATT-007, including proposed Persian labels, English keys, hierarchy boundary, and Size classification. | [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md#attribute-decisions) | Pending; qualified domain review required |
| FD-DATA-005 | Approve, revise, or reject INQ-001 through INQ-008. | [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md#inquiry-decisions) | Pending; Sales, security, and privacy review required |
| FD-DATA-006 | Assign owners and approve lifecycle, exact Family/Series values, Variant Rules, taxonomy/Collections/Tags, Application/Use-Case terminology, attributes/Size, local exceptions, Customer identity/lifecycle, values, units, SKU, slug, stock, inquiry, SEO, CRM, ERP, and CentralSteel policies before implementation. | [Batch 05 Open Questions](18_OPEN_QUESTIONS.md#product-data-questions) | Canonical hierarchy resolved by `FD-W2G-001`; remaining decisions pending; no implementation authorized |

## Information Architecture Decisions Required

| ID | Decision required | Source | Status |
| --- | --- | --- | --- |
| FD-IA-001 | Approve, revise, or reject IA-001 through IA-007. | [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md#information-architecture-decisions) | Pending; no implementation authorized |
| FD-IA-002 | Approve, revise, or reject SITE-001 through SITE-007. | [Enterprise Site Structure](25_SITE_STRUCTURE.md#site-structure-decisions) | Pending; no page/menu creation authorized |
| FD-IA-003 | Approve, revise, or reject URL-001 through URL-008. | [Enterprise URL Architecture](26_URL_ARCHITECTURE.md#url-architecture-decisions) | Pending; no URL/redirect configuration authorized |
| FD-IA-004 | Approve, revise, or reject SRCH-001 through SRCH-008. | [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md#search-decisions) | Pending; no search/filter/AI implementation authorized |
| FD-IA-005 | Approve, revise, or reject LINK-001 through LINK-007. | [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md#internal-linking-decisions) | Pending; no public link/template automation authorized |
| FD-IA-006 | Assign IA, navigation, URL, SEO, search, content, representative, support, and internal-link owners and approve exact public labels, representative scope, landing types, path policy, and discovery rules. | [Information Architecture Open Questions](18_OPEN_QUESTIONS.md#information-architecture-questions) | Pending; no implementation authorized |

## Content and Entity Architecture Decisions Required

| ID | Decision required | Source | Status |
| --- | --- | --- | --- |
| FD-CEA-001 | Approve, revise, or reject CONTENT-001 through CONTENT-008. | [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md#content-architecture-decisions) | Pending; no content/platform implementation authorized |
| FD-CEA-002 | Approve, revise, or reject ERM-001 through ERM-008. | [Enterprise Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md#entity-model-decisions) | Pending; no entity/storage implementation authorized |
| FD-CEA-003 | Approve, revise, or reject SCHEMA-001 through SCHEMA-009. | [Schema.org Semantic Strategy](31_SCHEMA_ORG_STRATEGY.md#schema-strategy-decisions) | Pending; no structured-data implementation authorized |
| FD-CEA-004 | Approve, revise, or reject CTYPE-001 through CTYPE-007. | [Enterprise Content Types](32_CONTENT_TYPES.md#content-type-decisions) | Pending; no platform content type authorized |
| FD-CEA-005 | Approve, revise, or reject MEDIA-001 through MEDIA-009. | [Enterprise Media Strategy](33_MEDIA_STRATEGY.md#media-decisions) | Pending; no media/CDN/DAM implementation authorized |
| FD-CEA-006 | Approve, revise, or reject SEOENT-001 through SEOENT-009. | [Enterprise SEO Entity Model](34_SEO_ENTITY_MODEL.md#seo-entity-decisions) | Pending; no SEO/AI/LLM/search implementation authorized |
| FD-CEA-007 | Assign content/entity/media/semantic/SEO owners and approve conditional public entities, lifecycles, fields, relationships, content types, media policies, semantic eligibility, and search-intent ownership. | [Content and Entity Open Questions](18_OPEN_QUESTIONS.md#content-and-entity-architecture-questions) | Pending; no implementation authorized |

## WordPress Solution Blueprint Decisions Required

| ID | Decision required | Source | Status |
| --- | --- | --- | --- |
| FD-WPB-001 | Approve, revise, or reject WPBP-001 through WPBP-010 and assign platform/configuration/deployment owners. | [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md#blueprint-decisions) | Pending; no implementation authorized |
| FD-WPB-002 | Approve, revise, or reject BLOCKSY-001 through BLOCKSY-009, design-system ownership, and presentation policies without creating a child/custom theme exception. | [Blocksy Configuration](36_BLOCKSY_CONFIGURATION.md#blocksy-decisions) | Pending; FD-GOV-008 remains open |
| FD-WPB-003 | Approve, revise, or reject ELEMENTOR-001 through ELEMENTOR-009 and exact delegated template families. | [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md#elementor-decisions) | Pending; no template authorized |
| FD-WPB-004 | Approve, revise, or reject WCCFG-001 through WCCFG-012 and exact catalog/no-price enforcement, stock, account, and Admin policies. | [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md#woocommerce-configuration-decisions) | Pending; no WooCommerce configuration authorized |
| FD-WPB-005 | Approve, revise, or reject CPTBP-001 through CPTBP-008 and decide which candidate content types, if any, require CPTs. | [Custom Post Types](39_CUSTOM_POST_TYPES.md#cpt-blueprint-decisions) | Pending; no CPT registration authorized |
| FD-WPB-006 | Approve, revise, or reject TAXBP-001 through TAXBP-009 and exact physical registry mappings, labels, keys, hierarchies, URLs, and owners. | [Taxonomy Implementation](40_TAXONOMY_IMPLEMENTATION.md#taxonomy-blueprint-decisions) | Pending; no taxonomy configuration authorized |
| FD-WPB-007 | Approve, revise, or reject FIELD-001 through FIELD-009 and exact field/relationship inventory, access, validation, and capability. | [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md#field-decisions) | Pending; no ACF or field implementation authorized |
| FD-WPB-008 | Approve, revise, or reject INQWF-001 through INQWF-011 and exact fields, routing, permissions, notifications, escalation, retention, and future quotation boundaries. | [Inquiry Workflow](42_INQUIRY_WORKFLOW.md#inquiry-workflow-decisions) | Pending; no workflow/plugin authorized |
| FD-WPB-009 | Approve, revise, or reject ROLE-001 through ROLE-009 and exact least-privilege capability/field/transition assignments. | [User Roles](43_USER_ROLES.md#role-decisions) | Pending; no role/capability authorized |
| FD-WPB-010 | Approve, revise, or reject PLUG-001 through PLUG-010, initial capability needs, owners, and later vendor-selection gate. | [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md#plugin-decisions) | Pending; no plugin installation/selection authorized |

## Release Engineering Decisions Required

| ID | Decision required | Source | Status |
| --- | --- | --- | --- |
| FD-REL-001 | Confirm or revise the Implementation Readiness conclusion and assign owners for its blocking prerequisites. | [Implementation Readiness](IMPLEMENTATION_READINESS.md) | Pending; implementation remains blocked |
| FD-REL-002 | Approve, revise, defer, or reject the Sprint 01–10 Roadmap and the entry conditions for Sprint 02. | [Sprint Roadmap](SPRINT_ROADMAP.md) | Pending; roadmap does not authorize work |
| FD-REL-003 | Approve, revise, or reject the Engineering Guidelines and future branch/review/rollback/quality controls. | [Engineering Guidelines](ENGINEERING_GUIDELINES.md) | Pending; exact baseline bootstrap does not approve future workflow |
| FD-REL-004 | Approve remote, independent mirror, backup custody, signing, branch protection, and recovery parameters for distribution of the local v1.0 baseline. | [Baseline Known Limitations](BASELINE_v1.0.md#known-limitations) and [Git Governance](GIT_GOVERNANCE.md) | Pending; local baseline only |

## Remote Access Decisions Required

| ID | Decision required | Source | Status |
| --- | --- | --- | --- |
| FD-RA-001 | Approve, revise, defer, or reject RA-001 through RA-012 and the primary/future/emergency access models. | [Remote Access Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md#proposed-architecture-decisions) | Pending; no connection or deployment authorized |
| FD-RA-002 | Approve the exact Server.ir account/service as a target only after SSH, cPanel, Git, PHP CLI, WP-CLI, path, logging, backup, and support evidence. | [Current Environment](45_REMOTE_ACCESS_ARCHITECTURE.md#current-environment) | Pending; target capabilities unverified |
| FD-RA-003 | Approve GitHub private-remote ownership, MFA, access, recovery, protection, independent backup, and Iran-connectivity controls. | [Recommended Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md#recommended-architecture) | Pending; no approved primary remote |
| FD-RA-004 | Approve the SSH operator, key custodian, hosting identity, project-path boundary, access expiry/review, logging, and revocation. | [SSH Access Checklist](../repository/config/SSH_ACCESS_CHECKLIST.md) | Pending; no key or access grant |
| FD-RA-005 | Approve backup/restore ownership, staging/safe-test target, emergency authority, and manual cPanel fallback rules. | [Deployment Access Policy](../repository/config/DEPLOYMENT_ACCESS_POLICY.md) | Pending; recovery unproven |
| FD-RA-006 | Decide the actual SSH setup go/no-go only after every mandatory access, security, Git, path, backup/restore, and approval gate passes. | [Go / No-Go Rules](45_REMOTE_ACCESS_ARCHITECTURE.md#go-for-actual-ssh-setup-only-if) | Pending; current decision is NO-GO |

## Explicit Founder TODO Register

| ID | Document | Section requiring decision | Status |
| --- | --- | --- | --- |
| FD-000-01 | [DS-000](00_PROJECT_BIBLE.md) | Scope | Pending |
| FD-000-02 | [DS-000](00_PROJECT_BIBLE.md) | Audience | Pending |
| FD-000-03 | [DS-000](00_PROJECT_BIBLE.md) | Overview | Pending |
| FD-000-04 | [DS-000](00_PROJECT_BIBLE.md) | Definitions | Pending |
| FD-000-05 | [DS-000](00_PROJECT_BIBLE.md) | Responsibilities | Pending |
| FD-000-06 | [DS-000](00_PROJECT_BIBLE.md) | Decisions | Pending |
| FD-000-07 | [DS-000](00_PROJECT_BIBLE.md) | Constraints | Pending |
| FD-000-08 | [DS-000](00_PROJECT_BIBLE.md) | Open Questions | Pending |
| FD-000-09 | [DS-000](00_PROJECT_BIBLE.md) | Founder Decisions | Pending |
| FD-000-10 | [DS-000](00_PROJECT_BIBLE.md) | Future Improvements | Pending |
| FD-001-01 | [DS-001](01_PROJECT_CONSTITUTION.md) | Scope | Pending |
| FD-001-02 | [DS-001](01_PROJECT_CONSTITUTION.md) | Audience | Pending |
| FD-001-03 | [DS-001](01_PROJECT_CONSTITUTION.md) | Overview | Pending |
| FD-001-04 | [DS-001](01_PROJECT_CONSTITUTION.md) | Definitions | Pending |
| FD-001-05 | [DS-001](01_PROJECT_CONSTITUTION.md) | Responsibilities | Pending |
| FD-001-06 | [DS-001](01_PROJECT_CONSTITUTION.md) | Decisions | Pending |
| FD-001-07 | [DS-001](01_PROJECT_CONSTITUTION.md) | Constraints | Pending |
| FD-001-08 | [DS-001](01_PROJECT_CONSTITUTION.md) | Open Questions | Pending |
| FD-001-09 | [DS-001](01_PROJECT_CONSTITUTION.md) | Founder Decisions | Pending |
| FD-001-10 | [DS-001](01_PROJECT_CONSTITUTION.md) | Future Improvements | Pending |
| FD-002-01 | [DS-002](02_ARCHITECTURE.md) | Scope | Pending |
| FD-002-02 | [DS-002](02_ARCHITECTURE.md) | Audience | Pending |
| FD-002-03 | [DS-002](02_ARCHITECTURE.md) | Overview | Pending |
| FD-002-04 | [DS-002](02_ARCHITECTURE.md) | Definitions | Pending |
| FD-002-05 | [DS-002](02_ARCHITECTURE.md) | Responsibilities | Pending |
| FD-002-06 | [DS-002](02_ARCHITECTURE.md) | Decisions | Pending |
| FD-002-07 | [DS-002](02_ARCHITECTURE.md) | Constraints | Pending |
| FD-002-08 | [DS-002](02_ARCHITECTURE.md) | Open Questions | Pending |
| FD-002-09 | [DS-002](02_ARCHITECTURE.md) | Founder Decisions | Pending |
| FD-002-10 | [DS-002](02_ARCHITECTURE.md) | Future Improvements | Pending |
| FD-003-01 | [DS-003](03_BUSINESS_RULES.md) | Scope | Pending |
| FD-003-02 | [DS-003](03_BUSINESS_RULES.md) | Audience | Pending |
| FD-003-03 | [DS-003](03_BUSINESS_RULES.md) | Overview | Pending |
| FD-003-04 | [DS-003](03_BUSINESS_RULES.md) | Definitions | Pending |
| FD-003-05 | [DS-003](03_BUSINESS_RULES.md) | Responsibilities | Pending |
| FD-003-06 | [DS-003](03_BUSINESS_RULES.md) | Decisions | Pending |
| FD-003-07 | [DS-003](03_BUSINESS_RULES.md) | Constraints | Pending |
| FD-003-08 | [DS-003](03_BUSINESS_RULES.md) | Open Questions | Pending |
| FD-003-09 | [DS-003](03_BUSINESS_RULES.md) | Founder Decisions | Pending |
| FD-003-10 | [DS-003](03_BUSINESS_RULES.md) | Future Improvements | Pending |
| FD-004-01 | [DS-004](05_TECH_STACK.md) | Scope | Pending |
| FD-004-02 | [DS-004](05_TECH_STACK.md) | Audience | Pending |
| FD-004-03 | [DS-004](05_TECH_STACK.md) | Overview | Pending |
| FD-004-04 | [DS-004](05_TECH_STACK.md) | Definitions | Pending |
| FD-004-05 | [DS-004](05_TECH_STACK.md) | Responsibilities | Pending |
| FD-004-06 | [DS-004](05_TECH_STACK.md) | Decisions | Pending |
| FD-004-07 | [DS-004](05_TECH_STACK.md) | Constraints | Pending |
| FD-004-08 | [DS-004](05_TECH_STACK.md) | Open Questions | Pending |
| FD-004-09 | [DS-004](05_TECH_STACK.md) | Founder Decisions | Pending |
| FD-004-10 | [DS-004](05_TECH_STACK.md) | Future Improvements | Pending |
| FD-005-01 | [DS-005](07_REPOSITORY_GUIDE.md) | Scope | Pending |
| FD-005-02 | [DS-005](07_REPOSITORY_GUIDE.md) | Audience | Pending |
| FD-005-03 | [DS-005](07_REPOSITORY_GUIDE.md) | Overview | Pending |
| FD-005-04 | [DS-005](07_REPOSITORY_GUIDE.md) | Definitions | Pending |
| FD-005-05 | [DS-005](07_REPOSITORY_GUIDE.md) | Responsibilities | Pending |
| FD-005-06 | [DS-005](07_REPOSITORY_GUIDE.md) | Decisions | Pending |
| FD-005-07 | [DS-005](07_REPOSITORY_GUIDE.md) | Constraints | Pending |
| FD-005-08 | [DS-005](07_REPOSITORY_GUIDE.md) | Open Questions | Pending |
| FD-005-09 | [DS-005](07_REPOSITORY_GUIDE.md) | Founder Decisions | Pending |
| FD-005-10 | [DS-005](07_REPOSITORY_GUIDE.md) | Future Improvements | Pending |
| FD-PDS-01 | [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md) | Purpose | Pending |
| FD-PDS-02 | [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md) | Scope | Pending |
| FD-PDS-03 | [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md) | Placeholder Sections | Pending |
| FD-WPA-01 | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md) | Purpose | Resolved by explicit Batch 04 Founder directive; document remains Review |
| FD-WPA-02 | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md) | Scope | Resolved by explicit Batch 04 Founder directive; document remains Review |
| FD-WPA-03 | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md) | Placeholder Sections | Resolved by explicit Batch 04 Founder directive; implementation decisions remain open |
| FD-DEV-01 | [Development Workflow](08_DEVELOPMENT_WORKFLOW.md) | Purpose | Pending |
| FD-DEV-02 | [Development Workflow](08_DEVELOPMENT_WORKFLOW.md) | Scope | Pending |
| FD-DEV-03 | [Development Workflow](08_DEVELOPMENT_WORKFLOW.md) | Placeholder Sections | Pending |
| FD-DEP-01 | [Deployment](09_DEPLOYMENT.md) | Purpose | Pending |
| FD-DEP-02 | [Deployment](09_DEPLOYMENT.md) | Scope | Pending |
| FD-DEP-03 | [Deployment](09_DEPLOYMENT.md) | Placeholder Sections | Pending |
| FD-SEC-01 | [Security](10_SECURITY.md) | Purpose | Pending |
| FD-SEC-02 | [Security](10_SECURITY.md) | Scope | Pending |
| FD-SEC-03 | [Security](10_SECURITY.md) | Placeholder Sections | Pending |
| FD-SEO-01 | [SEO Strategy](11_SEO_STRATEGY.md) | Purpose | Pending |
| FD-SEO-02 | [SEO Strategy](11_SEO_STRATEGY.md) | Scope | Pending |
| FD-SEO-03 | [SEO Strategy](11_SEO_STRATEGY.md) | Placeholder Sections | Pending |
| FD-UX-01 | [UX Principles](12_UX_PRINCIPLES.md) | Purpose | Pending |
| FD-UX-02 | [UX Principles](12_UX_PRINCIPLES.md) | Scope | Pending |
| FD-UX-03 | [UX Principles](12_UX_PRINCIPLES.md) | Placeholder Sections | Pending |
| FD-TST-01 | [Testing Strategy](13_TESTING_STRATEGY.md) | Purpose | Pending |
| FD-TST-02 | [Testing Strategy](13_TESTING_STRATEGY.md) | Scope | Pending |
| FD-TST-03 | [Testing Strategy](13_TESTING_STRATEGY.md) | Placeholder Sections | Pending |
| FD-CHG-01 | [Changelog](14_CHANGELOG.md) | Purpose | Pending |
| FD-CHG-02 | [Changelog](14_CHANGELOG.md) | Scope | Pending |
| FD-CHG-03 | [Changelog](14_CHANGELOG.md) | Placeholder Sections | Pending |

## Decision Recording Rules

- Record the Founder response in the authoritative source document.
- Update this log with the decision date, resulting source link, and status.
- Create an ADR when the approved process classifies the decision as architecturally significant.
- Do not close an entry solely because implementation has started.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Decision Log](10_DECISION_LOG.md)
- [Open Questions](18_OPEN_QUESTIONS.md)
