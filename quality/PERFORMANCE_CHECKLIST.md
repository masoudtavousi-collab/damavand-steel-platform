# Enterprise Performance Checklist

## Purpose

Provide a reusable review standard for frontend, backend, database, integration, and capacity performance.

## Scope

Applies to changes that can affect latency, throughput, resource use, page weight, concurrency, or scalability.

## Owner

TODO (Owner Assignment Required)

## Status

Draft

## Checklist

- [ ] Applicable performance budgets and service objectives are identified before measurement.
- [ ] Baseline and candidate measurements use representative data, traffic, devices, and environments.
- [ ] User-facing latency and Core Web Vitals are measured where relevant.
- [ ] Server response time, throughput, errors, and resource consumption are evaluated.
- [ ] Database query count, duration, indexing impact, and data-growth sensitivity are reviewed.
- [ ] Cache layers, keys, exclusions, invalidation, and stampede risks are understood.
- [ ] Background tasks, queues, retries, and scheduled work are included in capacity analysis.
- [ ] Images, fonts, scripts, styles, markup, and generated assets are assessed for avoidable cost.
- [ ] Third-party requests have documented performance and failure impact.
- [ ] Concurrency limits, bottlenecks, and scaling assumptions are tested or explicitly recorded.
- [ ] Performance regressions are quantified and resolved or approved as exceptions.
- [ ] Measurement commands, tools, results, and interpretation are retained as review evidence.

## Pass Criteria

Measured behavior meets approved budgets and service objectives with representative evidence and no unexplained regression or capacity risk.

## Fail Criteria

The review fails when required baselines are absent, budgets are exceeded without approval, results are not reproducible, or scalability risks remain unassessed.

## References

- [Enterprise Quality Standard](QUALITY_STANDARD.md)
- [Architecture Checklist](ARCHITECTURE_CHECKLIST.md)
- [Web Vitals](https://web.dev/articles/vitals)
- [WordPress Performance Handbook](https://make.wordpress.org/performance/handbook/)
