# Product Attribute Template

## Document Control

- **Document ID:** `repository/engine/product/ATTRIBUTE_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Qualified Domain Reviewer, SEO Reviewer, CRM Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On attribute classification, field contract, allowed value, use flag, validation, or template change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md), Product Attribute Model, Product Taxonomy Model, and Custom Fields Model
- **Dependencies:** [Enterprise Product Engine](PRODUCT_ENGINE.md), [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md), and [Engine Rules](ENGINE_RULES.md)
- **Related Documents:** [Variation Template](VARIATION_TEMPLATE.md), [Import Template](IMPORT_TEMPLATE.md), [SEO Template](SEO_TEMPLATE.md), and [Validation Template](VALIDATION_TEMPLATE.md)
- **Traceability:** TAX-001 through TAX-008, ATT-001 through ATT-007, FIELD-001 through FIELD-009, Sprint 03D
- **AI Compatibility:** AI-readable reusable template; no generated values or autonomous classification approval
- **Approval:** Pending Founder review; generated classifications/attributes remain unimplemented

## Purpose

Generate a family-specific field classification and global attribute profile without copying another family's fields or inventing values.

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `ATTRIBUTE_TEMPLATE` |
| Engine template version | `0.1.0` |
| Generated asset name | `{{FAMILY_KEY}}_ATTRIBUTE_MODEL.md` |
| Generated asset location | `repository/data/attributes/` or approved family-owned location |

## Field Intake Record

Create one record for every candidate field before defining attributes:

| Required property | Placeholder/rule |
| --- | --- |
| Field name | `{{ENGLISH_STABLE_KEY_OR_TBD}}` |
| Persian label | `{{PERSIAN_LABEL_OR_TBD}}` |
| Definition | `{{DOMAIN_DEFINITION_OR_TBD}}` |
| Source authority | `{{SOURCE_OR_TBD}}` |
| Data owner/reviewer | `{{OWNER_AND_REVIEWER_OR_TBD}}` |
| Data type/cardinality | `{{TYPE_AND_CARDINALITY_OR_TBD}}` |
| Unit/precision/tolerance | `{{UNIT_RULE_OR_TBD}}` |
| Allowed values | `{{CONTROLLED_VALUES_OR_TBD}}` |
| Access class | Public, protected, internal, integration-only, or `TBD` |
| Required condition | `{{LIFECYCLE_CONDITION_OR_TBD}}` |
| Unknown behavior | Preserve `TBD`; never default |

## Primary Classification

Assign each field exactly one class:

- WooCommerce Category
- WooCommerce Global Attribute
- WooCommerce Local Attribute
- WooCommerce Variation Attribute
- Custom Field
- Internal CRM Field
- SEO Metadata
- Import Helper Field
- Hidden/Internal Only
- Excluded

Use WooCommerce Local Attribute only for a separately approved, genuinely family-local non-reusable concern. Reusable specifications default to global identity. A field cannot receive multiple primary classes; downstream SEO/CRM consumption is represented by flags.

## Classification Matrix Template

| Field | Persian label | Primary classification | Reason | Public | Filter | Variation | SEO | CRM | Required | Founder review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{FIELD_KEY}}` | `{{FIELD_LABEL_FA}}` | `{{ONE_ALLOWED_CLASS}}` | `{{EVIDENCE_BASED_REASON}}` | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No |

Every generated row must use literal `Yes` or `No` for the seven flags. Conditional meaning belongs in Reason or validation rules.

## WooCommerce Attribute Registry Template

For fields classified Global or Variation Attribute, generate:

| Attribute | Persian label | Slug | Global/local | Variations | Filtering | Product table | SEO | Allowed values | Validation | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{ATTRIBUTE_NAME}}` | `{{LABEL_FA}}` | `{{ASCII_SLUG}}` | Global/Local | Yes/No | Yes/No | Yes/No | Yes/No | `{{VALUES_OR_TBD}}` | `{{RULE_OR_TBD}}` | `{{BOUNDARY}}` |

## Attribute Decision Rules

1. Category describes primary catalog hierarchy; attribute describes reusable specification.
2. Variation use and filtering use are independent decisions.
3. Filter eligibility does not grant indexable archive/landing authority.
4. Typed numeric values retain canonical unit, precision, and tolerance rules.
5. A display composite is not automatically an authoritative attribute.
6. Free text, tags, local duplicates, and automatic term creation cannot bypass governance.
7. Brand, origin, quality, application, environment, compatibility, safety, and warranty claims require evidence and qualified review.
8. Protected commercial/CRM fields remain non-public and out of schema/filters.

## Allowed-Value Contract

For each controlled attribute record value ID/key, Persian/English labels, definition, aliases, unit, ordering, lifecycle, owner, evidence, external mappings, and valid-combination constraints. An empty registry remains `TBD`; templates must not populate example values from Pipe or another family.

## Filter and Product-Table Contract

Record ordered filters, mobile Persian RTL behavior, zero-result/invalid-combination handling, URL/indexation boundary, performance/accessibility review, and table disclosure. Optional or `TBD` values do not render.

## Founder Gates

- Field inventory and one-class-per-field completeness.
- Category-versus-attribute decisions.
- Global/local/variation classification.
- Persian labels, English keys, definitions, units, values, aliases, and owners.
- Filter, product table, SEO, CRM, access, and requiredness flags.
- Runtime attribute/term mapping in a later implementation decision.

## Completion Rules

- No unclassified or multiply classified field.
- No local duplicate of a canonical reusable attribute.
- No uncontrolled value or mixed unit.
- Unknown values remain `TBD` and block affected generation gates.
- No WooCommerce attribute, term, filter, field, or product is created by this template.

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md)
- [Variation Template](VARIATION_TEMPLATE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
