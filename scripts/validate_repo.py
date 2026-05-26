#!/usr/bin/env python3
"""Validate the public workplace-boundary package."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "SAFETY.md",
    "DISCLAIMER.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "skills/workplace-pressure-patterns/SKILL.md",
    "skills/workplace-pressure-patterns/references/pressure_taxonomy.md",
    "skills/workplace-boundary-defense/SKILL.md",
    "skills/workplace-boundary-defense/references/defense_playbook.md",
    "evals/workplace-pressure-patterns.json",
    "evals/workplace-boundary-defense.json",
    "examples/standup_status_capture.md",
    "examples/meeting_minutes_correction.md",
    "examples/identity_rant_redirect.md",
    "examples/source_of_truth_correction.md",
    "examples/evidence_packet_addendum.md",
]

PRIVATE_PATH_PARTS = [
    "workplace-" + "adv" + "ersarial" + "-sim" + "ulator",
    "adv" + "ersarial" + "_simulation",
    "run_" + "red" + "team",
    "red" + "team",
]

PRIVATE_TEXT = [
    *PRIVATE_PATH_PARTS,
    "red" + "-team",
    "Red" + "-Team",
    "attack" + "-surface",
    "attack " + "capability",
    "attack" + "_capability",
    "\u963f\u4e09",
    "\u4e09\u54e5",
]


def iter_public_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        files.append(path)
    return files


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def check_required_files() -> None:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def check_forbidden_paths() -> None:
    bad: list[str] = []
    for path in iter_public_files():
        rel = path.relative_to(ROOT).as_posix()
        if any(part in rel for part in PRIVATE_PATH_PARTS):
            bad.append(rel)
    if bad:
        fail("forbidden public paths: " + ", ".join(bad))


def check_forbidden_text() -> None:
    bad: list[str] = []
    for path in iter_public_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for token in PRIVATE_TEXT:
            if token in text:
                bad.append(f"{path.relative_to(ROOT)} contains {token!r}")
    if bad:
        fail("forbidden public text: " + "; ".join(bad[:20]))


def check_skill_frontmatter() -> None:
    for rel in [
        "skills/workplace-pressure-patterns/SKILL.md",
        "skills/workplace-boundary-defense/SKILL.md",
    ]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
            fail(f"invalid skill frontmatter: {rel}")


def check_eval_json() -> None:
    for rel in ["evals/workplace-pressure-patterns.json", "evals/workplace-boundary-defense.json"]:
        try:
            json.loads((ROOT / rel).read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON in {rel}: {exc}")


def main() -> int:
    check_required_files()
    check_forbidden_paths()
    check_forbidden_text()
    check_skill_frontmatter()
    check_eval_json()
    print("OK: public workplace-boundary package validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
