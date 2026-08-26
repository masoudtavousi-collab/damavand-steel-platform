# Repository Reading Order

## Document Control

- **Document ID:** `docs/READING_ORDER.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.22.0
- **Last Updated:** 2026-08-26
- **Last Review:** 2026-08-26
- **Review Cycle:** On navigation or authority change; periodic cadence pending Founder approval
- **Lifecycle:** Review
- **Source of Truth:** [Documentation Index](08_DOCUMENTATION_INDEX.md) and [Navigation Map](09_NAVIGATION_MAP.md)
- **Dependencies:** [Documentation Index](08_DOCUMENTATION_INDEX.md), [Navigation Map](09_NAVIGATION_MAP.md)
- **Related Documents:** [Context Router](CONTEXT_ROUTER.md), [C000 OS2 Decision Package](C000_OS2_STRATEGIC_RECONCILIATION_DECISION_PACKAGE.md), [AI Collaboration Standard](AI_COLLABORATION.md), [AI Context Manifest](../repository/governance/ai_context_manifest.yaml), [Repository Metadata Standard](REPOSITORY_METADATA.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), [Knowledge Graph](KNOWLEDGE_GRAPH.md), [Git Governance](GIT_GOVERNANCE.md), and [Repository Health](REPOSITORY_HEALTH.md)
- **Traceability:** [Repository Traceability Matrix](TRACEABILITY_MATRIX.md), [Decision Log](10_DECISION_LOG.md), and controlled registers
- **AI Compatibility:** AI-ready after Founder approval
- **Approval:** Pending Founder approval

## Purpose

Provide role-specific reading paths so a new human or AI collaborator can understand authority, constraints, unresolved decisions, and next steps without historical chat context.

## Universal Entry Sequence

Every reader starts with:

1. [Codex Repository Instructions](../AGENTS.md) for Codex sessions; other roles may use it as a concise boundary summary.
2. Resolve the live GitHub `main` SHA and inspect the local branch and clean/dirty state; never substitute a fixed SHA from prose, memory, or a handoff.
3. Determine live active writer Missions/open pull requests, classify ownership, verify `MAX_ACTIVE_WIP = 3`, and check path collisions; stable files do not store the mutable active list.
4. [Current Project State](CURRENT_PROJECT_STATE.md), the only mutable operational-state pointer.
5. [Context Router](CONTEXT_ROUTER.md), which selects the smallest task-specific context set.
6. [C000 OS2 Decision Package](C000_OS2_STRATEGIC_RECONCILIATION_DECISION_PACKAGE.md), the accepted Project OS 2.0 strategic reconciliation.
7. [Project Baseline](PROJECT_BASELINE.md), the concise orientation layer.

An AI session must then read [AI Collaboration Standard](AI_COLLABORATION.md), establish its named role, complete the Task Context Envelope, and verify the material-artifact custody/checkpoint plan before mutation. The [AI Context Manifest](../repository/governance/ai_context_manifest.yaml) supplies stable machine-readable pointers and invariants only; it is not authority and does not contain mutable current state. A new writer without a live WIP slot returns `STOP — WIP_LIMIT_REACHED`.

Readers then follow only the applicable role and Layer 1 route. DS-PC (`HOW`), DS-SPD (`WHAT`), decision logs, roadmap, domain models, and historical evidence are loaded when that route or the active task requires them—not as a universal context dump.

For C006 Product Data semantic or Product Experience work, read [C006 Scope](C006_PRODUCT_DATA_SEMANTIC_PRODUCT_EXPERIENCE_ARCHITECTURE_SCOPE_V1.0.md), then the canonical Product/Attribute/Measurement owners and [Product Experience Engine](../repository/enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md). The latter is an architecture-only orchestration owner and does not replace Product, Knowledge, Media, Commerce or Inquiry truth.

For current work, readers must obtain the exact phase, branch, authorization, pull-request state, GO/NO-GO boundary, and next action from Current Project State. DS-PC (`HOW`) and DS-SPD (`WHAT`) are stable companion governing sources and do not compete with that operational pointer. Historical scopes retain their original bounded meanings: C003-R1/C003-R2/C003-R3 and C005 record their then-current `0/9` C002 evidence/readiness outcomes and create no Product/SKU authority. Later [C008](C008_C002_READINESS_REAL_WORLD_EVIDENCE_CLOSURE_SCOPE_V1.0.md) repaired the effective C002 result to `6/9 / NOT_READY`; [C008-R1](C008_R1_C002_REMAINING_REAL_WORLD_EVIDENCE_CLOSURE_SCOPE_V1.0.md) preserved it; [C008-FT1](C008_FT1_FAST_TRACK_INQUIRY_LAUNCH_GOVERNANCE_AMENDMENT_V1.0.md) created a separate fail-closed sibling gate; and [C009](C009_FIRST_COMMERCIAL_SLICE_CANONICAL_LEAF_PROMOTION_SCOPE_V1.0.md) separately promoted exactly `pilot:f5922666261e` into `pcomb:829e387ccdcb` and internal SKU leaf `prd:sku:66ebd0510693`. [C009-FT2](C009_FT2_POST_C009_FAST_TRACK_GATE_REEVALUATION_V1.0.md) changes only the effective Product-promotion prerequisite, while [FT-RB-00](FT_RB_00_FAST_TRACK_REMAINING_BLOCKERS_CAMPAIGN_STATUS_V1.0.md) only routes separately authorized lanes. Product Data remains `PARTIAL`; Taxonomy `NOT_READY`; C002 `6/9 / NOT_READY`; Availability `MISSING_DATA_VALUE`; Import, Publication and Runtime `NO-GO`; Commerce `INQUIRY_ONLY`; No Public Pricing preserved; no public commercial SKU exists; and no general Product readiness, Merge, Runtime, Deployment, Production, or successor authority follows.

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
3. [AI Context Manifest](../repository/governance/ai_context_manifest.yaml) as a pointer/invariant check, never as authorization.
4. Establish the named role and complete Task Context Envelope.
5. [Repository Metadata Standard](REPOSITORY_METADATA.md).
6. [Traceability Matrix](TRACEABILITY_MATRIX.md).
7. [Knowledge Graph](KNOWLEDGE_GRAPH.md).
8. [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md).
9. [Documentation Quality Standard](16_QUALITY_STANDARD.md).
10. Task-specific governing and dependent documents selected by the Context Router.
11. [Repository Health](REPOSITORY_HEALTH.md).
12. [Git Governance](GIT_GOVERNANCE.md) for repository mutations.
13. Latest applicable audit record only when the routed task requires historical evidence.

Treat listed future Sprint 09C–12A, Golden, GIT-02S, Git-baseline, and Repository-Freeze references as historical evidence only; referenced or absent files do not establish current readiness. Obtain current governance and Product state from [Current Project State](CURRENT_PROJECT_STATE.md) and the scope-specific sources selected by the Context Router, including C008/C009/FT-RB owners when applicable. Treat [Git File Classification](GIT_FILE_CLASSIFICATION.csv) as a dated snapshot, not current Git state or implementation authority.

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
10. [BP2 Data Administration Scope v1.0](BP2_DATA_ADMINISTRATION_SCOPE_V1.0.md), treated as an `APPROVED`, documentation-only governance contract with no implementation authority.
11. [PD-01 Product Data Contract Enablement Scope v1.0](PD01_PRODUCT_DATA_CONTRACT_SCOPE_V1.0.md), treated as the approved exact synthetic-only Scope/Approval and Test Contract; it creates no canonical Product Data.
12. [PD-02A Controlled Values and Attribute Profiles Scope v1.0](PD02A_CONTROLLED_VALUES_ATTRIBUTE_PROFILES_SCOPE_V1.0.md), treated as the approved synthetic-only Scope/Approval and Test Contract after legal lifecycle and independent PASS; its canonical registries must remain empty.
13. [PD-02B Minimum Canonical Slice Scope v1.0](PD02B_MINIMUM_CANONICAL_SLICE_SCOPE_V1.0.md), treated as the exact APPROVED authority and lifecycle/test/evidence boundary.
14. [PD-03A Pilot Prerequisite Foundation Scope v1.0](PD03A_PILOT_PREREQUISITE_FOUNDATION_SCOPE_V1.0.md) and [PD-03B Canonical Pilot Scope v1.0](PD03B_CANONICAL_PILOT_SCOPE_V1.0.md), treated within their exact immutable extension and seed/reference boundaries.
15. [C002 Commercial Pilot Truth and Product Administration Contracts v1.0](C002_COMMERCIAL_PILOT_PRODUCT_ADMINISTRATION_CONTRACTS_SCOPE_V1.0.md), treated as contract infrastructure with empty canonical instance registries.
16. [C003 Founder Discovery Reconciliation and Repository Intake v1.0](C003_FOUNDER_DISCOVERY_RECONCILIATION_SCOPE_V1.0.md), treated as classified evidence and inactive owner/backlog mapping rather than Product, value, tuple, SKU, Availability, price, stock, customer/order, or runtime truth.
17. [C003-R1 Checkpoint 03 Scope v1.0](C003_R1_CHECKPOINT03_201_51_PILOT_READINESS_SCOPE_V1.0.md), treated as immutable evidence/readiness input with zero valid tuples and `0/9` readiness.
18. [C003-R2 Scope](C003_R2_201_51_FOUNDER_EVIDENCE_COMPLETION_SCOPE_V1.0.md) and [Founder Packet](C003_R2_201_51_FOUNDER_EVIDENCE_COMPLETION_PACKET_V1.0.md), treated as the predecessor evidence-only review surface.
19. [C003-R3 Scope](C003_R3_201_51_FOUNDER_ANSWER_RECONCILIATION_SCOPE_V1.0.md), treated as exact Founder-answer evidence reconciliation with no canonical promotion and unchanged C002 `0/9` readiness.
20. [C004 Competitive Intelligence Scope](C004_COMPETITIVE_INTELLIGENCE_SCOPE_V1.0.md), [Competitive Matrix](COMPETITIVE_INTELLIGENCE_MATRIX_V1.0.md), [Damavand Advantage Specification](DAMAVAND_COMPETITIVE_ADVANTAGE_SPECIFICATION_V1.0.md), [Anti-Pattern Register](DAMAVAND_COMPETITIVE_ANTI_PATTERN_REGISTER_V1.0.md), and [201/51 Competitive Experience Blueprint](201_51_PILOT_COMPETITIVE_EXPERIENCE_BLUEPRINT_V1.0.md), treated only as supplementary external evidence and architecture planning with no Product/SEO/commerce/runtime authority.
21. [C005 Founder Evidence & C002 Readiness Re-evaluation Scope](C005_201_51_FOUNDER_EVIDENCE_READINESS_REEVALUATION_SCOPE_V1.0.md) and [Readiness Packet](C005_201_51_READINESS_REEVALUATION_PACKET_V1.0.md), treated as evidence/readiness reconciliation only: 8 submitted, 1 missing, 6 separately reviewable, 9 open/blocking and zero resolved.
22. [C006 Product Data Semantic & Product Experience Architecture Scope](C006_PRODUCT_DATA_SEMANTIC_PRODUCT_EXPERIENCE_ARCHITECTURE_SCOPE_V1.0.md) and [Product Experience Engine](../repository/enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md), treated as architecture-only semantic/projection reconciliation with no Product/value/tuple/SKU/commercial/runtime population.
23. [C007 Governance Convergence Scope](C007_GOVERNANCE_CONVERGENCE_PHASE1_ARCHITECTURE_BASELINE_SCOPE_V1.0.md), treated as bounded owner-summary convergence with no Product/commercial/Runtime authority.
24. [C008 Readiness Evidence Closure](C008_C002_READINESS_REAL_WORLD_EVIDENCE_CLOSURE_SCOPE_V1.0.md) and [C008-R1](C008_R1_C002_REMAINING_REAL_WORLD_EVIDENCE_CLOSURE_SCOPE_V1.0.md), treated as evidence/readiness owners for effective C002 `6/9 / NOT_READY`, not Product promotion.
25. [C008-FT1 Fast-Track Amendment](C008_FT1_FAST_TRACK_INQUIRY_LAUNCH_GOVERNANCE_AMENDMENT_V1.0.md), treated as the immutable historical sibling-gate owner at `FALSE / 4 of 12`, not launch or Runtime authority.
26. [C009 Canonical Leaf Promotion](C009_FIRST_COMMERCIAL_SLICE_CANONICAL_LEAF_PROMOTION_SCOPE_V1.0.md) and [C009 registry](../repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml), treated as the exact one-to-one binding `pilot:f5922666261e` → `pcomb:829e387ccdcb` → internal SKU leaf `prd:sku:66ebd0510693` for Stainless Steel / 201 / Silver / 51 mm / 0.50 mm / 6 m, with no public commercial SKU, Availability, import, publication, Runtime, or broad-readiness effect.
27. [C009-FT2](C009_FT2_POST_C009_FAST_TRACK_GATE_REEVALUATION_V1.0.md), treated as an effective prerequisite re-evaluation only; the sibling gate remains false.
28. [FT-RB-00 Campaign Status](FT_RB_00_FAST_TRACK_REMAINING_BLOCKERS_CAMPAIGN_STATUS_V1.0.md), treated as a routing/status owner that starts no lane automatically.
29. [Traceability Matrix](TRACEABILITY_MATRIX.md).
30. [Batch 05 Audit](AUDIT_REPORT_BATCH05.md), [Batch 05A Audit](AUDIT_REPORT_BATCH05A.md), and [Batch 05B Audit](AUDIT_REPORT_BATCH05B.md).

No product, term, attribute value, variation, inquiry form, setting, import, schema, UI, or implementation may be created from these Review-state models without explicit approval.

## Competitive Intelligence Reading Path

1. Universal Entry Sequence.
2. [Source of Truth Priority](SOURCE_OF_TRUTH_PRIORITY.md) for the supplementary-evidence boundary.
3. [C004 Competitive Intelligence Scope](C004_COMPETITIVE_INTELLIGENCE_SCOPE_V1.0.md) for authority, source, owner and copyright rules.
4. [Competitive Intelligence Matrix](COMPETITIVE_INTELLIGENCE_MATRIX_V1.0.md) for dated observations, score limitations and leadership hypotheses.
5. [Damavand Competitive Advantage Specification](DAMAVAND_COMPETITIVE_ADVANTAGE_SPECIFICATION_V1.0.md) and [Anti-Pattern Register](DAMAVAND_COMPETITIVE_ANTI_PATTERN_REGISTER_V1.0.md) for original dispositions.
6. [201/51 Competitive Experience Blueprint](201_51_PILOT_COMPETITIVE_EXPERIENCE_BLUEPRINT_V1.0.md) for the bounded Mobile RTL and SEO planning application.
7. Return to the canonical Product, Search/SEO, Commerce and C002/C003 owners before proposing any downstream change.

Competitor evidence never overrides Product specifications, taxonomy, valid
combinations, Availability, price, commerce, SEO ownership or Runtime state.

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
- [Context Router](CONTEXT_ROUTER.md)
- [AI Context Manifest](../repository/governance/ai_context_manifest.yaml)
- [C000 OS2 Decision Package](C000_OS2_STRATEGIC_RECONCILIATION_DECISION_PACKAGE.md)
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
