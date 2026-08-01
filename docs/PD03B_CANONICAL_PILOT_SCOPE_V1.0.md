# PD-03B Canonical Pilot Records Scope v1.0

## Control

- **Decision ID:** `FD-PD03B-001`
- **Status:** `APPROVED`
- **Date:** 2026-08-01
- **Starting GitHub main:** `e72c32bdb041448d34c925c969fe01a2156f9e1d`
- **Branch:** `codex/pd-03b-canonical-pilot-records`
- **Authority:** Founder authorization in task `019fa05e-1889-79b3-8e83-9477cd1648c6`
- **Lifecycle:** `DRAFT → REVIEW → APPROVED`; direct promotion is prohibited

`PD03B-TECH-REVIEW-001` passed with zero findings on corrected DRAFT SHA
`41849b30055efd828654995d7a6a13fbedd3bf39`, bound to successful CI run
`30698352338` / job `91364922275`. This permits only `DRAFT → REVIEW`;
Founder lifecycle approval was recorded after successful REVIEW CI
`30698582671` / job `91365511827` at `2026-08-01T11:54:38Z`. The legal
`REVIEW → APPROVED` transition consumed the nonce exactly once.

## Objective

Create exactly three repository-only canonical Pilot records from the settled
`FD-PILOT-001` tuples and the approved PD-03A prerequisite identities. A Pilot
record is not a Product, SKU, Master Data row, Golden package, availability
value, import asset, or runtime object.

## Exact Records

| Stable Pilot ID | Historical references (non-identity) | Exact tuple |
| --- | --- | --- |
| `pilot:b12aa359af76` | `GOLD-PIPE-201-16-035-6M`; `PIPE-COMB-0001` | 201 / Silver / 16 mm / 0.35 mm / 6 m |
| `pilot:8a1546edb732` | `GOLD-PIPE-201-38-050-6M`; `PIPE-COMB-0016` | 201 / Silver / 38 mm / 0.50 mm / 6 m |
| `pilot:f5922666261e` | `GOLD-PIPE-201-51-050-6M`; `PIPE-COMB-0023` | 201 / Silver / 51 mm / 0.50 mm / 6 m |

The set identity is `pilotset:36c1085ffbe9`. All four identities were allocated
with a CSPRNG 12-lowercase-hex suffix and checked for collisions. Labels,
historical references, slugs, WooCommerce IDs, and SKUs cannot become identity.

Each record references the approved Series, Variant Rule Set, INTERNAL Profile,
Material/Grade/Finish terms, Attribute identities, Metre, and Millimetre. The
only record status allowed before final lifecycle approval is
`CANDIDATE_UNVERIFIED`; after approval it is `APPROVED`. Availability remains
`MISSING_DATA_VALUE` at every lifecycle stage. `import_ready`, `runtime_ready`,
and `golden_ready` remain `false`.

## Evidence and Roles

- Business/data basis: `FD-PILOT-001` and `FD-PD03A-001`; no new technical,
  standard, tolerance, quality, application, availability, or commercial claim.
- Decision/final approval: Founder پروژه Damavand Steel.
- Data Steward: `product-data-steward`.
- Executor: `codex-build-engine`.
- Independent technical reviewer: `repository-guardian-independent`.
- QA/Rollback owner: `repository-guardian`.
- AI has no domain or Founder approval authority.

One approval-evidence record must bind the exact dataset hashes, reviewed Git
commit object, starting main SHA, CI run/job, technical verdict artifact, and a
single-use deterministic nonce. Failed or absent review cannot satisfy PASS.

## Test Contract

Positive tests require the exact count, identities, tuple lexemes, cross-file
references, units, precision, lifecycle status, provenance, missing
availability, false readiness, dataset hashes, commit/CI binding, and
anti-replay state.

Negative tests reject missing/extra/duplicate records, changed tuples, 430, PVD,
3m, wrong Unit or precision, historical-reference identity, unknown references,
premature status, actual availability, supply status, SKU/Slug/Product fields,
Master/Golden fields, readiness promotion, Cartesian generation, forged review,
direct lifecycle promotion, replay, and hash substitution.

Adversarial tests reject duplicate YAML/JSON keys, non-finite values, Unicode
confusables, unknown nested fields, remote references, permissive schemas, ID
collisions, and any counted mutation that is not dispatched. Validation is
deterministic, offline, network-free, and side-effect-free.

## Exact 33-Path Allowlist

Only the following paths may change; unused paths need not be created:

1. `repository/data/contracts/pd03b-canonical-pilot.contract.yaml`
2. `repository/data/schemas/pd03b-canonical-pilot.schema.json`
3. `repository/data/registries/extensions/pd03b/canonical-pilots.yaml`
4. `repository/data/validation/validate_pd03b_canonical_pilots.py`
5. `repository/data/contracts/pd03b-approval-evidence.contract.yaml`
6. `repository/data/schemas/pd03b-approval-evidence.schema.json`
7. `repository/data/registries/extensions/pd03b/approval-evidence.yaml`
8. `repository/data/validation/validate_pd03b_approval_evidence.py`
9. `tests/fixtures/pd03b/README.md`
10. `tests/fixtures/pd03b/valid-control.yaml`
11. `tests/fixtures/pd03b/adversarial-duplicate-keys.yaml`
12. `tests/fixtures/pd03b/adversarial-duplicate-keys.json`
13. `tests/fixtures/pd03b/adversarial-permissive-schema.json`
14. `tests/fixtures/pd03b/adversarial-remote-ref-schema.json`
15. `tests/fixtures/pd03b/adversarial-non-finite.json`
16. `tests/fixtures/pd03b/mutation-cases.json`
17. `tests/test_pd03b_canonical_pilots.py`
18. `scripts/test.sh`
19. `docs/PD03B_CANONICAL_PILOT_SCOPE_V1.0.md`
20. `docs/17_FOUNDER_DECISION_LOG.md`
21. `docs/CURRENT_PROJECT_STATE.md`
22. `docs/PROJECT_BASELINE.md`
23. `docs/IMPLEMENTATION_READINESS.md`
24. `docs/PROJECT_EXECUTION_ROADMAP.md`
25. `docs/REPOSITORY_HEALTH.md`
26. `docs/TRACEABILITY_MATRIX.md`
27. `docs/14_CHANGELOG.md`
28. `docs/18_OPEN_QUESTIONS.md`
29. `docs/08_DOCUMENTATION_INDEX.md`
30. `docs/READING_ORDER.md`
31. `docs/19_PRODUCT_DATA_MODEL.md`
32. `docs/11_GLOSSARY.md`
33. `docs/09_NAVIGATION_MAP.md`

## Stop Conditions

Stop without promotion, Ready, or Merge if a changed path is outside the
Allowlist; PD-02B/PD-03A identities or historical hashes change; an extra Pilot
or any of the 879 candidates appears; any test/CI/review fails; a Product, SKU,
Slug, availability value, Master Data, Golden package, WordPress/WooCommerce,
import, runtime, deployment, production, or branch deletion is attempted; or
the reviewed commit, hashes, roles, approval, or anti-replay evidence is
ambiguous.

## Conditional Git Boundary

The approved cycle permits this Branch, scoped DRAFT Commit/Push/Draft PR,
allowlisted corrections, independent technical review, legal lifecycle
promotion, final Founder evidence, and—only after all tests and CI pass with no
conflict or scope drift—Ready for Review and Merge Commit. The Branch must not
be deleted. PD-04 Golden Repository Package requires a separate authorization.
