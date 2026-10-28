# Content — spine

## Purpose

Teach the HOW: the trace/span mental model, the concrete reproducibility
levers and their real limits, a worked diagnosis, replay as a follow-on
capability, then the failure modes — so the reader can instrument and debug an
agent this tutorial never showed them.

## Claims

- Reader can describe an agent's execution as a trace: a tree of spans, each
  carrying inputs, outputs, timing, and metadata.
- Reader can name the four concrete reproducibility levers (model version,
  sampling parameters, prompt/tool versions, recorded tool responses) and
  state that none of them, even together, guarantee bit-for-bit determinism.
- Reader can read a trace top-to-bottom to localize which span caused a
  multi-step failure, rather than inspecting only the final output.
- Reader can turn a recorded failing trace into a targeted replay that tests a
  fix without re-running or re-paying for the whole chain.
- Reader can name the three practical pitfalls (sensitive data in traces,
  over-instrumentation, mistaking a clean trace for a correct one) and
  recognize each by its symptom.

## Decisions

- Used one continuous worked example (support agent, stale refund policy)
  across §§ "Using it" and "Going further" rather than a fresh case for
  replay — rejected a second scenario because reusing the same trace makes the
  replay section legible as a direct continuation ("take that same failing
  trace and...") instead of a new thing to onboard to. This resolves the open
  question topic.md left open in favor of one thread.
- Put the determinism caveat (floating-point non-associativity under batched
  inference) directly in § Reproducibility levers rather than deferring it to
  Pitfalls — it's a limit of the levers themselves, not a separate mistake a
  reader makes, so it belongs with the claim it qualifies.
- Chose one figure (the trace tree, § How it works) rather than one per
  section — matches figures/README.md's guidance that the mental-model figure
  in "how it works" is the one that earns its place; the worked example is
  instead shown as a text trace listing, since that IS the artifact a reader
  would actually see in a terminal or dashboard, not an abstraction needing a
  diagram.
- Presented the worked-example trace as a fenced text block rather than a
  screenshot of a real tracing tool — keeps it vendor-neutral and legible in
  all three render targets (a screenshot would be illegible on a slide).

## Open questions

- Whether to name specific tracing tools/standards (OpenTelemetry GenAI
  semantic conventions, a commercial LLM tracing product) anywhere in this
  section. Currently avoided entirely in favor of the underlying pattern,
  since tool-specific claims risk dating and the audience doesn't yet have a
  fixed toolchain to anchor to — but a pointer to "what this looks like in
  practice" may belong in § Conclusion's "where to go next" instead.
- Whether the pitfalls list needs a fourth entry on the false-determinism
  pitfall (treating temperature=0 as a guarantee) as its own item, separate
  from where it currently sits in § Reproducibility levers — leaning no, to
  avoid saying the same thing twice, but flagging it since a reviewer may
  disagree.

## Not doing

- Not covering multi-agent trace correlation (traces that span more than one
  agent talking to another agent) — the single-agent, multi-tool-call case is
  already enough to teach the mental model; multi-agent tracing is the same
  idea one level up and left as a natural next step, not new content.
- Not walking through instrumentation *code* (e.g., wrapping a function in a
  span-creation call) — the tutorial teaches the mental model and how to read
  and use a trace, not how to author one in a specific SDK, which would tie
  the tutorial to one framework's API.
