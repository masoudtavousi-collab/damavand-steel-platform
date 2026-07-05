# Design Accessibility Rules

## Document Control

- **Document ID:** `repository/design/ACCESSIBILITY_RULES.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Accessibility, UX, Persian Language, Motion, Content, Blocksy, Elementor, and QA Reviewers
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On accessibility target, component, motion, content, contrast, keyboard, platform, or legal requirement change
- **Lifecycle:** Review
- **Source of Truth:** [Design Manifest](DESIGN_MANIFEST.md), [Motion System](MOTION_SYSTEM.md), and approved accessibility requirements
- **Dependencies:** [Motion System](MOTION_SYSTEM.md), [Component Pattern Library](COMPONENT_PATTERN_LIBRARY.md), and [Performance Rules](PERFORMANCE_RULES.md)
- **Related Documents:** [Brand Language](BRAND_LANGUAGE.md), [Blocksy Blueprint](../../docs/36_BLOCKSY_CONFIGURATION.md), and [Elementor Blueprint](../../docs/37_ELEMENTOR_ARCHITECTURE.md)
- **Traceability:** CP-003, CP-004, WPBP-006, BLOCKSY-006, ELEMENTOR-008, DDR-0002, DDR-0004, and Sprint 05A
- **AI Compatibility:** AI-readable accessibility guidance; no automated result substitutes for human review
- **Approval:** Pending Founder and qualified accessibility review; implementation target/version remains to be approved

## Purpose

Ensure future Damavand presentation remains perceivable, operable, understandable, and robust for Persian RTL B2B use, with or without motion or decoration.

## Motion Safety

- No flashing, strobing, rapid luminance change, forced parallax, scroll-jacking, or unexpected large movement.
- Motion never carries the only instruction, state, error, relationship, or progress signal.
- Persistent content-bearing movement requires pause/stop/control and must not restart unexpectedly.
- User-triggered motion preserves focus, reading position, and target stability.
- Decorative motion cannot obstruct text, controls, captions, or focus indicators.

## Reduced Motion

- Respect `prefers-reduced-motion` and equivalent platform/user preference.
- Remove translation, rotation, scale, particles, beams, strands, rings, physics, parallax, and looping decoration where nonessential.
- Present final state/content immediately.
- Replace animated gradient/glow with a stable high-contrast token.
- Reduced-motion mode retains all functionality and information.

## Contrast

- Exact color tokens and target conformance version remain pending Founder/accessibility approval.
- Text, icons, controls, states, borders, charts, focus indicators, and content over gradients/media require measured contrast.
- Evaluate every animated frame/state that can reduce contrast, not only the resting state.
- Color and glow are never the sole state cue.
- Support high-contrast/forced-colors behavior where applicable.

## Keyboard Navigation

- Every interactive function is reachable and usable by keyboard without timing or pointer precision.
- Focus order follows the logical Persian RTL reading and task sequence.
- Focus remains visible, stable, unobscured, and distinct from decorative Border Glow.
- Menus, tabs/pills, disclosures, steppers, dialogs, forms, carousels/loops, and errors use correct semantics and keyboard behavior.
- No keyboard trap; overlays restore focus to the initiating control.

## RTL Readability

- Semantic source order and assistive-technology order remain logical.
- Directional animation, chevrons, progress, and spatial transitions respect meaning and RTL flow.
- Persian labels, Latin brands/grades, dimensions, units, phone/email, and punctuation remain readable in mixed-direction strings.
- Text alignment and truncation do not hide prefixes, units, validation, or distinguishing product values.
- Interfaces remain usable under text enlargement and longer Persian translations.

## Text Legibility

- Essential text remains real text, not embedded in motion, raster effects, or decorative SVG.
- Shiny/Gradient Text is limited to short display accents with a solid fallback.
- Body copy, specifications, form labels, errors, legal text, and navigation use stable high-legibility presentation.
- Do not animate line height, letter spacing, or widths in ways that cause reflow or loss of reading position.
- Exact typography families, sizes, weights, and line heights remain pending token approval.

## Button Clarity

- Buttons use explicit Persian action labels; icon-only controls require an approved accessible name and recognizable purpose.
- Primary inquiry actions are distinguishable from navigation and secondary actions.
- Loading, disabled, success, and error states remain textual/programmatic and do not shift the target.
- No pulsing urgency, false scarcity, hidden action, ambiguous price/checkout implication, or motion-only feedback.
- Touch and pointer targets require approved size/spacing criteria and representative-device validation.

## Animation Limits

- Follow the 85% clean / 10% purposeful motion / 5% controlled wow principle.
- Default to one expressive/ambient motion family per viewport.
- Avoid simultaneous motion near reading, input, or decision areas.
- Decorative loops are off by default on mobile and reduced motion.
- Content does not wait for animation and remains operable when enhancement fails.

## Component Accessibility Contract

Every future component records semantic role/structure, accessible name/description, keyboard behavior, focus management, state announcement, reading order, error handling, reduced-motion behavior, contrast results, text-resize behavior, touch behavior, language/direction, empty/failure states, and human-test evidence.

## Validation Rules

- Automated checks may identify defects but do not prove accessibility.
- Human keyboard, screen-reader, zoom/reflow, reduced-motion, high-contrast, touch, Persian RTL, mixed-script, and cognitive clarity reviews are required as applicable.
- Test representative content, long labels, missing optional data, errors, slow network, enhancement failure, and device constraints.
- Missing accessibility evidence blocks implementation/release.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial design accessibility and motion-safety rules. |

## Navigation

- [Design Manifest](DESIGN_MANIFEST.md)
- [Motion System](MOTION_SYSTEM.md)
- [Component Pattern Library](COMPONENT_PATTERN_LIBRARY.md)
- [Animation Library](ANIMATION_LIBRARY.md)
- [Performance Rules](PERFORMANCE_RULES.md)

