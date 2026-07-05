# Damavand Motion System

## Document Control

- **Document ID:** `repository/design/MOTION_SYSTEM.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Motion, UX, Accessibility, Performance, Blocksy, Elementor, and QA Reviewers
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On motion ratio, category, component, accessibility, performance, platform, browser, or device-policy change
- **Lifecycle:** Review
- **Source of Truth:** [Design Manifest](DESIGN_MANIFEST.md), explicit Sprint 05A motion direction, and approved Design Decision Records
- **Dependencies:** [Design Manifest](DESIGN_MANIFEST.md), [Performance Rules](PERFORMANCE_RULES.md), and [Accessibility Rules](ACCESSIBILITY_RULES.md)
- **Related Documents:** [ReactBits Inspiration Mapping](REACTBITS_INSPIRATION_MAPPING.md), [Animation Library](ANIMATION_LIBRARY.md), and [Component Pattern Library](COMPONENT_PATTERN_LIBRARY.md)
- **Traceability:** CP-003, CP-004, CP-010, DDR-0001, DDR-0002, DDR-0004, and Sprint 05A
- **AI Compatibility:** AI-readable motion guidance; no runtime motion generation or AI feature is authorized
- **Approval:** Pending Founder, accessibility, performance, and presentation review; no animation implementation is authorized

## Purpose

Define how motion may support orientation, feedback, hierarchy, and brand expression while protecting readability, accessibility, performance, and B2B trust.

## Motion Philosophy

Motion is a functional layer before it is a decorative layer. It should explain change, confirm action, preserve spatial context, or focus attention. Expressive motion is optional and must never be required to understand content.

The system prefers:

- Short, predictable state transitions.
- Transform/opacity-style visual change where future supported configuration permits it.
- User-triggered motion over autonomous motion.
- Finite motion over continuous motion.
- Static clarity over spectacle.

## Approved Motion Ratio: 85 / 10 / 5

| Share | Meaning | Typical content |
| --- | --- | --- |
| 85% clean | Stable, readable interface with no expressive motion | Body content, specifications, tables, forms, navigation structure |
| 10% motion | Purposeful transitions and feedback | Focus, hover, disclosure, step state, button/card response |
| 5% wow | Rare, brand-defining emphasis | One approved hero accent, trust moment, or campaign-quality feature |

This is an experience-allocation principle, not a measurement of DOM nodes, runtime, or page area. A page may—and often should—use less motion.

## Motion Categories

| Category | Purpose | Default intensity | Default policy |
| --- | --- | --- | --- |
| State | Communicate hover, focus, active, selected, expanded, success, or error | Low | Allowed when accessible |
| Spatial | Explain entry, exit, disclosure, or step progression | Low–medium | Limited and user-triggered |
| Attention | Emphasize one current action or status | Medium | Time-limited; never constant around forms |
| Ambient | Add controlled depth without conveying meaning | Low | Optional; off for reduced motion/mobile constraints |
| Expressive | Create a deliberate wow moment | Medium | Experimental until measured and approved |
| Data | Reveal a verified count or progression | Low | Content remains directly available |

## Timing and Behavior Guidance

- Micro-feedback target: approximately 120–240 ms.
- Disclosure or card transition target: approximately 180–360 ms.
- Section reveal target: approximately 240–500 ms.
- Expressive accent: normally completes within 600 ms unless it is a low-intensity ambient loop.
- Avoid long chained sequences, artificial loading, scroll-jacking, parallax dependence, or motion that waits before showing content.
- Timing values are review targets, not production tokens; measured implementation evidence may justify adjustment.

## Hero Motion

- Maximum one primary expressive/ambient motion system in the initial viewport.
- Headline, proposition, and inquiry action are readable immediately and independently.
- Approved inspirations may include limited Light Rays, Gradient Text, Rotating Text, Strands, or a restrained Border Glow—never all together.
- Mobile defaults to a simpler or static variant.
- Hero motion must not delay LCP content, move layout, obscure focus, or introduce a runtime dependency.

## CTA Motion

- Use concise state feedback: focus, hover, press, loading, success, or error.
- Border Glow, Star Border, or Shiny Text is limited to one approved primary action context and must remain legible when static.
- No pulsing urgency, infinite shake, fake scarcity, or movement that implies a price/transaction.
- Inquiry actions retain explicit text and keyboard-visible focus.

## Navigation Motion

- Motion supports opening, closing, selection, focus, and orientation.
- Pill Nav inspiration may shape the active indicator, but Blocksy retains global navigation ownership.
- No delayed menus, hover-only access, hidden focus, or directionally incorrect RTL travel.
- Mobile navigation favors immediate state change and short disclosure motion.

## Product Card Motion

- State changes may clarify focus, image selection, technical-detail disclosure, or inquiry action.
- Product cards must not tilt, chase the pointer, auto-rotate, or hide required data behind hover.
- Magic Bento or Border Glow inspiration is limited to non-blocking emphasis; actual product finish cannot be simulated as fact.
- Price, cart, checkout, and Offer behaviors remain prohibited.

## Form Motion

- Motion may confirm focus, validation, submission progress, success, or error.
- Error information is textual, programmatically associated, persistent until resolved, and never color/motion-only.
- No ambient, laser, particle, rotating, or continuous border effect inside inquiry forms.
- Motion must not reset input, move the submit target, or obscure privacy/consent text.

## Footer Motion

- Footer is predominantly static.
- A finite logo loop or subtle brand accent may be reviewed only when content, legal, contact, and support links remain stable.
- No heavy canvas background, autonomous decorative field, or motion that continues offscreen.

## Reduced-Motion Rules

When `prefers-reduced-motion: reduce` or an equivalent user/platform policy applies:

- Remove nonessential translation, rotation, zoom, parallax, particles, beams, strands, rings, and looping effects.
- Replace animated gradients/glows with static approved tokens.
- Show final content/state immediately.
- Keep necessary state changes short, non-spatial, and free of flashing.
- Never require a user to watch motion to receive information or complete an inquiry.

## Accessibility Rules

- No flashing, rapid luminance change, vestibular-heavy motion, or unexpected autoplay.
- Pause/stop controls are required for any approved persistent content-bearing movement.
- Focus order and visible focus remain stable during transitions.
- Screen-reader announcements describe state, not decorative movement.
- Color, glow, position, and animation are never the sole state indicator.
- Verify mixed Persian/Latin text remains readable throughout every animated state.

## Performance and Runtime Boundary

- ReactBits is conceptual inspiration only; no source component, package, runtime, dependency, or copied implementation is authorized.
- Prefer supported WordPress/Blocksy/Elementor state controls and low-cost CSS/SVG concepts in a future approved implementation.
- No production CSS, JavaScript, React, animation library, canvas, WebGL, video background, or Lottie asset is created here.
- Every future effect requires a static fallback, mobile policy, performance budget, measurement, ownership, and rollback plan.

## Motion Review Gate

An effect is eligible for future implementation only when purpose, location, owner, trigger, duration, repetition, mobile behavior, RTL behavior, reduced-motion fallback, accessibility result, performance result, SEO/content behavior, Blocksy/Elementor ownership, and rollback are approved.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial 85/10/5 motion guidance and safety boundaries. |

## Navigation

- [Design Manifest](DESIGN_MANIFEST.md)
- [ReactBits Inspiration Mapping](REACTBITS_INSPIRATION_MAPPING.md)
- [Animation Library](ANIMATION_LIBRARY.md)
- [Performance Rules](PERFORMANCE_RULES.md)
- [Accessibility Rules](ACCESSIBILITY_RULES.md)
