# Damavand Component Pattern Library

## Document Control

- **Document ID:** `repository/design/COMPONENT_PATTERN_LIBRARY.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Design, UX, Content, Accessibility, SEO, Product Data, Blocksy, Elementor, and Performance Reviewers
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-08-21
- **Last Review:** 2026-08-21
- **Review Cycle:** On component purpose, content/data contract, token, motion, ownership, accessibility, or platform change
- **Lifecycle:** Review
- **Source of Truth:** [Design Manifest](DESIGN_MANIFEST.md), approved content/data authorities, and approved platform ownership
- **Dependencies:** [Design Manifest](DESIGN_MANIFEST.md), [Product Experience Engine](../enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md), [Content Architecture](../../docs/29_CONTENT_ARCHITECTURE.md), [Blocksy Blueprint](../../docs/36_BLOCKSY_CONFIGURATION.md), and [Elementor Blueprint](../../docs/37_ELEMENTOR_ARCHITECTURE.md)
- **Related Documents:** [Brand Language](BRAND_LANGUAGE.md), [Motion System](MOTION_SYSTEM.md), [Animation Library](ANIMATION_LIBRARY.md), and [Accessibility Rules](ACCESSIBILITY_RULES.md)
- **Traceability:** CP-003–CP-007, `FD-W2G-001`, `FD-W2G-002`, BLOCKSY-003–BLOCKSY-009, ELEMENTOR-001–ELEMENTOR-009, and Sprint 05A
- **AI Compatibility:** AI-readable pattern contracts; no generated component, page, template, or runtime feature is authorized
- **Approval:** Pending Founder and specialist review; patterns are conceptual and implementation-neutral

## Purpose

Define reusable component contracts that future WordPress-native presentation may consume without creating Elementor templates, Blocksy configuration, CSS, JavaScript, pages, or content.

Canonical repository Product truth follows exactly `Catalog → Platform → Family → Series → Variant Rules → derived SKU`. WordPress and WooCommerce may consume that truth only as downstream operational or presentation projections with system-local records and mapping IDs. Blocksy and Elementor are presentation-only consumers: they cannot own Product facts, entity identity, Variant Rules, or derived SKU authority.

## Common Component Rules

Every component requires an approved purpose, owner, source fields/content, lifecycle, states, mobile/RTL behavior, accessibility contract, SEO role, performance budget, motion classification, empty/error fallback, Blocksy/Elementor owner, and retirement path.

- Canonical Product facts remain only in approved repository Product Data sources; WordPress/WooCommerce records and component fields are downstream projections. Content, Inquiry, and SEO sources retain authority only within their own governed non-Product concerns.
- Components do not contain public pricing, cart, checkout, payment, Offer, stock, certification, partner, or performance claims unless an approved source explicitly owns the fact; public pricing remains prohibited in all cases.
- Blocksy owns the global shell and defaults. Elementor may compose only approved body patterns.
- Exact visual tokens, copy, layout measurements, and runtime identifiers remain pending approval.

## Component Contracts

### Hero

- **Purpose:** Establish page identity, primary proposition, and one approved next action.
- **Required content:** Semantic heading, concise supporting text, contextual inquiry or navigation action, and optional governed media.
- **Ownership:** Blocksy for shell context; Elementor/content owner for delegated body composition.
- **Motion:** At most one Limited/Experimental accent; content is visible immediately.
- **Mobile/RTL:** Text-first stacking, stable reading order, no horizontal overflow or motion-dependent meaning.
- **Constraints:** No public price, unsupported claim, autoplay-heavy media, or competing CTAs.

### Header

- **Purpose:** Provide identity, primary navigation, search entry, and approved inquiry access.
- **Required content:** Approved brand identity, navigation labels, current state, and accessible mobile control.
- **Ownership:** Blocksy exclusively unless a later architecture decision changes it.
- **Motion:** Short state/disclosure feedback; Pill Nav may inform active state.
- **Mobile/RTL:** Blocksy-owned RTL menu behavior, keyboard/focus integrity, and visible close/open state.
- **Constraints:** Elementor must not duplicate; no decorative motion that delays navigation.

### Pill Navigation

- **Purpose:** Show compact current location or switch among approved peer views.
- **Required content:** Explicit labels, current state, valid destinations/control semantics.
- **Ownership:** Blocksy for global navigation; Elementor for approved in-page navigation only.
- **Motion:** Low-intensity active-indicator transition.
- **Mobile/RTL:** Wrap, accessible scroll, or approved disclosure; logical RTL order.
- **Constraints:** No clipped essential item, unlabeled icon, or fake-tab semantics.

### CTA Button

- **Purpose:** Initiate an approved inquiry, navigation, download, or support action.
- **Required content:** Action-specific label and complete accessible name; status when processing.
- **Ownership:** Shared global token contract; action owner depends on canonical workflow.
- **Motion:** State feedback only; Limited Border Glow/Star Border on one focal CTA after review.
- **Mobile/RTL:** Touch-safe, stable, and clearly separated from secondary actions.
- **Constraints:** No false urgency, price/checkout implication, movement of the target, or motion-only state.

### Product Card

- **Purpose:** Summarize an approved downstream Product projection and lead to its canonical public-page URL or inquiry.
- **Required content:** Approved projected name, media fallback, selected repository-sourced facts, canonical public-page link, and inquiry action/state.
- **Ownership:** Canonical Product facts remain in repository Product Data; WooCommerce supplies a downstream operational projection, while Blocksy owns only default archive/card presentation and Elementor may compose only an explicitly delegated body pattern.
- **Motion:** Low-intensity focus/hover/disclosure; no tilt or pointer chase.
- **Mobile/RTL:** Core facts and inquiry remain visible without hover; mixed-script dimensions are readable.
- **Constraints:** No public price, cart, checkout, Offer, invented availability, or local duplicate facts.

### Dependent Variant Selector

- **Purpose:** Ask only the next Family-configured question and expose only options permitted by governed Variant Rules.
- **Required content:** Current question, governed options, explicit selected/disabled/unknown/verification states, visible selected context, and back/change/reset controls.
- **Ownership:** Variant Rules owns axes, values, constraints, and valid tuples; the Product Experience Engine owns presentation sequence only.
- **Motion:** Short state feedback only; content and option availability never depend on animation.
- **Mobile/RTL:** One primary question per step, logical Persian RTL DOM/focus order, touch-safe controls, BiDi-safe technical values, and no horizontal trap.
- **Constraints:** No universal hard-coded order, Cartesian options, inferred compatibility, unsupported option, hover-only state, or Availability inference.

### Selected Product Summary

- **Purpose:** Keep the current governed selection visible and provide a compact live summary before Inquiry handoff.
- **Required content:** Canonical source context, selected attributes, independent combination-resolution state, and separately labeled technical/commercial projections when authorized.
- **Ownership:** Each source domain retains authority; the component composes read-only projections and stores no facts.
- **Motion:** Immediate update with optional restrained transition; assistive output announces material changes once.
- **Mobile/RTL:** Compact primary summary with accessible disclosure for technical detail; selected values remain changeable without restarting the journey.
- **Constraints:** No derived-as-measured value, unknown-as-out-of-stock, stale commercial fact, flattened ownership, public price, or purchase implication.

### Product Media and Knowledge Region

- **Purpose:** Present media and educational references that are explicitly applicable to the selected context.
- **Required content:** Eligible media reference or governed placeholder, applicability/rights/access state, and approved public Knowledge references when available.
- **Ownership:** Media and Knowledge/Content owners retain truth; Product Experience applies their inheritance and override rules.
- **Motion:** Static first; gallery behavior requires separate accessibility and performance review.
- **Mobile/RTL:** Preserve focal context, captions, alt text, reading order, and accessible disclosure on narrow viewports.
- **Constraints:** No false Family-image inheritance across materially different Appearance/Finish, unapproved competitor asset, invented Knowledge, protected item, or media-derived Availability claim.

### Inquiry Card

- **Purpose:** Explain and initiate the correct inquiry route with preserved context.
- **Required content:** Inquiry type/purpose, exact governed selection or explicit unresolved state, required-context summary, explicit action, and privacy/support cues where approved.
- **Ownership:** Inquiry model/capability owns workflow; presentation only renders approved states.
- **Motion:** Minimal focus, validation, progress, and outcome feedback.
- **Mobile/RTL:** One clear action, stable input/label alignment, no overlay dependency.
- **Constraints:** No inherited purchase eligibility, checkout imitation, price promise, guaranteed response time, unapproved fields, or decorative ambient motion.

### Brand Logo Loop

- **Purpose:** Present verified brand/partner/standards relationships.
- **Required content:** Approved logo asset, relationship type, lifecycle, alt/link policy, and provenance.
- **Ownership:** Content/media owner; presentation may use Elementor body or approved footer region.
- **Motion:** Static by default; Limited finite/pausable loop only after review.
- **Mobile/RTL:** Static grid or manual scroll; no autoplay requirement.
- **Constraints:** No fabricated, expired, unlicensed, or duplicated marks.

### Stats Counter

- **Purpose:** Present a verified metric with context and review date/source.
- **Required content:** Final value, unit, description, provenance, and lifecycle.
- **Ownership:** Approved content/data source; component cannot calculate business truth.
- **Motion:** Optional one-time finite count; final value exists immediately.
- **Mobile/RTL:** Clear value/unit grouping and mixed-script reading.
- **Constraints:** No public price, live stock, vanity metric, or repeated screen-reader announcement.

### Stepper

- **Purpose:** Explain or support an approved sequence such as inquiry stages or selection guidance.
- **Required content:** Ordered steps, current/completed state where applicable, and exceptions/fallbacks.
- **Ownership:** Governing workflow owns stages; component owns presentation only.
- **Motion:** Short user-triggered state transition.
- **Mobile/RTL:** Vertical sequence preferred; explicit text states.
- **Constraints:** No invented workflow, forced linearity, hidden requirement, or guaranteed outcome.

### Footer

- **Purpose:** Provide organization identity, support, inquiry, policies, approved navigation, and lifecycle information.
- **Required content:** Approved groups and links from Site Structure/content authorities.
- **Ownership:** Blocksy.
- **Motion:** Predominantly static; optional Limited verified logo treatment.
- **Mobile/RTL:** Logical stacked order, accessible headings, no collapsed essential legal/support content.
- **Constraints:** Elementor must not create a competing footer; no heavy background animation.

### Contact Section

- **Purpose:** Present approved contact channels, service context, and inquiry route.
- **Required content:** Verified contact facts, hours/coverage only if approved, action labels, and privacy context.
- **Ownership:** Content/organization source owns facts; inquiry capability owns submission.
- **Motion:** State feedback only.
- **Mobile/RTL:** Tap-safe contact actions with unambiguous Persian labels and LTR-safe phone/email rendering.
- **Constraints:** No unsupported availability, response promise, exposed private data, or decorative distraction.

### Feature Grid

- **Purpose:** Summarize approved capabilities, services, benefits, or technical themes.
- **Required content:** Equal-level items with concise title, description, optional icon, and source owner.
- **Ownership:** Content owner; Elementor may compose in a delegated body area.
- **Motion:** Magic Bento inspiration is Limited and optional.
- **Mobile/RTL:** Linear/two-column progression matching DOM order.
- **Constraints:** No unsupported benefits, hover-only details, or excessive card effects.

### Category Card

- **Purpose:** Lead to an approved taxonomy/category landing page.
- **Required content:** Canonical category name, approved description/media, canonical URL, and optional verified count.
- **Ownership:** Governed taxonomy and repository Product Data sources retain their respective identities; WordPress/WooCommerce records are downstream mappings, and Blocksy owns only default archive presentation.
- **Motion:** Low-intensity state emphasis only.
- **Mobile/RTL:** Name and destination remain visible without hover.
- **Constraints:** No duplicate category, invented subcategory, local slug, public price, or empty SEO doorway.

### Trust Section

- **Purpose:** Present verifiable reasons to engage, supported by approved evidence.
- **Required content:** Governed claims, provenance, owner, review date, and links where appropriate.
- **Ownership:** Brand/content authority with legal/domain review as applicable.
- **Motion:** Optional Counter, Logo Loop, Light Rays, or Border Glow within their limits; normally one family only.
- **Mobile/RTL:** Static clarity first; verified evidence precedes decoration.
- **Constraints:** No fabricated metrics, logos, certifications, testimonials, awards, guarantees, or motion-as-proof.

## Component State Model

Applicable components define: default, hover, focus-visible, active/current, selected, loading, disabled, empty, error, success, reduced-motion, offline/dependency-failure, and archived/unavailable states. Only states relevant to the component may be implemented; absent states are documented rather than improvised.

For Product selection, combination resolution and Availability are separate state
axes. A valid selection does not prove Availability; missing Availability evidence
does not make a combination incompatible or out of stock.

## Future Acceptance Checklist

- Canonical content/data and owner identified.
- Blocksy/Elementor responsibility is singular and explicit.
- Persian RTL/mobile, keyboard, focus, contrast, text scaling, reduced-motion, and mixed-script tests pass.
- Inquiry First and No Public Pricing checks pass.
- SEO semantics and canonical link ownership pass.
- Performance budget and Core Web Vitals evidence pass.
- Configuration export, dependency inventory, staging evidence, and rollback are approved.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-08-21 | C006 architecture-only reconciliation: added dependent selector, selected summary, Media/Knowledge applicability, separate combination/Availability state, and Inquiry handoff contracts; no component or Runtime behavior created. |
| 0.1.1 | 2026-08-03 | C1-T06 canonical-owner reconciliation under `FD-W2G-001` and `FD-W2G-002`: restricted Product facts to repository sources and qualified WordPress/WooCommerce, Blocksy, Elementor, and components as downstream operational/presentation consumers; no component, page, fact, or runtime object created. |
| 0.1.0 | 2026-07-05 | Initial conceptual library for 14 required component patterns. |

## Navigation

- [Design Manifest](DESIGN_MANIFEST.md)
- [Brand Language](BRAND_LANGUAGE.md)
- [Motion System](MOTION_SYSTEM.md)
- [ReactBits Inspiration Mapping](REACTBITS_INSPIRATION_MAPPING.md)
- [Animation Library](ANIMATION_LIBRARY.md)
- [Product Experience Engine](../enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md)
