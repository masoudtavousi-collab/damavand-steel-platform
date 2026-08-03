# Product Family Template

## Document Control

- **Document ID:** `repository/engine/product/PRODUCT_FAMILY_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** Product Data Owner and Qualified Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 1.0.0
- **Last Updated:** 2026-08-03
- **Last Review:** 2026-08-03
- **Review Cycle:** On Product Engine family identity, lifecycle, parent strategy, pipeline, or template change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md) and approved canonical Product Repository sources; WooCommerce and Inquiry models constrain downstream projections only
- **Dependencies:** [Enterprise Product Engine](PRODUCT_ENGINE.md) and [Engine Rules](ENGINE_RULES.md)
- **Related Documents:** [Attribute Template](ATTRIBUTE_TEMPLATE.md), [Variation Template](VARIATION_TEMPLATE.md), [Import Template](IMPORT_TEMPLATE.md), [SEO Template](SEO_TEMPLATE.md), and [Validation Template](VALIDATION_TEMPLATE.md)
- **Traceability:** PDM-001 through PDM-008, WCM-001 through WCM-008, INQ-001 through INQ-008, Sprint 03D
- **AI Compatibility:** AI-readable reusable template; placeholders cannot be inferred or autonomously approved
- **Approval:** Pending Founder review; generated output remains Review until its family-specific gates pass

## Purpose

Provide the mandatory starting structure for every canonical `Catalog → Platform → Family → Series → Variant Rules → derived SKU` contract and its optional downstream legacy or commerce mappings. Copy this structure through the Generation Guide and replace placeholders only with sourced values or `TBD`.

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `PRODUCT_FAMILY_TEMPLATE` |
| Engine template version | `1.0.0` |
| Required generated provenance | `PRODUCT_ENGINE@1.0.0` and `PRODUCT_FAMILY_TEMPLATE@1.0.0` |
| Generated asset name | `{{FAMILY_KEY}}_PRODUCT_FAMILY.md` |
| Generated asset location | `repository/data/products/{{FAMILY_FOLDER}}/` |
| Unresolved placeholder policy | Replace with `TBD`; never guess |

## Required Generated Metadata

- Document ID: `{{GENERATED_DOCUMENT_ID}}`
- Status: `Draft` or `Review`
- Authority: `Product Data Asset`
- Owner: `{{OWNER_OR_TBD}}`
- Reviewer: `{{REVIEWER_OR_TBD}}`
- Approval Authority: `Founder`
- Version: `0.1.0`
- Last Updated / Last Review: `{{DATE}}`
- Source of Truth: `{{GOVERNING_SOURCES}}`
- Engine Template: `PRODUCT_FAMILY_TEMPLATE@1.0.0`
- Engine Package: `PRODUCT_ENGINE@1.0.0`
- Dependencies / Related Documents / Traceability / Approval: `{{VALUES_OR_TBD}}`

## Required Generated Sections

### Purpose

State why the family contract exists. Do not write marketing content or unsupported claims.

### Family Identity

| Field | Generated value | Evidence/status |
| --- | --- | --- |
| Catalog/Platform source IDs | `{{CATALOG_PLATFORM_IDS_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| Stable Family ID | `{{FAMILY_ID_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| Stable Series ID | `{{SERIES_ID_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| Variant Rule Set ID | `{{VARIANT_RULE_SET_ID_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| Persian family name | `{{FAMILY_NAME_FA_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| English family name | `{{FAMILY_NAME_EN_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| English internal key | `{{FAMILY_KEY_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| Legacy Product Family/Group/Type mapping | `{{LEGACY_MAPPING_OR_TBD}}` | Downstream only; never canonical hierarchy |
| Parent/Variation mapping strategy | `{{DOWNSTREAM_MAPPING_OR_TBD}}` | Presentation/commerce adapter only |
| Public-page slug | `TBD` until URL/SEO approval | Never infer from name automatically; never identity authority |

### Scope and Exclusions

Define inclusion/exclusion criteria, adjacent families, and concepts this family must not own. Unknown boundaries remain `TBD`.

### Business Purpose

Describe approved inquiry/discovery purpose only. Do not add prices, stock, supplier data, warranties, certifications, or suitability claims.

### Downstream Parent Presentation Strategy

Define optional adapter-only Parent/Variation IDs, shared presentation fields, downstream category relationship, public page/URL/search-intent ownership proposal, and projection-specific overrides. Never assign Product Repository identity or fact authority.

### Variable Product Strategy

Project only allowed values, axes, and valid tuples referenced by the canonical Variant Rule Set through the generated Attribute and Variation assets. Never enumerate a Cartesian product as approved products.

### Inquiry Behavior

Require `inquiry_only=yes`; define the permitted product/variation context and prohibit cart, checkout, payment, public quote result, or automated pricing.

### No-Public-Price Behavior

Require empty public-price fields and prohibit zero/free/sentinel substitutes, price schema, feeds, analytics events, and transactional paths.

### Mobile Persian RTL Behavior

Record Persian labels, technical-token policy, mobile selection order, units, invalid-combination handling, and accessibility review needs.

### WooCommerce Mapping Summary

Reference downstream category, global-attribute, Variable Parent Product, Variation, inquiry, and no-price mappings. Runtime IDs/settings remain `TBD`, adapter-only, and separately approved.

### SEO Role

Record candidate public page/URL/search-intent owner, canonical-URL boundary, attribute/facet boundary, content evidence, and unresolved slug/indexation decisions without transferring Product Repository identity.

### CRM/Integration Relevance

List permitted stable references/snapshots and protected/internal fields. CRM/ERP/CentralSteel never become authority by copying values.

### Known Unknowns

List every unresolved canonical source reference, downstream mapping ID, field, Variant Rules allowed value/tuple, owner, URL, SEO, CRM, runtime, recovery, and approval item as `TBD`.

### Founder Approval Gates

List canonical source, downstream mapping, terminology, classification, Variant Rules, UX, SEO, CRM, import/runtime, and release decisions requiring Founder approval.

### Change Notes

Record template version, generated asset version, date, scope, compatibility, and approval impact.

## Completion Rules

- No placeholder token may survive in a review-ready generated asset; replace unresolved tokens with explicit `TBD`.
- `TBD` may remain in Review but blocks the lifecycle transition it affects.
- Every value names its evidence/owner or remains unknown.
- All downstream family assets must reference the same family ID/key and template version.
- Completion does not authorize product creation or import.

## Compatibility and Provenance

Version `1.0.0` is a major required-structure and semantic change because it replaces legacy hierarchy/identity fields with required canonical source references and explicit downstream mappings. Its compatibility impact is breaking for every Family with a generated 0.x Family asset. Before use, a separately authorized migration or regeneration task must record the affected-Family/asset inventory, exact engine/template provenance, migration and validation plan, diff review, full validation, and Founder approval. No existing Family asset is migrated or approved here.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03D Product Family template. |
| 1.0.0 | 2026-08-03 | Major canonical-source contract: added Catalog/Platform/Family/Series/Variant Rules provenance and limited legacy Product Family/Group/Type and Parent/Variation to downstream mappings. |

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
- [Attribute Template](ATTRIBUTE_TEMPLATE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
