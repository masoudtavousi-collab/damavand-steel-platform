# Founder Decision Log

## Document Control

- **Document ID:** `docs/17_FOUNDER_DECISION_LOG.md` (provisional path identifier)
- **Status:** Draft
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.10.0
- **Last Updated:** 2026-07-23
- **Last Review:** 2026-07-23
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
