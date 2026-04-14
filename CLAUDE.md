# CLAUDE.md

This repository uses `AGENTS.md` as the canonical collaboration and coding policy.

## Priority

1. Follow `AGENTS.md` first.
2. Follow explicit user instructions in the current task.
3. Keep changes minimal, verifiable, and hackathon-scoped.

## Claude-Specific Operating Notes

- Start each task by checking `git status` and relevant files under `docs/` and `projects/`.
- Prefer direct edits over broad refactors.
- When adding or editing markdown, respect docs-scope rules from `tools/validate_docs_scope.py`.
- Before finalizing, run:

```bash
. .venv/bin/activate
python -m pytest tests/tools/test_validate_docs_scope.py -v
python tools/validate_docs_scope.py $(git diff --name-only --cached)
```

- Summaries to the user should include:
  - what changed,
  - what was verified,
  - any follow-up needed from teammate(s).
