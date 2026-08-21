# C006 — Product Data Semantic & Product Experience Architecture Reconciliation Scope v1.0

## Document Control

- **Mission:** `C006 — Product Data Semantic & Product Experience Architecture Reconciliation`
- **Status:** Review; effective on `main` only after separately authorized merge
- **Starting live-main anchor:** `ea616b08ef2f4012afd011684dfe4e5c98cd8fcf`
- **Scope:** Product Data semantics, Product Experience projection architecture, closed machine policy, offline validation, tests, and bounded documentation reconciliation
- **Product / Runtime / Production / Merge authority:** None
- **Canonical experience owner:** `repository/enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md`
- **Machine package:** `repository/data/{contracts,schemas,registries,validation}` C006 Product Experience architecture set

## Authority and Source Gate

The live GitHub `main` ref was resolved before mutation. PR #42 was merged as
`ea616b08ef2f4012afd011684dfe4e5c98cd8fcf`, C005 is present on `main`, its
post-merge validation passed, no open PR owned this scope, and the starting tree
was clean.

The complete planning sources were read without remaining pagination:

| Source | Locator | Completeness / role |
| --- | --- | --- |
| C006 Master Orchestration Plan, Parts 1–3 | `C0BNHRRTE9F / 1787086720.993949`, replies `1787086738.441119`, `1787086759.886949` | Parent plus 2 replies; Founder-accepted planning/orchestration direction |
| Pipe Information Model | `C0BNHRRTE9F / 1787084095.125229` | Parent plus 1 reply; Founder-accepted design direction, planning only |
| Product Page Interaction Model — Addendum A | `C0BNHRRTE9F / 1787084980.103649` | Exact reply in the Pipe thread; Founder-accepted design direction, planning only |
| C004 201/51 Competitive Experience Blueprint | `docs/201_51_PILOT_COMPETITIVE_EXPERIENCE_BLUEPRINT_V1.0.md` | Immutable planning input, not Product truth |
| C005 merged state | Live `main` at the starting anchor | Predecessor and regression input |

Repository owners remain authoritative. The Slack sources direct reconciliation;
they do not populate Product truth or override a more specific approved owner.

## Mission Identity Reconciliation

The current Founder amendment assigns `C006` to this semantic/Product Experience
Mission. It supersedes only the never-started, deferred roadmap pointer
`C006 — Pilot Certification / Production Decision`. That old pointer receives no
replacement ID and no Certification, Runtime, Production, or merge authority.
The dated C000 decision package remains unchanged as historical context.

## Ownership Gate

C006 creates one composition/interface architecture; it does not become a
parallel Product, Availability, Pricing, Media, Knowledge, Inquiry, or Commerce
truth owner.

| Concern | Reused canonical or future-gated owner | C006 effect |
| --- | --- | --- |
| Product hierarchy and identity | Product Core; `Catalog → Platform → Family → Series → Variant Rules → SKU` | Reference only; no Product or SKU record |
| Attributes, values, profiles | Product Attribute/Value/Profile contracts and approved PD-02B/PD-03A extensions | Semantic reconciliation only; no value or lifecycle promotion |
| Axes, allowed values, valid combinations | `VARIANT_RULE_SET` | Architecture contract only; canonical instances remain empty |
| Brand identity | Future governed Brand identity owner | Boundary only; no Brand value or identity record |
| Brand provenance and relationships | C002 Brand Provenance | Reference and gate only; never substitutes for Brand identity |
| Measurements and derivations | Measurement foundation plus Product Attribute owner | Separates nominal, observed, and calculated facts |
| Mass provenance and lifecycle | C002 Mass Provenance | Compatible policy extension only; numeric observations remain zero |
| Availability | Founder-confirmed business intent plus a future governed Availability evidence owner | Projection prerequisites only; no Availability or stock fact |
| Price authority | Future separately governed Pricing authority | Boundary only; no price/value/formula |
| Customer order unit | Future separately governed Order Unit policy | Boundary only; no order or pricing fact |
| Pricing basis | Future separately governed Pricing Basis policy | Boundary only; never collapsed into Order Unit |
| Service/fulfillment choices | Future separately governed Service policy | Boundary only; Inquiry may carry selected context but does not own the service |
| Media | Media Strategy/Product Media Set | Read-only applicability resolver; no asset or rights claim |
| Knowledge/application | Content/Knowledge owners | Read-only reference; canonical Knowledge instances remain absent |
| Product Experience | Reserved Product Experience Engine owner | Architecture-only interaction/composition contract |
| Search and SEO | Search/Discovery and SEO Entity owners | Non-indexing/intent gates only; no page or URL |
| Inquiry/operator handoff | Inquiry Data Model and Inquiry Workflow | Selected-context interface only; no Inquiry/CRM/Order object |
| Commerce Eligibility | C002 per-SKU Commerce Eligibility | Future read-only input; current CTA remains Inquiry |
| WooCommerce | Downstream adapter/projection owners | No canonical Product or Commerce authority |

### Path Classification

The bounded patch map is exact. `MUST_CHANGE=25`, `MAY_CHANGE=14`, for an exact
candidate patch of `39` files. A file not named below is not authorized merely
because it is adjacent or linked.

#### MUST_CHANGE — 25 exact files

```text
docs/08_DOCUMENTATION_INDEX.md
docs/14_CHANGELOG.md
docs/19_PRODUCT_DATA_MODEL.md
docs/20_WOOCOMMERCE_PRODUCT_MODEL.md
docs/22_PRODUCT_ATTRIBUTE_MODEL.md
docs/35_WORDPRESS_BLUEPRINT.md
docs/C006_PRODUCT_DATA_SEMANTIC_PRODUCT_EXPERIENCE_ARCHITECTURE_SCOPE_V1.0.md
docs/CONTEXT_ROUTER.md
docs/CURRENT_PROJECT_STATE.md
docs/PROJECT_EXECUTION_ROADMAP.md
docs/READING_ORDER.md
docs/REPOSITORY_RELATIONSHIP_MAP.md
docs/TRACEABILITY_MATRIX.md
repository/data/attributes/ATTRIBUTE_DICTIONARY.md
repository/data/attributes/PIPE_ATTRIBUTE_MODEL.md
repository/data/contracts/pipe-product-experience-architecture.contract.yaml
repository/data/products/pipes/PIPE_VARIATION_MATRIX.md
repository/data/products/pipes/PIPE_WOOCOMMERCE_MAPPING.md
repository/data/registries/extensions/c006/pipe-product-experience-architecture.yaml
repository/data/schemas/pipe-product-experience-architecture.schema.json
repository/data/validation/validate_pipe_product_experience_architecture.py
repository/enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md
scripts/test.sh
tests/fixtures/c006-product-experience-architecture/mutation-cases.json
tests/test_pipe_product_experience_architecture.py
```

#### MAY_CHANGE — 14 exact files

Each optional file below is included only because the final patch resolves a
direct C006 contradiction or supplies an adversarial test fixture.

```text
docs/33_MEDIA_STRATEGY.md
repository/data/imports/woocommerce/PIPE_IMPORT_MAPPING.md
repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md
repository/data/seo/PIPE_SEO_ENTITY_MODEL.md
repository/data/taxonomies/PIPE_CATEGORY_MODEL.md
repository/data/taxonomies/PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md
repository/data/validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md
repository/data/validation/PRODUCT_DATA_VALIDATION_RULES.md
repository/design/COMPONENT_PATTERN_LIBRARY.md
tests/fixtures/c006-product-experience-architecture/README.md
tests/fixtures/c006-product-experience-architecture/adversarial-duplicate-keys.json
tests/fixtures/c006-product-experience-architecture/adversarial-duplicate-keys.yaml
tests/fixtures/c006-product-experience-architecture/adversarial-permissive-schema.json
tests/fixtures/c006-product-experience-architecture/adversarial-remote-ref-schema.json
```

`PIPE_IMPORT_MAPPING.md` is a documentation-only downstream mapping contract,
not an executable import payload. C006 may reconcile that exact file but may not
create or change CSV data, import input, command, job, runtime configuration, or
publication artifact.

#### MUST_NOT_CHANGE — 13 protected path groups

```text
AGENTS.md
docs/C000_OS2_STRATEGIC_RECONCILIATION_DECISION_PACKAGE.md
repository/data/registries/product-*.yaml
repository/data/registries/measurement-dimensions.yaml
repository/data/registries/attribute-*.yaml
repository/data/registries/extensions/pd03a/**
repository/data/registries/extensions/pd03b/**
repository/data/registries/extensions/c002/**
repository/data/registries/extensions/c003/**
repository/data/registries/extensions/c003r1/**
repository/data/registries/extensions/c003r2/**
repository/data/registries/extensions/c004/**
repository/data/registries/extensions/c005/**
```

The protected groups include all approved populated Product/Attribute/Value/
Profile and prior-Mission registries. C006 also prohibits any unlisted
WordPress/runtime/import payload, C1-T03 evidence, GitHub setting or Production
path even where it is outside the listed groups.

## Epic 1 — Semantic Foundation

Every projected field has exactly one truth class:

- `CANONICAL_SELECTION`: governed stable Product/attribute references only;
- `DERIVED_TECHNICAL`: formula, inputs, units, precision, rounding, source and
  approximation explicitly declared;
- `DYNAMIC_COMMERCIAL`: time-sensitive Mass, Availability, Price or supply
  context, each from its own owner;
- `KNOWLEDGE_CONTENT`: application, guidance, limitations and education;
- `SERVICE_FULFILLMENT`: cutting, packaging, shipping and related services;
- `OPERATOR_INTERNAL`: protected provenance, batch/load and audit context.

The following boundaries are mandatory:

1. `Finish`, `Color`, `Appearance`, and `Coating Method` remain distinct. The
   immutable PD-03A `finish=Silver` record is preserved as a bounded legacy
   internal appearance designation, not generalized into a new value taxonomy.
2. Market/nominal Diameter is not physical OD. Calculated ID uses the exact
   declared formula `ID = OD − 2 × Thickness`, is labeled
   `CALCULATED_NOMINAL`, and never becomes measured evidence.
3. Variant Rules alone owns axes, allowed values, constraints, and valid
   combinations. Profile flags and UI order are projections only. No Cartesian
   possibility becomes validity.
4. Brand may participate in selection only after governed identity, provenance,
   and Variant Rules evidence exist; Brand, manufacturer, supplier, and origin
   are never inferred from one another.
5. Mass lifecycle stays `NEXT_PENDING → CURRENT → HISTORICAL` under explicit
   operator promotion. Only governed CURRENT evidence may project; numeric Mass
   remains unpopulated and never enters Product identity.
6. Product identity, Mass, Availability, Price, customer order unit, pricing
   basis, Knowledge, Media, Inquiry, and Service remain separate owners.
7. Missing, unknown, expired, or conflicted evidence never becomes out-of-stock,
   Price, Product truth, or a supply promise.

## Epic 2 — Product Experience and Projection

The architecture composes:

```text
Canonical Family
→ Family-configurable dependent selector
→ Variant Rules resolution
→ selected-context summary
→ derived technical panel
→ dynamic commercial projection
→ Media/Knowledge resolver
→ Inquiry-first CTA
```

- Selector order is per Family, references governed axes, and cannot add axes,
  values, or tuples.
- Selection remains visible, reversible, resettable, keyboard-operable, touch
  safe, screen-reader announced, Persian RTL and BiDi safe.
- Combination resolution is separate from Availability projection. Unknown,
  incompatible, and needs-verification states remain distinct.
- Media resolution is exact variant override, then applicable appearance/finish
  override, then Family media only when explicitly truthful; otherwise it fails
  closed to no eligible media/placeholder.
- Knowledge references require a governed public ID, applicability and lifecycle;
  current bindings remain empty.
- Selector/query states are non-indexable. Pages, URLs, canonicals and sitemap
  entries require a separate approved intent owner and are never generated per
  tuple or facet.
- Current CTA is contextual Inquiry/operator verification. Purchase CTA requires
  a future exact SKU with an active evidence-complete C002 eligibility instance;
  no Family/Series/Product/Parent/Variation/Pilot inheritance is allowed.
- WooCommerce remains a read-only downstream projection of governed sources.

## Epic 3 — Cross-System Hardening

The C006 machine package is closed Draft 2020-12 and validated offline. It
requires strict duplicate-key JSON/YAML parsing, local references only,
repository-contained regular paths, symlink/path/byte/depth/node/non-finite
guards, deterministic sorted findings, exact source/order/count/owner/authority
invariants, semantic dependency pins, zero network, and zero side effects.

Mandatory adversarial coverage rejects at least:

- Finish/Color collapse and duplicate Brand ownership;
- derived ID as measured truth;
- unauthorized Mass promotion or Mass in Product identity;
- Availability inferred from supplier habit and Price in Product truth;
- Cartesian generation and unsupported selector options;
- false media inheritance;
- page-per-tuple or selector-state indexing;
- WooCommerce as canonical owner or premature purchase CTA;
- Service as Product attribute;
- Unknown as out-of-stock;
- order unit/pricing-basis collapse.

Regression anchors preserve C002 `0 candidates / 8 policies / 0 instances`,
C003-R3 216 evidence positions without persisted Cartesian rows, C004
`13 competitors / 364 scores / 10 advantages`, C005
`8 SUBMITTED / 1 MISSING / 6 REVIEWABLE / 9 OPEN_BLOCKING / 0 VERIFIED`,
three canonical Product entities, zero canonical SKU, six approved bounded
Attributes, zero current Mass/Supply/Price/Customer/Order/VIP/Loyalty objects,
`INQUIRY_ONLY`, Runtime/Production `NONE`, and frozen C1-T03.

## Hard No-Go

C006 creates no Product, Product value, Variant Rule instance, persisted tuple,
SKU, current Mass observation, Availability, stock, supplier fact, Price,
pricing formula, Media asset, Knowledge content, SEO page, Customer, CRM, Inquiry,
Quote, Reservation, Order, Cart, Checkout, Payment, public pricing, WordPress or
WooCommerce configuration, import, publication, hosting mutation, Runtime,
Staging, deployment, Production, C1-T03 repair, branch deletion, merge, or
successor Mission. It copies no competitor content or asset.

## Completion Gate

Success requires focused validator/tests, all counted mutation/adversarial cases,
full `make test`, repository/link/manifest/security validation,
`git diff --check`, clean branch, an independent review with zero unresolved
material findings, one non-draft PR, required CI PASS and mergeability. C006 then
stops for Founder/Project Commander review without merge or successor work.
