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

Verified on 2026-07-20:

- The canonical branch is `main`, and the verified shared baseline is `4a0f229107716a1b9f7f825f5cd5f16ea78a1b26`.
- Bootstrap PR #1 is complete and merged through merge commit `530a4c46cc47bd02b794cfac1ef24eef56918e75`.
- Wave 1 Governance PR #2 is complete and merged through merge commit `4a0f229107716a1b9f7f825f5cd5f16ea78a1b26`.
- Wave 1 is complete. Wave 2 has not started and remains unauthorized pending separate Founder approval.
- All included n8n workflows remain inactive. No workflow execution, WordPress or Product Repository implementation, deployment, publication, or production mutation has occurred.
- GitHub still reports `codex/bootstrap-atlas-foundation` as the repository default branch. The intended default is `main`; changing repository settings requires separate Founder approval.

Historically, the 2026-07-19 Wave 1 authorization allowed one scoped governance commit, branch push, and Draft PR while merge remained prohibited. That sequence and its separately approved merge are now complete. It granted no Wave 2, runtime, WordPress, product, publication, deployment, production, or repository-settings authority.

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

Runtime, import, publishing, deployment, product creation, bulk SKU generation, any further repository merge, and Factory implementation remain **NO-GO** without separate Founder approval. See the [Project Baseline](docs/PROJECT_BASELINE.md) for the exact current boundary.
