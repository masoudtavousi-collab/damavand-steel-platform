# Product Variation Template

## Document Control

- **Document ID:** `repository/engine/product/VARIATION_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Qualified Domain Reviewer, Sales/Operations Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 1.0.0
- **Last Updated:** 2026-08-03
- **Last Review:** 2026-08-03
- **Review Cycle:** On variation axis, value, combination, identity, display, lifecycle, or template change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md), approved canonical Family/Series/Variant Rules sources, and generated Family/Attribute references; the WooCommerce Product Model constrains downstream projection only
- **Dependencies:** [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md), [Attribute Template](ATTRIBUTE_TEMPLATE.md), and [Engine Rules](ENGINE_RULES.md)
- **Related Documents:** [Import Template](IMPORT_TEMPLATE.md), [Validation Template](VALIDATION_TEMPLATE.md), and [Engine Workflow](ENGINE_WORKFLOW.md)
- **Traceability:** PDM-001 through PDM-008, WCM-001 through WCM-008, ATT-001 through ATT-007, Sprint 03D
- **AI Compatibility:** AI-readable reusable template; no autonomous combination expansion, commercial inference, or SKU generation
- **Approval:** Pending Founder review; no variation or combination is approved by template completion

## Purpose

Generate a controlled downstream Parent/Variation mapping contract sourced from the canonical `Catalog → Platform → Family → Series → Variant Rules → derived SKU` hierarchy without treating candidate values as commercially valid products. SKU is not a canonical entity identity.

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `VARIATION_TEMPLATE` |
| Engine template version | `1.0.0` |
| Required generated provenance | `PRODUCT_ENGINE@1.0.0` and `VARIATION_TEMPLATE@1.0.0` |
| Generated asset name | `{{FAMILY_KEY}}_VARIATION_MODEL.md` |
| Generated asset location | `repository/data/products/{{FAMILY_FOLDER}}/` |

## Canonical Source and Downstream Parent Contract

| Property | Placeholder/rule |
| --- | --- |
| Catalog/Platform/Family/Series source IDs | `{{APPROVED_SOURCE_REFERENCES_OR_TBD}}` |
| Variant Rule Set ID | `{{APPROVED_VARIANT_RULE_SET_ID_OR_TBD}}` |
| Downstream Parent mapping ID | `{{PARENT_ADAPTER_ID_OR_TBD}}`; adapter-only and never canonical repository identity |
| Downstream Parent key/SKU | `TBD` until separately approved; never generate a final SKU |
| Downstream mapping type | Variable Parent Product presentation |
| Shared family/category presentation | `{{APPROVED_REFERENCE_OR_TBD}}` |
| Declared variation axes | `{{AXES_FROM_VARIANT_RULES_OR_TBD}}` |
| Inquiry behavior | Required |
| Public pricing | Prohibited |
| Public page/URL context | Downstream Parent only after SEO approval; never Product Repository ownership |

## Axis Definition Template

| Order | Axis | Attribute ID/key | Unit | Variant Rules allowed-values source | Filter | Public label | Domain reviewer | Status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{ORDER}}` | `{{AXIS_NAME}}` | `{{GLOBAL_ATTRIBUTE_KEY}}` | `{{UNIT_OR_NONE}}` | `{{REGISTRY_REFERENCE_OR_TBD}}` | Yes/No | `{{LABEL_FA_OR_TBD}}` | `{{REVIEWER_OR_TBD}}` | Draft/Review/Approved |

Only axes and allowed values authorized by the referenced Variant Rules may be projected as WooCommerce Variation Attributes. Controlled registries provide value identity but cannot authorize applicability independently.

## Controlled Value Template

| Axis | Stable value key | Persian label | English label | Unit/format | Evidence | Lifecycle | Commercial validity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{AXIS}}` | `{{VALUE_KEY_OR_TBD}}` | `{{LABEL_FA_OR_TBD}}` | `{{LABEL_EN_OR_TBD}}` | `{{RULE_OR_TBD}}` | `{{SOURCE_OR_TBD}}` | Review | `TBD` until approved |

No Pipe values or generic sample values may be copied into a new family without independent family evidence.

## Valid-Combination Template

| Variant Rule Set ID | Governed tuple reference | Downstream Parent mapping ID | Axis tuple | Domain evidence | Commercial evidence | Lifecycle | Import eligible |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{VARIANT_RULE_SET_ID_OR_TBD}}` | `{{GOVERNED_TUPLE_REFERENCE_OR_TBD}}` | `{{PARENT_ADAPTER_ID_OR_TBD}}` | `{{ONE_VALUE_PER_AXIS_OR_TBD}}` | `{{SOURCE_OR_TBD}}` | `TBD` | Review | No |

Candidate allowed-value sets do not establish valid combinations. Never generate the Cartesian product automatically. Each downstream tuple must resolve to an evidence-backed Variant Rules source and requires domain review, commercial evidence, lifecycle approval, and duplicate checks.

## Identity and Duplicate Rules

- One downstream Variation maps to exactly one downstream Parent.
- One approved governed tuple maps to at most one active Variation under that Parent.
- Parent and Variation IDs are adapter-only. Canonical Family, Series, and Variant Rules source IDs remain separate; final SKU is derived and requires later approval.
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

- Every downstream Parent/Variation mapping remains inquiry-only.
- Selected tuple is passed as controlled inquiry context.
- No public price, range, Offer, cart, checkout, payment, public order, or automated quote result.
- No stock, availability, supplier, lead time, minimum order, or suitability value is inferred from the tuple.

## Validation Gates

- Axis is an approved global attribute authorized by the referenced Variant Rules.
- Value is authorized by the referenced Variant Rules, belongs to the controlled registry, and uses approved unit/format.
- Tuple has one value per required axis and no prohibited field.
- Tuple is unique and independently approved as valid.
- Persian/English labels match structured values.
- Canonical source references and downstream Parent/Variation mappings, inquiry, no-price, SEO, CRM, import, and lifecycle rules are consistent without transferring authority.
- Runtime/Admin volume and manageability are reviewed before implementation.

## Founder Gates

- Canonical Family, Series, and Variant Rules source references.
- Downstream Parent mapping and family presentation relationship.
- Axis inventory/order and allowed values sourced from Variant Rules.
- Valid-combination evidence and responsible reviewers.
- Display/filter/mobile Persian RTL behavior.
- Adapter ID/final derived SKU policy in a separate decision.
- Runtime mapping, staging, recovery, and implementation authorization later.

## Compatibility and Provenance

Version `1.0.0` is a major required-structure and semantic change under Engine Rules. Its compatibility impact is breaking for every Family with a generated 0.x Variation asset. Before use, a separately authorized migration or regeneration task must record the affected-Family/asset inventory, exact engine/template provenance, migration and validation plan, diff review, full validation, and Founder approval. No Parent, Variation, tuple, SKU, availability, or runtime record is created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.1 | 2026-08-03 | Recast Parent and Variation as downstream adapter mappings sourced from canonical Family, Series, and Variant Rules references. |
| 1.0.0 | 2026-08-03 | Major provenance-compatible template revision: required canonical source references, adapter-only IDs, and Variant Rules ownership of allowed values, axes, and valid tuples. |

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Attribute Template](ATTRIBUTE_TEMPLATE.md)
- [Import Template](IMPORT_TEMPLATE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
