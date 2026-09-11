# Product Sales Availability Control — V1.0

**Date:** 2026-09-08  
**Authority:** Founder-approved runtime direction  
**Status:** Proposed implementation contract

## Purpose

Provide a simple Founder-controlled mechanism to remove an individual product or variation/SKU from active sale without deleting the catalog record.

## Required states

- `ACTIVE`: eligible to appear in the sellable catalog when required commercial data is complete.
- `DISABLED`: retained in the catalog but excluded from new purchase flows.

## Required behavior

Disabling a product/SKU MUST NOT delete:

- product identity
- SKU identity
- media
- technical specifications
- SEO metadata
- historical order relationships
- audit/history information

Re-enabling MUST restore the product/SKU to its previous sellable state subject to current stock and commercial validation.

## Hybrid Commerce

Commerce mode is independently represented:

- `PURCHASE`: may use public price, cart and checkout when commercial requirements are complete.
- `INQUIRY`: uses inquiry flow and does not expose public purchase controls.

Sales availability MUST NOT be conflated with commerce mode.

## Fail-closed rule

A product may be marked `ACTIVE` in the product registry by Founder decision, but the storefront MUST NOT expose a successful purchase flow unless the SKU has the required validated commercial fields (at minimum: identity/SKU, price where applicable, and stock/fulfillment state sufficient for the configured checkout rules).

Missing data MUST remain missing; no placeholder price, stock or supplier may be invented.

## Authorization boundary

The sales-availability control is Founder-controlled and MUST NOT be writable by a user merely because that user can edit a WooCommerce product.

The implementation uses a dedicated WordPress capability:

- `manage_damavand_sales_availability`

The capability is granted to the WordPress `administrator` role when the plugin is activated and removed from that role when the plugin is deactivated. Product and variation saves require both the normal object-edit permission and this dedicated capability.

Variation-level writes occur through WooCommerce's normal product-save flow. WooCommerce verifies the enclosing product-edit nonce before dispatching its product/variation save actions; the plugin therefore relies on that established nonce boundary rather than introducing a second per-variation nonce contract. The plugin-specific authorization boundary remains independent of that nonce validation.

## Implementation preference

Prefer configuration/plugin-based WordPress administration over custom theme code. The control should be available from the product administration surface with a clear label such as **وضعیت فروش: فعال / غیرفعال**.

Where variations exist, the same control must be available at variation/SKU level.

## Current projection state

The first recovered WooCommerce parent records use internal metadata flags:

- `_ds_sales_enabled=yes`
- `_ds_commerce_mode=purchase`
- `_ds_data_status=candidate`

These flags are implementation scaffolding only and are not canonical Product Truth. Final canonical Product Data remains governed outside WooCommerce.
