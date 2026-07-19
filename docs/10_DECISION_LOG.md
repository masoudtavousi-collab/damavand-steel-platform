# Decision Log

## Document Control

- **Document ID:** `docs/10_DECISION_LOG.md` (provisional path identifier)
- **Status:** Draft
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.3.0
- **Last Updated:** 2026-07-19
- **Last Review:** 2026-07-19
- **Review Cycle:** On decision classification, status, or authority change
- **Lifecycle:** Draft
- **Source of Truth:** Approved governing documents and explicitly accepted decision records; this log is an index only
- **Dependencies:** [Project Bible](00_PROJECT_BIBLE.md), [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md), and accepted ADRs
- **Related Documents:** [Founder Decision Log](17_FOUNDER_DECISION_LOG.md), [Open Questions](18_OPEN_QUESTIONS.md), and [Traceability Matrix](TRACEABILITY_MATRIX.md)
- **Traceability:** Decision classifications, source records, affected documents, and approval evidence indexed in this document
- **AI Compatibility:** AI-readable with gaps until Founder approval
- **Approval:** Pending Founder approval

## Purpose

Index decisions already recorded elsewhere. This log does not create, reinterpret, or replace decisions.

## Decision Classification Framework

Decision classification identifies the scope, authority path, ownership, modification control, inheritance behavior, and required traceability of a decision. Classification does not approve a decision.

Founder, Business, Architecture, Technical, Documentation, and Repository are primary scope classifications. Temporary, Deprecated, and Historical describe temporal treatment and may qualify a primary classification; they do not create additional authority.

| Classification | Authority | Owner | Approval process | Modification rules | Inheritance | Current repository example | Traceability |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Founder Decision | Explicitly accepted Founder decision within its recorded scope | Founder | Record proposal or directive, review impact, obtain explicit Founder acceptance, update authoritative source | Only a later explicit Founder decision may amend, supersede, or withdraw it | Constrains every dependent document within scope | CP-001 through CP-010 | Founder Decision Log, source document, affected documents, and evidence |
| Business Decision | Approved business-governing document or accepted decision record | Founder; delegated business owner requires Founder approval | Business review followed by Founder approval | Material change requires impact review and a superseding approved decision | Inherited by architecture, product-data, content, SEO, UX, commerce, and implementation documents within scope | ADR-0001 Inquiry-first commerce | Business Rules, ADR, Decision Log, dependents, and acceptance evidence |
| Architecture Decision | Accepted ADR or approved architecture-governing document | Architecture owner; current approval authority is Founder | Architecture review, ADR when significant, then Founder approval | Change through a superseding ADR or approved architecture revision | Constrains technical, repository, platform, and implementation documents within scope | No separately classified accepted architecture decision is currently indexed | Architecture source, ADR, Decision Log, dependents, and validation evidence |
| Technical Decision | Approved technical-governing document or accepted technical decision record | Technical owner; current approval authority is Founder | Technical review, compatibility and impact evidence, then Founder approval | Change requires compatibility, migration, rollback, and dependency review where applicable | Inherited by platform, delivery, operations, testing, and implementation documents within scope | No approved technical decision is currently indexed | Technology source, decision record, dependents, and test or review evidence |
| Documentation Decision | Approved documentation-governance document | Documentation owner; current approval authority is Founder | Documentation and governance review followed by Founder approval | Change must preserve authority, lifecycle, navigation, metadata, and traceability consistency | Applies to controlled documents without changing their business or architecture content | Document Lifecycle and Repository Metadata Standard remain proposals pending approval | Governance source, affected documents, validation record, and approval |
| Repository Decision | Approved repository-governance document or accepted repository decision record | Repository owner; current approval authority is Founder | Repository impact and governance review followed by Founder approval | Change requires path, ownership, navigation, baseline, and compatibility review | Applies to repository structure and workflows; cannot override business or architecture authority | Numbering and baseline proposals remain pending | Repository Standards, Founder Decision Log, affected paths, and approval evidence |
| Temporary Decision | Explicitly time-bound or condition-bound accepted decision | Owner of the primary classification | Same approval as the primary classification, with expiry or exit condition | May not become permanent by elapsed time; renewal, replacement, or expiry must be recorded | Inherits only within its stated scope and duration | No accepted temporary decision is currently indexed | Primary class, start, expiry or exit condition, owner, and successor outcome |
| Deprecated Decision | Previously accepted decision that is no longer preferred but remains visible during transition | Owner of the primary classification | Approved deprecation with replacement or rationale | Cannot be modified as current authority; corrective notes must preserve the original record | Must not govern new work; dependents migrate to the approved replacement | No deprecated decision is currently indexed | Original source, deprecation approval, replacement, and affected dependents |
| Historical Decision | Retained decision evidence with no current governing effect | Records owner | Historical classification requires evidence that active authority has ended | Immutable except for clearly marked metadata corrections | No inheritance into active requirements | No historical decision is currently indexed | Original source, terminal status, successor when applicable, and archival evidence |

## Classification and Approval Rules

- Every decision has one primary scope classification.
- Temporary, Deprecated, and Historical are recorded as additional treatment only when applicable.
- The current Approval Authority is Founder unless an approved governing document records delegation.
- A task, review, audit, proposal, or conversation cannot classify itself as an accepted decision.
- A more specific decision inherits higher-authority constraints and cannot weaken them.
- Unclear or cross-domain classification is escalated to the Founder Decision Log before approval.
- Approval records identify the decision ID, classification, source, approver, date, affected documents, and lifecycle or decision status.

## Decision Traceability Requirements

Every accepted decision must identify:

- Stable decision ID and classification.
- Authority source, owner, reviewer, and approval authority.
- Proposal, approval, effective date, and current status.
- Parent constraints and inherited rules.
- Documents and decisions it affects or requires.
- Replacement or supersession relationship when applicable.
- Validation evidence and unresolved impacts.

## Core Project Principle Decisions

| IDs | Decision set | Source | Status |
| --- | --- | --- | --- |
| CP-001–CP-010 | Plugin First, Configuration First, Mobile First, Persian RTL, Inquiry First, No Public Pricing, No Custom Theme, No Gravity Forms, No LiteSpeed Cache, and No AI Features (Phase 1) | [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) | Accepted by Founder directive |

## Architecture Decisions

| ID | Decision | Source | Status |
| --- | --- | --- | --- |
| None | No separately classified architecture decision is currently indexed. | [Enterprise Architecture](02_ARCHITECTURE.md) | Pending classification |

## Business Decisions

| ID | Decision | Source | Status |
| --- | --- | --- | --- |
| ADR-0001 | Inquiry-first commerce; WooCommerce is the product catalog authority; public pricing and direct transactional behavior remain disabled. | [ADR 0001](adr/0001-inquiry-first-commerce.md) | Accepted |
| FD-PILOT-001 | The Golden Parent is `لوله استیل دکوراتیو`; exactly three Pipe combinations are approved for the limited pilot under reference IDs `GOLD-PIPE-201-51-050-6M`, `GOLD-PIPE-201-38-050-6M`, and `GOLD-PIPE-201-16-035-6M`. These references are not final commercial SKUs. The remaining 879 rows stay `CANDIDATE_UNVERIFIED`; market availability stays `MISSING_DATA_VALUE` for all 882; import, runtime, and publishing remain `NO-GO`. | [Founder Decision Log](17_FOUNDER_DECISION_LOG.md#settled-golden-pipe-pilot-decision) and GIT-02S Founder directive dated 2026-07-14 | Accepted by explicit Founder directive; superseded only by a later explicit Founder decision |

## Technical Decisions

| ID | Decision | Source | Status |
| --- | --- | --- | --- |
| None | No approved technical decision is currently indexed. | [Technology Stack](05_TECH_STACK.md) | Pending |

## WordPress Founder Constraints

| ID | Decision | Source | Status |
| --- | --- | --- | --- |
| WP-FC-001 | WooCommerce is the product catalog platform within the inquiry-first boundary. | [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#wordpress-specific-founder-constraints) and ADR-0001 | Accepted by explicit Founder directive |
| WP-FC-002 | Blocksy Pro is the vendor-controlled presentation shell; no custom or child theme is authorized. | [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#wordpress-specific-founder-constraints) | Accepted by explicit Founder directive |
| WP-FC-003 | Elementor Pro is the controlled visual composition capability. | [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#wordpress-specific-founder-constraints) | Accepted by explicit Founder directive |
| WP-FC-004 | Variable Parent Product is the required product model. | [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#wordpress-specific-founder-constraints) | Accepted by explicit Founder directive |
| WP-FC-005 | Routine platform management must be available through WordPress Admin whenever supported. | [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#wordpress-specific-founder-constraints) | Accepted by explicit Founder directive |

## Batch 05 Product Data Model Decisions

| IDs | Decision set | Source | Status |
| --- | --- | --- | --- |
| PDM-001–PDM-008 | Product hierarchy, stable identity, canonical registries, product lifecycle, ownership requirements, Draft strategy authority boundary, and future external mapping | [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md#data-model-decisions) | Proposed; pending Founder approval |
| WCM-001–WCM-008 | Variable-product mapping, parent/variation ownership, SKU, attributes and local exceptions, hidden pricing, supply-after-order, and import/export governance | [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md#woocommerce-model-decisions) | Proposed; accepted Founder constraints preserved; mapping pending approval |
| TAX-001–TAX-008 | Canonical taxonomy registry, overlap, slug, SEO landing, term lifecycle, Collections, Product Tags, Application/Use-Case boundary, and CentralSteel mapping | [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md#taxonomy-decisions) | Proposed; pending Founder/domain/SEO approval |
| ATT-001–ATT-007 | Global attribute identity, profiles, values, hierarchy boundary, derived Size, variation/filtering, and SEO usage | [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md#attribute-decisions) | Proposed; pending Founder/domain approval |
| INQ-001–INQ-008 | Inquiry and Customer objects, product snapshots, customer identity, statuses, routing, anti-spam, CRM, and no-price enforcement | [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md#inquiry-decisions) | Proposed; CP-005/CP-006 boundary preserved; workflow pending approval |

## Batch 06 Information Architecture Decisions

| IDs | Decision set | Source | Status |
| --- | --- | --- | --- |
| IA-001–IA-007 | Knowledge-driven information layers, stable identity, canonical ownership, inquiry context, logical-before-physical design, and expansion governance | [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md#information-architecture-decisions) | Proposed; pending Founder/domain/SEO review |
| SITE-001–SITE-007 | Public site domains, governed product/context navigation, Knowledge Center, inquiry access, protected-data exclusion, and menu authority | [Enterprise Site Structure](25_SITE_STRUCTURE.md#site-structure-decisions) | Proposed; pending Founder/domain/UX/SEO review |
| URL-001–URL-008 | Canonical ownership, stable namespaces, parent-product URLs, slug/language, non-canonical states, redirects, and forbidden URLs | [Enterprise URL Architecture](26_URL_ARCHITECTURE.md#url-architecture-decisions) | Proposed; pending Founder/SEO review |
| SRCH-001–SRCH-008 | Governed cross-domain search, discovery, filtering, ranking, access exclusion, and future compatibility without AI implementation | [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md#search-decisions) | Proposed; pending Founder/domain/SEO/UX/security review |
| LINK-001–LINK-007 | Relationship-driven linking, hierarchy, authority distribution, inquiry paths, claim/access boundaries, and lifecycle governance | [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md#internal-linking-decisions) | Proposed; pending Founder/content/SEO review |

## Batch 07 Content and Entity Architecture Decisions

| IDs | Decision set | Source | Status |
| --- | --- | --- | --- |
| CONTENT-001–CONTENT-008 | Governed content identity, domain separation, canonical reuse, lifecycle, risk-based approval, core-principle compliance, platform-independent blocks, and versioning | [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md#content-architecture-decisions) | Proposed; pending Founder/content/domain/SEO review |
| ERM-001–ERM-008 | Stable entity identity, canonical authority, typed relationships, entity-domain separation, minimum contract, access boundaries, expansion, and platform independence | [Enterprise Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md#entity-model-decisions) | Proposed; pending Founder/domain/governance review |
| SCHEMA-001–SCHEMA-009 | Public semantic eligibility, canonical IDs, type specificity, connected graph, no Offer/price, conditional types, validation, platform independence, and vocabulary review | [Schema.org Semantic Strategy](31_SCHEMA_ORG_STRATEGY.md#schema-strategy-decisions) | Proposed; pending Founder/SEO/domain/legal/privacy review |
| CTYPE-001–CTYPE-007 | Controlled type registry, content-domain separation, source references, access classes, independent SEO/navigation approval, lifecycle separation, and physical-mapping deferral | [Enterprise Content Types](32_CONTENT_TYPES.md#content-type-decisions) | Proposed; pending Founder/content/domain/SEO review |
| MEDIA-001–MEDIA-009 | Media identity, source/derivatives, metadata organization, naming, product truth, accessibility/localization, WebP, protected downloads, and infrastructure deferral | [Enterprise Media Strategy](33_MEDIA_STRATEGY.md#media-decisions) | Proposed; pending Founder/content/technical/accessibility/security review |
| SEOENT-001–SEOENT-009 | Entity-first SEO, canonical/intent ownership, source authority, coordinated graph, landing eligibility, no-price/privacy, future retrieval compatibility, and platform independence | [Enterprise SEO Entity Model](34_SEO_ENTITY_MODEL.md#seo-entity-decisions) | Proposed; pending Founder/SEO/domain/content/security review |

## Batch 08 WordPress Solution Blueprint Decisions

All Batch 08 entries remain Review-state proposals and authorize no implementation.

| IDs | Decision set | Source | Status |
| --- | --- | --- | --- |
| WPBP-001–WPBP-010 | Layer authority, single ownership, platform allocation, inquiry/no-price boundary, configuration, RTL/mobile, logical-to-physical mapping, deployment, upgrades, and extension gates | [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md#blueprint-decisions) | Proposed; pending Founder/technical/domain review |
| BLOCKSY-001–BLOCKSY-009 | Vendor theme, no child theme, shell/layout ownership, Customizer/design-system, hooks, RTL/mobile, performance, and upgradeability | [Blocksy Configuration](36_BLOCKSY_CONFIGURATION.md#blocksy-decisions) | Proposed/derived; pending Founder/design/technical review |
| ELEMENTOR-001–ELEMENTOR-009 | Bounded composition, ownership limits, dynamic data, reuse, loops, design system, validation, and forbidden implementation | [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md#elementor-decisions) | Proposed/derived; pending Founder/design/content/technical review |
| WCCFG-001–WCCFG-012 | Catalog-only store, no public transactions/prices, inquiry, stock, attributes, customer/email boundaries, import/export, quotation, and Admin manageability | [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md#woocommerce-configuration-decisions) | Proposed/derived; pending Founder/domain/Sales/technical review |
| CPTBP-001–CPTBP-008 | Native-first mappings, CPT justification and visibility gates, candidate types, and configuration ownership | [Custom Post Types](39_CUSTOM_POST_TYPES.md#cpt-blueprint-decisions) | Proposed; no CPT approved for registration |
| TAXBP-001–TAXBP-009 | Canonical registries, attributes/categories, conditional taxonomies, SEO landings, tags/slugs, identity, and registration gate | [Taxonomy Implementation](40_TAXONOMY_IMPLEMENTATION.md#taxonomy-blueprint-decisions) | Proposed/derived; no taxonomy or term approved |
| FIELD-001–FIELD-009 | Native-first fields, canonical ownership, relationships, access, conditional entities, requiredness, no ACF assumption, and migration | [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md#field-decisions) | Proposed; no field capability approved |
| INQWF-001–INQWF-011 | Canonical lifecycle, validation, assignment, representative, protected quotation, notification, escalation, archive, and Plugin First capability | [Inquiry Workflow](42_INQUIRY_WORKFLOW.md#inquiry-workflow-decisions) | Proposed/derived; pending Founder/Sales/security/privacy review |
| ROLE-001–ROLE-009 | Authority separation, least privilege, core/specialized bundles, protected scope, dual review, Admin manageability, and CRM roles | [User Roles](43_USER_ROLES.md#role-decisions) | Proposed; no role/capability approved |
| PLUG-001–PLUG-010 | Capability fit, configuration, one owner, compatibility, lifecycle, forbidden outputs/vendors/AI, upgrades, and avoidable plugins | [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md#plugin-decisions) | Proposed/required; no new plugin selected |

## Repository Freeze v1.0 Decisions

These accepted decisions are limited to the exact Founder-authorized local repository baseline. They do not approve included Draft/Review content or implementation.

| ID | Decision | Source | Status |
| --- | --- | --- | --- |
| FRZ-001 | Use display label v1.0 and canonical repository/baseline version 1.0.0. | [Repository Baseline](BASELINE_v1.0.md#repository-version) | Accepted by Founder task directive dated 2026-07-04 |
| FRZ-002 | Freeze every non-ignored repository file in the exact baseline commit while preserving each artifact's recorded authority and lifecycle. | [Repository Scope](BASELINE_v1.0.md#repository-scope) | Accepted by Founder task directive dated 2026-07-04 |
| FRZ-003 | Create annotated local tags `baseline-v1.0.0` and `repo-v1.0.0` on the same exact `main` commit. | [Repository Version](BASELINE_v1.0.md#repository-version) | Accepted by Founder task directive dated 2026-07-04 |
| FRZ-004 | Baseline inclusion must not promote Draft/Review documents or unresolved decisions to Approved authority. | [Approved Architecture and Authority](BASELINE_v1.0.md#approved-architecture-and-authority) | Accepted by Founder task directive dated 2026-07-04 |
| FRZ-005 | Treat v1.0 as a repository/knowledge engineering baseline, not a product release, production release, or implementation authorization. | [Release Classification](RELEASE_NOTES_v1.0.md#release-classification) | Accepted by Founder task directive dated 2026-07-04 |
| FRZ-006 | Defer remote, mirror, backup custody, signing, branch protection, and production release until separately approved and evidenced. | [Known Limitations](BASELINE_v1.0.md#known-limitations) | Accepted for v1.0 scope; operational decisions remain pending |

## Sprint 01A Repository Bootstrap Decisions

All Sprint 01A decisions remain Review-state repository-engineering proposals except boundaries directly required by the current task and accepted baseline. They authorize no implementation.

| IDs | Decision set | Source | Status |
| --- | --- | --- | --- |
| S01A-001–S01A-010 | Isolated workspace, folder ownership, excluded runtime/sensitive data, naming, version separation, migration safety, external backups, quality gates, no implementation, and immutable-baseline rollback | [Repository Implementation Rules](../repository/IMPLEMENTATION_RULES.md#repository-bootstrap-decisions) | Proposed/derived; pending Founder review; no build or installation authorized |

## Sprint 01B Environment Preparation Decisions

| ID | Decision/observed boundary | Source | Status |
| --- | --- | --- | --- |
| S01B-001 | Treat the inspected target as a local workstation only; no external hosting environment is claimed or configured. | [Environment Report](../repository/config/ENVIRONMENT_REPORT.md#evidence-boundary) | Current-state evidence |
| S01B-002 | Stop WordPress/component installation because mandatory runtime, exact-version, package/license, security, recovery, testing, and approval prerequisites are missing. | [Blocking Dependencies](../repository/config/ENVIRONMENT_REPORT.md#blocking-dependencies) | Required stop decision under Pre-Implementation Checklist |
| S01B-003 | Install and activate no WordPress, WooCommerce, Blocksy/Blocksy Pro, Elementor Pro, or additional plugin/theme package. | [Plugin Inventory](../repository/config/PLUGIN_INVENTORY.md) | Current-state evidence |
| S01B-004 | Keep repository templates and declared constraints separate from observed active runtime values. | [Environment Report](../repository/config/ENVIRONMENT_REPORT.md) | Required evidence boundary |
| S01B-005 | Keep implementation readiness Blocked; environment reports close no unchecked gate. | [WordPress Baseline](../repository/config/WORDPRESS_BASELINE.md#installation-decision) | Current-state evidence; Founder remediation required |

## Sprint 01C Environment Validation Decisions

These records define evidence and stop boundaries for Sprint 01C. They do not approve versions, packages, dependencies, hosting, installation, activation, configuration, or implementation.

| ID | Decision/observed boundary | Source | Status |
| --- | --- | --- | --- |
| S01C-001 | Carry Sprint 01B observations forward only as dated local evidence; keep unknown, runtime-dependent, and hosting-dependent items unresolved. | [Hosting Validation Checklist](../repository/config/HOSTING_VALIDATION_CHECKLIST.md#sprint-01b-review-classification) | Required evidence boundary |
| S01C-002 | Require every mandatory real-hosting validation item to pass with evidence before installation. | [Hosting Validation Checklist](../repository/config/HOSTING_VALIDATION_CHECKLIST.md#checklist-rules) | Proposed gate; pending approval and evidence |
| S01C-003 | Permit a clean WordPress installation only after exact target/version/package, authorization, security, and restorable `R0` evidence exists. | [WordPress Installation Checklist](../repository/config/WORDPRESS_INSTALLATION_CHECKLIST.md) | Proposed gate; installation not authorized |
| S01C-004 | Limit the future component sequence to WordPress Core, Blocksy, WooCommerce, Blocksy Pro, and Elementor Pro as named by repository governance. | [Plugin Installation Sequence](../repository/config/PLUGIN_INSTALLATION_SEQUENCE.md#evidence-boundary) | Scope boundary; no install authorized |
| S01C-005 | Stop at any package whose exact dependency chain is not explicitly approved; do not infer or select a dependency. | [Plugin Installation Sequence](../repository/config/PLUGIN_INSTALLATION_SEQUENCE.md#dependency-and-activation-order) | Required stop boundary |
| S01C-006 | Require validation and acceptance after clean WordPress and after every approved component stage. | [Post-Install Validation](../repository/config/POST_INSTALL_VALIDATION.md) | Proposed evidence gate |
| S01C-007 | Require a complete, externally held, independently restorable checkpoint before every mutation. | [Rollback Plan](../repository/config/ROLLBACK_PLAN.md#rollback-checkpoints) | Proposed recovery gate |
| S01C-008 | Keep the current real-installation decision `NO-GO` because hosting, runtime, package/dependency, license, recovery, and approval evidence is missing. | [Sprint 01C Audit](AUDIT_REPORT_SPRINT01C.md#go--no-go-decision) | Current-state evidence |

## Sprint 01D Remote Access Architecture Decisions

RA-001 through RA-012 are Review-state proposals and security boundaries. Their registration does not create a GitHub remote, key, credential, SSH account, connection, deployment, hosting change, WordPress installation, or implementation authority.

| IDs | Decision set | Source | Status |
| --- | --- | --- | --- |
| RA-001–RA-005 | Documentation-only boundary; future private GitHub history; project-limited SSH primary candidate; conditional GitHub deployment/Actions; cPanel emergency fallback | [Remote Access Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md#proposed-architecture-decisions) | Proposed; pending Founder/security/operations/hosting review |
| RA-006–RA-007 | No root/shared identity; least privilege, project-path restriction, key-based access, and strict secret/license protection | [Remote Access Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md#security-rules) | Required security boundary; exact implementation pending |
| RA-008–RA-010 | Pre-change restorable backup, clean reviewed Git state, validation/audit, and tested rollback | [Remote Access Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md#risk-controls) | Proposed gates; evidence missing |
| RA-011–RA-012 | Founder-manageable operation and connectivity-independent fallback without weakening integrity, licensing, security, or approval | [Remote Access Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md#founder-usability-constraints) | Proposed; pending Founder review |

## Class B Wave 1 Repository-Control Decision

| Decision ID | Decision | Source | Status |
| --- | --- | --- | --- |
| `FD-GIT-W1-001` | Integrate exactly the 19 approved Wave 1 governance and repository-control paths through `codex/class-b-wave-01-governance`, one commit, push of only that branch, and one Draft PR. Preserve PR #1 and all other Class B work; do not merge or begin Wave 2. | [Founder Decision Log](17_FOUNDER_DECISION_LOG.md#settled-class-b-wave-1-repository-control-decision) and explicit Founder authorization dated 2026-07-19 | `APPROVED` for exact Git/documentation scope only; no runtime, WordPress, product, content, publication, deployment, production, repository-setting, or default-branch authority |

## Pending Decisions

- Items explicitly requiring Founder approval are tracked in the [Founder Decision Log](17_FOUNDER_DECISION_LOG.md).
- Unresolved questions and unclassified placeholders are tracked in [Open Questions](18_OPEN_QUESTIONS.md).
- Existing architecture principles require lifecycle and traceability confirmation before they are indexed as approved decisions.
- Existing environment statements require lifecycle and source confirmation before they are indexed as approved technical decisions.
- The modular numbering proposal and repository baseline strategy remain Founder decisions; no rename or baseline action is authorized.
- The existing Blocksy child-theme placeholder requires Founder clarification under CP-007 No Custom Theme before any theme implementation.
- The proposed Git Governance model, version semantics, first baseline, remotes, mirrors, backup custody, and retention remain pending Founder decisions; no Git mutation or baseline is authorized by the proposal.
- Batch 05 data-model decisions remain Review-state proposals. Exact product structures, values, labels, slugs, SKUs, states, fields, plugin capabilities, and mappings are not accepted decisions.
- Batch 06 Information Architecture decisions remain Review-state proposals. Exact public labels, site inventory, menu order, URLs, search/filter behavior, representative publication, link rules, owners, and implementation remain unapproved.
- Batch 07 Content and Entity Architecture decisions remain Review-state proposals. Exact content inventories, entities, owners, lifecycles, fields, schema eligibility, media standards, SEO intents, public projections, AI/LLM compatibility scope, and implementation remain unapproved.
- Batch 08 WordPress Solution Blueprint decisions remain Review-state proposals. Exact settings, components, versions, roles, fields, CPTs, taxonomies, templates, workflows, providers, deployment, upgrades, and implementation remain unapproved.
- Implementation Readiness, Sprint Roadmap, and Engineering Guidelines remain Review-state outputs. Their existence and inclusion in v1.0 do not authorize Sprint 02 or later work.
- Sprint 01A folders, rules, and checklists remain structure/readiness artifacts. Every Build and Pre-Implementation checklist item is unchecked, and WordPress installation remains blocked.
- Sprint 01B records a stop decision rather than an installation. Exact versions, packages, licenses, hosting, PHP, MariaDB, HTTPS, backup/restore, tests, and approvals remain unresolved.
- Sprint 01C records unchecked validation, installation, component-sequence, post-install, and rollback controls. It closes no environment or implementation gate and adds no approved dependency.
- Sprint 01D remote/access proposals remain Review-state. Server.ir, cPanel, GitHub, SSH, Git, PHP CLI, WP-CLI, target path, credentials, connectivity, backup/restore, and staging capabilities are unverified; actual SSH setup remains `NO-GO`.

## Decision Registration Rules

- The authoritative decision remains in its source document or ADR.
- Each indexed decision must have a stable identifier, source, owner, status, and date.
- A superseded decision must retain its historical link and point to its replacement.
- Pending ideas must not be represented as accepted decisions.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [ADR Guide](adr/README.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
