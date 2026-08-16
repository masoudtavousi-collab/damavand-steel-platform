# C002 Commercial Pilot Candidate Fixtures

These fixtures exercise the contract foundation without populating the canonical
candidate registry. `valid-synthetic.yaml` is test evidence only. It does not
select a Pilot, create a Product or SKU, assert availability, or authorize
commerce or Runtime.

The mutation manifest covers exact contract drift, deterministic evidence
evaluation at `evaluation_as_of`, temporal ordering, independent review,
coverage, Minimum Founder Data Packet completeness, readiness, seed references,
separate Product/SKU/Availability/projection/commerce states, authority
boundaries, and commercial-fact failures. `UNRESOLVED`, open conflicts and open
blockers are machine-visible and cannot yield `FOUNDER_SELECTION_READY` even at
nominal 9/9 evidence coverage.

The current C002 instance decision is strictly
`PENDING_FOUNDER_SELECTION` with a null decision reference and no recorded
selection effect. `FOUNDER_DECISION_RECORDED` is vocabulary-only for a future
contract revision and is rejected by the current instance schema.

Future separately authorized intake records may use the noncanonical
`FOUNDER_INTAKE_PROTECTED` classification with closed
`FOUNDER_EVIDENCE_PACKET` provenance captured by the Founder or an authorized
steward. This shape never changes the false authority boundary and cannot be
used in the empty canonical C002 registry or the synthetic classification.

Adversarial files prove strict duplicate-key loading, local-only references and
fail-closed schema auditing at nested object boundaries. The positive fixture is
synthetic and contains protected locators only; it carries no price, margin,
availability, Product, SKU, projection or commerce-activation claim.
