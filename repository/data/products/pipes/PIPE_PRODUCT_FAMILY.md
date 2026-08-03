# Stainless Steel Pipe Product Family

## Document Control

- **Document ID:** `repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md`
- **Status:** Review
- **Authority:** Product Data Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner and Qualified Steel-Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.1
- **Last Updated:** 2026-08-03
- **Last Review:** 2026-08-03
- **Review Cycle:** On family identity, naming, parent strategy, variation axes, inquiry, SEO, WooCommerce, CRM, or commercial-data change
- **Lifecycle:** Review
- **Source of Truth:** Sprint 03A task-defined Stainless Steel Pipe family and approved repository product-data principles
- **Dependencies:** [Enterprise Product Data Model](../../../../docs/19_PRODUCT_DATA_MODEL.md), [WooCommerce Product Model](../../../../docs/20_WOOCOMMERCE_PRODUCT_MODEL.md), and [Attribute Dictionary](../../attributes/ATTRIBUTE_DICTIONARY.md)
- **Related Documents:** [Pipe Variation Matrix](PIPE_VARIATION_MATRIX.md), [Pipe Import Template](../../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv), [Pipe SEO Entity Model](../../seo/PIPE_SEO_ENTITY_MODEL.md), and [Product Data Validation Rules](../../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, PDM-001 through PDM-008, WCM-001 through WCM-008, ATT-001 through ATT-007, and Sprint 03A
- **AI Compatibility:** AI-readable controlled product-family asset; no AI product feature, generated commercial value, or autonomous approval
- **Approval:** Pending Founder, Product Data, steel-domain, Sales, SEO, and WooCommerce review; not authorized for import

## Family Identity

The canonical Repository source follows `Catalog → Platform → Family → Series → Variant Rules → SKU`. Catalog through Variant Rules are canonical concepts; SKU is derived only after governed modeling and is not a canonical entity identity. The legacy and downstream labels in this asset do not replace that hierarchy.

| Field | Value | Status |
| --- | --- | --- |
| Canonical Family label | Stainless Steel Pipe | PD-02B APPROVED Family context; not Product/SKU/runtime authority |
| Persian family name | لوله استیل | Defined by Sprint 03A |
| Stable family ID | `prd:family:a10c6d8ceabc` | PD-02B APPROVED identity; not Product/SKU/runtime authority |
| Legacy Product Family presentation mapping | Stainless Steel Pipe | Historical Sprint 03A label; downstream mapping only |
| Legacy Product Group mapping | `TBD` | Must not be invented; not a canonical hierarchy layer |
| Legacy Product Type mapping | Stainless Steel Pipe / لوله استیل | Working downstream profile; Founder/domain approval required |
| Downstream initial Variable Parent Product mapping | Stainless Steel Pipe / لوله استیل | Candidate commerce presentation; mapping identity/SKU approval required |
| Canonical public-page slug | `TBD` | URL/SEO approval required; not Product identity |
| Lifecycle | Review | Not importable or public |

The canonical Family and downstream Variable Parent Product mapping remain separate even when their working display names match. A Family label must not become a WooCommerce product ID, SKU, taxonomy ID, or URL key, and a Parent mapping must never own canonical Product truth.

## Persian and English Naming

| Concern | Persian | English | Rule |
| --- | --- | --- | --- |
| Family display name | لوله استیل | Stainless Steel Pipe | Stable controlled labels; changes require alias/mapping review |
| Parent display name | لوله استیل | Stainless Steel Pipe | Working parent label; final approval pending |
| Variation display order | گرید، پرداخت، قطر، ضخامت، طول | Grade, Finish, Diameter, Thickness, Length | Persian RTL presentation; canonical Repository structured fields remain authoritative |
| Unit display | متر | meter | Unit key remains `meter`; quantity policy remains separate |

Persian labels use normalized Persian characters and RTL punctuation. English internal keys remain lowercase ASCII and never replace Persian public labels.

## Business Purpose

- Establish a controlled, reusable product-data contract for Stainless Steel Pipe.
- Support product discovery by governed technical configuration without creating uncontrolled product records.
- Preserve inquiry context at parent and variation level without public pricing or checkout.
- Provide a validation boundary for future WooCommerce import, SEO, CRM, ERP, and CentralSteel mapping.
- Keep routine future administration manageable through controlled attributes rather than duplicated free text.

This asset does not define prices, stock, suppliers, lead times, standards, warranties, final SKUs, or commercial availability.

## Parent Product Strategy

The initial downstream implementation candidate is one Variable Parent Product representing a shared Stainless Steel Pipe commerce presentation. It does not represent or own canonical Repository identity.

The downstream Parent mapping may own only:

- Persian and English shared presentation names.
- Downstream category and legacy Product Family/Product Type mappings.
- Shared description, inquiry guidance, media, and technical documents when approved.
- Declared presentation axes that mirror canonical Variant Rules; the Parent does not define axis or tuple validity.
- Public-page/search-intent ownership and one future approved canonical URL.
- Shared no-price and inquiry-only behavior.

The parent does not own:

- Canonical Catalog, Platform, Family, Series, Variant Rules, Product truth, or valid-combination authority.
- A public price or price range.
- A public purchasing action.
- A variation SKU.
- Unverified availability, brand, origin, quality, weight, standard, or supplier claims.
- Variation-specific dimensions or finish as authoritative shared values.

More than one parent may be required if future approved Product Types, use cases, technical structures, or valid matrices cannot be managed safely under one parent. Sprint 03A does not create those additional parents.

## Variable Product Strategy

### Historical Sprint 03A Candidate Axes

This Review-state table preserves the Sprint 03A candidate vocabulary. It is non-governing where later PD-02B/PD-03A evidence differs. Only canonical Variant Rules may authorize axes and structurally valid tuples; this table and a Variable Parent declaration cannot do so.

| Axis | Source | Variation use | Filter use | Notes |
| --- | --- | --- | --- | --- |
| Grade | Controlled values `201`, `304`, `316`, `430` | Yes | Yes | Sprint wording calls these Materials; canonical storage uses Grade to avoid duplicating Material authority |
| Finish | Silver, Gold PVD, Black PVD | Yes | Yes | Color/coating/finish terminology requires domain confirmation |
| Diameter | 16–102 mm controlled set | Yes | Yes | Numeric value stored separately from `mm` context |
| Thickness | 0.6–2 mm controlled set | Yes | Yes | Numeric value stored separately from `mm` context |
| Length | 3 m, 6 m | Yes | Yes | Numeric value stored separately from meter unit |

### Non-Axes

Material family, Unit, Brand, Country, Quality Level, Application, Environment, Installation Use, Stock Status, Inquiry Priority, and Surface do not create variations in Sprint 03A.

### Combination Boundary

- The controlled value sets define a candidate space, not verified commercial combinations.
- Canonical Variant Rules govern permitted axes and structurally valid tuples; the downstream Parent only mirrors an approved projection.
- No Cartesian product may be imported automatically.
- Every future Variation row must resolve to an approved tuple in the applicable Variant Rules.
- Commercial availability remains `TBD` until verified by the approved commercial authority.
- Duplicate attribute tuples are prohibited.
- One variation belongs to exactly one parent.

## Inquiry Behavior

- `inquiry_only` is `yes` for the parent and every variation.
- Inquiry action is contextual to the parent and selected variation values.
- The inquiry line carries stable canonical source references, separate downstream Parent/Variation mapping IDs, an approved derived-SKU snapshot when available, a Persian label snapshot, selected controlled attributes, Unit, requested quantity, and permitted notes.
- Quantity and commercial requirements remain customer inputs; no automated quotation or price response exists.
- Inquiry never creates public cart, checkout, payment, order, or public quotation behavior.

## No-Price Behavior

- `public_price` is empty in every import row.
- Zero is not used as a substitute price.
- `TBD`, `hidden`, text, currency, or sentinel values must not be entered in a price field.
- No price range, sale price, discount, Offer schema, cart, checkout, payment, price feed, or price-bearing analytics event is permitted.
- Private future quotation/pricing remains outside this asset and requires separate architecture and approval.

## UX Behavior

- Mobile First selection order: Grade → Finish → Diameter → Thickness → Length.
- Persian RTL labels appear before optional English technical tokens.
- Numeric dimensions display explicit units and never rely on column position alone.
- Invalid or unavailable combinations are not selectable or published.
- No default variation is assumed until a Founder/domain/UX decision is recorded.
- Inquiry remains reachable after a valid selection; unavailable commercial state must not become a false purchase promise.
- The Founder-facing Admin workflow must use controlled choices and validation reports rather than manual free-text duplication.

## SEO Role

- The Variable Parent Product is the candidate default public product-page and canonical-URL/search-intent owner only; it is not the canonical Repository Product entity or source of Product truth.
- Variation state is contextual to that downstream public page and has no independent canonical URL unless a later approved exception exists.
- Grade, Finish, Diameter, Thickness, and Length are supporting facts; no attribute archive becomes indexable automatically.
- A Product Family/category landing may own family discovery intent only after SEO/Founder approval.
- No price, Offer, transaction, stock promise, supplier, certification, or unsupported technical claim enters metadata or schema.
- Canonical public-page slug and indexation remain `TBD`.

## WooCommerce Mapping

| Logical asset | Future WooCommerce mapping | Current status |
| --- | --- | --- |
| Legacy Product Family presentation | Downstream taxonomy/category view of the canonical Family | `TBD`; no term created and no canonical identity transferred |
| Variable Parent Product | Downstream WooCommerce variable-product projection | Structure defined; no product created and no Product truth owned |
| Variation | Downstream WooCommerce variation mapping of one governed tuple | Valid rows only; no variation created |
| Grade/Finish/Dimensions | Approved global product attributes | Dictionary defined; no attribute/term created |
| Inquiry behavior | Approved inquiry capability/context | Mechanism `TBD`; no plugin/configuration selected |
| Pricing | Empty public price fields and exhaustive output suppression | Enforcement implementation `TBD` |
| Stock Status | Controlled domain state mapped later | Commercial state `TBD`; no WooCommerce stock setting |
| SEO | Parent public-page/canonical-URL projection plus approved supporting facts | Slug/index/schema output `TBD`; no Repository authority |

The CSV is a staging/import contract, not a direct execution authorization. Exact WooCommerce column mapping, global attribute IDs, term creation, product IDs, images, visibility, and rollback require a later approved import plan.

## CRM Relevance

Future inquiry/CRM handoff may use:

- Stable canonical source references and separate downstream Parent/Variation mapping identifiers.
- Approved SKU snapshot when final SKUs exist.
- Grade, Finish, Diameter, Thickness, Length, Unit, and requested quantity.
- Source entity/URL and Persian label snapshot.
- Stock State snapshot as context only.
- Inquiry Priority only when an approved Sales rule exists.

CRM must not become canonical Product Repository authority, infer availability, or receive public price data from this asset.

## Known Unknowns

- Stable downstream parent and variation mapping IDs; the PD-02B canonical Family identity is already recorded above.
- Final legacy Product Group/Product Type and downstream Parent mappings; the canonical Repository hierarchy is not an open question.
- Final downstream Parent reference and Variation derived-SKU syntax/values.
- Material-versus-Grade terminology and qualified steel-domain approval.
- Evidence-backed commercially valid tuples to be governed by the applicable Variant Rules; the candidate matrix is not authority.
- Stock state, supplier, brand, country, weight per meter, quality level, availability, lead time, and minimum order.
- Exact standards, tolerances, surface definitions, technical documents, and verified suitability claims.
- Media, alt text, rights, and variation image rules.
- WooCommerce attribute/term IDs, import mapping, inquiry mechanism, roles, and rollback.
- Canonical public-page slug, downstream category/public-page ownership, search intent, metadata, schema eligibility, and indexation.
- CRM/ERP/CentralSteel external mappings.

All commercial unknowns remain `TBD`; none may be converted into a claim during import.

## Founder Review Gates

- Approve the downstream Parent mapping and its relationship to the already governed canonical Family/Series; do not reopen the canonical hierarchy.
- Approve Material/Grade terminology and every controlled value.
- Approve the evidence-backed valid commercial combinations and limits recorded by the governing Variant Rules.
- Approve SKU policy and generated SKU values in a later sprint.
- Approve taxonomy, attribute, WooCommerce, inquiry, SEO, CRM, and import mappings.
- Approve responsible Product Data, domain, Sales, SEO, and technical reviewers.
- Approve no-price enforcement evidence and import rollback before execution.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03A Stainless Steel Pipe family asset; no WordPress product or import created. |
| 0.1.1 | 2026-08-03 | Reconciled Review-state Parent, variation, SEO, and WooCommerce language with `FD-W2G-001`; canonical Family/Series/Variant Rules remain Repository authority and no Product, SKU, mapping, or runtime object was created. |

## PD-02B Boundary

The stable Family identity and labels are governed by
`docs/PD02B_MINIMUM_CANONICAL_SLICE_SCOPE_V1.0.md`. PD-02B does not approve
this document's broader Series, variant, dimensions, Finish/Color/PVD,
availability, Product, SKU, SEO, import, or WooCommerce proposals. Those
sections remain Review-state context.

## Navigation

## PD-03A Prerequisite Override

For the exact PD-03A scope, the canonical Series label is
`لوله استیل دکوراتیو` and only the Persian official label exists. The Series
and internal Variant Rule identity are APPROVED only as the bounded PD-03A
prerequisite. Legacy Product Type, Parent Product, variation, WooCommerce, Slug,
and import descriptions in this file remain downstream or historical inputs.

PD-03A creates no Product, canonical Pilot, SKU, Slug, actual availability,
Master/Golden package, import mapping, or runtime record.

- [Attribute Dictionary](../../attributes/ATTRIBUTE_DICTIONARY.md)
- [Pipe Variation Matrix](PIPE_VARIATION_MATRIX.md)
- [Pipe SEO Entity Model](../../seo/PIPE_SEO_ENTITY_MODEL.md)
- [Product Data Validation Rules](../../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03A Audit](../../../../docs/AUDIT_REPORT_SPRINT03A.md)
