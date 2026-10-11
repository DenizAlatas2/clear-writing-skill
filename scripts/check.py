#!/usr/bin/env python3
"""Local packaging, fixture, link, and obvious disclosure checks.

Run gh skill publish --dry-run separately for Agent Skills schema validation.
This checker does not measure writing quality or guarantee absence of secrets.
"""

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "clear-writing"
errors = []

for relative in ["README.md", "LICENSE", "docs/sources.md", "evals/cases.json",
                 "evals/protocol.md", "skills/clear-writing/SKILL.md",
                 "skills/clear-writing/LICENSE",
                 "skills/clear-writing/references/examples.md"]:
    if not (ROOT / relative).is_file():
        errors.append(f"Missing file: {relative}")

if (ROOT / "LICENSE").read_bytes() != (SKILL / "LICENSE").read_bytes():
    errors.append("Installable license differs from the project license")

cases = json.loads((ROOT / "evals/cases.json").read_text())
ids = [case["id"] for case in cases]
if len(ids) != len(set(ids)):
    errors.append("Duplicate evaluation case IDs")
for case in cases:
    if case["language"] not in {"de", "en"} or case["mode"] not in {"draft", "revise"}:
        errors.append(f"Invalid evaluation metadata: {case['id']}")
    if not case["prompt"].strip() or not case["invariants"]:
        errors.append(f"Empty evaluation case: {case['id']}")

secret_patterns = [
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{30,}"),
    re.compile(r"AKIA[A-Z0-9]{16}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"/(?:Users|home)/[A-Za-z0-9_.-]+/"),
    re.compile(r"<source[_]thread_id>"),
    re.compile(r"chatgpt[.]com/space/"),
]
files = [p for p in ROOT.rglob("*")
         if p.is_file() and ".git" not in p.relative_to(ROOT).parts
         and "__pycache__" not in p.parts and p.name != ".DS_Store"]
for path in files:
    relative = path.relative_to(ROOT)
    if path.is_symlink():
        errors.append(f"Unexpected symlink: {relative}")
        continue
    if path.name in {".env", "auth.json", "credentials", "id_rsa", "id_ed25519"}:
        errors.append(f"Unexpected sensitive file: {relative}")
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeError:
        errors.append(f"Unexpected non-text file: {relative}")
        continue
    for pattern in secret_patterns:
        if pattern.search(text):
            errors.append(f"Potential secret or private path in {relative}")
    if path.suffix == ".md":
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if re.match(r"https?://|#", target):
                continue
            local_target = target.split("#", 1)[0]
            if not (path.parent / local_target).is_file():
                errors.append(f"Broken local link in {relative}: {target}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Checked {len(files)} text files and {len(cases)} synthetic cases.")
print("Packaging, local links, and obvious disclosure checks passed.")
print("No writing-quality or complete privacy claim follows from this check.")
