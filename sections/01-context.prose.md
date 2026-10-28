## A Correct Answer is Only the Beginning

An agent returns a convincing result. Its intermediate actions are missing.

::: {.question}

:::: {.prompt}
If an AI agent produces the correct final answer, do we still need to know how it got there?
::::

- **A.** No, the correct final result is all that matters.
- **B.** Yes: to verify inputs, reproduce execution, or investigate unexpected behavior.
- **C.** Only when the agent produces an incorrect answer.
:::

## A Correct Answer is Only the Beginning

::: {.answer}
**ANSWER — B is strongest for our experiments**

- A correct output does not establish reproducibility or reliability.
- We need evidence about inputs, actions, and failures.
- Today: capture a run, replay it, and explain a difference.
:::

::: {.detail}
An equation that fits yesterday's observations might receive a different score today. The final equation alone cannot tell us whether the data, code, or evaluation changed. Our offline example makes those alternatives inspectable without requiring an API key.
:::

## Why it matters for agentic development

Ordinary programs are deterministic: the same input produces the same output,
so a stack trace or a debugger reliably points at the cause of a failure. 

An agent breaks that guarantee in three ways at once:

- The model *samples* its output, so asking it the same question twice can give two different answers even with nothing else changed. 
- A tool it calls — a web search, a retrieval index, another service — can return a different result on the next call regardless of what the agent does.
- The agent's real output is the product of a *chain* of such calls, so the step that actually went wrong is often several steps upstream of the one where the wrong answer became visible.

Observability and reproducibility exist to answer exactly the question a stack trace answers for ordinary code, for a system where that trick no longer works.

## What goes wrong without it
 
 Without a trace, the output is the entire evidence: one cannot
see what the agent searched for, what the search actually returned, or which
part of the returned text the model misread. 

- One can only re-run the agent on a similar-sounding question and hope to hit the same failure, which a non-deterministic model may simply not reproduce for you.
- Without a stored trace to compare against, there is no way to check whether a change made a class of failure more or less common — only an impression, formed from whichever cases happened to be
noticed. 

An agent operating without observability is a system whose only debugging signal is what a user happened to report, and whose only evidence for whether a change helped is how the team feels about it afterward.

## Observability

**Observability** is instrumenting an agent's execution so that after a run
finishes, one can see what it actually did.

- Every call to a language model, every call to a tool, every intermediate plan, retry, or sub-agent hand-off, each timestamped and carrying its inputs, outputs, and metadata. 

In practice this record takes the shape of a *trace* — a tree of *spans*, one per step, nested to show which call happened inside which. 

Observability answers "what happened here?" after the fact.

## Reproducibility
**Reproducibility** is the
 ability to re-create a run, or enough of one, that a fix
can be tested against the same conditions that produced a failure

- Pinning the model version, fixing the sampling parameters, recording tool responses so they can be replayed instead of called live again, and versioning the prompts that
drove the run.

Reproducibility answers "can I make that happen again on purpose?" so a
proposed fix can be checked rather than guessed at.