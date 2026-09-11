# Founder Amendment — Hybrid Commerce & Sellable Default

**Date:** 2026-09-08  
**Authority:** Founder decision in active project conversation

## Effective business rule

Damavand Steel uses a Hybrid Commerce model. Products may be sold online when enabled for purchase; products that are not currently suitable for online purchase may be switched to an inquiry state or disabled from sale without deleting the catalog record.

## Sellable default

All currently collected product candidates in the following families are **sellable/active by default** unless the Founder later changes the status:

- Pipes
- Profiles
- Fittings / hardware (یراق)
- Miscellaneous fittings and related accessories (یراق متفرقه)

This default applies to newly admitted candidates as well as the existing collected candidate set, subject to the product data completeness rules.

## Product administration requirement

The runtime Product Administration surface must provide a Founder-controlled sales availability switch:

- Active / Sellable: product can be presented for purchase when its commerce mode is PURCHASE.
- Disabled: product remains in the catalog and retains its product identity, media, SEO, and historical order relationships, but is not available for new sale.

Where a product has variations/SKUs, the availability control must support variation/SKU-level disabling without deleting the parent product.

## Separation of concerns

Sales availability is separate from product-data completeness and from commerce mode. Missing technical data must never be invented merely to make a candidate sellable in the registry.

## Implementation boundary

This amendment authorizes reconciliation of the canonical project state and planning for runtime implementation. It does not itself claim that WordPress/WooCommerce has been mutated, that products have been created in production, or that the public launch has occurred.
