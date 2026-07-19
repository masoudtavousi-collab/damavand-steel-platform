# Damavand Steel

Canonical repository for the Damavand Steel Enterprise Product and Knowledge Platform. WordPress and WooCommerce are future controlled implementation layers, not the architectural source of truth. The commercial model is inquiry-first: public pricing, Offer schema, cart, checkout, and payment remain prohibited in the current phase.

## Start here

Every new contributor and AI session must read, in order:

1. [AGENTS.md](AGENTS.md)
2. [Project Baseline](docs/PROJECT_BASELINE.md)
3. [Repository Reading Order](docs/READING_ORDER.md)
4. [Current Project State](docs/CURRENT_PROJECT_STATE.md)

Repository status, file presence, or named target components do not prove implementation, licensing, runtime readiness, or commercial approval.

## Repository control state

Verified on 2026-07-19:

- Remote `main` exists at `96f2ea70f9010fce416a18310e98915e2be537b9`.
- The Atlas bootstrap commit is `b20e95de8b1b67d2bc610130648700e82a6855b3`.
- Draft PR #1 remains open and unmerged with exactly 24 approved bootstrap paths.
- Class B Wave 1 is limited to 19 governance and repository-control paths on `codex/class-b-wave-01-governance`.
- Class B Waves 2–10 remain local, unstaged, unapproved, and outside Wave 1.
- All included n8n workflows remain inactive. No workflow execution, deployment, publication, or production mutation has occurred.

Wave 1 authorizes only its controlled documentation reconciliation, one scoped commit, branch push, and Draft PR. It does not authorize merge, runtime, WordPress, content, product, publication, deployment, or production work.

## Repository map

- `public/` — deployable web root and versioned WordPress content
- `config/` — environment, web server, PHP, and WordPress templates
- `infrastructure/` — container and orchestration templates
- `docs/` — architecture, operations, content, SEO, security, and ADRs
- `prompts/` — versioned AI prompt templates
- `scripts/` — operational script placeholders
- `assets/` — source brand, media, font, and document assets
- `tests/` — QA, fixture, and end-to-end test scaffolding
- `repository/` — enterprise platform, product, knowledge, Master Data, design, content, configurator, and implementation-preparation assets

## Important constraints

- WordPress core, uploads, dependencies, secrets, and commercial plugin archives are not committed.
- Blocksy Pro and Elementor Pro are target ownership boundaries; their exact packages, licenses, compatibility, and runtime approval remain evidence-gated.
- No custom plugin or theme implementation is included in this scaffold.
- Pricing, cart, checkout, and payment behavior must remain private until an ADR explicitly changes that policy.
- The three Golden Pipe identifiers are pilot references only, not final commercial SKUs.
- The separate `damavand-enterprise-repository` is isolated `QUARANTINED_ARCHITECTURE_RESEARCH` and has no Damavand Steel authority.

Runtime, import, publishing, deployment, product creation, bulk SKU generation, repository merge, and Factory implementation remain **NO-GO**. See the [Project Baseline](docs/PROJECT_BASELINE.md) for the exact current boundary.
