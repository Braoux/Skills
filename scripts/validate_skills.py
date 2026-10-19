#!/usr/bin/env python3
"""Structural checks for SKILL.md files and related Markdown documentation.

Uses only Python's standard library. Does not evaluate an agent's behavior.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", re.DOTALL)
FIELD = re.compile(r"^([A-Za-z][A-Za-z_-]*):\s*(.*?)\s*$")
VALID_NAME = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
EXCLUDED = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if not any(parent.name in EXCLUDED for parent in p.parents)
    )


def check_fences(path: Path, content: str) -> list[str]:
    opened = None
    for line_no, line in enumerate(content.splitlines(), 1):
        match = FENCE.match(line)
        if not match:
            continue
        marker, remainder = match.groups()
        if opened is None:
            opened = (marker[0], len(marker), line_no)
        elif marker[0] == opened[0] and len(marker) >= opened[1] and not remainder.strip():
            opened = None
    if opened is not None:
        return [f"{path}: unclosed Markdown fence at line {opened[2]}"]
    return []


def check_links(path: Path, content: str) -> list[str]:
    errors = []
    for link in LINK.findall(content):
        destination = link.strip().split(" ", 1)[0].strip("<>")
        if not destination or destination.startswith(("#", "/", "//")):
            continue
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f"{path}: broken local link: {destination}")
    return errors


def main() -> int:
    errors = []
    names = {}
    documents = markdown_files()
    skills = [p for p in documents if p.name == "SKILL.md"]
    if not skills:
        errors.append("No SKILL.md found")

    for path in skills:
        content = path.read_text(encoding="utf-8")
        match = FRONTMATTER.match(content)
        if match is None:
            errors.append(f"{path}: YAML frontmatter must start at the first byte")
            continue
        fields = {}
        for line in match.group(1).splitlines():
            m = FIELD.match(line)
            if m:
                fields[m.group(1)] = m.group(2).strip().strip("\"'")
        name = fields.get("name", "")
        description = fields.get("description", "")
        if not VALID_NAME.fullmatch(name):
            errors.append(f"{path}: invalid or missing skill name: {name!r}")
        if not description:
            errors.append(f"{path}: missing skill description")
        if name in names:
            errors.append(f"{path}: duplicate name {name!r} (also in {names[name]})")
        else:
            names[name] = path

    for path in documents:
        content = path.read_text(encoding="utf-8")
        errors.extend(check_fences(path.relative_to(ROOT), content))
        errors.extend(check_links(path, content))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1

    print(f"Validation passed: {len(skills)} skill(s), {len(documents)} Markdown file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
