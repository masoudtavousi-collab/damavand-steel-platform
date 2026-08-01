# PD-03B Test Fixtures

These files are negative and adversarial test inputs for the exact three-record
PD-03B canonical pilot validator. They are never canonical data, approval
evidence, Product/SKU records, Master Data, Golden data, import assets, or
runtime inputs. The only canonical PD-03B records live under
`repository/data/registries/extensions/pd03b/` and remain lifecycle-gated.

`mutation-cases.json` is the counted dispatch contract. Every listed mutation
must execute and fail closed; a listed but undispatched case fails the suite.
