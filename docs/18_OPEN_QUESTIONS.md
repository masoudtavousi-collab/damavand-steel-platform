# Open Questions

## Document Control

- **Document ID:** `docs/18_OPEN_QUESTIONS.md` (provisional path identifier)
- **Status:** Draft
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On question creation, resolution, blocking impact, or source-document change
- **Lifecycle:** Draft
- **Source of Truth:** Unresolved questions and placeholders in controlled source documents; this register does not answer them
- **Dependencies:** [Founder Decision Log](17_FOUNDER_DECISION_LOG.md), [Decision Log](10_DECISION_LOG.md)
- **Related Documents:** [Documentation Index](08_DOCUMENTATION_INDEX.md), [Review Process](15_REVIEW_PROCESS.md), and [Repository Health](REPOSITORY_HEALTH.md)
- **Traceability:** Question ID, source, status, decision path, and resolution evidence
- **AI Compatibility:** AI-readable with gaps until Founder approval
- **Approval:** Pending Founder approval

## Purpose

Collect unresolved questions and unclassified placeholders without answering them or creating new decisions.

## Explicit Open-Question Sections

| ID | Question source | Current content | Status |
| --- | --- | --- | --- |
| OQ-001 | [DS-000 Open Questions](00_PROJECT_BIBLE.md#open-questions) | TODO (Founder Decision Required) | Open |
| OQ-002 | [DS-001 Open Questions](01_PROJECT_CONSTITUTION.md#open-questions) | TODO (Founder Decision Required) | Open |
| OQ-003 | [DS-002 Open Questions](02_ARCHITECTURE.md#open-questions) | TODO (Founder Decision Required) | Open |
| OQ-004 | [DS-003 Open Questions](03_BUSINESS_RULES.md#open-questions) | TODO (Founder Decision Required) | Open |
| OQ-005 | [DS-004 Open Questions](05_TECH_STACK.md#open-questions) | TODO (Founder Decision Required) | Open |
| OQ-006 | [DS-005 Open Questions](07_REPOSITORY_GUIDE.md#open-questions) | TODO (Founder Decision Required) | Open |

## Normalized Placeholder Register

The following older documents contained unresolved `TBD.` placeholders. Batch 02 normalized them to Founder-decision placeholders without answering them.

| ID | Document | Unresolved fields | Status |
| --- | --- | --- | --- |
| OQ-007 | [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md) | Purpose, Scope, Placeholder Sections | Open |
| OQ-008 | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md) | Purpose, Scope, Placeholder Sections | Resolved by Batch 04; detailed implementation prerequisites remain open below |
| OQ-009 | [Development Workflow](08_DEVELOPMENT_WORKFLOW.md) | Purpose, Scope, Placeholder Sections | Open |
| OQ-010 | [Deployment](09_DEPLOYMENT.md) | Purpose, Scope, Placeholder Sections | Open |
| OQ-011 | [Security](10_SECURITY.md) | Purpose, Scope, Placeholder Sections | Open |
| OQ-012 | [SEO Strategy](11_SEO_STRATEGY.md) | Purpose, Scope, Placeholder Sections | Open |
| OQ-013 | [UX Principles](12_UX_PRINCIPLES.md) | Purpose, Scope, Placeholder Sections | Open |
| OQ-014 | [Testing Strategy](13_TESTING_STRATEGY.md) | Purpose, Scope, Placeholder Sections | Open |
| OQ-015 | [Changelog](14_CHANGELOG.md) | Purpose, Scope, Placeholder Sections | Open |

## Governance Questions

| ID | Question | Related document | Status |
| --- | --- | --- | --- |
| OQ-GOV-001 | Who may approve each category of document? | [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md) | Resolved for Batch 02A: Founder |
| OQ-GOV-002 | What documentation versioning rule is approved? | [Document Template](13_DOCUMENT_TEMPLATE.md) and [Git Governance](GIT_GOVERNANCE.md#versioning-strategy) | Open |
| OQ-GOV-003 | What release-versioning policy governs the changelog? | [Changelog Policy](14_CHANGELOG_POLICY.md) and [Git Governance](GIT_GOVERNANCE.md#versioning-strategy) | Open |
| OQ-GOV-004 | Which roles perform architecture, business, technical, quality, and final validation? | [Review Process](15_REVIEW_PROCESS.md) | Resolved for Batch 02A: Repository Guardian reviews; Founder approves |
| OQ-GOV-005 | What lifecycle status and authority apply to existing architecture principles? | [Architecture Principles](architecture/principles.md) | Open |
| OQ-GOV-006 | What lifecycle status and authority apply to the existing environment matrix? | [Environment Matrix](operations/environments.md) | Open |
| OQ-GOV-007 | Which steel-industry terms and definitions are approved for project use? | [Glossary](11_GLOSSARY.md) | Open |
| OQ-GOV-008 | Should the proposed modular documentation numbering strategy be approved, revised, or rejected? | [Repository Standards](07_REPOSITORY_GUIDE.md#numbering-scalability-proposal) | Open |
| OQ-GOV-009 | When and under what approved version should the first repository baseline be created? | [Repository Baseline v1.0](BASELINE_v1.0.md) and [Git Governance](GIT_GOVERNANCE.md#baseline-strategy) | Resolved for local baseline version 1.0.0 by Founder task directive dated 2026-07-04 |
| OQ-GOV-010 | How must the existing Blocksy child-theme placeholder be handled under CP-007 No Custom Theme? | [Existing placeholder](../public/wp-content/themes/blocksy-child/README.md) | Open; no implementation authorized |
| OQ-GOV-011 | Should the AI Collaboration Standard be approved as repository governance without changing CP-010? | [AI Collaboration Standard](AI_COLLABORATION.md) | Open |
| OQ-GOV-012 | Should provisional path identifiers remain the metadata fallback until numbering migration is approved? | [Repository Metadata Standard](REPOSITORY_METADATA.md) | Open |
| OQ-GOV-013 | Should the Traceability Matrix become the canonical supporting view for end-to-end rule traceability? | [Traceability Matrix](TRACEABILITY_MATRIX.md) | Open |
| OQ-GOV-014 | Should the proposed role-based reading paths become the standard repository entry paths? | [Reading Order](READING_ORDER.md) | Open |
| OQ-GOV-015 | Should the proposed knowledge-graph relationship vocabulary and authority layers be approved? | [Knowledge Graph](KNOWLEDGE_GRAPH.md) | Open |
| OQ-GOV-016 | Should the Decision Classification Framework be approved as the repository classification model? | [Decision Classification Framework](10_DECISION_LOG.md#decision-classification-framework) | Open |
| OQ-GOV-017 | Should the expanded document lifecycle and repository state-transition model be approved? | [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md) | Open |
| OQ-GOV-018 | Should the relationship vocabulary, rule-inheritance hierarchy, and conflict-resolution framework be approved together or with recorded revisions? | [Relationship Metadata](REPOSITORY_METADATA.md#relationship-metadata-model) and [Project Constitution](01_PROJECT_CONSTITUTION.md#conflict-resolution-framework) | Open |
| OQ-GOV-019 | Should the Controlled Document Validation Checklist become the repository validation gate? | [Documentation Quality Standard](16_QUALITY_STANDARD.md#controlled-document-validation-checklist) | Open |
| OQ-GOV-020 | Should the expanded AI change-authority and repository-protection rules be approved without changing CP-010? | [AI Collaboration Standard](AI_COLLABORATION.md#ai-change-authority-matrix) | Open |
| OQ-GOV-021 | Should Git Governance be approved, and which primary remote, independent mirror, backup location, custodians, signing policy, and retention period are authorized? | [Git Governance](GIT_GOVERNANCE.md) and [Baseline Known Limitations](BASELINE_v1.0.md#known-limitations) | Open; exact local baseline authorized, but distribution, custody, signing, protection, and retention remain unresolved |

## WordPress Architecture Questions

| ID | Question | Related document | Status |
| --- | --- | --- | --- |
| OQ-WP-001 | Should WP-ARC-001 through WP-ARC-012 be approved as the governing WordPress Enterprise Architecture? | [Architecture Decision Register](06_WORDPRESS_ARCHITECTURE.md#architecture-decision-register) | Open |
| OQ-WP-002 | Which exact platform versions and plugin brands satisfy the approved capability categories and compatibility requirements? | [Plugin Architecture](06_WORDPRESS_ARCHITECTURE.md#plugin-architecture) | Open; no brand selected |
| OQ-WP-003 | Which product families, attributes, terms, dimensions, units, standards, SKUs, and valid variation combinations are approved? | [Product Architecture](06_WORDPRESS_ARCHITECTURE.md#enterprise-product-architecture) | Open; qualified domain review required |
| OQ-WP-004 | Which taxonomy mechanisms, terms, hierarchies, URLs, filters, and indexation rules are approved? | [Taxonomy Architecture](06_WORDPRESS_ARCHITECTURE.md#taxonomy-architecture) | Open |
| OQ-WP-005 | Which role capabilities, inquiry fields, routing, consent, retention, attachments, notifications, and service levels are approved? | [User Architecture](06_WORDPRESS_ARCHITECTURE.md#user-and-role-architecture) and [Inquiry Architecture](06_WORDPRESS_ARCHITECTURE.md#inquiry-first-architecture) | Open |
| OQ-WP-006 | Which SEO, media, cache, CDN, backup, security, analytics, consent, search, and integration policies and providers are approved? | [Open Architecture Decisions](06_WORDPRESS_ARCHITECTURE.md#open-architecture-decisions) | Open |

## Product Data Questions

| ID | Question | Related document | Status |
| --- | --- | --- | --- |
| OQ-DATA-001 | Which Product Families, Product Groups, Product Types, and parent/variation relationships are approved? | [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md) | Open; qualified domain review required |
| OQ-DATA-002 | Which SKU, stable-ID, stock-state, unit, visibility, and supply-after-order policies are approved? | [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md) | Open |
| OQ-DATA-003 | Which taxonomy mechanisms, terms, hierarchies, Collections, Product Tags, Application/Use-Case terminology, owners, lifecycle, slug language, SEO landings, and CentralSteel mappings are approved? | [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md) | Open |
| OQ-DATA-004 | Which Persian labels, English keys, allowed values, profiles, hierarchy exceptions, Size derivations, variations, filters, units, and SEO uses are approved? | [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md) | Open; qualified domain review required |
| OQ-DATA-005 | Which Customer identity/lifecycle rules, inquiry fields, statuses, routing, consent, attachments, notifications, anti-spam, retention/deletion, and CRM policies are approved? | [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md) | Open; Sales/security/privacy review required |
| OQ-DATA-006 | Which plugin capabilities and supported versions can implement the models through Admin configuration? | [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md#admin-manageability-constraints) | Open; no plugin selected |
| OQ-DATA-007 | Which data fields and systems will become authoritative when ERP, CRM, or CentralSteel integrations are approved? | [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md#crm-and-future-erp-compatibility) | Open; integrations not authorized |
| OQ-DATA-008 | Which product lifecycle transitions, owners, evidence, public behaviors, restoration rules, and archival rules are approved? | [Proposed Product Lifecycle](19_PRODUCT_DATA_MODEL.md#proposed-product-lifecycle) | Open |
| OQ-DATA-009 | Will the Draft Product Data Strategy be completed, superseded, deprecated, or archived? | [Product Data Strategy Relationship](19_PRODUCT_DATA_MODEL.md#relationship-to-product-data-strategy) | Open; FD-PDS-01 through FD-PDS-03 remain pending |

## Information Architecture Questions

| ID | Question | Related document | Status |
| --- | --- | --- | --- |
| OQ-IA-001 | Which public information domains, Persian labels, top-navigation order, footer groups, and mobile behaviors are approved? | [Enterprise Site Structure](25_SITE_STRUCTURE.md) | Open |
| OQ-IA-002 | Which Knowledge Center topics, content types, support pathways, public documents, and owners are approved? | [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md#knowledge-hierarchy) | Open; content/domain review required |
| OQ-IA-003 | Are representative directory/profile pages public, which fields/relationships may they expose, and who owns lifecycle/privacy/routing decisions? | [Representative Layers](24_INFORMATION_ARCHITECTURE.md#representative-layers) | Open; Founder/Sales/privacy review required |
| OQ-IA-004 | Which landing types and taxonomy/attribute views may own canonical indexable intent? | [Landing Page Hierarchy](24_INFORMATION_ARCHITECTURE.md#landing-page-hierarchy) and [SEO Landing Structure](25_SITE_STRUCTURE.md#seo-landing-structure) | Open; Founder/SEO/domain review required |
| OQ-IA-005 | Which namespace roots, slug script/language, canonical product/variation, redirect, and future-language rules are approved? | [Enterprise URL Architecture](26_URL_ARCHITECTURE.md) | Open; Founder/SEO review required |
| OQ-IA-006 | Which searchable fields, filters, synonyms, Persian normalization, ranking signals, result types, privacy/retention, and evaluation rules are approved? | [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md) | Open; domain/SEO/UX/security review required |
| OQ-IA-007 | Which explicit relationships may produce public category, product, knowledge, representative, landing, support, and inquiry links? | [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md) | Open; domain/content/SEO review required |
| OQ-IA-008 | Who owns IA, site structure, URLs, navigation, search, internal linking, representative information, knowledge, support, and migration review? | [Information Ownership](24_INFORMATION_ARCHITECTURE.md#information-ownership) | Open; Founder assignment required |

## Content and Entity Architecture Questions

| ID | Question | Related document | Status |
| --- | --- | --- | --- |
| OQ-CEA-001 | Which content domains, inventories, audiences, Persian labels, lifecycle, version, retention, reuse blocks, and approval workflows are approved? | [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md) | Open; Founder/content/domain review required |
| OQ-CEA-002 | Which conditional entities—Location, Project, Installation, Representative profile, Local Business, Review, News, and Announcement—are required and public? | [Enterprise Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md) | Open; Founder/business/privacy review required |
| OQ-CEA-003 | Who owns every entity and relationship type, and which fields are public, protected, internal, localized, derived, or integration-only? | [Common Entity Contract](30_ENTITY_RELATIONSHIP_MODEL.md#common-entity-contract) | Open; Founder assignment required |
| OQ-CEA-004 | Which Organization, LocalBusiness, Product/Variation, Article, FAQ, Collection, Search, Person, Project, Review, Image, and Video semantic projections are eligible? | [Schema.org Semantic Strategy](31_SCHEMA_ORG_STRATEGY.md) | Open; Founder/SEO/domain/legal/privacy review required |
| OQ-CEA-005 | Which logical content types are required and which receive public archives, canonical pages, search results, schema projections, or navigation entries? | [Enterprise Content Types](32_CONTENT_TYPES.md) | Open; Founder/content/SEO review required |
| OQ-CEA-006 | Which media types, roles, naming, folder views, lifecycle, rights, accessibility, dimensions, formats, WebP rules, PDFs, downloads, and localization policies are approved? | [Enterprise Media Strategy](33_MEDIA_STRATEGY.md) | Open; Founder/content/technical/accessibility/security review required |
| OQ-CEA-007 | Which canonical entities, relationships, search intents, and landing owners are in the approved initial SEO scope? | [Enterprise SEO Entity Model](34_SEO_ENTITY_MODEL.md) | Open; Founder/SEO/domain review required |
| OQ-CEA-008 | What evidence and phase decision would be required before any AI/LLM/semantic-search/knowledge-retrieval capability is evaluated? | [Future AI and LLM Compatibility](34_SEO_ENTITY_MODEL.md#future-ai-search-compatibility) | Open; no AI implementation authorized |
| OQ-CEA-009 | How will schema vocabulary/consumer-policy change, content/entity versioning, and semantic projection invalidation be reviewed? | [Validation and Change Control](31_SCHEMA_ORG_STRATEGY.md#validation-and-change-control) | Open; governance/SEO review required |
| OQ-CEA-010 | Who approves content claims, media rights, accessibility, privacy, legal, technical, SEO, and localization evidence by risk? | [Content Approval Workflow](29_CONTENT_ARCHITECTURE.md#content-approval-workflow) | Open; Founder assignment required |

## WordPress Solution Blueprint Questions

| ID | Question | Related document | Status |
| --- | --- | --- | --- |
| OQ-WPB-001 | Which owners, environments, providers, versions, deployment/upgrade/rollback policies, and evidence gates are approved? | [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md) | Open; Founder/technical review required |
| OQ-WPB-002 | Which design tokens, layouts, Blocksy modules/controls, hooks, presentation owners, and configuration custody are approved? | [Blocksy Configuration](36_BLOCKSY_CONFIGURATION.md) | Open; Founder/design/technical review required |
| OQ-WPB-003 | Which page/template families, dynamic fields, reusable blocks, widgets, conditions, and lifecycle rules are approved for Elementor? | [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md) | Open; Founder/content/design/technical review required |
| OQ-WPB-004 | Which catalog visibility, no-price enforcement, stock mapping, account, import/export, email, and Admin policies are approved? | [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md) | Open; Founder/domain/Sales/technical review required |
| OQ-WPB-005 | Which logical content types, if any, require CPTs, public archives, URLs, search/schema eligibility, permissions, and lifecycle mappings? | [Custom Post Types](39_CUSTOM_POST_TYPES.md) | Open; no CPT approved |
| OQ-WPB-006 | Which canonical registries map to categories, attributes, taxonomies, or relationships, and what terms/hierarchies/URLs are approved? | [Taxonomy Implementation](40_TAXONOMY_IMPLEMENTATION.md) | Open; domain/SEO/technical review required |
| OQ-WPB-007 | Which fields are not native, and what requiredness, access, validation, ownership, localization, and migration rules apply? | [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md) | Open; no ACF assumption or field capability selected |
| OQ-WPB-008 | What inquiry fields, consent, routing, roles, transitions, notifications, service thresholds, retention, and protected quotation/CRM rules apply? | [Inquiry Workflow](42_INQUIRY_WORKFLOW.md) | Open; Founder/Sales/security/privacy review required |
| OQ-WPB-009 | Which core/specialized role bundles become WordPress roles, and what object/field/transition capabilities and access-review rules apply? | [User Roles](43_USER_ROLES.md) | Open; Founder/security/privacy review required |
| OQ-WPB-010 | Which capability slots are required, which are satisfied by the platform/hosting, and which vendors/versions pass the future selection gate? | [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md) | Open; no new plugin selected |

## Release Engineering Questions

| ID | Question | Related document | Status |
| --- | --- | --- | --- |
| OQ-REL-001 | Which approval sequence, assigned owners, exact version matrix, and minimum security/operations evidence will close the blockers before Sprint 02? | [Implementation Readiness](IMPLEMENTATION_READINESS.md#blocking-items) | Open; Founder and specialist decisions required |
| OQ-REL-002 | When may the local v1.0 baseline be pushed to an approved primary remote and replicated to an independent mirror/backup? | [Repository Baseline](BASELINE_v1.0.md#baseline-integrity-and-supersession) | Open; OQ-GOV-021 remains canonical for provider/custody parameters |
| OQ-REL-003 | Which Sprint 02 objectives and deliverables receive separate implementation authorization? | [Sprint 02](SPRINT_ROADMAP.md#sprint-02-wordpress-foundation) | Open; roadmap inclusion is not authorization |

## Resolution Rules

- Answers belong in the authoritative source document, not only in this register.
- Link the approved answer and decision source before closing an item.
- Move Founder approval items through the [Founder Decision Log](17_FOUNDER_DECISION_LOG.md).
- Do not convert an unresolved question into a requirement without approval.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
- [Decision Log](10_DECISION_LOG.md)
