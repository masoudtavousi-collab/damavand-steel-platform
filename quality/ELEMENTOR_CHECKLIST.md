# Elementor Quality Checklist

## Purpose

Provide a reusable review standard for Elementor and Elementor Pro compatibility, content portability, security, and performance.

## Scope

Applies to Elementor core, Elementor Pro, templates, generated assets, forms, global settings, and supported integrations.

## Owner

TODO (Owner Assignment Required)

## Status

Draft

## Checklist

- [ ] Approved Elementor and Elementor Pro versions are recorded as a compatible pair.
- [ ] Runtime, browser, memory, and PHP-extension requirements are verified.
- [ ] Ownership of headers, footers, archives, templates, styles, and schema is unambiguous.
- [ ] Global design tokens are used according to approved design governance.
- [ ] Generated CSS, files, cache, and writable-path behavior is supported by the deployment model.
- [ ] Templates, kits, and settings have a tested export, import, or migration process.
- [ ] URL changes use a supported replacement and generated-data regeneration procedure.
- [ ] Form storage, notifications, webhooks, consent, and personal-data handling follow approved rules.
- [ ] Custom code, scripts, and third-party widgets are reviewed for necessity and safety.
- [ ] Responsive, RTL, localization, keyboard, and editor behavior are tested where affected.
- [ ] Security headers and frame policies remain compatible with the editor without weakening public controls unnecessarily.
- [ ] Feature flags and experiments are recorded and tested before promotion.
- [ ] Updates and license behavior are validated in an approved staging context.
- [ ] Page weight, DOM growth, asset loading, and cache impact remain within approved budgets.

## Pass Criteria

The change is compatible with the approved Elementor pair, preserves content portability and editor operation, and meets applicable security and performance standards.

## Fail Criteria

The review fails when version pairing, generated assets, migration, data handling, feature ownership, editor security, or performance impact is unresolved.

## References

- [Enterprise Quality Standard](QUALITY_STANDARD.md)
- [Blocksy Quality Checklist](BLOCKSY_CHECKLIST.md)
- [Performance Checklist](PERFORMANCE_CHECKLIST.md)
- [Elementor System Requirements](https://elementor.com/help/requirements/)
- [Elementor Developer Documentation](https://developers.elementor.com/)
