# Product Attribute Model

## Document Control

- **Document ID:** `docs/22_PRODUCT_ATTRIBUTE_MODEL.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On attribute definition, label, key, value, unit, variation, filtering, SEO, Product Type profile, or integration-mapping change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), and [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#enterprise-product-architecture)
- **Dependencies:** [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), and qualified steel-domain review
- **Related Documents:** [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md), and [Traceability Matrix](TRACEABILITY_MATRIX.md)
- **Traceability:** CP-002 through CP-006, WP-FC-004, WP-FC-005, WP-ARC-007, WP-ARC-008, and ATT-001 through ATT-007
- **AI Compatibility:** AI-readable; labels and policies remain proposed until Founder/domain approval
- **Approval:** Pending Founder approval and qualified domain review

## Purpose

Define the canonical global attribute registry, Persian labels, English internal keys, value governance, WooCommerce use, SEO boundaries, variation use, filtering use, and Admin guidance.

## Scope

This model defines attribute policy only. It does not create WooCommerce attributes, values, terms, variations, filters, URLs, imports, fields, UI, database schema, or code.

## Attribute Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| ATT-001 | Reusable product specifications use one canonical global attribute definition and stable English internal key. | Proposed pending Founder approval |
| ATT-002 | Each Product Type uses an approved attribute profile that separates required, optional, variation, filter, public, and integration uses. | Proposed pending Founder/domain approval |
| ATT-003 | Allowed values use controlled registries or validated typed values with explicit units; uncontrolled synonyms and mixed units are prohibited. | Proposed pending Founder/domain approval |
| ATT-004 | Variation and filtering are enabled independently and only when they provide valid catalog behavior. | Proposed pending Founder approval |
| ATT-005 | SEO landings may reference canonical attribute values but must not create duplicate term authority or cannibalizing archives. | Proposed pending Founder/SEO approval |
| ATT-006 | Attribute registries and value sets remain flat by default; any parent-child value relationship requires an attribute-specific definition and approval. | Proposed pending Founder/domain approval |
| ATT-007 | Size is derived presentation data, not a canonical global attribute or variation source; structured approved dimensions remain authoritative. | Proposed mapping of the existing Product Data Model Size definition; pending Founder/domain approval |

## Attribute Definition Standard

Every global attribute requires:

- Stable attribute ID.
- Approved Persian label and English internal key.
- Definition, scope, applicable Product Types, and non-applicable cases.
- Value type: controlled term, numeric, boolean, range, relationship, or governed text.
- Allowed-value source, owner, reviewer, lifecycle, synonyms, and external mappings.
- Unit policy, precision, tolerance, and display policy where relevant.
- Required/optional, public/private, variation, filtering, SEO, inquiry, import/export, CRM, and ERP use flags.
- Admin help text and validation behavior.

The Persian labels below are proposed working labels, not approved steel terminology.

## Global Attribute Registry

| Attribute | Proposed Persian label | English internal key | Allowed values policy | WooCommerce usage | SEO usage | Variation usage | Filtering usage | Admin notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Material | جنس | `material` | Controlled domain-reviewed material registry; synonyms map to one term | Global product attribute for applicable Product Types | Eligible only through one approved Material landing owner | Yes when material changes the offered configuration | Yes for applicable families | Do not create free-text material or duplicate Material Category identity |
| Alloy | آلیاژ | `alloy` | Controlled designation/family registry linked to compatible Material context | Global attribute; exact designation rules pending | Index only with unique approved intent and technical accuracy | Yes when alloy is a selectable supplied configuration | Yes when values are meaningful to users | Qualified technical review required; preserve exact approved notation |
| Finish | پرداخت سطح | `surface_finish` | Controlled finish registry with definitions and synonyms | Global attribute | Landing/archive only after cannibalization review | Yes when finish changes the supplied variation | Yes for applicable products | Do not mix finish, color, coating, or quality terminology |
| Color | رنگ | `color` | Controlled color registry only for products where color is meaningful | Global attribute for applicable profiles | Normally supporting metadata; landing requires approval | Conditional when color is a selectable supplied configuration | Conditional | Do not infer technical finish or coating from color alone |
| Diameter | قطر | `diameter` | Validated numeric value plus approved unit, precision, and range per Product Type | Global typed/controlled attribute as supported by approved implementation | Supporting specification; indexable archive requires explicit approval | Yes for products configured by diameter | Yes with unit-aware display | Never store unit inconsistently inside and outside the value |
| Thickness | ضخامت | `thickness` | Validated numeric value plus approved unit, precision, and range | Global typed/controlled attribute | Supporting specification; no automatic landing | Yes where thickness defines a supplied configuration | Yes for applicable products | Product Type defines dimensional meaning and tolerance context |
| Length | طول | `length` | Validated numeric or approved controlled supply-length value plus unit | Global typed/controlled attribute | Supporting specification; no automatic landing | Conditional when length is a selectable configuration | Conditional | Distinguish fixed, standard, cut, range, and unknown only after approval |
| Unit | واحد | `unit` | Approved unit registry with dimension, symbol, precision, and conversion authority | Global reference used with dimensions, quantities, and integrations | Not an independent SEO landing | No as a standalone variation axis | No as a standalone filter unless explicitly justified | Unit conversion is not label substitution and requires approved rules |
| Brand | برند | `brand` | One canonical approved brand/manufacturer registry | Global attribute or approved canonical brand mechanism; physical choice pending | One canonical Brand landing owner | No unless a future product model explicitly treats brand as a supplied configuration | Conditional | Brand Category, attribute, and page must share one identity |
| Quality Level | سطح کیفیت | `quality_level` | Controlled defined levels with evidence and owner | Global attribute for applicable profiles | Not indexable by default | Normally no; exception requires product rationale | Conditional | Must not imply grade, standard, certification, warranty, or origin without evidence |
| Installation Type | نوع نصب | `installation_type` | Controlled installation-method registry reviewed for applicable products | Global descriptive attribute | Possible use-case support; no automatic landing | Normally no | Conditional | Do not create unverified installation instructions or safety claims |
| Environment | محیط کاربرد | `environment` | Controlled operating/use-environment registry with defined scope | Global descriptive attribute | Supports approved application content | Normally no | Conditional | Do not imply suitability without technical evidence |
| Safety Requirement | الزامات ایمنی | `safety_requirement` | Controlled references to approved safety requirements or documents | Global descriptive/referential attribute | Not an automatic landing | No | Conditional only for verified user need | Requires qualified review; no unsupported compliance claim |
| Compatibility | سازگاری | `compatibility` | Verified relationship to product, system, standard, or use condition with evidence and direction | Relationship or governed attribute; physical mechanism pending | Eligible only when unique and verified | No unless compatibility defines a valid supplied option | Conditional | Never infer from shared tags, family, dimensions, or free text |
| Origin | مبدأ | `origin` | Controlled legally and operationally verified origin registry | Global attribute when approved and required | Not indexable by default | Normally no | Conditional | Definition must distinguish manufacture, material, brand, and shipment origin |
| Warranty/Guarantee | ضمانت / گارانتی | `warranty_guarantee` | Controlled reference to approved terms, coverage, duration, issuer, and document | Global reference or document relationship; physical mechanism pending | Not indexable by default | No | No by default | Must not publish promise without approved legal/commercial evidence |

## Attribute and Value Hierarchy Policy

- Global attributes form a flat registry; one attribute is not the parent of another attribute by default.
- Allowed values are flat within an attribute by default.
- Material-to-Alloy context, compatibility, unit families, synonyms, and external mappings are explicit relationships, not an implied parent-child tree.
- An attribute-specific hierarchy requires a defined purpose, parent rule, maximum depth, duplicate rule, owner, qualified reviewer, Admin behavior, import/export behavior, filter behavior, variation impact, SEO boundary, and migration plan.
- A hierarchical relationship must not be inferred from labels, shared words, category placement, or external-system hierarchy.

No hierarchical attribute or value set is approved by this policy. Exact exceptions remain TODO (Founder Decision Required).

## Size Architectural Status

Size is a derived human-facing composite defined in the [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md#core-entity-definitions). It is not part of the Global Attribute Registry, is not a local-attribute exception, and must not become an independent variation axis, filter authority, import key, or integration source.

Each Product Type profile must name the approved structured source fields—such as Diameter, Thickness, Length, or other separately approved dimensions—their order, units, separators, precision, and missing-value behavior before a Size display is produced. A stored display snapshot, if a future implementation requires one, remains derived and must be regenerable from the authoritative sources.

Size ownership and domain review follow the Product Type/attribute accountability recorded in the [Operational Ownership Matrix](19_PRODUCT_DATA_MODEL.md#operational-ownership-matrix). The exact formula, Persian display pattern, source fields, and reviewer remain TODO (Founder Decision Required).

## Attribute Profile Model

Each Product Type receives a profile with these flags per attribute:

| Profile field | Meaning |
| --- | --- |
| Applicability | Required, optional, prohibited, or conditional |
| Public visibility | Public, protected, internal, or integration-only |
| Variation axis | Allowed or prohibited |
| Filtering | Allowed or prohibited and filter order |
| Inquiry capture | Pre-filled, selectable, free requirement, or not used |
| SEO use | Supporting content, landing owner, non-indexable, or prohibited |
| Value source | Canonical registry, typed validation, relationship, or approved exception |
| Unit and precision | Required unit family, display unit, precision, and tolerance context |
| Ownership | Data owner, domain reviewer, and approval authority |

Profiles prevent every attribute from appearing on every product and prevent variation explosion.

## Allowed Values Policy

- Controlled-term attributes accept only approved canonical terms.
- Numeric attributes validate numeric type, range, precision, unit, and Product Type applicability.
- Synonyms, Persian/Arabic character variants, transliterations, and former values map to canonical IDs.
- Unknown, not applicable, not provided, and not yet verified are distinct controlled states; blank must not silently combine them.
- New value creation requires duplicate search, definition, owner, domain review, and external-mapping impact review.
- Imports may reject or quarantine unmatched values but must not silently create them.
- Deprecated values remain mapped for history and are replaced through a controlled migration.

## Variation Usage Policy

- An attribute becomes a variation axis only when customers or Sales must distinguish valid supplied configurations.
- Variation axes must be finite, approved, and compatible with Admin manageability.
- Descriptive, legal, safety, origin, warranty, environment, and relationship attributes do not become variation axes without an explicit Founder/domain decision.
- Valid-combination rules prevent a Cartesian explosion of impossible variations.
- Variation labels remain Persian RTL and mobile-usable; internal keys remain stable.

## Filtering Usage Policy

- Filters use canonical values and approved Product Type applicability.
- Empty, single-value, low-value, sensitive, unverified, or misleading filters remain hidden.
- Numeric filtering is unit-aware and must not compare incompatible units or contexts.
- Filter state, URLs, canonicals, indexation, performance, and mobile RTL behavior require SEO/UX approval.
- Filtering does not create product data or independent taxonomy authority.

## SEO Usage Policy

- Attribute values may support product content, internal links, schema facts, or curated landings only when accurate and approved.
- Raw attribute archive indexation is prohibited by default until an SEO intent matrix selects a unique canonical owner.
- No price or Offer schema is produced.
- Technical, safety, origin, compatibility, quality, and warranty claims require evidence before public SEO use.
- Persian labels and English internal keys do not decide public slug language.

## WooCommerce and Admin Boundaries

- Exact WooCommerce attribute names, slugs, ordering, archive settings, variation flags, and filter settings are not configured here.
- Routine value management must be possible through supported Admin workflows with controlled permissions.
- Admin screens must show Persian label, English key, definition, owner, Product Type applicability, and use flags.
- High-impact rename, merge, unit, variation, and visibility changes require impact preview and approval.
- Founder manageability does not grant unrestricted term creation or technical integration access.

## Founder Decisions

- Approve, revise, or reject ATT-001 through ATT-007.
- Approve each Persian label and English internal key.
- Approve the allowed-value owner and Product Type attribute profiles.
- Approve unit, precision, tolerance, variation, filter, and SEO policies.
- Assign qualified reviewers for Material, Alloy, dimensions, Standards, Safety, Compatibility, Origin, and Warranty/Guarantee.
- Approve the flat-by-default hierarchy policy and any attribute-specific exception.
- Approve Size source fields, formula, display pattern, ownership, and review responsibility by Product Type.

## Open Questions

- Are the proposed Persian labels acceptable for Damavand Steel users and domain experts?
- Which values and units are approved for each Product Type?
- Which attributes are required, variations, filters, public facts, or integration-only?
- How will controlled typed numeric values be represented through approved WooCommerce capabilities?
- Which attribute landings, if any, own SEO intent?
- Which external codes will ERP and CentralSteel require?
- Does any attribute require an approved parent-child value model; if so, what purpose and maximum depth apply?
- Which structured dimensions and display rule derive Size for each Product Type?

## Approval Status

Review. No attribute, term, value, variation axis, filter, archive, unit conversion, WooCommerce setting, or import is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-07-03 | Batch 05B remediation: explicit flat-by-default hierarchy policy and derived/non-global Size classification; documentation only. |
| 0.1.0 | 2026-07-03 | Initial Batch 05 global product attribute model with proposed Persian labels; documentation only. |

## References

- [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md)
- [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md)
- [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)
- [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Product Data Reading Path](READING_ORDER.md#product-data-and-woocommerce-reading-path)
