# Blocksy Quality Checklist

## Purpose

Provide a reusable review standard for Blocksy theme and companion compatibility without selecting project-specific features.

## Scope

Applies to Blocksy, Blocksy Companion, Blocksy Pro, child-theme changes, theme settings, and supported integrations.

## Owner

TODO (Owner Assignment Required)

## Status

Draft

## Checklist

- [ ] Approved Blocksy theme, Companion, and Pro versions are documented together.
- [ ] The parent theme remains vendor-controlled and unmodified.
- [ ] Project-owned theme changes are isolated in the approved child-theme boundary.
- [ ] Child-theme overrides are necessary, minimal, and checked against the current parent template.
- [ ] Responsibility boundaries between Blocksy, WordPress, WooCommerce, and page-builder features are explicit.
- [ ] Theme and Customizer settings have a reproducible capture or migration process.
- [ ] Vendor-supported hooks and extension points are preferred over fragile markup overrides.
- [ ] Enabled commerce modules comply with approved business and data-visibility rules.
- [ ] Schema ownership is reviewed to prevent conflicting or duplicated output.
- [ ] Responsive, RTL, localization, keyboard, and focus behavior are verified where affected.
- [ ] Updates are tested in a representative non-production environment before release.
- [ ] Package provenance, license status, renewal ownership, and update access are documented.

## Pass Criteria

The change is compatible with approved Blocksy versions, preserves vendor updateability, respects feature ownership, and has reproducible settings and review evidence.

## Fail Criteria

The review fails when parent files are changed, ownership conflicts are unresolved, settings cannot be reproduced, or vendor compatibility is unverified.

## References

- [Enterprise Quality Standard](QUALITY_STANDARD.md)
- [WordPress Quality Checklist](WORDPRESS_CHECKLIST.md)
- [WooCommerce Quality Checklist](WOOCOMMERCE_CHECKLIST.md)
- [Blocksy Documentation](https://creativethemes.com/blocksy/docs/)
- [Blocksy Child Theme Guidance](https://creativethemes.com/blocksy/docs/getting-started/child-theme/)
