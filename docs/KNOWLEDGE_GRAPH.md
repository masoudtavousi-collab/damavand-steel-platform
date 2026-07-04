# Repository Knowledge Graph

## Document Control

- **Document ID:** `docs/KNOWLEDGE_GRAPH.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On authority, relationship, or dependency change; periodic cadence pending Founder approval
- **Lifecycle:** Review
- **Source of Truth:** [Documentation Index](08_DOCUMENTATION_INDEX.md), [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles), and accepted ADRs; this graph is a supporting model
- **Dependencies:** [Documentation Index](08_DOCUMENTATION_INDEX.md), [Repository Metadata Standard](REPOSITORY_METADATA.md), [Traceability Matrix](TRACEABILITY_MATRIX.md)
- **Related Documents:** [AI Collaboration Standard](AI_COLLABORATION.md), [Reading Order](READING_ORDER.md), [Navigation Map](09_NAVIGATION_MAP.md), [Git Governance](GIT_GOVERNANCE.md), and [Repository Health](REPOSITORY_HEALTH.md)
- **Traceability:** [Repository Traceability Matrix](TRACEABILITY_MATRIX.md) and the relationship-maintenance rules in this document
- **AI Compatibility:** AI-ready after Founder approval
- **Approval:** Pending Founder approval

## Purpose

Describe the repository's document relationships, authority, dependencies, and cross-references in a machine-readable conceptual model without changing system architecture.

## Graph Scope

The knowledge graph models repository knowledge only. It does not model or authorize WordPress, WooCommerce, infrastructure, product, or business implementation architecture.

## Node Types

| Node type | Meaning | Examples |
| --- | --- | --- |
| Founder Directive | Explicit Founder-approved constraint | CP-001 through CP-010 |
| Governing Document | Intended authority for a defined concern | Project Bible, Business Rules, Enterprise Architecture |
| Decision Record | Authoritative record of an accepted decision | ADR 0001 |
| Supporting Document | Detail that cannot override its governing source | Topic-folder documents |
| Governance Standard | Lifecycle, review, metadata, or quality rule | Document Lifecycle, Metadata Standard |
| Git Governance | Repository evolution, branch, version, tag, baseline, release, and history policy | Git Governance |
| Platform Architecture | Governed logical platform responsibilities and boundaries | WordPress Enterprise Architecture |
| Product Data Model | Governed product, WooCommerce, taxonomy, attribute, and inquiry concepts | Enterprise Product Data Model and Batch 05 dependent models |
| Register | Index of decisions, questions, or traceability | Decision Log, Founder Decision Log, Open Questions |
| Navigation Artifact | Reading and discovery map | Documentation Index, Navigation Map, Reading Order |
| Evidence Record | Historical validation or audit | Batch audit reports |
| Health Record | Current-state coverage and readiness evidence | Repository Health |
| Template | Reusable structure without project decisions | Document Template, ADR Template |
| Future Implementation | Authorized implementation evidence that does not yet exist | Explicitly absent in Batch 02B |

## Relationship Types

| Relationship | Direction | Meaning |
| --- | --- | --- |
| `AUTHORITY_SOURCE` | Controlled document to governing source | Identifies the approved source or explicitly accepted decision that constrains interpretation. |
| `GOVERNS` | Authority to dependent | Defines constraints within declared scope. |
| `CONSTRAINS` | Rule to document or future work | Limits acceptable decisions or changes. |
| `DEPENDS_ON` | Dependent to prerequisite | Requires the prerequisite for correct interpretation. |
| `REQUIRED_BY` | Prerequisite to dependent | Inverse discoverability edge for `DEPENDS_ON`. |
| `EXTENDS` | Child to parent | Adds approved detail without weakening or replacing the parent. |
| `REFERENCES` | Source to related source | Provides navigation without authority transfer. |
| `RELATED_TO` | Either direction | Indicates a non-authoritative contextual relationship. |
| `PARENT_OF` | Parent to child | Identifies the source from which applicable rules are inherited. |
| `CHILD_OF` | Child to parent | Identifies the parent and inherited constraint path. |
| `DECIDED_BY` | Rule or outcome to authoritative decision | Identifies its decision origin. |
| `SUPPORTS` | Supporting to governing | Adds detail without overriding authority. |
| `TRACKS` | Register to item | Indexes an unresolved or historical item. |
| `VALIDATES` | Evidence to subject | Records review evidence for the subject. |
| `REPLACES` | Current document to replaced document | Substitutes a prior record after required approval and migration evidence. |
| `SUPERSEDES` | New authority to old authority | Replaces authority while retaining history. |

## Authority Layers

```text
Layer 0: Founder directives and Accepted decisions
  -> CP-001 through CP-010, Accepted ADRs

Layer 1: Governing project documents
  -> Project Bible, Constitution, Business Rules, Enterprise Architecture,
     Technology Stack, Repository Standards

Layer 2: Governance and platform documents
  -> Lifecycle, Review, Metadata, Quality, WordPress Architecture, Delivery documents

Layer 3: Supporting documents, registers, navigation, and templates
  -> Topic folders, indexes, traceability, reading order, open-question registers

Layer 4: Evidence and historical records
  -> Audit reports and future review evidence
```

A lower layer cannot override a higher layer. Lifecycle and declared scope still determine whether a node is approved authority.

## Relationship Enforcement

- `DEPENDS_ON` and `REQUIRED_BY` are reciprocal views of one dependency and must remain discoverable.
- `PARENT_OF` and `CHILD_OF` express inheritance; the child cannot override its parent.
- `EXTENDS` requires an identified parent and approved scope.
- `REFERENCES`, `RELATED_TO`, and Related Documents provide context only.
- `REPLACES` may substitute content or role only after approval; `SUPERSEDES` additionally ends the prior authority.
- `AUTHORITY_SOURCE` must resolve to approved governing authority or an explicitly accepted decision within its recorded scope.
- Circular navigation is permitted. Circular dependency or authority is a blocking validation failure.

## Core Knowledge Relationships

```text
Founder Directive
  DECIDED_BY -> Founder
  GOVERNS -> Core Project Principles

Core Project Principles
  CONSTRAINS -> Business Rules
  CONSTRAINS -> Enterprise Architecture
  CONSTRAINS -> Technology Stack
  CONSTRAINS -> Repository Standards
  CONSTRAINS -> WordPress Architecture
  CONSTRAINS -> Future Implementation

ADR 0001
  DECIDED_BY -> Founder-approved decision process
  GOVERNS -> Inquiry First and No Public Pricing consequences
  REFERENCES -> Business Rules and Enterprise Architecture

Documentation Index
  TRACKS -> Every documentation node

Traceability Matrix
  REFERENCES -> Rules, governing documents, dependencies, and future evidence

Founder Decision Log + Open Questions
  TRACKS -> Unresolved authority and content

Audit Reports
  VALIDATE -> Repository state at a recorded review point

Repository Health
  VALIDATES -> Current documentation, governance, authority, metadata,
               navigation, traceability, and validation coverage

Git Governance
  CONSTRAINS -> Branches, commits, versions, tags, baselines, releases,
                backups, history, and future repository changes

WordPress Enterprise Architecture
  DEPENDS_ON -> Enterprise Architecture + Business Rules + Technology Stack + ADR 0001
  CONSTRAINS -> Future WordPress + WooCommerce + Blocksy + Elementor implementation
  REFERENCES -> Product Data + SEO + UX + Security + Testing governance

Enterprise Product Data Model
  DEPENDS_ON -> Business Rules + WordPress Enterprise Architecture
  REFERENCES -> Product Data Strategy as non-governing Draft context pending Founder disposition
  PARENT_OF -> WooCommerce Product Model + Product Taxonomy Model
               + Product Attribute Model + Inquiry Data Model
  CONSTRAINS -> Product lifecycle + operational ownership requirements

Product Taxonomy Model
  CONSTRAINS -> Canonical classifications + Collections + Product Tags
                + Application/Use-Case identity + slugs + SEO landing ownership
  REFERENCES -> Product Attribute Model for overlap control

Product Attribute Model
  CONSTRAINS -> Global values + hierarchy boundary + derived Size
                + variation axes + filtering + SEO usage

WooCommerce Product Model
  CONSTRAINS -> Future parent products + variations + local-attribute exceptions
                + visibility + inquiry actions

Inquiry Data Model
  REFERENCES -> Stable product/variation identities
  CONSTRAINS -> Customer identity boundary + future inquiry capture + routing + CRM handoff

Enterprise Information Architecture
  DEPENDS_ON -> WordPress Enterprise Architecture + Product Data Model
                + Product Taxonomy Model + Inquiry Data Model
  CONSTRAINS -> Logical information layers + canonical ownership + authority flow
                + navigation philosophy + future expansion
  PARENT_OF -> Site Structure + URL Architecture
               + Search and Discovery + Internal Linking Model

Site Structure
  DEPENDS_ON -> Enterprise Information Architecture + Product/Taxonomy/Inquiry Models
  CONSTRAINS -> Public site tree + navigation domains + protected/public separation

URL Architecture
  DEPENDS_ON -> Enterprise Information Architecture + Site Structure
  CONSTRAINS -> Canonicals + slugs + namespaces + redirects + forbidden URLs

Search and Discovery
  DEPENDS_ON -> Enterprise Information Architecture + Site Structure + URL Architecture
               + Taxonomy Model + Attribute Model
  CONSTRAINS -> Searchable types + filtering + ranking + public access boundaries

Internal Linking Model
  DEPENDS_ON -> Enterprise Information Architecture + Site Structure
               + URL Architecture + Taxonomy Model
  REFERENCES -> Search and Discovery
  CONSTRAINS -> Link hierarchy + relationship meaning + canonical targets
                + inquiry paths + orphan prevention

Enterprise Content Architecture
  DEPENDS_ON -> Enterprise Information Architecture + Site Structure
               + Product Data Model + Taxonomy Model
  CONSTRAINS -> Content hierarchy + ownership + lifecycle + sources
                + reuse + validation + versioning + approval
  PARENT_OF -> Entity Relationship Model + Content Types + Media Strategy
               + Schema.org Strategy + SEO Entity Model

Entity Relationship Model
  DEPENDS_ON -> Product/Taxonomy/Attribute/Inquiry Models
               + Enterprise Information Architecture + Content Architecture
  CONSTRAINS -> Entity identity + fields + owners + lifecycles
                + typed relationships + public/protected projections

Schema.org Strategy
  DEPENDS_ON -> Entity Relationship Model + Content Architecture + URL Architecture
  REFERENCES -> Official Schema.org vocabulary
  CONSTRAINS -> Future public semantic eligibility + identity + relationship projection

Content Types
  DEPENDS_ON -> Content Architecture + Entity Relationship Model + Site Structure
  CONSTRAINS -> Content purpose + audience + fields + relationships
                + SEO/navigation roles + lifecycle + ownership

Media Strategy
  DEPENDS_ON -> Content Architecture + Entity Relationship Model + Product Media Set
  CONSTRAINS -> Media identity + rights + lifecycle + naming + organization
                + accessibility + localization + derivatives + protected delivery

SEO Entity Model
  DEPENDS_ON -> Information/URL/Content/Entity Architecture
  REFERENCES -> Search and Discovery + Internal Linking + Schema + Media
  CONSTRAINS -> Entity-first SEO + canonical/intent ownership + landing eligibility
                + future semantic/AI/LLM retrieval compatibility boundaries

Enterprise WordPress Solution Blueprint
  DEPENDS_ON -> WordPress Architecture + Product/IA/Content/Entity Models + ADR 0001
  PARENT_OF -> Blocksy Configuration + Elementor Architecture + WooCommerce Configuration
               + CPT Blueprint + Taxonomy Implementation + Custom Fields Model
               + Inquiry Workflow + User Roles + Plugin Responsibility Matrix
  CONSTRAINS -> Future separately approved WordPress implementation plans

Blocksy Configuration + Elementor Architecture
  CONSTRAINS -> Global shell + bounded page-body composition ownership
  DEPENDS_ON -> WordPress/WooCommerce data + SEO/schema + business authority

WooCommerce Configuration + Inquiry Workflow
  CONSTRAINS -> Catalog context + protected Inquiry lifecycle
  DEPENDS_ON -> Inquiry First + No Public Pricing

CPT Blueprint + Taxonomy Implementation + Custom Fields Model
  EXTENDS -> Logical entities/content/classifications/fields with future platform mapping gates
  DEPENDS_ON -> Founder approval + Plugin First/Configuration First selection before registration

User Roles + Plugin Responsibility Matrix
  CONSTRAINS -> Least privilege + one capability owner + upgrades/replacement
  DEPENDS_ON -> Future explicit authorization before roles + plugins + settings + runtime implementation

Repository Baseline v1.0
  DEPENDS_ON -> Exact Founder freeze directive + repository validation
  TRACKS -> Exact tagged repository tree + included authority/lifecycle states
  REFERENCES -> Release Notes + Freeze Audit + Repository Health
  CONSTRAINS -> Future changes through immutable baseline identity

Implementation Readiness
  DEPENDS_ON -> Repository Baseline + Architecture/Blueprint lifecycle + open prerequisites
  VALIDATES -> Current readiness and blocking items
  REQUIRED_BY -> Sprint 02 entry decision

Sprint Roadmap + Engineering Guidelines
  DEPENDS_ON -> Accepted Core Principles + future approved architecture/Blueprint decisions
  CONSTRAINS -> Future authorized sprint workflow and quality gates after approval
  REFERENCES -> Founder Decision Log + Open Questions

Repository Freeze v1.0 Audit
  VALIDATES -> Baseline scope + navigation + traceability + authority
               + architecture/Blueprint/documentation completeness + release/readiness boundaries

Sprint 01A Repository Workspace
  DEPENDS_ON -> Repository Baseline + Implementation Readiness + Engineering Guidelines
  EXTENDS -> Repository engineering structure without WordPress implementation
  PARENT_OF -> Implementation Rules + Build Checklist + Pre-Implementation Checklist

Repository Implementation Rules
  CONSTRAINS -> Folder ownership + naming + versioning + migration + backup
                + build + quality + rollback
  DEPENDS_ON -> Future Founder approval before implementation use

Build Checklist + Pre-Implementation Checklist
  TRACKS -> Unmet environment + hosting + DNS + TLS + database + PHP + MariaDB
            + WordPress + plugin + theme + developer + Founder prerequisites
  REQUIRED_BY -> Future exact Sprint 02 authorization

Sprint 01A Audit
  VALIDATES -> Repository/folder/document/Blueprint consistency
               + implementation-readiness and no-implementation boundaries

Sprint 01B Environment Report
  DEPENDS_ON -> Implementation Rules + Build Checklist + Pre-Implementation Checklist
  VALIDATES -> Local server + PHP + MariaDB + HTTPS + filesystem + limits
               + timezone + charset + tooling observations

Sprint 01B Plugin Inventory
  DEPENDS_ON -> Plugin Responsibility Matrix + current wp-content filesystem
  TRACKS -> Approved named components + exact observed absent installation state
  CONSTRAINS -> No replacement or unapproved package selection

Sprint 01B WordPress Baseline
  DEPENDS_ON -> Environment Report + Plugin Inventory + WordPress Solution Blueprint
  VALIDATES -> WordPress absent + database absent + permalink unverified
               + uploads local-owner writable + no theme/plugins installed

Sprint 01B Audit
  VALIDATES -> Mandatory installation stop + repository/Blueprint compliance
               + no pages/products/templates/customization/unauthorized implementation

Sprint 01C Hosting Validation Checklist
  DEPENDS_ON -> Sprint 01B Environment Report + Build Checklist + Pre-Implementation Checklist
  CLASSIFIES -> Verified + unknown + runtime-dependent + hosting-dependent + Founder actions
  GATES -> Future real hosting acceptance

Sprint 01C WordPress Installation Checklist
  DEPENDS_ON -> Hosting Validation Checklist + Rollback Plan + WordPress Blueprint
  GATES -> Future clean WordPress installation
  REQUIRES -> R0 + exact target/version/package + security/operations approval

Sprint 01C Plugin Installation Sequence
  DEPENDS_ON -> Accepted clean WordPress + Plugin Responsibility Matrix + Plugin Inventory
  ORDERS -> Blocksy + WooCommerce + Blocksy Pro + Elementor Pro conditionally
  STOPS_ON -> Missing exact package/dependency/license/compatibility/approval

Sprint 01C Post-Install Validation
  VALIDATES -> Versions + permalinks + uploads + theme + WooCommerce + Elementor
               + Blocksy + PHP extensions + security + performance
  REQUIRES -> Runtime evidence after each separately authorized stage

Sprint 01C Rollback Plan
  DEFINES -> R0 + R1 + R2 + R3 + R4 + R5 planned checkpoints
  REQUIRES -> External backup + integrity + isolated restore + independent acceptance
  DOES_NOT_PROVE -> Any backup, restore, or checkpoint currently exists

Sprint 01C Audit
  VALIDATES -> Evidence boundary + checklist coverage + dependency/rollback sequence
               + repository consistency + current NO-GO installation decision

Remote Access and Iran Execution Constraints Architecture
  DEPENDS_ON -> Repository Baseline + Engineering Guidelines + Implementation Readiness
                + Sprint 01B/01C evidence
  PROPOSES -> Private GitHub history + project-limited SSH primary candidate
              + conditional GitHub deployment/Actions + emergency cPanel fallback
  CONSTRAINS -> No root/shared access + no secrets + backup first + clean Git
                + validation + rollback + Founder approval
  DOES_NOT_PROVE -> GitHub remote + Server.ir capability + cPanel + SSH + path
                    + PHP CLI + WP-CLI + connectivity + backup/restore

Sprint 01D SSH Access Checklist
  DEPENDS_ON -> Remote Access Architecture + Hosting Validation + Access Policy + Rollback Plan
  GATES -> Future key creation + public-key registration + first connection + read-only inspection
  TRACKS -> Device + identity + host key + project path + PHP CLI + database method
            + WP-CLI + Git + permissions + redacted findings

Sprint 01D Deployment Access Policy
  CONSTRAINS -> Roles + access grant + change scope + approvals + forbidden actions
                + backup + rollback + secrets + emergency access
  DENIES_BY_DEFAULT -> Hosting + SSH + cPanel + GitHub deploy + WP-CLI + database access

Sprint 01D Iran Execution Risk Register
  TRACKS -> IR-001 through IR-012 with unknown likelihood
  REQUIRES -> Future dated path/provider/vendor evidence
  PRESERVES -> Package provenance + licensing + security + approval + rollback

Sprint 01D Audit
  VALIDATES -> Remote-access proposal + Iran constraints + Founder usability
               + security boundaries + repository consistency + no connection/implementation
```

## Dependency Rules

- Every governed node identifies its authority and lifecycle.
- Every rule links to origin, references, dependents, and evidence expectations.
- Every supporting node links to its governing node.
- Every unresolved node links to a register entry.
- Every historical node remains distinguishable from current authority.
- No relationship may imply implementation when implementation is not authorized.

## Cross-Reference Maintenance

When an authorized change adds, removes, supersedes, or changes the authority of a document:

1. Update the Documentation Index.
2. Update the Navigation Map and Reading Order when discovery changes.
3. Update the Traceability Matrix when rule or dependency paths change.
4. Update Decision and Founder registers when decision status changes.
5. Validate local links, anchors, authority direction, and orphan status.
6. Record the review evidence and lifecycle outcome.

## AI Interpretation Rules

- Resolve authority before summarizing a decision.
- Preserve lifecycle labels in generated context.
- Treat `TODO`, `Open`, and `Pending` as unknown, not implied approval.
- Prefer the shortest path to canonical authority.
- Do not infer missing graph edges from naming similarity.
- Report contradictions rather than selecting a preferred source.

## References

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Navigation Map](09_NAVIGATION_MAP.md)
- [Repository Metadata Standard](REPOSITORY_METADATA.md)
- [Traceability Matrix](TRACEABILITY_MATRIX.md)
- [Reading Order](READING_ORDER.md)
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
- [Blocksy Configuration Blueprint](36_BLOCKSY_CONFIGURATION.md)
- [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md)
- [WooCommerce Configuration Blueprint](38_WOOCOMMERCE_CONFIGURATION.md)
- [Custom Post Type Blueprint](39_CUSTOM_POST_TYPES.md)
- [Taxonomy Implementation Blueprint](40_TAXONOMY_IMPLEMENTATION.md)
- [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md)
- [Inquiry Workflow](42_INQUIRY_WORKFLOW.md)
- [User Roles](43_USER_ROLES.md)
- [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md)
- [Repository Baseline v1.0](BASELINE_v1.0.md)
- [Repository Release Notes v1.0](RELEASE_NOTES_v1.0.md)
- [Implementation Readiness Assessment](IMPLEMENTATION_READINESS.md)
- [Enterprise Sprint Roadmap](SPRINT_ROADMAP.md)
- [Enterprise Engineering Guidelines](ENGINEERING_GUIDELINES.md)
- [Repository Freeze v1.0 Audit](AUDIT_REPORT_FREEZE_v1.0.md)
- [Repository Implementation Rules](../repository/IMPLEMENTATION_RULES.md)
- [Repository Build Checklist](../repository/BUILD_CHECKLIST.md)
- [Pre-Implementation Checklist](../repository/PRE_IMPLEMENTATION_CHECKLIST.md)
- [Sprint 01A Audit](AUDIT_REPORT_SPRINT01A.md)
- [Sprint 01B Environment Report](../repository/config/ENVIRONMENT_REPORT.md)
- [Sprint 01B Plugin Inventory](../repository/config/PLUGIN_INVENTORY.md)
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

## Navigation

- [AI Collaboration Standard](AI_COLLABORATION.md)
- [Documentation Quality Standard](16_QUALITY_STANDARD.md)
