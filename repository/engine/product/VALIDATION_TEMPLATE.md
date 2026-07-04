# Product Validation Template

## Document Control

- **Document ID:** `repository/engine/product/VALIDATION_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Qualified Domain Reviewer, Quality Reviewer, SEO Reviewer, CRM Reviewer, Security Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On family contract, validation rule, evidence gate, rejection condition, pipeline, or template change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md), [Engine Rules](ENGINE_RULES.md), and generated family/attribute/variation/import/SEO assets
- **Dependencies:** [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md), [Attribute Template](ATTRIBUTE_TEMPLATE.md), [Variation Template](VARIATION_TEMPLATE.md), [Import Template](IMPORT_TEMPLATE.md), and [SEO Template](SEO_TEMPLATE.md)
- **Related Documents:** [Engine Workflow](ENGINE_WORKFLOW.md) and [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
- **Traceability:** CP-001 through CP-010, PDM/WCM/TAX/ATT/INQ/SEOENT/FIELD/PLUG, Sprint 03D
- **AI Compatibility:** AI-readable validation template; human evidence and Founder approvals cannot be auto-passed
- **Approval:** Pending Founder review; generated checklists do not authorize implementation/import

## Purpose

Generate one family-specific validation and governance contract that blocks incomplete, conflicting, invented, unsafe, or unauthorized Product Engine outputs.

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `VALIDATION_TEMPLATE` |
| Engine template version | `0.1.0` |
| Generated asset name | `{{FAMILY_KEY}}_VALIDATION.md` |
| Generated asset location | `repository/data/validation/` |

## Result Vocabulary

| Result | Meaning |
| --- | --- |
| PASS | Current controlled evidence satisfies the check |
| PENDING | Evidence/approval has not been supplied |
| BLOCKED | Known unresolved prerequisite prevents progression |
| FAIL | Supplied evidence violates the rule |
| NOT RUN | Requires separately authorized runtime/execution activity |

Any non-PASS hard gate yields `NO-GO` for the affected lifecycle transition.

## Validation Record Template

| Check ID | Layer | Rule | Evidence/source | Result | Owner/reviewer | Blocking | Remediation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{ID}}` | Template/Family/Attribute/Variation/Import/SEO/CRM/Repository/Runtime | `{{RULE}}` | `{{EVIDENCE_OR_TBD}}` | PASS/PENDING/BLOCKED/FAIL/NOT RUN | `{{OWNER_OR_TBD}}` | Yes/No | `{{ACTION_OR_TBD}}` |

## Template Validation

- Correct current template IDs/versions recorded.
- All required generated asset types exist exactly once.
- No surviving `{{PLACEHOLDER}}` token in review-ready outputs.
- Unknowns represented explicitly as `TBD`.
- No family-specific data copied from an example without independent evidence.
- No duplicate sections, authority, or source-of-truth claims.

## Family and Classification Validation

- Stable identity/key uniqueness and source evidence.
- One primary classification for every field.
- Category/attribute/custom/CRM/SEO/helper/internal/excluded responsibilities do not overlap.
- Persian labels, English keys, definitions, access, requiredness, owner, and lifecycle complete.
- Product Group/Type/family relationships and exclusions explicit.

## Attribute and Value Validation

- Reusable specifications are global; local exceptions explicitly approved.
- Variation/filter flags independently justified.
- Values use controlled registries or validated types/units/precision/tolerances.
- Synonyms/aliases map to one identity; no mixed units or free-text duplicates.
- Optional high-risk claims require qualified evidence.

## Variation Validation

- Parent declares every axis.
- One approved value per required axis.
- Combination exists in the approved combination set; no automatic Cartesian expansion.
- No orphan, duplicate tuple, placeholder identity, or final-SKU inference.
- Inquiry-only/no-price behavior consistent on parent and children.
- Mobile Persian RTL order and invalid-combination handling reviewed.

## Import Validation

- Exact schema/version, unique columns, encoding, row width, formula/macro/secret checks.
- Every column maps once and only to an approved responsibility.
- Final required IDs/SKUs and relationships approved; `TBD` blocks execution.
- No auto-created terms/categories/attributes/slugs/commercial states.
- Target capability, preview, staging, backup/restore, reconciliation, rollback, permissions, and authorization approved before runtime activity.

## Inquiry and No-Public-Price Validation

- Inquiry-only control affirmative for every applicable parent/variation.
- No cart, checkout, payment, public order, or automated public quote result.
- Public-price control empty and mapped nowhere.
- No price/Offer/currency/range/discount/zero/free/sentinel leakage through content, metadata, schema, API, feed, cache, search, analytics, email, export, or CRM.
- Runtime checks remain NOT RUN until separately authorized.

## SEO Validation

- One canonical owner per entity/intent.
- Slug/URL policy, collision, redirect, reserved path, robots, sitemap, and internal links approved.
- Variations/facets non-indexable/non-canonical by default.
- Metadata/content/schema use visible approved facts and contain no unsupported claims.
- Persian RTL/mobile/accessibility and cannibalization checks pass before publication.

## CRM and Protected-Data Validation

- Product facts retain product-master authority.
- CRM receives only approved stable references/snapshots.
- Protected/internal fields excluded from public output and schema.
- Consent, access, retention, routing, status, retry, reconciliation, audit, and recovery approved before integration.
- No customer/personal data is generated by templates.

## Repository Validation

- Metadata, filenames, locations, links, navigation, traceability, graph, version, and compatibility pass.
- Generated assets record engine/template provenance.
- No WordPress/hosting/plugin/database/product/page/import mutation.
- No production code, secret, backup payload, runtime log, commercial value, supplier data, stock value, price, or final SKU.

## Founder Approval Checklist Template

- [ ] Intake scope and owners approved.
- [ ] Identity/hierarchy/classification approved.
- [ ] Domain fields/values/combinations approved.
- [ ] Mobile Persian RTL/filter/table/inquiry behavior approved.
- [ ] SEO/canonical/content/schema/linking approved.
- [ ] CRM/privacy/integration boundary approved.
- [ ] Exact runtime mapping and Admin manageability approved.
- [ ] Staging/backup/restore/dry-run/reconciliation/rollback approved.
- [ ] Separate implementation/import/release authorization issued.

## Rejection Conditions

Reject generation or progression for missing source, invented value, unresolved required `TBD`, surviving template token, duplicate identity, uncontrolled term, multiple/no classification, invalid combination, local/category duplication, unsupported claim, price/transaction path, exposed protected data, missing reviewer, incompatible template version, broken reference, absent recovery, or unauthorized runtime action.

## Decision Template

- `GO` may apply only to the explicitly named next review stage.
- `NO-GO` applies to implementation/import until all relevant hard gates pass.
- A decision records scope, version, evidence, date, reviewer, approver, remaining risks, and expiry/review condition.

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Engine Rules](ENGINE_RULES.md)
- [Engine Workflow](ENGINE_WORKFLOW.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
