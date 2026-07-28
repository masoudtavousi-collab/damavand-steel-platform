# PD-01 Product Data Contract Enablement Scope v1.0

## Document Control

- **Document ID:** `docs/PD01_PRODUCT_DATA_CONTRACT_SCOPE_V1.0.md`
- **Status:** Draft
- **Authority:** Sprint Scope and Approval Packet
- **Owner:** Founder
- **Executor:** Codex Build Engine in the Founder-authorized PD-01 task
- **Independent Reviewer:** Separate read-only QA agent; evidence record `PD01-REVIEW-001` must identify the assigned reviewer before `REVIEW`
- **Approval Authority:** Founder
- **Rollback Owner:** Repository Guardian, acting only through a separately visible corrective commit or revert approved by the Founder
- **Version:** 1.0.0
- **Last Updated:** 2026-07-28
- **Lifecycle:** `DRAFT`
- **Decision ID:** `FD-PD01-001`
- **Starting GitHub `main` SHA:** `6577cd461e88463903b18c11b0e5bdbfa88375e2`
- **Starting evidence:** merged PR #20 and successful required check `repository-validation`, Actions run `30376465378`
- **Authorized branch:** `codex/pd-01-product-data-contract-enablement`
- **Approval:** Execution and the conditional Git/lifecycle cycle were authorized by the Founder on 2026-07-28; technical acceptance is not established while this packet is `DRAFT`

## Objective

Enable a platform-independent, machine-readable Product Data contract boundary for synthetic validation only. PD-01 defines Attribute Profiles, typed Product Value Assignments, and explicit Variant Rule Set combinations; hardens Product Attribute validation; and proves the boundary with positive, negative, boundary, cross-file, and adversarial tests.

PD-01 does not populate canonical Product Data. It creates no real Product, Product Attribute definition, SKU, commercial combination, Master Data package, Golden package, WordPress/WooCommerce object, import asset, runtime configuration, deployment, or production mutation.

## Exact 30-Path Allowlist

No tracked file outside this list may differ from the starting SHA.

### Technical paths — 17

1. `repository/data/contracts/product-attribute.contract.yaml`
2. `repository/data/schemas/product-attribute.schema.json`
3. `repository/data/registries/product-attributes.yaml`
4. `repository/data/validation/validate_product_attributes.py`
5. `tests/fixtures/product-attributes/valid-foundation.yaml`
6. `tests/fixtures/product-attributes/valid-measured-attribute.yaml`
7. `tests/fixtures/product-attributes/invalid-naming.yaml`
8. `repository/data/contracts/product-master-data.contract.yaml`
9. `repository/data/schemas/product-master-data.schema.json`
10. `repository/data/validation/validate_product_master_data.py`
11. `tests/fixtures/product-master-data/valid-synthetic-minimal.yaml`
12. `tests/fixtures/product-master-data/invalid-duplicate-key.yaml`
13. `tests/fixtures/product-master-data/adversarial-permissive-schema.json`
14. `tests/fixtures/product-master-data/adversarial-remote-ref-schema.json`
15. `tests/fixtures/product-master-data/mutation-cases.json`
16. `tests/test_product_master_data.py`
17. `scripts/test.sh`

### Governance paths — 13

18. `docs/PD01_PRODUCT_DATA_CONTRACT_SCOPE_V1.0.md`
19. `docs/17_FOUNDER_DECISION_LOG.md`
20. `docs/CURRENT_PROJECT_STATE.md`
21. `docs/PROJECT_BASELINE.md`
22. `docs/IMPLEMENTATION_READINESS.md`
23. `docs/PROJECT_EXECUTION_ROADMAP.md`
24. `docs/REPOSITORY_HEALTH.md`
25. `docs/TRACEABILITY_MATRIX.md`
26. `docs/14_CHANGELOG.md`
27. `docs/18_OPEN_QUESTIONS.md`
28. `docs/08_DOCUMENTATION_INDEX.md`
29. `docs/READING_ORDER.md`
30. `docs/19_PRODUCT_DATA_MODEL.md`

## Contract Boundary

- Product Attribute Contract advances in place from `1.0.0` to `2.0.0` to support strict entry validation while the canonical Product Attribute registry remains empty.
- Product Master Data Contract `1.0.0` accepts only `SYNTHETIC_FIXTURE` bundles.
- Stable IDs use explicit type prefixes plus twelve lowercase hexadecimal characters. Allocation policy is cryptographically secure random generation with a collision check; PD-01 allocates no canonical ID.
- Attribute Profiles may scope only to synthetic `FAMILY` or `SERIES` references and define requiredness, visibility, variation, filtering, inquiry, and SEO eligibility.
- Product Value Assignments use one typed value, an Attribute-compatible Unit policy, synthetic provenance, and `CANDIDATE_UNVERIFIED` status.
- Variant Rule Sets list explicit allowed synthetic combinations. Cartesian generation remains forbidden.
- `import_ready`, `runtime_ready`, and `golden_ready` are all constant `false`.
- SKU, slug, availability, pricing, Offer, stock, WordPress/WooCommerce IDs, import, publication, deployment, and production fields are prohibited.

## Synthetic Fixture Boundary

All PD-01 fixtures are test-only, deterministic, visibly synthetic, and carry synthetic provenance. They are not canonical repository rows and cannot be promoted by this Sprint.

The existing canonical Product Attribute registry must remain exactly:

```yaml
attributes: []
```

The fixture IDs, labels, values, Unit references, entity references, and combination references are non-commercial test inputs only. They do not prove a Product, valid commercial combination, availability, attribute vocabulary, or SKU.

## Test Contract

### Positive

- Validate default and explicit local paths.
- Apply the complete Draft 2020-12 schema.
- Validate strict Product Attribute `2.0.0` fixtures.
- Resolve synthetic Product Core, Product Attribute, Unit, Profile, Assignment, and Variant Rule Set references.
- Accept one minimal synthetic Profile, Assignment, and explicit combination.
- Prove import has no output or side effect.
- Prove validation succeeds with network access disabled.
- Prove the canonical Product Attribute registry remains empty.
- Prove deterministic error ordering and the legal lifecycle chain.

### Negative

- Reject missing, unknown, wrongly typed, malformed, duplicate, promoted, out-of-range, excess-precision, incompatible Unit, stale-version, invalid-reference, invalid-requiredness, invalid-axis, and incomplete-combination inputs.
- Reject duplicate YAML and JSON object keys.
- Reject invalid timestamps and non-finite numbers.
- Reject empty required collections and unauthorized readiness flags.
- Reject direct `DRAFT → APPROVED`.

### Adversarial and destructive

- Reject mass assignment and every prohibited Product/runtime/commercial field.
- Reject permissive or non-local-reference schemas.
- Reject path escape and symbolic-link inputs.
- Reject forged classification, evidence, status, and readiness.
- Reject duplicate identities, dependency substitution, unknown references, scope mismatch, Cartesian enablement, and combination gaps.
- Bound input size and execute with no network or side effects.
- Require at least 50 uniquely named negative/adversarial mutation cases.

### Repository acceptance

- Parse every changed YAML and JSON file with strict readers.
- Run targeted PD-01 tests and the unified `make test`/`scripts/test.sh` suite.
- Run `git diff --check`.
- Verify exact changed-path set equality with this 30-path allowlist.
- Scan changed files for secrets, unexpected endpoints, and non-synthetic Product/commercial data.
- Require successful branch CI, no merge conflict, independent `PASS`, and successful post-merge `main` CI.

## Roles and Separation of Duties

| Role | Authority in PD-01 |
| --- | --- |
| Founder | Authorizes exact scope, lifecycle promotion, Git publication, ready-for-review, and conditional Merge Commit |
| Codex Build Engine | Implements and validates only the exact allowlist; cannot independently approve its own work |
| Independent QA reviewer | Read-only review of scope, diff, validation, lifecycle, and prohibitions; returns `PASS` or `REWORK` as `PD01-REVIEW-001` |
| Repository Guardian | Confirms path equality, chronology, governance reconciliation, and rollback traceability; no business-data approval |
| CI service | Repeats deterministic repository validation; passing CI is evidence, not approval |

## Legal Lifecycle

| State | Entry evidence | Exit requirement |
| --- | --- | --- |
| `DRAFT` | Founder execution authorization; exact starting SHA and allowlist; synthetic-only implementation | Local tests pass, Draft PR exists, branch CI passes, and independent review begins |
| `REVIEW` | `DRAFT → REVIEW` recorded with `PD01-REVIEW-001`; no direct promotion | Independent `PASS`, all permitted corrections complete, tests/CI pass, scope and registry boundaries remain intact |
| `APPROVED` | `REVIEW → APPROVED` recorded with `FD-PD01-001` and Founder approval | PR may leave Draft only if all conditional Git gates remain satisfied |

Direct `DRAFT → APPROVED` is invalid and must fail validation.

## Git Controls

- Work occurs only on `codex/pd-01-product-data-contract-enablement`.
- Stage exactly the allowlisted paths; reject any extra path.
- Use normal commits and pushes; no force-push or history rewrite.
- Open the PR as Draft.
- Limited review corrections are allowed only inside the same 30 paths.
- Ready-for-review and merge require successful tests/CI, no conflicts, independent `PASS`, Founder approval, and no scope drift.
- Merge method is Merge Commit only.
- Verify required CI again on `main`.
- Branch deletion is prohibited.

## Stop Conditions

Stop and report `NO-GO` if:

- any changed tracked path falls outside the allowlist;
- the Product Attribute registry is nonempty;
- any real Product, Attribute definition, Pilot, 879-row set, Master Data, Golden data, SKU, slug, availability, commercial fact, price, or stock value appears;
- any WordPress/WooCommerce, import, runtime, deployment, production, external-write, or branch-deletion action is required;
- lifecycle history skips `REVIEW` or lacks its evidence;
- schema/validator/tests/CI fail or validation is nondeterministic/fail-open;
- the independent reviewer returns `REWORK` that cannot be resolved inside scope;
- a secret, credential, private datum, remote schema reference, network dependency, merge conflict, or ambiguous authority is found.

## GO / NO-GO

- **GO in `DRAFT`:** exact-scope repository implementation, synthetic fixtures, local validation, scoped commits/pushes, Draft PR, read-only independent review, and limited in-scope corrections.
- **Conditional later GO:** `DRAFT → REVIEW → APPROVED`, ready-for-review, Merge Commit, and post-merge `main` CI only after every recorded condition passes.
- **NO-GO:** canonical population, real Product data, Registry population, Pilot/879 rows, Master Data/Golden package, SKU/slug/availability, Admin UI, Product/SKU creation, WordPress/WooCommerce, import, runtime, deploy, production, branch deletion, or any work outside the allowlist.

## Change History

| Version | Date | State | Change |
| --- | --- | --- | --- |
| 1.0.0 | 2026-07-28 | `DRAFT` | Created exact PD-01 Scope/Approval Packet, 30-path allowlist, synthetic-only Contract and Test boundaries, roles, Git controls, and stop conditions from the Founder authorization. |
