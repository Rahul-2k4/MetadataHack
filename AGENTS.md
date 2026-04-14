# MetadataHack Agent Guide

Purpose: keep this repo submission-ready for the OpenMetadata hackathon while two teammates and AI agents work in parallel.

## Scope Rules (Non-Negotiable)

- Keep this repository hackathon-only.
- Allowed markdown locations:
  - `docs/`, `projects/main-submission/`, `projects/experiments/`, `assets/`, `.github/`
  - root control docs: `README.md`, `AGENTS.md`, `CLAUDE.md`
- Do not add personal notes, journals, or unrelated markdown.
- Do not move or rename top-level lanes without updating `docs/index.md` and `docs/decision-log.md`.

## Repository Contract

- `docs/`: source-of-truth for submission artifacts.
- `projects/main-submission/`: exactly one active candidate.
- `projects/experiments/`: parallel idea spikes (`exp-01-<name>`, `exp-02-<name>`, ...).
- `assets/`: screenshots, diagrams, and demo media used in submission docs.

## Implementation Practices

- Make small, focused commits with clear messages.
- Prefer improving existing files over introducing new structure.
- If behavior or architecture changes, update relevant docs in the same PR:
  - `docs/architecture.md`
  - `docs/demo-script.md`
  - `docs/submission-checklist.md`
  - `docs/decision-log.md`
- Keep `main` demoable; avoid landing half-finished flows in `projects/main-submission/`.

## Verification Before Commit

Run these before opening or updating a PR:

```bash
. .venv/bin/activate
python -m pytest tests/tools/test_validate_docs_scope.py -v
python tools/validate_docs_scope.py $(git diff --name-only --cached)
```

If the validator flags markdown outside allowed lanes, fix file placement before committing.

## Branch and PR Workflow

- Use short-lived branches: `feat/<name>/<scope>` or `docs/<name>/<scope>`.
- Open PRs instead of direct `main` pushes when collaborating.
- Fill `.github/pull_request_template.md` completely.
- Include runnable steps and proof (logs/screenshot) for behavior changes.

## Guardrails for AI Agents

- Do not rewrite large docs unless requested.
- Do not delete teammate-authored content without explicit instruction.
- Do not introduce new tooling unless required for the hackathon deliverable.
- If requirements are unclear, ask one targeted question and then proceed.
