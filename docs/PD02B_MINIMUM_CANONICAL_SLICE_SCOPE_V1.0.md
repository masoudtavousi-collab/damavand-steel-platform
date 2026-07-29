# PD-02B Minimum Canonical Slice Scope v1.0

**Decision ID:** `FD-PD02B-001`

**Lifecycle:** `DRAFT`

**Baseline:** `main@6ed6fc89e555b1be3a97d7f9c64c9e2b989af1df`

**Authority:** Founder-approved repository-only Product Data enablement

**Runtime authority:** None

## Objective

Create the smallest traceable canonical Product Data slice needed to prove the
repository contracts, closed schemas, offline validators, evidence controls, and
legal `DRAFT → REVIEW → APPROVED` lifecycle. This is not a Product catalog
population, commerce model, import package, or publication authorization.

## Exact Canonical Slice

- 3 Product Entity records: Catalog → Platform → Family.
- 2 Attributes: `material` and `grade`.
- 2 controlled Value Registries.
- 4 Controlled Terms: `stainless_steel`, `201`, `304`, and `316`.
- 1 Family-scoped Attribute Profile.
- 18 localized labels: Persian and English for exactly 9 identities.
- 1 machine-readable Approval Evidence record.
- 31 unique stable IDs allocated as 12 lowercase hexadecimal values with a
  collision check; identifiers are independent of labels, slugs, SKU, or runtime.

## Approved Names

| Subject | Persian | English |
| --- | --- | --- |
| Catalog | کاتالوگ محصولات دماوند استیل | Damavand Steel Product Catalog |
| Platform | محصولات فولاد زنگ‌نزن (استنلس استیل) | Stainless Steel Products |
| Family | لوله استیل | Stainless Steel Pipe |
| Material Attribute | جنس | Material |
| Material Term | فولاد زنگ‌نزن | Stainless Steel |
| Grade Attribute | گرید فولاد | Steel Grade |
| Grade Terms | `201`, `304`, `316` | `201`, `304`, `316` |

`استیل` is the sole common Persian alias for the `stainless_steel` Material
Term. No application, performance, standards, safety, inventory, or commercial
claim is authorized.

## Profile Boundary

Material and Grade are `REQUIRED` only in the repository-internal Family
Profile. Every rule must remain:

- `public_visibility: INTERNAL`
- `variation_axis: false`
- `filtering: false`
- `inquiry_use: NOT_USED`
- `seo_use: PROHIBITED`
- `value_source: CONTROLLED_REGISTRY`
- no Unit and no precision

## Roles and Evidence

- Decision authority: `Founder پروژه Damavand Steel`.
- Product Data Steward and executor role: `product-data-steward`.
- Repository Guardian/QA/Rollback role: `repository-guardian`.
- Material review: `SS-MATERIAL-REVIEWER-02`, Material scope only, PASS.
- Grade review: `SS-INDEPENDENT-REVIEWER-20Y-01`, Grade scope only, PASS.
- Independent technical review: `PD02B-TECH-REVIEW-001`, required before REVIEW.
- Final Founder approval evidence: required before APPROVED.
- AI/Codex is an assisting tool and is not a domain reviewer or decision authority.

The Approval Evidence binds the five canonical data registries by SHA-256,
records review scope and independence, and rejects premature or replayed final
approval.

## Lifecycle

1. `DRAFT`: canonical records exist only as `CANDIDATE_UNVERIFIED`; technical
   review is `PENDING`; final approval fields are null; anti-replay nonce is
   unconsumed.
2. `REVIEW`: allowed only after `PD02B-TECH-REVIEW-001` PASS; records remain
   `CANDIDATE_UNVERIFIED`; final Founder approval is still absent.
3. `APPROVED`: allowed only after explicit Founder approval; canonical records
   become `APPROVED`, evidence is complete, and the approval nonce is consumed.

Direct `DRAFT → APPROVED` is prohibited. Passing tests alone never promotes data.

## Independent Review History

- `PD02B-TECH-REVIEW-001` attempt 1 reviewed Commit
  `b9f8b5d4bc475a0c137ef3c29cacd0c7a2b68dea` and returned `REWORK`
  with Critical 0, High 0, Medium 1, Low 0.
- The finding identified that the declared 20-case mutation manifest was counted
  but not dispatched through real validators, and that the permissive-schema
  assertion did not exercise the schema loader.
- The DRAFT correction executes all 20 mutations against temporary copies of the
  canonical datasets/contracts, asserts each expected fail-closed code, and
  routes permissive and remote-reference schemas through the real loader.
- Lifecycle remains `DRAFT`; attempt 2 must independently return `PASS` before
  any transition to REVIEW.

## Exact Allowlist

Only these 57 paths may change:

1. `repository/data/contracts/product-core.contract.yaml`
2. `repository/data/registries/product-entities.yaml`
3. `repository/data/validation/validate_product_core.py`
4. `repository/data/contracts/product-attribute.contract.yaml`
5. `repository/data/schemas/product-attribute.schema.json`
6. `repository/data/registries/product-attributes.yaml`
7. `repository/data/validation/validate_product_attributes.py`
8. `repository/data/contracts/product-attribute-value-registry.contract.yaml`
9. `repository/data/schemas/product-attribute-value-registry.schema.json`
10. `repository/data/registries/product-attribute-value-registries.yaml`
11. `repository/data/validation/validate_product_attribute_values.py`
12. `repository/data/contracts/product-attribute-profile.contract.yaml`
13. `repository/data/schemas/product-attribute-profile.schema.json`
14. `repository/data/registries/product-attribute-profiles.yaml`
15. `repository/data/validation/validate_product_attribute_profiles.py`
16. `repository/data/contracts/product-data-localized-labels.contract.yaml`
17. `repository/data/schemas/product-data-localized-labels.schema.json`
18. `repository/data/registries/product-data-localized-labels.yaml`
19. `repository/data/validation/validate_product_data_localized_labels.py`
20. `repository/data/contracts/product-data-approval-evidence.contract.yaml`
21. `repository/data/schemas/product-data-approval-evidence.schema.json`
22. `repository/data/registries/product-data-approval-evidence.yaml`
23. `repository/data/validation/validate_product_data_approval_evidence.py`
24. `repository/data/validation/validate_pd02b_canonical_slice.py`
25. `tests/fixtures/pd02b/README.md`
26. `tests/fixtures/pd02b/valid-synthetic-localized-labels.yaml`
27. `tests/fixtures/pd02b/valid-synthetic-approval-evidence.yaml`
28. `tests/fixtures/pd02b/invalid-missing-domain-approval.yaml`
29. `tests/fixtures/pd02b/invalid-approval-replay.yaml`
30. `tests/fixtures/pd02b/invalid-unicode-confusable-label.yaml`
31. `tests/fixtures/pd02b/adversarial-permissive-schema.json`
32. `tests/fixtures/pd02b/adversarial-remote-ref-schema.json`
33. `tests/fixtures/pd02b/mutation-cases.json`
34. `tests/test_pd02b_product_data.py`
35. `scripts/test.sh`
36. `docs/PD02B_MINIMUM_CANONICAL_SLICE_SCOPE_V1.0.md`
37. `docs/17_FOUNDER_DECISION_LOG.md`
38. `docs/CURRENT_PROJECT_STATE.md`
39. `docs/PROJECT_BASELINE.md`
40. `docs/IMPLEMENTATION_READINESS.md`
41. `docs/PROJECT_EXECUTION_ROADMAP.md`
42. `docs/REPOSITORY_HEALTH.md`
43. `docs/TRACEABILITY_MATRIX.md`
44. `docs/14_CHANGELOG.md`
45. `docs/18_OPEN_QUESTIONS.md`
46. `docs/08_DOCUMENTATION_INDEX.md`
47. `docs/READING_ORDER.md`
48. `docs/19_PRODUCT_DATA_MODEL.md`
49. `docs/22_PRODUCT_ATTRIBUTE_MODEL.md`
50. `docs/21_PRODUCT_TAXONOMY_MODEL.md`
51. `docs/11_GLOSSARY.md`
52. `repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md`
53. `repository/data/attributes/ATTRIBUTE_DICTIONARY.md`
54. `repository/data/attributes/PIPE_ATTRIBUTE_MODEL.md`
55. `repository/data/validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md`
56. `tests/test_pd02_product_data.py`
57. `tests/test_product_master_data.py`

## Explicitly Deferred or Prohibited

- Grade `430`.
- Finish, Color, PVD, dimensions, and Units.
- Three real Pilots and 879 rows.
- Master Data and Golden Package.
- Product, SKU, slug, and availability.
- SEO, filtering, variation generation, inquiry, and commerce authority.
- WordPress, WooCommerce, import, runtime, deployment, and production.
- Branch deletion.

## Validation and Stop Conditions

Stop without promotion or merge if any of the following occurs:

- any changed path is outside the exact allowlist;
- a test or required CI check fails;
- conflict, scope drift, unstable identity, unresolved reference, or hash mismatch;
- direct lifecycle transition, premature `APPROVED` status, missing review evidence,
  forged reviewer, or approval replay;
- permissive/remote schema behavior, Unicode confusable, duplicate normalized label,
  or stable-ID collision;
- any deferred/prohibited data or any runtime/production effect.

## Git Boundary

The authorized cycle permits a dedicated Branch, scoped Commit, Push, Draft PR,
allowlisted review corrections, independent technical review, legal lifecycle
transitions, final Founder approval, and—only with all checks green, no conflict,
no scope drift, and PASS review—Ready for Review and Merge Commit. The Branch
must not be deleted.
