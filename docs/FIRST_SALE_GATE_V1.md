# Damavand Steel — First Sale Gate v1

**Date:** 2026-09-08
**Authority:** Founder-approved execution preparation
**Scope:** First real online sale readiness

## Purpose

Move the site from technical WooCommerce readiness to the first verifiable real purchase without inventing product or commercial data.

## Gates

### G0 — Commerce policy
- Current public pricing policy must be explicit and canonical before publication.
- No product may become publicly purchasable merely because a planning record or draft exists.
- Product/SKU data must be backed by confirmed Product Data.

### G1 — Product truth
Each first-sale SKU must have:
- exact product name
- material / grade where applicable
- exact dimensions / size
- finish / color where applicable
- exact SKU
- unit of sale
- stock quantity or explicit stock policy
- verified product image when available

### G2 — Commercial truth
Each purchase SKU must have:
- confirmed public price
- confirmed pricing unit
- confirmed sales quantity rules
- confirmed shipping / fulfillment rule
- confirmed tax treatment if applicable

### G3 — Checkout
- Cart page configured
- Checkout page configured
- My Account page configured
- Terms page configured
- Payment gateway credentials verified
- Customer contact fields validated

### G4 — Runtime verification
Perform, in order:
1. product selection
2. add to cart
3. cart totals
4. checkout validation
5. gateway handoff
6. payment callback / order creation
7. order status verification
8. customer-facing confirmation

### G5 — Production release
Only after G0–G4 pass:
- remove launch gating / Coming Soon only with explicit release authority
- publish the verified first-sale SKU(s)
- run a final smoke test

## Known current blockers

- Real public price data has not yet been supplied for the recovered product candidates.
- Real stock quantities have not yet been supplied.
- SKU codes have not yet been supplied.
- Exact unit of sale and fulfillment rules are incomplete.
- Zibal gateway is installed but disabled and currently has no merchant code configured.

## Safe current state

All newly created product candidates remain drafts. No production sale is claimed or enabled by this document.
