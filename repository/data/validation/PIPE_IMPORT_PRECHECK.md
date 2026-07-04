# Stainless Steel Pipe Import Precheck

## Document Control

- **Document ID:** `repository/data/validation/PIPE_IMPORT_PRECHECK.md`
- **Status:** Review
- **Authority:** Product Data Quality Gate
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Quality Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before any mapping approval, dry run, import authorization, or source-file change
- **Lifecycle:** Review
- **Source of Truth:** Current Sprint 03A pipe data assets and Sprint 03B mapping assets
- **Dependencies:** [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv), [Pipe Import Mapping](../imports/woocommerce/PIPE_IMPORT_MAPPING.md), [Pipe WooCommerce Mapping](../products/pipes/PIPE_WOOCOMMERCE_MAPPING.md), and [Product Data Validation Rules](PRODUCT_DATA_VALIDATION_RULES.md)
- **Related Documents:** [Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md), [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md), and [Attribute Dictionary](../attributes/ATTRIBUTE_DICTIONARY.md)
- **Traceability:** CP-001 through CP-010, PDM-001 through PDM-008, WCM-001 through WCM-008, ATT-001 through ATT-007, Sprint 03A, and Sprint 03B
- **AI Compatibility:** AI-readable deterministic quality gate; no inferred approvals, commercial values, or autonomous import
- **Approval:** Current result is `NO-GO FOR IMPORT`; Founder authorization remains unavailable until every hard gate passes

## Purpose

Provide a deterministic, non-mutating gate for deciding whether the Stainless Steel Pipe staging dataset may proceed to a separately authorized import dry run. This file does not run an import or approve WordPress changes.

## Result Vocabulary

| Result | Meaning |
| --- | --- |
| `PASS` | Current repository evidence satisfies the stated check |
| `PENDING` | Evidence or approval has not been supplied; no adverse value is inferred |
| `BLOCKED` | A known unresolved value or missing mandatory prerequisite prevents progression |
| `FAIL` | Supplied evidence violates the stated rule |
| `NOT RUN` | Requires an approved runtime/staging environment or separate execution activity |

`PENDING`, `BLOCKED`, `FAIL`, or required `NOT RUN` on any hard gate yields `NO-GO FOR IMPORT`.

## Hard-Stop Conditions

Stop precheck immediately if any of the following is detected:

- Any non-empty `public_price` value, price-bearing field, Offer data, or price claim.
- `inquiry_only` is not exactly `yes` on every row.
- A final required SKU is blank, duplicated, unapproved, or begins with `TBD-`.
- `stock_status` or another mandatory execution value remains `TBD`.
- An orphan variation, duplicate tuple, invalid controlled value, or unapproved combination exists.
- Category, attribute, term, or canonical identifiers would need to be invented or auto-created.
- Backup, staging, rollback, target capability, permissions, or Founder execution approval is absent.
- Any plan requires live WordPress mutation before a separately approved execution gate.

## Current Static Precheck

### File and Structure

| Check | Hard gate | Evidence | Result |
| --- | --- | --- | --- |
| Source file exists | Yes | `PIPE_IMPORT_TEMPLATE.csv` exists in the controlled repository path | `PASS` |
| CSV parseability | Yes | Four data rows parse against one header row | `PASS` |
| Encoding/character review | Yes | Current text is readable as UTF-8; full byte/normalization gate remains required for an execution file | `PASS` for current template shape |
| Exact header contract | Yes | 23 requested headers in the required order | `PASS` |
| Duplicate headers | Yes | No duplicate header in the current file | `PASS` |
| Row width | Yes | All four rows contain 23 fields | `PASS` |
| Formula/macro safety | Yes | No formula-leading value observed in the four placeholder rows | `PASS` |

### Parent and Variation Shape

| Check | Hard gate | Evidence | Result |
| --- | --- | --- | --- |
| Parent-row count | Yes | One placeholder `variable` row | `PASS` for template shape |
| Variation-row count | Yes | Three placeholder `variation` rows | `PASS` for template shape |
| Parent reference | Yes | All child rows use the same placeholder parent reference | `PASS` for template shape |
| Orphan variation | Yes | No orphan is visible within the four-row template | `PASS` for template shape |
| Duplicate five-axis tuple | Yes | Three sample tuples are distinct | `PASS` for template shape |
| Controlled variation values | Yes | Sample Grade, Finish, Diameter, Thickness, and Length values are within Sprint 03A sets | `PASS` for template shape |
| Approved commercial combinations | Yes | No approved valid-combination dataset exists | `BLOCKED` |
| Full product dataset | Yes | Current rows are explicitly placeholders, not a catalog | `BLOCKED` |

### Identity, Taxonomy, and Attributes

| Check | Hard gate | Evidence | Result |
| --- | --- | --- | --- |
| Stable family/parent/variation IDs | Yes | Remain `TBD` | `BLOCKED` |
| Final parent SKU | Yes | Current value begins with `TBD-` | `BLOCKED` |
| Final variation SKUs | Yes | Current values begin with `TBD-` | `BLOCKED` |
| SKU uniqueness against external/current systems | Yes | No approved baseline or lookup evidence supplied | `PENDING` |
| Canonical category/taxonomy mapping | Yes | Runtime destination and term ID remain `TBD` | `BLOCKED` |
| Global attribute/term mapping | Yes | Logical dictionary exists; runtime identities/terms do not | `BLOCKED` |
| Material/Grade/Finish terminology | Yes | Founder and qualified domain approval pending | `BLOCKED` |
| Canonical slug collision/reservation check | Yes | Canonical slug is `TBD`; no approved namespace evidence | `BLOCKED` |

### Commercial, Inquiry, and Pricing

| Check | Hard gate | Evidence | Result |
| --- | --- | --- | --- |
| `inquiry_only` | Yes | Exactly `yes` on all four rows | `PASS` |
| `public_price` | Yes | Empty on all four rows | `PASS` |
| Price/stock/supplier claims in sample rows | Yes | No price or supplier value; stock remains explicitly `TBD` | `PASS` for non-invention |
| Approved commercial availability | Yes | Not supplied | `BLOCKED` |
| Approved stock-state mapping | Yes | `stock_status=TBD` on every row | `BLOCKED` |
| Inquiry runtime capability | Yes | Mechanism and verified target behavior remain `TBD` | `BLOCKED` |
| Runtime no-price enforcement | Yes | No live target or runtime validation authorized | `NOT RUN` |

### SEO and Content

| Check | Hard gate | Evidence | Result |
| --- | --- | --- | --- |
| Approved canonical slug | Yes | `TBD` on all rows | `BLOCKED` |
| Approved SEO title/description | Publication gate | `TBD` on all rows | `BLOCKED` |
| Parent canonical ownership rule | Yes | Defined logically in Sprint 03A/Sprint 03B assets | `PASS` |
| No Offer/price schema | Yes | Mapping prohibits price/Offer targets | `PASS` at mapping-contract level |

### Target, Recovery, and Authorization

| Check | Hard gate | Evidence | Result |
| --- | --- | --- | --- |
| Verified target WooCommerce/importer version | Yes | Not supplied for this import | `PENDING` |
| Approved exact runtime column mapping | Yes | Logical mapping exists; runtime mapping approval pending | `BLOCKED` |
| Isolated staging target | Yes | Not authorized or evidenced | `PENDING` |
| Backup and proven restore | Yes | Not authorized or evidenced | `PENDING` |
| Dry-run preview | Yes | Import execution is prohibited in Sprint 03B | `NOT RUN` |
| Reconciliation and rollback plan | Yes | Product-import-specific evidence not approved | `PENDING` |
| Permissions and accountable operator | Yes | Not supplied | `PENDING` |
| Founder execution approval | Yes | Not supplied; file creation is not approval | `BLOCKED` |

## Required Pre-Execution Evidence

Before a future dry-run request can be considered, provide and approve:

1. Final family/parent/variation identities and SKU policy/values.
2. Founder/domain-approved terminology and a valid-combination dataset.
3. Verified commercial state values and responsible data owner; no inferred stock.
4. Approved taxonomy/category, global attributes, terms, canonical slug, and SEO metadata.
5. Verified inquiry capability and exhaustive no-public-price enforcement design.
6. Verified target/importer capabilities and an exact reviewed mapping preview.
7. Isolated staging, backup/restore evidence, rollback criteria, reconciliation expectations, and accountable operator.
8. Separate explicit Founder authorization for the dry run or import activity.

## Founder Review Checklist

- [ ] Approve family identity and Material/Grade/Finish terminology.
- [ ] Approve valid commercial combinations.
- [ ] Approve final SKU policy and values.
- [ ] Approve verified commercial-state vocabulary and owners.
- [ ] Approve taxonomy, attributes, terms, and canonical slug.
- [ ] Approve inquiry and no-price runtime acceptance criteria.
- [ ] Approve target mapping, staging, backup, rollback, and reconciliation evidence.
- [ ] Issue separate execution authorization.

Unchecked items are not approvals and must not be auto-completed.

## Current Decision

**NO-GO FOR IMPORT.**

The current files are ready for Founder, domain, Product Data, Sales, SEO, and WooCommerce mapping review. They are not ready for WordPress mutation, WooCommerce import, product publication, or commercial use.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03B non-mutating import precheck; current decision is `NO-GO FOR IMPORT`. |

## Navigation

- [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv)
- [Pipe Import Mapping](../imports/woocommerce/PIPE_IMPORT_MAPPING.md)
- [Pipe WooCommerce Mapping](../products/pipes/PIPE_WOOCOMMERCE_MAPPING.md)
- [Product Data Validation Rules](PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03B Audit](../../../docs/AUDIT_REPORT_SPRINT03B.md)
