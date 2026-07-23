# Damavand Steel

Canonical repository for the Damavand Steel Enterprise Product and Knowledge Platform. WordPress and WooCommerce are future controlled implementation layers, not the architectural source of truth. The commercial model is inquiry-first: public pricing, Offer schema, cart, checkout, and payment remain prohibited in the current phase.

## Start here

Every new contributor and AI session must read, in order:

1. [AGENTS.md](AGENTS.md)
2. [Current Project State](docs/CURRENT_PROJECT_STATE.md)
3. [Project Baseline](docs/PROJECT_BASELINE.md)
4. [Knowledge Archive Standard](docs/KNOWLEDGE_ARCHIVE_STANDARD.md)
5. [Repository Reading Order](docs/READING_ORDER.md)

Repository status, file presence, or named target components do not prove implementation, licensing, runtime readiness, or commercial approval.

## Repository control state

The mutable SHA, active branch, completed foundation waves, approved next action, and GO/NO-GO boundary are maintained only in [Current Project State](docs/CURRENT_PROJECT_STATE.md). Historical audits and older baselines preserve chronology but do not override that pointer.

Wave 2A–2C structural foundations now exist for Product core, Product Attributes, and measurements. They contain no canonical Product rows, approved Product Attribute definitions, final SKUs, Master Data, Golden package, WordPress implementation, import, publishing, or production authority.

## Repository map

- `public/` — deployable web root and versioned WordPress content
- `config/` — environment, web server, PHP, and WordPress templates
- `infrastructure/` — container and orchestration templates
- `docs/` — architecture, operations, content, SEO, security, and ADRs
- `prompts/` — versioned AI prompt templates
- `scripts/` — repository and data-foundation validation entry points
- `assets/` — source brand, media, font, and document assets
- `tests/` — QA, fixture, and end-to-end test scaffolding
- `repository/` — current Platform, Product Engine, Product Data, and Design proposals/scaffolds plus approved future canonical ownership boundaries; a named future directory is not an existing or implemented asset

Canonical ownership is `repository/data/contracts/`, `repository/data/schemas/`, `repository/data/registries/`, `repository/data/validation/`, future `repository/data/master-data/`, future `repository/data/golden-reference/`, future `repository/knowledge/`, future `repository/content/`, future `repository/implementation-assets/`, and adapter-only future `repository/wordpress/`. Existing foundation paths do not imply that the future data/content paths or their assets exist. WordPress, WooCommerce, imports, page builders, and runtime systems may consume canonical data but may never own Product or Knowledge truth.

## Important constraints

- WordPress core, uploads, dependencies, secrets, and commercial plugin archives are not committed.
- Blocksy Pro and Elementor Pro are target ownership boundaries; their exact packages, licenses, compatibility, and runtime approval remain evidence-gated.
- No custom plugin or theme implementation is included in this scaffold.
- Pricing, cart, checkout, and payment behavior must remain private until an ADR explicitly changes that policy.
- The three Golden Pipe identifiers are pilot references only, not final commercial SKUs.
- The separate `damavand-enterprise-repository` is isolated `QUARANTINED_ARCHITECTURE_RESEARCH` and has no Damavand Steel authority.

Runtime, import, publishing, deployment, product creation, bulk SKU generation, merge of any current Draft PR, and Factory implementation remain **NO-GO** without separate Founder approval. See [Current Project State](docs/CURRENT_PROJECT_STATE.md) for the exact current boundary and next action.
