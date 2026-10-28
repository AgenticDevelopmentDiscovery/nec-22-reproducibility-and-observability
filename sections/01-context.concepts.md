# Context — spine

## Purpose

Say WHAT reproducibility and observability are, and where the ideas came from,
so the reader can hold both terms in mind before being told why agents need
them or how to build them.

## Claims

- Observability = instrumenting execution into an inspectable record (a trace:
  a tree of spans with inputs, outputs, timing, metadata) so a finished run can
  be examined after the fact.
- Reproducibility = the ability to re-create a run, or enough of one, that a fix
  can be tested against the conditions that produced a failure.
- The two are related but distinct: observability explains a past run;
  reproducibility lets you re-run it (or part of it) on purpose.
- Both concepts predate agents (observability from distributed systems,
  reproducibility from computational science) but agents combine and sharpen
  both problems at once.

## Decisions

- Defined observability and reproducibility as a pair up front, rather than one
  per section, because the tutorial's whole arc depends on the reader holding
  both distinctly — motivation, content, and conclusion all use the
  distinction repeatedly.
- Kept the "where it came from" history to distributed systems + computational
  science in two sentences, rejecting a longer history of APM/tracing tooling
  (Dapper, Zipkin, etc.) — the lineage matters, the vendor history does not,
  and naming tools here would duplicate § Content's reproducibility-levers
  discussion.
- Named what's explicitly out of scope (production monitoring, training
  reproducibility, evaluation/scoring) here rather than only in topic.md, so
  the prose itself sets the reader's expectations.

## Open questions

- Whether "trace" and "span" should be introduced here or held for § Content —
  currently introduced here at a definitional level, with the mechanics (tree
  structure, what a span carries) deferred to § Content's mental model.

## Not doing

- No survey of specific observability/tracing products — that's a § Content
  concern for the reproducibility-levers discussion, and only to the extent it
  serves the pattern, not a tool comparison.
- No history of how LLM agents themselves evolved (chatbots → tool use →
  multi-agent) — orthogonal to this topic; assumed as background the declared
  audience already has.
