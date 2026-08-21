# Product Data Strategy

## Purpose

Define the strategy-level ownership, lifecycle, provenance, and promotion boundary
for Product Data while directing detailed truth to canonical contracts, registries,
models, and C006 semantic architecture.

## Scope

This Draft covers Product identity and hierarchy, controlled values, Variant Rules,
technical evidence, lifecycle, projections, and their separation from dynamic Mass,
Availability, supplier evidence, Price, Knowledge, Media, and Service. It creates
no Product, value, tuple, SKU, commercial, import, or Runtime record.

## Status

Draft

## Owner

Founder

## Reviewer

Repository Guardian

## Approval Authority

Founder

## Version

0.2.0

## Last Updated

2026-08-21

## Last Review

2026-08-21

## Strategy Baseline

- The repository is the canonical Product truth owner. The hierarchy is
  `Catalog → Platform → Family → Series → Variant Rules → SKU`.
- Product identity, derived technical data, dynamic commercial evidence,
  Knowledge, Service, and operator-internal context remain separate truth classes.
- Brand identity and Brand provenance are linked but distinct responsibilities;
  supplier or manufacturer identity is never inferred.
- Product Experience and WooCommerce consume approved references as projections;
  neither may write back or become canonical Product authority.
- Product and controlled-value promotion requires closed contracts, provenance,
  lifecycle review, independent validation, and separate authorization. No
  Cartesian tuple generation is allowed.

Detailed owners are [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md),
[Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute
Model](22_PRODUCT_ATTRIBUTE_MODEL.md), the governed `repository/data/` contracts
and registries, and [C006 Scope](C006_PRODUCT_DATA_SEMANTIC_PRODUCT_EXPERIENCE_ARCHITECTURE_SCOPE_V1.0.md).

`MISSING_AUTHORITY_INPUT` — exact input: the separately authorized Product and
Variant Rules promotion packet for the first bounded commercial slice, including
approved identities, values, evidence, owners, and qualified reviews. It is missing
because C002 readiness remains `0/9 / NOT_READY` and C007 is documentation-only.
Affected domain/document: Product Data Strategy and canonical Product owners. Safe
behavior without it: preserve existing approved records, create no Product/SKU or
tuple, and keep all commercial/Runtime projections inactive.

Original `Placeholder Sections` disposition: `RESOLVED_FROM_CANONICAL_EVIDENCE`;
the unsupported promotion decision above remains explicitly gated.

## Related Documents

- [Business Rules](03_BUSINESS_RULES.md)
- [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md)
- [Open Questions](18_OPEN_QUESTIONS.md)
- [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md)
- [C006 Product Data and Product Experience Scope](C006_PRODUCT_DATA_SEMANTIC_PRODUCT_EXPERIENCE_ARCHITECTURE_SCOPE_V1.0.md)
- [C007 Governance Convergence Scope](C007_GOVERNANCE_CONVERGENCE_PHASE1_ARCHITECTURE_BASELINE_SCOPE_V1.0.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md)
