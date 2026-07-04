# Damavand Steel

Production repository scaffold for a Persian, RTL, mobile-first, SEO-first WordPress and WooCommerce website using Blocksy Pro and Elementor Pro. The commercial model is inquiry-first: public prices and direct checkout are intentionally out of scope.

## Repository map

- `public/` — deployable web root and versioned WordPress content
- `config/` — environment, web server, PHP, and WordPress templates
- `infrastructure/` — container and orchestration templates
- `docs/` — architecture, operations, content, SEO, security, and ADRs
- `prompts/` — versioned AI prompt templates
- `scripts/` — operational script placeholders
- `assets/` — source brand, media, font, and document assets
- `tests/` — QA, fixture, and end-to-end test scaffolding

## Important constraints

- WordPress core, uploads, dependencies, secrets, and commercial plugin archives are not committed.
- Blocksy Pro and Elementor Pro require valid licenses and an approved private distribution process.
- No custom plugin or theme implementation is included in this scaffold.
- Pricing, cart, checkout, and payment behavior must remain private until an ADR explicitly changes that policy.

Start with [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md) and record consequential decisions in `docs/adr/`.
