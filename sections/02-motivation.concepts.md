# Motivation — spine

## Purpose

Say WHY reproducibility and observability matter specifically for agentic
development, and bound where the investment is (and isn't) worth it.

## Claims

- Agents break the "same input, same output" assumption ordinary debugging
  relies on, via three independent sources of variance: model sampling,
  non-deterministic tool results, and multi-step chains that separate cause
  from visible symptom.
- Without observability, a user-reported failure cannot be inspected, only
  guessed at by attempted re-runs that a non-deterministic model may not even
  reproduce.
- Without reproducibility, every prompt or tool change is an unverifiable guess
  — there is no stored comparison point to check it against.
- The investment does not pay off uniformly: a single-call, stateless,
  low-stakes agent gains little; the case strengthens with chain length,
  user-reported (vs. test-caught) failures, and decision stakes.

## Decisions

- Used one running scenario (support agent citing a nonexistent policy) for
  "what goes wrong" rather than several short vignettes — rejected a bulleted
  list of failure types because a single concrete case a reader can picture is
  more persuasive than a taxonomy, per this template's own guidance.
- Split "why it matters" (the mechanism: three sources of variance) from "what
  goes wrong" (the consequence, dramatized) rather than merging them — keeps
  each `##` to one idea and one slide.
- Stated an explicit boundary condition in § When to reach for it rather than
  implying the technique is universally worth its cost — matches the audience
  reviewer's expectation that a technique states its own limits.

## Open questions

- Whether the "when to reach for it" heuristic (trace first, add pinned
  reproducibility once a failure class recurs) should be sharpened into a more
  concrete rule of thumb, or is honestly as firm as current practice gets.

## Not doing

- Not quantifying instrumentation overhead (latency/cost numbers) — those are
  implementation- and vendor-specific and would date quickly; the tradeoff is
  named qualitatively instead.
- Not covering multi-*agent* orchestration failure modes (e.g., two agents
  disagreeing) as a separate motivation — treated as one more instance of
  "chains separate cause from symptom," not a distinct case.
