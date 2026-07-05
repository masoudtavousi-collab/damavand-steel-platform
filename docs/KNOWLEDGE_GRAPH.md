# Repository Knowledge Graph

## Document Control

- **Document ID:** `docs/KNOWLEDGE_GRAPH.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.2
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
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

Sprint 03A Stainless Steel Pipe Product Family
  DEPENDS_ON -> Product Data Model + WooCommerce Product Model + Attribute Dictionary
  DEFINES -> Family/parent candidate + inquiry-only + no-price + UX + SEO + CRM boundaries
  DOES_NOT_DEFINE -> Final IDs/SKUs + stock + supplier + price + commercial combinations

Sprint 03A Attribute Dictionary
  DEPENDS_ON -> Product Attribute Model + Pipe Product Family
  DEFINES -> 16 typed attributes + pipe profile + controlled Sprint 03A values
  CONSTRAINS -> Global reuse + finite variation axes + no silent term creation

Sprint 03A Pipe Variation Matrix
  DEPENDS_ON -> Pipe Product Family + Attribute Dictionary + WooCommerce Product Model
  DEFINES -> Grade + Finish + Diameter + Thickness + Length candidate sets
  CALCULATES -> 1,584 theoretical tuples
  DOES_NOT_PROVE -> Technical validity + supply + stock + price + final SKU

Sprint 03A WooCommerce Pipe Import Template
  DEPENDS_ON -> Pipe Family + Variation Matrix + Validation Rules
  CONTAINS -> One placeholder parent + three placeholder variations + empty public prices
  BLOCKED_BY -> TBD SKUs + TBD stock + TBD canonical slugs + unapproved mapping/combinations

Sprint 03A Pipe SEO Entity Model
  DEPENDS_ON -> SEO Entity Model + URL Architecture + Pipe Product Family
  CONSTRAINS -> Parent canonical + non-canonical variation state + no-price schema

Sprint 03A Product Data Validation Rules
  VALIDATES -> Fields + values + slugs + Persian naming + SKUs + duplicates
               + parent/variation consistency + no-price + import safety
  REQUIRES -> Founder/domain gates + dry run + backup/restore + rollback

Sprint 03A Audit
  VALIDATES -> Structure + dictionary + family + CSV + Inquiry First
               + No Public Pricing + variable product + SEO + TBD boundaries

Sprint 03B Pipe WooCommerce Mapping
  DEPENDS_ON -> Pipe Product Family + Variation Matrix + Attribute Dictionary + WCM/WCCFG
  MAPS -> Variable parent + variation + global attributes + inquiry + no-price + stock boundary
  DOES_NOT_CONFIGURE -> WordPress + WooCommerce + attributes + terms + products

Sprint 03B Pipe Import Mapping
  DEPENDS_ON -> 23-column CSV + Pipe WooCommerce Mapping + Validation Rules
  MAPS -> All 23 columns to logical destinations/status/rules/blockers
  PROHIBITS -> Public price target + silent term creation + default commercial state

Sprint 03B Pipe Import Precheck
  VALIDATES -> Static CSV shape + parent/variation shape + inquiry/no-price
  BLOCKED_BY -> TBD SKUs + combinations + stock + taxonomy/terms/slug + runtime/recovery/approval
  DECIDES -> NO-GO for import

Sprint 03C Pipe Taxonomy and Attribute Classification
  DEPENDS_ON -> Sprint 03A/03B Pipe contracts + TAX + ATT + FIELD + SEOENT + INQ
  CLASSIFIES -> 29 unique fields exactly once
  SEPARATES -> Category + global/variation attributes + custom + CRM + SEO + helper + internal + excluded

Sprint 03C Pipe Category Model
  DEFINES -> One candidate Product Family category + no approved subcategory
  EXCLUDES -> Grade + Finish + dimensions + other attributes from category authority
  RETAINS_TBD -> Higher parent + stable ID + approved public slug + indexation/canonical

Sprint 03C Pipe Attribute Model
  DEFINES -> 14 global attributes + 5 variation/filter axes + zero local attributes
  PRESERVES -> Controlled values + mobile Persian RTL order + no automatic indexable facets
  RETAINS_TBD -> Optional registries + valid combinations + runtime IDs/terms

Sprint 03C Pipe Data Governance Checklist
  GATES -> Founder + domain + attribute + category + import + price + inquiry + SEO + CRM + WooCommerce
  REJECTS -> Multiple/no classification + local/category duplicates + invented values + unauthorized implementation
  DECIDES -> GO for review; NO-GO for implementation/import

Sprint 03C Audit
  VALIDATES -> Classification + category + attributes + variations + filters + SEO + CRM
               + Inquiry First + No Public Pricing + remaining TBDs + scope boundaries

Sprint 03D Enterprise Product Engine
  DEPENDS_ON -> Governing product + taxonomy + attribute + inquiry + SEO + field + plugin + repository rules
  DEFINES -> Template-first generation philosophy + lifecycle + inputs/outputs + approval + logical pipelines
  IS_SOURCE_OF_TRUTH_FOR -> Generation structure + template provenance + engine workflow
  IS_NOT_AUTHORITY_FOR -> Business facts + domain values + commercial data + runtime configuration

Sprint 03D Six Templates
  CONTAINS -> Product Family + Attribute + Variation + Import + SEO + Validation templates
  GENERATES -> One coordinated source-backed family asset set
  PROHIBITS -> Family-value copying + guessing + runtime mutation + product creation

Sprint 03D Engine Rules
  GOVERNS -> Naming + versioning + folders + provenance + reviews + approvals
             + change control + backward compatibility + repository conventions
  PRESERVES -> Pipe example + stable authorities + no handwritten blank-start family assets

Sprint 03D Engine Workflow
  SEQUENCES -> Idea -> Family -> Attributes -> Variations -> Validation
               -> Import -> WooCommerce -> SEO -> QA -> Release
  REQUIRES -> Stage-scoped evidence + handoff + approval + stop conditions

Sprint 03D Engine Generation Guide
  ORCHESTRATES -> Intake + identity + six templates + cross-asset review + regeneration
  APPLIES_TO -> Pipe + Profile + Fittings + Glass Hardware + Pool Equipment
                + Wood + Fasteners + Tools + Accessories + future families
  DOES_NOT_GENERATE -> Unapproved family facts + prices + stock + suppliers + final SKUs

Sprint 03D Audit
  VALIDATES -> Engine completeness + reusability + scalability + no duplication
               + repository readiness + Pipe example boundary + no implementation

Sprint 03E Platform Manifest
  DEPENDS_ON -> Accepted Founder decisions + CP-001..CP-010 + ADR-0001 + Constitution
  PROPOSES -> Highest Platform architectural authority after explicit Founder approval
  DEFINES -> Purpose + vision + mission + principles + layers + scopes + evolution + metrics
  DOES_NOT_OVERRIDE -> Founder/business/Core Principle/ADR authority

Sprint 03E Platform Principles
  INHERITS -> Plugin/Configuration/Mobile/RTL/Inquiry/No-price + prohibited technologies
  ADDS_FOR_REVIEW -> Repository/Data/Knowledge/Engine/Template First + runtime replaceability
  REQUIRES -> Single scoped truth + ownership + reversibility + maintainability

Sprint 03E Platform Architecture
  SEQUENCES -> Platform -> Repository -> Engines -> Runtime -> Website
  PERMITS_FEEDBACK_AS -> Evidence and correction proposals
  PROHIBITS -> Reverse authority + runtime-as-platform-truth + website forks
  SUPPORTS -> WordPress replacement + multiple website consumers

Sprint 03E Engine Boundaries
  REGISTERS -> Product + Content + SEO + Commerce + Integration + Media + Analytics + Knowledge
  REQUIRES_PER_ENGINE -> Purpose + inputs + outputs + dependencies + ownership
                         + change + approval + future expansion
  CURRENT_STATE -> Product Engine Review; seven additional boundaries conceptual

Sprint 03E Platform Lifecycle
  SEQUENCES -> Idea -> Founder Decision -> Repository -> Engine -> Validation
               -> Implementation -> QA -> Release -> Maintenance -> Evolution -> Deprecation
  ENFORCES -> Stage-scoped GO + upstream correction + no downstream authority patching

Sprint 03E Platform Governance
  SEPARATES -> Founder Authority + Architecture Authority + Build Authority + review + operations
  GOVERNS -> Approval + change + risk + freeze + release + rollback + documentation

Sprint 03E Directory Standard
  MAPS -> Platform + Repository + Engine + Runtime + WordPress + Knowledge
          + imports + exports + backups + validation to existing physical boundaries
  CREATES_NOW -> repository/platform only
  PROHIBITS -> Duplicate authority + secrets/runtime payloads + implied restructuring

Sprint 03E Platform Versioning
  SEPARATES -> Platform + Repository + Engine + Template + Data + Release + Migration versions
  PRESERVES -> Repository v1.0.0 baseline + authority/lifecycle independence
  BLOCKS -> Unknown compatibility

Sprint 03E Platform Evolution
  EXTENDS_THROUGH -> Existing Engine + new admitted Engine + Runtime adapter + Website consumer
  EXAMPLES -> AI + Translation + Marketplace + ERP + PIM + Customer Portal + API
  PRESERVES -> CP-010 Phase 1 prohibition + Inquiry First + No Public Pricing

Sprint 03E Audit
  VALIDATES -> Platform completeness + architecture/boundary/repository/engine consistency
               + governance + scalability + runtime replacement + future readiness
  DOES_NOT_APPROVE -> Platform Constitution + Engines + Runtime + Website + implementation

Sprint 04A Infrastructure Audit
  DEPENDS_ON -> Sprint 02C evidence + current task findings + Platform/WordPress/plugin boundaries
  OBSERVES -> REST cURL 28/10s + WordPress.org failure + SMTP incomplete
              + Rank Math URL reconnect pending + Coming Soon expected
  SEPARATES -> Verified + prior verified + inference + possible cause + pending evidence
  DOES_NOT_CLAIM -> Root cause + current unrefreshed TLS state + production readiness

Sprint 04A REST API Diagnostic
  MAPS -> Site Health/caller -> WordPress HTTP API -> cURL -> DNS -> IPv4/IPv6
          -> route/firewall/loopback -> TLS -> LiteSpeed/WAF -> PHP/plugins -> REST response
  INVESTIGATES -> DNS + firewall + CloudLinux + ModSecurity + LiteSpeed + cache + cron
                  + plugins + cURL/OpenSSL/CA + internal DNS + HTTP API policy
  DOES_NOT_EXECUTE -> Request + plugin isolation + setting/server change

Sprint 04A Connectivity Audit
  MAPS -> api.wordpress.org + outbound HTTP(S) + DNS + TLS/certificates + firewall + ports
  REQUIRES -> Existing support/Admin evidence due shared hosting + SSH/shell NO-GO
  CORRELATES -> REST + WordPress.org only as unproven shared-connectivity hypothesis

Sprint 04A Remediation Plan
  PRIORITIZES -> Critical + High + Medium + Low evidence/remediation gates
  GATES -> Root cause + backup/restore + staging + one-variable change + validation + approval
  PRESERVES -> Coming Soon + no LiteSpeed Cache + no production experiment
  DECIDES -> Read-only evidence GO; remediation/WooCommerce implementation NO-GO

Sprint 04A Audit
  VALIDATES -> Documentation completeness + evidence completeness + unknowns + risks
               + read-only scope + repository consistency + go/no-go

Sprint 04B Audit
  RECORDS -> Evidence-limited WordPress audit + authenticated-access boundary
  DOES_NOT_AUTHORIZE -> Runtime inspection beyond supplied evidence + remediation

Sprint 04B Authenticated Audit
  REFINES -> WordPress + plugin + theme + content + commerce + SEO + security + operations evidence
  DOES_NOT_AUTHORIZE -> Save + install + update + delete + configure + reconnect + optimize

Master Remediation Roadmap
  DEPENDS_ON -> Sprint 02A-02C + Sprint 03A-03E + Sprint 04A + Sprint 04B + Authenticated Audit
  REGISTERS -> RM-001-RM-046 with one classification + one primary group + complete planning fields
  DOES_NOT_AUTHORIZE -> Remediation + WooCommerce production + runtime mutation

Implementation Sequence
  ORDERS -> Evidence + approvals + recovery + staging + infrastructure + runtime + business rules
            + platform components + WooCommerce + Product Data + CRM + content/SEO + release
  REQUIRES -> Applicable Execution Gates passed before each phase

Execution Gates
  DEFINES -> G00-G14 evidence + approval + pass/fail + stop conditions
  BLOCKS -> Implementation while any applicable gate is unpassed

Sprint 04C Audit
  VALIDATES -> Planning completeness + classification + grouping + navigation + traceability + scope
  DOES_NOT_APPROVE -> Any remediation + configuration + installation + production implementation

Sprint 05A Design Decisions
  DEPENDS_ON -> CP-001-CP-010 + WordPress/Blocksy/Elementor Blueprints + Founder direction
  CONTAINS -> DDR-0001 + DDR-0002 + DDR-0003 + DDR-0004
  PRESERVES -> ReactBits inspiration-only + 85/10/5 + industrial premium + native delivery

Design Manifest + Brand Language
  DEFINE -> Visual philosophy + trust + B2B + Persian RTL + Mobile First + restraint
  DO_NOT_DEFINE -> Final tokens + product facts + public content + runtime configuration

Motion System + ReactBits Inspiration Mapping
  MAP -> 15 named inspiration concepts to allowed/forbidden use + mobile/RTL + accessibility + performance
  EXCLUDE -> React + ReactBits package/source/runtime + production CSS/JS

Component Pattern Library + Animation Library
  DEFINE -> 14 component contracts + 12 animation contracts
  DEPEND_ON -> Canonical content/data + singular Blocksy/Elementor ownership + approval gates

Performance Rules + Accessibility Rules
  GATE -> Dependencies + Core Web Vitals + assets + reduced motion + contrast + keyboard + RTL + human validation
  BLOCK -> Unmeasured or inaccessible future implementation

Sprint 05A Audit
  VALIDATES -> Design/motion completeness + dependency safety + platform compatibility
               + performance + accessibility + Persian RTL + B2B + repository-only scope
  DOES_NOT_APPROVE -> WordPress + Elementor + Blocksy + page + template + CSS + JavaScript + runtime dependency
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

## Navigation

- [AI Collaboration Standard](AI_COLLABORATION.md)
- [Documentation Quality Standard](16_QUALITY_STANDARD.md)
