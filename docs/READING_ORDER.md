# Repository Reading Order

## Document Control

- **Document ID:** `docs/READING_ORDER.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.4.0
- **Last Updated:** 2026-07-20
- **Last Review:** 2026-07-20
- **Review Cycle:** On navigation or authority change; periodic cadence pending Founder approval
- **Lifecycle:** Review
- **Source of Truth:** [Documentation Index](08_DOCUMENTATION_INDEX.md) and [Navigation Map](09_NAVIGATION_MAP.md)
- **Dependencies:** [Documentation Index](08_DOCUMENTATION_INDEX.md), [Navigation Map](09_NAVIGATION_MAP.md)
- **Related Documents:** [AI Collaboration Standard](AI_COLLABORATION.md), [Repository Metadata Standard](REPOSITORY_METADATA.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), [Knowledge Graph](KNOWLEDGE_GRAPH.md), [Git Governance](GIT_GOVERNANCE.md), and [Repository Health](REPOSITORY_HEALTH.md)
- **Traceability:** [Repository Traceability Matrix](TRACEABILITY_MATRIX.md), [Decision Log](10_DECISION_LOG.md), and controlled registers
- **AI Compatibility:** AI-ready after Founder approval
- **Approval:** Pending Founder approval

## Purpose

Provide role-specific reading paths so a new human or AI collaborator can understand authority, constraints, unresolved decisions, and next steps without historical chat context.

## Universal Entry Sequence

Every reader starts with:

1. [Codex Repository Instructions](../AGENTS.md) for Codex sessions; other roles may use it as a concise boundary summary.
2. [Project Baseline](PROJECT_BASELINE.md), the concise current-state entry point.
3. [Repository Relationship Map](REPOSITORY_RELATIONSHIP_MAP.md) when another repository, Factory, Generator, or cross-repository concept is involved.
4. [Current Project State](CURRENT_PROJECT_STATE.md) and [Project Execution Roadmap](PROJECT_EXECUTION_ROADMAP.md).
5. [Project Bible](00_PROJECT_BIBLE.md), especially the Core Project Principles.
6. [Project Constitution](01_PROJECT_CONSTITUTION.md).
7. [Documentation Index](08_DOCUMENTATION_INDEX.md).
8. [Glossary](11_GLOSSARY.md).
9. [Decision Log](10_DECISION_LOG.md).
10. [Founder Decision Log](17_FOUNDER_DECISION_LOG.md) and [Open Questions](18_OPEN_QUESTIONS.md).

Readers then follow the applicable role path.

For the current Wave 2 pre-implementation governance reconciliation, readers must review [Project Baseline](PROJECT_BASELINE.md), the Wave 2 governance section in [Traceability Matrix](TRACEABILITY_MATRIX.md), `FD-W2G-001` through `FD-W2G-004` in the [Founder Decision Log](17_FOUNDER_DECISION_LOG.md#settled-wave-2-pre-implementation-governance-decisions), [Product Data Model](19_PRODUCT_DATA_MODEL.md), and [Platform Directory Standard](../repository/platform/PLATFORM_DIRECTORY_STANDARD.md). [FD-GIT-W1-001](17_FOUNDER_DECISION_LOG.md#settled-class-b-wave-1-repository-control-decision) and GIT-02S remain historical evidence. PR #1–#3 are merged, default `main` and protection are established, and Wave 2 discovery is complete. Wave 2A implementation, runtime, workflows, WordPress, Product/Knowledge implementation, publication, deployment, production, and repository-settings changes remain outside the current authorization.

## Founder Reading Path

1. Universal Entry Sequence.
2. [Batch 02A Audit](AUDIT_REPORT_BATCH02A.md).
3. [Founder Decision Log](17_FOUNDER_DECISION_LOG.md).
4. [Open Questions](18_OPEN_QUESTIONS.md).
5. [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md).
6. [Review Process](15_REVIEW_PROCESS.md).
7. [Repository Standards](07_REPOSITORY_GUIDE.md), especially numbering and baseline proposals.
8. [Batch 02B Audit](AUDIT_REPORT_BATCH02B.md).
9. [Repository Health](REPOSITORY_HEALTH.md).
10. [Git Governance](GIT_GOVERNANCE.md).
11. [Batch 03 Audit](AUDIT_REPORT_BATCH03.md).

## New Developer Reading Path

1. Universal Entry Sequence.
2. [Getting Started](GETTING_STARTED.md), treated as Draft guidance.
3. [Technology Stack](05_TECH_STACK.md).
4. [Repository Standards](07_REPOSITORY_GUIDE.md).
5. [Development Workflow](08_DEVELOPMENT_WORKFLOW.md).
6. [Testing Strategy](13_TESTING_STRATEGY.md).
7. [Git Governance](GIT_GOVERNANCE.md).
8. [AI Collaboration Standard](AI_COLLABORATION.md) when using AI assistance.

No implementation begins until the relevant Draft dependencies and Founder decisions are resolved and implementation is explicitly authorized.

## AI Reading Path

1. Universal Entry Sequence.
2. [AI Collaboration Standard](AI_COLLABORATION.md).
3. [Repository Metadata Standard](REPOSITORY_METADATA.md).
4. [Traceability Matrix](TRACEABILITY_MATRIX.md).
5. [Knowledge Graph](KNOWLEDGE_GRAPH.md).
6. [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md).
7. [Documentation Quality Standard](16_QUALITY_STANDARD.md).
8. Task-specific governing and dependent documents.
9. [Repository Health](REPOSITORY_HEALTH.md).
10. [Git Governance](GIT_GOVERNANCE.md) for repository mutations.
11. Latest applicable audit record.

For current work after Sprint 09B, treat the listed future Sprint 09C–12A, Golden, GIT-02S, Git baseline, and Repository Freeze references as historical evidence only; many referenced files are absent from canonical `main` and do not establish present asset readiness. For current governance, read `FD-W2G-001` through `FD-W2G-004`, [Current Project State](CURRENT_PROJECT_STATE.md), [Implementation Readiness](IMPLEMENTATION_READINESS.md), and [Git Baseline Approval Checklist](GIT_BASELINE_APPROVAL_CHECKLIST.md). Treat [Git File Classification](GIT_FILE_CLASSIFICATION.csv) as a dated snapshot, not current Git state or implementation authority.

An AI must verify current files and must not rely on a previous handoff or chat summary as authority.

## Auditor Reading Path

1. Universal Entry Sequence.
2. [Repository Metadata Standard](REPOSITORY_METADATA.md).
3. [Traceability Matrix](TRACEABILITY_MATRIX.md).
4. [Knowledge Graph](KNOWLEDGE_GRAPH.md).
5. [Review Process](15_REVIEW_PROCESS.md).
6. [Documentation Quality Standard](16_QUALITY_STANDARD.md).
7. Relevant repository quality checklists.
8. [Repository Health](REPOSITORY_HEALTH.md).
9. [Git Governance](GIT_GOVERNANCE.md).
10. Audit reports in chronological order, retaining their evidence-only status.

## SEO Reading Path

1. Universal Entry Sequence.
2. [Business Rules](03_BUSINESS_RULES.md).
3. [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md).
4. [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md).
5. [Enterprise Site Structure](25_SITE_STRUCTURE.md), [Enterprise URL Architecture](26_URL_ARCHITECTURE.md), [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md), and [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md).
6. [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), [Schema.org Semantic Strategy](31_SCHEMA_ORG_STRATEGY.md), [Enterprise Content Types](32_CONTENT_TYPES.md), [Enterprise Media Strategy](33_MEDIA_STRATEGY.md), and [Enterprise SEO Entity Model](34_SEO_ENTITY_MODEL.md).
7. [SEO Strategy](11_SEO_STRATEGY.md).
8. [SEO Supporting Document](seo/README.md).
9. [UX Principles](12_UX_PRINCIPLES.md).
10. [SEO Checklist](../quality/SEO_CHECKLIST.md).

## WordPress Engineer Reading Path

1. Universal Entry Sequence.
2. [Enterprise Architecture](02_ARCHITECTURE.md).
3. [Technology Stack](05_TECH_STACK.md).
4. [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md).
5. [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md).
6. [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md) and [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md).
7. [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md) and [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md).
8. [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Enterprise Site Structure](25_SITE_STRUCTURE.md), [Enterprise URL Architecture](26_URL_ARCHITECTURE.md), [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md), and [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md).
9. [Traceability Matrix](TRACEABILITY_MATRIX.md).
10. [Security](10_SECURITY.md), [Testing Strategy](13_TESTING_STRATEGY.md), and [Deployment](09_DEPLOYMENT.md).
11. WordPress, WooCommerce, Blocksy, and Elementor checklists under `/quality`.
12. [Batch 04 Audit](AUDIT_REPORT_BATCH04.md), [Batch 05 Audit](AUDIT_REPORT_BATCH05.md), and the applicable Information Architecture audit.

WordPress implementation remains prohibited until explicitly authorized.

## Content Team Reading Path

1. Universal Entry Sequence.
2. [Business Rules](03_BUSINESS_RULES.md).
3. [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md).
4. [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md).
5. [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md) and [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md).
6. [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Enterprise Site Structure](25_SITE_STRUCTURE.md), and [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md).
7. [Enterprise URL Architecture](26_URL_ARCHITECTURE.md) and [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md).
8. [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), and [Enterprise Content Types](32_CONTENT_TYPES.md).
9. [Schema.org Semantic Strategy](31_SCHEMA_ORG_STRATEGY.md), [Enterprise Media Strategy](33_MEDIA_STRATEGY.md), and [Enterprise SEO Entity Model](34_SEO_ENTITY_MODEL.md).
10. [Content Operations](content/README.md).
11. [Glossary](11_GLOSSARY.md).
12. [SEO Strategy](11_SEO_STRATEGY.md).
13. [UX Principles](12_UX_PRINCIPLES.md).

No product taxonomy or steel terminology may be inferred while the relevant Founder decisions remain open.

## Product Data and WooCommerce Reading Path

1. Universal Entry Sequence.
2. [Business Rules](03_BUSINESS_RULES.md) and [ADR 0001](adr/0001-inquiry-first-commerce.md).
3. [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md).
4. [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md), treated only as non-governing Draft related context pending Founder disposition.
5. [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), which is self-contained for its proposed scope and does not derive authority from Product Data Strategy.
6. [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md).
7. [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md).
8. [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md).
9. [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md).
10. [Traceability Matrix](TRACEABILITY_MATRIX.md).
11. [Batch 05 Audit](AUDIT_REPORT_BATCH05.md), [Batch 05A Audit](AUDIT_REPORT_BATCH05A.md), and [Batch 05B Audit](AUDIT_REPORT_BATCH05B.md).

No product, term, attribute value, variation, inquiry form, setting, import, schema, UI, or implementation may be created from these Review-state models without explicit approval.

## Information Architecture Reading Path

1. Universal Entry Sequence.
2. [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) and [ADR 0001](adr/0001-inquiry-first-commerce.md).
3. [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md).
4. [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), and [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md).
5. [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md).
6. [Enterprise Site Structure](25_SITE_STRUCTURE.md).
7. [Enterprise URL Architecture](26_URL_ARCHITECTURE.md).
8. [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md).
9. [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md).
10. [Decision Log](10_DECISION_LOG.md), [Founder Decision Log](17_FOUNDER_DECISION_LOG.md), [Open Questions](18_OPEN_QUESTIONS.md), and [Traceability Matrix](TRACEABILITY_MATRIX.md).
11. Applicable SEO, UX, content, security, testing, and quality documents.
12. [Batch 06 Audit](AUDIT_REPORT_BATCH06.md).

The Batch 06 documents are logical Review-state proposals. They authorize no page, menu, URL, search index, filter, internal link, representative profile, plugin, theme, WordPress configuration, or code.

## Content and Entity Architecture Reading Path

1. Universal Entry Sequence.
2. [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles), [ADR 0001](adr/0001-inquiry-first-commerce.md), and [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md).
3. [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), and [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md).
4. [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Enterprise Site Structure](25_SITE_STRUCTURE.md), [Enterprise URL Architecture](26_URL_ARCHITECTURE.md), [Enterprise Search and Discovery](27_SEARCH_AND_DISCOVERY.md), and [Enterprise Internal Linking Model](28_INTERNAL_LINKING_MODEL.md).
5. [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md).
6. [Enterprise Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md).
7. [Schema.org Semantic Strategy](31_SCHEMA_ORG_STRATEGY.md).
8. [Enterprise Content Types](32_CONTENT_TYPES.md).
9. [Enterprise Media Strategy](33_MEDIA_STRATEGY.md).
10. [Enterprise SEO Entity Model](34_SEO_ENTITY_MODEL.md).
11. [Decision Log](10_DECISION_LOG.md), [Founder Decision Log](17_FOUNDER_DECISION_LOG.md), [Open Questions](18_OPEN_QUESTIONS.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), and [Knowledge Graph](KNOWLEDGE_GRAPH.md).
12. Applicable content, SEO, UX, accessibility, security, privacy, legal, testing, and quality documents.
13. [Batch 07 Audit](AUDIT_REPORT_BATCH07.md).

The Batch 07 documents are logical Review-state proposals. They authorize no content, entity, WordPress object, schema markup, media operation, SEO output, AI/LLM/search capability, plugin, configuration, or code.

## WordPress Solution Blueprint Reading Path

1. Complete the Universal Entry Sequence and [WordPress Engineer Reading Path](#wordpress-engineer-reading-path).
2. Read [Enterprise WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md).
3. Read [Blocksy Configuration](36_BLOCKSY_CONFIGURATION.md), [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md), and [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md).
4. Read [Custom Post Types](39_CUSTOM_POST_TYPES.md), [Taxonomy Implementation](40_TAXONOMY_IMPLEMENTATION.md), and [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md).
5. Read [Inquiry Workflow](42_INQUIRY_WORKFLOW.md), [User Roles](43_USER_ROLES.md), and [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md).
6. Review [Decision Log](10_DECISION_LOG.md), [Founder Decision Log](17_FOUNDER_DECISION_LOG.md), [Open Questions](18_OPEN_QUESTIONS.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), and [Knowledge Graph](KNOWLEDGE_GRAPH.md).
7. Read [Batch 08 Audit](AUDIT_REPORT_BATCH08.md).

Documents 35 through 44 are Review-state Blueprints. They authorize no code, installation, configuration, template, CPT, taxonomy, field, role, workflow, vendor selection, or implementation.

## Repository Baseline and Release Engineering Reading Path

1. Complete the [Universal Entry Sequence](#universal-entry-sequence).
2. Read [Repository Baseline v1.0](BASELINE_v1.0.md) and [Repository Release Notes v1.0](RELEASE_NOTES_v1.0.md).
3. Read [Implementation Readiness](IMPLEMENTATION_READINESS.md) before interpreting any sprint as executable.
4. Read [Sprint Roadmap](SPRINT_ROADMAP.md) and [Engineering Guidelines](ENGINEERING_GUIDELINES.md).
5. Review [Founder Decision Log](17_FOUNDER_DECISION_LOG.md), [Open Questions](18_OPEN_QUESTIONS.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), [Knowledge Graph](KNOWLEDGE_GRAPH.md), and [Repository Health](REPOSITORY_HEALTH.md).
6. Finish with [Repository Freeze v1.0 Audit](AUDIT_REPORT_FREEZE_v1.0.md).

The baseline is approved only as an exact local repository snapshot. Read each included document's lifecycle before treating its content as authority. The Roadmap and Engineering Guidelines remain Review-state proposals, and no sprint is authorized by this path.

## Remote Access and Iran Execution Reading Path

1. Complete the [Universal Entry Sequence](#universal-entry-sequence).
2. Read [Repository Baseline v1.0](BASELINE_v1.0.md), [Engineering Guidelines](ENGINEERING_GUIDELINES.md), and [Implementation Readiness](IMPLEMENTATION_READINESS.md).
3. Read the evidence boundaries in [Sprint 01B Audit](AUDIT_REPORT_SPRINT01B.md) and [Sprint 01C Audit](AUDIT_REPORT_SPRINT01C.md).
4. Read [Remote Access and Iran Execution Constraints Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md).
5. Review [SSH Access Checklist](../repository/config/SSH_ACCESS_CHECKLIST.md), [Deployment Access Policy](../repository/config/DEPLOYMENT_ACCESS_POLICY.md), and [Iran Execution Risk Register](../repository/config/IRAN_EXECUTION_RISK_REGISTER.md).
6. Review [Founder Decision Log](17_FOUNDER_DECISION_LOG.md), [Open Questions](18_OPEN_QUESTIONS.md), and [Sprint 01D Audit](AUDIT_REPORT_SPRINT01D.md).

This path documents a proposed route only. It grants no remote, account, credential, SSH connection, hosting mutation, deployment, WP-CLI action, WordPress installation, or implementation authority.

## Reading-State Rules

- `Approved` sources may govern within their declared scope.
- `Review` sources are proposals awaiting approval.
- `Draft` sources provide context but cannot create approved requirements.
- `Blocked` sources identify an unresolved dependency and cannot progress until the exit condition is met.
- `Superseded`, `Deprecated`, `Archived`, `Historical`, and `Cancelled` sources do not define current authority; follow an approved successor when one exists.
- Audit reports provide evidence and recommendations, not governing decisions.
- Supporting documents cannot override governing documents.
- If a required path contains a conflict or missing authority, stop and register it.

## References

- [Navigation Map](09_NAVIGATION_MAP.md)
- [Knowledge Graph](KNOWLEDGE_GRAPH.md)
- [AI Collaboration Standard](AI_COLLABORATION.md)
- [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md)
- [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md)
- [Enterprise WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- [Repository Baseline v1.0](BASELINE_v1.0.md)
- [Implementation Readiness Assessment](IMPLEMENTATION_READINESS.md)
- [Remote Access and Iran Execution Constraints Architecture](45_REMOTE_ACCESS_ARCHITECTURE.md)
- [Sprint 01D Audit](AUDIT_REPORT_SPRINT01D.md)
- [Project Baseline](PROJECT_BASELINE.md)
- [Repository Relationship Map](REPOSITORY_RELATIONSHIP_MAP.md)
- Future Reference: GIT-02S Audit — `docs/AUDIT_REPORT_GIT02S.md` (Not yet approved)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Repository Traceability Matrix](TRACEABILITY_MATRIX.md)
