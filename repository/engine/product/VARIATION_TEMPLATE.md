# Product Variation Template

## Document Control

- **Document ID:** `repository/engine/product/VARIATION_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Qualified Domain Reviewer, Sales/Operations Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On variation axis, value, combination, identity, display, lifecycle, or template change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md), generated Product Family/Attribute assets, and approved WooCommerce Product Model
- **Dependencies:** [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md), [Attribute Template](ATTRIBUTE_TEMPLATE.md), and [Engine Rules](ENGINE_RULES.md)
- **Related Documents:** [Import Template](IMPORT_TEMPLATE.md), [Validation Template](VALIDATION_TEMPLATE.md), and [Engine Workflow](ENGINE_WORKFLOW.md)
- **Traceability:** PDM-001 through PDM-008, WCM-001 through WCM-008, ATT-001 through ATT-007, Sprint 03D
- **AI Compatibility:** AI-readable reusable template; no autonomous combination expansion, commercial inference, or SKU generation
- **Approval:** Pending Founder review; no variation or combination is approved by template completion

## Purpose

Generate a controlled family-specific variation contract for the approved Variable Parent Product architecture without treating candidate values as commercially valid products.

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `VARIATION_TEMPLATE` |
| Engine template version | `0.1.0` |
| Generated asset name | `{{FAMILY_KEY}}_VARIATION_MODEL.md` |
| Generated asset location | `repository/data/products/{{FAMILY_FOLDER}}/` |

## Parent Contract

| Property | Placeholder/rule |
| --- | --- |
| Stable parent ID | `{{PARENT_ID_OR_TBD}}` |
| Parent key/SKU | `TBD` until separately approved; never generate a final SKU |
| Parent type | Variable Parent Product |
| Shared family/category | `{{APPROVED_REFERENCE_OR_TBD}}` |
| Declared variation axes | `{{APPROVED_AXIS_LIST_OR_TBD}}` |
| Inquiry behavior | Required |
| Public pricing | Prohibited |
| Canonical owner | Parent by default; SEO approval required |

## Axis Definition Template

| Order | Axis | Attribute ID/key | Unit | Allowed values source | Filter | Public label | Domain reviewer | Status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{ORDER}}` | `{{AXIS_NAME}}` | `{{GLOBAL_ATTRIBUTE_KEY}}` | `{{UNIT_OR_NONE}}` | `{{REGISTRY_REFERENCE_OR_TBD}}` | Yes/No | `{{LABEL_FA_OR_TBD}}` | `{{REVIEWER_OR_TBD}}` | Draft/Review/Approved |

Only fields classified as WooCommerce Variation Attribute may appear as axes.

## Controlled Value Template

| Axis | Stable value key | Persian label | English label | Unit/format | Evidence | Lifecycle | Commercial validity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{AXIS}}` | `{{VALUE_KEY_OR_TBD}}` | `{{LABEL_FA_OR_TBD}}` | `{{LABEL_EN_OR_TBD}}` | `{{RULE_OR_TBD}}` | `{{SOURCE_OR_TBD}}` | Review | `TBD` until approved |

No Pipe values or generic sample values may be copied into a new family without independent family evidence.

## Valid-Combination Template

| Combination ID | Parent ID | Axis tuple | Domain evidence | Commercial evidence | Lifecycle | Import eligible |
| --- | --- | --- | --- | --- | --- | --- |
| `TBD` | `{{PARENT_ID_OR_TBD}}` | `{{ONE_VALUE_PER_AXIS_OR_TBD}}` | `{{SOURCE_OR_TBD}}` | `TBD` | Review | No |

Candidate allowed-value sets do not establish valid combinations. Never generate the Cartesian product automatically. Each accepted tuple requires domain review, stable identity, commercial evidence, lifecycle approval, and duplicate checks.

## Identity and Duplicate Rules

- One variation belongs to exactly one parent.
- One approved tuple identifies at most one active variation under that parent.
- Stable variation ID and final SKU remain separate and require later approval.
- Placeholder IDs/SKUs cannot pass import readiness.
- Duplicate checks cover active, archived, legacy, external, CRM, ERP, and CentralSteel mappings where evidence exists.
- Axis/value changes never silently overwrite another variation identity.

## Display and UX Template

Record:

- Mobile Persian RTL axis order.
- Persian label pattern derived from structured values.
- English Admin/reference pattern.
- Unit and precision display.
- Missing/invalid/unavailable-combination behavior.
- Default-selection decision, normally none until approved.
- Inquiry action/context after valid selection.
- Accessibility and performance review needs.

Display labels are not SKUs, canonical slugs, or identity keys.

## Inquiry and No-Price Rules

- Every parent/variation remains inquiry-only.
- Selected tuple is passed as controlled inquiry context.
- No public price, range, Offer, cart, checkout, payment, public order, or automated quote result.
- No stock, availability, supplier, lead time, minimum order, or suitability value is inferred from the tuple.

## Validation Gates

- Axis is approved global attribute and declared by parent.
- Value belongs to the controlled registry and uses approved unit/format.
- Tuple has one value per required axis and no prohibited field.
- Tuple is unique and independently approved as valid.
- Persian/English labels match structured values.
- Parent/variation identities, inquiry, no-price, SEO, CRM, import, and lifecycle rules are consistent.
- Runtime/Admin volume and manageability are reviewed before implementation.

## Founder Gates

- Parent identity and family relationship.
- Axis inventory/order and allowed values.
- Valid-combination evidence and responsible reviewers.
- Display/filter/mobile Persian RTL behavior.
- Stable ID/final SKU policy in a separate decision.
- Runtime mapping, staging, recovery, and implementation authorization later.

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Attribute Template](ATTRIBUTE_TEMPLATE.md)
- [Import Template](IMPORT_TEMPLATE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
