# Enterprise Media Strategy

## Document Control

- **Document ID:** `docs/33_MEDIA_STRATEGY.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On media type, identity, naming, organization, rights, accessibility, product photography, rendition, PDF, download, localization, storage, or CDN change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md#media-set-model), and [Content Types](32_CONTENT_TYPES.md)
- **Dependencies:** [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), and [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md)
- **Related Documents:** [Schema.org Strategy](31_SCHEMA_ORG_STRATEGY.md), [SEO Entity Model](34_SEO_ENTITY_MODEL.md), [URL Architecture](26_URL_ARCHITECTURE.md), [Security](10_SECURITY.md), and [Content Operations](content/README.md)
- **Traceability:** CP-001 through CP-006, CP-010, PDM-004, IA-001 through IA-007, CONTENT-001 through CONTENT-008, ERM-001 through ERM-008, and MEDIA-001 through MEDIA-009
- **AI Compatibility:** AI-readable media governance; no generated media, DAM, CDN, plugin, storage, or processing implementation authorized
- **Approval:** Pending Founder/content/technical/accessibility/security approval; no media implementation authorized

## Purpose

Define permanent logical governance for images, product photography, icons, illustrations, video, PDFs, downloads, derivatives, accessibility, localization, naming, organization, and future delivery infrastructure.

## Scope and Boundary

This strategy does not upload, create, edit, convert, compress, watermark, rename, move, delete, publish, or generate media. It does not create folders, WordPress Media Library records, CDN configuration, plugins, storage policies, image sizes, or processing code.

Exact dimensions, aspect ratios, file-size limits, codecs, licenses, retention periods, folder capability, CDN provider, and production workflows remain approval decisions.

## Media Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| MEDIA-001 | Govern every media asset through stable identity, owner, source, rights, access, lifecycle, relationships, language, and derivative evidence. | Proposed pending Founder approval |
| MEDIA-002 | Separate original/master assets, approved derivatives, public renditions, protected downloads, and internal working files. | Proposed pending Founder/content/security approval |
| MEDIA-003 | Organize media by metadata and entity relationships; logical folder views cannot become the only source of organization. | Proposed pending Founder approval |
| MEDIA-004 | Use controlled deterministic filenames that avoid personal, confidential, pricing, temporary, and presentation-only data. | Proposed pending Founder/content approval |
| MEDIA-005 | Require product photography and technical visuals to identify applicability without misrepresenting finish, color, scale, compatibility, quality, or availability. | Proposed pending Founder/domain approval |
| MEDIA-006 | Treat accessibility text, captions, transcripts, and localization as governed content tied to asset context and language. | Proposed pending Founder/accessibility/content approval |
| MEDIA-007 | Permit WebP or other derivatives only when source quality, transparency/animation needs, browser/channel support, fallback, and reversibility are validated. | Proposed pending Founder/technical approval |
| MEDIA-008 | Keep protected PDFs/downloads outside unrestricted public media paths and search/indexation. | Proposed pending Founder/security/technical approval |
| MEDIA-009 | Defer DAM, CDN, storage, optimization, transformation, and delivery selection to future Plugin First/Configuration First review. | Required by CP-001 and CP-002 |

## Media Governance

Every Media Asset records:

- Stable asset ID and type.
- Owner, source/creator, rights holder, license/permission, territory/channel/use constraints, expiry, and approval evidence.
- Original/master identity, derivative relationship, checksum/integrity evidence when required, and replacement history.
- Public/protected/internal access class.
- Related Organization, Product, Variation, Content, Project, Representative, or Document IDs.
- Language/locale, embedded text language, caption, alt-text context, transcript/captions status, and accessibility review.
- Lifecycle, review trigger, version/revision, publication eligibility, and retention/deletion authority.

No asset is public merely because it exists in a media library or public-looking folder.

## Media Lifecycle

| State | Meaning | Public boundary |
| --- | --- | --- |
| `received` | Asset is ingested with source identity pending validation | Not public |
| `rights_review` | Rights, privacy, access, and source are under review | Not public |
| `content_review` | Quality, accuracy, applicability, localization, and accessibility are under review | Not public |
| `approved` | Asset and approved uses are recorded | Publication remains context-specific |
| `published` | An approved rendition is publicly used in an eligible context | Public only for approved contexts |
| `restricted` | Use is limited or withdrawn by rights/security/content decision | Not publicly promoted |
| `expired` | Rights, relevance, or review period ended | Removed from public use pending renewal/replacement |
| `archived` | Retained as evidence/history, not active use | Internal/protected according to policy |

This lifecycle does not replace Product, Content, Technical Document, or Repository Document lifecycle.

## Naming Convention

Logical filename pattern:

```text
{entity-type}-{stable-public-safe-reference}-{asset-role}-{view-or-sequence}-{locale}-{revision}.{extension}
```

Rules:

- Use a stable public-safe reference, not database ID, customer name, inquiry ID, hidden SKU, price, date-only identity, or private external ID.
- Use lowercase ASCII and hyphens for technical filenames unless a later approved storage standard permits another form; Persian titles/captions remain metadata.
- Record asset role such as primary, gallery, detail, diagram, application, packaging, document-preview, icon, or illustration through controlled vocabulary.
- Include locale only when pixels/embedded text differ by locale.
- Use revision only when a new file must coexist; asset version authority remains metadata.
- Keep extension consistent with actual encoding.
- Do not stuff keywords, claims, dimensions, color/finish, compatibility, or status into filenames unless they are approved stable identity components.

Literal patterns, vocabulary, maximum lengths, collision rules, and migration behavior remain pending.

## Folder Strategy

Folders are logical operational views, not canonical classification. Proposed logical dimensions include:

- Access: public, protected, internal.
- Asset class: image, icon, illustration, video, PDF/document, other download.
- Canonical entity relationship: product, content, organization, representative, project, support.
- Lifecycle: review, active, restricted/expired, archive.
- Source/rights owner and campaign/collection only where operationally needed.

The same asset may appear in multiple logical views without file duplication. Upload date, editor name, arbitrary campaign folder, or filesystem path cannot be the only retrieval method. Exact folder capability and physical storage remain unselected.

## Image Standards

- Preserve an approved master with sufficient quality and known provenance.
- Derivatives declare purpose, crop/aspect, dimensions, format, compression/quality, color profile, transparency, and source asset.
- Avoid upscaling beyond approved quality thresholds.
- Prevent baked-in public prices, confidential data, unsupported claims, inaccessible text, and misleading color/scale.
- Text embedded in images requires localization, contrast, legibility, source-text, and update workflow; live text is preferred where feasible in future implementation.
- Responsive rendition policy, exact sizes, formats, quality targets, and performance budgets remain pending technical/UX approval.

## Product Photography

Each approved product photograph identifies:

- Parent Product/Variation applicability and asset role.
- Whether color, finish, dimensions, packaging, installation, application, or environment are representative or exact.
- Source, photographer/rights, capture/edit history where needed, and review owner.
- Background, scale/reference, crop-safe area, orientation, and mobile focal point when approved.
- Retouching boundary that cannot change technical/product truth.

Primary/gallery images must not imply a configuration, finish, included accessory, certification, stock, installation, location, brand, or availability that is not approved for the linked entity.

## Icons

- Icons express a single approved concept and use a controlled library, stable asset ID, name, owner, source/license, viewBox/dimensions when relevant, and accessibility role.
- Decorative icons are identified as decorative; meaningful icons require an accessible text equivalent in context.
- Directional icons support Persian RTL mirroring where meaning changes; universal symbols are not mirrored without review.
- Icons do not replace labels for critical inquiry, safety, document, or navigation actions.
- No icon library, SVG implementation, or component system is selected here.

## Illustrations

- Illustrations have explicit educational, editorial, or explanatory purpose and related entity IDs.
- Technical diagrams distinguish conceptual, not-to-scale, and verified engineering representations.
- Embedded labels require language/localization source and review.
- Generated or synthetic illustrations are not authorized; any future generated-media policy requires separate Founder, rights, disclosure, safety, and review decisions.
- Style system, production tools, and templates remain unselected.

## Video

- Record title, purpose, owner, source/rights, language, lifecycle, access, duration, related entities, transcript, captions/subtitles, thumbnail, and review evidence.
- Product demonstrations, installation, safety, compatibility, project, and representative claims require qualified review.
- Public video needs accessible controls, captions, transcript or equivalent, mobile behavior, and no autoplay assumption.
- Hosting, player, encoding ladder, streaming, analytics, consent, and CDN remain pending.
- Videos cannot contain public pricing, confidential customer/project data, unapproved locations/people, or transaction promises.

## PDF

- Treat every PDF as a versioned Document entity with title, type, language, version, issue date, owner, reviewer, access class, applicability, source, replacement, and integrity evidence where required.
- Public PDFs require searchable/selectable text where feasible, document language, tagged structure/accessibility review, descriptive title, reading order, and meaningful link text.
- Scanned-only PDFs require remediation or an approved exception.
- Product datasheets, certificates, warranties, installation guides, and safety documents require qualified evidence and applicability.
- PDF filename, document title, and version metadata remain consistent without making the filename the identity.

## Downloads

- Downloads declare asset/document ID, purpose, audience, format, size, version, owner, rights, access, related entities, and expiry/replacement.
- Public download links resolve through canonical content/document context; raw attachment URLs do not become uncontrolled SEO landings.
- Protected/internal downloads require authorization and are excluded from public search, sitemap, cache, previews, and unrestricted URLs.
- Executables, archives, source files, CAD/engineering files, and other high-risk formats require separate security and operational approval.
- No upload/download capability or access-control implementation is selected here.

## WebP Rules

- WebP may be an approved derivative, not the sole archival master by default.
- Preserve a source format appropriate to photography, lossless graphics, transparency, animation, technical fidelity, and future regeneration.
- Choose lossless/lossy behavior per asset purpose and validate visual differences, text/diagram clarity, transparency, metadata/privacy, and file size.
- Provide an approved fallback only where supported consumers require it; do not duplicate canonical asset identity per format.
- Recompression chains and conversion from low-quality derivatives are prohibited.
- WebP use does not authorize a plugin, server module, build process, or CDN transformer.

## Future CDN Strategy

A future CDN decision must define:

- Canonical origin and asset identity.
- Public/protected delivery separation and signed/private behavior if needed.
- Cache keys, locale/rendition parameters, invalidation, purge, replacement, rollback, and stale-content controls.
- Transformation ownership, allowed operations, quality, format negotiation, security, privacy, logging, consent, and data location.
- URL/canonical/SEO effects, CORS, hotlinking, backup, exportability, vendor exit, and cost governance.
- Plugin First/Configuration First selection, WordPress compatibility, Blocksy/Elementor/WooCommerce behavior, and Admin manageability.

No CDN provider or architecture is selected.

## Accessibility

- Every asset declares whether it is informative, functional, complex, decorative, or a document.
- Informative images require contextual text alternatives; complex diagrams need a concise alt plus nearby long description or equivalent.
- Functional media receives an accessible action label, not a visual description alone.
- Decorative media is excluded from assistive output through future supported implementation.
- Video requires captions and approved transcript/equivalent; audio requires transcript/equivalent.
- PDFs require document accessibility review.
- Do not place essential meaning only in color, image text, sound, motion, hover, or left-to-right layout.

## Alt Text Rules

- Describe the asset's purpose in the specific context, using natural Persian for Persian content.
- Use approved product/entity terminology and identify relevant view/detail only when useful.
- Do not repeat surrounding text, filename, keyword list, “image of,” public pricing, unsupported claims, or hidden SEO terms.
- Decorative context uses no descriptive alt; the same asset may need different contextual alt text in different uses.
- Charts/diagrams require data/meaning equivalence beyond a short alt when necessary.
- Alt text has owner, language, source context, review status, and update dependency on asset/entity change.

## Localization

- Asset identity is language-neutral; captions, alt text, transcripts, embedded text, thumbnails, and locale-specific derivatives are related localized expressions.
- Persian RTL is the current requirement; embedded Persian text uses reviewed typography/direction and does not rely on mirrored source artwork without validation.
- Translation preserves fact/source authority and technical terminology.
- A locale-specific derivative identifies source asset, locale, translator/reviewer, and revision.
- Future language expansion follows URL/content alternate and ownership rules; it does not duplicate master assets unnecessarily.

## Founder Decisions

- Approve, revise, or reject MEDIA-001 through MEDIA-009.
- Assign media, rights, accessibility, photography, technical-document, localization, security, and derivative owners.
- Approve file naming, logical folder views, media lifecycle, rights/retention, and access policy.
- Approve type-specific standards, WebP/format rules, PDF accessibility, and download restrictions.
- Approve any future DAM/CDN/optimization capability only through a separate implementation task.

## Open Questions

- Which media types, roles, sizes, aspect ratios, formats, and quality targets are approved?
- What rights, expiry, retention, deletion, privacy, and public/protected policies apply?
- What product-photography and technical-diagram standards are required?
- Which PDF/download types are public, protected, or internal?
- Who owns alt text, captions, transcripts, localization, and rights review?
- What evidence is required before a future CDN/DAM decision?

## Approval Status

Review. No media asset, filename change, folder, upload, image derivative, WebP conversion, video, PDF, CDN, DAM, plugin, Elementor/Blocksy component, storage rule, or processing code is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 07 enterprise media strategy; documentation only. |

## Related Documents

- [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md)
- [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- [Schema.org Strategy](31_SCHEMA_ORG_STRATEGY.md)
- [Content Types](32_CONTENT_TYPES.md)
- [SEO Entity Model](34_SEO_ENTITY_MODEL.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| MEDIA-001–MEDIA-009 | Product Media Set, CONTENT/ERM/CTYPE rules, CP-001–CP-006 | Schema and SEO entity models; future content operations | Asset inventory, rights, identity, access, lifecycle, naming, derivative, accessibility, localization, mobile performance, no-price, and protected-delivery validation |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Content and Entity Architecture Reading Path](READING_ORDER.md#content-and-entity-architecture-reading-path)
