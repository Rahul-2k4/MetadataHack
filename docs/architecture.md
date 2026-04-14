# Submission Architecture (Starter)

## Goal

Ship a demoable, judged-ready OpenMetadata-integrated project by submission deadline.

## System Boundaries

- **Hackathon app layer:** the feature we are submitting.
- **OpenMetadata integration layer:** API usage, entity/lineage/quality interactions.
- **Demo data/setup layer:** reproducible sample environment for judges.
- **Presentation layer:** README + demo flow aligned to judging criteria.

## Initial Technical Assumptions

- Keep setup steps short and reproducible.
- Prefer stable, documented OpenMetadata APIs over fragile internals.
- Capture one clear problem -> solution -> impact narrative in architecture decisions.

## Open Questions

- Which OpenMetadata entities and APIs are mandatory for the first demo cut?
- What local setup path gives the fastest judge onboarding?
- Which non-essential features should be deferred to protect demo reliability?
