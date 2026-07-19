# Damavand Steel Project Bible — Repository Baseline

## Document control

- **Status:** Draft
- **Authority:** Repository baseline and Atlas context entry point
- **Owner and approval authority:** Founder
- **Canonical governing source:** [docs/00_PROJECT_BIBLE.md](docs/00_PROJECT_BIBLE.md)
- **Current-state source:** [docs/PROJECT_BASELINE.md](docs/PROJECT_BASELINE.md)
- **Approval:** Pending Founder reconciliation and approval

This root document supplies an explicit context entry point for repository tooling and the imported Atlas. It does not supersede the canonical Project Bible, accepted Founder decisions, or the source-of-truth priority. Conflicts are recorded as Open Questions rather than resolved by inference.

## Business purpose

Damavand Steel is an Enterprise Product and Knowledge Platform, not a conventional retail store. Its purpose is to organize governed product facts, technical and commercial knowledge, guided selection, inquiry conversion, and future controlled delivery through replaceable implementation systems.

The platform must make stainless-steel product discovery and inquiry clearer without fabricating availability, specifications, pricing, compatibility, or operational evidence.

## Damavand Steel and Central Steel

- `DamavandSteel.com` is the first planned implementation of the platform.
- `CentralSteel.ir` is a future ecosystem consumer, not the current source of truth.
- Shared architecture and approved data may be reused only through explicit governance and implementation decisions.
- No current task authorizes Central Steel runtime work, cross-site publishing, or a shared production database.

## Commercial model: Inquiry First

The initial commercial experience is inquiry-first:

- customers discover, compare, configure, and submit an inquiry;
- the business validates the request and handles quotation outside the public catalog flow;
- public prices, Offer schema, discounts, sale badges, cart, checkout, payment, and public quotation remain prohibited;
- technical presence or a generated combination never proves commercial availability; and
- publishing any commercial claim requires evidence and Founder approval.

## Product Data First and Taxonomy First

Product structure is established before page composition or runtime import.

- **Product Data First:** identity, family, approved attributes, variation rules, provenance, status, and operational gaps must be modeled before presentation.
- **Taxonomy First:** categories, attribute ownership, term identity, aliases, and relationships must be governed before product population.
- A Variable Parent Product represents a coherent product family or commercial product; theoretical Cartesian combinations are not automatically valid variations.
- Missing values remain missing. They must not be inferred from competitors, generated content, or technical possibility.

## Product Repository and Knowledge Repository

The platform separates two controlled authorities:

- **Product Repository:** product identity, hierarchy, attributes, variant logic, SKU readiness, commercial metadata, operational fields, and evidence-backed availability.
- **Knowledge Repository:** material, alloy, installation, maintenance, selection, FAQ, trust, comparison, and explanatory knowledge with provenance and review status.

Product facts must not be silently generated from explanatory content. Knowledge content must not override approved Product Repository facts. WordPress, WooCommerce, n8n, AI outputs, and generated pages are projections or orchestrators, never architectural truth.

## Product hierarchy

The imported Atlas planning baseline specifies:

```text
Catalog → Platform → Family → Series → Template → Variant → SKU
```

The current canonical enterprise-platform documents specify:

```text
Catalog → Platform → Family → Series → Variant Rules → SKU
```

Until the Founder resolves this vocabulary and mapping, the canonical `Variant Rules` model remains controlling for existing project assets. `Template` and `Variant` in the Atlas are planning concepts only and must not trigger migration, bulk generation, final SKU creation, or runtime implementation.

## Pricing architecture

- No public pricing is permitted initially.
- Cost, margin, calculation, internal pricing inputs, quotation inputs, and currency handling are internal operational concerns.
- Internal pricing architecture must be access-controlled, evidence-backed, auditable, and separated from public product presentation and schema.
- No formula, exchange-rate source, rounding rule, commission rule, margin, cost, or quote authority is approved merely because the Atlas contains planned pricing documents.

## Product configurator

The Product Configurator is a guided selection and inquiry-support capability. It may use approved product rules and knowledge to narrow choices, explain options, and assemble an inquiry payload.

It must not:

- expose or infer public prices;
- treat a Cartesian combination as available;
- generate a final SKU without approval;
- invent compatibility, installation, stock, or supply claims; or
- publish or create WooCommerce variations automatically.

Pipe configurator assets are ready for Founder review only. Profile and Glass remain blocked by missing data, and Pool remains deferred.

## CRM, representatives, installers, and introducers

Inquiry and relationship architecture may cover customers, leads, representatives, installers, introducers, notifications, satisfaction, warranty, assignments, and lifecycle events.

Existing business and Atlas assets are models or planned documents, not evidence of an implemented CRM, portal, commission system, user role, contractual relationship, geographic coverage, eligibility, or runtime integration. Identity, permissions, assignment rules, commercial terms, privacy, retention, and approval responsibilities require evidence and Founder decisions before implementation.

## WordPress and WooCommerce delivery platform

WordPress and WooCommerce are controlled delivery adapters, not the source of architectural truth.

- Blocksy Pro owns the target site shell.
- Elementor Pro owns delegated page-body composition.
- WooCommerce maps approved Variable Parent Products and valid variations.
- Native WordPress/WooCommerce capabilities are preferred before custom fields or custom implementation.
- Package presence, licenses, compatibility, target environment, backup, rollback, import, publishing, and production mutation remain separately gated.

No live WordPress, hosting, cPanel, database, plugin, theme, product, variation, page, or schema change is authorized by this document.

## SEO and AI engines

The SEO architecture may govern search intent, titles, metadata, internal links, canonical rules, entity mapping, and non-price schema. SEO outputs must remain traceable to approved product and knowledge sources and must never leak price or Offer data.

The Atlas includes a planned AI Engine domain for context, prompting, retrieval, generation, recommendation, governance, and evaluation. These are planning records only. Core Principle CP-010 still prohibits AI features in Phase 1; repository assistance does not authorize a public, autonomous, publishing, recommendation, or production AI capability.

## Persian RTL and Mobile First

- Persian language and RTL behavior are first-class requirements for public and Admin experiences.
- Mobile behavior is validated before desktop expansion.
- Taxonomy labels, forms, navigation, tables, configurators, inquiry flows, and generated content must remain usable in Persian RTL on constrained screens.

## Founder-controlled governance

The Founder is the final authority for business rules, canonical documents, commercial facts, lifecycle promotion, publication, deployment, and production access. ChatGPT acts as Chief Architect, Product Owner, and QA; Codex acts as the controlled Build Engine; n8n acts as Orchestrator. None may approve its own output or override the Founder.

Documentation precedes implementation. Chronology, provenance, accepted architecture, Founder decisions, source status, and unresolved questions must remain visible.

## Repository-first deployment workflow

Future changes follow this order:

1. Record the approved requirement, architecture, data, source, status, and acceptance criteria in the repository.
2. Work on a scoped branch; never mutate `main` directly.
3. Validate structure, dependencies, security, inquiry-only behavior, RTL/mobile behavior, and rollback implications.
4. Obtain Founder approval for staging, commit, push, pull request, merge, automation, import, publishing, and runtime as separate gates where applicable.
5. Before deployment, confirm the exact target, least-privilege access, verified backup and restore evidence, documented rollback, and post-change QA.
6. Project the approved repository state into WordPress or another delivery system through a reversible, limited scope.
7. Record evidence and outcomes back in the repository without rewriting chronology.

The current repository bootstrap, Atlas import, and inactive n8n workflow files do not authorize execution or deployment.

## Open Questions

1. How should Atlas `Template → Variant` map to the canonical `Variant Rules` model without changing existing architecture or IDs?
2. Which of the 173 pending Atlas documents should be adopted, mapped to existing documents, rejected as duplicates, or deferred?
3. What private pricing formulas, exchange-rate sources, rounding, margins, commissions, and quotation controls will be approved?
4. What are the approved CRM, representative, installer, introducer, assignment, privacy, retention, and commercial rules?
5. Which configurator combinations and compatibility rules have commercial evidence beyond the approved three-combination Pipe pilot?
6. What AI scope, if any, may be considered after Phase 1, with what data, evaluation, privacy, and human-review controls?
7. What GitHub baseline and branch/PR process will the Founder approve for the current dirty working tree?
8. What exact staging/production target, backup/restore proof, rollback owner, and Blocksy/Elementor license evidence will satisfy runtime gates?
9. How will the inactive n8n workflows enforce dry-run behavior, human approval, and external-write controls before any execution?
10. How should Atlas workflow statuses such as `pending`, `draft`, `review_required`, `approved`, `canonical`, and `rejected` map to the repository's governed document and ADR lifecycle vocabularies?
