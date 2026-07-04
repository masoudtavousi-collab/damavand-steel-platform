# SEO Quality Checklist

## Purpose

Provide a reusable review standard for technical and content-facing SEO controls without defining project keywords or content strategy.

## Scope

Applies to crawlability, indexability, URLs, metadata, structured data, internal links, redirects, sitemaps, and environment behavior.

## Owner

TODO (Owner Assignment Required)

## Status

Draft

## Checklist

- [ ] SEO behavior traces to approved requirements and content ownership.
- [ ] Crawl and index controls are correct for the target environment.
- [ ] Canonical URLs are deterministic and do not conflict with redirects or index rules.
- [ ] Titles, descriptions, headings, and language metadata are structurally valid where affected.
- [ ] Structured-data ownership is explicit and duplicate schema generators are avoided.
- [ ] Structured data contains only visible, accurate, and approved information.
- [ ] XML sitemap inclusion and exclusion behavior is verified.
- [ ] Robots directives and `robots.txt` behavior are tested independently.
- [ ] Redirects preserve intent, avoid loops, and have an accountable source.
- [ ] URL, slug, pagination, filter, and parameter behavior is reviewed for duplicate-content risk.
- [ ] Internal links remain valid and preserve the approved information hierarchy.
- [ ] Localization and alternate-language signals are verified when applicable.
- [ ] Search-console or equivalent validation evidence is attached when available and applicable.

## Pass Criteria

The affected pages are crawlable and indexable only as intended, metadata and structured data are accurate, and no unresolved duplication or redirect defect remains.

## Fail Criteria

The review fails when index behavior, canonicalization, schema accuracy, redirects, sitemaps, or content traceability is incorrect or unverified.

## References

- [Enterprise Quality Standard](QUALITY_STANDARD.md)
- [SEO Strategy](../docs/11_SEO_STRATEGY.md)
- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Google Structured Data Guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
