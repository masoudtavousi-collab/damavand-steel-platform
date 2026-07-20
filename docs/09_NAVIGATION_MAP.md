# Navigation Map

## Document Control

- **Document ID:** `docs/09_NAVIGATION_MAP.md` (provisional path identifier)
- **Status:** Draft
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.4.0
- **Last Updated:** 2026-07-19
- **Last Review:** 2026-07-19
- **Review Cycle:** On repository path, document index, reading path, or relationship change
- **Lifecycle:** Draft
- **Source of Truth:** [Documentation Index](08_DOCUMENTATION_INDEX.md) and current repository paths
- **Dependencies:** [Documentation Index](08_DOCUMENTATION_INDEX.md)
- **Related Documents:** [Reading Order](READING_ORDER.md), [Knowledge Graph](KNOWLEDGE_GRAPH.md), [Git Governance](GIT_GOVERNANCE.md), and [Repository Health](REPOSITORY_HEALTH.md)
- **Traceability:** Repository paths, cross-reference rules, reading paths, and architecture paths
- **AI Compatibility:** AI-readable with gaps until Founder approval
- **Approval:** Pending Founder approval

## Purpose

Define repository navigation and reading paths without changing directory ownership or architecture.

## Repository Navigation

### Codex Governance Entry

1. [Codex Repository Instructions](../AGENTS.md)
2. [Project Baseline](PROJECT_BASELINE.md)
3. [Repository Reading Order](READING_ORDER.md)
4. [Current Project State](CURRENT_PROJECT_STATE.md)
5. [Repository Relationship Map](REPOSITORY_RELATIONSHIP_MAP.md)
6. [Project Execution Roadmap](PROJECT_EXECUTION_ROADMAP.md)
7. [Codex Sprint Protocol](CODEX_SPRINT_PROTOCOL.md)
8. [Source of Truth Priority](SOURCE_OF_TRUTH_PRIORITY.md)
9. [Settled Class B Wave 1 Repository-Control Decision](17_FOUNDER_DECISION_LOG.md#settled-class-b-wave-1-repository-control-decision)
10. Future Reference: GIT-02S Audit — `docs/AUDIT_REPORT_GIT02S.md` (Not yet approved) as historical 2026-07-14 evidence

This path is governance and Founder-review only. The current Wave 1 directive permits only its exact 19-path documentation commit, branch push, and Draft PR. It authorizes no merge, Wave 2–10 integration, runtime, import, WordPress, content, product, publishing, deployment, production mutation, or automatic pilot execution.

### Current Git Integration Path

`main` at `96f2ea70f9010fce416a18310e98915e2be537b9` → bootstrap commit `b20e95de8b1b67d2bc610130648700e82a6855b3` → open, Draft, unmerged PR #1 with 24 paths → `codex/class-b-wave-01-governance` with exactly 19 approved governance paths → new Draft PR → Founder review → **STOP before merge**.

Class B Waves 2–10 and the six Sprint 1 reports remain local, unstaged, unapproved, and outside this path.

| Path | Existing responsibility | Primary documentation |
| --- | --- | --- |
| `/docs` | Project documentation | [Documentation Index](08_DOCUMENTATION_INDEX.md) |
| `/quality` | Reusable quality gates | [Enterprise Quality Standard](../quality/QUALITY_STANDARD.md) |
| `/config` | Configuration templates | [Technology Stack](05_TECH_STACK.md) |
| `/infrastructure` | Infrastructure templates | [Deployment](09_DEPLOYMENT.md) |
| `/public` | Public web root and WordPress content boundary | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md) |
| `/scripts` | Repository operational scripts | [Development Workflow](08_DEVELOPMENT_WORKFLOW.md) |
| `/assets` | Source project assets | [Repository Standards](07_REPOSITORY_GUIDE.md) |
| `/prompts` | Versioned prompt materials | [Repository Standards](07_REPOSITORY_GUIDE.md) |
| `/tests` | Test scaffolding and evidence locations | [Testing Strategy](13_TESTING_STRATEGY.md) |
| `/var` | Local runtime placeholders | [Deployment](09_DEPLOYMENT.md) |

## Cross-Reference Rules

- Link to the canonical governing document before linking to supporting details.
- Link to an ADR for the decision itself and to the Decision Log for discovery.
- Topic-folder documents must link back to their top-level governing document.
- Audit reports may link to findings but must not become requirements authorities.
- Unresolved items must link to the Open Questions or Founder Decision Log entry that tracks them.

## Reading Paths

### Founder and Governance Path

[Project Baseline](PROJECT_BASELINE.md) → [Project Bible](00_PROJECT_BIBLE.md) → [Project Constitution](01_PROJECT_CONSTITUTION.md) → [Founder Decision Log](17_FOUNDER_DECISION_LOG.md) → [Open Questions](18_OPEN_QUESTIONS.md) → [Decision Log](10_DECISION_LOG.md)

### Historical GIT-02S Reconciliation and Pilot Evidence Path

[Current Project State](CURRENT_PROJECT_STATE.md) → [FD-PILOT-001](17_FOUNDER_DECISION_LOG.md#settled-golden-pipe-pilot-decision) → Future Reference: Sprint 10R Audit — `docs/AUDIT_REPORT_SPRINT10R.md` (Not yet approved) → Future Reference: Sprint 11 Audit — `docs/AUDIT_REPORT_SPRINT11.md` (Not yet approved) → Future Reference: Golden Product Runtime Preflight — `docs/GOLDEN_PRODUCT_RUNTIME_PREFLIGHT.md` (Not yet approved) → Future Reference: Sprint 12A Audit — `docs/AUDIT_REPORT_SPRINT12A.md` (Not yet approved) → Future Reference: Repository Freeze Report — `docs/REPOSITORY_FREEZE_REPORT.md` (Not yet approved) → Future Reference: GIT-02S Audit — `docs/AUDIT_REPORT_GIT02S.md` (Not yet approved)

### Git Reconciliation Evidence Path

[Git Governance](GIT_GOVERNANCE.md) → Future Reference: Git Baseline Audit — `docs/GIT_BASELINE_AUDIT.md` (Not yet approved) → Future Reference: Git Baseline Commit Report — `docs/GIT_BASELINE_COMMIT_REPORT.md` (Not yet approved) → Future Reference: Git EOF Normalization Report — `docs/GIT_EOF_NORMALIZATION_REPORT.md` (Not yet approved) → [Git Baseline Approval Checklist](GIT_BASELINE_APPROVAL_CHECKLIST.md) → [Git File Classification](GIT_FILE_CLASSIFICATION.csv) → Future Reference: Repository Freeze Report — `docs/REPOSITORY_FREEZE_REPORT.md` (Not yet approved) → Future Reference: GIT-02S Audit — `docs/AUDIT_REPORT_GIT02S.md` (Not yet approved)

### Cross-Repository Path

[Repository Relationship Map](REPOSITORY_RELATIONSHIP_MAP.md) controls interpretation. Repository B is isolated `QUARANTINED_ARCHITECTURE_RESEARCH`; its Factory and Generator concepts are not project authorities and are not implementation-ready.

### Architecture Path

[Enterprise Architecture](02_ARCHITECTURE.md) → [Architecture Principles](architecture/principles.md) → [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md) → [ADR Guide](adr/README.md) → [Decision Log](10_DECISION_LOG.md) → [Batch 04 Audit](AUDIT_REPORT_BATCH04.md)

### Business Path

[Business Rules](03_BUSINESS_RULES.md) → [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md) → [Content Operations](content/README.md) → [SEO Strategy](11_SEO_STRATEGY.md)

### Product Data Path

[Business Rules](03_BUSINESS_RULES.md) → [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md) → [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md) → [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md) → [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md) → [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md) → [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md) → [Batch 05 Audit](AUDIT_REPORT_BATCH05.md) → [Batch 05A Audit](AUDIT_REPORT_BATCH05A.md) → [Batch 05B Audit](AUDIT_REPORT_BATCH05B.md)

### Information Architecture Path

[Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) → [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md) → [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md) → [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md) → [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md) → [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md) → [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md) → [Enterprise Site Structure](25_SITE_STRUCTURE.md) → [Enterprise URL Architecture](26_URL_ARCHITECTURE.md) → [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md) → [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md) → [Batch 06 Audit](AUDIT_REPORT_BATCH06.md)

### Content and Entity Architecture Path

[Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md) → [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md) → [Enterprise Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md) → [Schema.org Semantic Strategy](31_SCHEMA_ORG_STRATEGY.md) → [Enterprise Content Types](32_CONTENT_TYPES.md) → [Enterprise Media Strategy](33_MEDIA_STRATEGY.md) → [Enterprise SEO Entity Model](34_SEO_ENTITY_MODEL.md) → [Batch 07 Audit](AUDIT_REPORT_BATCH07.md)

### WordPress Solution Blueprint Path

[WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md) → [Enterprise WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md) → [Blocksy Configuration](36_BLOCKSY_CONFIGURATION.md) + [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md) + [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md) → [Custom Post Types](39_CUSTOM_POST_TYPES.md) + [Taxonomy Implementation](40_TAXONOMY_IMPLEMENTATION.md) + [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md) → [Inquiry Workflow](42_INQUIRY_WORKFLOW.md) + [User Roles](43_USER_ROLES.md) + [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md) → [Batch 08 Audit](AUDIT_REPORT_BATCH08.md)

### Repository Freeze and Release Engineering Path

[Repository Baseline v1.0](BASELINE_v1.0.md) → [Repository Release Notes v1.0](RELEASE_NOTES_v1.0.md) → [Implementation Readiness](IMPLEMENTATION_READINESS.md) → [Sprint Roadmap](SPRINT_ROADMAP.md) → [Engineering Guidelines](ENGINEERING_GUIDELINES.md) → [Repository Freeze v1.0 Audit](AUDIT_REPORT_FREEZE_v1.0.md)

This path records the local baseline and future gates. It does not promote Review-state architecture/Blueprint documents or authorize implementation.

### Sprint 01A Repository Bootstrap Path

[Repository Baseline v1.0](BASELINE_v1.0.md) → [Implementation Readiness](IMPLEMENTATION_READINESS.md) → [Engineering Guidelines](ENGINEERING_GUIDELINES.md) → [Repository Implementation Rules](../repository/IMPLEMENTATION_RULES.md) → [Repository Build Checklist](../repository/BUILD_CHECKLIST.md) → [Pre-Implementation Checklist](../repository/PRE_IMPLEMENTATION_CHECKLIST.md) → [Sprint 01A Audit](AUDIT_REPORT_SPRINT01A.md)

This path describes structure and gates only. No folder or checklist authorizes installation, configuration, code, migration, backup execution, or build activity.

### Sprint 01B Environment Preparation Path

[Repository Baseline v1.0](BASELINE_v1.0.md) → [Implementation Readiness](IMPLEMENTATION_READINESS.md) → [Build Checklist](../repository/BUILD_CHECKLIST.md) + [Pre-Implementation Checklist](../repository/PRE_IMPLEMENTATION_CHECKLIST.md) → [Environment Report](../repository/config/ENVIRONMENT_REPORT.md) → [Plugin Inventory](../repository/config/PLUGIN_INVENTORY.md) → [WordPress Baseline](../repository/config/WORDPRESS_BASELINE.md) → [Sprint 01B Audit](AUDIT_REPORT_SPRINT01B.md)

The observed environment fails mandatory gates, so this path ends at a documented stop decision and contains no installation or configuration.

### Sprint 01C Environment Validation Path

[Sprint 01B Audit](AUDIT_REPORT_SPRINT01B.md) → [Hosting Validation Checklist](../repository/config/HOSTING_VALIDATION_CHECKLIST.md) → [WordPress Installation Checklist](../repository/config/WORDPRESS_INSTALLATION_CHECKLIST.md) → [Plugin Installation Sequence](../repository/config/PLUGIN_INSTALLATION_SEQUENCE.md) → [Post-Install Validation](../repository/config/POST_INSTALL_VALIDATION.md) + [Rollback Plan](../repository/config/ROLLBACK_PLAN.md) → [Sprint 01C Audit](AUDIT_REPORT_SPRINT01C.md)

This path defines evidence gates only. All checks and rollback checkpoints are unresolved, unresolved package dependencies stop the sequence, and the real-installation decision remains `NO-GO`.

### Sprint 01D Remote Access Architecture Path

[Repository Baseline v1.0](BASELINE_v1.0.md) + [Engineering Guidelines](ENGINEERING_GUIDELINES.md) + [Sprint 01C Audit](AUDIT_REPORT_SPRINT01C.md) → [Remote Access Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md) → [SSH Access Checklist](../repository/config/SSH_ACCESS_CHECKLIST.md) + [Deployment Access Policy](../repository/config/DEPLOYMENT_ACCESS_POLICY.md) + [Iran Execution Risk Register](../repository/config/IRAN_EXECUTION_RISK_REGISTER.md) → [Sprint 01D Audit](AUDIT_REPORT_SPRINT01D.md)

This path is documentation-only. GitHub, Server.ir, cPanel, SSH, WP-CLI, target paths, credentials, and network behavior remain unverified; actual SSH setup is `NO-GO`.

### Sprint 03A Product Data Engine Path

[Product Data Model](19_PRODUCT_DATA_MODEL.md) + [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md) + [Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md) + [Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md) + [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md) → [Pipe Product Family](../repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md) + [Attribute Dictionary](../repository/data/attributes/ATTRIBUTE_DICTIONARY.md) → [Pipe Variation Matrix](../repository/data/products/pipes/PIPE_VARIATION_MATRIX.md) + [Pipe SEO Entity Model](../repository/data/seo/PIPE_SEO_ENTITY_MODEL.md) → [WooCommerce Pipe Import Template](../repository/data/imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv) + [Product Data Validation Rules](../repository/data/validation/PRODUCT_DATA_VALIDATION_RULES.md) → [Sprint 03A Audit](AUDIT_REPORT_SPRINT03A.md)

This path creates controlled repository data assets only. Placeholder SKUs, `TBD` commercial values, unapproved combinations, taxonomy/slug decisions, and absent rollback evidence block WordPress import.

### Sprint 03B–03C Pipe Mapping and Classification Path

[Pipe Product Family](../repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md) + [Attribute Dictionary](../repository/data/attributes/ATTRIBUTE_DICTIONARY.md) + [Pipe Variation Matrix](../repository/data/products/pipes/PIPE_VARIATION_MATRIX.md) → [Pipe WooCommerce Mapping](../repository/data/products/pipes/PIPE_WOOCOMMERCE_MAPPING.md) + [Pipe Import Mapping](../repository/data/imports/woocommerce/PIPE_IMPORT_MAPPING.md) → [Pipe Import Precheck](../repository/data/validation/PIPE_IMPORT_PRECHECK.md) → [Pipe Taxonomy and Attribute Classification](../repository/data/taxonomies/PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md) → [Pipe Category Model](../repository/data/taxonomies/PIPE_CATEGORY_MODEL.md) + [Pipe Attribute Model](../repository/data/attributes/PIPE_ATTRIBUTE_MODEL.md) → [Pipe Data Governance Checklist](../repository/data/validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md) → [Sprint 03C Audit](AUDIT_REPORT_SPRINT03C.md)

[Sprint 03B Audit](AUDIT_REPORT_SPRINT03B.md) records the mapping/precheck boundary. These paths authorize review only: final IDs/SKUs, valid commercial combinations, stock, public slug, runtime mappings, staging, backup, rollback, and execution approval remain unresolved.

### Sprint 03D Enterprise Product Engine Path

[Governing Product/Taxonomy/Attribute/Inquiry/SEO/WooCommerce Models](19_PRODUCT_DATA_MODEL.md) → [Enterprise Product Engine](../repository/engine/product/PRODUCT_ENGINE.md) → [Engine Rules](../repository/engine/product/ENGINE_RULES.md) + [Engine Workflow](../repository/engine/product/ENGINE_WORKFLOW.md) + [Engine Generation Guide](../repository/engine/product/ENGINE_GENERATION_GUIDE.md) → [Product Family Template](../repository/engine/product/PRODUCT_FAMILY_TEMPLATE.md) + [Attribute Template](../repository/engine/product/ATTRIBUTE_TEMPLATE.md) + [Variation Template](../repository/engine/product/VARIATION_TEMPLATE.md) + [Import Template](../repository/engine/product/IMPORT_TEMPLATE.md) + [SEO Template](../repository/engine/product/SEO_TEMPLATE.md) + [Validation Template](../repository/engine/product/VALIDATION_TEMPLATE.md) → future family-specific controlled assets → separate implementation authorization

[Pipe Product Family](../repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md) remains the current implementation example. The engine owns generation structure/provenance only; governing documents and approved family evidence own facts. Sprint 03D creates no future family data or runtime output.

### Sprint 03E Enterprise Platform Constitution Path

[Accepted Founder/Core Principles/ADR authority](00_PROJECT_BIBLE.md#core-project-principles) + [Project Constitution](01_PROJECT_CONSTITUTION.md) + [Business Rules](03_BUSINESS_RULES.md) → [Platform Manifest](../repository/platform/PLATFORM_MANIFEST.md) → [Platform Principles](../repository/platform/PLATFORM_PRINCIPLES.md) + [Platform Architecture](../repository/platform/PLATFORM_ARCHITECTURE.md) + [Platform Governance](../repository/platform/PLATFORM_GOVERNANCE.md) → [Engine Boundaries](../repository/platform/ENGINE_BOUNDARIES.md) + [Platform Lifecycle](../repository/platform/PLATFORM_LIFECYCLE.md) + [Directory Standard](../repository/platform/PLATFORM_DIRECTORY_STANDARD.md) + [Platform Versioning](../repository/platform/PLATFORM_VERSIONING.md) + [Platform Evolution](../repository/platform/PLATFORM_EVOLUTION.md) → [Product Engine](../repository/engine/product/PRODUCT_ENGINE.md) and future approved Engines → replaceable Runtime adapters → reusable Websites

The Platform set remains Review/Proposed Governing until explicit Founder approval. It defines architecture only: no Runtime, WordPress, Engine implementation, website, product, content, integration, or release is created.

### Sprint 04A Infrastructure Audit Path

[Sprint 02C Site Health Evidence](AUDIT_REPORT_SPRINT02C.md) + current Sprint 04A findings → [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md) → [REST API Diagnostic](REST_API_DIAGNOSTIC.md) + [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md) → [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md) → [Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md)

This path is evidence/read-only. cURL error 28 proves timeout but not root cause. DNS, IPv6, loopback/hairpin, TLS, firewall, ModSecurity, LiteSpeed, CloudLinux, HTTP API, plugin, and resource causes remain hypotheses until evidence resolves them. WooCommerce implementation and all remediation remain `NO-GO`.

### Sprint 04B–04C Authenticated Audit and Remediation Planning Path

[Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md) → [Sprint 04B Audit](AUDIT_REPORT_SPRINT04B.md) → [Sprint 04B Authenticated Audit](AUDIT_REPORT_SPRINT04B_AUTHENTICATED.md) → [Master Remediation Roadmap](MASTER_REMEDIATION_ROADMAP.md) → [Implementation Sequence](IMPLEMENTATION_SEQUENCE.md) + [Execution Gates](EXECUTION_GATES.md) → [Sprint 04C Audit](AUDIT_REPORT_SPRINT04C.md)

Authenticated evidence refines earlier unknowns but does not authorize a change. The Roadmap is the deduplicated planning register; the Sequence orders future work; the Gates define evidence and approvals. Every execution gate remains closed until separately satisfied and approved.

### Sprint 05A Design Intelligence and Motion Path

[Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) + [WordPress Blueprint](35_WORDPRESS_BLUEPRINT.md) + [Blocksy Blueprint](36_BLOCKSY_CONFIGURATION.md) + [Elementor Blueprint](37_ELEMENTOR_ARCHITECTURE.md) → [Design Manifest](../repository/design/DESIGN_MANIFEST.md) + [Brand Language](../repository/design/BRAND_LANGUAGE.md) + [Design Decision Records](../repository/design/DESIGN_DECISION_RECORDS.md) → [Motion System](../repository/design/MOTION_SYSTEM.md) + [ReactBits Inspiration Mapping](../repository/design/REACTBITS_INSPIRATION_MAPPING.md) → [Component Pattern Library](../repository/design/COMPONENT_PATTERN_LIBRARY.md) + [Animation Library](../repository/design/ANIMATION_LIBRARY.md) → [Performance Rules](../repository/design/PERFORMANCE_RULES.md) + [Accessibility Rules](../repository/design/ACCESSIBILITY_RULES.md) → [Sprint 05A Audit](AUDIT_REPORT_SPRINT05A.md)

This is a repository-guidance path only. ReactBits is inspiration, not a package or runtime dependency. No WordPress, Blocksy, Elementor, page, template, CSS, JavaScript, React, or production asset is created.

### Sprint 06A Knowledge Intelligence Path

[Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md) + [Product Data Model](19_PRODUCT_DATA_MODEL.md) + [Content Architecture](29_CONTENT_ARCHITECTURE.md) + [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md) + [SEO Entity Model](34_SEO_ENTITY_MODEL.md) + [Knowledge Engine Boundary](../repository/platform/ENGINE_BOUNDARIES.md#knowledge-engine) → Future Reference: Knowledge Manifest — `repository/knowledge/KNOWLEDGE_MANIFEST.md` (Not yet approved) → Future Reference: Entity Model — `repository/knowledge/ENTITY_MODEL.md` (Not yet approved) + Future Reference: Ontology Model — `repository/knowledge/ONTOLOGY_MODEL.md` (Not yet approved) + Future Reference: Relationship Model — `repository/knowledge/RELATIONSHIP_MODEL.md` (Not yet approved) → Future Reference: Product Knowledge Graph — `repository/knowledge/PRODUCT_KNOWLEDGE_GRAPH.md` (Not yet approved) + Future Reference: SEO Knowledge Graph — `repository/knowledge/SEO_KNOWLEDGE_GRAPH.md` (Not yet approved) + Future Reference: CRM Knowledge Graph — `repository/knowledge/CRM_KNOWLEDGE_GRAPH.md` (Not yet approved) → Future Reference: AI Knowledge Readiness — `repository/knowledge/AI_KNOWLEDGE_READINESS.md` (Not yet approved) + Future Reference: Knowledge Governance — `repository/knowledge/KNOWLEDGE_GOVERNANCE.md` (Not yet approved) → Future Reference: Sprint 06A Audit — `docs/AUDIT_REPORT_SPRINT06A.md` (Not yet approved)

This path defines platform-independent semantic contracts only. Source domains retain authority; no graph runtime, index, database, CRM, recommendation, Product Finder, search, AI feature, WordPress object, or product is created.

### Sprint 07A Enterprise Business Operating System Path

[Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) + [Business Rules](03_BUSINESS_RULES.md) + [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md) + [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md) + [Platform Manifest](../repository/platform/PLATFORM_MANIFEST.md) + Future Reference: Knowledge Manifest — `repository/knowledge/KNOWLEDGE_MANIFEST.md` (Not yet approved) → Future Reference: Business Manifest — `repository/business/BUSINESS_MANIFEST.md` (Not yet approved) + Future Reference: Business Entity Model — `repository/business/BUSINESS_ENTITY_MODEL.md` (Not yet approved) → Future Reference: Customer Lifecycle — `repository/business/CUSTOMER_LIFECYCLE.md` (Not yet approved) + Future Reference: Inquiry Engine — `repository/business/INQUIRY_ENGINE.md` (Not yet approved) + Future Reference: Sales Pipeline — `repository/business/SALES_PIPELINE.md` (Not yet approved) → Future Reference: Representative Model — `repository/business/REPRESENTATIVE_MODEL.md` (Not yet approved) + Future Reference: Commission Engine — `repository/business/COMMISSION_ENGINE.md` (Not yet approved) + Future Reference: Project Lifecycle — `repository/business/PROJECT_LIFECYCLE.md` (Not yet approved) + Future Reference: Supplier Model — `repository/business/SUPPLIER_MODEL.md` (Not yet approved) + Future Reference: Service Model — `repository/business/SERVICE_MODEL.md` (Not yet approved) → Future Reference: Business Governance — `repository/business/BUSINESS_GOVERNANCE.md` (Not yet approved) → Future Reference: Sprint 07A Audit — `docs/AUDIT_REPORT_SPRINT07A.md` (Not yet approved)

This path is Business First, Platform Second, Runtime Last. All DEBOS models remain Review/TBD; no CRM/WooCommerce/WordPress/database/API/runtime/AI implementation or business record is created.

### Sprint 08A Enterprise Product and Knowledge Platform Blueprint Path

[Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) + [Product Data Model](19_PRODUCT_DATA_MODEL.md) + [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md) + [Platform Manifest](../repository/platform/PLATFORM_MANIFEST.md) + [Product Engine](../repository/engine/product/PRODUCT_ENGINE.md) + Future Reference: Knowledge Manifest — `repository/knowledge/KNOWLEDGE_MANIFEST.md` (Not yet approved) + Future Reference: Business Manifest — `repository/business/BUSINESS_MANIFEST.md` (Not yet approved) + [WordPress Blueprint](35_WORDPRESS_BLUEPRINT.md) → Future Reference: Enterprise Product and Knowledge Platform Manifest — `repository/enterprise-platform/01_PLATFORM_MANIFEST.md` (Not yet approved) → Future Reference: Product Repository Architecture — `repository/enterprise-platform/02_PRODUCT_REPOSITORY_ARCHITECTURE.md` (Not yet approved) + Future Reference: Knowledge Repository Architecture — `repository/enterprise-platform/03_KNOWLEDGE_REPOSITORY_ARCHITECTURE.md` (Not yet approved) → Future Reference: Product Configurator Engine — `repository/enterprise-platform/04_PRODUCT_CONFIGURATOR_ENGINE.md` (Not yet approved) + Future Reference: Product Experience Engine — `repository/enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md` (Not yet approved) + Future Reference: Guided Selection Engine — `repository/enterprise-platform/06_GUIDED_SELECTION_ENGINE.md` (Not yet approved) + Future Reference: Assembly Engine — `repository/enterprise-platform/07_ASSEMBLY_ENGINE.md` (Not yet approved) → Future Reference: Market Intelligence Repository — `repository/enterprise-platform/08_MARKET_INTELLIGENCE_REPOSITORY.md` (Not yet approved) + Future Reference: Customer Knowledge Repository — `repository/enterprise-platform/09_CUSTOMER_KNOWLEDGE_REPOSITORY.md` (Not yet approved) + Future Reference: Decision Rules Engine — `repository/enterprise-platform/10_DECISION_RULES_ENGINE.md` (Not yet approved) + Future Reference: Single Source of Truth Rules — `repository/enterprise-platform/11_SINGLE_SOURCE_OF_TRUTH_RULES.md` (Not yet approved) → Future Reference: WordPress and WooCommerce Mapping — `repository/enterprise-platform/12_WORDPRESS_WOOCOMMERCE_MAPPING.md` (Not yet approved) + Future Reference: Sprint 08A Implementation Roadmap — `repository/enterprise-platform/13_IMPLEMENTATION_ROADMAP.md` (Not yet approved) → Future Reference: Sprint 08A Audit — `docs/AUDIT_REPORT_SPRINT08A.md` (Not yet approved)

This path is Blueprint only. GO means Founder review only; WordPress, WooCommerce, plugins, products, public pricing, theme changes, AI features, and runtime implementation remain `NO-GO`.

### Sprint 08B Visual Experience System Path

[Design Manifest](../repository/design/DESIGN_MANIFEST.md) + [Brand Language](../repository/design/BRAND_LANGUAGE.md) + [Motion System](../repository/design/MOTION_SYSTEM.md) + [ReactBits Inspiration Mapping](../repository/design/REACTBITS_INSPIRATION_MAPPING.md) + [Component Pattern Library](../repository/design/COMPONENT_PATTERN_LIBRARY.md) + [Performance Rules](../repository/design/PERFORMANCE_RULES.md) + [Accessibility Rules](../repository/design/ACCESSIBILITY_RULES.md) + Future Reference: Sprint 08A Platform Blueprint — `repository/enterprise-platform/01_PLATFORM_MANIFEST.md` (Not yet approved) + Future Reference: WordPress and WooCommerce Mapping — `repository/enterprise-platform/12_WORDPRESS_WOOCOMMERCE_MAPPING.md` (Not yet approved) → Future Reference: Damavand Visual Experience System — `repository/design/DAMAVAND_VISUAL_EXPERIENCE_SYSTEM.md` (Not yet approved) → Future Reference: Elementor Component Guide — `repository/design/ELEMENTOR_COMPONENT_GUIDE.md` (Not yet approved) + Future Reference: ReactBits Inspired UI Rules — `repository/design/REACTBITS_INSPIRED_UI_RULES.md` (Not yet approved) → Future Reference: Sprint 08B Audit — `docs/AUDIT_REPORT_SPRINT08B.md` (Not yet approved)

This path is visual implementation planning only. It is `GO` for Founder visual review and Sprint 08C planning. WordPress implementation, runtime CSS/JavaScript, dependency installation, and publishing remain `NO-GO`.

### Sprint 08B.5 Design Language Foundation Path

[Design Manifest](../repository/design/DESIGN_MANIFEST.md) + Future Reference: Damavand Visual Experience System — `repository/design/DAMAVAND_VISUAL_EXPERIENCE_SYSTEM.md` (Not yet approved) + Future Reference: Elementor Component Guide — `repository/design/ELEMENTOR_COMPONENT_GUIDE.md` (Not yet approved) + Future Reference: ReactBits Inspired UI Rules — `repository/design/REACTBITS_INSPIRED_UI_RULES.md` (Not yet approved) → Future Reference: Enterprise Design Language — `repository/design/01_DESIGN_LANGUAGE.md` (Not yet approved) → Future Reference: Design Tokens — `repository/design/02_DESIGN_TOKENS.md` (Not yet approved) + Future Reference: Component State System — `repository/design/03_COMPONENT_STATE_SYSTEM.md` (Not yet approved) + Future Reference: Visual Hierarchy — `repository/design/04_VISUAL_HIERARCHY.md` (Not yet approved) → Future Reference: Spacing System — `repository/design/05_SPACING_SYSTEM.md` (Not yet approved) + Future Reference: Grid System — `repository/design/06_GRID_SYSTEM.md` (Not yet approved) + Future Reference: Typography System — `repository/design/07_TYPOGRAPHY_SYSTEM.md` (Not yet approved) + Future Reference: Color System — `repository/design/08_COLOR_SYSTEM.md` (Not yet approved) → Future Reference: Iconography System — `repository/design/09_ICONOGRAPHY_SYSTEM.md` (Not yet approved) + Future Reference: Image System — `repository/design/10_IMAGE_SYSTEM.md` (Not yet approved) + Future Reference: Enterprise Motion System — `repository/design/11_MOTION_SYSTEM.md` (Not yet approved) + Future Reference: Component Naming — `repository/design/12_COMPONENT_NAMING.md` (Not yet approved) + Future Reference: Admin Experience — `repository/design/13_ADMIN_EXPERIENCE.md` (Not yet approved) + Future Reference: Design Versioning — `repository/design/14_VERSIONING.md` (Not yet approved) → Future Reference: Sprint 08B.5 Audit — `docs/AUDIT_REPORT_SPRINT08B5.md` (Not yet approved)

This path is Design Language governance only. It is `GO` for Founder Design Review. Runtime, publishing, WordPress implementation, CSS generation, JavaScript generation, dependency installation, Elementor templates, and Blocksy settings remain `NO-GO`.

### Sprint 08B.6 Enterprise Content Language Path

[Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md) + [Content Types](32_CONTENT_TYPES.md) + [SEO Entity Model](34_SEO_ENTITY_MODEL.md) + Future Reference: Knowledge Manifest — `repository/knowledge/KNOWLEDGE_MANIFEST.md` (Not yet approved) + Future Reference: Enterprise Design Language — `repository/design/01_DESIGN_LANGUAGE.md` (Not yet approved) → Future Reference: Enterprise Content Language — `repository/content/01_CONTENT_LANGUAGE.md` (Not yet approved) → Future Reference: Product Content Standard — `repository/content/02_PRODUCT_CONTENT_STANDARD.md` (Not yet approved) + Future Reference: Category Content Standard — `repository/content/03_CATEGORY_CONTENT_STANDARD.md` (Not yet approved) + Future Reference: Knowledge Article Standard — `repository/content/04_KNOWLEDGE_ARTICLE_STANDARD.md` (Not yet approved) + Future Reference: FAQ Standard — `repository/content/05_FAQ_STANDARD.md` (Not yet approved) + Future Reference: Brand Content Standard — `repository/content/06_BRAND_CONTENT_STANDARD.md` (Not yet approved) + Future Reference: Installation Guide Standard — `repository/content/07_INSTALLATION_GUIDE_STANDARD.md` (Not yet approved) → Future Reference: Material Knowledge Standard — `repository/content/08_MATERIAL_KNOWLEDGE_STANDARD.md` (Not yet approved) + Future Reference: Alloy Knowledge Standard — `repository/content/09_ALLOY_KNOWLEDGE_STANDARD.md` (Not yet approved) + Future Reference: Content Component Library — `repository/content/10_CONTENT_COMPONENT_LIBRARY.md` (Not yet approved) + Future Reference: Content Tone of Voice — `repository/content/11_CONTENT_TONE_OF_VOICE.md` (Not yet approved) + Future Reference: Content Semantic Entity Model — `repository/content/12_SEMANTIC_ENTITY_MODEL.md` (Not yet approved) + Future Reference: Content Reuse Rules — `repository/content/13_CONTENT_REUSE_RULES.md` (Not yet approved) + Future Reference: AI Content Governance — `repository/content/14_AI_CONTENT_GOVERNANCE.md` (Not yet approved) + Future Reference: Content Versioning — `repository/content/15_CONTENT_VERSIONING.md` (Not yet approved) → Future Reference: Sprint 08B.6 Audit — `docs/AUDIT_REPORT_SPRINT08B6.md` (Not yet approved)

This path is Content Language governance only. It is `GO` for Founder Content Review. WordPress implementation, publishing, runtime files, SEO implementation, product description generation, and AI generation remain `NO-GO`.

### Sprint 08C Enterprise WordPress Implementation Blueprint Path

[WordPress Blueprint](35_WORDPRESS_BLUEPRINT.md) + Future Reference: WordPress and WooCommerce Mapping — `repository/enterprise-platform/12_WORDPRESS_WOOCOMMERCE_MAPPING.md` (Not yet approved) + Future Reference: Product Repository Architecture — `repository/enterprise-platform/02_PRODUCT_REPOSITORY_ARCHITECTURE.md` (Not yet approved) + Future Reference: Enterprise Design Language — `repository/design/01_DESIGN_LANGUAGE.md` (Not yet approved) + Future Reference: Enterprise Content Language — `repository/content/01_CONTENT_LANGUAGE.md` (Not yet approved) + Future Reference: Knowledge Manifest — `repository/knowledge/KNOWLEDGE_MANIFEST.md` (Not yet approved) → Future Reference: Enterprise WordPress Implementation Architecture — `repository/wordpress/01_WORDPRESS_ARCHITECTURE.md` (Not yet approved) → Future Reference: WooCommerce Product Model Blueprint — `repository/wordpress/02_WOOCOMMERCE_PRODUCT_MODEL.md` (Not yet approved) + Future Reference: Attribute Strategy — `repository/wordpress/03_ATTRIBUTE_STRATEGY.md` (Not yet approved) + Future Reference: Taxonomy Strategy — `repository/wordpress/04_TAXONOMY_STRATEGY.md` (Not yet approved) + Future Reference: ACF and Custom Field Strategy — `repository/wordpress/05_ACF_STRATEGY.md` (Not yet approved) → Future Reference: Blocksy Implementation Architecture — `repository/wordpress/06_BLOCKSY_ARCHITECTURE.md` (Not yet approved) + Future Reference: Elementor Implementation Architecture — `repository/wordpress/07_ELEMENTOR_ARCHITECTURE.md` (Not yet approved) + Future Reference: Rank Math SEO Mapping Blueprint — `repository/wordpress/08_RANKMATH_MAPPING.md` (Not yet approved) → Future Reference: Admin Workflow — `repository/wordpress/09_ADMIN_WORKFLOW.md` (Not yet approved) + Future Reference: Media Library Architecture — `repository/wordpress/10_MEDIA_LIBRARY_ARCHITECTURE.md` (Not yet approved) + Future Reference: Product Import Strategy — `repository/wordpress/11_PRODUCT_IMPORT_STRATEGY.md` (Not yet approved) + Future Reference: Configuration Workflow — `repository/wordpress/12_CONFIGURATION_WORKFLOW.md` (Not yet approved) + Future Reference: Testing Strategy — `repository/wordpress/13_TESTING_STRATEGY.md` (Not yet approved) + Future Reference: Runtime Boundaries — `repository/wordpress/14_RUNTIME_BOUNDARIES.md` (Not yet approved) + Future Reference: Release Plan — `repository/wordpress/15_RELEASE_PLAN.md` (Not yet approved) → Future Reference: Sprint 08C Audit — `docs/AUDIT_REPORT_SPRINT08C.md` (Not yet approved)

This path is WordPress implementation blueprint only. It is `GO` for Founder Architecture Review. Runtime, publishing, live WordPress, product creation, plugin installation, PHP, CSS, JavaScript, import execution, and configuration remain `NO-GO`.

### Sprint 08D.1 WordPress Environment Verification Path

Future Reference: Runtime Boundaries — `repository/wordpress/14_RUNTIME_BOUNDARIES.md` (Not yet approved) + Future Reference: WordPress Implementation Release Plan — `repository/wordpress/15_RELEASE_PLAN.md` (Not yet approved) + [Sprint 04B-A Authenticated Audit](AUDIT_REPORT_SPRINT04B_AUTHENTICATED.md) + public read-only endpoint checks → Future Reference: WordPress Environment Inventory — `docs/WORDPRESS_ENVIRONMENT_INVENTORY.md` (Not yet approved) → Future Reference: WordPress Read-only Audit — `docs/WORDPRESS_READ_ONLY_AUDIT.md` (Not yet approved) + Future Reference: Plugin and Theme Compatibility Report — `docs/PLUGIN_THEME_COMPATIBILITY_REPORT.md` (Not yet approved) + Future Reference: Site Health Blockers — `docs/SITE_HEALTH_BLOCKERS.md` (Not yet approved) → Future Reference: Runtime Readiness Report — `docs/RUNTIME_READINESS_REPORT.md` (Not yet approved) → Future Reference: Sprint 08D.1 Audit — `docs/AUDIT_REPORT_SPRINT08D1.md` (Not yet approved)

This path is read-only verification only. It is `GO` for Founder review of evidence. Runtime, publishing, live WordPress mutation, cPanel/database/file changes, product creation, plugin changes, imports, settings changes, and remediation remain `NO-GO`.

### Sprint 08D.1R Runtime Blocker Remediation Planning Path

Future Reference: Sprint 08D.1 Audit — `docs/AUDIT_REPORT_SPRINT08D1.md` (Not yet approved) + Future Reference: Site Health Blockers — `docs/SITE_HEALTH_BLOCKERS.md` (Not yet approved) + Future Reference: Runtime Readiness Report — `docs/RUNTIME_READINESS_REPORT.md` (Not yet approved) + Future Reference: Runtime Boundaries — `repository/wordpress/14_RUNTIME_BOUNDARIES.md` (Not yet approved) → Future Reference: Runtime Blocker Remediation Plan — `docs/RUNTIME_BLOCKER_REMEDIATION_PLAN.md` (Not yet approved) → Future Reference: Remediation Sequence and Dependencies — `docs/REMEDIATION_SEQUENCE_AND_DEPENDENCIES.md` (Not yet approved) + Future Reference: Backup Restore Proof Checklist — `docs/BACKUP_RESTORE_PROOF_CHECKLIST.md` (Not yet approved) + Future Reference: Founder Runtime Approval Checklist — `docs/FOUNDER_RUNTIME_APPROVAL_CHECKLIST.md` (Not yet approved) → Future Reference: Sprint 08D.1R Audit — `docs/AUDIT_REPORT_SPRINT08D1R.md` (Not yet approved)

This path is remediation planning only. It is `GO` for Founder review of the plan. Runtime, publishing, product creation, plugin/theme changes, backup creation, restore execution, and WordPress modification remain `NO-GO`.

### Sprint 09A Product Foundation Asset Path

Future Reference: Product Repository Architecture — `repository/enterprise-platform/02_PRODUCT_REPOSITORY_ARCHITECTURE.md` (Not yet approved) + [Product Engine](../repository/engine/product/PRODUCT_ENGINE.md) + [Pipe Product Family](../repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md) + [Pipe Variation Matrix](../repository/data/products/pipes/PIPE_VARIATION_MATRIX.md) + [Pipe Attribute Model](../repository/data/attributes/PIPE_ATTRIBUTE_MODEL.md) + Future Reference: WordPress Product Import Strategy — `repository/wordpress/11_PRODUCT_IMPORT_STRATEGY.md` (Not yet approved) → Future Reference: Master Product Taxonomy v1 — `repository/implementation-assets/product-foundation/01_MASTER_PRODUCT_TAXONOMY_V1.yaml` (Not yet approved) + Future Reference: Global Attribute Library v1 — `repository/implementation-assets/product-foundation/02_GLOBAL_ATTRIBUTE_LIBRARY_V1.yaml` (Not yet approved) → Future Reference: Pipe Family Template v1 — `repository/implementation-assets/product-foundation/03_PIPE_FAMILY_TEMPLATE_V1.yaml` (Not yet approved) + Future Reference: Profile Family Template v1 — `repository/implementation-assets/product-foundation/04_PROFILE_FAMILY_TEMPLATE_V1.yaml` (Not yet approved) → Future Reference: Variant and SKU Rules v1 — `repository/implementation-assets/product-foundation/05_VARIANT_AND_SKU_RULES_V1.md` (Not yet approved) + Future Reference: Product Knowledge Mapping v1 — `repository/implementation-assets/product-foundation/06_PRODUCT_KNOWLEDGE_MAPPING_V1.yaml` (Not yet approved) + Future Reference: Founder Decision Register v1 — `repository/implementation-assets/product-foundation/07_FOUNDER_DECISION_REGISTER_V1.md` (Not yet approved) → Future Reference: Pipe/Profile WooCommerce Mapping v1 — `repository/implementation-assets/import-preparation/PIPE_PROFILE_WOOCOMMERCE_MAPPING_V1.csv` (Not yet approved) + Future Reference: Pipe/Profile Attribute Seed v1 — `repository/implementation-assets/import-preparation/PIPE_PROFILE_ATTRIBUTE_SEED_V1.csv` (Not yet approved) + Future Reference: Pipe/Profile Validation Rules v1 — `repository/implementation-assets/import-preparation/PIPE_PROFILE_VALIDATION_RULES_V1.md` (Not yet approved) → Future Reference: Sprint 09A Audit — `docs/AUDIT_REPORT_SPRINT09A.md` (Not yet approved)

This path is Product Foundation review only. Pipe values are limited to current repository evidence. Profile values remain `STATUS: FOUNDER_INPUT_REQUIRED` where not approved. WordPress import, runtime changes, publishing, public pricing, stock, final SKUs, bulk SKU generation, and product creation remain `NO-GO`.

### Sprint 09B Product DNA System Path

Future Reference: Product Repository Architecture — `repository/enterprise-platform/02_PRODUCT_REPOSITORY_ARCHITECTURE.md` (Not yet approved) + Future Reference: Knowledge Repository Architecture — `repository/enterprise-platform/03_KNOWLEDGE_REPOSITORY_ARCHITECTURE.md` (Not yet approved) + Future Reference: Product Configurator Engine — `repository/enterprise-platform/04_PRODUCT_CONFIGURATOR_ENGINE.md` (Not yet approved) + Future Reference: Product Experience Engine — `repository/enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md` (Not yet approved) + Future Reference: WordPress and WooCommerce Mapping — `repository/enterprise-platform/12_WORDPRESS_WOOCOMMERCE_MAPPING.md` (Not yet approved) + Future Reference: Product Content Standard — `repository/content/02_PRODUCT_CONTENT_STANDARD.md` (Not yet approved) + Future Reference: Content Component Library — `repository/content/10_CONTENT_COMPONENT_LIBRARY.md` (Not yet approved) + Future Reference: Product Foundation Assets — `repository/implementation-assets/product-foundation/01_MASTER_PRODUCT_TAXONOMY_V1.yaml` (Not yet approved) → Future Reference: Master Product DNA — `repository/implementation-assets/product-dna/01_MASTER_PRODUCT_DNA.md` (Not yet approved) → Future Reference: Product Information Model — `repository/implementation-assets/product-dna/02_PRODUCT_INFORMATION_MODEL.yaml` (Not yet approved) + Future Reference: Product Component Library — `repository/implementation-assets/product-dna/03_PRODUCT_COMPONENT_LIBRARY.yaml` (Not yet approved) + Future Reference: Product Knowledge Block Library — `repository/implementation-assets/product-dna/04_PRODUCT_KNOWLEDGE_BLOCK_LIBRARY.yaml` (Not yet approved) → Future Reference: Product Page Assembly Engine — `repository/implementation-assets/product-dna/05_PRODUCT_PAGE_ASSEMBLY_ENGINE.yaml` (Not yet approved) + Future Reference: Product Configurator UI Model — `repository/implementation-assets/product-dna/06_PRODUCT_CONFIGURATOR_UI_MODEL.yaml` (Not yet approved) + Future Reference: Product Media Model — `repository/implementation-assets/product-dna/07_PRODUCT_MEDIA_MODEL.yaml` (Not yet approved) + Future Reference: Product SEO Model — `repository/implementation-assets/product-dna/08_PRODUCT_SEO_MODEL.yaml` (Not yet approved) + Future Reference: Product Schema Model — `repository/implementation-assets/product-dna/09_PRODUCT_SCHEMA_MODEL.yaml` (Not yet approved) + Future Reference: Product Relation Model — `repository/implementation-assets/product-dna/10_PRODUCT_RELATION_MODEL.yaml` (Not yet approved) → Future Reference: Product Lifecycle Model — `repository/implementation-assets/product-dna/11_PRODUCT_LIFECYCLE_MODEL.md` (Not yet approved) + Future Reference: Product Validation Rules — `repository/implementation-assets/product-dna/12_PRODUCT_VALIDATION_RULES.md` (Not yet approved) + Future Reference: Product Extensibility Model — `repository/implementation-assets/product-dna/13_PRODUCT_EXTENSIBILITY_MODEL.md` (Not yet approved) + Future Reference: Product Admin Model — `repository/implementation-assets/product-dna/14_PRODUCT_ADMIN_MODEL.md` (Not yet approved) → Future Reference: Product DNA Example Pipe — `repository/implementation-assets/product-dna/15_PRODUCT_DNA_EXAMPLE_PIPE.yaml` (Not yet approved) + Future Reference: Product DNA Example Profile — `repository/implementation-assets/product-dna/16_PRODUCT_DNA_EXAMPLE_PROFILE.yaml` (Not yet approved) → Future Reference: Sprint 09B Audit — `docs/AUDIT_REPORT_SPRINT09B.md` (Not yet approved)

This path is Product DNA review only. It defines reusable product structure and Pipe/Profile examples without product creation, import, runtime code, SEO/schema publishing, Elementor/Blocksy/WooCommerce configuration, public pricing, or content generation.

### Technical Path

[Technology Stack](05_TECH_STACK.md) → [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md) → [Development Workflow](08_DEVELOPMENT_WORKFLOW.md) → [Testing Strategy](13_TESTING_STRATEGY.md) → [Deployment](09_DEPLOYMENT.md)

### Assurance Path

[Documentation Quality Standard](16_QUALITY_STANDARD.md) → [Review Process](15_REVIEW_PROCESS.md) → [Enterprise Quality Standard](../quality/QUALITY_STANDARD.md) → [Repository Health](REPOSITORY_HEALTH.md) → [Batch 02C Audit](AUDIT_REPORT_BATCH02C.md)

### Repository Intelligence Path

[AI Collaboration Standard](AI_COLLABORATION.md) → [Repository Metadata Standard](REPOSITORY_METADATA.md) → [Traceability Matrix](TRACEABILITY_MATRIX.md) → [Reading Order](READING_ORDER.md) → [Knowledge Graph](KNOWLEDGE_GRAPH.md) → [Repository Health](REPOSITORY_HEALTH.md) → [Batch 02C Audit](AUDIT_REPORT_BATCH02C.md)

### Governance Completion Path

[Project Constitution](01_PROJECT_CONSTITUTION.md#governance-rule-inheritance) → [Decision Classification](10_DECISION_LOG.md#decision-classification-framework) → [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md) → [Relationship Metadata](REPOSITORY_METADATA.md#relationship-metadata-model) → [Knowledge Graph](KNOWLEDGE_GRAPH.md#relationship-types) → [Conflict Resolution](01_PROJECT_CONSTITUTION.md#conflict-resolution-framework) → [Validation Checklist](16_QUALITY_STANDARD.md#controlled-document-validation-checklist)

### Git Governance Path

[Repository Standards](07_REPOSITORY_GUIDE.md) → [Git Governance](GIT_GOVERNANCE.md) → [Changelog Policy](14_CHANGELOG_POLICY.md) → [Repository Health](REPOSITORY_HEALTH.md) → [Batch 03 Audit](AUDIT_REPORT_BATCH03.md)

### Role-Based Reading Paths

Founder, New Developer, AI, Auditor, SEO, WordPress Engineer, and Content Team paths are maintained in [Repository Reading Order](READING_ORDER.md).

## Architecture Paths

- Architecture authority: [DS-002 Enterprise Architecture](02_ARCHITECTURE.md)
- Architecture supporting material: [`docs/architecture/`](architecture/README.md)
- Architecture decisions: [`docs/adr/`](adr/README.md)
- Architecture decision discovery: [Decision Log](10_DECISION_LOG.md)
- Architecture validation: [Review Process](15_REVIEW_PROCESS.md)
- WordPress platform architecture: [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md)
- WordPress implementation-readiness Blueprint: [Enterprise WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- Blueprint responsibility boundary: [Enterprise Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md)
- Repository baseline: [Repository Baseline v1.0](BASELINE_v1.0.md)
- Implementation gate: [Implementation Readiness Assessment](IMPLEMENTATION_READINESS.md)
- Repository bootstrap rules: [Repository Implementation Rules](../repository/IMPLEMENTATION_RULES.md)
- Environment evidence: [Sprint 01B Environment Report](../repository/config/ENVIRONMENT_REPORT.md)
- Environment-validation gate: [Sprint 01C Hosting Validation Checklist](../repository/config/HOSTING_VALIDATION_CHECKLIST.md)
- Conditional component sequence: [Sprint 01C Plugin Installation Sequence](../repository/config/PLUGIN_INSTALLATION_SEQUENCE.md)
- Recovery gate: [Sprint 01C Rollback Plan](../repository/config/ROLLBACK_PLAN.md)
- Remote-access proposal: [Remote Access and Iran Execution Constraints Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md)
- Access-control gate: [Sprint 01D Deployment Access Policy](../repository/config/DEPLOYMENT_ACCESS_POLICY.md)
- Iran execution risks: [Sprint 01D Iran Execution Risk Register](../repository/config/IRAN_EXECUTION_RISK_REGISTER.md)
- Product Data Engine family source: [Stainless Steel Pipe Product Family](../repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md)
- Product Data Engine validation: [Product Data Validation Rules](../repository/data/validation/PRODUCT_DATA_VALIDATION_RULES.md)
- Product Data Engine import staging: [WooCommerce Pipe Import Template](../repository/data/imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv)
- Pipe mapping gate: [Stainless Steel Pipe Import Precheck](../repository/data/validation/PIPE_IMPORT_PRECHECK.md)
- Pipe classification source: [Pipe Taxonomy and Attribute Classification](../repository/data/taxonomies/PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md)
- Pipe governance gate: [Pipe Data Governance Checklist](../repository/data/validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md)
- Product generation source: [Enterprise Product Engine](../repository/engine/product/PRODUCT_ENGINE.md)
- Product generation procedure: [Product Engine Generation Guide](../repository/engine/product/ENGINE_GENERATION_GUIDE.md)
- Product generation validation: [Product Validation Template](../repository/engine/product/VALIDATION_TEMPLATE.md)
- Platform constitutional source: [Enterprise Platform Manifest](../repository/platform/PLATFORM_MANIFEST.md)
- Platform layer/runtime boundary: [Enterprise Platform Architecture](../repository/platform/PLATFORM_ARCHITECTURE.md)
- Platform engine registry: [Enterprise Engine Boundaries](../repository/platform/ENGINE_BOUNDARIES.md)
- Platform evolution gate: [Enterprise Platform Evolution](../repository/platform/PLATFORM_EVOLUTION.md)
- Infrastructure evidence source: [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md)
- REST diagnostic gate: [REST API Diagnostic](REST_API_DIAGNOSTIC.md)
- Connectivity evidence gate: [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md)
- Site Health action gate: [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md)
- Product Foundation taxonomy source: Future Reference: Master Product Taxonomy v1 — `repository/implementation-assets/product-foundation/01_MASTER_PRODUCT_TAXONOMY_V1.yaml` (Not yet approved)
- Product Foundation attribute source: Future Reference: Global Attribute Library v1 — `repository/implementation-assets/product-foundation/02_GLOBAL_ATTRIBUTE_LIBRARY_V1.yaml` (Not yet approved)
- Product Foundation validation gate: Future Reference: Pipe/Profile Validation Rules v1 — `repository/implementation-assets/import-preparation/PIPE_PROFILE_VALIDATION_RULES_V1.md` (Not yet approved)
- Product DNA source: Future Reference: Master Product DNA — `repository/implementation-assets/product-dna/01_MASTER_PRODUCT_DNA.md` (Not yet approved)
- Product DNA validation gate: Future Reference: Product Validation Rules — `repository/implementation-assets/product-dna/12_PRODUCT_VALIDATION_RULES.md` (Not yet approved)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Project Baseline](PROJECT_BASELINE.md)
- [Repository Relationship Map](REPOSITORY_RELATIONSHIP_MAP.md)
- [Glossary](11_GLOSSARY.md)
- [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md)
- [Repository Reading Order](READING_ORDER.md)
- [Repository Knowledge Graph](KNOWLEDGE_GRAPH.md)
- [Repository Health](REPOSITORY_HEALTH.md)
- [Git Governance](GIT_GOVERNANCE.md)
- [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md)
- [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md)
- [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md)
- [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)
- [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md)
- [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- Future Reference: GIT-02S Audit — `docs/AUDIT_REPORT_GIT02S.md` (Not yet approved)
- [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md)
- [Enterprise Site Structure](25_SITE_STRUCTURE.md)
- [Enterprise URL Architecture](26_URL_ARCHITECTURE.md)
- [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md)
- [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md)
- [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md)
- [Enterprise Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- [Schema.org Semantic Strategy](31_SCHEMA_ORG_STRATEGY.md)
- [Enterprise Content Types](32_CONTENT_TYPES.md)
- [Enterprise Media Strategy](33_MEDIA_STRATEGY.md)
- [Enterprise SEO Entity Model](34_SEO_ENTITY_MODEL.md)
- [Enterprise WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- [Enterprise Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md)
- [Batch 08 Audit](AUDIT_REPORT_BATCH08.md)
- [Repository Baseline v1.0](BASELINE_v1.0.md)
- [Implementation Readiness Assessment](IMPLEMENTATION_READINESS.md)
- [Repository Freeze v1.0 Audit](AUDIT_REPORT_FREEZE_v1.0.md)
- [Repository Implementation Rules](../repository/IMPLEMENTATION_RULES.md)
- [Pre-Implementation Checklist](../repository/PRE_IMPLEMENTATION_CHECKLIST.md)
- [Sprint 01A Audit](AUDIT_REPORT_SPRINT01A.md)
- [Sprint 01B Environment Report](../repository/config/ENVIRONMENT_REPORT.md)
- [Sprint 01B WordPress Baseline](../repository/config/WORDPRESS_BASELINE.md)
- [Sprint 01B Audit](AUDIT_REPORT_SPRINT01B.md)
- [Sprint 01C Hosting Validation Checklist](../repository/config/HOSTING_VALIDATION_CHECKLIST.md)
- [Sprint 01C WordPress Installation Checklist](../repository/config/WORDPRESS_INSTALLATION_CHECKLIST.md)
- [Sprint 01C Plugin Installation Sequence](../repository/config/PLUGIN_INSTALLATION_SEQUENCE.md)
- [Sprint 01C Post-Install Validation](../repository/config/POST_INSTALL_VALIDATION.md)
- [Sprint 01C Rollback Plan](../repository/config/ROLLBACK_PLAN.md)
- [Sprint 01C Audit](AUDIT_REPORT_SPRINT01C.md)
- [Remote Access and Iran Execution Constraints Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md)
- [Sprint 01D SSH Access Checklist](../repository/config/SSH_ACCESS_CHECKLIST.md)
- [Sprint 01D Deployment Access Policy](../repository/config/DEPLOYMENT_ACCESS_POLICY.md)
- [Sprint 01D Iran Execution Risk Register](../repository/config/IRAN_EXECUTION_RISK_REGISTER.md)
- [Sprint 01D Audit](AUDIT_REPORT_SPRINT01D.md)
- [Stainless Steel Pipe Product Family](../repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md)
- [Product Attribute Dictionary](../repository/data/attributes/ATTRIBUTE_DICTIONARY.md)
- [Stainless Steel Pipe Variation Matrix](../repository/data/products/pipes/PIPE_VARIATION_MATRIX.md)
- [WooCommerce Pipe Import Template](../repository/data/imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv)
- [Stainless Steel Pipe SEO Entity Model](../repository/data/seo/PIPE_SEO_ENTITY_MODEL.md)
- [Product Data Validation Rules](../repository/data/validation/PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03A Audit](AUDIT_REPORT_SPRINT03A.md)
- [Stainless Steel Pipe WooCommerce Mapping](../repository/data/products/pipes/PIPE_WOOCOMMERCE_MAPPING.md)
- [Stainless Steel Pipe Import Mapping](../repository/data/imports/woocommerce/PIPE_IMPORT_MAPPING.md)
- [Stainless Steel Pipe Import Precheck](../repository/data/validation/PIPE_IMPORT_PRECHECK.md)
- [Sprint 03B Audit](AUDIT_REPORT_SPRINT03B.md)
- [Pipe Taxonomy and Attribute Classification](../repository/data/taxonomies/PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md)
- [Pipe Category Model](../repository/data/taxonomies/PIPE_CATEGORY_MODEL.md)
- [Pipe Attribute Model](../repository/data/attributes/PIPE_ATTRIBUTE_MODEL.md)
- [Pipe Data Governance Checklist](../repository/data/validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md)
- [Sprint 03C Audit](AUDIT_REPORT_SPRINT03C.md)
- [Enterprise Product Engine](../repository/engine/product/PRODUCT_ENGINE.md)
- [Product Engine Rules](../repository/engine/product/ENGINE_RULES.md)
- [Product Engine Workflow](../repository/engine/product/ENGINE_WORKFLOW.md)
- [Product Engine Generation Guide](../repository/engine/product/ENGINE_GENERATION_GUIDE.md)
- [Product Family Template](../repository/engine/product/PRODUCT_FAMILY_TEMPLATE.md)
- [Product Attribute Template](../repository/engine/product/ATTRIBUTE_TEMPLATE.md)
- [Product Variation Template](../repository/engine/product/VARIATION_TEMPLATE.md)
- [Product Import Template](../repository/engine/product/IMPORT_TEMPLATE.md)
- [Product SEO Template](../repository/engine/product/SEO_TEMPLATE.md)
- [Product Validation Template](../repository/engine/product/VALIDATION_TEMPLATE.md)
- [Sprint 03D Audit](AUDIT_REPORT_SPRINT03D.md)
- [Enterprise Platform Manifest](../repository/platform/PLATFORM_MANIFEST.md)
- [Enterprise Platform Principles](../repository/platform/PLATFORM_PRINCIPLES.md)
- [Enterprise Platform Architecture](../repository/platform/PLATFORM_ARCHITECTURE.md)
- [Enterprise Engine Boundaries](../repository/platform/ENGINE_BOUNDARIES.md)
- [Enterprise Platform Lifecycle](../repository/platform/PLATFORM_LIFECYCLE.md)
- [Enterprise Platform Governance](../repository/platform/PLATFORM_GOVERNANCE.md)
- [Enterprise Platform Directory Standard](../repository/platform/PLATFORM_DIRECTORY_STANDARD.md)
- [Enterprise Platform Versioning](../repository/platform/PLATFORM_VERSIONING.md)
- [Enterprise Platform Evolution](../repository/platform/PLATFORM_EVOLUTION.md)
- [Sprint 03E Audit](AUDIT_REPORT_SPRINT03E.md)
- [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md)
- [REST API Diagnostic](REST_API_DIAGNOSTIC.md)
- [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md)
- [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md)
- [Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md)
- [Sprint 04B Audit](AUDIT_REPORT_SPRINT04B.md)
- [Sprint 04B Authenticated Audit](AUDIT_REPORT_SPRINT04B_AUTHENTICATED.md)
- [Master Remediation Roadmap](MASTER_REMEDIATION_ROADMAP.md)
- [Implementation Sequence](IMPLEMENTATION_SEQUENCE.md)
- [Execution Gates](EXECUTION_GATES.md)
- [Sprint 04C Audit](AUDIT_REPORT_SPRINT04C.md)
- [Design Manifest](../repository/design/DESIGN_MANIFEST.md)
- [Brand Language](../repository/design/BRAND_LANGUAGE.md)
- [Motion System](../repository/design/MOTION_SYSTEM.md)
- [ReactBits Inspiration Mapping](../repository/design/REACTBITS_INSPIRATION_MAPPING.md)
- [Component Pattern Library](../repository/design/COMPONENT_PATTERN_LIBRARY.md)
- [Animation Library](../repository/design/ANIMATION_LIBRARY.md)
- [Design Performance Rules](../repository/design/PERFORMANCE_RULES.md)
- [Design Accessibility Rules](../repository/design/ACCESSIBILITY_RULES.md)
- [Design Decision Records](../repository/design/DESIGN_DECISION_RECORDS.md)
- [Sprint 05A Audit](AUDIT_REPORT_SPRINT05A.md)
- Future Reference: Knowledge Manifest — `repository/knowledge/KNOWLEDGE_MANIFEST.md` (Not yet approved)
- Future Reference: Knowledge Entity Model — `repository/knowledge/ENTITY_MODEL.md` (Not yet approved)
- Future Reference: Knowledge Ontology Model — `repository/knowledge/ONTOLOGY_MODEL.md` (Not yet approved)
- Future Reference: Knowledge Relationship Model — `repository/knowledge/RELATIONSHIP_MODEL.md` (Not yet approved)
- Future Reference: Product Knowledge Graph — `repository/knowledge/PRODUCT_KNOWLEDGE_GRAPH.md` (Not yet approved)
- Future Reference: SEO Knowledge Graph — `repository/knowledge/SEO_KNOWLEDGE_GRAPH.md` (Not yet approved)
- Future Reference: CRM Knowledge Graph — `repository/knowledge/CRM_KNOWLEDGE_GRAPH.md` (Not yet approved)
- Future Reference: AI Knowledge Readiness — `repository/knowledge/AI_KNOWLEDGE_READINESS.md` (Not yet approved)
- Future Reference: Knowledge Governance — `repository/knowledge/KNOWLEDGE_GOVERNANCE.md` (Not yet approved)
- Future Reference: Sprint 06A Audit — `docs/AUDIT_REPORT_SPRINT06A.md` (Not yet approved)
- Future Reference: Business Manifest — `repository/business/BUSINESS_MANIFEST.md` (Not yet approved)
- Future Reference: Business Entity Model — `repository/business/BUSINESS_ENTITY_MODEL.md` (Not yet approved)
- Future Reference: Customer Lifecycle — `repository/business/CUSTOMER_LIFECYCLE.md` (Not yet approved)
- Future Reference: Inquiry Engine — `repository/business/INQUIRY_ENGINE.md` (Not yet approved)
- Future Reference: Sales Pipeline — `repository/business/SALES_PIPELINE.md` (Not yet approved)
- Future Reference: Representative Model — `repository/business/REPRESENTATIVE_MODEL.md` (Not yet approved)
- Future Reference: Commission Engine — `repository/business/COMMISSION_ENGINE.md` (Not yet approved)
- Future Reference: Project Lifecycle — `repository/business/PROJECT_LIFECYCLE.md` (Not yet approved)
- Future Reference: Supplier Model — `repository/business/SUPPLIER_MODEL.md` (Not yet approved)
- Future Reference: Service Model — `repository/business/SERVICE_MODEL.md` (Not yet approved)
- Future Reference: Business Governance — `repository/business/BUSINESS_GOVERNANCE.md` (Not yet approved)
- Future Reference: Sprint 07A Audit — `docs/AUDIT_REPORT_SPRINT07A.md` (Not yet approved)
- Future Reference: Enterprise Product and Knowledge Platform Manifest — `repository/enterprise-platform/01_PLATFORM_MANIFEST.md` (Not yet approved)
- Future Reference: Product Repository Architecture — `repository/enterprise-platform/02_PRODUCT_REPOSITORY_ARCHITECTURE.md` (Not yet approved)
- Future Reference: Knowledge Repository Architecture — `repository/enterprise-platform/03_KNOWLEDGE_REPOSITORY_ARCHITECTURE.md` (Not yet approved)
- Future Reference: Product Configurator Engine — `repository/enterprise-platform/04_PRODUCT_CONFIGURATOR_ENGINE.md` (Not yet approved)
- Future Reference: Product Experience Engine — `repository/enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md` (Not yet approved)
- Future Reference: Guided Selection Engine — `repository/enterprise-platform/06_GUIDED_SELECTION_ENGINE.md` (Not yet approved)
- Future Reference: Assembly Engine — `repository/enterprise-platform/07_ASSEMBLY_ENGINE.md` (Not yet approved)
- Future Reference: Market Intelligence Repository — `repository/enterprise-platform/08_MARKET_INTELLIGENCE_REPOSITORY.md` (Not yet approved)
- Future Reference: Customer Knowledge Repository — `repository/enterprise-platform/09_CUSTOMER_KNOWLEDGE_REPOSITORY.md` (Not yet approved)
- Future Reference: Decision Rules Engine — `repository/enterprise-platform/10_DECISION_RULES_ENGINE.md` (Not yet approved)
- Future Reference: Single Source of Truth Rules — `repository/enterprise-platform/11_SINGLE_SOURCE_OF_TRUTH_RULES.md` (Not yet approved)
- Future Reference: WordPress and WooCommerce Mapping — `repository/enterprise-platform/12_WORDPRESS_WOOCOMMERCE_MAPPING.md` (Not yet approved)
- Future Reference: Sprint 08A Implementation Roadmap — `repository/enterprise-platform/13_IMPLEMENTATION_ROADMAP.md` (Not yet approved)
- Future Reference: Sprint 08A Audit — `docs/AUDIT_REPORT_SPRINT08A.md` (Not yet approved)
- Future Reference: Damavand Visual Experience System — `repository/design/DAMAVAND_VISUAL_EXPERIENCE_SYSTEM.md` (Not yet approved)
- Future Reference: Elementor Component Guide — `repository/design/ELEMENTOR_COMPONENT_GUIDE.md` (Not yet approved)
- Future Reference: ReactBits Inspired UI Rules — `repository/design/REACTBITS_INSPIRED_UI_RULES.md` (Not yet approved)
- Future Reference: Sprint 08B Audit — `docs/AUDIT_REPORT_SPRINT08B.md` (Not yet approved)
- Future Reference: Enterprise Design Language — `repository/design/01_DESIGN_LANGUAGE.md` (Not yet approved)
- Future Reference: Design Tokens — `repository/design/02_DESIGN_TOKENS.md` (Not yet approved)
- Future Reference: Component State System — `repository/design/03_COMPONENT_STATE_SYSTEM.md` (Not yet approved)
- Future Reference: Visual Hierarchy — `repository/design/04_VISUAL_HIERARCHY.md` (Not yet approved)
- Future Reference: Spacing System — `repository/design/05_SPACING_SYSTEM.md` (Not yet approved)
- Future Reference: Grid System — `repository/design/06_GRID_SYSTEM.md` (Not yet approved)
- Future Reference: Typography System — `repository/design/07_TYPOGRAPHY_SYSTEM.md` (Not yet approved)
- Future Reference: Color System — `repository/design/08_COLOR_SYSTEM.md` (Not yet approved)
- Future Reference: Iconography System — `repository/design/09_ICONOGRAPHY_SYSTEM.md` (Not yet approved)
- Future Reference: Image System — `repository/design/10_IMAGE_SYSTEM.md` (Not yet approved)
- Future Reference: Enterprise Motion System — `repository/design/11_MOTION_SYSTEM.md` (Not yet approved)
- Future Reference: Component Naming — `repository/design/12_COMPONENT_NAMING.md` (Not yet approved)
- Future Reference: Admin Experience — `repository/design/13_ADMIN_EXPERIENCE.md` (Not yet approved)
- Future Reference: Design Versioning — `repository/design/14_VERSIONING.md` (Not yet approved)
- Future Reference: Sprint 08B.5 Audit — `docs/AUDIT_REPORT_SPRINT08B5.md` (Not yet approved)
- Future Reference: Enterprise Content Language — `repository/content/01_CONTENT_LANGUAGE.md` (Not yet approved)
- Future Reference: Product Content Standard — `repository/content/02_PRODUCT_CONTENT_STANDARD.md` (Not yet approved)
- Future Reference: Category Content Standard — `repository/content/03_CATEGORY_CONTENT_STANDARD.md` (Not yet approved)
- Future Reference: Knowledge Article Standard — `repository/content/04_KNOWLEDGE_ARTICLE_STANDARD.md` (Not yet approved)
- Future Reference: FAQ Standard — `repository/content/05_FAQ_STANDARD.md` (Not yet approved)
- Future Reference: Brand Content Standard — `repository/content/06_BRAND_CONTENT_STANDARD.md` (Not yet approved)
- Future Reference: Installation Guide Standard — `repository/content/07_INSTALLATION_GUIDE_STANDARD.md` (Not yet approved)
- Future Reference: Material Knowledge Standard — `repository/content/08_MATERIAL_KNOWLEDGE_STANDARD.md` (Not yet approved)
- Future Reference: Alloy Knowledge Standard — `repository/content/09_ALLOY_KNOWLEDGE_STANDARD.md` (Not yet approved)
- Future Reference: Content Component Library — `repository/content/10_CONTENT_COMPONENT_LIBRARY.md` (Not yet approved)
- Future Reference: Content Tone of Voice — `repository/content/11_CONTENT_TONE_OF_VOICE.md` (Not yet approved)
- Future Reference: Content Semantic Entity Model — `repository/content/12_SEMANTIC_ENTITY_MODEL.md` (Not yet approved)
- Future Reference: Content Reuse Rules — `repository/content/13_CONTENT_REUSE_RULES.md` (Not yet approved)
- Future Reference: AI Content Governance — `repository/content/14_AI_CONTENT_GOVERNANCE.md` (Not yet approved)
- Future Reference: Content Versioning — `repository/content/15_CONTENT_VERSIONING.md` (Not yet approved)
- Future Reference: Sprint 08B.6 Audit — `docs/AUDIT_REPORT_SPRINT08B6.md` (Not yet approved)
- Future Reference: Enterprise WordPress Implementation Architecture — `repository/wordpress/01_WORDPRESS_ARCHITECTURE.md` (Not yet approved)
- Future Reference: WooCommerce Product Model Blueprint — `repository/wordpress/02_WOOCOMMERCE_PRODUCT_MODEL.md` (Not yet approved)
- Future Reference: Attribute Strategy — `repository/wordpress/03_ATTRIBUTE_STRATEGY.md` (Not yet approved)
- Future Reference: Taxonomy Strategy — `repository/wordpress/04_TAXONOMY_STRATEGY.md` (Not yet approved)
- Future Reference: ACF and Custom Field Strategy — `repository/wordpress/05_ACF_STRATEGY.md` (Not yet approved)
- Future Reference: Blocksy Implementation Architecture — `repository/wordpress/06_BLOCKSY_ARCHITECTURE.md` (Not yet approved)
- Future Reference: Elementor Implementation Architecture — `repository/wordpress/07_ELEMENTOR_ARCHITECTURE.md` (Not yet approved)
- Future Reference: Rank Math SEO Mapping Blueprint — `repository/wordpress/08_RANKMATH_MAPPING.md` (Not yet approved)
- Future Reference: WordPress Admin Workflow Blueprint — `repository/wordpress/09_ADMIN_WORKFLOW.md` (Not yet approved)
- Future Reference: Media Library Architecture — `repository/wordpress/10_MEDIA_LIBRARY_ARCHITECTURE.md` (Not yet approved)
- Future Reference: Product Import Strategy — `repository/wordpress/11_PRODUCT_IMPORT_STRATEGY.md` (Not yet approved)
- Future Reference: Configuration Workflow — `repository/wordpress/12_CONFIGURATION_WORKFLOW.md` (Not yet approved)
- Future Reference: WordPress Implementation Testing Strategy — `repository/wordpress/13_TESTING_STRATEGY.md` (Not yet approved)
- Future Reference: Runtime Boundaries — `repository/wordpress/14_RUNTIME_BOUNDARIES.md` (Not yet approved)
- Future Reference: WordPress Implementation Release Plan — `repository/wordpress/15_RELEASE_PLAN.md` (Not yet approved)
- Future Reference: Sprint 08C Audit — `docs/AUDIT_REPORT_SPRINT08C.md` (Not yet approved)
- Future Reference: WordPress Environment Inventory — `docs/WORDPRESS_ENVIRONMENT_INVENTORY.md` (Not yet approved)
- Future Reference: WordPress Read-only Audit — `docs/WORDPRESS_READ_ONLY_AUDIT.md` (Not yet approved)
- Future Reference: Plugin and Theme Compatibility Report — `docs/PLUGIN_THEME_COMPATIBILITY_REPORT.md` (Not yet approved)
- Future Reference: Site Health Blockers — `docs/SITE_HEALTH_BLOCKERS.md` (Not yet approved)
- Future Reference: Runtime Readiness Report — `docs/RUNTIME_READINESS_REPORT.md` (Not yet approved)
- Future Reference: Sprint 08D.1 Audit — `docs/AUDIT_REPORT_SPRINT08D1.md` (Not yet approved)
- Future Reference: Runtime Blocker Remediation Plan — `docs/RUNTIME_BLOCKER_REMEDIATION_PLAN.md` (Not yet approved)
- Future Reference: Remediation Sequence and Dependencies — `docs/REMEDIATION_SEQUENCE_AND_DEPENDENCIES.md` (Not yet approved)
- Future Reference: Backup Restore Proof Checklist — `docs/BACKUP_RESTORE_PROOF_CHECKLIST.md` (Not yet approved)
- Future Reference: Founder Runtime Approval Checklist — `docs/FOUNDER_RUNTIME_APPROVAL_CHECKLIST.md` (Not yet approved)
- Future Reference: Sprint 08D.1R Audit — `docs/AUDIT_REPORT_SPRINT08D1R.md` (Not yet approved)
- Future Reference: Master Product Taxonomy v1 — `repository/implementation-assets/product-foundation/01_MASTER_PRODUCT_TAXONOMY_V1.yaml` (Not yet approved)
- Future Reference: Global Attribute Library v1 — `repository/implementation-assets/product-foundation/02_GLOBAL_ATTRIBUTE_LIBRARY_V1.yaml` (Not yet approved)
- Future Reference: Pipe Family Template v1 — `repository/implementation-assets/product-foundation/03_PIPE_FAMILY_TEMPLATE_V1.yaml` (Not yet approved)
- Future Reference: Profile Family Template v1 — `repository/implementation-assets/product-foundation/04_PROFILE_FAMILY_TEMPLATE_V1.yaml` (Not yet approved)
- Future Reference: Variant and SKU Rules v1 — `repository/implementation-assets/product-foundation/05_VARIANT_AND_SKU_RULES_V1.md` (Not yet approved)
- Future Reference: Product Knowledge Mapping v1 — `repository/implementation-assets/product-foundation/06_PRODUCT_KNOWLEDGE_MAPPING_V1.yaml` (Not yet approved)
- Future Reference: Founder Decision Register v1 — `repository/implementation-assets/product-foundation/07_FOUNDER_DECISION_REGISTER_V1.md` (Not yet approved)
- Future Reference: Pipe/Profile WooCommerce Mapping v1 — `repository/implementation-assets/import-preparation/PIPE_PROFILE_WOOCOMMERCE_MAPPING_V1.csv` (Not yet approved)
- Future Reference: Pipe/Profile Attribute Seed v1 — `repository/implementation-assets/import-preparation/PIPE_PROFILE_ATTRIBUTE_SEED_V1.csv` (Not yet approved)
- Future Reference: Pipe/Profile Validation Rules v1 — `repository/implementation-assets/import-preparation/PIPE_PROFILE_VALIDATION_RULES_V1.md` (Not yet approved)
- Future Reference: Sprint 09A Audit — `docs/AUDIT_REPORT_SPRINT09A.md` (Not yet approved)
- Future Reference: Master Product DNA — `repository/implementation-assets/product-dna/01_MASTER_PRODUCT_DNA.md` (Not yet approved)
- Future Reference: Product Information Model — `repository/implementation-assets/product-dna/02_PRODUCT_INFORMATION_MODEL.yaml` (Not yet approved)
- Future Reference: Product Component Library — `repository/implementation-assets/product-dna/03_PRODUCT_COMPONENT_LIBRARY.yaml` (Not yet approved)
- Future Reference: Product Knowledge Block Library — `repository/implementation-assets/product-dna/04_PRODUCT_KNOWLEDGE_BLOCK_LIBRARY.yaml` (Not yet approved)
- Future Reference: Product Page Assembly Engine — `repository/implementation-assets/product-dna/05_PRODUCT_PAGE_ASSEMBLY_ENGINE.yaml` (Not yet approved)
- Future Reference: Product Configurator UI Model — `repository/implementation-assets/product-dna/06_PRODUCT_CONFIGURATOR_UI_MODEL.yaml` (Not yet approved)
- Future Reference: Product Media Model — `repository/implementation-assets/product-dna/07_PRODUCT_MEDIA_MODEL.yaml` (Not yet approved)
- Future Reference: Product SEO Model — `repository/implementation-assets/product-dna/08_PRODUCT_SEO_MODEL.yaml` (Not yet approved)
- Future Reference: Product Schema Model — `repository/implementation-assets/product-dna/09_PRODUCT_SCHEMA_MODEL.yaml` (Not yet approved)
- Future Reference: Product Relation Model — `repository/implementation-assets/product-dna/10_PRODUCT_RELATION_MODEL.yaml` (Not yet approved)
- Future Reference: Product Lifecycle Model — `repository/implementation-assets/product-dna/11_PRODUCT_LIFECYCLE_MODEL.md` (Not yet approved)
- Future Reference: Product Validation Rules — `repository/implementation-assets/product-dna/12_PRODUCT_VALIDATION_RULES.md` (Not yet approved)
- Future Reference: Product Extensibility Model — `repository/implementation-assets/product-dna/13_PRODUCT_EXTENSIBILITY_MODEL.md` (Not yet approved)
- Future Reference: Product Admin Model — `repository/implementation-assets/product-dna/14_PRODUCT_ADMIN_MODEL.md` (Not yet approved)
- Future Reference: Product DNA Example Pipe — `repository/implementation-assets/product-dna/15_PRODUCT_DNA_EXAMPLE_PIPE.yaml` (Not yet approved)
- Future Reference: Product DNA Example Profile — `repository/implementation-assets/product-dna/16_PRODUCT_DNA_EXAMPLE_PROFILE.yaml` (Not yet approved)
- Future Reference: Sprint 09B Audit — `docs/AUDIT_REPORT_SPRINT09B.md` (Not yet approved)
