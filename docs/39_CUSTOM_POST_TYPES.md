# Custom Post Type Blueprint

## Document Control

- **Document ID:** `docs/39_CUSTOM_POST_TYPES.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Solution Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On logical content-type, entity, ownership, lifecycle, visibility, relationship, storage, or extension change
- **Lifecycle:** Review
- **Source of Truth:** [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), [Content Types](32_CONTENT_TYPES.md), and [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- **Dependencies:** [Content Architecture](29_CONTENT_ARCHITECTURE.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), [Content Types](32_CONTENT_TYPES.md), and [URL Architecture](26_URL_ARCHITECTURE.md)
- **Related Documents:** [Taxonomy Implementation Blueprint](40_TAXONOMY_IMPLEMENTATION.md), [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md), [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md), and [User Roles](43_USER_ROLES.md)
- **Traceability:** CP-001 through CP-007, CP-010, ERM-001 through ERM-008, CTYPE-001 through CTYPE-007, WPBP-005 through WPBP-007, and CPTBP-001 through CPTBP-008
- **AI Compatibility:** AI-readable Blueprint; no AI feature or content-type registration is authorized
- **Approval:** Pending Founder/content/technical approval; no CPT is approved for registration

## Purpose

Map approved logical content types to native WordPress/WooCommerce structures or gated CPT candidates without registering any content type.

## Scope and Boundary

Logical content/entity approval does not imply a CPT. This document identifies native defaults, candidate CPTs, required decisions, ownership, relationships, lifecycle, visibility, and future expansion. It defines no post-type keys, rewrite rules, labels, capabilities, templates, fields, or code.

## CPT Blueprint Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| CPTBP-001 | Prefer native WordPress/WooCommerce structures when they satisfy the approved entity contract. | Required by Plugin First and Configuration First |
| CPTBP-002 | Require a distinct lifecycle, ownership, permissions, relationships, query behavior, and Admin value before approving a CPT. | Proposed pending Founder approval |
| CPTBP-003 | Keep Products in WooCommerce `product`; no duplicate product CPT is permitted. | Derived from WordPress/WooCommerce architecture |
| CPTBP-004 | Keep standard Pages/landings/policies in native Pages unless an approved model proves otherwise. | Proposed pending Founder/content approval |
| CPTBP-005 | Treat Knowledge, FAQ, Representative, Project, and Technical Document as candidates, not registered structures. | Proposed pending Founder approval |
| CPTBP-006 | Do not use a CPT to represent Inquiry, Customer, Variation, taxonomy term, attribute term, media binary, ADR, decision, audit, or repository document by convenience. | Proposed pending Founder/technical approval |
| CPTBP-007 | Approve public archive, URL, search, schema, navigation, permissions, and migration behavior before registration. | Derived from IA/URL/SEO/content models |
| CPTBP-008 | Select a supported Plugin First registration/configuration owner only after the physical mapping is approved. | Required by CP-001 and CP-002 |

## Native Platform Mapping

| Logical entity/content type | Proposed native owner | CPT status | Rationale/boundary |
| --- | --- | --- | --- |
| Product / Variable Parent Product | WooCommerce `product` | No custom CPT | Canonical catalog owner |
| Variation | WooCommerce product variation primitive | No custom CPT | Child of product parent; not independent content |
| Page / Landing / Policy | WordPress Page | No custom CPT by default | Hierarchical editorial content; landing approval remains separate |
| Article / News / Announcement | WordPress Post or an approved native editorial mapping | No custom CPT by default | Exact shared/separate lifecycle and archive decision pending |
| Media Asset | WordPress Attachment plus approved media governance | No custom CPT by default | Binary and metadata ownership remain with Media Strategy |
| Category / Taxonomy / Attribute / Brand / Material / Finish | Approved taxonomy/attribute mechanism | Not a CPT | Classification entities follow Taxonomy Blueprint |
| ADR / Decision / Audit / repository Document | Repository Markdown | No WordPress CPT approved | Governance records remain repository-controlled |
| Inquiry / Customer | Approved protected inquiry capability | No CPT assumption | Privacy, workflow, access, retention, and integration determine storage |

## Candidate CPT Catalog

No candidate below is approved as required. Each candidate must pass CPTBP-002 and Founder review.

### Knowledge Candidate

- **Purpose:** Govern Knowledge Articles and possibly Guides when a dedicated lifecycle, archive, relationships, and search behavior are approved.
- **Owner:** TODO (Founder assignment required).
- **Relationships:** Topics, Products, taxonomies, media, documents, author/reviewer, related knowledge, inquiry/support.
- **Lifecycle:** Content lifecycle; exact transitions and permissions pending.
- **Visibility:** Public only after URL, archive, canonical, schema, search, and publication approval.
- **Future expansion:** Localization and approved structured relationships without changing entity identity.

### FAQ Candidate

- **Purpose:** Maintain governed question/answer entities only if reuse, relationship, review, and schema needs cannot be satisfied by approved content blocks.
- **Owner:** TODO (Founder assignment required).
- **Relationships:** Page/landing, Product, Knowledge, category, evidence, reviewer.
- **Lifecycle:** Content lifecycle with source and answer-review evidence.
- **Visibility:** Embedded or canonical behavior requires SEO approval; no automatic FAQ archive.
- **Future expansion:** Multiple placement through one canonical answer, not duplication.

### Representative Candidate

- **Purpose:** Govern representative profiles/scopes if public or internal representative entities are approved.
- **Owner:** TODO (Founder/Sales/privacy assignment required).
- **Relationships:** Location/coverage, Product Family, Industry, Inquiry assignment, media, organization.
- **Lifecycle:** Pending Sales/privacy rules; suspension must stop public display and routing as approved.
- **Visibility:** Protected by default until public fields, consent, URLs, schema, and directory behavior are approved.
- **Future expansion:** CRM identity mapping without exposing private data.

### Project Candidate

- **Purpose:** Govern approved project/case-study entities with consent, claims, media, and relationships.
- **Owner:** TODO (Founder/content/legal assignment required).
- **Relationships:** Products, Industry, Use Case, Location, Installation, media, documents, representative.
- **Lifecycle:** Content lifecycle plus consent/rights validity.
- **Visibility:** Private by default until publication and evidence review.
- **Future expansion:** Structured case-study views without making projects transactions.

### Technical Document Candidate

- **Purpose:** Govern document records only if Attachment metadata and content relationships cannot satisfy version, access, replacement, and review requirements.
- **Owner:** TODO (Founder/technical/content assignment required).
- **Relationships:** Media file, Product, Product Family, version, language, replacement, evidence, access class.
- **Lifecycle:** Document approval, effective, superseded, archived states require separate approval.
- **Visibility:** Determined per document and attachment; protected files remain inaccessible publicly.
- **Future expansion:** External document/DAM mapping through stable identity.

## Ownership and Administration

Each approved CPT requires business owner, content owner, technical configuration owner, reviewer, approval authority, permission map, Admin list columns, filters, validation, bulk-action limits, import/export, retention, and support runbook. A non-programmer must be able to perform normal operations without code or CLI.

## Relationships

Relationships use stable entity IDs and typed, directional contracts from the Entity Relationship Model. Template links, free-text names, tags, or duplicated fields do not establish canonical relationships. The physical relationship mechanism remains unselected.

## Lifecycle and Visibility

CPT lifecycle maps approved domain/content states onto supported WordPress workflow only after transition, role, scheduling, revision, suspension, archive, redirect, search, schema, cache, and relationship behavior are defined. `Published` does not automatically mean indexable, navigable, searchable, or schema-eligible.

## Future Expansion

New CPTs require evidence that native structures and approved plugins cannot satisfy the contract, plus exportability, migration, version compatibility, performance, accessibility, RTL/mobile Admin behavior, search/SEO, security/privacy, rollback, and retirement review.

## Founder Decisions

- Approve, revise, or reject CPTBP-001 through CPTBP-008.
- Decide which candidate entities, if any, justify CPT registration.
- Approve native mappings for editorial content and protected Inquiry/Customer storage boundaries.
- Assign owners, visibility, lifecycles, archives, URLs, roles, relationship capability, and registration capability.

## Open Questions

- Which logical content types require distinct WordPress storage and why?
- Can FAQ and Technical Document requirements be met through governed blocks/attachments instead of CPTs?
- Are Representative and Project entities required and public, protected, or absent in the initial scope?
- Which supported configuration capability can register approved structures without custom code?

## Approval Status

Review. No CPT, post-type key, rewrite, capability, field group, template, archive, or content record is registered or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 08 CPT decision Blueprint; documentation only. |

## Related Documents

- [Content Types](32_CONTENT_TYPES.md)
- [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- [Taxonomy Implementation Blueprint](40_TAXONOMY_IMPLEMENTATION.md)
- [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| CPTBP-001–CPTBP-008 | CP-001–CP-007, CP-010, ERM/CTYPE and IA/URL rules | Taxonomy, fields, Elementor, roles, plugins, and future content-structure plan | Native-vs-CPT analysis, owner/lifecycle/permissions matrix, URL/search/schema/privacy impact, Admin walkthrough, export/rollback evidence |

Implementation status: `Not authorized`.
