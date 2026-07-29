# PD-02B validator fixtures

All fixtures in this directory are synthetic and have no canonical-data authority.
They exercise localized-label and approval-evidence validators without creating a
Product, SKU, slug, availability, runtime mapping, import, deployment, or
production effect.

- `valid-*` files are positive controls.
- `invalid-*` files are negative controls for missing/replayed evidence and
  Unicode confusables.
- `adversarial-*` files must be rejected as unsafe schemas.
- `mutation-cases.json` declares the fail-closed mutation matrix used by the
  Python test runner.
