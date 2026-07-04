# WordPress Enterprise Architecture

## Document Control

- **Document ID:** `docs/06_WORDPRESS_ARCHITECTURE.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On WordPress, WooCommerce, product, taxonomy, inquiry, theme, plugin, integration, security, performance, SEO, or Founder-constraint change
- **Lifecycle:** Review
- **Source of Truth:** [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles), [ADR 0001](adr/0001-inquiry-first-commerce.md), and WordPress-specific Founder constraints recorded below
- **Dependencies:** [Enterprise Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [ADR 0001](adr/0001-inquiry-first-commerce.md), and [Project Constitution](01_PROJECT_CONSTITUTION.md)
- **Related Documents:** [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md), [SEO Strategy](11_SEO_STRATEGY.md), [Security](10_SECURITY.md), [UX Principles](12_UX_PRINCIPLES.md), [Testing Strategy](13_TESTING_STRATEGY.md), and [Traceability Matrix](TRACEABILITY_MATRIX.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, WP-FC-001 through WP-FC-005, and WP-ARC-001 through WP-ARC-012
- **AI Compatibility:** AI-readable with explicit implementation and decision boundaries
- **Approval:** Pending Founder approval; accepted Founder constraints retain only their recorded decision scope

## Purpose

Define the permanent logical WordPress Enterprise Architecture for future Damavand Steel implementation while preserving Founder constraints, approved governance, inquiry-first commerce, and administration-first manageability.

This document defines responsibilities, boundaries, dependencies, ownership, and extension rules. It does not install, configure, recommend, or implement WordPress, WooCommerce, plugins, themes, integrations, infrastructure, or production code.

## Scope

The architecture covers WordPress Core, WooCommerce, Blocksy Pro, Elementor Pro, product and taxonomy structures, content, users, inquiry, plugin capability categories, performance, security, SEO, integrations, administration, repository relationships, and future extension governance.

Exact plugin brands beyond Founder-mandated platforms, versions, product terms, taxonomy values, capability assignments, URL patterns, integration providers, service levels, and configuration values remain implementation prerequisites or Founder/domain decisions.

## Founder Constraints and Decision Sources

### Existing Governing Constraints

| Source | Constraint |
| --- | --- |
| CP-001 | Plugin First |
| CP-002 | Configuration First |
| CP-003 | Mobile First |
| CP-004 | Persian RTL |
| CP-005 and ADR-0001 | Inquiry First |
| CP-006 and ADR-0001 | No Public Pricing |
| CP-007 | No Custom Theme |
| CP-008 | No Gravity Forms |
| CP-009 | No LiteSpeed Cache |
| CP-010 | No AI Features in Phase 1 |

### WordPress-Specific Founder Constraints

These constraints are recorded from the explicit Batch 04 Founder directive. Their accepted scope is WordPress architecture; they do not approve implementation or unspecified configuration.

| ID | Constraint | Decision status | Architectural effect |
| --- | --- | --- | --- |
| WP-FC-001 | WooCommerce | Accepted Founder constraint and ADR-0001 alignment | WooCommerce is the product catalog authority within the inquiry-first boundary. |
| WP-FC-002 | Blocksy Pro | Accepted Founder constraint | Blocksy Pro is the vendor-controlled presentation shell; no custom or child theme is authorized. |
| WP-FC-003 | Elementor Pro | Accepted Founder constraint | Elementor Pro is the controlled visual composition capability within the ownership boundaries below. |
| WP-FC-004 | Variable Parent Product | Accepted Founder constraint | Product families are represented through variable parent products with approved variations and attributes. |
| WP-FC-005 | Founder Admin Manageability | Accepted Founder constraint | Supported WordPress Admin configuration is preferred; the Founder must not be required to program. |

## Architecture Decision Register

| ID | Decision | Source | Status |
| --- | --- | --- | --- |
| WP-ARC-001 | Use a layered logical architecture with explicit ownership and dependency direction. | Batch 04 objective and Enterprise Architecture | Proposed pending document approval |
| WP-ARC-002 | Prefer supported Admin configuration and approved plugins before code. | CP-001, CP-002, WP-FC-005 | Accepted constraint; detailed boundary proposed |
| WP-ARC-003 | Limit WordPress Core to CMS, identity, media, administration, and platform services. | CP-001, CP-002 | Proposed pending document approval |
| WP-ARC-004 | Use WooCommerce as product catalog authority while checkout, payments, cart, and public pricing remain inactive. | WP-FC-001, CP-005, CP-006, ADR-0001 | Accepted commerce boundary |
| WP-ARC-005 | Assign the global presentation shell to Blocksy Pro without vendor-file, child-theme, or custom-theme modification. | WP-FC-002, CP-007 | Accepted constraint; ownership detail proposed |
| WP-ARC-006 | Assign controlled page composition to Elementor Pro without overlapping global template ownership. | WP-FC-003, CP-002 | Accepted platform; ownership detail proposed |
| WP-ARC-007 | Represent configurable products as variable parent products and variations. | WP-FC-004 | Accepted product-model constraint |
| WP-ARC-008 | Govern taxonomies logically first; approve physical WordPress storage and term sets before configuration. | CP-002; Product Data Strategy is Draft related context, not an authority source or strict dependency | Proposed pending document approval |
| WP-ARC-009 | Use a contextual inquiry domain rather than transaction checkout. | CP-005, CP-006, ADR-0001 | Accepted boundary; workflow detail proposed |
| WP-ARC-010 | Assign one owner for metadata, canonical, schema, breadcrumb data, and other SEO outputs to prevent duplication. | SEO and maintainability requirements | Proposed pending document approval |
| WP-ARC-011 | Keep integrations behind governed interfaces and inactive until separately approved. | CP-002, CP-010, governance constraints | Proposed pending document approval |
| WP-ARC-012 | Select plugin capabilities by category, ownership, compatibility, support, security, and Admin manageability without brand selection in this batch. | CP-001, CP-002, WP-FC-005 | Proposed pending document approval |

## Architecture Principles

- One authoritative owner per responsibility and public output.
- Configuration before extension; approved plugin before custom development.
- WordPress Admin manageability for routine content, catalog, inquiry, SEO, and presentation operations whenever supported.
- Persian RTL and mobile behavior are acceptance boundaries, not optional enhancements.
- Product, taxonomy, and content structures use controlled identifiers and explicit data ownership.
- Public pages never expose pricing, checkout, payment, cart, or price-bearing structured data.
- Vendor core, theme, and plugin files remain unmodified.
- Future systems integrate through governed interfaces rather than direct shared-database assumptions.
- Draft integration and extension points do not authorize implementation.

## Logical System Architecture

| Layer | Responsibilities | Boundary | Depends on |
| --- | --- | --- | --- |
| Presentation Layer | Global shell, responsive layout, Persian RTL rendering, accessible components, approved visual templates | Does not own business rules, product authority, inquiry storage, SEO policy, or integration logic | Content, Commerce, SEO, Media, and Application layers |
| Application Layer | WordPress request lifecycle, Admin workflows, approved plugin orchestration, capability enforcement, supported APIs and events | Does not redefine business or commerce rules | WordPress Core, approved plugin capabilities, Business Layer |
| Business Layer | Inquiry-first constraints, visibility rules, product-model policy, routing policy, governance enforcement | Does not render pages or directly own vendor storage | Founder decisions, Business Rules, ADRs |
| Commerce Layer | WooCommerce products, variations, attributes, catalog taxonomies, inventory representation, product relationships | No public pricing, cart, checkout, payment, or direct sale | Business Layer, Application Layer, Integration Layer |
| Content Layer | Pages, articles, knowledge, FAQ, brand, industry, application, and support content | Does not own product master data or commercial transactions | WordPress Core, SEO, Media, Presentation |
| SEO Layer | Indexation policy, metadata, canonicals, schema, sitemap, breadcrumb data, redirect policy, internal-link governance | One public-output owner; no price-bearing schema | Content, Commerce, Presentation |
| Media Layer | Images, documents, downloads, metadata, derivatives, access classification, lifecycle | Does not become an unrestricted document repository | WordPress media services, Security, CDN-compatible delivery |
| Integration Layer | Governed adapters for ERP, CRM, email, SMS, WhatsApp, accounting, inventory, payments, shipping, APIs, and future systems | No direct authority transfer or shared-database coupling | Business, Commerce, Security, Administration |
| Administration Layer | Founder-manageable configuration, users, roles, content, catalog, inquiry, SEO, media, health, and audit views | Does not expose secrets or require routine programming | All managed layers and least-privilege policy |
| Repository Layer | Approved architecture, configuration templates, documentation, decision records, validation evidence | Runtime content, secrets, uploads, vendor packages, and generated state remain outside Git | Git Governance and Repository Standards |

### Dependency Direction

```text
Founder Decisions + Governance + Business Rules
  -> Business Layer
      -> Application + Commerce + Content + SEO + Media
          -> Presentation + Administration
              -> Integration Interfaces

Repository Layer -> governs definitions and evidence, not runtime execution
```

A lower layer cannot override a higher constraint. Presentation and integration concerns cannot redefine business, commerce, or authority rules.

## WordPress Core Responsibilities

### WordPress Core Owns

- Content persistence and revision history for native content types.
- Users, authentication primitives, roles, capabilities, and sessions within approved security controls.
- Media attachment records and supported upload handling within Media and Security boundaries.
- Admin navigation, editing lifecycle, settings APIs, supported REST interfaces, scheduled-event primitives, and site health capabilities.
- Native taxonomy and metadata primitives used through supported APIs.
- Extension lifecycle and supported hooks for approved plugins and the vendor theme.
- Localization, Persian content storage, timezone, locale, and RTL platform primitives.

### WordPress Core Must Never Own

- Founder approval, architecture authority, business-rule decisions, or repository governance.
- ERP, accounting, CRM, or external inventory master authority unless a future approved decision explicitly assigns it.
- Public pricing, cart, checkout, payments, shipping transactions, or direct-sale behavior under the current inquiry-first model.
- Reliable outbound mail delivery, CDN operation, external backup custody, perimeter security, analytics authority, or third-party consent records without an approved capability owner.
- Secrets embedded in content, source files, templates, or public settings.
- Custom modifications to WordPress Core files.
- AI product functionality in Phase 1.

## WooCommerce Responsibilities

| Concern | WooCommerce responsibility | Boundary |
| --- | --- | --- |
| Products | Canonical catalog records for approved sellable or inquiryable products | Product content must follow approved data and taxonomy rules |
| Variable parent products | Parent identity, shared content, family context, selectable configuration model | Parent is not a public transaction or price authority |
| Variations | Approved configuration combinations, variation identity, variation-level SKU and availability where applicable | No invalid or unapproved attribute combinations |
| Attributes | Global normalized specification vocabulary and variation/filter axes | Exact attribute sets, units, and values require product-data approval |
| Taxonomies | Product categories, tags, attributes, and approved extension taxonomies | No duplicate classification sources or invented term hierarchy |
| Inventory | Current catalog availability representation and stock-related data when approved | Future ERP authority and synchronization policy remain separate decisions |
| Inquiry context | Product, variation, quantity, attributes, attachments, and source-page context passed to the Inquiry Layer | WooCommerce does not convert inquiry into checkout or order |
| Commerce boundary | Catalog browsing, filtering, comparison-ready data, and inquiry initiation | Cart, checkout, payment, shipping purchase flow, and public price output remain inactive |
| Future pricing compatibility | Stable product and variation identifiers permit a future governed pricing adapter | No pricing engine, price display, or price schema is authorized now |

WooCommerce data is accessed through supported administration, APIs, and extension interfaces. Direct storage assumptions are prohibited for future integrations.

## Plugin Architecture

Plugin categories describe required capabilities, not brands or one-plugin-per-category mandates. A capability may be satisfied by WordPress Core, WooCommerce, Blocksy Pro, Elementor Pro, the hosting boundary, or one approved plugin after overlap analysis.

| Capability category | Responsibility | Architectural boundary |
| --- | --- | --- |
| SEO | Indexation, titles, descriptions, canonicals, sitemap, social metadata, and governed SEO controls | Must coordinate with the single schema and breadcrumb owner |
| Caching | Page-cache policy, invalidation, exclusions, and cache observability | Must not be LiteSpeed Cache; inquiry and authenticated responses require exclusion analysis |
| Forms and Inquiry | Secure inquiry capture, validation, consent, attachments, notifications, and product context | Must not be Gravity Forms; must not create checkout or expose pricing |
| Media | Image processing, metadata, derivatives, compression, and document organization | Original ownership, accessibility, retention, and protected media rules remain explicit |
| Security | Authentication hardening, monitoring, integrity, abuse controls, and security events | Does not replace least privilege, secure hosting, or update governance |
| Backup | Application/database backup coordination, restore evidence, and retention interfaces | External custody and disaster recovery remain outside the live WordPress database |
| SMTP and Email Delivery | Authenticated transactional delivery, retries, failure evidence, and sender governance | WordPress native mail is not the delivery authority |
| Analytics | Consent-aware measurement and event governance | No uncontrolled personal data, duplicate tags, or unapproved commercial tracking |
| Performance | Asset policy, diagnostics, optimization, and performance evidence | Must not duplicate cache, media, CDN, or theme ownership |
| Search | Catalog and content search relevance, Persian text behavior, and query observability | Must preserve product authority and access constraints |
| Filtering | Approved taxonomy and attribute filtering for variable products | Must use canonical terms and mobile/RTL interaction patterns |
| Redirects | Redirect lifecycle, loop detection, migration mapping, and 404 evidence | Must coordinate with URL and canonical ownership |
| Schema | Public structured-data generation and validation | Exactly one primary schema owner; no public price-bearing output |
| CRM Connector | Governed inquiry handoff, identity mapping, retries, status synchronization, and audit references | CRM is future integration, not currently selected or implemented |
| Cookie Consent | Consent categories, regional behavior, preference evidence, and script gating | Legal policy and vendor selection remain pending decisions |
| Import and Export | Validated bulk catalog/content exchange, dry-run, error reporting, rollback, and identifier preservation | No direct uncontrolled database writes |
| Roles and Capabilities | Admin-manageable least-privilege roles for SEO, Sales, and Representatives | Cannot grant Founder approval authority through WordPress capability alone |
| Integration Connectors | Governed adapters for approved future systems | One owner per integration; no AI connector in Phase 1 |

### Plugin Selection Gate

Before a brand or package is approved, document category fit, overlap, WordPress/WooCommerce compatibility, Blocksy/Elementor compatibility, RTL behavior, mobile behavior, Admin manageability, data ownership, security history, support, licensing, exportability, uninstall behavior, performance, update/rollback, and repository boundaries.

Plugin count is minimized by ownership clarity, not by combining unrelated responsibilities into an ungovernable package.

## Theme and Visual Composition Architecture

### Blocksy Pro Responsibilities

- Vendor-controlled theme foundation and global presentation shell.
- Header, footer, navigation, global responsive behavior, WooCommerce presentation integration, and theme-level design configuration.
- Global typography, color, spacing, container, and component defaults when supported through Admin configuration.
- Persian RTL and mobile rendering at the shell and theme-component level.

### Elementor Pro Responsibilities

- Admin-managed composition of approved pages, landing pages, and reusable content sections.
- Page-level responsive and RTL presentation within global design governance.
- Approved dynamic templates only where ownership is explicitly delegated and does not overlap Blocksy.
- Reusable design tokens and components aligned with the global Blocksy-owned shell.

### Template Ownership

| Template concern | Primary owner | Prohibited overlap |
| --- | --- | --- |
| Header, footer, primary navigation | Blocksy Pro | Elementor must not create competing global shell templates |
| Global theme and WooCommerce shell | Blocksy Pro | Elementor and plugins must not override the same template responsibility |
| Standard pages and landing-page body | Elementor Pro within approved templates | Blocksy custom layouts must not duplicate page-body ownership |
| Product and archive content data | WooCommerce and WordPress | Theme and Elementor do not become data authorities |
| Product and archive presentation | Blocksy Pro by default | Elementor ownership requires a future explicit architecture decision |
| Global design tokens | One approved Admin-managed design system, coordinated through Blocksy and Elementor | Independent conflicting token sets are prohibited |
| SEO metadata, canonical, and schema | SEO Layer | Blocksy and Elementor outputs must be disabled or coordinated when duplicative |

### Prohibited Theme Actions

- No custom theme or child theme.
- No direct changes to Blocksy, Elementor, WordPress, WooCommerce, or plugin vendor files.
- No copied vendor templates or unsupported overrides without a future superseding Founder decision.
- No overlapping ownership of header, footer, archive, product, schema, breadcrumb, or global style outputs.
- The existing repository child-theme placeholder is not an approved architecture component and remains subject to FD-GOV-008.

## Enterprise Product Architecture

### Product Entity Model

| Entity or concern | Architectural definition | Ownership and constraints |
| --- | --- | --- |
| Variable Parent Product | Canonical family-level catalog entity containing shared description, approved media, documents, and variation axes | WooCommerce; required by WP-FC-004 |
| Variation | Valid selectable configuration of the parent product | WooCommerce; only approved combinations are published |
| Product Family | Governed commercial and navigational grouping | Logical model; exact hierarchy and physical mapping require approval |
| Global Attribute | Reusable normalized specification or selectable axis shared across applicable products | WooCommerce global attributes; no duplicate term set |
| Material | Controlled product specification and potential variation/filter axis | Canonical vocabulary requires Founder and steel-domain review |
| Surface Finish | Controlled product specification and potential variation/filter axis | Canonical vocabulary requires domain review |
| Dimensions | Structured family-specific specifications with controlled units and validation | Do not collapse incompatible dimensional concepts into one free-text field |
| Shape | Controlled product specification and navigation/filter concept | Canonical vocabulary requires domain review |
| Standard | Controlled reference to approved technical standard terminology | Exact standards and claims require qualified review |
| SKU | Stable unique identifier at the variation level when variations are operationally distinct; parent identifier may also exist | Format, ownership, and ERP mapping remain pending decisions |
| Inquiry | Non-transactional request linked to product, variation, attributes, quantity, notes, and source context | Inquiry Layer; no checkout or public pricing |
| Media | Approved product images and visual assets with accessibility and usage metadata | Media Layer |
| Downloads and Documents | Approved datasheets, certificates, guides, and supporting files with version and access metadata | Media/Content boundary; document type and access rules pending |
| Related Products | Governed directional relationships for alternatives, compatible items, or editorial discovery | Relationship meaning must be explicit; no inferred compatibility claims |
| ERP Compatibility | Stable external IDs, units, attribute codes, and synchronization metadata reserved for future mapping | Integration Layer; ERP and field mapping are not selected |

### Product Rules

- The variable parent owns shared narrative and approved common assets; variations own configuration-specific identifiers and data.
- Variation axes must use approved global attributes when reused across products.
- Exact product families, terms, dimensional models, units, SKU formats, and valid combinations are not invented by this architecture.
- Product relationships distinguish alternative, related, and compatible meanings before use.
- Downloads and technical claims require version, owner, review status, and access classification.
- Public output excludes price, sale price, price ranges, cart, checkout, payment, and price-bearing schema.
- Future ERP integration uses stable IDs and supported interfaces rather than public labels as keys.

## Taxonomy Architecture

| Logical taxonomy | Purpose | Preferred mechanism and boundary |
| --- | --- | --- |
| Product Categories | Primary hierarchical catalog navigation and Product Family placement | WooCommerce product categories; exact hierarchy pending approval |
| Product Attributes | Structured specifications, filtering, and approved variation axes | WooCommerce global attributes when reusable |
| Product Tags | Optional non-hierarchical editorial discovery | Never the source for governed family, material, standard, or compatibility data |
| Collections | Curated cross-family grouping with defined owner and duration | Logical taxonomy; physical mechanism requires plugin/configuration decision |
| Applications | Products grouped by approved use context | Logical taxonomy; exact claims and physical mechanism require approval |
| Industries | Products and content grouped by approved industry context | Logical taxonomy; exact hierarchy requires approval |
| Materials | Canonical material vocabulary | Prefer one WooCommerce global attribute set when used for specification/filter/variation |
| Surface Finish | Canonical finish vocabulary | Prefer one WooCommerce global attribute set when used for specification/filter/variation |
| Shape | Canonical shape vocabulary | Prefer one WooCommerce global attribute set when used for specification/filter/variation |
| Standards | Approved technical-standard references | Controlled attribute or governed taxonomy; exact mapping requires domain review |
| Compatibility | Explicit relationship or controlled compatibility classification | Must not be inferred from shared tags or free text |

### Taxonomy Expansion Rules

- Every taxonomy has a purpose, owner, authority source, scope, hierarchy rule, identifier strategy, Persian label, machine-stable key, and change process.
- One concept has one canonical term set; synonyms redirect or map rather than duplicate authority.
- Reusable product specifications use global attributes; product-specific narrative does not become a global taxonomy.
- Variation use, filtering use, navigation use, and SEO indexation are approved independently.
- Term creation is Admin-manageable but permission-controlled and reviewed.
- Taxonomy changes assess URLs, redirects, canonicals, filters, products, integrations, analytics, and content.
- New countries and languages preserve stable IDs and add localized labels rather than duplicating products by default.
- No taxonomy term, hierarchy, translation, standard, material, finish, dimension, shape, application, or industry value is approved by this document.

## Content Architecture

| Content type | Responsibility | Default platform boundary |
| --- | --- | --- |
| Pages | Stable institutional, legal, contact, and primary informational content | WordPress Pages |
| Landing Pages | Campaign or focused conversion content leading to inquiry | WordPress Pages composed through Elementor Pro |
| Knowledge Pages | Durable educational or reference content | Native Pages or approved content capability; exact model pending |
| Articles | Time-ordered editorial and educational publishing | WordPress Posts |
| FAQ | Governed questions and answers with optional FAQ schema when eligible | Native content or approved structured-content capability |
| Brand Pages | Approved brand/manufacturer information without unsupported claims | Page or governed taxonomy landing; exact model pending |
| Industry Pages | Approved industry context connected to relevant products and knowledge | Page linked to Industry taxonomy |
| Application Pages | Approved application context connected to relevant products and knowledge | Page linked to Application taxonomy |
| Support Pages | Contact, inquiry help, documentation access, policies, and support guidance | WordPress Pages |

### Content Rules

- Product master data remains in WooCommerce; editorial content links to products rather than duplicating product authority.
- Page type, URL, template, indexation, owner, reviewer, update cycle, and inquiry goal are explicit.
- Persian is the Phase 1 content language and all presentation supports RTL.
- Exact editorial hierarchy, publishing workflow, brand list, industry list, application list, and FAQ content require separate approval.

### Media Library Organization

- Use stable file naming, descriptive Persian alt text, captions where needed, owner, rights, source, product/content relationship, access class, and review status.
- Separate public marketing assets from protected or internal documents through explicit access rules.
- Preserve originals according to approved retention while serving optimized derivatives.
- Organize by governed metadata or an approved media capability; do not rely solely on upload date or ad hoc folders.
- File replacement preserves URL, version, accessibility, cache, CDN, SEO, and product-reference impact.

## User and Role Architecture

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Founder | Approves governing decisions, architecture, major configuration, roles, releases, and exceptions | Business authority does not require routine programming or unrestricted technical access |
| Administrator | Performs controlled platform administration, updates, configuration, recovery, and technical diagnostics | Least number of named accounts; cannot self-approve Founder decisions |
| Editor | Manages approved non-product content and editorial workflow | No plugin, theme, role, security, or integration administration |
| SEO Manager | Manages approved metadata, indexation, redirects, internal linking, and SEO evidence | No product master, user administration, or architecture authority |
| Sales | Reviews and progresses authorized inquiry data | No site administration, public pricing, or taxonomy governance |
| Representative | Receives and manages assigned inquiries within approved scope | No global inquiry access unless explicitly authorized |
| Customer | Future optional authenticated requester capability | Account model, data access, and features require future approval; no checkout assumed |
| Guest | Public visitor who may browse and submit an approved inquiry | No private content or administration access |

Role names are logical. Exact WordPress capabilities, account creation, customer accounts, representative scope, separation of duties, and retention require a reviewed capability matrix before configuration.

No shared privileged accounts are permitted. Approval authority is governance metadata and cannot be granted merely by a WordPress role.

## Inquiry-First Architecture

### Inquiry Types

- General inquiry without product context.
- Product inquiry linked to a parent product or selected variation.
- Bulk inquiry containing multiple product lines or an approved structured attachment.
- Representative-assisted inquiry with recorded routing context.

### Logical Workflow

```text
Browse or Search
  -> Select Product / Variation Context (optional for general inquiry)
      -> Enter quantity, requirements, contact data, consent, notes, attachments
          -> Validate and protect submission
              -> Create inquiry record and immutable submission reference
                  -> Apply approved representative routing
                      -> Notify authorized recipients
                          -> Optional future CRM handoff
                              -> Track status and response history
```

### Inquiry Data Model

| Component | Required architectural data |
| --- | --- |
| Inquiry record | Stable ID, type, source, status, timestamps, consent evidence, language, and owner |
| Contact | Minimum approved identity and communication fields with access and retention controls |
| Inquiry line | Product/variation stable IDs, displayed labels snapshot, quantity, unit, selected attributes, and notes |
| Attachments | File metadata, validation result, access classification, retention, and protected retrieval reference |
| Routing | Rule version, assigned representative or queue, reason, timestamp, and reassignment history |
| Communications | Delivery channel, recipient, template/version reference, outcome, and retry evidence |
| Integration | External system ID, synchronization state, attempt history, and error evidence |

### Inquiry Boundaries

- No cart, checkout, order placement, public price, payment, or shipping-purchase flow.
- Inquiry submission never promises stock, price, delivery, compatibility, or acceptance.
- Attachments use allowlisted types, size limits, malware controls, randomized storage names, protected access, and retention policy.
- Representative routing is Admin-configurable and auditable; exact territories, priorities, fallback, and service levels require Sales and Founder approval.
- CRM compatibility uses idempotent handoff and stable IDs; CRM selection and synchronization are future decisions.
- Notifications do not replace the inquiry record and must expose delivery failures to authorized administrators.

## Performance Architecture

| Concern | Architecture rule |
| --- | --- |
| Page caching | Cache only eligible public responses; exclude Admin, authenticated, preview, inquiry submission, consent-sensitive, and personalized paths as required |
| Cache invalidation | Content, product, taxonomy, template, redirect, and approved integration changes trigger owned invalidation paths |
| Object cache | Future compatible capability for supported WordPress/WooCommerce object behavior; not assumed or selected |
| Image strategy | Responsive derivatives, modern compatible formats, compression, dimensions, alt text, and original retention |
| Lazy loading | Use supported behavior for below-the-fold assets; protect primary visual and layout stability |
| CDN | Future origin-compatible delivery for public static assets with purge, HTTPS, CORS, privacy, and Persian asset support |
| Database | WordPress/WooCommerce own supported application data; maintenance, indexing, cleanup, and backup follow approved operations |
| Elementor | Govern DOM size, widgets, fonts, effects, generated assets, and template duplication |
| Blocksy | Use supported responsive and asset controls without vendor modifications |
| Monitoring | Measure mobile and representative desktop experience; thresholds require approved performance budgets |

No cache plugin is selected. LiteSpeed Cache is prohibited. Performance optimization must not break inquiry submission, Admin editing, RTL, consent, security, or content freshness.

## Security Architecture

### Authentication and Authorization

- Named accounts, least privilege, strong authentication, session controls, and approved recovery.
- Multi-factor authentication for privileged roles when the selected capability and operations policy are approved.
- Capability checks at every administrative or data-access boundary.
- Founder approval authority remains outside WordPress role escalation.

### Files and Media

- Restrict executable uploads and validate extension, MIME type, size, content, and authorization.
- Public media is separated from protected inquiry attachments and restricted documents.
- Inquiry attachments require protected access, malware-scanning capability, retention, deletion, and audit evidence.
- Vendor packages, licenses, secrets, and backups are not public media.

### Operations and Recovery

- WordPress, WooCommerce, Blocksy Pro, Elementor Pro, and approved plugins follow staged update, compatibility, backup, rollback, and evidence requirements.
- Backups include database, approved uploads, configuration evidence, and restore testing; backup custody is external to the live site.
- Security events, failed authentication, privileged changes, plugin/theme changes, and inquiry access require appropriate logging and review.
- Debug output, stack traces, secrets, and personal data are not publicly exposed.
- Future hardening requires threat modeling and approved hosting/runtime architecture; this document does not select infrastructure or security products.

## SEO Architecture

### SEO Ownership

| Concern | Owner | Boundary |
| --- | --- | --- |
| URL strategy | SEO Layer with Content and Commerce input | Exact slugs and hierarchy require approval; URLs remain stable and redirect-governed |
| Titles and descriptions | SEO capability and authorized SEO role | Elementor and theme must not emit competing metadata |
| Canonicals | Single SEO owner | Must reflect approved indexation, filters, pagination, and product variation policy |
| Schema | Single Schema owner using approved Content and Commerce data | No duplicate output and no price, offer, checkout, or payment schema |
| Breadcrumb data | Single SEO/navigation owner | Blocksy may render only the approved source; competing breadcrumb systems are prohibited |
| Internal linking | Content and SEO governance | Links use canonical URLs and approved product/taxonomy relationships |
| Sitemaps | SEO owner | Include only approved canonical indexable content |
| Redirects | Redirect capability under SEO governance | Preserve reason, source, destination, status, owner, and review evidence |

### SEO Rules

- Product, variation, taxonomy, filter, pagination, and search indexation require an approved URL and canonical matrix before configuration.
- WooCommerce provides product facts; the SEO Layer controls public structured output.
- Inquiry pages and events use conversion-safe URLs without exposing personal or commercial data.
- Persian URL and transliteration policy remains a Founder/SEO decision; this architecture does not invent slug language.
- Future multilingual support uses language-aware canonicals, alternates, sitemaps, redirects, and stable entity IDs after a separate decision.

## Integration Architecture

All integrations are inactive future ports until separately approved. No provider, protocol implementation, credential, endpoint, or data mapping is selected here.

| Integration | Future responsibility | Current boundary |
| --- | --- | --- |
| ERP | Product, SKU, specification, availability, and future pricing/master-data synchronization | System-of-record and field mapping pending |
| CRM | Inquiry, contact, routing, activity, and status handoff | CRM not selected; WordPress inquiry record remains auditable |
| Accounting | Future approved commercial document or financial synchronization | No accounting or transaction behavior authorized |
| SMS | Consent-aware notifications and delivery evidence | Provider, templates, and triggers pending |
| Email | Authenticated inquiry and operational notifications | SMTP capability required; provider pending |
| WhatsApp | Future consent-aware representative communication | No provider or automation authorized |
| Payment Gateway | Future payment interface only after superseding commerce decision | Prohibited by current inquiry-first/no-checkout boundary |
| Shipping | Future fulfillment/rate interface only after superseding commerce decision | No shipping purchase flow authorized |
| Inventory | Future authoritative availability synchronization | ERP/Woo authority and conflict policy pending |
| AI | Future governed capability after Phase 1 and explicit Founder decision | Prohibited in Phase 1 |
| API | Versioned, authenticated, least-privilege interface for approved consumers | No public sensitive data, direct database access, or unapproved writes |

### Integration Rules

- Stable internal and external IDs; labels are not integration keys.
- Explicit source of truth per field and conflict direction.
- Authentication, authorization, encryption, consent, minimization, retry, idempotency, observability, reconciliation, and revocation.
- Versioned mappings and compatibility evidence.
- Queue or asynchronous processing when required without hiding failure.
- Admin-visible health and recoverable error states wherever possible.
- Integration failure must not expose prices, personal data, secrets, or broken public transactions.

## Administration Architecture

- The Founder manages approvals, high-level catalog governance, presentation choices, and operational visibility through understandable Admin interfaces whenever supported.
- Routine operations must not require PHP, JavaScript, CSS, SQL, command-line, or vendor-file editing.
- Admin pages use clear Persian-compatible labels, least privilege, safe defaults, validation, help text, and reversible workflows.
- Advanced technical actions remain assigned to qualified administrators and require documented evidence.
- Bulk changes provide preview, validation, error reporting, and rollback or recovery strategy.
- Configuration exportability and environment portability are evaluated before plugin approval.

## Extension Strategy

| Extension | Required gate |
| --- | --- |
| New plugin | Category ownership, overlap, compatibility, security, support, license, exportability, Admin manageability, rollback, and approval |
| New product family | Approved data model, parent/variation axes, taxonomy placement, content, media, inquiry context, SEO, and ERP identifiers |
| New taxonomy | Purpose, owner, non-duplication proof, hierarchy, terms, URLs, indexation, filtering, integration, and migration review |
| New workflow | Business decision, states, roles, data, notifications, integration, security, audit, and rollback |
| New country | Legal, content, units, contact, routing, privacy, SEO, and operational decision |
| New language | Translation ownership, locale, RTL/LTR, URLs, canonicals, alternates, taxonomy labels, search, and content workflow |
| Future marketplace | New business and architecture decision; seller, commission, moderation, payment, shipping, legal, and data boundaries required |
| Future B2B | New business and architecture decision; accounts, entitlements, private catalogs, pricing, approval, order, tax, and integration boundaries required |

Extensions cannot bypass the Core Project Principles. Public pricing, checkout, payments, custom themes, Gravity Forms, LiteSpeed Cache, and Phase 1 AI require the applicable rule or phase to be explicitly changed before architecture or implementation.

## Architecture Validation Matrix

| Constraint | Architecture evidence | Result |
| --- | --- | --- |
| Plugin First | Capability categories and selection gate precede custom development | Pass at architecture level |
| Configuration First | Admin-manageable configuration and no routine programming | Pass at architecture level |
| Inquiry First | Inquiry domain replaces transaction checkout | Pass |
| Variable Parent Product | Parent/variation model defined | Pass |
| Blocksy Pro compatibility | Vendor-controlled shell and ownership boundaries defined | Pass pending version validation |
| Elementor Pro compatibility | Controlled composition and non-overlap boundaries defined | Pass pending version validation |
| WooCommerce compatibility | Products, variations, attributes, taxonomies, inventory, and inquiry context use WooCommerce responsibility | Pass pending version validation |
| WordPress compatibility | Core responsibilities use supported platform primitives and extension boundaries | Pass pending version validation |
| Mobile First | Presentation, performance, filtering, and inquiry require mobile behavior | Pass at architecture level |
| Persian RTL | Presentation, content, search, Admin, and validation include Persian RTL | Pass at architecture level |
| Founder Manageability | Administration architecture avoids routine programming | Pass at architecture level |
| Repository compatibility | Runtime/vendor/generated boundaries remain separate from repository governance | Pass |
| Governance compatibility | Authority, approval, lifecycle, traceability, and open decisions remain explicit | Pass |
| No Public Pricing | Public price, price schema, cart, checkout, and payment outputs prohibited | Pass |
| No Custom Theme | Blocksy vendor files remain unmodified; no child/custom theme | Pass; repository placeholder remains unresolved |
| No Gravity Forms | Forms category has no brand and explicitly excludes Gravity Forms | Pass |
| No LiteSpeed Cache | Caching category has no brand and explicitly excludes LiteSpeed Cache | Pass |
| No AI Features Phase 1 | AI integration remains prohibited and inactive | Pass |

Architecture-level Pass means the written boundary is consistent. It does not prove runtime compatibility or authorize implementation.

## Open Architecture Decisions

The following remain unresolved implementation prerequisites and must not be inferred:

- Supported WordPress, WooCommerce, Blocksy Pro, Elementor Pro, PHP, database, and browser versions.
- Plugin brands, package count, licenses, support ownership, and capability-to-plugin mapping.
- Product families, materials, finishes, dimensions, units, shapes, standards, SKUs, variation matrices, and compatibility definitions.
- Taxonomy physical mechanisms, term sets, hierarchies, Persian labels, machine keys, URLs, and indexation.
- User capability matrix, customer-account policy, representative access, and separation of duties.
- Inquiry fields, consent text, statuses, routing, service levels, retention, attachment limits, and notification templates.
- SEO URL, slug language, canonical, filter, pagination, variation, and structured-data matrices.
- Media naming, rights, access, derivative, retention, and protected-document policies.
- ERP, CRM, analytics, consent, email, SMS, WhatsApp, search, CDN, cache, backup, and security providers.
- Integration sources of truth, APIs, mappings, credentials, retries, reconciliation, and ownership.
- Future pricing, payments, shipping, marketplace, B2B, country, language, and AI phases.

## Implementation Boundary

No implementation is authorized. Approval of this architecture would authorize it as a governing design input only. Installation, configuration, data creation, migration, code, credentials, infrastructure, plugin selection, theme activation, and production change require separate approved tasks and validation.

## References

- [Enterprise Architecture](02_ARCHITECTURE.md)
- [Business Rules](03_BUSINESS_RULES.md)
- [Technology Stack](05_TECH_STACK.md)
- [ADR 0001](adr/0001-inquiry-first-commerce.md)
- [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md)
- [SEO Strategy](11_SEO_STRATEGY.md)
- [Security](10_SECURITY.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Architecture Path](09_NAVIGATION_MAP.md#architecture-path)
- [WordPress Engineer Reading Path](READING_ORDER.md#wordpress-engineer-reading-path)
- [Batch 04 Audit](AUDIT_REPORT_BATCH04.md)
