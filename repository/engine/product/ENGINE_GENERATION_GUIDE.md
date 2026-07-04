# Product Engine Generation Guide

## Document Control

- **Document ID:** `repository/engine/product/ENGINE_GENERATION_GUIDE.md`
- **Status:** Review
- **Authority:** Product Engine Procedure
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Repository Guardian, Qualified Domain Reviewer, and Quality Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On engine/template version, generation sequence, output set, validation, handoff, or compatibility change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md), [Engine Rules](ENGINE_RULES.md), and [Engine Workflow](ENGINE_WORKFLOW.md)
- **Dependencies:** [Enterprise Product Engine](PRODUCT_ENGINE.md), [Engine Rules](ENGINE_RULES.md), [Engine Workflow](ENGINE_WORKFLOW.md), and all six Product Engine templates
- **Related Documents:** [Validation Template](VALIDATION_TEMPLATE.md) and [Sprint 03D Audit](../../../docs/AUDIT_REPORT_SPRINT03D.md)
- **Traceability:** CP-001 through CP-010, PDM/WCM/TAX/ATT/INQ/SEOENT/FIELD/PLUG, Sprint 03D
- **AI Compatibility:** AI-readable controlled procedure; assistance cannot invent inputs, approve outputs, or execute implementation
- **Approval:** Pending Founder review; guide authorizes no family implementation/import

## Purpose

Explain how to create a complete new Product Family repository set using only the controlled Product Engine templates and approved evidence.

## Preconditions

Before generation:

- An explicit task names the family and authorizes repository-only Product Engine generation.
- Current engine/template versions are identified.
- Founder confirms the intake may proceed and assigns owners/reviewers or marks them `TBD`.
- Governing product, taxonomy, attribute, inquiry, SEO, WordPress, WooCommerce, field, plugin, and repository rules are read.
- Available domain sources are listed; missing sources remain `TBD`.
- No runtime access, import, product creation, price, stock, supplier data, final SKU, or public content is required.

If these preconditions fail, stop at Idea/Intake.

## Generation Set

Create exactly one coordinated family set:

| Order | Template | Generated family asset |
| ---: | --- | --- |
| 1 | [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md) | `{{FAMILY_KEY}}_PRODUCT_FAMILY.md` |
| 2 | [Attribute Template](ATTRIBUTE_TEMPLATE.md) | `{{FAMILY_KEY}}_ATTRIBUTE_MODEL.md` |
| 3 | [Variation Template](VARIATION_TEMPLATE.md) | `{{FAMILY_KEY}}_VARIATION_MODEL.md` |
| 4 | [Import Template](IMPORT_TEMPLATE.md) | `{{FAMILY_KEY}}_IMPORT_MODEL.md` |
| 5 | [SEO Template](SEO_TEMPLATE.md) | `{{FAMILY_KEY}}_SEO_MODEL.md` |
| 6 | [Validation Template](VALIDATION_TEMPLATE.md) | `{{FAMILY_KEY}}_VALIDATION.md` |

A future approved family audit completes the review package. Do not create a family-specific file that lacks a template owner.

## Step 1 — Intake

Record family purpose, Persian/English working labels, scope, exclusions, source documents, owner/reviewers, Product Group/Type evidence, known specifications, inquiry context, known unknowns, and prohibited data.

Do not solve missing information during intake. Write `TBD` and assign a decision/evidence owner.

## Step 2 — Establish Identity and Paths

After naming review, define:

- Stable family ID/key or `TBD`.
- Lowercase approved family folder name.
- Generated filenames from Engine Rules.
- Engine/template provenance metadata.
- Links to governing documents and sibling generated assets.

Do not derive public slugs or final SKUs from the family key.

## Step 3 — Generate the Family Contract

Copy the Product Family Template structure. Fill only sourced identity, scope, parent strategy, inquiry, no-price, Mobile First/Persian RTL, WooCommerce summary, SEO, CRM, unknowns, and Founder gates. Replace every unresolved placeholder token with `TBD` before Review.

## Step 4 — Generate Field Classification and Attributes

Build the complete field inventory from the family/domain sources. For every field:

1. Define stable key, Persian label, meaning, owner, type, unit, values, access, and requiredness.
2. Assign exactly one primary classification.
3. Assign public/filter/variation/SEO/CRM/required/Founder-review flags.
4. Create the global/local attribute registry only from classified attribute fields.
5. Record value registries and validation; leave unsupported values `TBD`.

Do not copy Pipe fields into Profile, Fittings, Glass Hardware, Pool Equipment, Wood, Fasteners, Tools, Accessories, or a future family unless independent evidence defines the same canonical global attribute.

## Step 5 — Generate the Variation Contract

Reference only fields classified as Variation Attribute. Define axis order, values, units, display, valid-combination evidence, identities, duplicate rules, inquiry/no-price constraints, and Founder gates. Never generate the Cartesian product and never create final SKUs.

If no approved variation evidence exists, keep the axis/combination set `TBD`; do not invent a simple-product exception to the Variable Parent Product rule.

## Step 6 — Generate the Import Contract

Create the logical staging schema and map every source column once. Generate family-specific attribute columns from the approved field model. Classify unresolved commercial/runtime fields as HOLD, and any public-price control as PROHIBITED with an empty-only rule. Define rejection, preview, staging, reconciliation, and rollback prerequisites without executing them.

## Step 7 — Generate the SEO Contract

Define candidate entities, intent, canonical ownership, category/product/attribute boundaries, metadata unknowns, FAQ topics, internal-link relationships, schema eligibility, and no-price restrictions. Keep all unapproved public slugs/content/indexation `TBD`.

## Step 8 — Generate Validation

Instantiate checks for every generated section/field/value/relationship and all engine invariants. Record actual results as PASS, PENDING, BLOCKED, FAIL, or NOT RUN. Include Founder/specialist checklist and an explicit stage-scoped GO/NO-GO.

## Step 9 — Cross-Asset Review

Confirm:

- Same family ID/key, labels, owners, engine/template versions, and sources.
- One primary classification per field.
- Same category and canonical attribute identities across family/import/SEO/CRM.
- Same variation axes/values/order/combination references.
- Inquiry First and No Public Pricing everywhere.
- No product fact is owned by SEO, CRM, importer, template, or runtime projection.
- Links, metadata, traceability, graph, navigation, and compatibility are synchronized.

## Step 10 — Handoff and Decision

Submit the complete set to domain/Product Data/SEO/CRM/quality/technical reviewers, then Founder. Record remaining `TBD` items and the exact next permitted stage. A repository review `GO` does not authorize WooCommerce, import, SEO publication, CRM integration, or release.

## Regeneration

When approved inputs or templates change:

1. Identify source and affected generated assets.
2. Classify compatibility impact under Engine Rules.
3. Preserve stable identities and approved values.
4. Regenerate only affected sections through current templates.
5. Review the diff; never silently overwrite manual evidence.
6. Re-run full cross-asset validation and approval gates.
7. Record template/output versions and migration notes.

## Family Coverage

The same six-template generation set applies to Pipe, Profile, Fittings, Glass Hardware, Pool Equipment, Wood, Fasteners, Tools, Accessories, and future families. The templates are deliberately domain-neutral; each family supplies its own approved fields, values, axes, categories, SEO intent, and evidence.

If a family exposes a genuinely reusable concern absent from the engine, stop and submit an Engine change request. Do not redesign locally or add an unowned family document type.

## Completion Checklist

- [ ] Authorized intake and sources recorded.
- [ ] Six generated assets use current templates and provenance.
- [ ] No surviving placeholder token; unknowns are explicit `TBD`.
- [ ] Every field classified exactly once.
- [ ] Values/units/combinations have domain evidence.
- [ ] Inquiry/no-price/mobile Persian RTL rules preserved.
- [ ] Import/SEO/CRM projections preserve source authority.
- [ ] Validation, links, traceability, compatibility, and approvals recorded.
- [ ] No runtime, product, price, stock, supplier, final-SKU, or import action occurred.

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Engine Rules](ENGINE_RULES.md)
- [Engine Workflow](ENGINE_WORKFLOW.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
- [Sprint 03D Audit](../../../docs/AUDIT_REPORT_SPRINT03D.md)
