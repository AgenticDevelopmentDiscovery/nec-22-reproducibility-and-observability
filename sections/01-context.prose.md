# Context

## A correct answer is only the beginning {#s01}

An agent returns a convincing result. Its intermediate actions are missing.

::: {.question}
**ASK THE CLASS**

:::: {.prompt}
If an AI agent produces the correct final answer, do we still need to know how it got there?
::::

- **A.** No, the correct final result is all that matters.
- **B.** Yes: to verify inputs, reproduce execution, or investigate unexpected behavior.
- **C.** Only when the agent produces an incorrect answer.
:::

::: {.answer}
**ANSWER — B is strongest for our experiments**

- A correct output does not establish reproducibility or reliability.
- We need evidence about inputs, actions, and failures.
- Today: capture a run, replay it, and explain a difference.
:::

::: {.detail}
An equation that fits yesterday's observations might receive a different score today. The final equation alone cannot tell us whether the data, code, or evaluation changed. Our offline example makes those alternatives inspectable without requiring an API key.
:::

## Logging records; observability investigates {#s02}

**Logging:** recording events, inputs, outputs, scores, and errors during execution.

Example: record that equation `c004`, $1/x$, failed with division by zero. The failed attempt stays visible.

**Observability:** using connected logs, traces, and metrics to understand internal behavior.

Example: connect that failure to **which equation, which input, and which run**, so we can investigate it.

Useful connections matter more than the number of log lines. [@otelprimer]

::: {.detail}
Logging is an activity; observability is the ability those records help provide. Structured logs use consistent fields, so we can connect an error to an attempted equation, that equation to its run, and that run to its input snapshot. Relevant execution metadata includes identifiers, timestamps, and durations. More log lines alone do not guarantee useful observability.

A **trace** connects related operations in an execution; a **span** records one unit of work within that trace. Metrics are numerical summaries, such as failure counts or evaluation durations. The demo stores local trace/span identifiers and result counts; it does not export production telemetry. Later we distinguish execution nesting from equation ancestry.
:::

## Reproducibility verifies; provenance explains origins {#s02-repeat}

**Reproducibility:** repeat with preserved inputs, code, settings, and runtime; check outcomes against agreed criteria.

Example: replay and verify all **five equation evaluations**. New run IDs and timestamps may differ.

**Provenance:** the recorded origin and history of a result—its inputs, code, settings, and preceding operations.

Example: follow winner `c003` back through `c002` and `c001` to investigate how it was produced. [@w3cprov]

Repeat and verify the execution; trace where the result came from.

::: {.detail}
A **comparison contract** defines the criteria for equivalent outcomes. Here it requires matching experiment identity and ordered evaluation outcomes, while allowing new execution identifiers and timing. Reproducibility checks a new execution against that contract; a matching final answer alone cannot establish it.

Provenance supports debugging by connecting results to their origin. Candidate ancestry is one part of provenance; input snapshots, code identity, configuration, and source-run relationships are other parts. An inspectable failure can have excellent provenance even when it cannot be reproduced. Neither a trace nor a provenance chain proves that an equation is scientifically correct.

The distinction is: logging records what happened; observability helps us investigate what happened; reproducibility helps us repeat and verify an execution; provenance explains where results came from.
:::
