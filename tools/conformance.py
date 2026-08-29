from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.metadata
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def semantic_errors(contract: str, instance: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract == "work_state":
        active = instance.get("active_count")
        limit = instance.get("wip_limit")
        if isinstance(active, int) and isinstance(limit, int) and active > limit:
            errors.append("active_count_exceeds_wip_limit")
        if instance.get("state") == "ANDON":
            blocker = instance.get("blocker")
            if not isinstance(blocker, str) or not blocker.strip():
                errors.append("andon_requires_nonempty_blocker")
    elif contract == "evidence_receipt":
        digest = instance.get("receipt_digest")
        if isinstance(digest, dict) and digest.get("algorithm") == "sha256" and isinstance(digest.get("value"), str):
            body = copy.deepcopy(instance)
            body.pop("receipt_digest", None)
            expected = sha256_bytes(canonical_json(body))
            if digest["value"] != expected:
                errors.append("receipt_digest_mismatch")
        else:
            errors.append("receipt_digest_unusable")
    return errors


def validate_case(spec: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    contract = case["contract"]
    if contract not in spec.get("$defs", {}):
        return {"id": case["id"], "contract": contract, "errors": ["unknown_contract"]}
    wrapper = {
        "$schema": spec["$schema"],
        "$defs": spec["$defs"],
        "$ref": f"#/$defs/{contract}",
    }
    validator = Draft202012Validator(wrapper)
    schema_errors = sorted(
        (e.message for e in validator.iter_errors(case["instance"])),
        key=str,
    )
    semantic = semantic_errors(contract, case["instance"])
    return {
        "id": case["id"],
        "contract": contract,
        "errors": schema_errors + semantic,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--fixtures", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    spec_path = Path(args.spec)
    fixtures_path = Path(args.fixtures)
    spec_bytes = spec_path.read_bytes()
    fixtures_bytes = fixtures_path.read_bytes()
    spec = json.loads(spec_bytes)
    fixtures = json.loads(fixtures_bytes)

    Draft202012Validator.check_schema(spec)

    results: list[dict[str, Any]] = []
    positive_pass = 0
    negative_pass = 0

    for case in fixtures.get("positive", []):
        result = validate_case(spec, case)
        result["expected"] = "VALID"
        result["verdict"] = "PASS" if not result["errors"] else "FAIL"
        positive_pass += result["verdict"] == "PASS"
        results.append(result)

    for case in fixtures.get("negative", []):
        result = validate_case(spec, case)
        result["expected"] = "INVALID"
        result["verdict"] = "PASS" if bool(result["errors"]) else "FAIL"
        negative_pass += result["verdict"] == "PASS"
        results.append(result)

    positive_total = len(fixtures.get("positive", []))
    negative_total = len(fixtures.get("negative", []))
    required_contracts = {"authority_envelope", "evidence_receipt", "work_state", "capability_adapter"}
    positive_contracts = {c["contract"] for c in fixtures.get("positive", [])}
    negative_contracts = {c["contract"] for c in fixtures.get("negative", [])}
    coverage_ok = required_contracts <= positive_contracts and required_contracts <= negative_contracts
    all_pass = positive_pass == positive_total and negative_pass == negative_total and coverage_ok

    receipt = {
        "schema": "pgr.conformance_receipt.v0_1",
        "card": "PGR-A05",
        "validator": {
            "package": "jsonschema",
            "version": importlib.metadata.version("jsonschema"),
            "draft": "2020-12",
        },
        "spec_sha256": sha256_bytes(spec_bytes),
        "fixtures_sha256": sha256_bytes(fixtures_bytes),
        "positive": {"pass": positive_pass, "total": positive_total},
        "negative": {"pass": negative_pass, "total": negative_total},
        "required_contract_coverage": coverage_ok,
        "cases": results,
        "claim_boundary": "Validates the EFAD v0.1 JSON Schema contracts plus the declared WIP, ANDON, and evidence-digest semantic invariants. It does not certify a model, agent, backend, or deployment.",
        "verdict": "PASS" if all_pass else "FAIL",
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
