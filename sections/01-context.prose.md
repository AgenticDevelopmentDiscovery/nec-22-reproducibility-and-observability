## A Correct Answer is Only the Beginning {#r01}

An agent returns a convincing result. Its intermediate actions are missing.

::: {.standalone-question}

:::: {.standalone-prompt}
If an AI agent produces the correct final answer, do we still need to know how it got there?
::::

- **A.** No, the correct final result is all that matters.
- **B.** Yes: to verify inputs, reproduce execution, or investigate unexpected behavior.
- **C.** Only when the agent produces an incorrect answer.
:::

## A Correct Answer is Only the Beginning {#r02}

::: {.standalone-answer}
**ANSWER — B is strongest for our experiments**

- A correct output does not establish reproducibility or reliability.
- We need evidence about inputs, actions, and failures.
- Today: capture a run, replay it, and explain a difference.
:::

::: {.standalone-detail}
An equation that fits yesterday's observations might receive a different score today. The final equation alone cannot tell us whether the data, code, or evaluation changed. Our offline example makes those alternatives inspectable without requiring an API key.
:::

## Why it matters for agentic development {#r03}

Deterministic software is easier to replay under controlled conditions.
External inputs and concurrency can also make ordinary software vary.

Agent workflows can introduce three additional debugging difficulties:

- The model *samples* its output, so asking it the same question twice can give two different answers even with nothing else changed.
- A tool it calls — a web search, a retrieval index, another service — can return a different result on the next call regardless of what the agent does.
- The agent's real output is the product of a *chain* of such calls, so the step that actually went wrong is often several steps upstream of the one where the wrong answer became visible.

::: {.detail}
Observability and reproducibility exist to answer exactly the question a stack trace answers for ordinary code, for a system where that trick no longer works.
:::

## What goes wrong without it {#r04}

 Without a trace, the output is the entire evidence: one cannot
see what the agent searched for, what the search actually returned, or which
part of the returned text the model misread.

- One can only re-run the agent on a similar-sounding question and hope to hit the same failure, which a non-deterministic model may simply not reproduce for you.
- Without a stored trace to compare against, there is no way to check whether a change made a class of failure more or less common — only an impression, formed from whichever cases happened to be
noticed.

An agent operating without observability is a system whose only debugging signal is what a user happened to report, and whose only evidence for whether a change helped is how the team feels about it afterward.

## Observability {#r05}

**Observability** is instrumenting an agent's execution so that after a run
finishes, one can see what it actually did.

- Every call to a language model, every call to a tool, every intermediate plan, retry, or sub-agent hand-off, each timestamped and carrying its inputs, outputs, and metadata.

In practice this record takes the shape of a *trace* — a tree of *spans*, one per step, nested to show which call happened inside which.

Observability answers "what happened here?" after the fact.

## Reproducibility {#r06}
**Reproducibility** is the
 ability to re-create a run, or enough of one, that a fix
can be tested against the same conditions that produced a failure

- Pinning the model version, fixing the sampling parameters, recording tool responses so they can be replayed instead of called live again, and versioning the prompts that
drove the run.

Reproducibility answers "can I make that happen again on purpose?" so a
proposed fix can be checked rather than guessed at.

## What goes wrong without it {#r07}

 Without a trace, the output is the entire evidence: one cannot
see what the agent searched for, what the search actually returned, or which
part of the returned text the model misread.

- One can only re-run the agent on a similar-sounding question and hope to hit the same failure, which a non-deterministic model may simply not reproduce for you.
- Without a stored trace to compare against, there is no way to check whether a change made a class of failure more or less common — only an impression, formed from whichever cases happened to be
noticed.

An agent operating without observability is a system whose only debugging signal is what a user happened to report, and whose only evidence for whether a change helped is how the team feels about it afterward.

## When to reach for it {#r08}

The cost of instrumenting and pinning a run is not free, so it should scale with what is at stake.

- A single-call, stateless agent (a one-shot summarizer with no tools) has little to gain: a bad output is trivial to inspect directly.

The case for full tracing and reproducibility strengthens sharply once:

- An agent chains multiple tool calls, once its failures are reported by users rather than caught in testing
- Its decisions carry enough weight — financial, medical, safety-relevant — that someone must be able to answer "why did it do that" after the fact.

::: {.detail}
Between those extremes, a reasonable default is to trace first and treat pinned, replayable reproduction as something you add once a class of failure has actually shown up twice.
:::

## How it works: a trace is a tree of spans {#r09}

- A **span** records one operation: inputs, outputs, timing, and metadata.
- A **trace** connects the run's spans; nesting shows which call contains which.

![A trace for one support-agent run: a root span for the whole request, with child spans for the planning call, the doc-search tool call, and the drafting call. The tool-call span carries its own attributes — the query it sent and the raw response it got back — which is exactly the detail a final-answer-only log would discard.](figures/trace-tree.svg){#fig:trace width=85%}

::: {.detail}
- The unit of observability is the **span**: one step of execution recorded with its inputs, its outputs, when it started and ended, and whatever metadata matters later (model name, sampling parameters, token counts, the tool's arguments).
- A **trace** is
the tree those spans form for one agent run: a root span for the run as a
whole, with a child span for each step, nested to show which call happened
inside which.



This is the payoff of the tree structure: a bad final answer is one leaf of the
tree, but the tree also holds every intermediate step that led to it. Reading a
trace means walking from the root down, comparing each span's output against
what the next span used as input, until the mismatch appears.
:::

## Reproducibility levers, and their real limits {#r10}

Four things can be pinned or recorded to make a run re-creatable:

- **Model version.** Provider APIs update models behind a stable name; pin an
  exact snapshot identifier so "the same model" actually means the same model.
- **Sampling parameters.** Fix temperature and any seed the API accepts.
- **Prompt and tool versions.** Log which exact system prompt and tool
  definitions produced this run, the same way you would version application
  code.
- **Tool responses.** Record what a tool actually returned, so a re-run can
  replay that response instead of calling a live search index, API, or clock
  that may answer differently next time.

**None of these controls guarantees identical output.**

::: {.detail}
None of this guarantees bit-for-bit determinism.
Reproducibility here means enough of the run pinned that a fix
can be tested under the *same conditions* that produced the failure
— the same tool responses, the same prompt, a model that behaves the same
way in practice — not a guarantee of the identical output token for token.
:::
