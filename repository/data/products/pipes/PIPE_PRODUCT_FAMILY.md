# Stainless Steel Pipe Product Family

## Document Control

- **Document ID:** `repository/data/products/pipes/PIPE_PRODUCT_FAMILY.md`
- **Status:** Review
- **Authority:** Product Data Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner and Qualified Steel-Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On family identity, naming, parent strategy, variation axes, inquiry, SEO, WooCommerce, CRM, or commercial-data change
- **Lifecycle:** Review
- **Source of Truth:** Sprint 03A task-defined Stainless Steel Pipe family and approved repository product-data principles
- **Dependencies:** [Enterprise Product Data Model](../../../../docs/19_PRODUCT_DATA_MODEL.md), [WooCommerce Product Model](../../../../docs/20_WOOCOMMERCE_PRODUCT_MODEL.md), and [Attribute Dictionary](../../attributes/ATTRIBUTE_DICTIONARY.md)
- **Related Documents:** [Pipe Variation Matrix](PIPE_VARIATION_MATRIX.md), [Pipe Import Template](../../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv), [Pipe SEO Entity Model](../../seo/PIPE_SEO_ENTITY_MODEL.md), and [Product Data Validation Rules](../../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, PDM-001 through PDM-008, WCM-001 through WCM-008, ATT-001 through ATT-007, and Sprint 03A
- **AI Compatibility:** AI-readable controlled product-family asset; no AI product feature, generated commercial value, or autonomous approval
- **Approval:** Pending Founder, Product Data, steel-domain, Sales, SEO, and WooCommerce review; not authorized for import

## Family Identity

| Field | Value | Status |
| --- | --- | --- |
| Product Family | Stainless Steel Pipe | Defined by Sprint 03A |
| Persian family name | لوله استیل | Defined by Sprint 03A |
| Stable family ID | `TBD` | Founder/Product Data decision required |
| Product Group | `TBD` | Must not be invented |
| Product Type | Stainless Steel Pipe / لوله استیل | Working profile; Founder/domain approval required |
| Initial Variable Parent Product | Stainless Steel Pipe / لوله استیل | Candidate parent; identity/SKU approval required |
| Canonical public slug | `TBD` | URL/SEO approval required |
| Lifecycle | Review | Not importable or public |

The Product Family and Variable Parent Product remain separate identities even when their working display names match. A family label must not become a WooCommerce product ID, SKU, taxonomy ID, or URL key.

## Persian and English Naming

| Concern | Persian | English | Rule |
| --- | --- | --- | --- |
| Family display name | لوله استیل | Stainless Steel Pipe | Stable controlled labels; changes require alias/mapping review |
| Parent display name | لوله استیل | Stainless Steel Pipe | Working parent label; final approval pending |
| Variation display order | گرید، پرداخت، قطر، ضخامت، طول | Grade, Finish, Diameter, Thickness, Length | Persian RTL presentation; structured fields remain authoritative |
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

The initial implementation candidate is one Variable Parent Product representing the shared Stainless Steel Pipe catalog identity.

The parent owns:

- Persian and English shared names.
- Product Family/Product Type relationships.
- Shared description, inquiry guidance, media, and technical documents when approved.
- Declared variation axes and valid-combination policy.
- Canonical SEO ownership and one future approved canonical URL.
- Shared no-price and inquiry-only behavior.

The parent does not own:

- A public price or price range.
- A public purchasing action.
- A variation SKU.
- Unverified availability, brand, origin, quality, weight, standard, or supplier claims.
- Variation-specific dimensions or finish as authoritative shared values.

More than one parent may be required if future approved Product Types, use cases, technical structures, or valid matrices cannot be managed safely under one parent. Sprint 03A does not create those additional parents.

## Variable Product Strategy

### Approved Sprint 03A Candidate Axes

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
- No Cartesian product may be imported automatically.
- Every future variation row requires an approved valid-combination record.
- Commercial availability remains `TBD` until verified by the approved commercial authority.
- Duplicate attribute tuples are prohibited.
- One variation belongs to exactly one parent.

## Inquiry Behavior

- `inquiry_only` is `yes` for the parent and every variation.
- Inquiry action is contextual to the parent and selected variation values.
- The inquiry line carries stable parent/variation identities, a Persian label snapshot, selected controlled attributes, Unit, requested quantity, and permitted notes.
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

- The Variable Parent Product is the default canonical product entity.
- Variation state is contextual and non-canonical unless a later approved exception exists.
- Grade, Finish, Diameter, Thickness, and Length are supporting facts; no attribute archive becomes indexable automatically.
- A Product Family/category landing may own family discovery intent only after SEO/Founder approval.
- No price, Offer, transaction, stock promise, supplier, certification, or unsupported technical claim enters metadata or schema.
- Canonical slug and indexation remain `TBD`.

## WooCommerce Mapping

| Logical asset | Future WooCommerce mapping | Current status |
| --- | --- | --- |
| Product Family | Approved taxonomy/category mapping | `TBD`; no term created |
| Variable Parent Product | WooCommerce variable product | Structure defined; no product created |
| Variation | WooCommerce variation | Valid rows only; no variation created |
| Grade/Finish/Dimensions | Approved global product attributes | Dictionary defined; no attribute/term created |
| Inquiry behavior | Approved inquiry capability/context | Mechanism `TBD`; no plugin/configuration selected |
| Pricing | Empty public price fields and exhaustive output suppression | Enforcement implementation `TBD` |
| Stock Status | Controlled domain state mapped later | Commercial state `TBD`; no WooCommerce stock setting |
| SEO | Parent canonical plus approved supporting facts | Slug/index/schema output `TBD` |

The CSV is a staging/import contract, not a direct execution authorization. Exact WooCommerce column mapping, global attribute IDs, term creation, product IDs, images, visibility, and rollback require a later approved import plan.

## CRM Relevance

Future inquiry/CRM handoff may use:

- Stable parent and variation identifiers.
- Approved SKU snapshot when final SKUs exist.
- Grade, Finish, Diameter, Thickness, Length, Unit, and requested quantity.
- Source entity/URL and Persian label snapshot.
- Stock State snapshot as context only.
- Inquiry Priority only when an approved Sales rule exists.

CRM must not become product-master authority, infer availability, or receive public price data from this asset.

## Known Unknowns

- Stable family, parent, and variation IDs.
- Final Product Group/Product Type hierarchy.
- Final parent and variation SKU syntax/values.
- Material-versus-Grade terminology and qualified steel-domain approval.
- Commercially valid combinations from the candidate matrix.
- Stock state, supplier, brand, country, weight per meter, quality level, availability, lead time, and minimum order.
- Exact standards, tolerances, surface definitions, technical documents, and verified suitability claims.
- Media, alt text, rights, and variation image rules.
- WooCommerce attribute/term IDs, import mapping, inquiry mechanism, roles, and rollback.
- Canonical slug, category ownership, search intent, metadata, schema eligibility, and indexation.
- CRM/ERP/CentralSteel external mappings.

All commercial unknowns remain `TBD`; none may be converted into a claim during import.

## Founder Review Gates

- Approve family/parent identity and hierarchy.
- Approve Material/Grade terminology and every controlled value.
- Approve valid commercial combinations and variation limits.
- Approve SKU policy and generated SKU values in a later sprint.
- Approve taxonomy, attribute, WooCommerce, inquiry, SEO, CRM, and import mappings.
- Approve responsible Product Data, domain, Sales, SEO, and technical reviewers.
- Approve no-price enforcement evidence and import rollback before execution.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03A Stainless Steel Pipe family asset; no WordPress product or import created. |

## Navigation

- [Attribute Dictionary](../../attributes/ATTRIBUTE_DICTIONARY.md)
- [Pipe Variation Matrix](PIPE_VARIATION_MATRIX.md)
- [Pipe SEO Entity Model](../../seo/PIPE_SEO_ENTITY_MODEL.md)
- [Product Data Validation Rules](../../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03A Audit](../../../../docs/AUDIT_REPORT_SPRINT03A.md)
