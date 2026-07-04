# Navigation Map

## Document Control

- **Document ID:** `docs/09_NAVIGATION_MAP.md` (provisional path identifier)
- **Status:** Draft
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
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

[Project Bible](00_PROJECT_BIBLE.md) → [Project Constitution](01_PROJECT_CONSTITUTION.md) → [Founder Decision Log](17_FOUNDER_DECISION_LOG.md) → [Open Questions](18_OPEN_QUESTIONS.md) → [Decision Log](10_DECISION_LOG.md)

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

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
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
