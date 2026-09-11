# Damavand Steel Sales Availability Control

This plugin is the runtime implementation candidate for `docs/PRODUCT_SALES_AVAILABILITY_CONTROL_SPEC_V1.0.md`.

## Scope

- Founder-controlled product sales switch: `وضعیت فروش: فعال / غیرفعال`.
- Variation/SKU-level switch for variable products.
- Explicit `no` blocks purchasability and new add-to-cart flows without deleting the catalog record.
- Missing product sales metadata follows the Founder-approved active-by-default policy; malformed explicit states fail closed.
- `_ds_commerce_mode` and `_ds_data_status` are read-only to this plugin and are never rewritten.
- The plugin never creates or changes SKU, price, stock, supplier, shipping promise, order, or payment data.

## Placement

Install only as a standalone plugin under WordPress `wp-content/plugins/`. It intentionally contains no theme or Elementor dependency.

## Validation

Run the focused offline contract test:

```sh
python3 tests/test_sales_availability_control.py
```

Full repository validation remains governed by the existing `make validate` / `make test` suite and CI. No validator bypass is permitted.

## Production posture

This repository change is a review candidate only. It does not authorize installation, activation, product publication, merge, deployment, or public launch.
