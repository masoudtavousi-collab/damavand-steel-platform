#!/usr/bin/env python3
"""Fail-closed structural validation for the BP1 static prototype."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = (
    ROOT / "index.html",
    ROOT / "pipes" / "index.html",
    ROOT / "pipes" / "representative-pipe" / "index.html",
)
REQUIRED_FILES = HTML_FILES + (
    ROOT / "README.md",
    ROOT / "fixtures" / "representative-pipe.json",
    ROOT / "assets" / "css" / "tokens.css",
    ROOT / "assets" / "css" / "base.css",
    ROOT / "assets" / "css" / "components.css",
    ROOT / "assets" / "css" / "pages.css",
    ROOT / "assets" / "js" / "prototype.js",
)
PROHIBITED_TERMS = (
    "add to cart",
    "checkout",
    "aggregateoffer",
    "pricecurrency",
    "pricevaliduntil",
    "availability",
)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[oprsu]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
)


class PrototypeParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.html_attrs: dict[str, str | None] = {}
        self.links: list[str] = []
        self.forms = 0
        self.external_resources: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.html_attrs = attributes
        if tag == "form":
            self.forms += 1
        if identifier := attributes.get("id"):
            self.ids.add(identifier)

        reference = attributes.get("href") if tag in {"a", "link"} else attributes.get("src")
        if reference:
            if tag == "a":
                self.links.append(reference)
            parsed = urlparse(reference)
            if parsed.scheme in {"http", "https", "ws", "wss"} or reference.startswith("//"):
                self.external_resources.append(reference)


def fail(message: str) -> None:
    print(f"BP1 VALIDATION FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


for required_file in REQUIRED_FILES:
    if not required_file.is_file():
        fail(f"missing required file: {required_file.relative_to(ROOT)}")

scanned_files = HTML_FILES + tuple((ROOT / "assets").rglob("*.*"))
all_text = "\n".join(path.read_text(encoding="utf-8") for path in scanned_files)
lower_text = all_text.lower()

for term in PROHIBITED_TERMS:
    if term in lower_text:
        fail(f"prohibited commerce/runtime term found: {term}")

for pattern in SECRET_PATTERNS:
    if pattern.search(all_text):
        fail(f"possible secret found: {pattern.pattern}")

for html_file in HTML_FILES:
    source = html_file.read_text(encoding="utf-8")
    parser = PrototypeParser()
    parser.feed(source)

    if parser.html_attrs.get("lang") != "fa" or parser.html_attrs.get("dir") != "rtl":
        fail(f"{html_file.relative_to(ROOT)} must use lang=fa and dir=rtl")
    if parser.forms:
        fail(f"{html_file.relative_to(ROOT)} contains an active form")
    if parser.external_resources:
        fail(f"{html_file.relative_to(ROOT)} contains external resources: {parser.external_resources}")
    if "main" not in parser.ids or "main-navigation" not in parser.ids:
        fail(f"{html_file.relative_to(ROOT)} is missing required landmark IDs")
    if 'name="robots" content="noindex,nofollow,noarchive"' not in source:
        fail(f"{html_file.relative_to(ROOT)} must be explicitly non-indexable")

    for link in parser.links:
        parsed = urlparse(link)
        if parsed.scheme or link.startswith(("#", "mailto:", "tel:")):
            continue
        target = (html_file.parent / parsed.path).resolve()
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            fail(f"broken local link in {html_file.relative_to(ROOT)}: {link}")

fixture = json.loads((ROOT / "fixtures" / "representative-pipe.json").read_text(encoding="utf-8"))
if fixture.get("canonical") is not False or fixture.get("publishable") is not False:
    fail("fixture must remain non-canonical and non-publishable")
if fixture.get("status") != "CANDIDATE_UNVERIFIED":
    fail("fixture must use CANDIDATE_UNVERIFIED status")
if len(fixture.get("facts", [])) != 5:
    fail("fixture must contain exactly five explicitly unresolved UI facts")
if any(item.get("value_fa") != "نیازمند تأیید" for item in fixture["facts"]):
    fail("all BP1 technical fixture values must remain نیازمند تأیید")

javascript = (ROOT / "assets" / "js" / "prototype.js").read_text(encoding="utf-8")
for network_api in ("fetch(", "XMLHttpRequest", "WebSocket", "sendBeacon"):
    if network_api in javascript:
        fail(f"network API found in prototype JavaScript: {network_api}")
for storage_api in ("localStorage", "sessionStorage", "indexedDB", "document.cookie"):
    if storage_api in javascript:
        fail(f"browser storage API found in prototype JavaScript: {storage_api}")

print(
    "BP1 VALIDATION PASSED: "
    f"{len(HTML_FILES)} Persian RTL pages; no forms, external resources, "
    "network APIs, browser storage, public-commerce markup, or secrets."
)
