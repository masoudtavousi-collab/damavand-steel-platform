#!/usr/bin/env python3
"""Validate one-to-one disposition of the Atlas planning registry."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "atlas" / "DOCUMENT_REGISTRY.csv"
MATRIX = ROOT / "atlas" / "ATLAS_ADOPTION_MATRIX.csv"
LEGACY_DISPOSITION = ROOT / "atlas" / "LEGACY_ATLAS_DISPOSITION.md"
ALLOWED = {
    "MAP_TO_EXISTING",
    "ADOPT",
    "MERGE",
    "DEFER",
    "REJECT",
    "ARCHIVE_REFERENCE",
}


def read_csv(path: Path, encoding: str = "utf-8") -> list[dict[str, str]]:
    with path.open(encoding=encoding, newline="") as handle:
        return list(csv.DictReader(handle))


def fail(message: str) -> None:
    raise SystemExit(f"[ATLAS_ADOPTION_INVALID] {message}")


def main() -> None:
    if not MATRIX.is_file():
        fail(f"missing {MATRIX.relative_to(ROOT)}")
    if not LEGACY_DISPOSITION.is_file():
        fail(f"missing {LEGACY_DISPOSITION.relative_to(ROOT)}")

    registry = read_csv(REGISTRY, "utf-8-sig")
    matrix = read_csv(MATRIX)
    registry_ids = [row["id"] for row in registry]
    matrix_ids = [row["atlas_id"] for row in matrix]

    duplicates = sorted(
        atlas_id for atlas_id, count in Counter(matrix_ids).items() if count > 1
    )
    if duplicates:
        fail(f"duplicate matrix IDs: {', '.join(duplicates)}")

    missing = sorted(set(registry_ids) - set(matrix_ids))
    extra = sorted(set(matrix_ids) - set(registry_ids))
    if missing or extra:
        fail(f"registry mismatch; missing={missing}, extra={extra}")

    registry_by_id = {row["id"]: row for row in registry}
    for row in matrix:
        atlas_id = row["atlas_id"]
        source = registry_by_id[atlas_id]
        disposition = row["disposition"]
        owner = row["canonical_owner"]

        if row["title"] != source["title"] or row["atlas_path"] != source["path"]:
            fail(f"{atlas_id} title/path differs from registry")
        if disposition not in ALLOWED:
            fail(f"{atlas_id} has unknown disposition {disposition!r}")
        if not row["decision_status"] or not row["rationale"]:
            fail(f"{atlas_id} lacks decision status or rationale")
        if disposition in {"MAP_TO_EXISTING", "MERGE"}:
            if not owner:
                fail(f"{atlas_id} requires a canonical owner")
            if not (ROOT / owner).is_file():
                fail(f"{atlas_id} owner does not exist: {owner}")
        if disposition in {"DEFER", "REJECT", "ARCHIVE_REFERENCE"} and owner:
            fail(f"{atlas_id} disposition {disposition} must not claim an owner")

    print(
        "Atlas adoption matrix is valid: "
        f"{len(matrix)} rows, {len(set(row['domain'] for row in matrix))} domains."
    )


if __name__ == "__main__":
    main()
