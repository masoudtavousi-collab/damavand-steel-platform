# ReactBits Inspiration Mapping

## Document Control

- **Document ID:** `repository/design/REACTBITS_INSPIRATION_MAPPING.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Design, Accessibility, Performance, Blocksy, Elementor, SEO, and Security Reviewers
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On inspiration pattern, use case, platform capability, performance, accessibility, or dependency change
- **Lifecycle:** Review
- **Source of Truth:** [Design Manifest](DESIGN_MANIFEST.md), [Motion System](MOTION_SYSTEM.md), and explicit Sprint 05A inspiration decision
- **Dependencies:** [Motion System](MOTION_SYSTEM.md), [Performance Rules](PERFORMANCE_RULES.md), [Accessibility Rules](ACCESSIBILITY_RULES.md), [Blocksy Blueprint](../../docs/36_BLOCKSY_CONFIGURATION.md), and [Elementor Blueprint](../../docs/37_ELEMENTOR_ARCHITECTURE.md)
- **Related Documents:** [Component Pattern Library](COMPONENT_PATTERN_LIBRARY.md), [Animation Library](ANIMATION_LIBRARY.md), and [Design Decision Records](DESIGN_DECISION_RECORDS.md)
- **Traceability:** DDR-0001, DDR-0002, DDR-0004, BLOCKSY-001–BLOCKSY-009, ELEMENTOR-001–ELEMENTOR-009, and Sprint 05A
- **AI Compatibility:** AI-readable inspiration mapping; no ReactBits code, asset, package, or runtime is authorized
- **Approval:** Pattern decisions are design-review classifications only; implementation remains unauthorized

## Purpose

Translate approved ReactBits-inspired concepts into Damavand use cases and safety boundaries without importing React, ReactBits, source implementations, or runtime dependencies.

## Interpretation Rule

“WordPress-native implementation approach” describes a future evaluation route through supported Blocksy, Elementor, WordPress, CSS, or SVG capabilities. It is not code, configuration, a dependency choice, or implementation approval. Each future use still requires accessibility, performance, licensing/provenance, mobile/RTL, ownership, staging, and rollback evidence.

## Pattern Mappings

### Magic Bento

- **Pattern name:** Magic Bento
- **Original inspiration:** A modular card grid with coordinated hover/focus emphasis and layered depth.
- **Damavand use case:** Product-family, capability, service, or trust-feature overview where cards have equal semantic weight.
- **Approved areas:** Delegated landing-page body sections and approved category-introduction regions.
- **Forbidden areas:** Product specification tables, inquiry forms, checkout-like flows, global navigation, and dense mobile grids.
- **WordPress-native implementation approach:** Future semantic card/grid markup with supported layout controls and restrained state styling; no pointer-tracking engine.
- **Elementor compatibility:** Compatible within an approved reusable body-section pattern using the shared token system.
- **Blocksy compatibility:** Must inherit Blocksy containers/tokens and cannot replace archives, product cards, or the global shell.
- **Performance risk:** Medium; multiple shadows, filters, pointer listeners, or per-card animation can multiply rendering cost.
- **Mobile behavior:** Linear or two-column static cards; no cursor-dependent highlight; reduce simultaneous effects.
- **Accessibility notes:** DOM order follows reading order; focus and hover parity; card links have explicit names.
- **Final decision:** Limited.

### Shiny Text

- **Pattern name:** Shiny Text
- **Original inspiration:** A moving highlight passes across text to create a reflective emphasis.
- **Damavand use case:** Short nonessential premium accent in a hero eyebrow or one primary campaign label.
- **Approved areas:** One short decorative phrase in an approved hero or trust section.
- **Forbidden areas:** Body copy, product facts, form labels, errors, navigation, prices, certifications, and continuous page-wide use.
- **WordPress-native implementation approach:** Future restrained CSS-based highlight with a static text fallback.
- **Elementor compatibility:** Limited to an approved text style in delegated body content; no custom runtime widget dependency.
- **Blocksy compatibility:** Not for global navigation or essential shell text; may consume approved color tokens.
- **Performance risk:** Low–medium; animated gradients can repaint and reduce contrast.
- **Mobile behavior:** Static or slower single-pass treatment; default off on constrained devices.
- **Accessibility notes:** Text remains real, selectable, high-contrast, and understandable with motion/gradient removed.
- **Final decision:** Limited.

### Gradient Text

- **Pattern name:** Gradient Text
- **Original inspiration:** Text filled with a controlled color gradient, optionally animated.
- **Damavand use case:** One concise brand or section emphasis that reinforces hierarchy.
- **Approved areas:** Hero headline fragment or selected display heading after contrast review.
- **Forbidden areas:** Long text, product data, links whose state depends on color, controls, errors, and legal content.
- **WordPress-native implementation approach:** Future static token-based gradient; animation is a separate Limited motion decision.
- **Elementor compatibility:** Compatible as an approved global text variant, not a page-local color system.
- **Blocksy compatibility:** Must use the coordinated Blocksy token source and preserve base heading behavior.
- **Performance risk:** Low for static use; medium when animated or combined with filters.
- **Mobile behavior:** Prefer static gradient or solid-color fallback for small/low-contrast text.
- **Accessibility notes:** Verify contrast across every glyph position and preserve a legible solid fallback.
- **Final decision:** Limited.

### Rotating Text

- **Pattern name:** Rotating Text
- **Original inspiration:** A short sequence of words replaces or rotates within a stable phrase.
- **Damavand use case:** Optional hero descriptor sequence for approved product/service concepts.
- **Approved areas:** One nonessential descriptor slot where the static surrounding statement is complete.
- **Forbidden areas:** SEO-critical headline meaning, product specifications, navigation, CTAs, forms, alerts, and any claim sequence not content-approved.
- **WordPress-native implementation approach:** Future finite, accessible text-state sequence with all content available in source semantics; no React component.
- **Elementor compatibility:** Experimental in a delegated hero body only after widget/dependency and semantic review.
- **Blocksy compatibility:** Not allowed in the global shell by default.
- **Performance risk:** Medium due to timers, layout shifts, and potential script dependency.
- **Mobile behavior:** Static first approved phrase by default; no width-shifting loop.
- **Accessibility notes:** Pause control for persistent sequences; no repeated live-region announcements; reduced motion shows one stable phrase.
- **Final decision:** Experimental.

### Logo Loop

- **Pattern name:** Logo Loop
- **Original inspiration:** A continuous or stepped row of partner/customer/brand marks.
- **Damavand use case:** Verified brands, standards bodies, or approved partner relationships.
- **Approved areas:** Trust section only after every logo, relationship, license, link, and lifecycle is verified.
- **Forbidden areas:** Fabricated social proof, unlicensed marks, product claims, header clutter, and content without pause/control.
- **WordPress-native implementation approach:** Prefer a static responsive logo list; a future finite/pausable CSS track may be evaluated.
- **Elementor compatibility:** Compatible as a reusable content block backed by governed media/content data.
- **Blocksy compatibility:** May appear within body/footer content but cannot displace required footer/navigation information.
- **Performance risk:** Medium from duplicate images, continuous compositing, and oversized media.
- **Mobile behavior:** Static grid or manually scrollable list; autoplay off by default.
- **Accessibility notes:** Meaningful alt text or intentionally empty alt for redundant marks; pause control; no duplicate focus targets.
- **Final decision:** Limited.

### Magic Rings

- **Pattern name:** Magic Rings
- **Original inspiration:** Layered luminous rings create an ambient focal field.
- **Damavand use case:** Rare abstract hero background suggesting precision and engineered depth.
- **Approved areas:** A single non-content-bearing hero accent after performance evidence.
- **Forbidden areas:** Forms, product images/specifications, navigation, footer, multiple sections, or any representation of actual product finish.
- **WordPress-native implementation approach:** Prefer one optimized static SVG/WebP; any motion requires a lightweight supported future method.
- **Elementor compatibility:** Experimental as a decorative background in a delegated hero region.
- **Blocksy compatibility:** Must remain inside the content region and never alter shell behavior.
- **Performance risk:** High when animated with canvas/WebGL, blur, particles, or large composited layers.
- **Mobile behavior:** Static image or removed.
- **Accessibility notes:** Decorative only, ignored by assistive technology, no flashing or foreground contrast loss.
- **Final decision:** Experimental.

### Laser Flow

- **Pattern name:** Laser Flow
- **Original inspiration:** Directional beams or luminous paths animate through a scene.
- **Damavand use case:** Rare campaign/hero accent for flow, fabrication, or supply-process storytelling without technical claim.
- **Approved areas:** Controlled prototype or nonessential hero background after evidence.
- **Forbidden areas:** Product facts, inquiry forms, navigation, cards, persistent page background, and safety-sensitive content.
- **WordPress-native implementation approach:** Prefer static artwork or a short, finite SVG/CSS concept; no canvas/WebGL dependency by default.
- **Elementor compatibility:** Experimental decorative layer in one delegated section only.
- **Blocksy compatibility:** Cannot enter header/footer/navigation or global backgrounds.
- **Performance risk:** High from blur, blend modes, particles, and continuous animation.
- **Mobile behavior:** Removed or static low-cost fallback.
- **Accessibility notes:** No flashing, rapid traversal, or focus interference; reduced motion always static.
- **Final decision:** Experimental.

### Strands

- **Pattern name:** Strands
- **Original inspiration:** Fine animated lines or threads produce depth and directional movement.
- **Damavand use case:** Abstract brand atmosphere for precision, continuity, or engineered networks.
- **Approved areas:** Prototype or one low-intensity nonessential background.
- **Forbidden areas:** Behind dense Persian text, product media, forms, navigation, multiple sections, or technical diagrams.
- **WordPress-native implementation approach:** Prefer optimized static SVG/WebP; motion only if a future lightweight supported route passes measurement.
- **Elementor compatibility:** Experimental decorative background with strict containment.
- **Blocksy compatibility:** Not permitted in the shell or archive/product defaults.
- **Performance risk:** High when line count, canvas, or pointer response grows.
- **Mobile behavior:** Static or removed.
- **Accessibility notes:** Decorative and noninteractive; protect text contrast; disable for reduced motion.
- **Final decision:** Experimental.

### Star Border

- **Pattern name:** Star Border
- **Original inspiration:** A moving highlight or particle-like accent travels along a component border.
- **Damavand use case:** Rare emphasis for a primary inquiry CTA or featured trust card.
- **Approved areas:** One approved focal component per viewport.
- **Forbidden areas:** Every button/card, form controls, errors, pricing-like cards, navigation lists, and continuous high-speed loops.
- **WordPress-native implementation approach:** Future pseudo-element/border treatment with a static border fallback; no plugin dependency.
- **Elementor compatibility:** Limited reusable style for a delegated CTA/card.
- **Blocksy compatibility:** May use shared tokens; global header usage requires separate shell approval.
- **Performance risk:** Medium from continuous gradients, masks, or pseudo-element compositing.
- **Mobile behavior:** Static border glow or standard border.
- **Accessibility notes:** Border is not the only CTA/state cue; focus indicator remains distinct.
- **Final decision:** Limited.

### Pill Nav

- **Pattern name:** Pill Nav
- **Original inspiration:** A rounded active indicator moves between compact navigation items.
- **Damavand use case:** Approved primary/secondary navigation state, category tabs, or compact in-page section navigation.
- **Approved areas:** Blocksy-owned navigation or accessible tab/section controls after information-architecture approval.
- **Forbidden areas:** Deep taxonomies that need wrapping, hidden overflow, unlabeled icons, or fake tab controls implemented as links without semantics.
- **WordPress-native implementation approach:** Supported WordPress/Blocksy menu or semantic control with a restrained state indicator.
- **Elementor compatibility:** Compatible for delegated in-page navigation, not the global shell.
- **Blocksy compatibility:** Preferred owner for global navigation; consumes approved tokens and responsive behavior.
- **Performance risk:** Low when the indicator uses simple state transitions.
- **Mobile behavior:** Wrap, scroll with visible affordance, or transform into an approved disclosure; never clip essential items.
- **Accessibility notes:** Current state is programmatically exposed; full keyboard/focus behavior; RTL movement follows logical order.
- **Final decision:** Approved.

### Lanyard

- **Pattern name:** Lanyard
- **Original inspiration:** A suspended card/object responds with physical or pointer-driven movement.
- **Damavand use case:** Optional event badge, representative card, or campaign artifact in a controlled prototype.
- **Approved areas:** Experimental nonessential storytelling region only.
- **Forbidden areas:** Product cards, staff identity without approval, forms, navigation, mobile-critical paths, and any drag interaction required for access.
- **WordPress-native implementation approach:** Prefer a static card illustration; no physics engine or React runtime.
- **Elementor compatibility:** Experimental only as static media or a separately approved lightweight treatment.
- **Blocksy compatibility:** No role in shell/navigation or product/archive defaults.
- **Performance risk:** High due to physics, pointer tracking, canvas/WebGL, and motion sensitivity.
- **Mobile behavior:** Static card; no drag/tilt.
- **Accessibility notes:** Content exists outside the effect; keyboard/touch do not need to manipulate the object; reduced motion is static.
- **Final decision:** Experimental.

### Border Glow

- **Pattern name:** Border Glow
- **Original inspiration:** A subtle luminous edge responds to focus, hover, or emphasis.
- **Damavand use case:** Clarify interactive focus or create restrained premium depth on one selected component.
- **Approved areas:** CTA, selected product/category card, focus state, or trust panel where contrast is preserved.
- **Forbidden areas:** All components simultaneously, error-only indication, product-finish simulation, and persistent high-intensity animation.
- **WordPress-native implementation approach:** Future token-based border/shadow state through supported styling; static fallback.
- **Elementor compatibility:** Compatible as a shared component state, not ad hoc widget styling.
- **Blocksy compatibility:** Compatible with coordinated tokens and shell focus conventions.
- **Performance risk:** Low–medium; large blur radii and animation increase paint cost.
- **Mobile behavior:** Static selected/focus state; hover animation omitted.
- **Accessibility notes:** Maintain visible high-contrast focus independent of glow and respect forced-colors behavior.
- **Final decision:** Limited.

### Counter

- **Pattern name:** Counter
- **Original inspiration:** A numeric value animates from a starting point to a verified final value.
- **Damavand use case:** Verified operational, catalog, project, experience, or service metric with owner and review date.
- **Approved areas:** Trust/statistics section backed by approved content data.
- **Forbidden areas:** Fabricated metrics, live stock, public price, unsupported claims, essential values hidden until scroll, or repeated animation.
- **WordPress-native implementation approach:** Render the final semantic value immediately; optional one-time visual enhancement through a future supported method.
- **Elementor compatibility:** Compatible as a governed reusable statistic component.
- **Blocksy compatibility:** May be used in body/footer regions while inheriting typography/tokens.
- **Performance risk:** Low when finite and dependency-free; medium if one script observes many counters.
- **Mobile behavior:** Immediate final value or short one-time transition; no delayed visibility.
- **Accessibility notes:** Assistive technology receives the final value once; no rapid live announcements; units and context are explicit.
- **Final decision:** Approved.

### Stepper

- **Pattern name:** Stepper
- **Original inspiration:** A sequence communicates stages and current progress.
- **Damavand use case:** Inquiry lifecycle explanation, product-selection guidance, project process, or multi-step form progress after workflow approval.
- **Approved areas:** Informational process sections and approved multi-step interactions.
- **Forbidden areas:** Invented sales statuses, hidden requirements, non-linear processes forced into linear display, and progress that implies guaranteed fulfillment.
- **WordPress-native implementation approach:** Semantic ordered steps with supported disclosure/progress states and no framework dependency.
- **Elementor compatibility:** Compatible for informational body content and approved form presentation.
- **Blocksy compatibility:** May inherit global tokens; global shell ownership is unaffected.
- **Performance risk:** Low.
- **Mobile behavior:** Vertical RTL-aware sequence with current/completed labels; no horizontal overflow.
- **Accessibility notes:** Ordered semantics, explicit current step, textual status, keyboard support, and no motion-only progression.
- **Final decision:** Approved.

### Light Rays

- **Pattern name:** Light Rays
- **Original inspiration:** Soft directional rays create depth and draw attention to a focal area.
- **Damavand use case:** Restrained hero or trust-section atmosphere suggesting precision and premium finish.
- **Approved areas:** One nonessential background accent with protected foreground contrast.
- **Forbidden areas:** Product photography, forms, technical tables, navigation, all-page backgrounds, and any claim about physical finish.
- **WordPress-native implementation approach:** Prefer optimized static SVG/WebP or a low-cost CSS concept after measurement.
- **Elementor compatibility:** Limited decorative background in a delegated body section.
- **Blocksy compatibility:** Not for shell/navigation by default; must inherit approved tokens and containers.
- **Performance risk:** Medium–high when animated with filters, blend modes, canvas, or pointer response.
- **Mobile behavior:** Static, simplified, or removed.
- **Accessibility notes:** Decorative only, ignored by assistive technology, no flicker, no contrast reduction, and reduced-motion static.
- **Final decision:** Limited.

## Decision Summary

| Decision | Patterns |
| --- | --- |
| Approved | Pill Nav, Counter, Stepper |
| Limited | Magic Bento, Shiny Text, Gradient Text, Logo Loop, Star Border, Border Glow, Light Rays |
| Experimental | Rotating Text, Magic Rings, Laser Flow, Strands, Lanyard |

“Approved” means suitable for future design consideration within all governing gates. It does not authorize implementation.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial mapping of all 15 approved inspiration patterns. |

## Navigation

- [Design Manifest](DESIGN_MANIFEST.md)
- [Motion System](MOTION_SYSTEM.md)
- [Component Pattern Library](COMPONENT_PATTERN_LIBRARY.md)
- [Animation Library](ANIMATION_LIBRARY.md)
- [Performance Rules](PERFORMANCE_RULES.md)
- [Accessibility Rules](ACCESSIBILITY_RULES.md)
