# BP1 Visible Local Prototype

## Status and authority

- **Scope:** BP1 visible local prototype only.
- **Runtime:** local static files served on `127.0.0.1`.
- **Data:** demonstration fixture; non-canonical and not publishable.
- **External effects:** none. No API, form submission, storage, analytics, WordPress, or production connection.
- **Architecture boundary:** the header, navigation, footer, archive shell, and product shell preview future Blocksy ownership. Delegated page-body sections preview future Elementor ownership.

This prototype does not approve final colors, typography, copy, media, Product data, WordPress configuration, Blocksy configuration, Elementor templates, or runtime technology.

## Start

From the repository root:

```sh
python3 -m http.server 4173 \
  --bind 127.0.0.1 \
  --directory prototypes/bp1-visible-local
```

Open:

```text
http://127.0.0.1:4173/
```

## Stop

Press `Control-C` in the terminal running the local server.

## Validate

```sh
python3 prototypes/bp1-visible-local/tests/validate_bp1.py
make test
git diff --check
```

## Review route

1. Homepage
2. Main navigation
3. Pipes landing
4. Representative Pipe page
5. Inquiry CTA preview

Review at minimum at 360 px and a desktop viewport, with keyboard-only navigation and reduced-motion enabled.

## Fixture policy

`fixtures/representative-pipe.json` is a UI fixture, not Product Master Data.

- It contains no SKU, price, stock, availability, brand, origin, certification, performance, compatibility, or commercial combination.
- Technical values render as `نیازمند تأیید`.
- It must not be imported, synchronized, published, or treated as an approved Product.

## Rollback

Stop the local server and revert the BP1 commit. No database, remote service, browser storage, or external state is created.
