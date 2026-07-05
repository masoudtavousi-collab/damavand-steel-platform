# Design Performance Rules

## Document Control

- **Document ID:** `repository/design/PERFORMANCE_RULES.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Performance, WordPress, Blocksy, Elementor, Accessibility, SEO, and QA Reviewers
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On performance budget, Core Web Vitals, asset, motion, platform, browser, device, or dependency change
- **Lifecycle:** Review
- **Source of Truth:** [Design Manifest](DESIGN_MANIFEST.md), [Motion System](MOTION_SYSTEM.md), and approved performance governance
- **Dependencies:** [Motion System](MOTION_SYSTEM.md), [Animation Library](ANIMATION_LIBRARY.md), and [Enterprise Performance Checklist](../../quality/PERFORMANCE_CHECKLIST.md)
- **Related Documents:** [Accessibility Rules](ACCESSIBILITY_RULES.md), [Blocksy Blueprint](../../docs/36_BLOCKSY_CONFIGURATION.md), and [Elementor Blueprint](../../docs/37_ELEMENTOR_ARCHITECTURE.md)
- **Traceability:** CP-001–CP-004, CP-007, CP-009, CP-010, DDR-0001, DDR-0004, and Sprint 05A
- **AI Compatibility:** AI-readable performance guidance; no runtime optimization or generated asset is authorized
- **Approval:** Pending Founder and performance/platform review; no implementation or budget exception is authorized

## Purpose

Protect WordPress performance and Core Web Vitals while allowing a restrained, premium design language.

## Mandatory Rules

### No Heavy JavaScript

- A visual effect must not require a large client-side runtime merely to decorate content.
- Content, navigation, inquiry, and critical states work before optional enhancement.
- Per-element listeners, high-frequency scroll/pointer handlers, and perpetual animation loops require explicit rejection-by-default review.

### No React Runtime

- React is not added for the public design system.
- ReactBits remains inspiration only; no package, component source, bundle, transitive dependency, or build pipeline is introduced.
- Existing WordPress internals do not create permission to ship a new frontend React experience.

### No Unnecessary Animation Libraries

- Use the smallest supported native platform capability that meets an approved need.
- A new animation library fails review unless supported WordPress/Blocksy/Elementor/CSS/SVG approaches cannot meet the need and an exception passes dependency, security, accessibility, performance, maintenance, replacement, and rollback review.

### Prefer CSS

- Future state transitions should prefer low-cost supported CSS concepts where possible.
- Favor opacity/transform-style changes over layout-affecting properties, while still testing actual paint/composite behavior.
- CSS preference does not authorize custom production CSS in this sprint or bypass Blocksy/Elementor ownership.

### Prefer SVG and WebP

- Use appropriately optimized, correctly dimensioned assets with intrinsic dimensions.
- SVG is suitable for simple controlled vectors; WebP may be suitable for raster imagery where compatibility and quality pass.
- Avoid embedding scripts, untrusted markup, oversized filters, invisible layers, or duplicated assets.
- Media format choice follows the approved Media Strategy and measured evidence.

### Lazy Motion

- Below-fold decorative motion does not initialize before it can be meaningfully viewed.
- Do not lazy-load critical text, primary inquiry actions, or layout dimensions.
- Motion observers/listeners are bounded and removed when no longer needed.

### Mobile Complexity Reduction

- Complex ambient/expressive motion is static, simplified, or disabled on constrained mobile conditions.
- Do not use hover-only behavior, cursor tracking, canvas fields, or persistent background animation as a mobile requirement.
- Device policy is based on measurement and user preference, not only viewport width.

### Core Web Vitals Protection

- Motion must not move already-rendered layout or delay primary content.
- Hero decoration must not become the LCP dependency unless explicitly approved and optimized.
- Interactions must remain responsive under representative mobile hardware and network conditions.
- No design enhancement may trade away stable layout, fast input response, or readable primary content.

## Design Performance Budget Contract

Exact numeric budgets remain `TBD (Performance/Founder Approval Required)`. A future component/effect proposal must record:

- Baseline and candidate LCP, INP, CLS, TTFB, transferred bytes, request count, CPU time, long tasks, memory, and frame behavior where applicable.
- Representative Persian RTL content, device, browser, network, logged-in/logged-out, cache, and reduced-motion conditions.
- Asset sizes and formats, font impact, third-party requests, Elementor/Blocksy asset impact, and failure behavior.
- Budget owner, threshold, evidence, exception decision, rollback, and monitoring.

## Effect Risk Tiers

| Tier | Typical concepts | Default posture |
| --- | --- | --- |
| Low | State transition, Pill Nav, Stepper, finite Counter | Eligible for measured review |
| Medium | Border Glow, Shiny/Gradient Text, Magic Bento, Logo Loop, Light Rays | Limited use with strict budget |
| High | Magic Rings, Laser Flow, Strands, Lanyard/physics, canvas/WebGL fields | Experimental; static fallback preferred |

## Prohibited Performance Shortcuts

- No LiteSpeed Cache assumption or dependency.
- No cache layer used to conceal excessive frontend cost.
- No broad optimization toggle without baseline, ownership, exclusions, and rollback.
- No duplicate Blocksy/Elementor assets or multiple libraries for the same capability.
- No autoplay background video or high-cost visual effect by default.
- No production experiment before infrastructure, staging, recovery, and applicable Sprint 04C gates pass.

## Future Validation Gate

Pass requires reproducible baseline/candidate measurements meeting approved budgets with no regression to mobile RTL, accessibility, inquiry, SEO, security, or maintainability. Missing representative evidence is a failure, not an approval.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial design-performance and dependency safety rules. |

## Navigation

- [Design Manifest](DESIGN_MANIFEST.md)
- [Motion System](MOTION_SYSTEM.md)
- [Animation Library](ANIMATION_LIBRARY.md)
- [Accessibility Rules](ACCESSIBILITY_RULES.md)

