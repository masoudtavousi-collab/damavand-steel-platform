# BP2 Data Administration Scope v1.0

## Document control

- **Document ID:** `docs/BP2_DATA_ADMINISTRATION_SCOPE_V1.0.md`
- **Status:** Approved
- **Authority:** Governing within the documentation-only BP2 Data Administration scope
- **Owner:** Founder
- **Reviewers:** Chief Architect / Product Owner / QA; Repository Guardian
- **Approval Authority:** Founder
- **Version:** 1.0.0
- **Last Updated:** 2026-07-28
- **Lifecycle:** Approved
- **Decision ID:** `FD-BP2-ADM-001`
- **Review Record:** `BP2-ADM-REVIEW-001`
- **Execution Authority:** Documentation and machine-readable contracts only
- **Implementation Authority:** `false`
- **Approval:** `FD-BP2-ADM-001`; Founder approved the ordered `DRAFT → REVIEW → APPROVED` lifecycle on 2026-07-28 after successful review

## Purpose

Define the governed administration boundary for BP2 pipe master data without implementing an administration panel, creating Product/SKU records, changing WordPress/WooCommerce, importing data, publishing, or deploying.

## Canonical boundary

The hierarchy remains:

`Catalog → Platform → Family → Series → Variant Rules → SKU`

This scope administers evidence-backed registry values and valid-combination rules. It does not promote candidates to approved truth and does not generate a Cartesian product of variants.

## Governed registries

Every registry exposes the same administrative capabilities: `ADD`, `EDIT`, and `DELETE_OR_ARCHIVE`.

1. Material
2. Grade
3. Diameter / size
4. Thickness
5. Color / finish
6. Surface / design
7. Branch length
8. Sales and calculation units
9. Supply status
10. Valid-combination rules
11. Pilot combinations
12. Provenance / evidence

## Mutation governance

- Soft delete is the default.
- Every mutation requires actor, timestamp, reason, before/after snapshots, and evidence reference.
- History is preserved.
- Cascade deletion is forbidden.
- Dependencies must be checked before archive/delete.
- Deletion of an approved record requires Founder approval.
- Physical deletion is limited to unused erroneous drafts with audit evidence.
- Archival is lifecycle metadata, not a new governance status.

## Status vocabulary

Only these statuses are valid:

- `APPROVED`
- `CANDIDATE_UNVERIFIED`
- `MISSING_DATA_VALUE`
- `FOUNDER_INPUT_REQUIRED`
- `DEFERRED`
- `NOT_APPLICABLE`
- `INVALID`

## Pipe-family administration rules

- Active administered grades: 201, 304, 316.
- Grade 430 remains excluded from active administration and is `DEFERRED`; this does not rewrite the source blueprint.
- Base branch lengths: 3 m and 6 m; custom lengths remain inquiry-only.
- Sales and inquiry unit: branch.
- Technical calculation unit: meter.
- Thickness must not appear in product names or categories.
- Three approved pilot combinations remain unchanged.
- The 879 historical candidates remain unverified and are not promoted.
- Aluminum and iron thickness administration is `NOT_APPLICABLE` in v1.
- Sheet administration is `DEFERRED`.

## Smart Inquiry order

1. Family
2. Material
3. Alloy / grade
4. Size / diameter
5. Valid thickness
6. Color / finish
7. Surface / design
8. Length

## Future administration experience

The future panel is specified as Persian RTL and mobile-first. It should provide registry counts, status filters, search, add/edit/archive actions, dependency previews, combination previews, audit history, and a Founder approval queue.

This document does not authorize or implement that panel.

## Acceptance criteria

- All 12 registries are represented by machine-readable administration contracts.
- Add, edit, and soft-delete/archive policies are deterministic.
- Audit and dependency requirements are mandatory.
- Only approved combinations are selectable.
- Candidate records cannot be promoted automatically.
- Three approved pilots and 879 candidates reconcile with the source blueprint.
- Automated validation fails on forbidden implementation authority or scope expansion.
- No Product/SKU, WordPress/WooCommerce, import, publication, deployment, or production mutation is introduced.

## Lifecycle review record

| Field | Recorded value |
| --- | --- |
| Document | `docs/BP2_DATA_ADMINISTRATION_SCOPE_V1.0.md`, version 1.0.0 |
| Change scope | Lifecycle evidence and fail-closed Contract/Schema/Validator/Test hardening only |
| Reviewers | Chief Architect / Product Owner / QA; Repository Guardian |
| Evidence | Contract, closed Draft 2020-12 schema, deterministic offline validator, 12 positive/negative/adversarial test methods, 51 mutation cases, local `make test`, merged PR #18, and successful protected Review-stage, final-PR, and post-merge `main` CI |
| Findings | No blocking findings; direct `DRAFT → APPROVED` remains forbidden and is tested |
| Exceptions | None |
| Outcome | Pass |
| Proposed lifecycle | Approved |
| Approval | `FD-BP2-ADM-001`; Founder authorization and approval dated 2026-07-28 |

## Stop conditions

Stop and request separate Founder approval before:

- implementing an administration UI;
- creating or mutating Product/SKU records;
- changing WordPress/WooCommerce;
- importing source data;
- publishing or deploying;
- promoting any candidate value;
- expanding administration beyond this contract.

## Rollback

The change is documentation and validation only. Rollback consists of reverting the commit that introduces this scope, contract, schema, validator, and test hook.
