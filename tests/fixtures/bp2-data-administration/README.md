# BP2 Data Administration Fixtures

These fixtures exercise the BP2 data administration contract without duplicating
the canonical contract as a second source of truth.

- `mutation-cases.json` applies synthetic mutations to deep copies of the
  canonical contract, schema, or source blueprint.
- Raw JSON fixtures cover parser-level and schema-tampering cases that cannot be
  represented safely as parsed mutation values.
- All data is synthetic and contains no production, customer, credential, or
  commercially inferred values.

Every invalid or adversarial case must fail with a stable error code and without
a Python traceback.
