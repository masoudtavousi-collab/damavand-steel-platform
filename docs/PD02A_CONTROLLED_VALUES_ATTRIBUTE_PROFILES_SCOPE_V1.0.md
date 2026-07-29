# PD-02A Controlled Values and Attribute Profiles Foundation Scope v1.0

## Document Control

- **Document ID:** `docs/PD02A_CONTROLLED_VALUES_ATTRIBUTE_PROFILES_SCOPE_V1.0.md`
- **Status:** Review
- **Authority:** Sprint Scope and Approval Packet
- **Owner:** Founder
- **Executor:** Codex controlled Build Engine
- **Independent Reviewer:** Codex independent read-only QA reviewer `/root/pd01_review_retry`, recorded as `PD02A-REVIEW-001`
- **Approval Authority:** Founder
- **Rollback Owner:** Repository Guardian through a separately visible corrective commit or Founder-approved revert
- **Version:** 1.0.1
- **Last Updated:** 2026-07-29
- **Lifecycle:** `REVIEW`
- **Decision ID:** `FD-PD02A-001`
- **Starting GitHub `main` SHA:** `d8ae556d17ab518970149533d975b7924f3af3e1`
- **Starting evidence:** merged PR #21 and successful required post-merge `repository-validation`
- **Authorized branch:** `codex/pd-02a-controlled-values-profile-foundation`
- **Approval:** Founder execution and conditional Git authorization recorded on 2026-07-29; legal `DRAFT → REVIEW` recorded after independent `PASS`

## Objective

Create a platform-independent, fail-closed Contract/Schema/Validator/Test
foundation for Product Attribute controlled-value registries and standalone
Attribute Profiles. PD-02A uses synthetic fixtures only and requires the two
new canonical registries and the existing Product Attribute registry to remain
empty.

PD-02A creates no canonical Family, Product Attribute, controlled term,
Attribute Profile, Product, Pilot, combination, Master Data, Golden package,
SKU, slug, availability, WordPress/WooCommerce object, import, runtime,
deployment, or production mutation.

## Exact 38-Path Allowlist

No tracked path outside this list may differ from the starting SHA.

### Technical paths — 24

1. `repository/data/contracts/product-attribute.contract.yaml`
2. `repository/data/schemas/product-attribute.schema.json`
3. `repository/data/validation/validate_product_attributes.py`
4. `repository/data/contracts/product-attribute-value-registry.contract.yaml`
5. `repository/data/schemas/product-attribute-value-registry.schema.json`
6. `repository/data/registries/product-attribute-value-registries.yaml`
7. `repository/data/validation/validate_product_attribute_values.py`
8. `repository/data/contracts/product-attribute-profile.contract.yaml`
9. `repository/data/schemas/product-attribute-profile.schema.json`
10. `repository/data/registries/product-attribute-profiles.yaml`
11. `repository/data/validation/validate_product_attribute_profiles.py`
12. `tests/fixtures/pd02/README.md`
13. `tests/fixtures/pd02/valid-synthetic-controlled-values.yaml`
14. `tests/fixtures/pd02/valid-synthetic-profile.yaml`
15. `tests/fixtures/pd02/invalid-unresolved-registry.yaml`
16. `tests/fixtures/pd02/invalid-orphan-profile.yaml`
17. `tests/fixtures/pd02/invalid-term-attribute-mismatch.yaml`
18. `tests/fixtures/pd02/invalid-duplicate-normalized-term.yaml`
19. `tests/fixtures/pd02/invalid-status-promotion.yaml`
20. `tests/fixtures/pd02/adversarial-permissive-schema.json`
21. `tests/fixtures/pd02/adversarial-remote-ref-schema.json`
22. `tests/fixtures/pd02/mutation-cases.json`
23. `tests/test_pd02_product_data.py`
24. `scripts/test.sh`

### Governance paths — 14

25. `docs/PD02A_CONTROLLED_VALUES_ATTRIBUTE_PROFILES_SCOPE_V1.0.md`
26. `docs/17_FOUNDER_DECISION_LOG.md`
27. `docs/CURRENT_PROJECT_STATE.md`
28. `docs/PROJECT_BASELINE.md`
29. `docs/IMPLEMENTATION_READINESS.md`
30. `docs/PROJECT_EXECUTION_ROADMAP.md`
31. `docs/REPOSITORY_HEALTH.md`
32. `docs/TRACEABILITY_MATRIX.md`
33. `docs/14_CHANGELOG.md`
34. `docs/18_OPEN_QUESTIONS.md`
35. `docs/08_DOCUMENTATION_INDEX.md`
36. `docs/READING_ORDER.md`
37. `docs/19_PRODUCT_DATA_MODEL.md`
38. `docs/22_PRODUCT_ATTRIBUTE_MODEL.md`

## Contract Boundary

- Product Attribute Contract `2.0.0` retains the approved PD-01 record shape
  and adds a PD-02A extension that requires stable `vreg:<12-lowercase-hex>`
  references without granting population authority.
- Product Attribute Value Registry Contract `1.0.0` defines stable registry
  and term identities, NFC normalization, aliases, ownership, reviewer
  separation, provenance, status, and closed record structure.
- Product Attribute Profile Contract `1.0.0` defines Family/Series scope,
  requiredness, visibility, variation/filter flags, inquiry/SEO use, typed or
  controlled value source, unit restrictions, precision, ownership, reviewer,
  provenance, and status.
- Profile scope, Attribute, Unit, and controlled-registry references must
  resolve. Cartesian generation remains forbidden.
- The contracts remain offline, deterministic, and side-effect free.

## Canonical Empty-Registry Boundary

The following canonical content must remain exact throughout PD-02A:

```yaml
# repository/data/registries/product-attributes.yaml
attributes: []

# repository/data/registries/product-attribute-value-registries.yaml
data_classification: CANONICAL_EMPTY
value_registries: []

# repository/data/registries/product-attribute-profiles.yaml
data_classification: CANONICAL_EMPTY
profiles: []
```

Nonempty content in any of these collections is an immediate stop condition.
Synthetic fixture IDs and labels are test inputs and cannot be promoted by
this Sprint.

## Test Contract

### Positive

- Validate both canonical empty registries and both synthetic fixtures.
- Validate strict Draft 2020-12 closed schemas with local references only.
- Resolve synthetic Profile scope, Attribute, controlled-registry, and Unit
  dependencies.
- Validate stable IDs, owner/reviewer separation, provenance, normalization,
  typed value source, requiredness, and use flags.
- Prove imports have no output or canonical side effect.
- Prove validation succeeds with network access disabled.
- Prove deterministic sorted errors and legal lifecycle history.

### Negative

- Reject unknown or orphan scope, Attribute, Unit, registry, and term
  references.
- Reject controlled registries attached to the wrong Attribute or value type.
- Reject duplicate IDs, keys, normalized labels, aliases, and terms.
- Reject missing owner, reviewer, provenance, required rule fields, invalid
  status promotion, role self-review, contradictory Profile behavior, invalid
  precision, and invalid Unit policy.
- Reject duplicate YAML/JSON keys, non-finite numbers, unknown fields, and
  direct `DRAFT → APPROVED`.

### Adversarial and destructive

- Reject permissive and remote-reference schemas.
- Reject path escape, symbolic links, oversized/deep input, Unicode
  normalization collisions, mass assignment, forged classification/evidence,
  registry substitution, and every Product/commercial/runtime field.
- Require at least 60 uniquely named negative/adversarial mutations.
- Prove no network and no external or repository side effects.

### Repository acceptance

- Parse every changed YAML and JSON with strict readers.
- Run targeted PD-02A tests and unified `make test`.
- Run `git diff --check`.
- Verify changed-path equality with this 38-path allowlist.
- Verify all three canonical collections remain empty.
- Scan for secrets, unexpected endpoints, and real Product/commercial data.
- Require successful branch CI, no conflict, independent `PASS`, and
  successful post-merge `main` CI.

## Independent Review History

### `PD02A-REVIEW-001` — DRAFT attempt 1

- **Reviewed commit:** `a6f7e095cc48dffb987f9a48b67c71e329ee7d3b`
- **Branch CI:** PASS, run `30469027782`
- **Findings:** Critical 0; High 2; Medium 2; Low 0
- **Verdict:** `REWORK`
- **High corrections required:** resolve controlled-value registries against a
  validated `CONTROLLED_TERM` Product Attribute and replace caller-asserted
  Profile scopes with validated Product Core dependencies.
- **Medium corrections required:** prevent Profiles from weakening an
  Attribute's declared registry/Unit/precision policy and reject aliases that
  collide with value codes.
- **Chronology:** lifecycle remains `DRAFT`; no promotion occurred. Corrections
  are limited to this exact 38-path allowlist and require independent
  re-review.

### `PD02A-REVIEW-001` — DRAFT attempt 2

- **Reviewer:** Codex independent read-only QA reviewer
  `/root/pd01_review_retry`
- **Reviewed commit:** `23e8ac2e16ca42cd43d4957298edbc18a7d8740f`
- **Branch CI:** PASS, run `30469883442`
- **Findings:** Critical 0; High 0; Medium 0; Low 0
- **Verdict:** `PASS`
- **Regression evidence:** all four prior findings are closed; targeted tests
  pass 16/16; the mutation matrix contains 71/71 unique cases; exact cumulative
  path equality is 38/38; all three canonical collections remain empty.
- **Boundary evidence:** closed local-only schemas, synthetic fixtures, and no
  secret, unexpected endpoint, real Product/commercial datum, or runtime
  change.
- **Chronology:** this independent `PASS` is the evidence for the legal
  `DRAFT → REVIEW` transition. Founder approval remains the separate
  `REVIEW → APPROVED` gate.

## Roles and Separation of Duties

| Role | Authority in PD-02A |
| --- | --- |
| Founder | Authorizes exact scope, lifecycle promotion, Git publication, ready-for-review, and conditional Merge Commit |
| Codex controlled Build Engine | Implements and validates only the exact allowlist; cannot independently review or approve its own work |
| Independent QA reviewer | Performs read-only diff, lifecycle, schema, validator, test, security, and prohibition review as `PD02A-REVIEW-001` |
| Repository Guardian | Confirms path equality, chronology, empty registries, rollback traceability, and no business-data promotion |
| CI service | Repeats deterministic repository validation; passing CI is evidence, not approval |

Product Data Steward and Qualified Steel-Domain Reviewer are intentionally not
assigned by PD-02A because no real data enters the registries. Their assignment
is mandatory before PD-02B.

## Legal Lifecycle

| State | Entry evidence | Exit requirement |
| --- | --- | --- |
| `DRAFT` | Founder execution approval, exact starting SHA, 38-path allowlist, synthetic-only boundary | Local tests pass, Draft PR exists, branch CI passes, independent review starts |
| `REVIEW` | `DRAFT → REVIEW` recorded with `PD02A-REVIEW-001` | Independent `PASS`, all in-scope corrections complete, tests/CI pass, registries remain empty |
| `APPROVED` | `REVIEW → APPROVED` recorded with `FD-PD02A-001` and Founder authorization | PR may leave Draft only while every conditional Git gate remains satisfied |

Direct `DRAFT → APPROVED` is invalid and must fail validation.

## Git Controls

- Work only on `codex/pd-02a-controlled-values-profile-foundation`.
- Stage exactly the allowlisted paths; no force-push or history rewrite.
- Open the PR as Draft.
- Permit corrections only inside the same 38 paths.
- Require branch CI, no conflict, independent `PASS`, Founder authorization,
  exact path equality, and empty-registry evidence before ready-for-review.
- Merge method is Merge Commit only.
- Verify required CI again on `main`.
- Branch deletion is prohibited.

## Stop Conditions

Stop and report `NO-GO` if:

- any changed path falls outside the allowlist;
- any canonical Product Attribute, controlled-value, or Profile registry is
  nonempty;
- any real Family, Product, Attribute, term, Profile, Pilot, 879-row set,
  Master Data, Golden data, combination, SKU, slug, availability, price, stock,
  or commercial fact appears;
- any WordPress/WooCommerce, import, Admin UI, runtime, deployment, production,
  external-write, or branch-deletion action is required;
- lifecycle history skips `REVIEW` or lacks review evidence;
- validation is nondeterministic or fail-open;
- test/CI, independent review, conflict, scope, secret, credential, or
  authority checks fail.

## GO / NO-GO

- **Completed DRAFT gate:** exact-scope implementation, in-scope corrections,
  local tests, Draft PR #22, CI runs `30469027782` and `30469883442`, and
  independent `PD02A-REVIEW-001` PASS.
- **Current REVIEW gate:** repeat validation and CI with the legal lifecycle
  record while preserving exact path equality and empty canonical registries.
- **GO:** exact PD-02A synthetic Contract/Schema/Validator/Test work and its
  remaining conditional Git lifecycle.
- **NO-GO:** PD-02B canonical population; Family identity; real Attribute,
  controlled term, or Profile data; PD-03; Product/SKU; WordPress/WooCommerce;
  import; runtime; deploy; production; branch deletion.

## Change History

| Version | Date | State | Change |
| --- | --- | --- | --- |
| 1.0.1 | 2026-07-29 | `REVIEW` | Recorded attempt-1 `REWORK`, the four exact-scope corrections, attempt-2 `PD02A-REVIEW-001` PASS on Commit `23e8ac2`, CI run `30469883442`, and the legal `DRAFT → REVIEW` transition. |
| 1.0.0 | 2026-07-29 | `DRAFT` | Created the exact 38-path, synthetic-only PD-02A foundation scope and recorded Founder execution and conditional Git authorization. |
