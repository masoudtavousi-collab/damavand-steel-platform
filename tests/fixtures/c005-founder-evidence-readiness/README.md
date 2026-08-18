# C005 adversarial fixtures

These fixtures exercise the bounded C005 evidence/readiness validator. They contain no Product, SKU, Availability, price, Mass, supply, Customer, Order, VIP, Loyalty, Runtime, WordPress, WooCommerce, deployment, or successor population.

- `mutation-cases.json`: 66 deterministic fail-closed mutations against the canonical package, including exact source/owner bindings, Photo-vs-Text substates, supplementary planning provenance, evidence-path ranking and explicit no-promotion adversaries.
- `adversarial-duplicate-keys.yaml`: duplicate-key rejection.
- `adversarial-duplicate-keys.json`: duplicate-key rejection for schema JSON.
- `adversarial-permissive-schema.json`: nested open-object rejection.
- `adversarial-remote-ref-schema.json`: remote-reference rejection.
