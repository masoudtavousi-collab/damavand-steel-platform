# PP-01 Public Homepage V1 Specification v1.0

## Document Control

- **Mission:** `PP-01 — PUBLIC HOMEPAGE V1 READINESS`
- **Status:** `REVIEW / IMPLEMENTATION-READY PACKAGE`
- **Artifact classification:** `NOT_DEPLOYED / NOT_PUBLISHED / IMPLEMENTATION_CANDIDATE`
- **Authority:** [PP-01 Scope](PP_01_PUBLIC_HOMEPAGE_V1_READINESS_SCOPE_V1.0.md)
- **Audience:** Founder, Project Commander, design reviewer, and a future authorized PP-02 operator
- **Runtime authority:** `NONE`
- **Formal launch authority:** `NONE`

## Experience Contract

The homepage must feel industrial, premium, calm, precise, credible, uncluttered, product-first, Persian-native, and mobile-first. It must give a visitor a short path to understand the business, enter the primary product family, and request price/availability information or purchasing consultation without implying ecommerce or live inventory.

The effective controls remain:

- **Inquiry First**: the public conversion path is an inquiry, not a purchase transaction.
- **No Public Pricing**: no price, price range, discount, promotion, cart, checkout, or payment UI.
- **Product Data First**: only governed evidence may become Product or combination truth.
- **Fail Closed**: missing content, data, media rights, configuration, or backend capability stays hidden or visibly unavailable; it is never simulated.
- **Persian RTL and Mobile First**: source order, reading order, focus order, and interaction must be correct before larger breakpoints.
- **Public Preview First + Progressive Enablement**: a future preview may expose only verified surfaces. `PUBLIC PREVIEW ≠ FORMAL PUBLIC LAUNCH`.

## Frozen Information Architecture

The homepage section order is fixed:

**Header → Hero → Primary Product Entry → Capability Overview → Why Damavand Steel → Inquiry CTA → Contact Surface → Footer**

No carousel, blog feed, public catalog grid, fake stock panel, pricing table, trust-counter strip, marketplace UI, or checkout surface is part of V1.

## Content Matrix

| Surface | Purpose | Approved or candidate content | Status and evidence rule | Explicitly prohibited |
| --- | --- | --- | --- | --- |
| Header | Identify the brand, expose concise navigation, and keep inquiry reachable. | Brand mark/wordmark slot; `خانه`, `محصولات`, `درباره ما`, `تماس`; inquiry action. Final destination URLs remain PP-02 preflight items. | Navigation labels are `POLICY_BACKED_DRAFT`; logo asset is `MISSING_CONTENT / FOUNDER_VISUAL_REVIEW`. Hide any item without a verified destination. | Invented taxonomy, dead links, ecommerce account/cart, social links without evidence. |
| Hero | Explain the offer immediately and provide two governed next actions. | H1: **تأمین تخصصی لوله استیل، آلومینیوم و محصولات دکوراتیو**. Supporting copy: **دماوند استیل مجموعه‌ای از لوله‌های استیل، آلومینیوم و محصولات دکوراتیو را در رنگ‌ها، سایزها و مشخصات مختلف عرضه می‌کند. برای دریافت قیمت، بررسی موجودی یا انتخاب محصول مناسب، درخواست خود را ثبت کنید.** Primary CTA: **استعلام قیمت و موجودی**. Secondary CTA: **مشاوره خرید**. | Text and CTA labels are `MISSION_FROZEN`. Destinations must remain disabled/hidden until verified in PP-02. Hero media is optional and rights-gated. | Price amount, stock promise, delivery claim, unsupported superlative, autoplay media, text baked into imagery. |
| Primary Product Entry | Give the first clear product-family entry without fabricating variants. | Primary launch family: **لوله استیل دکوراتیو**. A future guided inquiry may ask for color, size, thickness, brand, length, and quantity. | Family label and axes are `MISSION_FROZEN AS INTERACTION INTENT`; they are not canonical Product values, available combinations, or inventory. The initial preview may show one family card or text link only. | Cartesian combinations, SKU claims, availability badges, specification tables sourced from assumption, price, Add to Cart. |
| Capability Overview | Describe supported business areas at a high level. | Three restrained areas: لوله استیل، آلومینیوم، محصولات دکوراتیو. Use one short neutral sentence per area only after Founder content review. | Category names are mission-supplied context; all explanatory copy is `REVIEW_REQUIRED`. Unverified cards stay absent. | Detailed technical specifications, brand representation, inventory breadth, capacity, certification, delivery territory, or ranking claims. |
| Why Damavand Steel | Explain the governed buying experience without unsupported marketing. | Candidate themes: انتخاب بر اساس مشخصات موردنیاز؛ استعلام پیش از اعلام قیمت و موجودی؛ مسیر مستقیم برای مشاوره خرید. | `POLICY_BACKED_DRAFT / REVIEW_REQUIRED`. These describe process intent, not business performance. | «بزرگ‌ترین»، «ارزان‌ترین»، «بهترین»، «شماره یک»، «نمایندگی رسمی»، «تضمینی»، «سریع‌ترین»، invented counters, certifications, testimonials, or awards. |
| Inquiry CTA | Provide the main non-commerce conversion point. | Price and availability inquiry, purchase consultation, telephone, and WhatsApp. Use the two frozen CTA labels consistently. | UI is an `IMPLEMENTATION_CANDIDATE`; no governed lead backend is implemented by PP-01. PP-02 must verify every action and fail closed if unavailable. | Fake form submission, success message without persistence, response-time promise, checkout, payment, public stock. |
| Contact Surface | Present only verified contact facts. | Phone: `09128506858`. WhatsApp: `09128506858`. Email reference: `sales@damavandsteel.com`. | Phone and WhatsApp are `APPROVED_CONTACT_FACT`. Email is `PLANNED / DEFERRED / NOT PROVEN OPERATIONAL` and must not be presented as a working public channel until verified. | Address, map, business hours, licenses, certifications, social accounts, leadership, delivery coverage, or additional contact identities without evidence. |
| Footer | Close navigation and repeat only proven contact information. | Brand slot, concise navigation, phone/WhatsApp when verified, future policy/legal slots, and a plain copyright structure. | `POLICY_BACKED_DRAFT`. Empty policy/legal slots remain hidden. Copyright year mechanism is verified in PP-02. | Fake policy links, unsupported address/social details, ecommerce links, badges, or claims. |

## Copy and Claim Rules

### Approved Public Copy

Only the frozen hero content, frozen CTA labels, primary family label, and verified contact facts may be treated as approved within this package. All other Persian copy is either a section label, a policy-backed candidate, or a review item.

### Prohibited Claims

The future implementation must reject or remove:

- largest, cheapest, best, fastest, number-one, official-representative, guaranteed, certified, nationwide-stock, always-available, same-day, exact lead-time, or exact response-time claims without governed evidence;
- price amounts, discounts, price ranges, public inventory, availability badges, and delivery promises;
- invented address, licenses, certifications, customer counts, project counts, partners, testimonials, social accounts, leadership, or service territory;
- inferred Product attributes, valid combinations, brand coverage, dimensions, material grade, finish, use suitability, SKU, or supplier truth; and
- any interaction that appears operational when its destination, backend, consent, persistence, notification, monitoring, or recovery path is not verified.

## Design System

This is a reusable candidate system, not final brand approval. Items marked `FOUNDER_VISUAL_REVIEW` may be implemented in an isolated staging preview only after the Founder checkpoint; they must not be silently treated as permanent brand decisions.

### Visual Tokens

| Token group | Implementation-ready rule | Approval state |
| --- | --- | --- |
| Color | Use semantic roles: `surface`, `surface-muted`, `text`, `text-muted`, `border`, `brand-primary`, `brand-on-primary`, `focus`, `success/error` only where truthful. Meet accessible contrast and avoid decorative gradients. | Exact palette/hex values: `FOUNDER_VISUAL_REVIEW`. |
| Typography | Use one Persian-capable primary family with reliable digits and punctuation; no display font dependency. Roles: H1, H2, H3, body, small/meta, button. Use real text. | Exact family and weights: `FOUNDER_VISUAL_REVIEW`; font licensing and local delivery must be verified. |
| Spacing | Base candidate scale: 4, 8, 12, 16, 24, 32, 48, 64, and 96 CSS pixels. Prefer section rhythm over extra containers. | Candidate, adjustable in Founder visual review without changing IA. |
| Radius/shadow | One restrained button radius and one restrained surface radius; use borders before shadows and no glassmorphism. | Exact values: `FOUNDER_VISUAL_REVIEW`. |
| Iconography | One small, coherent, stroke-consistent SVG set; labels must not rely on icons alone. | Final set: `FOUNDER_VISUAL_REVIEW / RIGHTS_REVIEW`. |
| Imagery | Industrial/product-focused, factual, rights-cleared, color-accurate, and free of embedded claims or text. A clean no-image layout is the fail-closed fallback. | Selection/crop/color treatment: `FOUNDER_VISUAL_REVIEW / RIGHTS_REQUIRED`. |

### Typography Hierarchy

- H1: one instance, compact line length, candidate responsive range `2rem–3.5rem`, weight chosen only after font review.
- H2: section headings, candidate responsive range `1.5rem–2.25rem`.
- H3: entry/capability headings, candidate responsive range `1.125rem–1.5rem`.
- Body: candidate `1rem–1.125rem`, generous Persian line height (`1.7–1.9`), maximum readable measure about 44 Persian characters where practical.
- Small/meta: never below `0.875rem`; do not use muted color below contrast requirements.
- Buttons: same type family as body, medium emphasis, never all-caps Latin styling.

All numeric values are layout candidates, not approved brand tokens.

### Containers and Section Rhythm

- Page content container candidate: maximum `1200px`.
- Reading container candidate: maximum `720px`.
- Inline gutters: `20px` at 360px, `24px` at 390/430px, `32px` on tablet, and `40px` on desktop.
- Vertical section padding: candidate `64px` mobile and `96px` desktop; reduce where content is short.
- Keep hero content visible without requiring a tall decorative viewport. Avoid full-screen hero locking.
- Use whitespace, rules, and typography before cards. Capability items may become a simple grid only when the content earns it.

### Buttons and Links

- Primary CTA is visually dominant once per viewport region; secondary CTA uses lower emphasis.
- Minimum interactive target is `44 × 44px`; preferred button height is at least `48px`.
- Include visible hover, focus-visible, active, and disabled states. Disabled behavior must be explicit and must not imitate success.
- Link purpose must be clear outside visual context. External behaviors such as telephone and WhatsApp require PP-02 device testing.
- Do not use animation as the only state cue.

### Imagery Rules

- Use explicit width, height, or aspect ratio to prevent layout shift.
- Keep primary message as HTML text; do not place essential copy over detailed imagery.
- Provide meaningful Persian alternative text only for informative images. Decorative images use empty alternative text.
- Avoid stock imagery that implies facilities, inventory, staff, certifications, or operations not evidenced as Damavand Steel.
- No slider, autoplay video, parallax, or decorative third-party media script.

### Motion

The page should be approximately 85% static, 10% functional micro-interaction, and at most 5% restrained accent. At most one subtle hero accent may be proposed. Honor reduced-motion preferences; content and state must remain complete with motion disabled.

## Blocksy and Elementor Ownership

| Surface or concern | Owner | Boundary |
| --- | --- | --- |
| Header, footer, navigation shell | Blocksy | Global shell only; no Elementor duplicate header/footer. |
| Global container, typography, color, focus, and spacing tokens | Blocksy | Values are consumed by Elementor; exact visual values require Founder review. |
| Site-wide layout and responsive shell | Blocksy | Must preserve RTL, keyboard navigation, and global consistency. |
| Homepage body and section composition | Elementor | Hero through Contact Surface only. |
| Homepage presentation and responsive section controls | Elementor | Must consume global tokens and avoid per-widget drift. |
| Product/archive/single-product templates | Blocksy by default / separately governed | Not changed or designed by PP-01. |
| Inquiry backend, forms, consent, persistence, notifications | Unassigned pending separate authority | Elementor must not fabricate backend success. |
| SEO/indexing/schema/runtime settings | Separately governed | PP-01 records future intent only. |

## Elementor Build Map

Use containers rather than legacy sections/columns. Keep the DOM shallow and assign stable semantic CSS classes only where needed.

```text
main.pp01-home
├── section.pp01-hero
│   └── container.pp01-container.pp01-hero__content
│       ├── heading (H1, frozen copy)
│       ├── text (frozen supporting copy)
│       └── container.pp01-actions
│           ├── primary CTA
│           └── secondary CTA
├── section.pp01-primary-entry
│   └── container.pp01-container
│       ├── heading (H2)
│       ├── product-family entry
│       └── optional rights-cleared media
├── section.pp01-capabilities
│   └── container.pp01-container
│       ├── heading (H2)
│       └── simple list/grid of verified capability items
├── section.pp01-why
│   └── container.pp01-container.pp01-reading
│       ├── heading (H2)
│       └── governed process themes
├── section.pp01-inquiry
│   └── container.pp01-container.pp01-reading
│       ├── heading (H2)
│       ├── concise prompt
│       └── verified inquiry actions
└── section.pp01-contact
    └── container.pp01-container.pp01-reading
        ├── heading (H2)
        └── verified phone/WhatsApp facts
```

Rules:

- The Header and Footer are outside this Elementor tree and remain Blocksy-owned.
- Use one H1 only; subsequent section headings use H2 and child labels use H3.
- Do not add a form widget until backend, consent, privacy, storage, error, replay, notification, and recovery behaviors are governed and tested.
- Do not add custom JavaScript, animation packages, global CSS duplication, popup builders, dynamic Product queries, or WooCommerce widgets under PP-01.
- If an Elementor feature requires Pro, its installed package/license compatibility must be verified before selection; no Pro assumption is part of this spec.

## Responsive Specification

| Viewport | Required behavior |
| --- | --- |
| 360px | One-column source order; 20px gutters; no horizontal overflow; CTA labels wrap cleanly or stack; no over-tall hero; contact number remains readable and tappable. |
| 390px | Preserve the 360px contract with 24px gutters; no breakpoint-only text or hidden essential content. |
| 430px | Allow comfortable CTA width and product entry composition without premature multi-column layout. |
| Tablet (`768–1023px`) | Two columns only where reading order remains obvious; navigation behavior is keyboard-operable; imagery never displaces the inquiry path. |
| Desktop (`≥1024px`) | Maximum 1200px container; hero may use a restrained two-column composition if rights-cleared media exists; capability layout may use up to three columns. |

At every breakpoint:

- preserve logical RTL order and intentional mixed-direction handling for phone, email, and URLs;
- preserve DOM/focus order; do not use visual reordering that changes meaning;
- prevent clipping, overlap, orphaned punctuation, broken Persian joining, and off-canvas controls;
- keep touch targets at least 44px and spacing sufficient for one-handed use;
- avoid text over busy images and reserve media dimensions to minimize layout shift; and
- test zoom, large text, landscape phone, keyboard navigation, and reduced motion.

## Accessibility Specification

- Use semantic landmarks: one `header`, one `nav`, one `main`, and one `footer`; the Elementor body supplies meaningful sections, not extra main landmarks.
- Use one H1 and a logical H2/H3 hierarchy.
- Target WCAG AA contrast: at least 4.5:1 for normal text and 3:1 for large text and meaningful non-text UI.
- Provide persistent visible keyboard focus and a skip-to-content mechanism in the Blocksy shell.
- Associate accessible names with icon-only controls; do not rely on color, position, or motion alone.
- Use Persian language metadata and RTL direction at the document level. Isolate LTR phone/email fragments with appropriate direction markup.
- Error, pending, and unavailable states must be programmatically determinable and written in plain Persian.
- No fake forms, empty anchors, focus traps, auto-advancing content, or hover-only information.

Exact conformance tooling and browser/assistive-technology matrix remain a PP-02 Test Contract item.

## Performance Specification

- Above the fold contains only the global shell, real text, two actions, and at most one optimized image.
- Prefer governed local font delivery with minimal weights; use a compatible system fallback while licensing/loading remains unresolved.
- Prefer responsive AVIF/WebP derivatives with an approved source retained in custody; SVG is permitted only for controlled logos/icons.
- Set explicit dimensions/aspect ratios, lazy-load below-fold media, and never lazy-load the principal LCP image.
- No slider, autoplay video, parallax, animation library, React runtime, decorative third-party script, or new cache plugin.
- Keep Elementor nesting and widgets minimal; avoid duplicated CSS and inline one-off token values.
- Numeric performance budgets are `FOUNDER_VISUAL_REVIEW / PERFORMANCE_APPROVAL_REQUIRED`; PP-01 does not invent pass thresholds.

## Asset Requirements Manifest

No approved production asset payload exists in the repository at PP-01 authoring time. PP-01 creates no media file. A future operator must accept only assets with owner, source, rights/license, capture date where relevant, allowed-use scope, integrity hash, and approval status.

| Asset ID | Placement | Candidate delivery requirement | Required evidence | Current disposition |
| --- | --- | --- | --- | --- |
| `PP01-BRAND-LOGO` | Header/footer | Vector SVG master plus transparent PNG fallback; legible at mobile header size; light/dark variants only if approved. | Brand-owner approval, provenance, rights, checksum, safe SVG review. | `MISSING_CONTENT / FOUNDER_VISUAL_REVIEW / NOT_DEPLOYED`. |
| `PP01-HERO-PRODUCT` | Optional hero | Rights-cleared original with candidate 8:5 desktop and 4:3 mobile crops; no embedded text/claim; explicit dimensions. | Source, rights, subject/product truth, crop approval, checksum, derivatives manifest. | `OPTIONAL / MISSING_CONTENT / RIGHTS_REQUIRED / NOT_DEPLOYED`. |
| `PP01-PRIMARY-FAMILY` | Primary Product Entry | Candidate 4:3 product image, neutral background, color-accurate, no inferred specification. | Rights and evidence that subject matches the named family; Founder crop/treatment approval. | `MISSING_CONTENT / RIGHTS_REQUIRED / NOT_DEPLOYED`. |
| `PP01-CAPABILITY-MEDIA` | Capability Overview | Zero to three candidate 4:3 images; the section must work without them. | Rights plus truthful association with each displayed capability. | `DEFERRED`; omit until proven. |
| `PP01-ICON-SET` | Actions/process themes | Minimal optimized SVG set with consistent stroke and accessible labels. | Source/license, sanitization, manifest, Founder style review. | `FOUNDER_VISUAL_REVIEW / RIGHTS_REQUIRED / NOT_DEPLOYED`. |
| `PP01-PERSIAN-FONT` | Global type | WOFF2 in only required weights, preload only if justified, robust fallback. | License allowing web embedding, file integrity, Persian glyph/digit coverage, performance review. | `MISSING_CONTENT / FOUNDER_VISUAL_REVIEW / NOT_DEPLOYED`. |

Candidate crop ratios and delivery formats are implementation guidance, not approved exact media dimensions or file-size budgets. Missing assets invoke the no-image fallback; placeholders must never be published as real content.

## SEO and Discovery Boundary

### Future Homepage Metadata

- Proposed title: **دماوند استیل | لوله استیل، آلومینیوم و محصولات دکوراتیو**
- Canonical host: `https://damavandsteel.com` (non-`www`)
- Candidate homepage canonical after target verification: `https://damavandsteel.com/`
- Meta description: `DEFERRED / REVIEW_REQUIRED`; do not infer one from unapproved copy.
- One H1: the frozen hero H1.

### Structured Data

Only `Organization`, `WebSite`, and `BreadcrumbList` may be considered in a future separately authorized runtime Mission, and only with verified entity/contact/URL facts. `Offer`, price, price range, public availability, inventory, review/rating, and unsupported `Product` properties are forbidden.

PP-01 performs no indexing, sitemap, robots, canonical, redirect, Search Console, analytics, schema, or runtime SEO mutation.

## Inquiry and Contact Behavior

- The primary CTA label is `استعلام قیمت و موجودی`; it must never display price or assert availability.
- The secondary CTA label is `مشاوره خرید`; it must not promise response time, suitability, or successful fulfillment.
- Telephone and WhatsApp may be linked only after device behavior, formatting, analytics/privacy implications, and destination ownership are verified.
- `sales@damavandsteel.com` stays internal to the plan as `PLANNED / DEFERRED / NOT PROVEN OPERATIONAL`; it is hidden from the public page until send/receive ownership and monitoring are tested.
- If no governed lead path is ready, PP-02 must expose only a verified direct channel or retain Coming Soon. It must not publish a form-shaped dead end.

## Founder Visual Checklist

The Founder checkpoint must record approve/revise/reject for:

- [ ] logo/wordmark asset, variants, clear space, and mobile legibility;
- [ ] exact semantic color palette and accessible color pairings;
- [ ] Persian font family, weights, licensing, digits, and fallback behavior;
- [ ] H1/H2/body scale, line length, and section rhythm on 360px and desktop;
- [ ] button radius, surface radius, borders/shadows, and focus appearance;
- [ ] hero composition with the no-image fallback shown alongside any media option;
- [ ] primary-family and capability imagery, provenance, crop, color treatment, and alternative text;
- [ ] icon set/source and whether icons add value;
- [ ] restrained motion proposal with reduced-motion version;
- [ ] Header/Footer appearance in Blocksy and body-token consistency in Elementor;
- [ ] Persian copy density, hierarchy, readability, and absence of unsupported claims;
- [ ] 360px, 390px, 430px, tablet, and desktop screenshots;
- [ ] visible absence of price, cart, checkout, payment, stock badges, fake counters, and Offer schema; and
- [ ] final publish/no-publish disposition at the explicit Coming Soon removal gate.

Unresolved visual choices are `FOUNDER_VISUAL_REVIEW`; they do not by themselves block completion of this repository-only PP-01 package. They do block a runtime publication decision where the affected choice is visible.

## Acceptance Checklist for This Specification

- [x] Exact IA and frozen hero/CTA/family copy recorded.
- [x] Complete content matrix and prohibited-claim rules recorded.
- [x] Reusable design-system candidate and Founder-controlled unknowns separated.
- [x] Blocksy/Elementor ownership and Elementor hierarchy fixed.
- [x] 360px, 390px, 430px, tablet, desktop, RTL, accessibility, and performance rules recorded.
- [x] Asset needs classified without fabricating or generating assets.
- [x] Future SEO title/canonical and no-price/no-Offer boundary recorded.
- [x] Contact facts separated from deferred unproven email operation.
- [x] No runtime, production, deployment, publication, or formal-launch authority granted.
