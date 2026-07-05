# Damavand Design Manifest

## Document Control

- **Document ID:** `repository/design/DESIGN_MANIFEST.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Design, UX, Accessibility, Performance, SEO, Content, Blocksy, and Elementor Reviewers
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On brand, design-token, component, motion, accessibility, platform, or presentation-boundary change
- **Lifecycle:** Review
- **Source of Truth:** [Core Project Principles](../../docs/00_PROJECT_BIBLE.md#core-project-principles), [WordPress Solution Blueprint](../../docs/35_WORDPRESS_BLUEPRINT.md), and explicit Sprint 05A Founder direction
- **Dependencies:** [Blocksy Configuration Blueprint](../../docs/36_BLOCKSY_CONFIGURATION.md), [Elementor Architecture](../../docs/37_ELEMENTOR_ARCHITECTURE.md), and [Platform Principles](../platform/PLATFORM_PRINCIPLES.md)
- **Related Documents:** [Brand Language](BRAND_LANGUAGE.md), [Motion System](MOTION_SYSTEM.md), [Component Pattern Library](COMPONENT_PATTERN_LIBRARY.md), [Performance Rules](PERFORMANCE_RULES.md), and [Accessibility Rules](ACCESSIBILITY_RULES.md)
- **Traceability:** CP-001–CP-010, BLOCKSY-001–BLOCKSY-009, ELEMENTOR-001–ELEMENTOR-009, DDR-0001–DDR-0004, and Sprint 05A
- **AI Compatibility:** AI-readable design guidance; no AI feature, generated runtime asset, or autonomous design decision is authorized
- **Approval:** Pending Founder and specialist review; no runtime implementation is authorized

## Purpose

Define the durable visual and interaction principles for Damavand Steel without selecting production tokens, creating pages, configuring WordPress, or introducing runtime dependencies.

## Design Philosophy

Damavand design should make a complex industrial catalog feel dependable, understandable, and easy to inquire about. Visual distinction supports comprehension and trust; it never replaces product facts, navigation, accessibility, or commercial clarity.

The system follows these priorities, in order:

1. Correct and legible information.
2. Clear path to an inquiry.
3. Mobile and Persian RTL usability.
4. Trust, restraint, and industrial credibility.
5. Selective premium expression.
6. Motion only when it adds orientation, feedback, or emphasis.

## Brand Feeling

The intended feeling is industrial, premium, calm, precise, and trustworthy. It must avoid both commodity-market clutter and entertainment-first spectacle. Exact logo treatment, palette, typography, photography direction, and token values remain pending Founder/design approval.

## Industrial Trust

- Show hierarchy, specifications, source labels, and inquiry actions without ambiguity.
- Use stable alignment, consistent spacing, predictable states, and disciplined repetition.
- Separate verified facts from marketing statements and from `TBD` information.
- Avoid visual treatments that suggest price, availability, certification, origin, warranty, or performance when those facts are not approved.
- Keep trust signals factual, attributable, current, and readable without animation.

## Premium Steel Identity

Premium expression may draw from precision, reflection, controlled contrast, structural rhythm, engineered surfaces, and material depth. It must not rely on excessive chrome effects, constant glow, decorative particles, or simulated claims about a product's actual finish.

Steel-inspired effects are presentation metaphors only. Product media and attributes remain the authority for actual material, grade, finish, color, and surface.

## B2B Usability

- Prioritize scanning, comparison, technical clarity, and inquiry context.
- Keep the primary inquiry action explicit and persistent where approved, without pressure tactics.
- Do not expose public pricing or imply checkout behavior.
- Support repeat visits, procurement review, project context, and handoff to Sales.
- Keep interfaces manageable through approved Blocksy and Elementor capabilities rather than page-specific inventions.

## Persian RTL Rules

- Design and validate in Persian RTL first; do not mirror an LTR composition after completion.
- Preserve logical reading order in the DOM and visual order in the interface.
- Keep Persian labels, numerals, units, Latin technical keys, grades, dimensions, and bidirectional strings unambiguous.
- Use direction-aware icons, spacing, controls, progressions, and motion.
- Do not reverse universal media controls, brand marks, numeric values, or technical notation without semantic reason.
- Validate wrapping, truncation, focus order, tables, cards, filters, forms, errors, and mixed-script content on narrow screens.

## Mobile-First Design Rules

- Define the smallest supported layout and interaction before larger variants.
- Preserve one clear primary action and readable content hierarchy per viewport.
- Avoid hover-only meaning, precision gestures, auto-playing complex motion, and horizontally trapped content.
- Use progressive disclosure for dense technical information without hiding required facts.
- Ensure touch targets, focus targets, sticky elements, overlays, and motion do not compete for limited space.
- Complex decorative motion is removed or replaced with a static fallback when device, bandwidth, viewport, or reduced-motion conditions require it.

## No Over-Animation Rule

The approved design ratio is 85% clean/static foundation, 10% purposeful motion, and 5% controlled wow moments. The ratio describes experience emphasis, not a requirement to animate 15% of elements.

- No page requires a wow effect.
- One primary ambient or expressive motion family per viewport is the default ceiling.
- Never stack competing continuous effects around the same content.
- Motion must not delay reading, inquiry, navigation, input, or Core Web Vitals.
- Every effect has a static and reduced-motion state before it is eligible for implementation review.

## Platform Boundaries

| Concern | Design guidance owner | Future runtime boundary |
| --- | --- | --- |
| Global shell, header, footer, navigation, base tokens | Blocksy-coordinated design system | Supported Blocksy/WordPress configuration only |
| Approved page and landing body composition | Elementor within delegated regions | Supported Elementor configuration only |
| Product/archive presentation | Blocksy by default | No delegation is created here |
| Product, inquiry, SEO, and business facts | Existing canonical data/governing sources | Design consumes; it does not author facts |
| Motion inspiration | This design system after approval | No React or ReactBits runtime dependency |

## Prohibited Design Outcomes

- Public price, cart, checkout, payment, or Offer presentation.
- Custom theme or vendor/core file edits.
- React, ReactBits, or an unnecessary animation-library dependency.
- AI-generated runtime features in Phase 1.
- Motion that blocks content, causes loss of control, or conveys unavailable facts.
- Duplicate Blocksy/Elementor token systems or competing global shells.
- Production CSS, JavaScript, Elementor artifacts, or WordPress configuration in this sprint.

## Approval Gates

Before future implementation, the Founder and applicable reviewers must approve:

- Exact design tokens and their Blocksy/Elementor ownership.
- Component use cases and content/data owners.
- Motion classification, budget, reduced-motion fallback, and device behavior.
- Persian RTL, mobile, keyboard, contrast, legibility, SEO, and Core Web Vitals evidence.
- Supported implementation route, export/rollback method, and dependency inventory.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial Sprint 05A Design Intelligence foundation; guidance only. |

## Navigation

- [Brand Language](BRAND_LANGUAGE.md)
- [Motion System](MOTION_SYSTEM.md)
- [ReactBits Inspiration Mapping](REACTBITS_INSPIRATION_MAPPING.md)
- [Component Pattern Library](COMPONENT_PATTERN_LIBRARY.md)
- [Animation Library](ANIMATION_LIBRARY.md)
- [Design Decision Records](DESIGN_DECISION_RECORDS.md)

