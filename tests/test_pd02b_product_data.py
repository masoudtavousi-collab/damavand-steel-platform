#!/usr/bin/env python3
"""Positive, negative, and adversarial tests for PD-02B."""

from __future__ import annotations

import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[1]
VALIDATION = ROOT / "repository/data/validation"
sys.path.insert(0, str(VALIDATION))

import validate_pd02b_canonical_slice as canonical_validator  # noqa: E402
from validate_product_attributes import (  # noqa: E402
    DefinitionError,
    load_json,
    load_yaml,
    reject_nonlocal_schema_references,
)
from validate_product_data_approval_evidence import (  # noqa: E402
    REGISTRY_PATH as APPROVAL_PATH,
    load_validator as load_approval_validator,
    validate_registry as validate_approval,
)
from validate_product_data_localized_labels import (  # noqa: E402
    CONTRACT_PATH as LABEL_CONTRACT_PATH,
    REGISTRY_PATH as LABEL_PATH,
    load_validator as load_label_validator,
    validate_registry as validate_labels,
)


FIXTURES = ROOT / "tests/fixtures/pd02b"


def set_at_path(document: object, path: list[object], value: object) -> None:
    current = document
    for part in path[:-1]:
        current = current[part]
    current[path[-1]] = value


def get_at_path(document: object, path: list[object]) -> object:
    current = document
    for part in path:
        current = current[part]
    return current


class PD02BProductDataTests(unittest.TestCase):
    def test_positive_canonical_slice(self) -> None:
        self.assertEqual(canonical_validator.main(), 0)

    def test_positive_synthetic_labels(self) -> None:
        validator, lifecycle = load_label_validator()
        value, _ = load_yaml(
            FIXTURES / "valid-synthetic-localized-labels.yaml", "positive labels"
        )
        self.assertEqual(
            validate_labels(
                value, "positive labels", validator, lifecycle, canonical=False
            ),
            [],
        )

    def test_positive_synthetic_approval(self) -> None:
        validator, lifecycle = load_approval_validator()
        value, _ = load_yaml(
            FIXTURES / "valid-synthetic-approval-evidence.yaml", "positive approval"
        )
        self.assertEqual(
            validate_approval(
                value, "positive approval", validator, lifecycle, canonical=False
            ),
            [],
        )

    def test_negative_missing_domain_approval(self) -> None:
        validator, lifecycle = load_approval_validator()
        value, _ = load_yaml(
            FIXTURES / "invalid-missing-domain-approval.yaml", "missing domain"
        )
        rendered = "\n".join(
            validate_approval(
                value, "missing domain", validator, lifecycle, canonical=False
            )
        )
        self.assertIn("MISSING_DOMAIN_APPROVAL", rendered)

    def test_negative_approval_not_consumed(self) -> None:
        validator, lifecycle = load_approval_validator()
        value, _ = load_yaml(
            FIXTURES / "invalid-approval-replay.yaml", "approval replay"
        )
        rendered = "\n".join(
            validate_approval(
                value, "approval replay", validator, lifecycle, canonical=False
            )
        )
        self.assertIn("APPROVAL_NOT_CONSUMED", rendered)

    def test_negative_unicode_confusable(self) -> None:
        validator, lifecycle = load_label_validator()
        value, _ = load_yaml(
            FIXTURES / "invalid-unicode-confusable-label.yaml", "confusable label"
        )
        rendered = "\n".join(
            validate_labels(
                value, "confusable label", validator, lifecycle, canonical=False
            )
        )
        self.assertIn("UNICODE_CONFUSABLE_LABEL", rendered)

    def test_negative_missing_locale_pair(self) -> None:
        validator, lifecycle = load_label_validator()
        value, _ = load_yaml(LABEL_PATH, "canonical labels")
        mutated = copy.deepcopy(value)
        mutated["labels"].pop()
        rendered = "\n".join(
            validate_labels(
                mutated, "missing locale", validator, lifecycle, canonical=True
            )
        )
        self.assertIn("EXACT_LABEL_COUNT", rendered)
        self.assertIn("LOCALE_PAIR_MISSING", rendered)

    def test_adversarial_dataset_hash_tampering(self) -> None:
        validator, lifecycle = load_approval_validator()
        value, _ = load_yaml(APPROVAL_PATH, "canonical approval")
        mutated = copy.deepcopy(value)
        mutated["evidence"][0]["dataset_hashes"][0]["sha256"] = "f" * 64
        rendered = "\n".join(
            validate_approval(
                mutated,
                "tampered hash",
                validator,
                lifecycle,
                canonical=True,
                verify_hashes=True,
            )
        )
        self.assertIn("DATASET_HASH_MISMATCH", rendered)

    def test_adversarial_missing_founder_approval(self) -> None:
        validator, lifecycle = load_approval_validator()
        value, _ = load_yaml(APPROVAL_PATH, "canonical approval")
        mutated = copy.deepcopy(value)
        mutated["evidence"][0]["approval"]["approved_by"] = None
        rendered = "\n".join(
            validate_approval(
                mutated,
                "missing Founder approval",
                validator,
                lifecycle,
                canonical=True,
                verify_hashes=False,
            )
        )
        self.assertIn("FOUNDER_APPROVAL_MISSING", rendered)

    def test_adversarial_permissive_schema_rejected(self) -> None:
        with self.assertRaisesRegex(DefinitionError, "closed Draft 2020-12"):
            load_label_validator(
                contract_path=LABEL_CONTRACT_PATH,
                schema_path=FIXTURES / "adversarial-permissive-schema.json",
            )

    def test_adversarial_remote_ref_rejected(self) -> None:
        schema = load_json(
            FIXTURES / "adversarial-remote-ref-schema.json", "remote-ref schema"
        )
        with self.assertRaisesRegex(DefinitionError, "non-local schema reference"):
            reject_nonlocal_schema_references(schema)

    def test_mutation_manifest_executes_all_cases(self) -> None:
        cases = json.loads((FIXTURES / "mutation-cases.json").read_text("utf-8"))
        names = [case["name"] for case in cases]
        self.assertEqual(len(cases), 20)
        self.assertEqual(len(set(names)), 20)
        self.assertTrue(all(case["expected_code"] for case in cases))
        for case in cases:
            with self.subTest(case=case["name"]):
                if case["document"] == "schema":
                    with self.assertRaisesRegex(
                        DefinitionError, case["expected_code"]
                    ):
                        load_label_validator(
                            contract_path=LABEL_CONTRACT_PATH,
                            schema_path=FIXTURES / case["fixture"],
                        )
                    continue

                datasets = {
                    name: load_yaml(path, f"mutation {case['name']} {name}")[0]
                    for name, path in canonical_validator.PATHS.items()
                }
                contracts = {
                    name: load_yaml(path, f"mutation {case['name']} {name} contract")[0]
                    for name, path in canonical_validator.CONTRACTS.items()
                }
                if case["document"].startswith("contract_"):
                    document = contracts[case["document"].removeprefix("contract_")]
                else:
                    document = datasets[case["document"]]
                if case["operation"] == "set":
                    set_at_path(document, case["path"], case["value"])
                elif case["operation"] == "append_copy":
                    target = get_at_path(document, case["path"])
                    target.append(copy.deepcopy(target[case["source_index"]]))
                elif case["operation"] == "pop":
                    target = get_at_path(document, case["path"])
                    target.pop(case["index"])
                else:
                    self.fail(f"unsupported mutation operation: {case['operation']}")

                with tempfile.TemporaryDirectory(
                    dir=FIXTURES, prefix=".pd02b-mutation-"
                ) as temporary:
                    temporary_root = Path(temporary)
                    dataset_paths = {}
                    contract_paths = {}
                    for name, value in datasets.items():
                        output_path = temporary_root / f"{name}.yaml"
                        output_path.write_text(
                            yaml.safe_dump(
                                value,
                                allow_unicode=True,
                                sort_keys=False,
                            ),
                            encoding="utf-8",
                        )
                        dataset_paths[name] = output_path
                    for name, value in contracts.items():
                        output_path = temporary_root / f"contract-{name}.yaml"
                        output_path.write_text(
                            yaml.safe_dump(
                                value,
                                allow_unicode=True,
                                sort_keys=False,
                            ),
                            encoding="utf-8",
                        )
                        contract_paths[name] = output_path
                    stdout = io.StringIO()
                    stderr = io.StringIO()
                    with (
                        patch.object(canonical_validator, "PATHS", dataset_paths),
                        patch.object(canonical_validator, "CONTRACTS", contract_paths),
                        redirect_stdout(stdout),
                        redirect_stderr(stderr),
                    ):
                        result = canonical_validator.main()
                    rendered = stdout.getvalue() + stderr.getvalue()
                    self.assertNotEqual(result, 0, rendered)
                    self.assertIn(case["expected_code"], rendered)

    def test_no_deferred_grade_430_in_terms(self) -> None:
        values, _ = load_yaml(
            ROOT
            / "repository/data/registries/product-attribute-value-registries.yaml",
            "canonical values",
        )
        codes = {
            term["value_code"]
            for registry in values["value_registries"]
            for term in registry["values"]
        }
        self.assertEqual(codes, {"stainless_steel", "201", "304", "316"})
        self.assertNotIn("430", codes)

    def test_profile_has_no_public_runtime_authority(self) -> None:
        profiles, _ = load_yaml(
            ROOT / "repository/data/registries/product-attribute-profiles.yaml",
            "canonical profiles",
        )
        rules = profiles["profiles"][0]["attribute_rules"]
        self.assertEqual(len(rules), 2)
        for rule in rules:
            self.assertEqual(rule["public_visibility"], "INTERNAL")
            self.assertFalse(rule["variation_axis"])
            self.assertFalse(rule["filtering"])
            self.assertEqual(rule["inquiry_use"], "NOT_USED")
            self.assertEqual(rule["seo_use"], "PROHIBITED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
