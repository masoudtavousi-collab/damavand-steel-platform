# WooCommerce Quality Checklist

## Purpose

Provide a reusable review standard for WooCommerce compatibility, data integrity, extensibility, and operations.

## Scope

Applies to WooCommerce core, extensions, product and order behavior, APIs, templates, scheduled actions, and data migrations.

## Owner

TODO (Owner Assignment Required)

## Status

Draft

## Checklist

- [ ] Supported WooCommerce and WordPress versions are present in the approved compatibility matrix.
- [ ] The change traces to approved business rules without creating new commerce behavior.
- [ ] WooCommerce public CRUD APIs are used instead of direct storage assumptions where applicable.
- [ ] High-Performance Order Storage compatibility is declared and verified when relevant.
- [ ] Action Scheduler jobs are idempotent, observable, and recoverable when relevant.
- [ ] Store API and REST API exposure is reviewed against approved data-visibility rules.
- [ ] Product, customer, inquiry, and order data changes preserve integrity and migration safety.
- [ ] Theme or template overrides are minimized, version-tracked, and compatibility-tested.
- [ ] Session, cache, and personalized-response behavior is reviewed.
- [ ] Structured data and public commerce output match approved SEO and business rules.
- [ ] Extension dependencies, licenses, provenance, and support status are recorded.
- [ ] WooCommerce status diagnostics and scheduled actions contain no unexplained critical failure.

## Pass Criteria

The change is compatible with the approved WooCommerce matrix, preserves data integrity, follows public APIs, and implements only authorized commerce behavior.

## Fail Criteria

The review fails when compatibility, data exposure, storage behavior, migration safety, scheduled work, or business-rule traceability is unresolved.

## References

- [Enterprise Quality Standard](QUALITY_STANDARD.md)
- [WordPress Quality Checklist](WORDPRESS_CHECKLIST.md)
- [WooCommerce Server Recommendations](https://woocommerce.com/document/server-requirements/)
- [WooCommerce Extension Compatibility](https://developer.woocommerce.com/docs/extensions/best-practices-extensions/compatibility)
- [WooCommerce HPOS Documentation](https://developer.woocommerce.com/docs/features/high-performance-order-storage)
