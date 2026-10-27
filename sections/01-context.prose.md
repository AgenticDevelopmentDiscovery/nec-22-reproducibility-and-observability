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

## Four ideas, four different jobs {#s02}

| Idea | What it gives us |
| --- | --- |
| **Logging** | Events, inputs, outputs, errors |
| **Observability** | Evidence to investigate behavior |
| **Reproducibility** | Re-execution under a contract |
| **Provenance** | Links to inputs, code, ancestors |

A log says “candidate failed.” Connected records show **which run, which input, and where**. [@otelprimer]

::: {.detail}
Logging is an activity; observability is the ability those records help provide. Structured logs use consistent fields, so we can connect an error to a candidate, the candidate to its run, and that run to its input snapshot. More log lines alone do not guarantee useful observability. Traces organize operations; metrics summarize behavior across operations.

Reproducibility asks whether a repeat execution meets a defined contract. Provenance asks where an artifact came from. An inspectable failure can have excellent provenance even when it cannot be reproduced. Neither a trace nor a provenance chain proves that an equation is scientifically correct. [@w3cprov]
:::
