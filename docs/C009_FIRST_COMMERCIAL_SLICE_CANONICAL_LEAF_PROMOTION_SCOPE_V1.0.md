# C009 — First Commercial Slice Canonical Leaf Promotion Scope v1.0

## Document Control

- **Mission:** `C009 — First Commercial Slice Canonical Leaf Promotion`
- **Status:** Review; effective on `main` only after separately authorized Merge
- **Authority:** Founder / Project Commander
- **Owner:** Founder
- **Executor:** Codex Build Engine
- **Independent reviewer:** Repository Guardian independent from authoring
- **Date:** 2026-08-23
- **Starting main:** `f226381622e94a1d0b2d598f5ed933bde37bd7df`
- **Branch:** `codex/c009-first-commercial-slice-canonical-leaf-promotion`
- **Merge authority:** None
- **Successor authority:** None

## Exact Authority

The controlling Founder authorization is Slack
`C0BNHRRTE9F / 1787440938.184179`, authored by `U0BNFS43TBL` at
`2026-08-23T02:52:18.184179+03:30`. It is both reply 21 of the complete
Founder direction thread `1787398697.475999` and a complete direct thread with
zero replies. The current command SHA-256 is
`0e0a03ae9f445e6d42c6a45284b2869b007fcd709eb1e442ce30bf1cd4205f16`.
The predecessor is C008-FT1, merged at the starting main above with post-merge
CI `32604542391 = PASS`.

This authority permits one bounded combination and one canonical SKU leaf,
the C009 machine package, required governance reconciliation, one commit/push
path and one non-draft PR. It grants no Merge, gate re-evaluation, Runtime,
publication or successor authority.

## Owner Archaeology Result

The repository has no `PRODUCT` entity type. The canonical hierarchy is:

```text
CATALOG → PLATFORM → FAMILY → SERIES → VARIANT_RULE_SET → SKU
```

Product Core owns the structural vocabulary, but its PD-02B base registry is
historically closed at exactly Catalog, Platform and Family. PD-03A establishes
the immutable extension convention and owns the approved Series and Variant
Rule Set. PD-03B owns the exact Pilot evidence but explicitly not Product/SKU
truth. Product Master Data and pilot-combination packages are synthetic-only.

Accordingly, C009 creates a new canonical exact-slice extension and does not
modify any predecessor owner. A distinct `pcomb:` is required because Product
Core SKU records cannot own Material/Grade/Finish/dimensional facts and the
Variant Rule Set requires an explicit evidence-backed combination before the
leaf can exist.

The extension is only the persistence and immutable-binding surface. Product
identity semantics remain owned by Product Core, combination validity remains
owned by the Variant Rule Set, and source Pilot evidence remains owned by
PD-03B. C009 transfers none of those authorities.

## Realized Write Allowlist

Exactly 20 paths are authorized and realized.

### MUST_CREATE — 13

1. `docs/C009_FIRST_COMMERCIAL_SLICE_CANONICAL_LEAF_PROMOTION_SCOPE_V1.0.md`
2. `repository/data/contracts/c009-first-commercial-slice-canonical-leaf-promotion.contract.yaml`
3. `repository/data/schemas/c009-first-commercial-slice-canonical-leaf-promotion.schema.json`
4. `repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml`
5. `repository/data/validation/validate_c009_first_commercial_slice_canonical_leaf_promotion.py`
6. `tests/test_c009_first_commercial_slice_canonical_leaf_promotion.py`
7. `tests/fixtures/c009-first-commercial-slice-canonical-leaf-promotion/README.md`
8. `tests/fixtures/c009-first-commercial-slice-canonical-leaf-promotion/valid-synthetic.yaml`
9. `tests/fixtures/c009-first-commercial-slice-canonical-leaf-promotion/mutation-cases.json`
10. `tests/fixtures/c009-first-commercial-slice-canonical-leaf-promotion/adversarial-duplicate-keys.yaml`
11. `tests/fixtures/c009-first-commercial-slice-canonical-leaf-promotion/adversarial-duplicate-keys.json`
12. `tests/fixtures/c009-first-commercial-slice-canonical-leaf-promotion/adversarial-permissive-schema.json`
13. `tests/fixtures/c009-first-commercial-slice-canonical-leaf-promotion/adversarial-remote-ref-schema.json`

### MUST_CHANGE — 5

14. `docs/CURRENT_PROJECT_STATE.md`
15. `docs/PROJECT_EXECUTION_ROADMAP.md`
16. `docs/TRACEABILITY_MATRIX.md`
17. `docs/08_DOCUMENTATION_INDEX.md`
18. `docs/14_CHANGELOG.md`

### Condition-bound MAY_CHANGE — 2, both triggered

19. `docs/18_OPEN_QUESTIONS.md` — triggered because C009 resolves only the
    exact first-slice combination/leaf identity questions while preserving all
    commercial and launch questions.
20. `scripts/test.sh` — triggered to place C009 validation inside unified tests.

`docs/09_NAVIGATION_MAP.md` is not triggered: Index, Current State and
Traceability already provide the smallest durable route.

## Protected Owners

Product Core, Product Master Data, PD-03A, PD-03B, C003-R3, C002, C006, C008,
C008-R1 and C008-FT1 contracts, schemas, registries, validators, tests and
fixtures are immutable dependencies. Product Attributes, controlled values,
profiles, measurements, units, localized labels, approval evidence and all
Runtime/WordPress/WooCommerce/import/media/public assets are also protected.

## Exact Promotion

| Field | Canonical result |
| --- | --- |
| Source Pilot | `pilot:f5922666261e` |
| Family | `prd:family:a10c6d8ceabc` / `Stainless Steel Pipe` |
| Series | `prd:series:e1657d35ac35` / `لوله استیل دکوراتیو` |
| Variant Rule Set | `prd:variant-rule-set:eb255662accc` |
| Profile | `pprof:4c556c63c1a9` |
| Combination | `pcomb:829e387ccdcb` / `APPROVED` |
| SKU leaf | `prd:sku:66ebd0510693` / `APPROVED` |
| Material | `vterm:5ff9c0ceca39` / Stainless Steel |
| Grade | `vterm:a891bfdfdd6b` / 201 |
| Finish | `vterm:1df9a5493546` / Silver; internal appearance designation only |
| Diameter | `51` / `unit:000000000002` Millimetre |
| Thickness | `0.50` / `unit:000000000002` Millimetre |
| Length | `6` / `unit:000000000001` Metre |
| Availability | `MISSING_DATA_VALUE`; evidence reference only, not a leaf fact |
| Brand / Color / Mass | absent and not promoted |

Both new stable IDs were allocated using CSPRNG 12-hex suffixes and checked
against the governed registry namespace before persistence. `GOLD-PIPE-201-51-050-6M`
and `PIPE-COMB-0023` remain historical references and are not identities.

Exactly one explicit combination and one SKU leaf are created. No other Pilot,
candidate row, size, sibling combination or Cartesian expansion is promoted.
The SKU is an internal canonical hierarchy leaf, not a public commercial SKU
code, stockkeeping claim, WooCommerce variation or commerce activation.

## Preserved State

- C002 remains `6/9 / NOT_READY`; `FOUNDER_SELECTION_READY=FALSE`; candidates `0`.
- Supply and Fulfillment remain `SUBMITTED_REVIEW_INCOMPLETE`; Photo/Content
  remains `MISSING_EVIDENCE`.
- The C008-FT1 owner remains byte-unchanged at `FALSE / 4 of 12`.
- C009 does not re-evaluate or set the C008-FT1
  `CANONICAL_PRODUCT_PROMOTION_COMPLETE` prerequisite.
- Commerce stays `INQUIRY_ONLY`; Availability stays `MISSING_DATA_VALUE`.

## Hard No-Go

No Product Core base rewrite; no extra Product/SKU/combination/value/unit; no
Brand, Color, Mass, Availability, Stock, Price, ETA/SLA or supplier truth; no
Commerce Eligibility activation; no public commercial SKU; no import,
publication, deployment, WordPress, WooCommerce, Runtime, Staging or
Production mutation; no C008-FT1 mutation; no C1-T03 repair; no auto-merge,
Merge, branch deletion, C009 successor, M4 or other Mission.

## Validation and Review Record

- Owner archaeology: `PASS — 0 material findings`
- Exact 20-path allowlist: `PASS`
- Four semantic digests: `PINNED / EXACT`
- Canonical and distinct synthetic strict validators: `PASS`
- Focused tests / mutations: `15/15 PASS; 81/81 dispatched`
- Product Core / Product Master / PD-03A / PD-03B / valid-combination validation: `PASS`
- `make validate` / `make test`: `PASS / PASS`
- Manifest / Atlas / agentic / links: `173/173; 173 rows / 21 domains; 15/15; 5,119`
- Independent pre-pin review: `all findings repaired before pin`
- Independent final pinned-tree review: `PASS — 0 material / 0 non-material findings`
- Exact-head CI: `PENDING`

Passing validation demonstrates technical consistency only. It does not create
Merge, Fast-Track gate re-evaluation, Runtime or successor authority.

## Final Stop

After one bounded non-draft PR, exact-head CI and zero-finding independent
review, stop at `PR_READY / WAIT_FOR_PROJECT_COMMANDER_REVIEW`. Do not merge,
re-evaluate C008-FT1 or start any successor Mission.
