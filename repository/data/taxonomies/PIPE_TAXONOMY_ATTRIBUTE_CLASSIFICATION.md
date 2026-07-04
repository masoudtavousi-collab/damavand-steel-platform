# Pipe Taxonomy and Attribute Classification

## Document Control

- **Document ID:** `repository/data/taxonomies/PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md`
- **Status:** Review
- **Authority:** Product Data Classification Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Qualified Steel-Domain Reviewer, SEO Reviewer, CRM Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On field, classification, display, filter, variation, SEO, CRM, requiredness, or source-contract change
- **Lifecycle:** Review
- **Source of Truth:** Sprint 03A/03B Pipe data contracts and the approved Product Taxonomy, Product Attribute, SEO Entity, Custom Fields, and Inquiry models
- **Dependencies:** [Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md), [Attribute Dictionary](../attributes/ATTRIBUTE_DICTIONARY.md), [Pipe WooCommerce Mapping](../products/pipes/PIPE_WOOCOMMERCE_MAPPING.md), and [Pipe Import Mapping](../imports/woocommerce/PIPE_IMPORT_MAPPING.md)
- **Related Documents:** [Pipe Category Model](PIPE_CATEGORY_MODEL.md), [Pipe Attribute Model](../attributes/PIPE_ATTRIBUTE_MODEL.md), [Pipe Data Governance Checklist](../validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md), and [Pipe Import Precheck](../validation/PIPE_IMPORT_PRECHECK.md)
- **Traceability:** CP-001 through CP-010, PDM-001 through PDM-008, TAX-001 through TAX-008, ATT-001 through ATT-007, WCM-001 through WCM-008, INQ-001 through INQ-008, SEOENT-001 through SEOENT-009, FIELD-001 through FIELD-009, Sprint 03A, Sprint 03B, and Sprint 03C
- **AI Compatibility:** AI-readable controlled classification; no autonomous classification changes, generated commercial values, or Phase 1 AI feature
- **Approval:** Pending Founder and specialist review; no WordPress object, field, taxonomy, attribute, filter, CRM mapping, or SEO output is authorized

## Purpose

Assign one primary classification to every Pipe field currently defined by the 23-column import contract or the 16-field Attribute Dictionary. The classification prevents category/attribute duplication and identifies the field's canonical responsibility before implementation.

## Classification Semantics

- Each field has exactly one **Final classification** in this model.
- Final means the single proposed canonical class for Sprint 03C review; it does not mean Founder approval or physical WordPress implementation.
- A field may be consumed by SEO or CRM without becoming SEO Metadata or an Internal CRM Field. The classification identifies primary authority/storage responsibility; the use flags identify downstream consumers.
- `Yes` for public display means eligible for approved display after value/evidence approval. It does not publish a `TBD` value.
- `Required` is evaluated for the applicable row/lifecycle. For example, a variation SKU is required for a variation, not for the parent.
- WooCommerce Variation Attributes in this model are reusable global attributes that additionally drive Pipe variations. They must not be implemented as local attributes.
- No field is classified as WooCommerce Local Attribute. Reusable governed specifications must use canonical global identities.

## Field Classification Matrix

| # | Field name | Persian label | Final classification | Reason | Public display | Filterable | Variation-driving | SEO use | CRM use | Required | Founder review required |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `parent_sku` | شناسهٔ کالایی والد | Import Helper Field | Resolves the parent row and future native parent SKU; not a taxonomy or specification | No | No | No | No | Yes | Yes | Yes |
| 2 | `variation_sku` | شناسهٔ کالایی تنوع | Import Helper Field | Resolves future native variation identity; final syntax/value remains outside this sprint | No | No | No | No | Yes | Yes | Yes |
| 3 | `product_type` | نوع ردیف محصول | Import Helper Field | Controls parent/variation row role during mapping | No | No | No | No | No | Yes | No |
| 4 | `parent_name_fa` | نام فارسی محصول والد | Import Helper Field | Maps the approved Persian parent label to native product title behavior | Yes | No | No | Yes | Yes | Yes | Yes |
| 5 | `variation_name_fa` | نام فارسی تنوع | Import Helper Field | Deterministic display projection of approved structured variation values | Yes | No | No | No | Yes | Yes | Yes |
| 6 | `category` | دسته‌بندی محصول | WooCommerce Category | Represents the Product Family hierarchy, not a specification | Yes | Yes | No | Yes | Yes | Yes | Yes |
| 7 | `material` | آلیاژ | WooCommerce Global Attribute | Reusable family material context; working value is `stainless-steel` | Yes | No | No | Yes | Yes | Yes | Yes |
| 8 | `grade` | گرید | WooCommerce Variation Attribute | Controlled reusable technical designation and a Pipe variation axis | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| 9 | `finish` | رنگ و پوشش | WooCommerce Variation Attribute | Controlled finish/coating selection and a Pipe variation axis | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| 10 | `diameter_mm` | قطر (میلی‌متر) | WooCommerce Variation Attribute | Controlled unit-aware dimension and a Pipe variation axis | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| 11 | `thickness_mm` | ضخامت (میلی‌متر) | WooCommerce Variation Attribute | Controlled unit-aware dimension and a Pipe variation axis | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| 12 | `length_m` | طول (متر) | WooCommerce Variation Attribute | Controlled unit-aware supply length and a Pipe variation axis | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| 13 | `surface` | سطح | WooCommerce Global Attribute | Reusable specification distinct from Finish; values remain `TBD` | Yes | No | No | No | Yes | No | Yes |
| 14 | `unit` | واحد | WooCommerce Global Attribute | Controlled shared reference value `meter`; not a variation/filter axis | Yes | No | No | No | Yes | Yes | No |
| 15 | `brand` | برند | WooCommerce Global Attribute | Reusable canonical brand identity if later verified | Yes | No | No | No | Yes | No | Yes |
| 16 | `country` | کشور سازنده | WooCommerce Global Attribute | Reusable verified manufacturing-origin fact, distinct from shipping origin | Yes | No | No | No | Yes | No | Yes |
| 17 | `quality_level` | سطح کیفیت | WooCommerce Global Attribute | Reusable controlled specification only after evidence and definition exist | Yes | No | No | No | Yes | No | Yes |
| 18 | `application` | کاربرد | WooCommerce Global Attribute | Reusable product-use classification; not a category in the Pipe family model | Yes | No | No | Yes | Yes | No | Yes |
| 19 | `environment` | محیط استفاده | WooCommerce Global Attribute | Reusable evidence-backed use-environment specification | Yes | No | No | No | Yes | No | Yes |
| 20 | `installation_use` | نوع مصرف | WooCommerce Global Attribute | Reusable controlled consumption/installation-use specification | Yes | No | No | No | Yes | No | Yes |
| 21 | `weight_per_meter` | وزن هر متر | Custom Field | Typed technical value not represented by a Pipe taxonomy or variation axis | No | No | No | No | Yes | No | Yes |
| 22 | `stock_status` | وضعیت تأمین | Hidden/Internal Only | Protected commercial state; required for an execution-ready row but `TBD` must not become a public stock promise | No | No | No | No | Yes | Yes | Yes |
| 23 | `inquiry_priority` | اولویت استعلام | Internal CRM Field | Internal Sales/CRM routing concern, never product taxonomy or public ranking | No | No | No | No | Yes | No | Yes |
| 24 | `inquiry_only` | فقط استعلام | Custom Field | Product-level behavior flag required to enforce Inquiry First; physical mechanism remains unselected | No | No | No | No | Yes | Yes | No |
| 25 | `public_price` | قیمت عمومی | Excluded | Required empty-control column; No Public Pricing prohibits storage/mapping of any value | No | No | No | No | No | Yes | No |
| 26 | `seo_title` | عنوان سئو | SEO Metadata | Canonical parent search projection; not product-fact authority | Yes | No | No | Yes | No | No | Yes |
| 27 | `seo_description` | توضیحات سئو | SEO Metadata | Canonical parent search projection; must use approved facts only | Yes | No | No | Yes | No | No | Yes |
| 28 | `canonical_slug` | نامک کانونیکال | SEO Metadata | Canonical parent URL projection required before publication after URL/SEO approval | Yes | No | No | Yes | Yes | Yes | Yes |
| 29 | `notes` | یادداشت داخلی | Hidden/Internal Only | Controlled staging/review context; never a public product field | No | No | No | No | Yes | No | Yes |

## Classification Coverage

| Source | Field count | Coverage |
| --- | ---: | --- |
| Pipe CSV contract | 23 | All classified exactly once |
| Attribute Dictionary fields not present as CSV columns | 6 | Surface, Quality Level, Application, Environment, Installation Use, Inquiry Priority classified exactly once |
| Unique field total | 29 | All classified exactly once |

## Category-versus-Attribute Decisions

- Product Family `لوله استیل / Stainless Steel Pipe` is the only Pipe category concept approved for this review model.
- Material, Grade, Finish, Diameter, Thickness, Length, Surface, Unit, Brand, Country, Quality Level, Application, Environment, and Installation Use are attributes, not Pipe subcategories.
- Grade, Finish, Diameter, Thickness, and Length are controlled global variation attributes.
- Product type, names, and SKUs are import/native identity helpers, not categories or attributes.
- SEO metadata, CRM routing, protected commercial state, and review notes do not create public taxonomy terms.
- No local attribute or product tag is authorized to duplicate a governed global attribute.

## Custom-Field Boundary

Only `weight_per_meter` and `inquiry_only` receive the logical Custom Field classification:

- `weight_per_meter` requires a verified value, unit, precision, source, and technical reviewer before use.
- `inquiry_only` is a required behavior flag, but its physical field/plugin/configuration mechanism remains `TBD` under Plugin First and Configuration First.
- This classification does not select ACF, create a field group, choose a meta key, or authorize code.

## CRM Boundary

- `inquiry_priority` is the only primary Internal CRM Field.
- Other fields marked CRM use `Yes` may be copied as controlled snapshots/references; CRM does not become their product-master authority.
- `stock_status`, notes, customer/inquiry context, and commercial records remain protected and must never be exposed through public filters, schema, or product pages.

## Founder Decisions Required

- Approve all classifications marked Founder review required `Yes`.
- Approve Material/Grade/Finish terminology and public Persian labels.
- Approve the logical custom-field boundary and physical mechanism later.
- Approve CRM field ownership, access, retention, and mapping later.
- Approve SEO metadata ownership and public slug policy.
- Approve whether any currently non-filterable attribute becomes filterable through a future evidence-backed change.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03C classification of all 29 Pipe fields; no WordPress implementation or import. |

## Navigation

- [Pipe Category Model](PIPE_CATEGORY_MODEL.md)
- [Pipe Attribute Model](../attributes/PIPE_ATTRIBUTE_MODEL.md)
- [Pipe Data Governance Checklist](../validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md)
- [Sprint 03C Audit](../../../docs/AUDIT_REPORT_SPRINT03C.md)
