# PD-03A Pilot Prerequisite Foundation Scope v1.0

**Decision ID:** `FD-PD03A-001`

**Lifecycle:** `REVIEW`

**Baseline:** `main@dd4d4e9dde59ce652edb5b99d2df3e84b56b8031`

**Authority:** Founder-approved repository-only Product Data prerequisite

**Runtime authority:** None

## Objective

Create the smallest successor-safe prerequisite for a later PD-03B cycle without
changing the immutable PD-02B aggregate registries or their historical hashes.
PD-03A defines the Series, internal Variant Rule Set identity, four Attributes,
one appearance-only Silver term, one Series Profile, approved Length/Metre/
Millimetre references, and a synthetic-only pilot-combination test contract.

PD-03A creates no canonical Pilot combination, Product, SKU, Slug, availability,
Master Data, Golden package, import asset, runtime mapping, or publication.

## Immutable Extension Architecture

The approved PD-02B aggregate registries and their evidence remain unchanged.
PD-03A is a separately governed extension under
`repository/data/registries/extensions/pd03a/`. Its validator composes the base
and extension views for collision, dependency, hierarchy, Unit, label, and
policy checks while preserving the exact PD-02B regression validator.

This avoids rewriting historical approval hashes when a later decision adds
records. The extension cannot shadow, replace, or mutate any PD-02B stable ID.

## Exact Foundation Slice

- 2 Product Entity records:
  - Series `لوله استیل دکوراتیو` under the approved Pipe Family.
  - one internal Variant Rule Set entity under the Series.
- 4 Attributes: `finish`, `diameter`, `thickness`, and `length`.
- 1 controlled Value Registry and 1 term: `silver`.
- 1 Series-scoped Profile with exactly 6 rules.
- 11 localized labels: Persian-only for the Series; Persian and English for
  the four Attributes and Silver term.
- 1 Approval Evidence record.
- 21 new stable IDs allocated as 12 lowercase hexadecimal values with a
  collision check across the immutable base and extension.
- Existing `length`, `metre`, and `millimetre` definitions are promoted only
  when this lifecycle reaches `APPROVED`; Mass/Kilogram/Gram remain unchanged.

## Names and Claim Boundary

| Subject | Canonical/internal | Persian label | Meaning |
| --- | --- | --- | --- |
| Series | `لوله استیل دکوراتیو` | `لوله استیل دکوراتیو` | Persian official label only in this scope |
| Finish Attribute | `finish` / `Finish` | `رنگ و پوشش` | Internal pilot appearance designation |
| Silver Term | `silver` / `Silver` | `نقره‌ای` | Appearance designation only |
| Diameter | `diameter` / `Diameter` | `قطر` | Decimal value in millimetres |
| Thickness | `thickness` / `Thickness` | `ضخامت` | Decimal value in millimetres |
| Length | `length` / `Length` | `طول` | Decimal value in metres |

`finish=Silver` does not assert PVD, coating type, material, quality, standard,
tolerance, application, suitability, availability, stock, or supply. The label
does not establish a general global Finish/Color/Surface taxonomy beyond this
bounded internal prerequisite.

## Unit and Precision Policy

| Attribute | Unit | Maximum decimal places |
| --- | --- | ---: |
| Diameter | `unit:000000000002` (`mm`) | 0 |
| Thickness | `unit:000000000002` (`mm`) | 2 |
| Length | `unit:000000000001` (`m`) | 0 |

Values are represented as deterministic decimal lexemes in the synthetic test
contract. Non-finite numbers and implicit Unit conversion are prohibited.

## Series Profile

All six rules are `REQUIRED`, `INTERNAL`, non-filtering, `NOT_USED` for inquiry,
and `PROHIBITED` for SEO.

- Variation axes: Grade, Finish, Diameter, Thickness, and Length.
- Fixed non-axis: Material.
- Cartesian generation is forbidden.
- The Profile creates no public presentation, filter, Variation, commerce, or
  runtime authority.

## Synthetic Pilot Test Contract

The Product Pilot Combination contract has
`canonical_population_authority=false`. Its fixtures exercise only these three
bounded tuples with synthetic `pcomb:` identities:

1. `201 / Silver / 16 mm / 0.35 mm / 6 m`
2. `201 / Silver / 38 mm / 0.50 mm / 6 m`
3. `201 / Silver / 51 mm / 0.50 mm / 6 m`

`PIPE-COMB-*` values are historical references with
`historical_reference_is_identity=false`. They are not Product IDs, SKUs, or
Slugs. Every fixture is `CANDIDATE_UNVERIFIED`; availability uses only the
controlled missingness status `MISSING_DATA_VALUE`; all readiness flags are
false. Fixtures must never be promoted or copied into a canonical registry.

## Review and Evidence Model

- Decision authority: `Founder پروژه Damavand Steel`.
- Product Data Steward: `product-data-steward`.
- Executor: `codex-build-engine`.
- Independent technical reviewer: `repository-guardian-independent`.
- AI/Codex assists and executes but is not a human domain reviewer or Founder.
- Two failed human-review attempts are preserved as Blocked history and never
  satisfy PASS.
- No human PASS is claimed. This exact scope relies on previously approved
  Founder pilot references and explicitly prohibits technical and commercial
  claims. Independent technical PASS remains mandatory before REVIEW.
- Approval Evidence binds the extension and three measurement assets by
  SHA-256 and rejects forged review, premature approval, hash tampering, and
  approval replay.

## Lifecycle

1. `DRAFT`: all extension records remain `CANDIDATE_UNVERIFIED`; measurement
   entries remain Candidate; technical review is `PENDING`; final approval is
   null; the anti-replay nonce is unconsumed.
2. `REVIEW`: allowed only after `PD03A-TECH-REVIEW-001` returns PASS. Records
   and measurements remain Candidate; Founder approval remains absent.
3. `APPROVED`: allowed only under the explicit Founder authorization recorded
   by `FD-PD03A-001`; extension records plus Length/Metre/Millimetre become
   `APPROVED`; the nonce is consumed exactly once.

Direct `DRAFT → APPROVED` is prohibited. Tests, CI, a Commit, or a PR never
substitute for the independent technical review or Founder approval.

## Technical Review History

- Attempt 1 reviewed DRAFT SHA
  `26e67af184a02f5ade0263f163c5c01a40d5aeef` against baseline
  `dd4d4e9dde59ce652edb5b99d2df3e84b56b8031` with CI run
  `30694859806` successful. Verdict: `PD03A-TECH-REVIEW-001: REWORK`
  (`Critical 0 / High 2 / Medium 3 / Low 0`). Required corrections bind the
  technical review artifact, nonce, exact semantics, Approval ID collisions,
  cross-file references, nested Schema boundaries, Contracts, and adversarial
  tests. No lifecycle promotion occurred from this attempt.
- Attempt 2 reviewed corrected DRAFT SHA
  `43d6dc0ce98af1a390d73bf3c5a43c91cdb37da8` with CI run
  `30695723727` successful. Verdict: `PD03A-TECH-REVIEW-001: REWORK`
  (`Critical 0 / High 1 / Medium 1 / Low 0`). It confirmed four prior finding
  groups closed and required proof that the reviewed SHA resolves to a real
  Git commit plus rejection of implicit-true Schema equivalents. No lifecycle
  promotion occurred from this attempt.
- Attempt 3 reviewed corrected DRAFT SHA
  `cb6c817116d0e97e2d217fe2402d85ff4b96f53a`; CI run `30696083295`
  and job `91359111107` succeeded. Verdict:
  `PD03A-TECH-REVIEW-001: PASS` with zero findings at every severity. The
  reviewed Commit object SHA-256 is
  `b1bff46dab757efbdf6e107654a1d5df379cc1e220bf9d6b33abf8c3e1fdd4e1`
  and the bound verdict-artifact digest is
  `f843938deb49189f04f16add10c24b4ab32633bce7beb9a12d1f6e9eb8b0ee01`.
  This evidence authorizes only the legal `DRAFT → REVIEW` transition; final
  Founder approval remains a separate lifecycle step.

## Test Contract

Positive coverage requires:

- exact counts, identities, hierarchy, labels, claim boundaries, Profile rules,
  Units, precision, status, provenance, and cross-base collision checks;
- PD-02B historical validator and hashes remain valid;
- exactly three synthetic tuples, historical non-identity references,
  `MISSING_DATA_VALUE`, and readiness false;
- deterministic offline execution without network or side effects.

Negative coverage rejects:

- direct lifecycle promotion, extra entities/combinations, Grade 430, PVD, 3m,
  out-of-scope values, wrong Unit/precision, Cartesian generation, actual
  availability, supply status, SKU, Slug, and readiness promotion;
- forged technical PASS, premature Founder approval, approval replay, failed
  review presented as PASS, or dataset hash tampering.

Adversarial coverage rejects:

- duplicate YAML/JSON keys, permissive or remote-reference schemas, unknown
  fields, Unicode confusables, non-finite numbers, ID collisions, and malformed
  nested structures.

The mutation manifest contains 50 dispatched cases, including exact review-SHA
and artifact-digest binding, deterministic nonce binding and consumption
history, global ID collision, cross-file resolution, exact role/relationship/
alias semantics, Contract tampering, duplicate JSON, non-finite JSON, and
nested implicit-true Schema branches. A counted but undispatched
case fails the test suite.

## Exact Allowlist

Only these 49 paths may change:

1. `repository/data/contracts/pd03a-pilot-prerequisite.contract.yaml`
2. `repository/data/schemas/pd03a-pilot-prerequisite.schema.json`
3. `repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml`
4. `repository/data/validation/validate_pd03a_pilot_prerequisite.py`
5. `repository/data/contracts/pd03a-approval-evidence.contract.yaml`
6. `repository/data/schemas/pd03a-approval-evidence.schema.json`
7. `repository/data/registries/extensions/pd03a/approval-evidence.yaml`
8. `repository/data/validation/validate_pd03a_approval_evidence.py`
9. `repository/data/contracts/product-pilot-combination.contract.yaml`
10. `repository/data/schemas/product-pilot-combination.schema.json`
11. `repository/data/validation/validate_product_pilot_combinations.py`
12. `repository/data/contracts/measurement.contract.yaml`
13. `repository/data/registries/measurement-dimensions.yaml`
14. `repository/data/registries/attribute-units.yaml`
15. `repository/data/validation/validate_measurements.py`
16. `tests/fixtures/pd03a/README.md`
17. `tests/fixtures/pd03a/valid-synthetic-foundation.yaml`
18. `tests/fixtures/pd03a/valid-synthetic-pilot-combinations.yaml`
19. `tests/fixtures/pd03a/invalid-extra-combination.yaml`
20. `tests/fixtures/pd03a/invalid-out-of-scope-value.yaml`
21. `tests/fixtures/pd03a/invalid-wrong-unit-precision.yaml`
22. `tests/fixtures/pd03a/invalid-cartesian-generation.yaml`
23. `tests/fixtures/pd03a/invalid-availability-supply-status.yaml`
24. `tests/fixtures/pd03a/invalid-sku-slug-runtime.yaml`
25. `tests/fixtures/pd03a/adversarial-duplicate-keys.yaml`
26. `tests/fixtures/pd03a/adversarial-permissive-schema.json`
27. `tests/fixtures/pd03a/adversarial-remote-ref-schema.json`
28. `tests/fixtures/pd03a/mutation-cases.json`
29. `tests/test_pd03a_foundation.py`
30. `scripts/test.sh`
31. `docs/PD03A_PILOT_PREREQUISITE_FOUNDATION_SCOPE_V1.0.md`
32. `docs/17_FOUNDER_DECISION_LOG.md`
33. `docs/CURRENT_PROJECT_STATE.md`
34. `docs/PROJECT_BASELINE.md`
35. `docs/IMPLEMENTATION_READINESS.md`
36. `docs/PROJECT_EXECUTION_ROADMAP.md`
37. `docs/REPOSITORY_HEALTH.md`
38. `docs/TRACEABILITY_MATRIX.md`
39. `docs/14_CHANGELOG.md`
40. `docs/18_OPEN_QUESTIONS.md`
41. `docs/08_DOCUMENTATION_INDEX.md`
42. `docs/READING_ORDER.md`
43. `docs/19_PRODUCT_DATA_MODEL.md`
44. `docs/22_PRODUCT_ATTRIBUTE_MODEL.md`
45. `docs/11_GLOSSARY.md`
46. `repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md`
47. `repository/data/attributes/ATTRIBUTE_DICTIONARY.md`
48. `repository/data/attributes/PIPE_ATTRIBUTE_MODEL.md`
49. `repository/data/validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md`

Allowlist means a maximum boundary; unused paths need not be touched. Any
changed path outside the set is a Stop Condition.

## Stop Conditions

Stop without promotion, push, Ready, or Merge if:

- any changed path is outside the Allowlist;
- PD-02B files, hashes, stable identities, or approval history change;
- a test or required CI check fails;
- independent technical review is not PASS;
- lifecycle, hash, anti-replay, Unit, precision, reference, or collision checks
  fail;
- scope attempts to create a canonical Pilot/Product/SKU/Slug/availability,
  879 rows, Master/Golden, WordPress/WooCommerce, import, runtime, deployment,
  production, technical/commercial claim, or branch deletion.

## Git Boundary

The authorized cycle permits a dedicated Branch, scoped DRAFT Commit and Push,
Draft PR, allowlisted review corrections, independent technical review, legal
`DRAFT → REVIEW → APPROVED`, final Founder evidence, and—only after all tests
and CI pass with no conflict or scope drift—Ready for Review and Merge Commit.
The remote Branch must not be deleted.
