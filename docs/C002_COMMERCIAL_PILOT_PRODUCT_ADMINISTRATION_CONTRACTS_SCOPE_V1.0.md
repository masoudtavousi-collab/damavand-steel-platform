# C002 Commercial Pilot Truth and Product Administration Contracts v1.0

## Control

- **Mission:** `C002 — COMMERCIAL PILOT TRUTH & PRODUCT ADMINISTRATION CONTRACTS`
- **Authority:** Founder + Project Commander Slack Mission Packet (parent plus four replies)
- **Starting GitHub main:** `d603322e238d4cf06070da8fb8096cf7050527c2`
- **Branch:** `codex/c002-commercial-pilot-product-admin-contracts`
- **Document lifecycle:** Review; effective on `main` only after separately authorized merge
- **Runtime authority:** None
- **Population authority:** None

## Objective

Define the smallest deterministic repository contracts needed to receive and
assess evidence-backed Commercial Pilot candidates and to govern future Product
administration. C002 creates contract infrastructure only. It does not select a
Pilot slice, create a Product or SKU, assert Availability, invent commercial
facts, or activate a runtime or purchase path.

## Canonical Ownership

C002 extends, and does not replace, the existing owners:

```text
Product Core / PD-03 extensions
  -> Product Attributes and Controlled Value Registries
  -> Measurements
  -> Product Master Data contract boundary
  -> C002 candidate-intake and administration-policy extensions
```

The Product hierarchy remains:

```text
Catalog -> Platform -> Family -> Series -> Variant Rules -> SKU
```

Candidate intake, readiness, proposals, Pilot references, WordPress/WooCommerce
objects, and UI labels never become canonical Product identity.

## Package 1 — Commercial Pilot Candidate

The package defines an empty canonical intake registry plus a closed schema,
offline validator, and synthetic tests. A candidate separates:

- seed/reference evidence from candidate identity;
- Product truth from candidate and selection state;
- SKU readiness, Availability evidence, projection readiness, and Commerce
  Eligibility from one another;
- evidence coverage from Founder selection.

The three approved PD-03B Pilot records may be cited only as non-identifying
seed/reference evidence. They are neither Product/SKU/Availability nor a ceiling
on future bounded Fast-Track intake.

### Deterministic readiness

Every intake assesses exactly these nine evidence criteria:

1. `DEMAND_SIGNAL`
2. `SUPPLY_EVIDENCE`
3. `GROSS_PROFIT_POTENTIAL`
4. `REPEATABILITY`
5. `PRODUCT_DATA_COMPLETENESS`
6. `PHOTO_CONTENT_READINESS`
7. `SEO_BUYER_INTENT`
8. `OPERATIONAL_COMPLEXITY`
9. `FULFILLMENT_RISK`

Each criterion records evidence state, assessment, evidence references, owner,
reviewer, capture/review time, and validity. `VERIFIED` and an explicitly
approved `NOT_APPLICABLE_APPROVED` are resolved. Coverage is only
`resolved_count / 9`; it is not a weighted commercial score. Founder-supplied
gross-profit evidence may be referenced or protected by locator, but C002 never
calculates or invents price, cost, margin, or revenue.

`FOUNDER_SELECTION_READY` requires 9/9 resolved evidence, valid provenance, and
no blocker. It does not select the candidate or create Product, SKU,
Availability, projection, import, runtime, or commerce authority.

## Minimum Founder Evidence/Data Packet

For each future candidate the packet must provide or explicitly mark unresolved:

- bounded business objective, customer/use case, channel, Family/Series and
  proposed configurations;
- canonical references where they exist and clearly labeled proposals where
  they do not;
- dated demand, supply, repeatability, operations, and fulfillment evidence;
- protected Founder-supplied gross-profit-potential evidence when provided;
- manufacturer catalog/specification, invoice, store record, approved manual
  observation, or other authorized evidence locators;
- brand, manufacturer, and supplier roles with separate provenance;
- mass evidence method and unit basis;
- electrostatic/coating and appearance semantics where applicable;
- Product-data, photo, content, rights, SEO, and buyer-intent readiness;
- Inventory Harmony need/evidence and Commerce intent;
- Damavand component versus Central future-solution boundary;
- owner/reviewer separation, confidentiality, conflicts, exclusions, blockers,
  and the explicit Founder selection decision.

An unsupported assertion is not evidence. Redacted evidence locators are valid
when protected commercial facts must not be copied into the repository.

## Package 2 — Product Administration Policy

The package defines policy records and an empty instance registry for:

- `PRODUCT_BUILDER`
- `CONTROLLED_VALUE_PROPOSAL`
- `BRAND_PROVENANCE`
- `MASS_PROVENANCE`
- `ELECTROSTATIC_APPEARANCE`
- `COMMERCE_ELIGIBILITY`
- `INVENTORY_HARMONY`
- `DAMAVAND_CENTRAL_BOM_INTERFACE`

### Product Builder and Add Value

Product Builder may form only a draft candidate bundle from approved
Family/Series/Profile/Variant Rules and explicitly approved controlled values.
It cannot generate a Cartesian product, derive a final SKU, assert Availability,
or write to a runtime adapter.

`+ Add Value` is a proposal queue with the exact lifecycle:

```text
DRAFT -> VALIDATE -> REVIEW -> APPROVED | REJECTED
```

Pending proposals are excluded from canonical selectors. Even an approved
proposal has no automatic registry effect; promotion into the canonical owner
requires separate authorization, duplicate/confusable checks, domain evidence,
and impact review.

### Brand and Mass provenance

Brand, manufacturer, and supplier are separate roles. One never proves another.
Every assertion requires scope, evidence, applicability, effective period,
owner, and reviewer.

Mass provenance methods are exactly:

- `MANUFACTURER_STATED`
- `MEASURED`
- `CALCULATED`

Every record carries value as an exact decimal lexeme, Unit reference, basis,
precision, evidence, and review. Measured records require method, instrument,
calibration, sample, and time evidence. Calculated records require a versioned
formula, every input and source, rounding, and `approximate=true`. Conflicting
evidence remains separate and cannot be overwritten. Existing Mass, Kilogram,
and Gram records remain `CANDIDATE_UNVERIFIED`; C002 promotes none.

### Electrostatic Appearance

Electrostatic appearance keeps substrate/material, coating method, color,
texture, and sheen as separate governed concepts. It is not the stainless
surface-finish namespace and is not PVD. Examples are proposal targets only;
C002 creates no appearance value.

### Commerce Eligibility

The target state vocabulary is:

```text
INQUIRY_ONLY
  -> PURCHASE_CANDIDATE
  -> PURCHASE_ELIGIBLE_INACTIVE
  -> PURCHASE_ENABLED
  -> SUSPENDED | REVOKED
```

`INQUIRY_ONLY` is the current and fail-closed default. Eligibility is versioned
per approved canonical SKU and never inherited from Catalog, Family, Series,
Product, Variable Parent, Variation, Pilot, or assortment. C002 has no Product,
SKU, commercial, Runtime, Production, or Founder activation authority, so its
canonical eligibility instance set remains empty and no effective purchase
capability exists.

### Inventory Harmony

Inventory Harmony is a versioned, evidence-backed compatibility or assortment
rule between exact component references. It records positive ratios, dimension
predicates, provenance, effective period, owner/reviewer, conflicts, and one
result: `ELIGIBLE`, `INELIGIBLE`, or `UNDETERMINED`.

It cannot prove stock or Availability, enable Commerce Eligibility, add to cart,
substitute automatically, or encode price, cost, margin, discount, coupon, or a
pricing formula. The historical `1 x 51 + 1 x 38 + 3 x 16` example remains
unverified and is not populated by C002.

### Damavand / Central boundary

```text
Damavand approved component Product/SKU/BOM snapshot
  -> versioned read-only interface
  -> future Central Solution BOM
  -> future calculator / project / quote
```

Damavand owns component truth. Central may later consume versioned identities
but cannot mutate them; its solution composition and quote context remain a
separate future owner. C002 creates no Central record, calculator, service, or
implementation.

## Validation Contract

- Draft 2020-12 schemas are closed at every object boundary and use local
  references only.
- YAML/JSON duplicate keys, non-finite values, unsafe paths, remote references,
  permissive schemas, unresolved references, forbidden state inheritance, and
  implicit promotion fail closed.
- Canonical C002 instance registries remain empty; positive records exist only
  in unmistakable `SYNTHETIC_FIXTURE` files.
- Errors are deterministic and sorted; validation is offline, network-free, and
  side-effect-free.
- Positive, negative, mutation, and adversarial tests run through `make test`.

## Explicit No-Go

No final Pilot selection, Product/SKU/Availability/stock claim, price/cost/
margin/discount invention, 879-row population, WordPress/WooCommerce, import,
publication, Runtime, Staging, Production, Central implementation, Asan access,
n8n/OpenAI integration, C1-T03 repair, merge, or successor Mission is authorized.

## Completion Boundary

C002 is complete only when its bounded artifacts pass local validation,
independent review returns zero findings, CI passes on exactly one PR, and the
PR is ready for Project Commander review. Merge and every successor remain
separately authorized.
