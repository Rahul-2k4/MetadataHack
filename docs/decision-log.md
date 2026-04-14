# Decision Log

## 2026-04-15 - Docs Skeleton Baseline

### Decision

Create a focused documentation skeleton for hackathon execution and submission quality.

### Why

The hackathon judges include presentation quality and technical excellence; a structured doc system improves consistency and reduces last-day submission risk.

### Impact

- Clear owner-visible checklist for submission readiness.
- Faster alignment between README, demo, and architecture narrative.
- Lower risk of scope drift outside hackathon requirements.

### Follow-up

Add dated entries here whenever we make major submission-shaping decisions.

## 2026-04-15 - Umbrella Structure and Content Policy

### Decision

- Adopt umbrella structure A:
  - `docs/`
  - `projects/main-submission/`
  - `projects/experiments/`
  - `assets/`
- Keep repository content restricted to hackathon docs, hackathon code, and submission assets.

### Why

This keeps collaboration clean for a 2-person team and reduces accidental scope drift from non-hackathon notes.

### Impact

- One stable lane for the active submission candidate
- Parallel experiment lanes without destabilizing `main-submission`
- Clear admissible-content boundary for all commits

## 2026-04-15 - Offline Hackathon Knowledge Pack

### Decision

Mirror hackathon rules, schedule, resources, and track references into repo docs so the team does not need constant website lookups.

### Why

Centralized in-repo references reduce context switching and keep teammates aligned during implementation.

### Impact

- Added `docs/hackathon-rules.md`, `docs/hackathon-resources.md`, `docs/hackathon-schedule.md`, and `docs/ideas-tracks.md`
- Expanded `docs/index.md` and `docs/hackathon-brief.md` to link the snapshot set
