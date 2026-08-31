from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "publication_manifest.json"

FORBIDDEN_PATH_PARTS = {
    "private",
    "runtime",
    "production",
    "prompts",
    "prompt_library",
    "orchestration",
    "deployment",
    "credentials",
    "secrets",
    "user_data",
    "internal_receipts",
}

FORBIDDEN_CONTENT_PATTERNS = {
    "private_repo_reference": re.compile(r"github\.com/rickdatascientist/pythiagrid(?:\.git|/|$)", re.IGNORECASE),
    "windows_private_path": re.compile(r"\b[A-Z]:\\(?:PythiaGrid|Users\\[^\\]+\\(?:\.ssh|AppData))", re.IGNORECASE),
    "private_key_material": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github_token": re.compile(r"\b(?:ghp_|github_pat_)[A-Za-z0-9_]{16,}"),
    "openai_style_secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    "generic_secret_assignment": re.compile(r"(?i)\b(?:password|passwd|api[_-]?key|access[_-]?token|secret)\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
}

TEXT_SUFFIXES = {"", ".md", ".json", ".py", ".yml", ".yaml", ".txt", ".toml"}
MAX_PUBLIC_FILE_BYTES = 200_000


def tracked_files() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files"],
            check=True,
            capture_output=True,
            text=True,
        )
        return sorted(line.strip() for line in result.stdout.splitlines() if line.strip())
    except (OSError, subprocess.CalledProcessError):
        return sorted(
            str(path.relative_to(ROOT)).replace("\\", "/")
            for path in ROOT.rglob("*")
            if path.is_file() and ".git" not in path.parts
        )


def main() -> int:
    failures: list[dict[str, str]] = []

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        print(json.dumps({"verdict": "FAIL", "failures": [{"code": "manifest_unreadable", "detail": str(exc)}]}, indent=2))
        return 1

    allowed_classes = set(manifest.get("allowed_classes", []))
    required_risk = manifest.get("required_reconstruction_risk", "LOW")
    declared = manifest.get("files", {})
    tracked = tracked_files()

    undeclared = sorted(set(tracked) - set(declared))
    stale = sorted(set(declared) - set(tracked))
    for path in undeclared:
        failures.append({"code": "unclassified_file", "detail": path})
    for path in stale:
        failures.append({"code": "manifest_entry_missing_file", "detail": path})

    for rel in tracked:
        meta = declared.get(rel)
        if not isinstance(meta, dict):
            continue

        if meta.get("class") not in allowed_classes:
            failures.append({"code": "invalid_public_class", "detail": rel})
        if meta.get("contains_private_implementation") is not False:
            failures.append({"code": "private_implementation_declared", "detail": rel})
        if meta.get("reconstruction_risk") != required_risk:
            failures.append({"code": "reconstruction_risk_not_low", "detail": rel})

        parts = {part.lower() for part in Path(rel).parts}
        forbidden_parts = sorted(parts & FORBIDDEN_PATH_PARTS)
        if forbidden_parts:
            failures.append({"code": "forbidden_path", "detail": f"{rel}: {','.join(forbidden_parts)}"})

        path = ROOT / rel
        try:
            size = path.stat().st_size
        except OSError as exc:
            failures.append({"code": "file_unreadable", "detail": f"{rel}: {exc}"})
            continue

        if size > MAX_PUBLIC_FILE_BYTES:
            failures.append({"code": "file_too_large_for_public_surface", "detail": f"{rel}: {size}"})

        if path.suffix.lower() not in TEXT_SUFFIXES:
            failures.append({"code": "binary_or_unapproved_file_type", "detail": rel})
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append({"code": "non_utf8_public_file", "detail": rel})
            continue

        # The publication policy necessarily names categories that must remain private.
        # Secret/private-identifier detection still applies to it except for the semantic
        # category names themselves, which are not secrets or implementation details.
        for name, pattern in FORBIDDEN_CONTENT_PATTERNS.items():
            match = pattern.search(text)
            if match:
                failures.append({"code": name, "detail": f"{rel}: {match.group(0)[:120]}"})

        if rel.endswith(".py") and not rel.startswith("tools/"):
            failures.append({"code": "executable_outside_reference_tools", "detail": rel})

    receipt = {
        "schema": "pgr.publication_gate_receipt.v1",
        "tracked_files": len(tracked),
        "classified_files": len(declared),
        "policy": manifest.get("policy"),
        "default_deny": True,
        "reconstruction_risk_required": required_risk,
        "failures": failures,
        "verdict": "PASS" if not failures else "FAIL",
        "claim_boundary": (
            "Checks manifest completeness, public classification, prohibited paths, file type/size, "
            "and configured secret/private-identifier leakage patterns. Semantic IP review remains required."
        ),
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
