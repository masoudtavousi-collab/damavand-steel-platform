# Damavand Steel Enterprise Product Engine

## Document Control

- **Document ID:** `repository/engine/product/PRODUCT_ENGINE.md`
- **Status:** Review
- **Authority:** Product Engine Standard
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Enterprise Architect, Qualified Domain Reviewer, SEO Reviewer, CRM Reviewer, Quality Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On engine lifecycle, input, output, template, pipeline, validation, approval, or compatibility change
- **Lifecycle:** Review
- **Source of Truth:** Approved repository product, taxonomy, attribute, inquiry, SEO, WordPress, WooCommerce, field, plugin, and implementation rules plus the Sprint 03D mandate
- **Dependencies:** [Enterprise Product Data Model](../../../docs/19_PRODUCT_DATA_MODEL.md), [WooCommerce Product Model](../../../docs/20_WOOCOMMERCE_PRODUCT_MODEL.md), [Product Taxonomy Model](../../../docs/21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute Model](../../../docs/22_PRODUCT_ATTRIBUTE_MODEL.md), and [Inquiry Data Model](../../../docs/23_INQUIRY_DATA_MODEL.md)
- **Related Documents:** [Engine Rules](ENGINE_RULES.md), [Engine Workflow](ENGINE_WORKFLOW.md), [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md), and the six Product Engine templates in this directory
- **Traceability:** CP-001 through CP-010, PDM-001 through PDM-008, WCM-001 through WCM-008, TAX-001 through TAX-008, ATT-001 through ATT-007, INQ-001 through INQ-008, SEOENT-001 through SEOENT-009, FIELD-001 through FIELD-009, PLUG-001 through PLUG-010, Sprint 03A through Sprint 03D
- **AI Compatibility:** AI-readable template engine; no AI product feature, autonomous decision, generated commercial claim, or Phase 1 AI behavior
- **Approval:** Pending Founder and specialist review; no family generation is approved for implementation/import solely by this document

## Purpose

Define one reusable, template-driven Product Engine for every Damavand Steel product family. The engine standardizes how approved family facts become controlled repository assets without redesigning the repository, inventing domain data, or mutating WordPress.

## Authority Boundary

Once approved, this directory is the single source of truth for the **generation contract**: template set, workflow, naming, validation, and compatibility rules. It is not the source of truth for business rules, family facts, commercial data, taxonomy decisions, technical specifications, SEO intent, CRM policy, or runtime configuration.

Authority flows as follows:

```text
Approved governing documents + Founder/domain evidence
  -> Product Engine templates and rules
      -> Family-specific controlled assets
          -> Validation and approval evidence
              -> separately authorized implementation/import pipeline
```

Generated family assets never override governing documents. Task text, AI output, template defaults, or existing examples cannot become product fact authority without the required human evidence and approval.

## Engine Philosophy

- Template First: every new family starts from the controlled templates in this directory.
- Product Data First: structured identity, taxonomy, attributes, variations, validation, and ownership precede platform configuration.
- Evidence First: unknown values remain `TBD`; no default creates a business or technical claim.
- Variable Parent Product: the approved parent/variation architecture remains the default governing model; an exception requires an explicit governing decision.
- Inquiry First and No Public Pricing: every generated family inherits inquiry-only and empty/no-price constraints.
- Global Reuse: reusable specifications use canonical global identities rather than local duplicates or free text.
- Configuration First and Plugin First: outputs define capability requirements, not custom code or vendor assumptions.
- Mobile First and Persian RTL: labels, selection order, filter design, and validation include these requirements from the start.
- Separation of Concerns: category, attribute, custom field, CRM, SEO, import helper, and internal data remain distinct.
- Reversible Delivery: implementation/import remains blocked until staging, backup, reconciliation, rollback, and approval evidence exists.

## Family Registry

| Product family | Engine state | Current evidence boundary |
| --- | --- | --- |
| Pipe | Implementation example | Sprint 03A–03C assets exist; they remain Review and import-blocked |
| Profile | Not generated | Family facts and Founder/domain input `TBD` |
| Fittings | Not generated | Family facts and Founder/domain input `TBD` |
| Glass Hardware | Not generated | Family facts and Founder/domain input `TBD` |
| Pool Equipment | Not generated | Family facts and Founder/domain input `TBD` |
| Wood | Not generated | Family facts and Founder/domain input `TBD` |
| Fasteners | Not generated | Family facts and Founder/domain input `TBD` |
| Tools | Not generated | Family facts and Founder/domain input `TBD` |
| Accessories | Not generated | Family facts and Founder/domain input `TBD` |
| Future families | Not generated | A family is added only through the Engine Workflow |

This registry does not approve names, product structures, categories, attributes, variations, stock, suppliers, prices, SKUs, URLs, or public content for ungenerated families.

## Lifecycle

| Stage | Purpose | Minimum exit condition |
| --- | --- | --- |
| Idea | Record a candidate family without creating product facts | Founder confirms review may begin |
| Intake | Collect authoritative business/domain inputs | Source, owner, scope, unknowns, and evidence recorded |
| Family Draft | Generate family contract from the Product Family Template | Identity and parent strategy ready for review |
| Classification Draft | Generate attribute, variation, import, SEO, and validation assets | Every field has one responsibility and every unknown is `TBD` |
| Specialist Review | Domain, Product Data, SEO, CRM, quality, and technical review | Findings resolved or explicitly blocked |
| Founder Review | Founder approves or rejects recorded decisions | Dated approval record exists |
| Validated | All repository/static gates pass | Validation report has no unresolved generation defects |
| Import Candidate | Exact runtime mapping and recovery evidence may be prepared | Separate readiness gate permits planning only |
| Released | Separately authorized implementation is reconciled and accepted | Release evidence and rollback status recorded |
| Maintained | Approved family evolves through controlled changes | Compatibility and dependent assets remain synchronized |
| Deprecated/Archived | Family or asset is replaced/retired safely | Replacement, redirects/mappings, retention, and audit recorded |

These are Product Engine stages. They do not replace the repository Document Lifecycle states Draft, Review, Approved, Deprecated, and Archived.

## Inputs

Every generation request requires:

- Approved task scope and intended family name.
- Founder-confirmed Persian and English working labels.
- Product Family/Product Group/Product Type evidence or explicit `TBD`.
- Qualified domain evidence for specifications, units, controlled values, and valid combinations.
- Product Data owner, reviewers, approval authority, version, and source references.
- Proposed parent/variation structure consistent with governing rules.
- Field inventory and one proposed classification per field.
- Inquiry context requirements with no transaction/public-price behavior.
- SEO/search intent evidence, canonical owner proposal, and URL unknowns.
- CRM/integration needs as references only, with privacy/access boundaries.
- Explicit unknown, excluded, prohibited, and deferred items.

Prices, stock values, supplier data, final SKUs, unsupported suitability claims, and inferred commercial facts are not valid generation inputs in Sprint 03D.

## Outputs

A complete family generation set contains:

1. Family contract generated from [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md).
2. Attribute classification/profile generated from [Attribute Template](ATTRIBUTE_TEMPLATE.md).
3. Variation model generated from [Variation Template](VARIATION_TEMPLATE.md).
4. Import contract generated from [Import Template](IMPORT_TEMPLATE.md).
5. SEO entity contract generated from [SEO Template](SEO_TEMPLATE.md).
6. Validation and approval contract generated from [Validation Template](VALIDATION_TEMPLATE.md).
7. A generation manifest embedded in every output header: engine version, template ID/version, source evidence, generated date, owner, reviewer, and status.
8. A family audit recording completeness, conflicts, unknowns, validation, and go/no-go status.

Outputs are controlled repository Markdown/data contracts. They are not WordPress objects, WooCommerce settings, CSV imports, SEO output, CRM records, or production data.

## Generation Process

1. Open an Idea/Intake record through an authorized task.
2. Confirm the current Product Engine version and copy—not rewrite—the required template structures.
3. Assign a stable family key only after naming review.
4. Populate evidence-backed values; preserve every unknown as `TBD`.
5. Generate family, attribute, variation, import, SEO, and validation assets as one versioned set.
6. Record template IDs/versions and all governing/source references in each output.
7. Run structural, terminology, classification, duplication, link, metadata, value, no-price, inquiry, and compatibility checks.
8. Submit specialist and Founder gates; do not convert unresolved review items into defaults.
9. Publish the repository asset set only after review status is accurately recorded.
10. Treat implementation/import as a separate authorized pipeline.

## Validation Process

Validation occurs at four layers:

| Layer | Required checks |
| --- | --- |
| Template | Required sections/tokens, template version, no family-specific residue, no duplicate authority |
| Family contract | Identity, one classification per field, units, allowed values, parent/variation consistency, Persian normalization, duplicates, unknowns |
| Cross-pipeline | Import/WooCommerce/SEO/CRM mappings consume the same canonical identities without copying authority |
| Repository | Metadata, links, index/navigation, traceability, graph, naming, compatibility, prohibited-data, and no-implementation boundaries |

Any missing source, conflicting authority, invented value, uncontrolled term, duplicate classification, public-price path, transactional path, unapproved commercial claim, or absent Founder gate is a blocking failure.

## Founder Approval Gates

| Gate | Founder decision required |
| --- | --- |
| Intake | Family scope, accountable owners, and authority sources |
| Identity | Persian/English labels, family/group/type placement, stable identifiers policy |
| Classification | Category, global/local/variation attribute, custom field, CRM, SEO, helper, internal, excluded decisions |
| Domain | Specifications, units, values, terminology, valid combinations, claims, and evidence owners |
| Experience | Mobile Persian RTL order, filters, tables, inquiry path, accessibility expectations |
| SEO | Intent, canonical owner, public slug, metadata, indexation, schema, linking |
| CRM/Integration | Field ownership, access, consent, retention, references, reconciliation, recovery |
| Import/Runtime | Exact mapping, versions, staging, backup/restore, dry run, rollback, permissions, release |

No gate is satisfied by template completion, AI output, or file creation alone.

## Import Pipeline

```text
Approved family set
  -> deterministic import contract
      -> source validation + collision checks
          -> non-mutating preview
              -> isolated staging + backup/restore evidence
                  -> explicit Founder authorization
                      -> separately executed import + reconciliation + rollback decision
```

The engine creates only the import contract and validation requirements. It does not create/import CSV data, select an importer, connect to a runtime, or resolve `TBD` values.

## WooCommerce Pipeline

- Map Product Family to one approved category identity.
- Map reusable specifications to approved global attributes.
- Map only approved axes to variations under one Variable Parent Product.
- Keep custom, CRM, SEO, helper, and internal fields out of attribute/category authority.
- Require `inquiry_only=yes` and no public-price target.
- Block on missing IDs, terms, combinations, runtime capability, Admin manageability, or rollback evidence.

The pipeline is logical until a separate implementation task verifies exact WooCommerce/runtime behavior.

## SEO Pipeline

- Resolve one canonical entity/intent owner.
- Use approved family facts and canonical attribute identities.
- Keep variations/facets non-canonical and non-indexable by default.
- Generate no keyword, metadata, FAQ answer, schema, URL, or landing claim without evidence and approval.
- Prohibit Offer/price, stock promise, supplier, certification, safety, or suitability claims without authority.
- Validate Persian RTL content, mobile experience, internal links, duplicates, and cannibalization before publication.

## CRM Pipeline

- Product Engine remains product-master authority for approved product facts.
- CRM receives stable references and approved snapshots, not copied uncontrolled facts.
- Inquiry context may include family, parent, variation, selected attributes, source, and permitted customer fields.
- Internal priority, routing, status, access, consent, retention, and reconciliation require separate approval.
- No price, supplier, unverified stock, protected note, or personal data is generated by the engine.

## Pipe as Implementation Example

[Pipe Product Family](../../data/products/pipes/PIPE_PRODUCT_FAMILY.md) and its Sprint 03A–03C assets demonstrate a family-specific implementation. They are not templates and must not be copied as universal values. The engine may cite Pipe for examples of traceability and gating while all Pipe-specific names, dimensions, values, and classifications remain confined to the Pipe data set.

Pipe assets remain unchanged by Sprint 03D. Future migration to engine headers/templates, if desired, requires a separate compatibility-preserving task; no rename or rewrite is implied.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03D Enterprise Product Engine contract; no product/runtime implementation. |

## Navigation

- [Engine Rules](ENGINE_RULES.md)
- [Engine Workflow](ENGINE_WORKFLOW.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
- [Sprint 03D Audit](../../../docs/AUDIT_REPORT_SPRINT03D.md)
