#!/usr/bin/env python3
"""Offline, fail-closed validation for FT-RB-02 Inquiry/CRM readiness."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import socket
import subprocess
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "repository/data/contracts/ft-rb-02-inquiry-crm-flow-readiness.contract.yaml"
SCHEMA = ROOT / "repository/data/schemas/ft-rb-02-inquiry-crm-flow-readiness.schema.json"
REGISTRY = ROOT / "repository/data/registries/extensions/ftrb02/inquiry-crm-flow-readiness.yaml"
SYNTHETIC = ROOT / "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/valid-synthetic.yaml"
C009 = ROOT / "repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml"
MAX_BYTES, MAX_DEPTH, MAX_NODES = 2 * 1024 * 1024, 100, 50_000

ALLOWLIST = [
    "docs/FT_RB_02_INQUIRY_CRM_FLOW_READINESS_SCOPE_V1.0.md",
    "repository/data/contracts/ft-rb-02-inquiry-crm-flow-readiness.contract.yaml",
    "repository/data/registries/extensions/ftrb02/inquiry-crm-flow-readiness.yaml",
    "repository/data/schemas/ft-rb-02-inquiry-crm-flow-readiness.schema.json",
    "repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py",
    "scripts/test.sh",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/README.md",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-duplicate-keys.json",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-duplicate-keys.yaml",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-permissive-schema.json",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-remote-ref-schema.json",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/mutation-cases.json",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/valid-synthetic.yaml",
    "tests/test_ft_rb_02_inquiry_crm_flow_readiness.py",
]
ORIGINAL_MISSION_BASE = "5f452703dd35e1fee050f09529a0de379767e2bb"
APPROVED_SUCCESSOR_BASE = "ff3077cd7041f7bed2f74d6ba2f8e685031eb5b0"
APPROVED_BASES = (ORIGINAL_MISSION_BASE, APPROVED_SUCCESSOR_BASE)
BRANCH = "codex/ft-rb-02-inquiry-crm-flow-readiness"
REPAIR_BASE = "1fa127859655f8027aaea9dc84db7b109cc5949d"
REPAIR_BRANCH = "codex/ft-rb-02-generic-successor-context-repair"
REPAIR_ALLOWLIST = [
    "repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py",
    "tests/test_ft_rb_02_inquiry_crm_flow_readiness.py",
]
HISTORICAL_CONTEXT = "HISTORICAL_FT_RB_02"
REPAIR_CONTEXT = "AUTHORIZED_GENERIC_SUCCESSOR_REPAIR"
SUCCESSOR_CONTEXT = "GENERIC_SUCCESSOR"
REPOSITORY_FULL_NAME = "masoudtavousi-collab/damavand-steel-platform"
BASE_SCRIPT_BLOBS = {base: "943b67e977dbe8975e226fb28858d2ec3a38ea03" for base in APPROVED_BASES}
BASE_TOTAL_TREE_ENTRIES = {base: 646 for base in APPROVED_BASES}
COMMITTED_TREE_PROOFS = {
    ORIGINAL_MISSION_BASE: ("9f316afa552bf84d930f2cadb85ec7fb9c5d0e02e5bee77c8b2c7927a937c2bb", 645, 659),
    APPROVED_SUCCESSOR_BASE: ("de41ae50a3382212805cd25b8d9874414256558bbfb42dcd5ca6d8437928dad0", 645, 659),
}
BASE_ABSENT_PATHS = [path for path in ALLOWLIST if path != "scripts/test.sh"]
PROTECTED_PATHS = tuple(BASE_ABSENT_PATHS)
PROTECTED_BLOBS = {
    "docs/FT_RB_02_INQUIRY_CRM_FLOW_READINESS_SCOPE_V1.0.md": "e5e08084cfedcb39f17b0386fbf52f3ba66a09de",
    "repository/data/contracts/ft-rb-02-inquiry-crm-flow-readiness.contract.yaml": "e2a05a17cd6b01b2ad315f73bdfaa3993d8ab35e",
    "repository/data/registries/extensions/ftrb02/inquiry-crm-flow-readiness.yaml": "0f6c4448d1750e7a5cc8a751af7fa0a8e23ddc2d",
    "repository/data/schemas/ft-rb-02-inquiry-crm-flow-readiness.schema.json": "68cdd525eda91f2679939eb4567c821c3e73109f",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/README.md": "dd9ce2e4872d1f75b7b596cb3e8db6a9fb579b70",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-duplicate-keys.json": "bd682cb4cdc902e9982d01e03a6221a620c5513e",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-duplicate-keys.yaml": "bde3c9f488a32ad164c95e7886afbe81d09f9ce9",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-permissive-schema.json": "818d3efd200ee6aaf9fcd861d2561160c2623735",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-remote-ref-schema.json": "a8b538a1eba45260615f6401a54e4c107228b9df",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/mutation-cases.json": "2628100b11263ea2e562ed730aedaa8324f191ee",
    "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/valid-synthetic.yaml": "47b4731a9033eff56caaa74f561f29e0c1e200b5",
    "tests/test_ft_rb_02_inquiry_crm_flow_readiness.py": "7fadd2be25edb0ff3a9d60af9fd432620fa3982a",
}
VALIDATOR_NORMALIZED_SHA256 = "75001121188141ad2a6fdb0114bfee2e6cf5bdeff35bb113fb5560d16c16b790"
RUNNER_SLOT_START = '"$python" -B -m unittest tests.test_ft_rb_02_inquiry_crm_flow_readiness\n\n'
RUNNER_SLOT_END = '"$python" repository/data/validation/validate_bp2_data_blueprint.py\n'
RUNNER_PREFIX_SHA256 = "2bde612096f850be1625d79b494fc5137b6589bf0740d2fc33037983a91b1352"
RUNNER_SUFFIX_SHA256 = "a67683da6c19a59206d2db2074d3af98b539af48aebe1875cc861a0c0a75279a"
MAX_PUSH_COMMITS = 20

DEPENDENCIES = {
    "c002_contract": "repository/data/contracts/commercial-pilot-candidate.contract.yaml",
    "c002_schema": "repository/data/schemas/commercial-pilot-candidate.schema.json",
    "c002_registry": "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml",
    "c006_contract": "repository/data/contracts/pipe-product-experience-architecture.contract.yaml",
    "c006_schema": "repository/data/schemas/pipe-product-experience-architecture.schema.json",
    "c006_registry": "repository/data/registries/extensions/c006/pipe-product-experience-architecture.yaml",
    "c008_contract": "repository/data/contracts/c008-c002-readiness-evidence-closure.contract.yaml",
    "c008_schema": "repository/data/schemas/c008-c002-readiness-evidence-closure.schema.json",
    "c008_registry": "repository/data/registries/extensions/c008/201-51-readiness-evidence-closure.yaml",
    "c008_r1_contract": "repository/data/contracts/c008-r1-remaining-real-world-evidence-closure.contract.yaml",
    "c008_r1_schema": "repository/data/schemas/c008-r1-remaining-real-world-evidence-closure.schema.json",
    "c008_r1_registry": "repository/data/registries/extensions/c008r1/201-51-remaining-real-world-evidence-closure.yaml",
    "c008_ft1_contract": "repository/data/contracts/c008-ft1-fast-track-inquiry-launch-gate.contract.yaml",
    "c008_ft1_schema": "repository/data/schemas/c008-ft1-fast-track-inquiry-launch-gate.schema.json",
    "c008_ft1_registry": "repository/data/registries/extensions/c008ft1/fast-track-inquiry-launch-gate.yaml",
    "c009_contract": "repository/data/contracts/c009-first-commercial-slice-canonical-leaf-promotion.contract.yaml",
    "c009_schema": "repository/data/schemas/c009-first-commercial-slice-canonical-leaf-promotion.schema.json",
    "c009_registry": "repository/data/registries/extensions/c009/201-51-canonical-leaf-promotion.yaml",
    "c009_ft2_contract": "repository/data/contracts/c009-ft2-post-c009-fast-track-gate-reevaluation.contract.yaml",
    "c009_ft2_schema": "repository/data/schemas/c009-ft2-post-c009-fast-track-gate-reevaluation.schema.json",
    "c009_ft2_registry": "repository/data/registries/extensions/c009ft2/post-c009-fast-track-gate-reevaluation.yaml",
    "ft_rb_00_contract": "repository/data/contracts/ft-rb-campaign-status.contract.yaml",
    "ft_rb_00_schema": "repository/data/schemas/ft-rb-campaign-status.schema.json",
    "ft_rb_00_registry": "repository/data/registries/extensions/ftrb/campaign-status.yaml",
    "ft_rb_01_contract": "repository/data/contracts/ft-rb-01-rights-safe-media-readiness.contract.yaml",
    "ft_rb_01_schema": "repository/data/schemas/ft-rb-01-rights-safe-media-readiness.schema.json",
    "ft_rb_01_registry": "repository/data/registries/extensions/ftrb01/rights-safe-media-readiness.yaml",
}
PINS = {
    "c002_contract": "923731cb080b0ecc05abb21b1189bfdd0df94297780cce364bb791479f7f47e3",
    "c002_schema": "1e1b1977f369ab7e5961d4e69111682d1117bc6eeedf666a9e568f0115952741",
    "c002_registry": "deb0215d2b5f4b5ec0061f937aec9c3e37cf97c94432a23737bf5756cef9587e",
    "c006_contract": "131b2c79a3d017c65bac896e95e7a638164a77b821546e5217266f6d3829dcc0",
    "c006_schema": "9a9009c4431c097c062dcef81fad03fae51784ff466bb8cc5db6ed14237f79e3",
    "c006_registry": "5b5510af1b521daa7b2539007cab0681885f2bbc3eff4a75dde67cb38857ad8b",
    "c008_contract": "bf450358e11c82df7ae41a7777bd2889f2c4b7cffe64a5f2ee21f3303cbd2f5c",
    "c008_schema": "82f8dbfb93233b6d40603a56bdb7661ee4d477003ba13b97c59d80bb0c8a27af",
    "c008_registry": "bd06e76da52750b9b54c09ccba88421ae82778dce84a4afa15475a88297081d9",
    "c008_r1_contract": "da5a70f0e7330df8afab52e931f664bda453266740646a4d4183d25370ea75d7",
    "c008_r1_schema": "fea342c3210dca9e5c2e98030bf8b5e64464cdd550cbb3b5675109c49673b904",
    "c008_r1_registry": "9dcf2cc7cc10ab01a9b97ab40ac896debd12e6f25ad5b7e700921a6c782fb87b",
    "c008_ft1_contract": "4c940eed75fe433bc8adbc85cb45954068b233cc1de6d80b40bc28eb71466fb5",
    "c008_ft1_schema": "8eb3c93a37932e6676e8a3d1c22e0c35d3f6a4d0f47f7467ea718f466ceabd80",
    "c008_ft1_registry": "799dad2f7fdf9f6ffb5a9fe37c707f222f6f92f1cc6b1e251bd3f366dd2e9cf3",
    "c009_contract": "a1179a6ef97735431f89ef075e7d40c9dd6973b5eacbeca6599d9666bc7674d3",
    "c009_schema": "aea8a6dd7b521a83576bbd00ce686d3bc2477552bc4a2f3642a80b648b6e31e2",
    "c009_registry": "1b50d28ddded3a818afb82d19759713bd6c2f2b058b4020510d8b5f74a7f6a3f",
    "c009_ft2_contract": "0200e474df33fcd8b74308c678107d53dbc9f9999b84fa753db97fc1f1ced5e8",
    "c009_ft2_schema": "558153f5f3bba6206215be46454f6add6c8fdabc414b0105c141327a12903e82",
    "c009_ft2_registry": "51d9298e2e63b44986a921d72eabc069db5b46dfda0c614ee70d4d7e2e434d08",
    "ft_rb_00_contract": "0abac587eff448770493e9afd9dc908503f40f519525b160b8e30d1cb0f59aca",
    "ft_rb_00_schema": "9ccc2f734ca766a52a10811d1b03c2c78cf1f1c0c8db525477ec16727bf86a0d",
    "ft_rb_00_registry": "242df96bf329950e80830a90b1e5a5cd202b89418113347fbbf705b69c8419b1",
    "ft_rb_01_contract": "b615c55751a3d5efd6d7f395f849ac5e7e992e890f13130a348f783491d0468f",
    "ft_rb_01_schema": "676f1f0180ee2a47d69dc68f2f170a5008ec00126b3540be9a771674f16dec84",
    "ft_rb_01_registry": "c89067202e5d2f93953e05bf74b5d47cab5f6db7aa8944afcf2715b047828547",
}
OWNER_FILES = {
    "docs_03_business_rules": "docs/03_BUSINESS_RULES.md",
    "docs_06_wordpress_architecture": "docs/06_WORDPRESS_ARCHITECTURE.md",
    "docs_10_security": "docs/10_SECURITY.md",
    "docs_19_product_data_model": "docs/19_PRODUCT_DATA_MODEL.md",
    "docs_20_woocommerce_product_model": "docs/20_WOOCOMMERCE_PRODUCT_MODEL.md",
    "docs_23_inquiry_data_model": "docs/23_INQUIRY_DATA_MODEL.md",
    "docs_38_woocommerce_configuration": "docs/38_WOOCOMMERCE_CONFIGURATION.md",
    "docs_41_custom_fields_model": "docs/41_CUSTOM_FIELDS_MODEL.md",
    "docs_42_inquiry_workflow": "docs/42_INQUIRY_WORKFLOW.md",
    "docs_43_user_roles": "docs/43_USER_ROLES.md",
    "docs_44_plugin_responsibility": "docs/44_PLUGIN_RESPONSIBILITY_MATRIX.md",
    "adr_0001_inquiry_first": "docs/adr/0001-inquiry-first-commerce.md",
}
OWNER_PINS = {
    "docs_03_business_rules": "cb8e33c5be9c86906b44e9b7535dd0af0178ec46",
    "docs_06_wordpress_architecture": "6e45067bdf8c0db26929a20cecc84205e5a7add7",
    "docs_10_security": "ceb31fa171c0a10ca631c322fe6e3a8918760ed9",
    "docs_19_product_data_model": "f346fb8896f2808d3cc39699eb750266b8914c0f",
    "docs_20_woocommerce_product_model": "664dae1e9439910d9ee58567659016a7adc6fbe5",
    "docs_23_inquiry_data_model": "d36c643987e724684c2dde0e68c2a03c2411bfd4",
    "docs_38_woocommerce_configuration": "478412c171f7b8105c264a8119f6de24a5ec7e26",
    "docs_41_custom_fields_model": "d1f09f266a1b458df3f2f30a841cfdc7da7c1679",
    "docs_42_inquiry_workflow": "ec168dd9d5a480d97e2fcb8cd4a5b4bc07c60295",
    "docs_43_user_roles": "c3796bd1652e20b630dda3daee0d4f8b31db9be3",
    "docs_44_plugin_responsibility": "fb4352cc1210faddeeb00b0c75c8c7234e363968",
    "adr_0001_inquiry_first": "b04176c9108ecff3bfe0776342a853c5455c9c19",
}

# These pre-pin exactness anchors are independent of the final four package pins.
EXPECTED_CONTRACT_DIGEST = "21d1694931f54eb25355f026b1fb01646f11ad415467ca2882ad7432fde43850"
EXPECTED_SCHEMA_DIGEST = "146e75ce2d6489e9fd7b5fa11d7e672aad942c0df60c3e94eb0ea39a6fdfd479"
EXPECTED_SECTION_DIGESTS = {
    "registry_id": "7a4afa0ec8eede3447628f01ca1ddee3a0f19727088fcc6bde4302d1ac9eb94f",
    "registry_version": "39fe4a40977d0585fd5704359e3685b0ada5cf5ee061e5d97385601d120cd0ec",
    "mission_id": "71e2c6f28ffd998597a9a703d6dbd3bf241706fcb67604590e8503532cf8d3dc",
    "campaign_authorized_starting_main": "4c892becb90bec64a2c574af33d8b4e8ac13cfa9bcb134724690f2999a9118e5",
    "mission_base_main": "839ddde0c0bb147395f45ff6460ca8296707e994b17faf9e52dbb80726a3e5b4",
    "source": "c956e3940d888b779248138dcab4b7caf1b42fad9bff1fda90cc3be6e896e638",
    "source_policy": "2cbdff4b453fa5eea1cb69f663102f71bfa2f627634a253064249b74d0aa5e18",
    "exact_changed_paths": "812d2b2825b718cd02af24c9945463207ee30e6d235c9f164f3c1103c7617029",
    "owner_model": "021ab3961e35d2b3d82bbbd2a89024cb077f009178ad1131de6989fca985f08d",
    "canonical_slice_binding": "26bb2ee60a314bb779e4be6c726f83e417518acc7ceb5d8f65a1b11c6177a079",
    "readiness": "49cfac9aba01724c88c5d971d7deb9587da2538b67de9a7b73a2f67b9822ab73",
    "customer_form": "fa75683d4f7aaa478fbe8c1028813fb80c3facc07c9ee19e11e75131fc75834b",
    "city_reconciliation": "fe08039bb6fc6aa3d603c82d54556e1fe09acbefdb05ae2ae994c308da0463a1",
    "inquiry_record_policy": "9ef3f6639c946777bf1aee19b924503f87e2ac556eb56c03c8cec227e2427a29",
    "future_payload_contract": "47a4a00e5a4c0bd6df54c402bc3c3d02a10d4e326d12326915ae323774a131d5",
    "state_planes": "3c4f035d871dd3afadcc552a485ff26e3710ea95265505a809b8215f32672f4f",
    "lead_stage_vocabulary": "34494fa85e9b13e11c526288c110b5274bb97f6f8efe431ff304ff6cbd6c623d",
    "supply_check_policy": "400ffc5bfb9979663d229556635d8638db9afa2ca746057f2229b1ec0e81aaca",
    "deduplication_delivery": "04d47e92373c2738b76308784fcea8f6e6b17353166e797d548ccee3c6d31617",
    "consent_privacy": "5a61b2b19596d80ef60422c89b81005d0bc3009a0b104aa1a82336053477e05f",
    "form_security_requirements": "e2d859bc97e4a73b8ef497daa7790cbce37c60cbca5ca9c161f85022838af2cc",
    "analytics_boundary": "ba84951333ffe0f5ac79b6f0441d5e0d6aeb69212e90281ef0d3b17ee4b6790d",
    "missing_authority_inputs": "46c484c621a1f53e397583f9bbbd2ad7c9cbf952ca47cc3cbb205e3150d15cf0",
    "no_claim_boundaries": "8b5ddb7413c5454fb374e9d445230281266c28afb77a2eb9bc913d4da7f4828c",
    "gate_snapshot": "4c666393a4442f782bcd447ffa00595110ba8953fc942b3f1f00aa5a2ce6a163",
    "c002_snapshot": "386514081ea4a7b2e43b8dc0f40d8fdbad2ae0e0a690a8c43dc26280fadbd55b",
}
DIGESTS = {
    "contract": "21d1694931f54eb25355f026b1fb01646f11ad415467ca2882ad7432fde43850",
    "schema": "146e75ce2d6489e9fd7b5fa11d7e672aad942c0df60c3e94eb0ea39a6fdfd479",
    "canonical": "5fdc9a5ebe830d4f91f4b1b5978ccc033af813e7326de6a219603b49ed64c6f2",
    "synthetic": "2c778bc60df2c3381390efa1d5258f666e96fed9e5059a67c19b44e95e5e9019",
}
PROVISIONAL_RUNNER_BLOB = "db7cfa5f44072e43cb7fb0cf8b55d9c0ffa68c91"
PINNED_RUNNER_BLOB = "f8ebec998a8fb21e2468e5f5a762a8c122a4af46"


class StrictLoader(yaml.SafeLoader):
    pass


def _mapping(loader: StrictLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def _json_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def bounded(value: Any) -> None:
    nodes = 0

    def visit(item: Any, depth: int) -> None:
        nonlocal nodes
        nodes += 1
        if nodes > MAX_NODES:
            raise ValueError("node cap exceeded")
        if depth > MAX_DEPTH:
            raise ValueError("depth cap exceeded")
        if isinstance(item, float) and not math.isfinite(item):
            raise ValueError("nonfinite number")
        if isinstance(item, dict):
            for key, child in item.items():
                if not isinstance(key, str):
                    raise ValueError("non-string mapping key")
                visit(child, depth + 1)
        elif isinstance(item, list):
            for child in item:
                visit(child, depth + 1)

    visit(value, 0)


def safe_file(path: Path) -> bytes:
    if not path.is_absolute():
        path = path.resolve()
    if path.is_symlink() or any(parent.is_symlink() for parent in path.parents if parent.exists()):
        raise ValueError("symlink path forbidden")
    if not path.is_file():
        raise ValueError("regular file required")
    raw = path.read_bytes()
    if len(raw) > MAX_BYTES:
        raise ValueError("byte cap exceeded")
    raw.decode("utf-8")
    return raw


def load_data(path: Path) -> Any:
    raw = safe_file(path).decode("utf-8")
    if path.suffix == ".json":
        value = json.loads(raw, object_pairs_hook=_json_pairs, parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite JSON: {token}")))
    else:
        value = yaml.load(raw, Loader=StrictLoader)
    bounded(value)
    return value


def digest(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_oid(path: Path) -> str:
    raw = safe_file(path)
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def is_oid(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 40 and all(char in "0123456789abcdef" for char in value)


def safe_repo_path(value: Any) -> str:
    if not isinstance(value, str) or not value or value.startswith("/") or "\\" in value:
        raise ValueError("unsafe repository path")
    if any(part in {"", ".", ".."} for part in value.split("/")):
        raise ValueError("unsafe repository path")
    return value


def schema_issues(schema: Any) -> list[str]:
    issues: list[str] = []
    forbidden = {"allOf", "anyOf", "oneOf", "not", "if", "then", "else", "contains", "patternProperties", "unevaluatedProperties", "unevaluatedItems", "prefixItems", "dependentSchemas", "dependentRequired", "propertyNames", "contentSchema", "contentEncoding", "contentMediaType"}
    object_keys = {"properties", "required", "additionalProperties", "minProperties", "maxProperties"}
    array_keys = {"items", "minItems", "maxItems", "uniqueItems"}
    string_keys = {"minLength", "maxLength", "pattern", "format"}
    numeric_keys = {"minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "multipleOf"}

    def visit(node: Any, path: str) -> None:
        if node is True or node == {}:
            issues.append(f"PERMISSIVE_SCHEMA:{path}")
            return
        if node is False:
            return
        if not isinstance(node, dict):
            issues.append(f"SCHEMA_NODE_TYPE:{path}")
            return
        if forbidden.intersection(node):
            issues.append(f"UNSUPPORTED_SCHEMA_KEYWORD:{path}")
        ref = node.get("$ref")
        if isinstance(ref, str):
            if not ref.startswith("#/"):
                issues.append(f"REMOTE_SCHEMA_REF:{path}")
            if set(node) != {"$ref"}:
                issues.append(f"REF_SIBLING:{path}")
            return
        kind = node.get("type")
        if isinstance(kind, list):
            issues.append(f"TYPE_UNION:{path}")
        if not any(key in node for key in ("type", "const", "enum")):
            issues.append(f"NON_ASSERTIVE_SCHEMA:{path}")
        if object_keys.intersection(node) and kind != "object":
            issues.append(f"WRONG_INSTANCE_OBJECT:{path}")
        if array_keys.intersection(node) and kind != "array":
            issues.append(f"WRONG_INSTANCE_ARRAY:{path}")
        if string_keys.intersection(node) and kind != "string":
            issues.append(f"WRONG_INSTANCE_STRING:{path}")
        if numeric_keys.intersection(node) and kind not in {"integer", "number"}:
            issues.append(f"WRONG_INSTANCE_NUMBER:{path}")
        if kind == "object" and node.get("additionalProperties") is not False:
            issues.append(f"OPEN_SCHEMA:{path}")
        if kind == "array" and ("items" not in node or node.get("items") is True):
            issues.append(f"OPEN_ARRAY:{path}")
        for container in ("properties", "$defs"):
            value = node.get(container)
            if value is not None:
                if not isinstance(value, dict):
                    issues.append(f"SCHEMA_CONTAINER:{path}/{container}")
                else:
                    for name, child in value.items():
                        visit(child, f"{path}/{container}/{name}")
        if "items" in node:
            visit(node["items"], f"{path}/items")

    visit(schema, "#")
    if issues:
        return sorted(set(issues))
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        return [f"SCHEMA_META:{type(exc).__name__}"]
    return []


def parse_raw_commit(raw: str) -> tuple[str, list[str]]:
    if len(raw.encode("utf-8")) > MAX_BYTES:
        raise ValueError("commit object byte cap")
    headers = raw.split("\n\n", 1)[0].splitlines()
    if not headers or not headers[0].startswith("tree ") or not is_oid(headers[0][5:]):
        raise ValueError("malformed commit tree")
    tree_oid = headers[0][5:]
    parents: list[str] = []
    open_parents = True
    for line in headers[1:]:
        if line.startswith("parent "):
            if not open_parents or not is_oid(line[7:]) or len(parents) >= 2:
                raise ValueError("malformed commit parents")
            parents.append(line[7:])
        else:
            open_parents = False
            if line.startswith("tree "):
                raise ValueError("duplicate commit tree")
    return tree_oid, parents


def raw_commit(commit: str = "HEAD") -> tuple[str, list[str]]:
    result = subprocess.run(["git", "cat-file", "-p", commit], cwd=ROOT, check=True, capture_output=True, text=True)
    return parse_raw_commit(result.stdout)


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=ROOT, check=check, capture_output=True, text=True)


def diff_paths(base: str) -> list[str]:
    if not is_oid(base):
        raise ValueError("invalid diff base")
    paths: set[str] = set()
    for args in (("diff", "--name-only", f"{base}...HEAD"), ("diff", "--name-only", "HEAD"), ("ls-files", "--others", "--exclude-standard")):
        result = git(*args)
        paths.update(line for line in result.stdout.splitlines() if line)
    return sorted(paths)


def changed_paths(base: str) -> list[str]:
    if base not in APPROVED_BASES:
        raise ValueError("unapproved FT-RB-02 base")
    return diff_paths(base)


def commit_available(commit: str) -> bool:
    return is_oid(commit) and git("cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode == 0


def base_available(base: str) -> bool:
    return base in APPROVED_BASES and commit_available(base)


def is_ancestor(ancestor: str, descendant: str = "HEAD") -> bool:
    return git("merge-base", "--is-ancestor", ancestor, descendant, check=False).returncode == 0


def current_branch() -> str:
    result = git("symbolic-ref", "--quiet", "--short", "HEAD", check=False)
    if result.returncode:
        raise RuntimeError("detached or ambiguous branch")
    branch = result.stdout.strip()
    if not valid_branch_ref(branch):
        raise RuntimeError("malformed branch")
    return branch


def valid_branch_ref(value: Any) -> bool:
    return (
        isinstance(value, str)
        and 0 < len(value) <= 255
        and value != "HEAD"
        and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", value) is not None
        and ".." not in value
        and "@{" not in value
        and not value.endswith(("/", ".", ".lock"))
    )


def classify_pr_context(base_sha: Any, head_ref: Any) -> str:
    if not is_oid(base_sha) or not valid_branch_ref(head_ref):
        raise RuntimeError("malformed mission context")
    historical_base = base_sha in APPROVED_BASES
    historical_branch = head_ref == BRANCH
    if historical_base != historical_branch:
        raise RuntimeError("ambiguous historical context")
    if historical_base:
        return HISTORICAL_CONTEXT
    repair_base = base_sha == REPAIR_BASE
    repair_branch = head_ref == REPAIR_BRANCH
    if repair_base != repair_branch:
        raise RuntimeError("ambiguous repair context")
    return REPAIR_CONTEXT if repair_base else SUCCESSOR_CONTEXT


def local_context() -> str:
    branch = current_branch()
    if branch == BRANCH:
        approved_base_for_head()
        return HISTORICAL_CONTEXT
    if branch == REPAIR_BRANCH:
        if not commit_available(REPAIR_BASE) or not is_ancestor(REPAIR_BASE):
            raise RuntimeError("invalid repair ancestry")
        return REPAIR_CONTEXT
    if not commit_available(REPAIR_BASE) or not is_ancestor(REPAIR_BASE):
        raise RuntimeError("successor predates integrated FT-RB-02")
    return SUCCESSOR_CONTEXT


def approved_base_for_head(head: str = "HEAD") -> str:
    candidates = [base for base in APPROVED_BASES if base_available(base) and is_ancestor(base, head)]
    most_specific = [
        candidate
        for candidate in candidates
        if not any(candidate != other and is_ancestor(candidate, other) for other in candidates)
    ]
    if len(most_specific) != 1:
        raise RuntimeError("ambiguous or unavailable approved FT-RB-02 base")
    return most_specific[0]


def base_shape_issues(base: str) -> list[str]:
    if base not in APPROVED_BASES:
        return ["BASE_SHAPE:unapproved"]
    issues: list[str] = []
    if git("rev-parse", f"{base}:scripts/test.sh", check=False).stdout.strip() != BASE_SCRIPT_BLOBS[base]:
        issues.append("BASE_SHAPE:script")
    for path in BASE_ABSENT_PATHS:
        if git("cat-file", "-e", f"{base}:{path}", check=False).returncode == 0:
            issues.append(f"BASE_SHAPE:unexpected:{path}")
    total = git("ls-tree", "-r", "--name-only", base, check=False)
    if total.returncode or len(total.stdout.splitlines()) != BASE_TOTAL_TREE_ENTRIES[base]:
        issues.append("BASE_SHAPE:count")
    return sorted(issues)


def parse_tree(raw: bytes) -> tuple[str, int, int, dict[str, tuple[str, str, str]]]:
    if len(raw) > MAX_BYTES or not raw.endswith(b"\0"):
        raise ValueError("tree framing or byte cap")
    excluded = set(ALLOWLIST)
    entries: dict[str, tuple[str, str, str]] = {}
    retained: list[bytes] = []
    previous: bytes | None = None
    for record in raw[:-1].split(b"\0"):
        if not record or b"\t" not in record:
            raise ValueError("malformed tree record")
        metadata, raw_path = record.split(b"\t", 1)
        parts = metadata.split(b" ")
        if len(parts) != 3:
            raise ValueError("malformed tree metadata")
        mode, kind, oid = (part.decode("ascii") for part in parts)
        path = safe_repo_path(raw_path.decode("utf-8"))
        if previous is not None and raw_path <= previous:
            raise ValueError("tree order")
        previous = raw_path
        if mode not in {"100644", "100755", "120000", "160000"} or kind not in {"blob", "commit"} or not is_oid(oid) or path in entries:
            raise ValueError("tree entry")
        entries[path] = (mode, kind, oid)
        if path not in excluded:
            retained.append(record + b"\0")
    return hashlib.sha256(b"".join(retained)).hexdigest(), len(retained), len(entries), entries


def normalized_validator_digest(raw: bytes) -> str:
    normalized, replacements = re.subn(
        rb'(?m)^VALIDATOR_NORMALIZED_SHA256 = "[^"\r\n]*"$',
        b'VALIDATOR_NORMALIZED_SHA256 = "<NORMALIZED>"',
        raw,
        count=1,
    )
    if replacements != 1:
        raise ValueError("validator self-pin shape")
    return hashlib.sha256(normalized).hexdigest()


def protected_entry_issues(
    entries: dict[str, tuple[str, str, str]],
    validator_source: bytes,
) -> list[str]:
    issues: list[str] = []
    runner = entries.get("scripts/test.sh")
    if runner is None:
        issues.append("PROTECTED_RUNNER:missing")
    elif runner[0] != "100755" or runner[1] != "blob":
        issues.append("PROTECTED_RUNNER:shape")
    validator_path = "repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py"
    for path in PROTECTED_PATHS:
        entry = entries.get(path)
        if entry is None:
            issues.append(f"PROTECTED_ARTIFACT:missing:{path}")
            continue
        if entry[0] != "100644" or entry[1] != "blob":
            issues.append(f"PROTECTED_ARTIFACT:shape:{path}")
            continue
        if path == validator_path:
            try:
                actual = normalized_validator_digest(validator_source)
            except Exception as exc:
                issues.append(f"PROTECTED_ARTIFACT:validator:{type(exc).__name__}")
                continue
            if VALIDATOR_NORMALIZED_SHA256 == "TO_BE_FINALIZED" or actual != VALIDATOR_NORMALIZED_SHA256:
                issues.append("PROTECTED_ARTIFACT:content:" + path)
        else:
            expected = PROTECTED_BLOBS.get(path)
            if expected in {None, "TO_BE_FINALIZED"} or entry[2] != expected:
                issues.append(f"PROTECTED_ARTIFACT:content:{path}")
    return sorted(issues)


def successor_protected_issues(commit: str = "HEAD") -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-rz", "--full-tree", commit],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        _, _, _, entries = parse_tree(result.stdout)
        validator_path = "repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py"
        validator_entry = entries.get(validator_path)
        if validator_entry is None or validator_entry[1] != "blob" or not is_oid(validator_entry[2]):
            return [f"PROTECTED_ARTIFACT:missing:{validator_path}"]
        validator = subprocess.run(
            ["git", "cat-file", "blob", validator_entry[2]],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout
        return protected_entry_issues(entries, validator)
    except Exception as exc:
        return [f"PROTECTED_ARTIFACT:{type(exc).__name__}"]


def committed_tree_issues(base: str, commit: str = "HEAD") -> list[str]:
    expected = COMMITTED_TREE_PROOFS.get(base)
    if expected is None:
        return ["TREE_PROOF:unapproved_base"]
    issues: list[str] = []
    result = subprocess.run(["git", "ls-tree", "-rz", "--full-tree", commit], cwd=ROOT, check=True, capture_output=True)
    try:
        retained_digest, retained_count, total_count, entries = parse_tree(result.stdout)
    except Exception as exc:
        return [f"TREE_PROOF:{type(exc).__name__}"]
    if (retained_digest, retained_count, total_count) != expected:
        issues.append("TREE_PROOF:digest_or_count")
    for path in BASE_ABSENT_PATHS:
        entry = entries.get(path)
        if entry is None or entry[0] != "100644" or entry[1] != "blob":
            issues.append(f"TREE_PROOF:new_entry:{path}")
    runner = entries.get("scripts/test.sh")
    provisional = any(value == "TO_BE_FINALIZED" for value in DIGESTS.values())
    expected_runner_blob = PROVISIONAL_RUNNER_BLOB if provisional else PINNED_RUNNER_BLOB
    if runner is None or runner[0] != "100755" or runner[1] != "blob" or runner[2] != expected_runner_blob:
        issues.append("TREE_PROOF:runner")
    return sorted(issues)


def regular_path_issues() -> list[str]:
    issues: list[str] = []
    for path in ALLOWLIST:
        candidate = ROOT / path
        if candidate.is_symlink() or any(parent.is_symlink() for parent in candidate.parents if parent.exists()) or not candidate.is_file():
            issues.append(f"PATH_SHAPE:{path}")
    return sorted(issues)


def load_event() -> Any:
    event_path = os.environ.get("GITHUB_EVENT_PATH", "")
    if not event_path:
        raise ValueError("event path missing")
    path = Path(event_path)
    if not path.is_absolute():
        raise ValueError("event path not absolute")
    return load_data(path)


def repository_matches(event: Any) -> bool:
    return isinstance(event, dict) and isinstance(event.get("repository"), dict) and event["repository"].get("full_name") == REPOSITORY_FULL_NAME


def clean_checkout() -> bool:
    return not git("status", "--porcelain").stdout.strip()


def ci_event_context() -> str:
    event = load_event()
    if not repository_matches(event):
        raise RuntimeError("repository")
    event_name = os.environ.get("GITHUB_EVENT_NAME")
    if event_name == "pull_request":
        pull = event.get("pull_request")
        if not isinstance(pull, dict) or not isinstance(pull.get("base"), dict) or not isinstance(pull.get("head"), dict):
            raise RuntimeError("pull payload")
        return classify_pr_context(pull["base"].get("sha"), pull["head"].get("ref"))
    if event_name == "push":
        before = event.get("before")
        if not is_oid(before):
            raise RuntimeError("push base")
        if before in APPROVED_BASES:
            return HISTORICAL_CONTEXT
        if before == REPAIR_BASE:
            return REPAIR_CONTEXT
        return SUCCESSOR_CONTEXT
    raise RuntimeError("event type")


def execution_context() -> str:
    if os.environ.get("CI") == "true" or os.environ.get("GITHUB_ACTIONS") == "true":
        if os.environ.get("CI") != "true" or os.environ.get("GITHUB_ACTIONS") != "true":
            raise RuntimeError("partial CI environment")
        return ci_event_context()
    return local_context()


def ci_context_issues() -> list[str]:
    issues: list[str] = []
    if os.environ.get("CI") != "true" or os.environ.get("GITHUB_ACTIONS") != "true" or not clean_checkout():
        return ["CI_CONTEXT:environment_or_cleanliness"]
    try:
        event = load_event()
        checkout = git("rev-parse", "HEAD").stdout.strip()
        tree_oid, parents = raw_commit()
        event_name = os.environ.get("GITHUB_EVENT_NAME")
        if not repository_matches(event):
            raise RuntimeError("repository")
        if event_name == "pull_request":
            pull = event.get("pull_request")
            if not isinstance(pull, dict):
                raise RuntimeError("pull payload")
            base, head = pull.get("base"), pull.get("head")
            if not isinstance(base, dict) or not isinstance(head, dict):
                raise RuntimeError("pull base/head")
            for side in (base, head):
                if not isinstance(side.get("repo"), dict) or side["repo"].get("full_name") != REPOSITORY_FULL_NAME:
                    raise RuntimeError("fork")
            base_sha, head_sha = base.get("sha"), head.get("sha")
            context = classify_pr_context(base_sha, head.get("ref"))
            synthetic_merge = parents == [base_sha, head_sha]
            direct_head = checkout == head_sha
            if (
                base.get("ref") != "main"
                or not is_oid(head_sha)
                or not (direct_head or synthetic_merge)
                or (direct_head and context != HISTORICAL_CONTEXT and (not commit_available(base_sha) or not is_ancestor(base_sha, checkout)))
            ):
                raise RuntimeError("pull checkout")
            changed_files = pull.get("changed_files")
            if context == HISTORICAL_CONTEXT:
                if type(changed_files) is not int or changed_files != len(ALLOWLIST):
                    raise RuntimeError("pull exactness")
                issues.extend(committed_tree_issues(base_sha))
            elif context == REPAIR_CONTEXT:
                if type(changed_files) is not int or changed_files != len(REPAIR_ALLOWLIST):
                    raise RuntimeError("repair pull exactness")
                issues.extend(committed_tree_issues(APPROVED_SUCCESSOR_BASE))
                issues.extend(successor_protected_issues())
                issues.extend(regular_path_issues())
            else:
                if type(changed_files) is not int or changed_files < 1:
                    raise RuntimeError("future pull metadata")
                issues.extend(successor_protected_issues())
                issues.extend(regular_path_issues())
        elif event_name == "push":
            before, after = event.get("before"), event.get("after")
            if event.get("ref") != "refs/heads/main" or not is_oid(before) or after != checkout or event.get("created") is not False or event.get("deleted") is not False or event.get("forced") is not False:
                raise RuntimeError("push exactness")
            commits, head_commit = event.get("commits"), event.get("head_commit")
            if not isinstance(commits, list) or not commits or len(commits) > MAX_PUSH_COMMITS or not isinstance(head_commit, dict) or head_commit.get("id") != after or head_commit.get("tree_id") != tree_oid:
                raise RuntimeError("push commits")
            ids: list[str] = []
            path_metadata_presence: bool | None = None
            added: set[str] = set()
            modified: set[str] = set()
            removed: set[str] = set()
            for row in commits:
                if not isinstance(row, dict) or not is_oid(row.get("id")) or not is_oid(row.get("tree_id")) or not isinstance(row.get("distinct"), bool):
                    raise RuntimeError("push commit row")
                ids.append(row["id"])
                present = [key in row for key in ("added", "modified", "removed")]
                if any(present) and not all(present):
                    raise RuntimeError("partial path metadata")
                has_paths = all(present)
                if path_metadata_presence is None:
                    path_metadata_presence = has_paths
                elif path_metadata_presence != has_paths:
                    raise RuntimeError("inconsistent path metadata")
                if has_paths:
                    row_seen: set[str] = set()
                    for key, aggregate in (("added", added), ("modified", modified), ("removed", removed)):
                        values = row[key]
                        if not isinstance(values, list):
                            raise RuntimeError("path metadata type")
                        for value in values:
                            path = safe_repo_path(value)
                            if path in row_seen:
                                raise RuntimeError("overlapping commit path")
                            row_seen.add(path)
                            aggregate.add(path)
            if len(set(ids)) != len(ids) or ids[-1] != after or commits[-1].get("tree_id") != tree_oid:
                raise RuntimeError("push relations")
            if before in APPROVED_BASES:
                if len(commits) < 2 or len(parents) != 2 or parents[0] != before or parents[1] not in ids:
                    raise RuntimeError("integration source relation")
                if path_metadata_presence and (added != set(BASE_ABSENT_PATHS) or modified != {"scripts/test.sh"} or removed):
                    raise RuntimeError("integration path metadata")
                issues.extend(committed_tree_issues(before))
            elif before == REPAIR_BASE:
                if len(commits) < 2 or len(parents) != 2 or parents[0] != before or parents[1] not in ids:
                    raise RuntimeError("repair integration source relation")
                if not path_metadata_presence or added or modified != set(REPAIR_ALLOWLIST) or removed:
                    raise RuntimeError("repair integration path metadata")
                issues.extend(committed_tree_issues(APPROVED_SUCCESSOR_BASE))
                issues.extend(successor_protected_issues())
                issues.extend(regular_path_issues())
            else:
                direct = parents == [before]
                merged = len(parents) == 2 and parents[0] == before and parents[1] in ids
                if not (direct or merged):
                    raise RuntimeError("future integration parent relation")
                if not path_metadata_presence:
                    raise RuntimeError("future path metadata missing")
                touched = added | modified | removed
                if touched & set(PROTECTED_PATHS):
                    raise RuntimeError("future protected path metadata")
                issues.extend(successor_protected_issues())
                issues.extend(regular_path_issues())
        else:
            raise RuntimeError("event type")
    except Exception as exc:
        issues.append(f"CI_CONTEXT:{type(exc).__name__}")
    return sorted(set(issues))


def git_context_issues() -> list[str]:
    if os.environ.get("CI") == "true" or os.environ.get("GITHUB_ACTIONS") == "true":
        return ci_context_issues()
    if not clean_checkout():
        return ["GIT_CONTEXT:dirty_checkout"]
    try:
        context = local_context()
    except Exception as exc:
        return [f"GIT_CONTEXT:{type(exc).__name__}"]
    issues = regular_path_issues()
    if context == HISTORICAL_CONTEXT:
        try:
            base = approved_base_for_head()
            issues.extend(base_shape_issues(base))
            if changed_paths(base) != ALLOWLIST:
                issues.append("ALLOWLIST_ACTUAL_DIFF")
        except Exception as exc:
            issues.append(f"GIT_CONTEXT:{type(exc).__name__}")
    elif context == REPAIR_CONTEXT:
        if diff_paths(REPAIR_BASE) != REPAIR_ALLOWLIST:
            issues.append("REPAIR_ALLOWLIST_ACTUAL_DIFF")
        issues.extend(committed_tree_issues(APPROVED_SUCCESSOR_BASE))
        issues.extend(successor_protected_issues())
    else:
        issues.extend(successor_protected_issues())
    return sorted(set(issues))


def runner_issues(context: str | None = None) -> list[str]:
    try:
        text = safe_file(ROOT / "scripts/test.sh").decode("utf-8")
    except Exception as exc:
        return [f"RUNNER:{type(exc).__name__}"]
    provisional = any(value == "TO_BE_FINALIZED" for value in DIGESTS.values())
    suffix = " --allow-unpinned" if provisional else ""
    required = [
        'ft_rb_02_inquiry_validator="repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py"',
        f'"$python" "$ft_rb_02_inquiry_validator"{suffix}',
        f'"$python" "$ft_rb_02_inquiry_validator" --registry tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/valid-synthetic.yaml --synthetic{suffix}',
        '"$python" -B -m unittest tests.test_ft_rb_02_inquiry_crm_flow_readiness',
    ]
    runner_lines = text.splitlines()
    issues = [f"RUNNER:dispatch:{line}" for line in required if runner_lines.count(line) != 1]
    if context is None:
        try:
            context = execution_context()
        except Exception as exc:
            issues.append(f"RUNNER:context:{type(exc).__name__}")
    if context in {HISTORICAL_CONTEXT, REPAIR_CONTEXT}:
        expected_blob = PROVISIONAL_RUNNER_BLOB if provisional else PINNED_RUNNER_BLOB
        if expected_blob in {"TO_BE_RECOMPUTED", "TO_BE_FINALIZED"} or git_blob_oid(ROOT / "scripts/test.sh") != expected_blob:
            issues.append("RUNNER:exact_blob")
        available_bases = [base for base in APPROVED_BASES if base_available(base)]
        context_base: str | None = None
        if available_bases:
            try:
                context_base = approved_base_for_head()
            except Exception as exc:
                issues.append(f"RUNNER:base_context:{type(exc).__name__}")
        if context_base is not None:
            base = git("show", f"{context_base}:scripts/test.sh", check=False)
            anchor = '"$python" -B -m unittest tests.test_ft_rb_01_rights_safe_media_readiness\n\n'
            block = (
                '# FT-RB-02 pre-pin Inquiry/CRM readiness validation and focused/adversarial dispatch.\n'
                'ft_rb_02_inquiry_validator="repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py"\n'
                f'"$python" "$ft_rb_02_inquiry_validator"{suffix}\n'
                f'"$python" "$ft_rb_02_inquiry_validator" --registry tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/valid-synthetic.yaml --synthetic{suffix}\n'
                '"$python" -B -m unittest tests.test_ft_rb_02_inquiry_crm_flow_readiness\n\n'
            )
            if base.returncode or base.stdout.count(anchor) != 1 or text != base.stdout.replace(anchor, anchor + block, 1):
                issues.append("RUNNER:exact_transform")
    elif context == SUCCESSOR_CONTEXT:
        if text.count(RUNNER_SLOT_START) != 1 or text.count(RUNNER_SLOT_END) != 1:
            issues.append("RUNNER:successor_slot")
        else:
            prefix, remainder = text.split(RUNNER_SLOT_START, 1)
            inserted, suffix_text = remainder.split(RUNNER_SLOT_END, 1)
            if hashlib.sha256((prefix + RUNNER_SLOT_START).encode()).hexdigest() != RUNNER_PREFIX_SHA256:
                issues.append("RUNNER:successor_prefix")
            if hashlib.sha256((RUNNER_SLOT_END + suffix_text).encode()).hexdigest() != RUNNER_SUFFIX_SHA256:
                issues.append("RUNNER:successor_suffix")
            if inserted and (not inserted.endswith("\n\n") or "ft_rb_02_inquiry_validator" in inserted or "tests.test_ft_rb_02_inquiry_crm_flow_readiness" in inserted):
                issues.append("RUNNER:successor_insertion")
    else:
        issues.append("RUNNER:invalid_context")
    if not provisional and "--allow-unpinned" in "\n".join(line for line in text.splitlines() if "ft_rb_02_inquiry_validator" in line):
        issues.append("RUNNER:allow_unpinned")
    return sorted(issues)


def protected_owner_issues(contract: Any) -> list[str]:
    issues: list[str] = []
    if (
        not isinstance(contract, dict)
        or contract.get("dependencies") != DEPENDENCIES
        or contract.get("dependency_pins") != PINS
        or contract.get("owner_documents") != OWNER_FILES
        or contract.get("owner_document_pins") != OWNER_PINS
    ):
        issues.append("CONTRACT_PROTECTED_OWNER_MAP")
    for key, relative in DEPENDENCIES.items():
        try:
            if digest(load_data(ROOT / relative)) != PINS[key]:
                issues.append(f"DEPENDENCY_PIN:{key}")
        except Exception as exc:
            issues.append(f"DEPENDENCY_PIN:{key}:{type(exc).__name__}")
    for key, relative in OWNER_FILES.items():
        try:
            if git_blob_oid(ROOT / relative) != OWNER_PINS[key]:
                issues.append(f"OWNER_BLOB_PIN:{key}")
        except Exception as exc:
            issues.append(f"OWNER_BLOB_PIN:{key}:{type(exc).__name__}")
    return sorted(issues)


def c009_owner_issues() -> tuple[list[str], set[str]]:
    try:
        owner = load_data(C009)
        promotion = owner["promotion"]
        ids = {
            promotion["target_pilot_id"],
            promotion["canonical_combination"]["combination_id"],
            promotion["canonical_leaf"]["entity"]["entity_id"],
        }
        if len(ids) != 3 or not all(isinstance(item, str) for item in ids):
            raise ValueError("owner IDs")
        return [], ids
    except Exception as exc:
        return [f"C009_OWNER:{type(exc).__name__}"], set()


def leakage_issues(ids: set[str]) -> list[str]:
    issues: list[str] = []
    governed = [ROOT / relative for relative in BASE_ABSENT_PATHS]
    suffixes = {item.rsplit(":", 1)[-1] for item in ids}
    for path in governed:
        try:
            text = safe_file(path).decode("utf-8")
        except Exception as exc:
            issues.append(f"STABLE_ID_LEAK:{path.name}:{type(exc).__name__}")
            continue
        if any(item in text for item in ids | suffixes):
            issues.append(f"STABLE_ID_LEAK:{path.name}")
        stable_prefixes = ("pi" + "lot", "pc" + "omb", "prd" + ":sku")
        stable_pattern = r"(?<![A-Za-z0-9_])(?:" + "|".join(re.escape(item) for item in stable_prefixes) + r"):[A-Za-z0-9][A-Za-z0-9._:-]*"
        if re.search(stable_pattern, text):
            issues.append(f"STABLE_ID_PATTERN:{path.name}")
        if re.search(r"(?<!\d)09\d{9}(?!\d)", text):
            issues.append(f"PII_SURFACE:iranian_mobile:{path.name}")
        international_mobile = r"(?<!\d)(?:" + re.escape("+" + "98") + r"|00" + "98" + r")9\d{9}(?!\d)"
        if re.search(international_mobile, text):
            issues.append(f"PII_SURFACE:international_iranian_mobile:{path.name}")
        for email in re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text):
            if not email.endswith("@example.invalid"):
                issues.append(f"PII_SURFACE:email:{path.name}")
        if re.search(r"AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", text):
            issues.append(f"SECRET_SURFACE:{path.name}")
        for url in re.findall(r"https?://[^\s\"'<>]+", text):
            if ".invalid" not in url and "json-schema.org" not in url:
                issues.append(f"ENDPOINT_SURFACE:{path.name}")
    return sorted(issues)


def pii_issues(data: Any, *, synthetic: bool) -> list[str]:
    text = json.dumps(data, ensure_ascii=False, sort_keys=True)
    issues: list[str] = []
    if re.search(r"(?<!\d)09\d{9}(?!\d)", text):
        issues.append("PII_FIXTURE:iranian_mobile")
    international_mobile = r"(?<!\d)(?:" + re.escape("+" + "98") + r"|00" + "98" + r")9\d{9}(?!\d)"
    if re.search(international_mobile, text):
        issues.append("PII_FIXTURE:international_iranian_mobile")
    for email in re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text):
        if not email.endswith("@example.invalid"):
            issues.append("PII_FIXTURE:email")
    if synthetic and any(token in text for token in ("Masoud Tavousi", "مسعود طاووسی")):
        issues.append("PII_FIXTURE:person")
    return sorted(set(issues))


def semantic_issues(contract: Any, schema: Any, registry: Any, *, synthetic: bool) -> list[str]:
    issues: list[str] = []
    if digest(contract) != EXPECTED_CONTRACT_DIGEST:
        issues.append("CONTRACT_EXACTNESS")
    if digest(schema) != EXPECTED_SCHEMA_DIGEST:
        issues.append("SCHEMA_EXACTNESS")
    if not isinstance(registry, dict):
        return issues + ["REGISTRY_TYPE"]
    expected_keys = [
        "registry_id", "registry_version", "mission_id", "fixture_mode", "fixture_identity",
        "campaign_authorized_starting_main", "mission_base_main", "status_as_of", "source", "source_policy",
        "exact_changed_paths", "owner_model", "canonical_slice_binding", "readiness", "customer_form",
        "city_reconciliation", "future_payload_contract", "inquiry_record_policy", "state_planes", "lead_stage_vocabulary",
        "supply_check_policy", "deduplication_delivery", "consent_privacy", "form_security_requirements",
        "analytics_boundary", "missing_authority_inputs", "no_claim_boundaries", "gate_snapshot", "c002_snapshot",
    ]
    if list(registry) != expected_keys:
        issues.append("REGISTRY_KEYS_OR_ORDER")
    mode = "SYNTHETIC" if synthetic else "CANONICAL"
    identity = "SYNTHETIC_FTRB02_INQUIRY_CRM" if synthetic else "CANONICAL_FTRB02_INQUIRY_CRM"
    timestamp = "2026-08-24T00:15:01+03:30" if synthetic else "2026-08-24T00:15:00+03:30"
    if registry.get("fixture_mode") != mode:
        issues.append("FIXTURE_MODE")
    if registry.get("fixture_identity") != identity:
        issues.append("FIXTURE_IDENTITY")
    if registry.get("status_as_of") != timestamp:
        issues.append("STATUS_AS_OF")
    for key, expected in EXPECTED_SECTION_DIGESTS.items():
        if digest(registry.get(key)) != expected:
            issues.append(f"REGISTRY_EXACTNESS:{key}")
    if registry.get("exact_changed_paths") != ALLOWLIST:
        issues.append("ALLOWLIST_DECLARATION")
    return sorted(set(issues))


def package_digest_issues(contract: Any, schema: Any, registry: Any, *, synthetic: bool, allow_unpinned: bool) -> list[str]:
    issues: list[str] = []
    values = {"contract": digest(contract), "schema": digest(schema), "synthetic" if synthetic else "canonical": digest(registry)}
    for key, actual in values.items():
        expected = DIGESTS[key]
        if expected == "TO_BE_FINALIZED":
            if not allow_unpinned:
                issues.append(f"DIGEST_UNPINNED:{key}")
        elif actual != expected:
            issues.append(f"DIGEST_MISMATCH:{key}")
    return sorted(issues)


def validate_values(
    contract: Any,
    schema: Any,
    registry: Any,
    *,
    synthetic: bool = False,
    allow_unpinned: bool = False,
    check_git: bool = False,
    check_protected: bool = True,
    check_surfaces: bool = True,
) -> list[str]:
    issues: list[str] = []
    schema_errors = schema_issues(schema)
    issues.extend(schema_errors)
    if not schema_errors:
        try:
            validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
            for error in validator.iter_errors(registry):
                path = "/".join(str(item) for item in error.absolute_path)
                issues.append(f"SCHEMA_VALIDATION:{path or '$'}:{error.validator}")
        except Exception as exc:
            issues.append(f"SCHEMA_VALIDATION:{type(exc).__name__}")
    issues.extend(semantic_issues(contract, schema, registry, synthetic=synthetic))
    issues.extend(package_digest_issues(contract, schema, registry, synthetic=synthetic, allow_unpinned=allow_unpinned))
    if check_protected:
        issues.extend(protected_owner_issues(contract))
    owner_problems, ids = c009_owner_issues()
    issues.extend(owner_problems)
    if check_surfaces:
        issues.extend(leakage_issues(ids))
    issues.extend(pii_issues(registry, synthetic=synthetic))
    if check_git:
        issues.extend(git_context_issues())
        issues.extend(runner_issues())
    return sorted(set(issues))


def validate_all(registry_path: Path = REGISTRY, *, synthetic: bool = False, allow_unpinned: bool = False, check_git: bool = True) -> list[str]:
    try:
        contract = load_data(CONTRACT)
        schema = load_data(SCHEMA)
        registry = load_data(registry_path)
    except Exception as exc:
        return [f"LOAD:{type(exc).__name__}"]
    return validate_values(contract, schema, registry, synthetic=synthetic, allow_unpinned=allow_unpinned, check_git=check_git)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--allow-unpinned", action="store_true")
    args = parser.parse_args()
    original_socket = socket.socket

    def offline_socket(*_args: Any, **_kwargs: Any) -> Any:
        raise RuntimeError("network disabled")

    socket.socket = offline_socket
    try:
        registry_argument = args.registry
        registry_path = registry_argument.resolve()
        expected_registry = (SYNTHETIC if args.synthetic else REGISTRY).resolve()
        if (
            registry_argument.is_symlink()
            or any(parent.is_symlink() for parent in registry_argument.absolute().parents if parent.exists())
            or registry_path != expected_registry
        ):
            issues = ["CLI_REGISTRY_PATH"]
        else:
            issues = validate_all(expected_registry, synthetic=args.synthetic, allow_unpinned=args.allow_unpinned, check_git=True)
    finally:
        socket.socket = original_socket
    for issue in issues:
        print(issue)
    if issues:
        return 1
    print("FT-RB-02 Inquiry/CRM readiness validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
