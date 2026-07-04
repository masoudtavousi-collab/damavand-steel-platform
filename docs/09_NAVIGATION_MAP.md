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
