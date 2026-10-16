# Content — spine

## Claims

- Manifest snapshots and code checks constrain replay.
- Every attempted candidate has a completed-step record, including division by zero.
- Ordered outcome comparison catches divergence even if the winner stays the same.
- Candidate ancestry and span nesting describe different relationships.

## Decisions

- Five serial candidates; score feedback selects the incumbent.
- Use a real arithmetic failure, not a simulated timeout.
- Retain partial predictions and null score for failed evaluation.
- Compare semantic outcomes while excluding execution IDs and timing.
- Keep detailed shell instructions outside rendered slide units.

## Open questions

- Production timeouts, crash recovery, and statistical equivalence need separate implementations.
- Further content edits will require another slide-fit check.

## Not doing

- Live LLM calls, tracing backends, full evolutionary search, and hidden model reasoning.
