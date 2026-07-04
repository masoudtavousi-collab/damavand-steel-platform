# Product Family Template

## Document Control

- **Document ID:** `repository/engine/product/PRODUCT_FAMILY_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** Product Data Owner and Qualified Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On Product Engine family identity, lifecycle, parent strategy, pipeline, or template change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md) and approved Product Data/WooCommerce/Inquiry models
- **Dependencies:** [Enterprise Product Engine](PRODUCT_ENGINE.md) and [Engine Rules](ENGINE_RULES.md)
- **Related Documents:** [Attribute Template](ATTRIBUTE_TEMPLATE.md), [Variation Template](VARIATION_TEMPLATE.md), [Import Template](IMPORT_TEMPLATE.md), [SEO Template](SEO_TEMPLATE.md), and [Validation Template](VALIDATION_TEMPLATE.md)
- **Traceability:** PDM-001 through PDM-008, WCM-001 through WCM-008, INQ-001 through INQ-008, Sprint 03D
- **AI Compatibility:** AI-readable reusable template; placeholders cannot be inferred or autonomously approved
- **Approval:** Pending Founder review; generated output remains Review until its family-specific gates pass

## Purpose

Provide the mandatory starting structure for every new Product Family contract. Copy this structure through the Generation Guide and replace placeholders only with sourced values or `TBD`.

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `PRODUCT_FAMILY_TEMPLATE` |
| Engine template version | `0.1.0` |
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
- Engine Template: `PRODUCT_FAMILY_TEMPLATE@0.1.0`
- Dependencies / Related Documents / Traceability / Approval: `{{VALUES_OR_TBD}}`

## Required Generated Sections

### Purpose

State why the family contract exists. Do not write marketing content or unsupported claims.

### Family Identity

| Field | Generated value | Evidence/status |
| --- | --- | --- |
| Stable family ID | `{{FAMILY_ID_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| Persian family name | `{{FAMILY_NAME_FA_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| English family name | `{{FAMILY_NAME_EN_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| English internal key | `{{FAMILY_KEY_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| Product Group | `{{PRODUCT_GROUP_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| Product Type(s) | `{{PRODUCT_TYPES_OR_TBD}}` | `{{SOURCE_OR_TBD}}` |
| Parent strategy | Variable Parent Product | Governing rule; exception requires approval |
| Public slug | `TBD` until URL/SEO approval | Never infer from name automatically |

### Scope and Exclusions

Define inclusion/exclusion criteria, adjacent families, and concepts this family must not own. Unknown boundaries remain `TBD`.

### Business Purpose

Describe approved inquiry/discovery purpose only. Do not add prices, stock, supplier data, warranties, certifications, or suitability claims.

### Parent Product Strategy

Define parent identity, shared fields, category relationship, canonical ownership proposal, and fields that must remain variation-specific. Record all unresolved choices.

### Variable Product Strategy

List candidate variation axes by reference to the generated Attribute and Variation assets. Never enumerate a Cartesian product as approved products.

### Inquiry Behavior

Require `inquiry_only=yes`; define the permitted product/variation context and prohibit cart, checkout, payment, public quote result, or automated pricing.

### No-Public-Price Behavior

Require empty public-price fields and prohibit zero/free/sentinel substitutes, price schema, feeds, analytics events, and transactional paths.

### Mobile Persian RTL Behavior

Record Persian labels, technical-token policy, mobile selection order, units, invalid-combination handling, and accessibility review needs.

### WooCommerce Mapping Summary

Reference logical category, global attributes, Variable Parent Product, variations, inquiry, and no-price behavior. Runtime IDs/settings remain `TBD` until separately approved.

### SEO Role

Record candidate intent owner, canonical boundary, attribute/facet boundary, content evidence, and unresolved slug/indexation decisions.

### CRM/Integration Relevance

List permitted stable references/snapshots and protected/internal fields. CRM/ERP/CentralSteel never become authority by copying values.

### Known Unknowns

List every unresolved identity, hierarchy, field, value, combination, owner, URL, SEO, CRM, runtime, recovery, and approval item as `TBD`.

### Founder Approval Gates

List identity, hierarchy, terminology, classification, combinations, UX, SEO, CRM, import/runtime, and release decisions requiring Founder approval.

### Change Notes

Record template version, generated asset version, date, scope, compatibility, and approval impact.

## Completion Rules

- No placeholder token may survive in a review-ready generated asset; replace unresolved tokens with explicit `TBD`.
- `TBD` may remain in Review but blocks the lifecycle transition it affects.
- Every value names its evidence/owner or remains unknown.
- All downstream family assets must reference the same family ID/key and template version.
- Completion does not authorize product creation or import.

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
- [Attribute Template](ATTRIBUTE_TEMPLATE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
