# Contributing

Contributions should solve a clearly observed problem while preserving the scope of each skill.

## Before a change

1. Read the current `SKILL.md` and any adjacent guide.
2. Describe the actual failure or missing behavior, with a concrete task or example.
3. Keep the fix small. Do not duplicate responsibilities of existing skills.
4. Clearly separate facts, deductions, assumptions and unknowns.
5. Exercise the skill on representative simple, complex and ambiguous scenarios; document any behavior change.
6. Prefer concise core instructions and optional reference files when large guides can be safely split.

## File format

The YAML frontmatter must start at **the first byte** of `SKILL.md`, without a wrapping Markdown code fence:

~~~yaml
---
name: example-skill
description: Explains what this skill does and when it should be used.
---

# Example Skill
~~~

Use unique lowercase kebab-case identifiers and meaningful descriptions. New directories should use lowercase kebab-case; **legacy directory paths remain unchanged** until a documented migration.

## Validation

Run `python3 scripts/validate_skills.py` before opening a PR. This checks document structure and links, not the quality of agent decisions. Describe what was tested and what was not.

## Security and permission to publish

Never commit secrets, tokens, passwords or personal data. Do not publish internal architecture, business workflows, repository-derived functional descriptions or customer data without explicit permission from their owner. Keep generated client-specific artifacts in the authorized project workspace, not the reusable public skills collection.

Removing an already-public file does not remove it from Git history. Escalate suspected confidentiality exposures appropriately rather than assuming deletion is sufficient.

## Pull requests

Include the reason for the change, intended behavior, tests or scenarios, compatibility impact and any consciously deferred improvements.
