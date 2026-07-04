# Enterprise Testing Checklist

## Purpose

Provide a reusable review standard for test scope, traceability, reliability, and evidence.

## Scope

Applies to automated and manual testing for code, configuration, documentation-sensitive behavior, integrations, migrations, and releases.

## Owner

TODO (Owner Assignment Required)

## Status

Draft

## Checklist

- [ ] Test cases trace to approved requirements, decisions, risks, or defects.
- [ ] Unit, integration, contract, end-to-end, and manual test levels are selected by risk.
- [ ] Test data is synthetic or appropriately protected and represents required scenarios.
- [ ] The test environment is sufficiently representative for the behavior under review.
- [ ] Supported platform and dependency combinations are covered according to the compatibility matrix.
- [ ] Critical journeys and state transitions have positive and negative coverage.
- [ ] Boundary conditions, failure handling, retries, and recovery paths are exercised.
- [ ] Relevant browsers, viewports, input methods, languages, and text directions are covered.
- [ ] Accessibility checks combine automated analysis with appropriate manual verification.
- [ ] Security and performance tests follow their dedicated standards rather than being implied by functional tests.
- [ ] Flaky, quarantined, skipped, and expected-failure tests are visible and owned.
- [ ] Test failures cannot be suppressed without an approved exception.
- [ ] Test reports identify the build, environment, data set, result, and execution time.

## Pass Criteria

Required risk-based coverage passes on the release candidate, results are reproducible, and skipped or unstable tests have approved disposition.

## Fail Criteria

The review fails when critical behavior is untested, failures are hidden, test data is unsafe, environments are unsuitable, or evidence cannot be reproduced.

## References

- [Enterprise Quality Standard](QUALITY_STANDARD.md)
- [Testing Strategy](../docs/13_TESTING_STRATEGY.md)
- [WordPress Automated Testing](https://make.wordpress.org/core/handbook/testing/automated-testing/)
- [WooCommerce Testing Guidance](https://developer.woocommerce.com/docs/contribution/testing)
