# Product Taxonomy Model

## Document Control

- **Document ID:** `docs/21_PRODUCT_TAXONOMY_MODEL.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On taxonomy purpose, hierarchy, term, slug, overlap, SEO, product, integration, or CentralSteel-mapping change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#taxonomy-architecture), and governing Founder constraints
- **Dependencies:** [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md) and [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md)
- **Related Documents:** [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md), [SEO Strategy](11_SEO_STRATEGY.md), and [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- **Traceability:** CP-002 through CP-006, WP-FC-004, WP-FC-005, WP-ARC-008, and TAX-001 through TAX-008
- **AI Compatibility:** AI-readable with explicit no-term, no-hierarchy, and no-configuration boundaries
- **Approval:** Pending Founder approval

## Purpose

Define taxonomy purpose, ownership, overlap controls, identity, slug, SEO, expansion, and future CentralSteel compatibility without creating taxonomy terms or configuring WordPress/WooCommerce.

## Scope

This model governs Product Families, Materials, Alloys, Use Cases/Applications, Industries, Finishes, Brands, Collections, Product Tags, SEO Landing classifications, and future CentralSteel mappings. Exact terms, hierarchies, labels, slugs, URLs, indexation, and physical WordPress mechanisms remain unapproved.

## Taxonomy Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| TAX-001 | Maintain one canonical term registry per concept, with stable internal IDs and controlled synonyms. | Proposed pending Founder approval |
| TAX-002 | Separate navigation classification, product specification, filtering, and SEO landing ownership; do not duplicate one concept across uncontrolled categories and attributes. | Proposed pending Founder approval |
| TAX-003 | Require one approved slug-language policy per taxonomy and prohibit mixed-script slugs. | Proposed pending Founder/SEO approval |
| TAX-004 | Create indexable SEO landing ownership only through an approved search-intent and cannibalization review. | Proposed pending Founder/SEO approval |
| TAX-005 | Govern term creation, merge, move, deprecation, redirect, and external mapping through Admin-manageable review. | Proposed pending Founder approval |
| TAX-006 | Map future CentralSteel identities to canonical internal terms instead of copying an external taxonomy into repository authority. | Proposed pending Founder approval |
| TAX-007 | Govern Collections and Product Tags as distinct optional editorial classifications with explicit owners, lifecycle, and SEO boundaries; neither may replace product hierarchy, specification, or compatibility authority. | Proposed pending Founder/SEO approval |
| TAX-008 | Treat `Applications` and `Use-Case Categories` as names for one logical classification unless the Founder approves a documented distinction and mapping; parallel term registries are prohibited. | Proposed pending Founder/domain/SEO approval |

## Taxonomy Registry

| Logical taxonomy | Purpose | Hierarchy | Relationship to attributes | SEO boundary |
| --- | --- | --- | --- | --- |
| Product Families | Primary governed catalog structure for related products | Hierarchical; exact levels pending | Family is not a specification attribute | Eligible landing ownership requires SEO approval |
| Material Categories | Broad navigational material grouping | Hierarchical only when domain structure is approved | Precise Material specification uses canonical Material attribute terms mapped to the category where necessary | Category and attribute archive must not target the same intent |
| Alloy Categories | Optional navigational alloy grouping when meaningful at category level | Hierarchy requires qualified steel-domain approval | Precise Alloy specification uses canonical Alloy attribute terms | Indexation requires demand and cannibalization review |
| Use-Case Categories | Approved application/use contexts | Hierarchical only when stable parent-child meaning exists | Installation Type, Environment, and Safety Requirement remain attributes unless an approved taxonomy purpose exists | One landing owner per use-case intent |
| Industry Categories | Approved industry contexts | Hierarchical only when governance defines scope | Not a substitute for product specifications | One landing owner per industry intent |
| Finish Categories | Optional navigational surface-finish grouping | Usually shallow; exact structure pending | Precise Finish value remains a canonical attribute | Category/attribute archive duplication prohibited |
| Brand Categories | Navigational view of one canonical Brand registry | Flat or hierarchical only with approved manufacturer relationships | Brand attribute and Brand landing reference the same canonical identity | One Brand landing owner; no duplicate category/page intent |
| Collections | Time-bounded curated grouping across approved products or families | Non-hierarchical by default; a hierarchy requires separate approval | References canonical products and terms; never creates specification values | Non-indexable by default; an indexable collection requires unique intent, owner, start/review/end conditions, and SEO approval |
| Product Tags | Optional non-hierarchical editorial discovery vocabulary | Non-hierarchical | Must not represent Family, Material, Alloy, Finish, Standard, Compatibility, Application/Use Case, Industry, Brand, or any governed attribute | Non-indexable by default; no automatic archive or landing authority |
| SEO Landing Categories | Curated search-intent ownership not already served by canonical product/category/content pages | Not a general dumping hierarchy | References canonical taxonomy/attribute combinations without copying terms | Indexable only with unique purpose, content, canonical, and maintenance owner |
| CentralSteel Mapping | Future external classification mapping | Mirrors no hierarchy by default | Maps internal IDs to external IDs and versions | Must not create duplicate public landings automatically |

Logical taxonomy names do not approve WooCommerce product categories, custom taxonomies, plugins, or database structures. The physical mechanism for each taxonomy requires a separate configuration decision under Plugin First and Configuration First.

## Collections and Product Tags Governance

Every Collection requires an assigned owner, stated purpose, inclusion criteria, start condition, review condition, end or renewal condition, lifecycle status, and affected-product evidence. Expired or ownerless Collections cannot remain operational. Collection filtering, navigation, URLs, archives, indexation, and physical mechanism remain unapproved until Founder/SEO review.

Every Product Tag requires an assigned editorial owner, definition, duplicate check, approved usage scope, lifecycle status, and review cycle. Tags are not filtering, variation, compatibility, product hierarchy, technical specification, or SEO landing authority by default. A tag that becomes reusable structured data must be migrated to the appropriate canonical taxonomy or attribute through review.

Exact owners, lifecycle vocabulary, review cadence, Collection duration rules, Tag vocabulary, filtering, and indexation remain TODO (Founder Decision Required).

## Application and Use-Case Terminology

`Applications` in [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#taxonomy-architecture) and `Use-Case Categories` in this model currently identify the same proposed logical concern: grouping products by an approved use context. `Use-Case Categories` is the working canonical name in Batch 05; `Applications` is an architecture alias, not permission to create a second taxonomy or duplicate term set.

The Founder, qualified domain reviewer, and SEO reviewer must approve the final name, Persian label, scope, hierarchy, term set, page relationship, and physical mechanism. If they decide Applications and Use Cases are distinct, the decision must define each purpose, inclusion/exclusion rules, relationship, migration path, and single SEO owner before either is created.

## Canonical Term Record

Each approved term requires:

- Stable internal term ID.
- Taxonomy ID and parent term ID when hierarchical.
- Persian display label.
- Approved English internal key.
- Approved public slug and declared slug language/script.
- Definition, inclusion criteria, exclusion criteria, and examples approved by the relevant domain owner.
- Synonyms, former labels, spelling variants, and transliteration mappings.
- Owner, reviewer, approval source, lifecycle, and review cycle.
- SEO indexation and landing-owner decision.
- Filter, navigation, variation, content, and inquiry use flags where applicable.
- External IDs scoped by system and mapping version.
- Merge, replacement, redirect, and deprecation relationships.

## Slug and Language Policy

- English internal keys use stable lowercase ASCII snake case and are not public slugs by default.
- Every public taxonomy declares either an approved Persian slug policy or an approved ASCII/transliteration policy before term creation.
- A single slug must not mix Persian and Latin scripts except an explicitly approved technical token.
- Slugs are normalized consistently for spacing, punctuation, digits, diacritics, Unicode, and case.
- Changing a public slug requires redirect, canonical, sitemap, internal-link, analytics, and external-integration impact review.
- Batch 05 does not decide whether public slugs are Persian or transliterated English.

## Category and Attribute Overlap Control

Use the following decision order:

1. If a concept defines primary catalog hierarchy, evaluate a category taxonomy.
2. If a concept is a reusable product specification, use a global attribute.
3. If a specification also needs navigation, derive or map the landing from the same canonical term identity.
4. Do not create an independent category term and attribute term with unrelated IDs for the same concept.
5. Do not use tags to bypass taxonomy/attribute governance.
6. Record the single SEO landing owner and canonical URL before indexation.

| Conflict example | Required resolution |
| --- | --- |
| Material category and Material attribute use the same wording | Link both views to one canonical Material identity and choose one SEO landing owner |
| Finish category duplicates Finish filter archive | Keep one indexable landing; other views canonicalize, noindex, or remain non-public according to approved SEO policy |
| Brand Page, Brand Category, and Brand attribute archive compete | Select one canonical Brand landing and make other representations supporting references |
| Product Family and Product Type names overlap | Define scope and hierarchy; do not publish ambiguous siblings |
| Use Case and Industry share terms | Assign each term to its true classification and document cross-relationships rather than duplicate labels |
| Application and Use Case use different labels for the same context | Use one canonical term identity and treat the other label as an alias until a distinct approved model exists |
| Collection or Product Tag duplicates a governed category/attribute | Remove or migrate the editorial classification; the governed registry remains authoritative |

## Duplicate Prevention

- Term creation searches canonical labels, internal keys, slugs, synonyms, former names, and external mappings.
- Unicode, Persian/Arabic character variants, spacing, punctuation, singular/plural, and transliteration are normalized for duplicate detection.
- Only authorized roles may propose terms; approval is separate from entry permission.
- Bulk import must not create unmatched terms automatically.
- Duplicate terms are merged through a reviewed migration with product reassignment, redirect, canonical, filter, and integration evidence.
- Deleted term IDs are not reused for a different meaning.

## SEO Cannibalization Control

Every potentially indexable taxonomy or landing records:

- Target search intent and audience.
- Canonical owner among product, family, category, attribute archive, curated landing, article, or page.
- Unique value, content responsibility, products included, and maintenance owner.
- Canonical, robots/indexation, pagination, filter/facet, sitemap, breadcrumb, and internal-link behavior.
- Competing URLs and consolidation plan.
- Review evidence before publication and after material term changes.

Thin, empty, duplicate, filter-only, or uncontrolled combination pages must not become indexable by default. Exact SEO rules remain pending.

## Unmanaged Product Sprawl Controls

- A new product must map to an approved Product Family, Product Type, attribute profile, and inquiry path.
- A new taxonomy term requires demonstrated non-duplication and a named owner.
- One-off labels remain product content until reuse and taxonomy purpose justify governance.
- Variations represent valid configurations, not marketing synonyms or duplicate products.
- Product duplication for language, region, brand spelling, material synonym, or SEO intent is prohibited without an approved model.
- Periodic review identifies empty terms, single-use terms, duplicate products, invalid combinations, and abandoned landings.

## Future CentralSteel Compatibility

CentralSteel is treated as a future external mapping target only.

- Preserve Damavand stable internal IDs and taxonomy authority.
- Store external taxonomy/term ID, external parent ID, mapping version, status, and last reconciliation evidence when later approved.
- Support one-to-one, one-to-many, many-to-one, and unmapped states explicitly.
- Do not rename internal terms or restructure hierarchy solely to mirror an external system without approved migration.
- Conflicts are resolved through mapping rules, not silent overwrite.
- External imports cannot create public categories, attributes, products, or SEO landings without review.

No CentralSteel API, taxonomy, field, provider, import, export, database mapping, or synchronization is implemented or assumed.

## Admin Manageability

- Term proposal, duplicate search, parent selection, synonyms, lifecycle, SEO owner, and external mapping must be manageable in supported Admin workflows when later implemented.
- Persian labels and English internal keys are displayed together to reduce ambiguity.
- High-impact merge, move, delete, slug, and indexation actions require preview, impact summary, approval, and recovery evidence.
- The Founder must not need code, SQL, command line, or direct database access.

## Founder Decisions

- Approve, revise, or reject TAX-001 through TAX-008.
- Approve the physical mechanism for each logical taxonomy.
- Approve Persian versus transliterated public slug policy.
- Approve taxonomy owners, term-creation authority, and review cadence.
- Approve which categories and landings may be indexable.
- Approve CentralSteel mapping authority and future integration scope.
- Approve Collections and Product Tags purpose, owners, lifecycle, duration/review, filtering, navigation, and SEO boundaries.
- Approve the canonical Application/Use-Case term, Persian label, scope, and whether one or two logical concepts are required.

## Open Questions

- What are the approved Product Family, Material, Alloy, Use Case, Industry, Finish, and Brand hierarchies?
- Which concepts remain attributes only, categories only, or mapped dual views?
- Which slug language and digit policy applies to public taxonomies?
- Which landing types own SEO intent for Material, Alloy, Finish, Brand, Use Case, and Industry?
- What CentralSteel identifiers, versions, and mapping directions will be required?
- Are Collections needed, who owns them, how are duration and expiry governed, and may any be indexable?
- Are Product Tags needed, who owns their vocabulary, and may they support navigation without filter or SEO authority?
- Should Applications and Use Cases remain one logical classification, and what is its approved canonical name?

## Approval Status

Review. No taxonomy, term, hierarchy, slug, archive, landing page, filter, custom taxonomy, plugin, or CentralSteel integration is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-07-03 | Batch 05B remediation: Collections and Product Tags governance plus explicit Application/Use-Case alias boundary; documentation only. |
| 0.1.0 | 2026-07-03 | Initial Batch 05 product taxonomy governance model; documentation only. |

## References

- [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md)
- [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md)
- [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md)
- [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#taxonomy-architecture)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Product Data Reading Path](READING_ORDER.md#product-data-and-woocommerce-reading-path)
