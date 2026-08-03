# Enterprise Site Structure

## Document Control

- **Document ID:** `docs/25_SITE_STRUCTURE.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.1.1
- **Last Updated:** 2026-08-03
- **Last Review:** 2026-08-03
- **Review Cycle:** On site section, navigation, menu, product, taxonomy, knowledge, representative, support, landing, URL, search, or language change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md), and the Batch 05 product/taxonomy/inquiry reference models
- **Dependencies:** [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), and [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- **Related Documents:** [URL Architecture](26_URL_ARCHITECTURE.md), [Search and Discovery](27_SEARCH_AND_DISCOVERY.md), [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md), and [Content Operations](content/README.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, IA-001 through IA-007, and SITE-001 through SITE-007
- **AI Compatibility:** AI-readable with explicit required, conditional, protected, and unresolved nodes
- **Approval:** Pending Founder approval; no site or menu implementation authorized

## Purpose

Define the complete logical site tree and navigation responsibilities for products, knowledge, representatives, support, SEO landings, and inquiry-first journeys.

## Scope and Boundary

This structure names logical destinations and relationships, not approved Persian menu labels, WordPress pages, post types, templates, menus, widgets, URLs, taxonomy terms, or search configuration.

`Required` means required in the logical structure if this document is approved. `Conditional` means the node exists only after its referenced business, privacy, domain, SEO, or content decision. Placeholder tokens do not approve real content names.

## Site Structure Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| SITE-001 | Use one public entry structure with governed domain hubs for Products, Knowledge, Support, Company/Trust, Search, and Inquiry; Representative discovery remains conditional. | Proposed pending Founder approval |
| SITE-002 | Source product navigation from the canonical Product Repository hierarchy `Catalog → Platform → Family → Series → Variant Rules → SKU` without requiring the site tree to reproduce that hierarchy; SKU remains a derived identifier after governed modeling. | Proposed pending Founder/domain approval |
| SITE-003 | Use legacy Product Family/Product Group/Product Type labels, Variable Parent Product pages, Variation states, contextual classifications, and approved SEO landings only as governed navigation or public-page projections that do not own Product Repository identity. | Proposed pending Founder/domain/SEO approval |
| SITE-004 | Keep Knowledge Center organization separate from product taxonomy while connecting knowledge to authoritative Product Repository sources and approved public context projections. | Proposed pending Founder/content/SEO approval |
| SITE-005 | Make inquiry accessible from relevant destinations without creating cart, checkout, pricing, or transaction navigation. | Required by CP-005, CP-006, and ADR-0001 |
| SITE-006 | Exclude protected/internal inquiry, Customer, routing, CRM, operational, and document data from the public site tree. | Proposed pending Founder/security/privacy approval |
| SITE-007 | Treat menu composition as a view of governed information; menus do not become taxonomy, URL, or content authority. | Proposed pending Founder approval |

## Complete Site Tree

```text
Public Platform
├── Home [Required]
├── Products [Required]
│   ├── Product Discovery [Required]
│   ├── Family / Series Hubs [Navigation projections; source values pending]
│   ├── Product Family / Group / Type Views [Conditional legacy navigation mappings]
│   ├── Variable Parent Product Pages [Downstream public-page/commerce projections]
│   ├── Variation Context [Downstream selection state; non-canonical page by default]
│   ├── Application / Use Case [Conditional taxonomy/landing]
│   ├── Industry [Conditional taxonomy/landing]
│   ├── Material [Conditional governed landing]
│   ├── Finish [Conditional governed landing]
│   ├── Brand [Conditional governed landing]
│   └── Collection [Conditional and time-governed]
├── Knowledge Center [Required logical hub; inventory pending]
│   ├── Knowledge Topics [Conditional; terms pending]
│   ├── Knowledge Pages / Guides [Conditional content type]
│   ├── Articles [Conditional content type]
│   ├── FAQ [Conditional content type]
│   └── Approved Technical Documents [Public subset only]
├── Representatives [Conditional]
│   ├── Representative Discovery [Conditional]
│   └── Representative Profile [Conditional]
├── Support [Required]
│   ├── Inquiry Help [Required logical function]
│   ├── Product / Technical Document Help [Conditional]
│   ├── FAQ / Troubleshooting [Conditional]
│   ├── Contact and Escalation Context [Exact scope pending]
│   └── Policies and Access Guidance [Approved public subset]
├── Company and Trust [Required logical domain]
│   ├── Company Information [Exact inventory pending]
│   ├── Contact Context [Required]
│   └── Approved Public Policies [Exact inventory pending]
├── SEO / Campaign Landings [Conditional; not a standalone menu by default]
├── Search [Required capability entry; physical implementation pending]
└── Inquiry [Required engagement function]
    ├── General Inquiry
    ├── Product Inquiry [Contextual]
    ├── Multi-product Inquiry [Contextual]
    └── Project Inquiry

Protected / Internal Platform [Excluded from public tree]
├── Inquiry operations
├── Customer identity and consent
├── Representative routing and workload
├── Protected technical documents
├── CRM / ERP / CentralSteel mapping
└── Review, ownership, and audit evidence
```

The tree is complete by information responsibility. It does not approve real Product Families, topics, representatives, policies, landing pages, labels, or physical routes.

## Top Navigation

The proposed top-navigation slots are:

1. Home.
2. Products.
3. Knowledge Center.
4. Support.
5. Company/Trust.
6. Representatives, only if public representative discovery is approved.
7. Search access.
8. A clearly distinguished inquiry action.

Application/Use Case, Industry, Material, Brand, and other high-value discovery paths may appear inside Products or a governed contextual-navigation area after their purpose and demand are approved. Exact labels, order, visibility, and breakpoint behavior remain UX/Founder decisions.

Mobile navigation must preserve every essential destination and inquiry action without relying on hover, oversized mega menus, or left-to-right assumptions.

## Footer Structure

| Footer group | Logical content |
| --- | --- |
| Identity and trust | Approved company identity, contact context, public policies, and accessibility/privacy links |
| Products | Product hub and a controlled subset of approved Family/context links |
| Knowledge | Knowledge Center and approved content-type/topic entries |
| Support | Inquiry help, document help, FAQ/troubleshooting, and contact context |
| Representatives | Public directory only if approved |
| Engagement | General inquiry and approved inquiry guidance; no purchase or public-price path |
| Utility | Search, language access when later approved, sitemap, and other approved utility links |

Footer links must not create orphan campaign pages, duplicate taxonomy archives, or a second canonical hierarchy.

## Mega Menu Strategy

- Mega menus are optional navigation views, not required implementation components.
- A mega menu is justified only when an approved destination set cannot remain usable in a simpler structure.
- Product mega-menu content may expose a controlled subset of Family/Series navigation projections, explicitly mapped legacy Product Family labels, and approved context paths; it must not list uncontrolled terms or every downstream Variation.
- Knowledge mega-menu content may expose approved content types/topics and featured governed items.
- Representative entries do not appear unless public status and scope are approved.
- Mobile uses progressive disclosure with Persian RTL order and accessible focus/touch behavior.
- Ownership, item limits, ordering evidence, empty-state handling, review cycle, and analytics criteria require approval.
- No plugin, Elementor widget, Blocksy component, or menu configuration is selected here.

## Category Navigation

- Canonical Family and Series sources may drive primary catalog-navigation projections without making navigation the Product Repository authority.
- Product Family labels are legacy presentation/navigation mappings to an approved Family source only when the mapping is explicit.
- Product Group and Product Type are optional legacy navigation mappings, not canonical Repository layers; they appear only when an approved source mapping exists.
- Variant Rules govern eligible selection structure at the Repository layer; navigation may expose only approved downstream views of that structure.
- Material, Alloy, Application/Use Case, Industry, Finish, Brand, Collection, Product Tag, and SEO Landing classifications retain Taxonomy Model boundaries.
- Product Tags are not primary navigation, filters, specifications, or SEO landing authority by default.
- Collections are temporary curated paths and require owner/duration evidence.
- Category navigation hides unapproved, empty, duplicate, expired, protected, or non-canonical nodes.

## Product Navigation

- Breadcrumb/context shows an approved navigation path without redefining Product Repository identity or canonical public URLs.
- Family/Series hubs and explicitly mapped legacy Product Family/Group/Type views may lead to downstream Variable Parent Product pages without transferring source authority.
- Product pages expose downstream Variation selection derived from governed Variant Rules, specifications, documents, related products, knowledge/support context, and inquiry.
- A downstream Variation context does not automatically create a separate menu entry or canonical public page.
- Alternatives, accessories, compatibility, and related products use explicit relationship types; proximity does not imply compatibility.
- Stock or lifecycle state does not create public pricing or transaction navigation.

## Representative Navigation

- Representative navigation is conditional and absent until public scope is approved.
- If approved, users may discover representatives through the directory or explicit context relationships.
- Product, region, Application/Use Case, Industry, language, or support relationships require governed evidence.
- Public profiles expose only approved business information and contextual inquiry; internal routing, workload, private contact, status, and CRM data remain protected.
- No territory, qualification, priority, availability, or service-level claim is inferred.

## Support Navigation

- Provide a stable Support hub rather than scattering unrelated help pages.
- Route users to inquiry guidance, approved documents, FAQs/troubleshooting, contact context, and representative assistance when authorized.
- Keep public help separate from protected technical documents and inquiry records.
- Support journeys retain source context and end in the appropriate inquiry type when human follow-up is required.
- Support navigation must not promise warranty, compatibility, safety, delivery, or commercial terms without approved evidence.

## Knowledge Center Navigation

- The Knowledge Center is a distinct domain hub with controlled topic and content-type views.
- Topic paths must not duplicate canonical Family, taxonomy, or explicitly mapped legacy Product Family navigation authority.
- Knowledge items link to their authoritative Product Repository sources or approved public product-page projections, plus taxonomy, support, document, and inquiry contexts.
- Featured, latest, popular, and recommended views are presentation/discovery views, not new authority or taxonomy.
- Exact topics, content types, labels, archive behavior, and editorial cadence remain pending.

## SEO Landing Structure

SEO landings exist only when an approved unique search intent is not already owned by a product, category, attribute, knowledge item, or other page.

```text
Approved search intent
  -> One canonical landing owner
      -> Canonical taxonomy/product/knowledge references
          -> Contextual inquiry
```

Thin, empty, filter-generated, duplicate, expired, unowned, and uncontrolled-combination landings are excluded from indexable structure. Campaign landing lifecycle and canonical behavior must be recorded before publication.

## Future Expansion

New navigation domains must pass the expansion rules in the Information Architecture. Additions must identify owner, audience, content inventory, canonical relationship, URL, search, mobile RTL behavior, inquiry path, lifecycle, and migration impact before being added to any menu.

New languages or countries add localized views of stable identities by default; they do not duplicate product authority or create a parallel site tree without an approved localization architecture.

## Relationship with Taxonomy

- Taxonomy defines canonical classifications; Site Structure decides where approved classifications are discoverable.
- A menu label does not create a taxonomy term.
- A taxonomy term does not automatically require a menu item, archive, landing, or indexation.
- Application/Use Case uses one logical identity unless an approved decision separates the concepts.
- Site changes must preserve taxonomy duplicate, overlap, lifecycle, and SEO-owner controls.

## Relationship with URLs

- Site hierarchy and URL hierarchy are related but not identical.
- Navigation may change without changing a stable canonical URL.
- Breadcrumbs may show the logical product path even when the URL uses a stable type-owned namespace.
- Every public node resolves to the canonical behavior defined by URL Architecture.
- Menu aliases, campaign links, and filter links must not create duplicate canonicals.

## Relationship with Search

- Search provides a cross-tree discovery view; it does not replace site navigation or taxonomy.
- Search results group and identify node type, canonical owner, and approved context.
- Protected/internal nodes never enter public search.
- Filters use canonical taxonomy/attribute identities and do not create new site-tree nodes.
- Search ranking must preserve inquiry-first/no-price boundaries and cannot fabricate representative or product relationships.

## Founder Decisions

- Approve, revise, or reject SITE-001 through SITE-007.
- Approve top-navigation domains, Persian labels, order, mobile behavior, and inquiry action placement.
- Approve public Representative and Knowledge Center scope.
- Approve which contextual/SEO landing types may appear in navigation.
- Assign menu, site-tree, support, and knowledge ownership.

## Open Questions

- What are the approved Persian labels and order for top navigation and footer groups?
- Which contextual classifications deserve direct navigation?
- Is a mega menu necessary, and what governed limits apply?
- Are representative directory/profile destinations public?
- Which Knowledge Center topics and content types are approved?
- Which support, policy, and document destinations are public?

## Approval Status

Review. No page, menu, route, archive, search view, landing, representative profile, inquiry UI, template, widget, plugin, or configuration is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 06 logical site structure; documentation only. |
| 0.1.1 | 2026-08-03 | Reconciled product navigation with `FD-W2G-001` and `FD-W2G-002`; legacy hierarchy terms and Parent/Variation views remain downstream projections only. |

## Related Documents

- [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md)
- [URL Architecture](26_URL_ARCHITECTURE.md)
- [Search and Discovery](27_SEARCH_AND_DISCOVERY.md)
- [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md)
- [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)

## Traceability

| Decision range | Origin | Dependent concerns | Future evidence |
| --- | --- | --- | --- |
| SITE-001–SITE-007 | IA-001–IA-007, product/taxonomy/inquiry models, CP-003–CP-006 | URL, search, internal linking, future menus/content | Approved inventory, mobile RTL navigation, canonical ownership, public/protected separation, inquiry, and no-price validation |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Information Architecture Reading Path](READING_ORDER.md#information-architecture-reading-path)
