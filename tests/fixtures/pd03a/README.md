# PD-03A Test Fixtures

These fixtures are offline test evidence only. They are not canonical Product,
Pilot, Master Data, Golden, SKU, availability, import, or runtime records.

- `valid-synthetic-foundation.yaml` records the expected extension shape used by
  tests without allocating canonical data.
- `valid-synthetic-pilot-combinations.yaml` exercises the three bounded tuples
  with synthetic identities, `CANDIDATE_UNVERIFIED` status, missing-availability
  semantics, historical non-identity references, and all readiness flags false.
- `adversarial-duplicate-keys.yaml` must fail before validation.
- `adversarial-permissive-schema.json` and
  `adversarial-remote-ref-schema.json` exercise the real schema loader.
- `mutation-cases.json` is dispatched by the test suite; every entry must reach
  a real validator and fail with the declared code.
- The manifest covers review head/base/artifact binding, deterministic nonce
  binding, Approval-ID collisions, exact roles/relationships/aliases, cross-file
  references, Contract tampering, duplicate/non-finite JSON, and nested
  implicit-true Schema branches.

No fixture may be promoted, imported, published, or copied into a canonical
Pilot registry.
