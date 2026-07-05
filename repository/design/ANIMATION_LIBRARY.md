# Damavand Animation Library

## Document Control

- **Document ID:** `repository/design/ANIMATION_LIBRARY.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Motion, Accessibility, Performance, Blocksy, Elementor, and QA Reviewers
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On animation purpose, behavior, duration, intensity, device, accessibility, or runtime-policy change
- **Lifecycle:** Review
- **Source of Truth:** [Motion System](MOTION_SYSTEM.md) after approval
- **Dependencies:** [Motion System](MOTION_SYSTEM.md), [ReactBits Inspiration Mapping](REACTBITS_INSPIRATION_MAPPING.md), [Performance Rules](PERFORMANCE_RULES.md), and [Accessibility Rules](ACCESSIBILITY_RULES.md)
- **Related Documents:** [Component Pattern Library](COMPONENT_PATTERN_LIBRARY.md) and [Design Decision Records](DESIGN_DECISION_RECORDS.md)
- **Traceability:** DDR-0001, DDR-0002, DDR-0004, Sprint 05A, and the 12 animation contracts below
- **AI Compatibility:** AI-readable animation guidance; no generated animation or runtime implementation is authorized
- **Approval:** Pending Founder and specialist review; all entries remain implementation-ineligible until their gates pass

## Purpose

Define bounded behavior for the required motion concepts without specifying production code, assets, selectors, Elementor artifacts, or WordPress configuration.

## Library Rules

- Duration guidance is a review range, not a production token.
- Intensity is `Low`, `Medium`, or `High`; High is not eligible for production without explicit exception review.
- Continuous motion is exceptional and must be pausable, nonessential, measured, and removed under reduced motion.
- Approved locations and forbidden areas come from [ReactBits Inspiration Mapping](REACTBITS_INSPIRATION_MAPPING.md).

## Animation Contracts

### Light Rays

- **Purpose:** Add restrained directional depth to a nonessential focal background.
- **Use cases:** Approved hero or trust accent.
- **Motion behavior:** Slow finite fade/drift or static artwork; no pointer tracking by default.
- **Duration guidance:** 400–600 ms finite reveal; ambient loop requires separate approval.
- **Intensity level:** Low–medium.
- **Mobile rule:** Static, simplified, or removed.
- **Performance rule:** Prefer optimized SVG/WebP; reject heavy blur, canvas, or WebGL without exceptional evidence.
- **Reduced-motion fallback:** Static approved background or no decoration.

### Border Glow

- **Purpose:** Reinforce focus, selection, or one premium focal component.
- **Use cases:** Primary inquiry CTA, selected card, or focus-visible state.
- **Motion behavior:** Short edge emphasis tied to a state; no permanent pulsing.
- **Duration guidance:** 120–240 ms state transition.
- **Intensity level:** Low.
- **Mobile rule:** Static focus/selected border; no hover-only effect.
- **Performance rule:** Constrain blur radius and animated area; avoid large repaint regions.
- **Reduced-motion fallback:** Solid high-contrast border.

### Shiny Text

- **Purpose:** Add one reflective accent to short nonessential display text.
- **Use cases:** Hero eyebrow or approved brand phrase.
- **Motion behavior:** One finite highlight pass; no perpetual sweep by default.
- **Duration guidance:** 400–600 ms after content is visible.
- **Intensity level:** Low–medium.
- **Mobile rule:** Static solid or gradient text.
- **Performance rule:** Small text area only; protect contrast and avoid filter stacks.
- **Reduced-motion fallback:** Static solid approved text color.

### Gradient Text

- **Purpose:** Create restrained premium emphasis without changing text meaning.
- **Use cases:** Short headline fragment.
- **Motion behavior:** Static by default; if approved, one subtle background-position transition.
- **Duration guidance:** 300–500 ms finite transition.
- **Intensity level:** Low.
- **Mobile rule:** Static gradient or solid fallback.
- **Performance rule:** No large animated text blocks; no gradient plus blur plus glow combination.
- **Reduced-motion fallback:** Static gradient or solid high-contrast color.

### Magic Bento

- **Purpose:** Coordinate emphasis across a modular feature/category grid.
- **Use cases:** Approved feature or product-family overview.
- **Motion behavior:** Individual card focus/hover depth and border response; no global pointer-tracking field.
- **Duration guidance:** 160–280 ms per state.
- **Intensity level:** Low–medium.
- **Mobile rule:** Static cards or simple press/focus feedback in linear/two-column layout.
- **Performance rule:** Limit simultaneous shadows, filters, observers, and animated cards.
- **Reduced-motion fallback:** Static grid with visible focus and selected states.

### Counter

- **Purpose:** Add finite visual emphasis to a verified metric.
- **Use cases:** Approved statistics/trust section.
- **Motion behavior:** Optional one-time progression to a final value already present semantically.
- **Duration guidance:** 300–600 ms; no repeated autoplay.
- **Intensity level:** Low.
- **Mobile rule:** Immediate final value or short one-time transition.
- **Performance rule:** One shared low-cost trigger; never delay content or instantiate per-frame libraries.
- **Reduced-motion fallback:** Final value shown immediately.

### Logo Loop

- **Purpose:** Present verified marks in a compact sequence when a static grid is insufficient.
- **Use cases:** Approved brand/partner/standards trust block.
- **Motion behavior:** Slow, linear, pausable track; no duplicated keyboard targets.
- **Duration guidance:** Persistent motion has no default approval; speed/duration require content-width and accessibility evidence.
- **Intensity level:** Low.
- **Mobile rule:** Static grid or manual scroll; autoplay disabled.
- **Performance rule:** Optimized correctly sized assets, lazy loading below the fold, and no uncontrolled duplication.
- **Reduced-motion fallback:** Static wrapping logo list.

### Stepper

- **Purpose:** Preserve orientation through an approved sequence.
- **Use cases:** Inquiry stages, selection guidance, project process, or approved multi-step interaction.
- **Motion behavior:** Current/completed state transition and optional short disclosure.
- **Duration guidance:** 120–240 ms.
- **Intensity level:** Low.
- **Mobile rule:** Vertical progression with explicit text state.
- **Performance rule:** No runtime library; number of steps and content remain bounded by the workflow.
- **Reduced-motion fallback:** Immediate state change.

### Star Border

- **Purpose:** Create rare focal emphasis on one approved component.
- **Use cases:** Primary inquiry CTA or featured trust card.
- **Motion behavior:** One finite border pass on entry/focus, or a low-frequency loop only by exception.
- **Duration guidance:** 300–600 ms finite pass.
- **Intensity level:** Medium.
- **Mobile rule:** Static border/glow.
- **Performance rule:** Avoid masks/filters across large surfaces and simultaneous instances.
- **Reduced-motion fallback:** Solid approved border.

### Laser Flow

- **Purpose:** Provide a rare expressive background suggesting flow without conveying facts.
- **Use cases:** Controlled prototype or one campaign/hero accent.
- **Motion behavior:** Finite beam/path traversal; no rapid or interactive pursuit.
- **Duration guidance:** 400–600 ms finite reveal; continuous flow is not approved by default.
- **Intensity level:** High.
- **Mobile rule:** Static artwork or removed.
- **Performance rule:** Prefer static/finite SVG concept; canvas/WebGL/large blur requires exception and measurements.
- **Reduced-motion fallback:** Static artwork or empty background.

### Strands

- **Purpose:** Add abstract depth and continuity to one nonessential background.
- **Use cases:** Controlled hero/brand prototype.
- **Motion behavior:** Slow finite line reveal or very low-intensity drift; no pointer response by default.
- **Duration guidance:** 400–600 ms finite reveal.
- **Intensity level:** High.
- **Mobile rule:** Static or removed.
- **Performance rule:** Strict line/layer count; prefer optimized static SVG/WebP; reject unmeasured canvas fields.
- **Reduced-motion fallback:** Static simplified illustration or no decoration.

### Magic Rings

- **Purpose:** Add a rare engineered-depth focal motif.
- **Use cases:** Controlled hero prototype.
- **Motion behavior:** Finite scale/opacity reveal; no continuous orbit by default.
- **Duration guidance:** 300–600 ms.
- **Intensity level:** High.
- **Mobile rule:** Static image or removed.
- **Performance rule:** No physics, canvas, WebGL, particle field, or large filter stack without explicit exception evidence.
- **Reduced-motion fallback:** Static single-ring motif or no decoration.

## Library Acceptance Rule

An entry remains guidance only until its exact component/location, content owner, runtime owner, supported implementation method, performance budget, representative-device measurements, reduced-motion behavior, Persian RTL behavior, keyboard/focus behavior, SEO impact, staging evidence, and rollback are approved.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial 12-entry animation guidance library. |

## Navigation

- [Motion System](MOTION_SYSTEM.md)
- [ReactBits Inspiration Mapping](REACTBITS_INSPIRATION_MAPPING.md)
- [Component Pattern Library](COMPONENT_PATTERN_LIBRARY.md)
- [Performance Rules](PERFORMANCE_RULES.md)
- [Accessibility Rules](ACCESSIBILITY_RULES.md)

