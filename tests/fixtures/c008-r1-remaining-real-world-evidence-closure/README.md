# C008-R1 focused fixtures

These fixtures exercise the delta-only remaining-evidence closure without creating supplier, media, Product, Availability, Price, Runtime, M4, or successor truth.

- `valid-synthetic.yaml` is a distinct positive surface accepted only with `--synthetic`.
- `mutation-cases.json` contains counted semantic mutations; every named case must dispatch and fail with its expected code.
- duplicate-key, permissive-schema, and remote-reference fixtures prove fail-closed parsing and schema controls.
