# C003 Founder Discovery fixtures

These fixtures exercise the closed C003 evidence package without creating a
second 115-record source of truth. `valid-synthetic.yaml` is a test-control
manifest that points to the canonical evidence package; mutation tests deep-copy
that package in memory. Adversarial files test duplicate-key, permissive-schema,
and remote-reference rejection. No fixture is Product, SKU, Availability,
pricing, runtime, or commerce evidence.
