# Custom Fields Model Blueprint

## Document Control

- **Document ID:** `docs/41_CUSTOM_FIELDS_MODEL.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Solution Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On entity, field, validation, relationship, Admin, privacy, migration, or source-authority change
- **Lifecycle:** Review
- **Source of Truth:** [Product Data Model](19_PRODUCT_DATA_MODEL.md), [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), and [Content Types](32_CONTENT_TYPES.md)
- **Dependencies:** [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md), [Custom Post Type Blueprint](39_CUSTOM_POST_TYPES.md), and [Taxonomy Implementation Blueprint](40_TAXONOMY_IMPLEMENTATION.md)
- **Related Documents:** [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md), [Inquiry Workflow](42_INQUIRY_WORKFLOW.md), [User Roles](43_USER_ROLES.md), [Media Strategy](33_MEDIA_STRATEGY.md), and [SEO Entity Model](34_SEO_ENTITY_MODEL.md)
- **Traceability:** CP-001 through CP-006, CP-010, PDM/WCM/TAX/ATT/INQ, ERM-001 through ERM-008, CTYPE-001 through CTYPE-007, and FIELD-001 through FIELD-009
- **AI Compatibility:** AI-readable Blueprint; no AI feature, ACF group, field, or storage configuration is authorized
- **Approval:** Pending Founder/domain/content/privacy/technical approval; no custom field implementation is authorized

## Purpose

Define logical field groups, ownership, validation, administration, relationships, and migration boundaries without implementing ACF or any field capability.

## Scope and Boundary

This model describes data contracts, not database schema, meta keys, UI, plugin selection, or field creation. Native WordPress/WooCommerce fields, taxonomies, attributes, relationships, and external authorities are preferred before custom fields.

## Field Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| FIELD-001 | Use a custom field only when an approved entity contract is not satisfied by a native field, taxonomy, attribute, or relationship. | Required by Configuration First |
| FIELD-002 | Assign every field one canonical owner, type, cardinality, requiredness, validation, access class, lifecycle, and migration rule. | Proposed pending Founder approval |
| FIELD-003 | Store relationships by stable entity reference, not copied labels or URLs. | Derived from ERM rules |
| FIELD-004 | Keep reusable business/product facts in canonical source fields, not Elementor/Blocksy template settings. | Proposed pending Founder approval |
| FIELD-005 | Separate public, protected, internal, derived, integration-only, and secret data; secrets are never content fields. | Required by security/privacy boundaries |
| FIELD-006 | Conditional entities and CPTs do not receive fields until their existence and physical mapping are approved. | Proposed pending Founder approval |
| FIELD-007 | Requiredness depends on entity type, lifecycle state, and publication/inquiry transition; unknown values are not fabricated. | Proposed pending Founder/domain approval |
| FIELD-008 | No ACF product or implementation is assumed; select a supported Plugin First capability only after approval. | Required by CP-001 and CP-002 |
| FIELD-009 | Preserve stable semantics and exportable values across future plugin, CRM, ERP, DAM, or CentralSteel migration. | Proposed pending Founder/technical approval |

## Common Field Contract

Every approved field definition records: stable logical ID; label; description; entity/type; owner; source authority; data type; cardinality; required condition; allowed values/format/unit; default/null behavior; validation; access class; edit/view roles; localization; lifecycle; relationships; search/filter/SEO/schema eligibility; import/export key; external mapping; migration; and deprecation/replacement.

## Proposed Field Groups

| Logical group | Applies to | Required field families | Optional field families | Owner/boundary |
| --- | --- | --- | --- | --- |
| Entity governance | Every managed entity | Stable ID, owner, lifecycle, source, language, access, review | External IDs, replacement | Entity owner; native values preferred |
| Editorial content | Page, Landing, Knowledge, FAQ, Guide, Policy, News, Announcement | Purpose/type, owner, lifecycle, source, audience | Summary, relationships, review/expiry | Content owner |
| Product supplemental | Product parent/variation | Only approved PDM fields not native to WooCommerce | Approved technical/document/CRM/ERP references | Product authority; never duplicate native attributes/SKUs |
| Classification term | Approved taxonomy/attribute term | Stable identity, label/key, definition, owner, lifecycle | aliases, external mappings, landing relation | Taxonomy/attribute authority |
| Media and document | Attachment/Document entity | Media ID, role, rights, access, language, lifecycle, source | caption, alt, derivatives, replacement, relations | Media/document authority |
| Representative | Conditional Representative entity | Identity/scope/owner/lifecycle/access only after approval | public profile, coverage, relations | Protected by default; Sales/privacy authority |
| Project/Installation/Location | Conditional entities | Identity, owner, lifecycle, evidence/access after approval | public narrative, relations, media | Private by default; consent/claims required |
| Inquiry | Canonical Inquiry object | Approved INQ required fields/status/context/consent | approved optional context/attachments | Protected Inquiry authority; not public post meta by assumption |
| SEO projection | Public eligible entity | Canonical ownership and approved metadata references | social/search presentation | SEO owner; no competing source or price data |
| Integration mapping | Approved entities | Stable local/external IDs, source, sync state/version | retry/error evidence | Integration-specific; not public |

## Ownership

Field-value ownership follows the source entity: Product/domain owners govern specifications; Taxonomy owners govern terms; Content owners govern editorial fields; Media owners govern rights/access; Sales/privacy owners govern protected Inquiry/Representative data; SEO governs projections, not underlying facts; technical administrators govern configuration but cannot approve values.

## Validation

- Validate type, format, cardinality, allowed vocabulary, unit, range, precision, script/language, relationship target, lifecycle, access, and required condition.
- Reject duplicate authority, invalid relationships, stale external references, unsafe markup, secret values, public pricing, and protected-data exposure.
- Required-field failure blocks the applicable transition; optional absence renders an approved fallback or no output.
- Derived values identify source fields and deterministic rule; manual overrides require explicit authority.

## Required and Optional Fields

No exact project field is approved solely by appearing in this Blueprint. A field becomes required only through its governing entity/product/content/inquiry contract and a Founder-approved physical mapping. Optional fields must have a defined purpose and absence behavior; “optional” is not permission for uncontrolled data.

## Relationships

Relationship fields use stable target identity, relationship type, direction, source, owner, lifecycle, access class, and evidence when they imply claims. Bidirectional display does not require duplicated storage. The supported relationship mechanism remains unselected.

## Administration

- Group fields by user task and reveal advanced/integration fields only to authorized roles.
- Use Persian labels/help where appropriate while retaining stable English internal identifiers.
- Provide validation messages, controlled vocabularies, safe defaults, revision evidence, filters, and meaningful Admin columns.
- Prevent routine editors from changing IDs, authority, integration state, or protected controls.
- Keep normal workflows manageable without code or CLI.

## Future Migration

Migration plans require source/target schema, stable key mapping, transformations, term/entity resolution, localization/unit handling, protected-data controls, dry run, validation, error report, rollback, audit, and dual-write prohibition. Plugin-specific storage is not treated as the domain contract.

## Founder Decisions

- Approve, revise, or reject FIELD-001 through FIELD-009.
- Approve exact field inventory, requiredness, values, types, access, labels, validation, and source owners per approved entity.
- Approve physical field/relationship capability and migration/export requirements.
- Assign domain, content, privacy/security, SEO, integration, configuration, and review owners.

## Open Questions

- Which approved fields are not satisfied by native WordPress/WooCommerce structures?
- Which candidate entities/CPTs exist, and what fields are required at each lifecycle transition?
- Which fields are public, protected, internal, derived, integration-only, or prohibited?
- Which supported field/relationship capability meets export, Admin, version, security, RTL, and rollback requirements?

## Approval Status

Review. No ACF, field group, field, meta key, relationship, database schema, validation rule, UI, import, or migration is created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 08 custom fields model Blueprint; documentation only. |

## Related Documents

- [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- [Custom Post Type Blueprint](39_CUSTOM_POST_TYPES.md)
- [Taxonomy Implementation Blueprint](40_TAXONOMY_IMPLEMENTATION.md)
- [Inquiry Workflow](42_INQUIRY_WORKFLOW.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| FIELD-001–FIELD-009 | CP-001–CP-006, CP-010, PDM/WCM/TAX/ATT/INQ, ERM/CTYPE/MEDIA/SEOENT | Elementor, inquiry, roles, plugins, imports/integrations, and future field configuration plan | Field dictionary, owner/access/validation matrix, native-vs-custom analysis, Admin walkthrough, export/migration/rollback evidence |

Implementation status: `Not authorized`.
