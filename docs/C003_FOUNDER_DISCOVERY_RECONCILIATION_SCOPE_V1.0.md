# C003 Founder Discovery Reconciliation and Repository Intake v1.0

## Control

- **Mission:** `C003 — FOUNDER DISCOVERY RECONCILIATION & REPOSITORY INTAKE`
- **Decision:** `FD-C003-DISCOVERY-001`
- **Authority:** Founder + Project Commander Slack Mission Packet, parent plus two replies
- **Starting GitHub main:** `b45e1b592213f8d3d98805cef2681be781d8cff8`
- **Branch:** `codex/c003-founder-discovery-reconciliation`
- **Document lifecycle:** Review; effective on `main` only after separately authorized merge
- **Product / SKU / Availability population authority:** None
- **Runtime / WordPress / WooCommerce / Production authority:** None
- **Merge authority:** None

## Objective

Convert the complete Founder Product & Commerce Discovery Session 01 into
durable, governed Repository evidence, owner mappings, inactive backlog, and
deterministically validated machine-readable records. C003 preserves the
Founder evidence without promoting it into canonical Product, controlled-value,
valid-combination, SKU, Availability, price, stock, customer, order, or runtime
truth.

## Verified Sources

The required Slack source was read completely before repository mutation:

- C003 Mission Packet: channel `C0BNHRRTE9F`, parent
  `1786969720.051019`, plus both replies;
- Founder Product & Commerce Discovery Session 01: channel
  `C0BNHRRTE9F`, parent `1786929259.157699`, plus all eight replies,
  including `PART 1` through `PART 7` and `CHECKPOINT 02`.

Slack remains source evidence for this bounded intake. After integration, the
Repository package is the durable governed reference; Slack does not become a
parallel Product authority.

## Classification Discipline

| Classification | Repository meaning | Promotion boundary |
| --- | --- | --- |
| `FOUNDER_CONFIRMED` | Direct business or market evidence, intent, requirement, or future capability explicitly stated or accepted by the Founder | May be preserved as evidence or a requirement; never automatically creates a Product, value, valid tuple, SKU, Availability, stock, price, or runtime object |
| `FOUNDER_ACCEPTED_CANDIDATE` | A candidate explicitly accepted by the Founder for later modeling or consideration | Remains candidate-only until the applicable canonical owner, evidence, review, and Founder gates pass |
| `ARCHITECTURE_PROPOSAL` | Design input derived from or supported by discovery | Must carry an explicit owner and disposition; it is not implemented authority |

Temporal meaning is independent of evidence class:

Deferral changes only `temporal_role`. A Founder-originated or
Founder-explicitly-approved requirement remains `FOUNDER_CONFIRMED` when its
temporal role is `FUTURE_CONCEPT`; it must not be downgraded to
`ARCHITECTURE_PROPOSAL` merely because implementation is deferred. Likewise, a
Founder-accepted future candidate retains `FOUNDER_ACCEPTED_CANDIDATE`.

| Temporal role | Meaning |
| --- | --- |
| `CURRENT_INTENT` | Current business evidence or requirement, still bounded by its evidence class |
| `HISTORICAL_EXAMPLE_NONCURRENT` | Historical/illustrative evidence that cannot become current/public price, stock, Availability, universal validity, or an active policy rule |
| `FUTURE_CONCEPT` | Future target or idea that remains inactive and separately gated |

Every machine-readable record carries a canonical owner and a closed
`authority_effects` object whose Product/SKU/Availability/stock/price/commerce/
Runtime/Production effects are all false; this Scope supplies the explicit
disposition mapping. A complete source-attribution re-audit of all 115 records
separates Founder business intent from proposed architecture. Evidence-class
counts are `FOUNDER_CONFIRMED=70`, `FOUNDER_ACCEPTED_CANDIDATE=3`, and
`ARCHITECTURE_PROPOSAL=42`; temporal-role counts remain `CURRENT_INTENT=86`,
`HISTORICAL_EXAMPLE_NONCURRENT=4`, and `FUTURE_CONCEPT=25`.

## Canonical Owner Reconciliation

| Discovery concept | Disposition | Canonical or future owner | C003 boundary |
| --- | --- | --- | --- |
| Consolidated Product Group and dependent valid options | `RECORD` | Canonical Family/Series/Variant Rules plus downstream presentation mapping | Product Group remains UX/presentation only; no new canonical hierarchy layer |
| Evidence-backed valid combinations | `KEEP` | Variant Rules and future governed Product records | Controlled vocabularies never imply Cartesian validity or Availability |
| Product Builder and controlled `+ Add Value` | `KEEP` | C002 Product Administration Policy | Proposal lifecycle remains inactive and cannot mutate canonical registries |
| Brand, manufacturer, supplier, and origin | `KEEP` | C002 Brand Provenance | Roles remain distinct; market-brand evidence creates no Brand or availability instance |
| Size, grade, length, and appearance evidence | `RECORD` | Product Attributes, controlled values, measurements, and Variant Rules | Confirmed evidence and candidates retain their source class; no value or tuple is promoted |
| Commercial mass variability | `KEEP` | C002 Mass Provenance and Measurements | Mass is an observation with provenance, not a primary Variant Identifier |
| `SUPPLIER_STATED` mass provenance | `BACKLOG` | Proposed extension to C002 Mass Provenance | Discovery record `C003-DISC-035` remains solely `ARCHITECTURE_PROPOSAL` with `proposed_extension_state=PROPOSED_EXTENSION_REQUIRING_SEPARATE_REVIEW`. It is not a Founder-accepted candidate. No mass instance, canonical value, Product, SKU, or availability claim is created |
| Electrostatic color/sheen/texture/coating | `KEEP` | C002 Electrostatic Appearance | Remains separate from stainless finish and PVD; no appearance value is created |
| Smart History | `BACKLOG` | Future Product Administration policy | Suggestions require context, provenance, explicit operator choice, and anomaly review; history never becomes current truth automatically |
| Flexible pricing units, group pricing, and manual override | `BACKLOG` | Future confidential Pricing policy | Requirements and audit fields only; no current/public prices, formulas, discounts, margins, or automatic updates |
| FX-linked pricing signal | `DEFER` | Future separately authorized Pricing Signal policy | Human-reviewed target only; no FX integration or automatic price mutation |
| Damavand seller and internal upstream sourcing | `KEEP` | C002 Brand Provenance and future sourcing policy | Damavand remains customer-facing seller; upstream source identity stays internal at current state |
| Marketplace / supplier portal | `DEFER` | Future strategy decision | Marketplace remains `NO-GO`; compatibility does not authorize a panel or transaction flow |
| Deals, Volume, Pack, Assortment, and Inventory Harmony | `BACKLOG` | C002 Inventory Harmony plus future Deals policy | Examples are evidence only; no stock, pricing, discount, eligibility, substitution, or activation effect |
| Availability, reservation, operator verification, and dispatch timing | `BACKLOG` | Future Availability/Order policy | Public-state requirements create no Availability instance, exact stock count, fixed ETA, reservation, or order workflow |
| Cutting, packaging, delivery, freight, and shipment evidence | `BACKLOG` | Future Fulfillment and Service policy | Services do not become Product attributes; open pricing/remainder rules remain unresolved |
| OTP identity, Customer profile, CRM segmentation, and follow-up | `BACKLOG` | Inquiry/Customer/CRM policy owners | Target requirements only; no account, customer record, PII, CRM, notification, or workflow is created |
| Loyalty, Referral, Customer Type, Loyalty Tier, and Price Group | `BACKLOG` | Future Growth/CRM policy | Dimensions remain separate; no points, reward, discount, tier, segment, or price assignment is activated |
| Payment and commercial documents | `BACKLOG` | Future private Order/Payment/Document policy | Current business evidence is preserved without checkout, gateway, payment, quote, invoice, or public price implementation |
| Returns, damage claims, and shipment records | `BACKLOG` | Future Returns/Fulfillment policy | Damage and change-of-mind remain separate; no automated return entitlement or runtime record is created |
| RBAC | `DEFER` | Existing future role/permission architecture | Readiness intent only; no role or capability is activated |
| Tax extensibility | `DEFER` | Future legally reviewed Tax policy | Preserve base/tax/final separation intent; no rate, calculation, evasion behavior, or runtime setting is created |

## Machine-Readable Package

C003 adds one evidence package while reusing existing Product and C002 owners:

- `repository/data/contracts/founder-product-commerce-discovery.contract.yaml`;
- `repository/data/schemas/founder-product-commerce-discovery.schema.json`;
- `repository/data/registries/extensions/c003/founder-product-commerce-discovery-session-01.yaml`;
- `repository/data/validation/validate_founder_product_commerce_discovery.py`;
- deterministic positive, negative, mutation, and adversarial fixtures/tests.

The package is an evidence and disposition registry, not a Product registry.
The canonical C002 Commercial Pilot candidate registry remains empty. The C002
Product Administration registry retains eight policy definitions and zero
instances. No C003 evidence ID is a Product ID, SKU, Availability record,
commerce-eligibility instance, price record, customer identity, or order.

## Backlog and Open-Question Boundary

C003 records inactive requirements and explicitly unresolved policy work for:

- exact evidence-backed Brand/size/grade/appearance/length combinations;
- Product Group display order and content/media inheritance;
- Smart History matching, anomaly, retention, and approval rules;
- pricing groups, manual overrides, confidential price authority, rounding,
  and quote validity;
- availability evidence, reservation, replenishment, operator verification,
  cancellation, and dispatch communication;
- cutting remainder, packaging pricing, freight quotation, and shipment proof;
- privacy, consent, OTP, CRM, segmentation, loyalty, referral, contact-channel,
  and follow-up rules;
- payment verification, documents, returns, damage, RBAC, and legal tax policy.

These are candidate future scopes only. C003 starts neither `C003-A — Offline
Pilot Projection Package` nor `C003-B — Manual-First Growth/CRM Loop` and does
not recommend either as automatically ready.

## Validation and Independent Review

The package must pass:

- closed JSON Schema Draft 2020-12 validation using local references only;
- duplicate-key, non-finite-value, unsafe-path, unknown-field, and provenance
  rejection;
- deterministic positive, negative, mutation, and adversarial tests;
- checks that no historical price, candidate dimension, market brand, Harmony
  example, or Availability requirement is promoted;
- verification that C002 candidate and policy-instance registries remain empty,
  current commerce remains `INQUIRY_ONLY`, and no Runtime authority exists;
- repository `make test`, manifest/link/security checks, and
  `git diff --check`;
- independent review result `PASS — 0 MATERIAL FINDINGS` before PR-ready.

## Explicit No-Go

No Product, SKU, valid-combination, controlled-value, Availability, stock,
current/public price, margin, discount, coupon, offer, customer, order,
payment, Product/SKU population, C002 candidate/policy-instance population,
WordPress, WooCommerce, import, Runtime, Staging, Publishing, Deployment,
Production, FX automation, marketplace, supplier portal, Central Steel, n8n,
OpenAI API, C1-T03 repair, successor Mission, or merge is authorized.

## Completion Boundary

C003 is complete only when the bounded branch is independently reviewed,
locally validated, pushed, represented by exactly one open non-draft PR, and
required CI passes. Merge remains a separate Founder/Project Commander gate.

## References

- [Current Project State](CURRENT_PROJECT_STATE.md)
- [C000 / Project OS 2.0 Decision Package](C000_OS2_STRATEGIC_RECONCILIATION_DECISION_PACKAGE.md)
- [C002 Contract Scope](C002_COMMERCIAL_PILOT_PRODUCT_ADMINISTRATION_CONTRACTS_SCOPE_V1.0.md)
- [Context Router](CONTEXT_ROUTER.md)
- [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md)
- [Inquiry-first ADR](adr/0001-inquiry-first-commerce.md)
