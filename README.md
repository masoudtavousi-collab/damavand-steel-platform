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

- The canonical and GitHub default branch is `main`, and the verified shared baseline is `d702c5217f7caa2f23e56f965f3f993967e3c17d`.
- Bootstrap PR #1 is complete and merged through merge commit `530a4c46cc47bd02b794cfac1ef24eef56918e75`.
- Wave 1 Governance PR #2 is complete and merged through merge commit `4a0f229107716a1b9f7f825f5cd5f16ea78a1b26`.
- Post-merge Governance Reconciliation PR #3 is complete and merged through merge commit `d702c5217f7caa2f23e56f965f3f993967e3c17d`.
- Wave 1 and the read-only Wave 2 kickoff discovery are complete. Wave 2 implementation has not started; Wave 2A is proposed and requires separate Founder authorization after this governance reconciliation is reviewed and merged.
- Main-branch protection is enabled with administrator enforcement, strict/up-to-date checks, required check `repository-validation`, force-push disabled, and branch deletion disabled.
- All included n8n workflows remain inactive. No workflow execution, WordPress or Product Repository implementation, deployment, publication, or production mutation has occurred.

Historically, the 2026-07-19 Wave 1 authorization allowed one scoped governance commit, branch push, and Draft PR while merge remained prohibited. That sequence and its separately approved merge are complete. Later approvals separately authorized PR #3, default-branch correction, main protection, Wave 2 discovery, and this documentation-only reconciliation; none authorizes Wave 2A implementation, runtime, WordPress, product creation, publication, deployment, or production mutation.

## Repository map

- `public/` — deployable web root and versioned WordPress content
- `config/` — environment, web server, PHP, and WordPress templates
- `infrastructure/` — container and orchestration templates
- `docs/` — architecture, operations, content, SEO, security, and ADRs
- `prompts/` — versioned AI prompt templates
- `scripts/` — operational script placeholders
- `assets/` — source brand, media, font, and document assets
- `tests/` — QA, fixture, and end-to-end test scaffolding
- `repository/` — current Platform, Product Engine, Product Data, and Design proposals/scaffolds plus approved future canonical ownership boundaries; a named future directory is not an existing or implemented asset

Canonical future ownership is `repository/data/contracts/`, `repository/data/schemas/`, `repository/data/registries/`, `repository/data/validation/`, `repository/data/master-data/`, `repository/data/golden-reference/`, `repository/knowledge/`, `repository/content/`, `repository/implementation-assets/`, and adapter-only `repository/wordpress/`. These paths may be created only by a separately approved implementation sprint. WordPress, WooCommerce, imports, page builders, and runtime systems may consume canonical data but may never own Product or Knowledge truth.

## Important constraints

- WordPress core, uploads, dependencies, secrets, and commercial plugin archives are not committed.
- Blocksy Pro and Elementor Pro are target ownership boundaries; their exact packages, licenses, compatibility, and runtime approval remain evidence-gated.
- No custom plugin or theme implementation is included in this scaffold.
- Pricing, cart, checkout, and payment behavior must remain private until an ADR explicitly changes that policy.
- The three Golden Pipe identifiers are pilot references only, not final commercial SKUs.
- The separate `damavand-enterprise-repository` is isolated `QUARANTINED_ARCHITECTURE_RESEARCH` and has no Damavand Steel authority.

Runtime, import, publishing, deployment, product creation, bulk SKU generation, Wave 2A implementation, merge of the current Draft PR, and Factory implementation remain **NO-GO** without separate Founder approval. The approved next action is Founder review and merge decision for this documentation reconciliation PR, followed only then by a separate Wave 2A authorization decision. See the [Project Baseline](docs/PROJECT_BASELINE.md) for the exact current boundary.
