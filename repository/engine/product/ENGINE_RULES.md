# Product Engine Rules

## Document Control

- **Document ID:** `repository/engine/product/ENGINE_RULES.md`
- **Status:** Review
- **Authority:** Product Engine Standard
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Enterprise Architect, Repository Guardian, Quality Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On naming, versioning, folder, template, review, approval, change, compatibility, or repository-convention change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md), Repository Implementation Rules, Engineering Guidelines, and repository governance
- **Dependencies:** [Enterprise Product Engine](PRODUCT_ENGINE.md) and [Repository Implementation Rules](../../IMPLEMENTATION_RULES.md)
- **Related Documents:** [Engine Workflow](ENGINE_WORKFLOW.md), [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md), and all Product Engine templates
- **Traceability:** CP-001 through CP-010, S01A-001 through S01A-010, PDM/WCM/TAX/ATT/INQ/SEOENT/FIELD/PLUG, Sprint 03D
- **AI Compatibility:** AI-readable engine governance; AI may assist deterministic drafting/validation but cannot supply facts or approvals
- **Approval:** Pending Founder review; rules do not authorize product/runtime implementation

## Purpose

Govern naming, versioning, folder structure, review, approval, change control, backward compatibility, and repository behavior for all template-generated product families.

## Core Rules

1. Every new family starts from the current approved Product Engine templates.
2. No family asset is authored from a blank document or copied from another family as its source structure.
3. Generated outputs record engine/template provenance and source evidence.
4. Unknown data is `TBD`; templates never provide business defaults.
5. Governing documents and Founder/domain evidence outrank engine templates and generated outputs.
6. Pipe is an implementation example, never a universal value source.
7. Product generation and WordPress/WooCommerce implementation are separate authorizations.

## Naming

### Engine Files

The task-defined canonical engine filenames are:

- `PRODUCT_ENGINE.md`
- `PRODUCT_FAMILY_TEMPLATE.md`
- `ATTRIBUTE_TEMPLATE.md`
- `VARIATION_TEMPLATE.md`
- `IMPORT_TEMPLATE.md`
- `SEO_TEMPLATE.md`
- `VALIDATION_TEMPLATE.md`
- `ENGINE_RULES.md`
- `ENGINE_WORKFLOW.md`
- `ENGINE_GENERATION_GUIDE.md`

### Generated Family Files

| Artifact | Pattern |
| --- | --- |
| Family | `{{FAMILY_KEY}}_PRODUCT_FAMILY.md` |
| Attributes/classification | `{{FAMILY_KEY}}_ATTRIBUTE_MODEL.md` |
| Variations | `{{FAMILY_KEY}}_VARIATION_MODEL.md` |
| Import contract | `{{FAMILY_KEY}}_IMPORT_MODEL.md` |
| SEO | `{{FAMILY_KEY}}_SEO_MODEL.md` |
| Validation | `{{FAMILY_KEY}}_VALIDATION.md` |

`FAMILY_KEY` is a stable approved uppercase ASCII identifier. Family folders use approved lowercase ASCII kebab-case. Persian display labels remain data, not filenames/slugs. This is an engine-specific controlled convention; it does not change the general repository naming rule outside the engine.

## Versioning

- Engine package version is the version of `PRODUCT_ENGINE.md` and coordinated rules/workflow compatibility.
- Every template has its own semantic document version.
- Generated assets record engine version plus exact template ID/version.
- Generated family-set version is distinct from repository, template, WordPress, plugin, import, and release versions.
- Patch: clarification/validation compatible with existing generated structure.
- Minor: backward-compatible optional section/field or stricter non-breaking validation.
- Major: incompatible required structure, semantics, classification, or pipeline contract requiring migration.
- Version changes require change notes, compatibility impact, affected families, migration/validation, and Founder approval.

## Folder Structure

```text
repository/
├── engine/product/                 canonical engine rules and templates
└── data/
    ├── products/<family-folder>/   generated family and variation contracts
    ├── attributes/                 generated family/global attribute contracts
    ├── taxonomies/                 generated family category/classification contracts
    ├── imports/woocommerce/        generated import contracts and later approved staging schemas
    ├── seo/                        generated SEO entity contracts
    ├── validation/                 generated validation/governance contracts
    └── templates/                  reserved; not a second Product Engine template authority
```

No second template set may be created under `repository/data/templates/`. That folder remains reserved for future generated/data-level artifacts only if explicitly approved.

## Template Provenance

Every generated asset records:

- Engine name/version.
- Template ID/version.
- Generation date and authorized task.
- Family ID/key and generated asset version.
- Governing sources and family evidence.
- Owner, reviewers, status, approval, and unresolved items.
- Compatibility/migration notes when regenerated.

An asset lacking provenance fails the engine validation gate.

## Review Gates

| Gate | Required reviewers |
| --- | --- |
| Structure/provenance | Repository Guardian and Product Data Owner |
| Family identity/hierarchy | Founder, Product Data Owner, qualified domain reviewer |
| Attributes/variations | Product Data, domain, Sales/Operations, WooCommerce reviewer |
| Inquiry/no-price | Founder, Sales, security/privacy, WooCommerce reviewer |
| SEO | Founder, SEO, content, qualified domain reviewer |
| CRM/integrations | Founder, Sales, privacy/security, integration reviewer |
| Import/release | Founder, quality, operations, security, WooCommerce reviewer |

Reviewers validate evidence; only the Approval Authority changes approval state.

## Approval Process

1. Generated set enters Draft/Review.
2. Structural validation checks template compliance and unknowns.
3. Specialist findings are resolved or recorded as blockers.
4. Founder reviews the decision/evidence matrix.
5. Approval is recorded with date, version, scope, and conditions.
6. Separate implementation/import/release approvals remain required.

Silence, file creation, conversation output, AI completion, or unchecked checklist items are not approval.

## Change Control

- Modify canonical templates only through an explicit Product Engine change task.
- Record reason, affected templates, affected generated families, compatibility class, migration, validation, rollback, and approval.
- Never edit a template to accommodate one family when an existing extension point suffices.
- A genuinely new reusable concept requires engine review; a family-only concept belongs in its generated asset under the appropriate classification.
- Regeneration produces a reviewed change, not silent overwrite.
- Preserve stable IDs and approved facts; compare generated diff before acceptance.

## Backward Compatibility

- Existing Pipe assets remain valid implementation examples and are not renamed or rewritten in Sprint 03D.
- Engine v0.1.0 documents a mapping from future standard outputs to existing Pipe responsibilities; filename identity need not match.
- New optional template sections must have defined absence behavior for older family sets.
- New required sections/semantic changes require a major version and family migration plan.
- Deprecated templates identify replacement and support window; they are not deleted while active family assets depend on them.
- Runtime storage/plugin formats never define the canonical engine contract.

## Repository Conventions

- Markdown only for Sprint 03D; no scripts, generators, WordPress code, plugin code, configuration, CSV rows, or databases.
- Complete controlled metadata and relative cross-references.
- One source authority per fact and one primary classification per field.
- Persian labels plus stable English internal keys where applicable.
- No secrets, personal/customer data, prices, stock values, supplier data, final SKUs, executable content, or production artifacts.
- Update Index, Navigation, Traceability, Knowledge Graph, and Health when engine inventory changes.
- Audit current-state evidence without unsupported historical or maturity claims.

## Quality and Stop Conditions

Stop when templates conflict with governing rules, family input is insufficient, classification duplicates authority, a template token survives review-ready output, backward compatibility is unknown, mandatory reviewer/approval is missing, or implementation/import would be required to complete the task.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03D Product Engine rules. |

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Engine Workflow](ENGINE_WORKFLOW.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
