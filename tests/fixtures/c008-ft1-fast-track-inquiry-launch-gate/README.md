# C008-FT1 focused fixtures

These fixtures validate a separate, initially false Fast-Track Inquiry launch governance gate. They never modify C002, create Product/Variant/SKU truth, infer supplier or media evidence, or authorize Runtime, Staging, Production, publication, C009, M4, Merge or a successor Mission.

- `valid-synthetic.yaml` is a semantically distinct positive surface accepted only with `--synthetic`.
- `mutation-cases.json` is the counted fail-closed semantic mutation manifest.
- duplicate-key, permissive-schema and remote-reference fixtures exercise parser and schema-policy boundaries.
