# Product Experience Engine

## Document Control

- **Document ID:** `repository/enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md`
- **Status:** Review
- **Authority:** C006 architecture-only owner
- **Owner:** Founder
- **Reviewer:** Product Data, UX, Accessibility, SEO, Media, Knowledge, Inquiry, and WooCommerce Reviewers
- **Approval Authority:** Founder
- **Version:** 1.0.0
- **Last Updated:** 2026-08-21
- **Lifecycle:** Review
- **Source of Truth:** canonical Product and Variant Rules owners, [C002 Contract Scope](../../docs/C002_COMMERCIAL_PILOT_PRODUCT_ADMINISTRATION_CONTRACTS_SCOPE_V1.0.md), [C004 Experience Blueprint](../../docs/201_51_PILOT_COMPETITIVE_EXPERIENCE_BLUEPRINT_V1.0.md), and the C006 Product Page Interaction Model
- **Dependencies:** [Product Data Model](../../docs/19_PRODUCT_DATA_MODEL.md), [Search and Discovery](../../docs/27_SEARCH_AND_DISCOVERY.md), [Content Architecture](../../docs/29_CONTENT_ARCHITECTURE.md), [Media Strategy](../../docs/33_MEDIA_STRATEGY.md), [SEO Entity Model](../../docs/34_SEO_ENTITY_MODEL.md), and [Inquiry Data Model](../../docs/23_INQUIRY_DATA_MODEL.md)
- **Implementation Authority:** None

## Purpose and Boundary

Define how a future Product-family experience composes governed Product,
technical, commercial, media, Knowledge, SEO, and Inquiry projections without
becoming an authority for any of them.

This document creates no Product, Variant, SKU, Availability, Mass, price,
content, media, page, URL, WooCommerce record, selector, CTA, or Runtime state.
It does not authorize WordPress, WooCommerce, Blocksy, or Elementor changes.

## Authority Map

| Concern | Authority | Product Experience role |
| --- | --- | --- |
| Identity, attributes, axes, values, valid combinations | Canonical Product owners and Variant Rules | Read-only projection |
| Mass, Availability, price, and supply evidence | Their separately governed dynamic/commercial owners | Optional evidence-bound composition; never inference |
| Media | Media Strategy and Product Media Set | Applicability resolver only |
| Knowledge and application guidance | Approved Knowledge/Content owner | Reference and disclosure only |
| Public page, search intent, canonical, indexation | SEO Entity and Search owners | Non-authoritative projection |
| Inquiry record and handoff | Inquiry Data Model and Inquiry Workflow | Preserve and submit selected context |
| Purchase eligibility | C002 Commerce Eligibility, per canonical SKU | Read-only future input; never inherited |
| WordPress/WooCommerce/Blocksy/Elementor | Downstream adapter and presentation owners | Render approved projection only |

## Experience Flow

```text
Canonical Family context
  -> family-configured dependent selection
  -> Variant Rules resolution
  -> selected-context summary
  -> technical and commercial projections kept separate
  -> applicable media and Knowledge references
  -> Inquiry CTA under current INQUIRY_ONLY operation
```

The flow is architecture only. It does not imply that any current Family has an
approved selector profile, public page, or eligible Product record.

## Dependent Selector Contract

- Each Family defines its own ordered selection dimensions; no universal order
  is hard-coded.
- Every dimension and option is a stable reference to a governed attribute,
  value, or Variant Rules source. Labels and WooCommerce terms are projections.
- Each accepted choice filters later options through evidence-backed Variant
  Rules. Controlled-vocabulary membership alone never proves a valid tuple.
- Cartesian generation, unsupported options, duplicate dimensions, inferred
  compatibility, and automatic Product/SKU creation are prohibited.
- The selected context remains visible, reversible, changeable, and resettable.
- Partial and missing evidence fail closed without turning unknown into invalid,
  unavailable, or out of stock.

### Separate state axes

Combination resolution and Availability are independent:

- combination resolution may be `UNSELECTED`, `PARTIAL`, `VALID`, `UNKNOWN`,
  `INCOMPATIBLE`, or `NEEDS_VERIFICATION`;
- Availability is absent unless a separately governed owner provides current,
  valid, reviewed evidence for the exact subject;
- an Availability projection never proves combination validity, and a valid
  combination never proves Availability.

The Founder-confirmed customer Availability vocabulary remains governed outside
this engine. No state, source habit, missing record, or WooCommerce flag may be
translated into a stock or delivery claim here.

## Selected Context and Live Summary

The compact primary summary may display only currently governed facts for the
selected context: canonical identity references, Brand, Grade, Diameter/Size,
Thickness, Finish, Color/Appearance, Length, customer order Unit, and separately
labeled technical or commercial projections.

- Derived values must be labeled as calculated/nominal and retain formula/input
  provenance; they cannot be presented as measured evidence.
- Current Mass, Availability, price basis, and supply context remain separate
  optional domains with their own evidence and freshness.
- Missing, conflicting, expired, or unauthorized values use an explicit
  unavailable/verification state; they are never guessed.
- Mobile shows a compact primary summary with accessible progressive disclosure
  for technical detail. Required facts are never hover-only or motion-dependent.

## Media and Knowledge Resolution

Media resolution is deterministic:

```text
exact eligible Variant override
  -> eligible Appearance/Finish override
  -> eligible Family asset only when explicitly accurate for the selected context
  -> governed placeholder or no media
```

Every selected asset must have applicability, rights, access, lifecycle,
localization, and accessibility evidence. A Family image must not be inherited
when the selected Appearance or Finish materially differs.

Knowledge uses approved public references only. Family Knowledge may be extended
or overridden by Grade, Brand, or Variant context only when applicability and
source authority are explicit. Missing Knowledge remains absent. This engine
does not create Knowledge content or technical claims.

## SEO and Search Boundary

- Selector, filter, and query states are non-canonical and non-indexable by
  default.
- No page, URL, sitemap entry, canonical, or schema entity is generated per
  Brand, Thickness, Finish, Length, or arbitrary tuple.
- An indexable page requires a separately approved unique intent, one public
  owner, original useful content, governed sources, and anti-cannibalization
  review.
- Product structured data must not contain unauthorized Offer, price, stock, or
  Availability claims.
- Search and filtering may complement selection but cannot become Variant Rules
  or Product authority.

## Inquiry and Commerce CTA Boundary

The current effective CTA is contextual Inquiry with operator verification. The
handoff preserves canonical source references, the selected valid context or
explicit unresolved selections, submission-time labels, quantity/Unit when
provided, source URL, and permitted media/document references.

Purchase CTA is prohibited unless a future exact canonical SKU has a current,
evidence-complete and separately activated C002 Commerce Eligibility instance.
Eligibility is never inherited from Catalog, Family, Series, Product, Parent,
Variation, Pilot, selector state, or Availability. WooCommerce does not confer
Product or Commerce authority and must not imitate checkout while eligibility is
absent or `INQUIRY_ONLY`.

## Persian RTL, Mobile, and Accessibility

- Define and test logical DOM, visual, focus, and announcement order in Persian
  RTL from the smallest supported viewport.
- Preserve readable mixed-direction Grade, Brand, dimensions, decimals, and
  Units without changing their technical meaning.
- Use touch-safe and keyboard-operable controls with visible focus and explicit
  selected, disabled, loading, empty, error, and verification states.
- Keep back/change/reset available without precision gestures, hover, or hidden
  context; restore focus after disclosures or dialogs.
- Screen readers receive the current question, selected value, option changes,
  validation result, and summary update without repeated or motion-only output.

## Projection Ownership

Blocksy owns the default product shell and WooCommerce presentation. Elementor
may compose only a separately delegated body region. Neither may store Product
facts, selector rules, media applicability, SEO authority, Inquiry state, or
Commerce Eligibility in template-local values. WooCommerce owns only supported
system-local adapter records and interfaces; canonical truth remains upstream.

## Validation and No-Go

Future machine validation must reject at minimum: Cartesian selectors,
unsupported options, Availability/validity conflation, false media inheritance,
unapproved Knowledge, selector-state indexation, page-per-tuple generation,
WooCommerce authority inversion, inherited purchase eligibility, premature
purchase CTA, unknown-as-out-of-stock, and public pricing/Offer leakage.

Implementation, Product/SKU population, Availability or current Mass creation,
price activation, content/media publication, SEO page creation, WordPress or
WooCommerce configuration, Runtime, deployment, and Production remain `NO-GO`.

## Navigation

- [Component Pattern Library](../design/COMPONENT_PATTERN_LIBRARY.md)
- [WooCommerce Product Model](../../docs/20_WOOCOMMERCE_PRODUCT_MODEL.md)
- [WooCommerce Configuration](../../docs/38_WOOCOMMERCE_CONFIGURATION.md)
- [C004 Experience Blueprint](../../docs/201_51_PILOT_COMPETITIVE_EXPERIENCE_BLUEPRINT_V1.0.md)
