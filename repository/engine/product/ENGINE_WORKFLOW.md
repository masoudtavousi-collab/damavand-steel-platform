# Product Engine Workflow

## Document Control

- **Document ID:** `repository/engine/product/ENGINE_WORKFLOW.md`
- **Status:** Review
- **Authority:** Product Engine Standard
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Enterprise Architect, Quality Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On workflow stage, handoff, gate, output, responsibility, or engine-version change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md) and [Engine Rules](ENGINE_RULES.md)
- **Dependencies:** [Enterprise Product Engine](PRODUCT_ENGINE.md), [Engine Rules](ENGINE_RULES.md), and all Product Engine templates
- **Related Documents:** [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md) and [Validation Template](VALIDATION_TEMPLATE.md)
- **Traceability:** CP-001 through CP-010, PDM/WCM/TAX/ATT/INQ/SEOENT/FIELD/PLUG, Sprint 03D
- **AI Compatibility:** AI-readable workflow; handoffs and approvals remain human-controlled
- **Approval:** Pending Founder review; workflow does not authorize runtime execution

## Purpose

Define the repeatable handoff sequence from a Product Family idea to a separately controlled release without allowing templates to bypass evidence, approval, or implementation boundaries.

## Workflow

```text
Idea
  ↓
Family
  ↓
Attributes
  ↓
Variations
  ↓
Validation
  ↓
Import
  ↓
WooCommerce
  ↓
SEO
  ↓
QA
  ↓
Release
```

Sprint 03D defines this workflow only. Import, WooCommerce, SEO publication, QA runtime execution, and release require later exact authorizations.

## Stage Contracts

| Stage | Inputs | Template/output | Required gate | Stop condition |
| --- | --- | --- | --- | --- |
| Idea | Founder request and problem statement | Intake facts embedded in family draft | Scope and owner confirmed | Family purpose/authority absent |
| Family | Approved intake sources | Product Family Template output | Identity, scope, parent strategy, inquiry/no-price review | Invented hierarchy/name/claim |
| Attributes | Field inventory and family contract | Attribute Template output | Every field classified once; definitions/values sourced | Duplicate/unclassified/uncontrolled field |
| Variations | Approved variation-class fields | Variation Template output | Axes/values/combination method approved | Cartesian expansion or missing domain evidence |
| Validation | Complete generated set | Validation Template output | Structural/domain/governance checks pass | Required `TBD`, conflict, prohibited data |
| Import | Validated contracts | Import Template output and non-mutating mapping preview later | Exact schema/mapping and recovery plan approved | Placeholder IDs/SKUs, commercial unknowns, no rollback |
| WooCommerce | Approved import candidate and verified target | Separately approved configuration/import activity | Runtime capability, Admin, inquiry/no-price evidence | No authorization or incompatible target |
| SEO | Approved public facts/entity/URL decisions | SEO Template output then separate publication activity | Intent/canonical/content/schema/link review | Duplicate intent, `TBD` slug, unsupported claim |
| QA | Approved staging result | Quality evidence | Functional, data, mobile RTL, accessibility, SEO, security, performance, recovery pass | Any blocking failure |
| Release | Accepted QA/reconciliation evidence | Separate release record | Founder release approval and rollback readiness | Incomplete acceptance or recovery |

## Responsibilities

| Role | Workflow responsibility |
| --- | --- |
| Founder | Scope and final approval authority at defined gates |
| Product Data Owner | Family set coordination, identities, classification, consistency |
| Qualified Domain Reviewer | Definitions, units, values, combinations, technical claims |
| Sales/Operations Reviewer | Commercial evidence and inquiry workflow boundaries |
| SEO/Content Reviewer | Intent, canonical, content, links, metadata, schema eligibility |
| CRM/Privacy/Security Reviewer | Protected fields, consent, access, retention, integration risks |
| WooCommerce Technical Reviewer | Logical/runtime mapping, Admin manageability, compatibility |
| Quality/Repository Reviewer | Template compliance, links, traceability, tests, recovery evidence |

Role names are accountability placeholders until Founder assignment. A technical role cannot approve business/domain facts.

## Handoff Package

Every handoff includes:

- Family/set ID and version.
- Engine and template versions.
- Inputs and source evidence.
- Generated outputs and change summary.
- Passed, pending, blocked, failed, and not-run checks.
- Open `TBD` items and owners.
- Compatibility impact and affected consumers.
- Explicit permitted next action and prohibited actions.
- Reviewer/approver/date/conditions.

## Gate Rules

- A stage may be `GO` while later stages remain `NO-GO`.
- `GO` never broadens scope beyond its named next stage.
- Any required `TBD`, FAIL, BLOCKED, or required NOT RUN prevents progression.
- Templates provide no default approval, owner, value, or target mapping.
- A downstream consumer cannot repair an upstream source by inventing data.
- Changes discovered downstream return to the authoritative upstream asset and then regenerate/revalidate dependents.

## Failure and Rework Flow

```text
Failed gate
  -> stop and preserve evidence
      -> identify authoritative upstream source
          -> obtain approved correction
              -> regenerate affected outputs
                  -> rerun validation and dependent gates
```

No silent patching of generated output, WordPress object, CRM record, SEO metadata, or import row is permitted.

## Release Boundary

Release means an approved family-set version or separately implemented runtime change has passed its own acceptance criteria. Engine template approval alone does not release products. No Product Engine document creates a page, product, variation, taxonomy, attribute, field, SEO output, CRM record, import, or deployment.

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Engine Rules](ENGINE_RULES.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
