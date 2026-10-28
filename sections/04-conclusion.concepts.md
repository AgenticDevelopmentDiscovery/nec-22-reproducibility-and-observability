# Conclusion — spine

## Purpose

Say what the reader can now do (must match topic.md's capability list and
03-content's claims exactly), point at what comes next in a sensible order,
and name what is genuinely still unsettled.

## Claims

- The four "what you can do now" items are a direct restatement of topic.md's
  "What the reader will be able to do" list and 03-content.concepts.md's
  claims — checked for exact agreement, not just similarity.
- "Where to go next" is ordered by dependency, not by interest: practice on
  your own agent first (needs nothing new), then evaluation (needs a new
  method this tutorial didn't teach), then multi-agent tracing (a
  generalization of what was just taught).
- "Open edges" names three genuinely unsettled things, not restated
  limitations: tooling/standards churn, the determinism ceiling being a fact
  about current inference infrastructure rather than an engineering gap, and
  the side-effect boundary on what can safely be replayed.

## Decisions

- Ordered "where to go next" as practice → evaluation → multi-agent, rejecting
  a pointer straight to "learn a tracing product," because the highest-value
  next step for this audience is exercising the mental model on their own
  code, not adopting tooling.
- Repeated the replay side-effect limit (read-only tools vs. side-effecting
  tools) here rather than in § Content's pitfalls — it's a boundary on the
  *capability* (what can be replayed at all), which belongs in Conclusion's
  "open edges," not a mistake a reader makes while using the tool, which is
  what Pitfalls is for.

## Open questions

- None outstanding for this section; the open edges named in the prose are the
  team's honest position, not placeholders.

## Not doing

- Not proposing a specific tool or curriculum for "learning evaluation next" —
  naming the topic and why it's next is enough; recommending a specific
  framework would date the document and isn't this tutorial's promise to keep.
