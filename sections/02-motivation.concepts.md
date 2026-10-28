# Experiment preparation — spine

## Claims

- Symbolic regression seeks an equation fitting observations.
- The offline policy uses deterministic rules and a seeded offset, with incumbent feedback.
- A candidate replaces the incumbent only when valid and strictly better; c005 adds seed-7 offset +1 to c003 and loses.
- Evidence is saved before, during, and after search, not only at the end.
- MSE zero establishes exact fit to the recorded dataset, not generalization.
- Saving only a winner loses essential execution evidence.

## Decisions

- Retain the existing section pair; teach workflow and scoring before artifact formats.
- Q2 is open-ended and occurs before the live demonstration.
- Expand S03 and the existing workflow SVG to show initialization, logging, feedback, and finalization.
- Keep S04 focused on the MSE definition; add S04-attempts for all five attempts and incumbent decisions.
- Define candidate/incumbent, seed/budget/determinism, and JSONL/hash in context; keep detailed code mapping off the projector.
- Associate three records through a common run ID; do not depict files as executable pipeline stages.
- Put detailed arithmetic and schema descriptions in manuscript-only detail blocks.

## Open questions

- The actual C2 harness interface has not been provided; this remains a teaching stand-in.

## Not doing

- General symbolic-regression optimization or independent LLM proposal generation.
