# The experiment

## Propose, evaluate, select {#s03}

**Symbolic regression:** search for an equation that fits observed data.

![](figures/agent-workflow.svg){width=100%}

- The **incumbent** is the best valid equation so far.
- Our proposer follows fixed rules and a seeded mutation.
- Five serial attempts; no independent LLM-generated proposals.

::: {.detail}
The diagram describes the existing teaching agent. It starts with $x$, squares the incumbent, adds 1 to the best equation, attempts $1/x$, and then adds a seeded nonzero offset to the incumbent. Candidate selection uses the harness score; failed candidates never become the incumbent. With the recorded data, seed, and runtime, this sequence is deterministic.

The rule-based sequence isolates instrumentation from hosted-model variability. It is not a general symbolic-regression solver or a demonstration of scientific discovery. In the course, the scoring harness illustrates auditable fitness evaluation (C2); it does not import a separately supplied C2 implementation.
:::

## What does a better fit mean? {#s04}

$x=[-2,-1,0,1,2]$; observed $y=[5,2,1,2,5]$.

$$\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(\hat y_i-y_i)^2,\qquad n=5.$$

| Candidate equation | MSE |
| --- | ---: |
| $x$ | 13.8 |
| $x^2$ | 1.0 |
| $x^2+1$ | 0.0 |

**Lower is better on these observations.** Zero error here does not guarantee accuracy on unseen data.

::: {.detail}
Here $\hat y_i$ is a predicted value and $y_i$ is an observed target. Squaring makes both positive and negative residuals contribute nonnegative error; averaging keeps the score per observation.

For $x$, predictions are $[-2,-1,0,1,2]$. Residuals are $[-7,-3,-1,-1,-3]$, so squared errors sum to $49+9+1+1+9=69$ and MSE is $69/5=13.8$. For $x^2$, each prediction is one below its target, giving MSE $5/5=1.0$. For $x^2+1$, every residual is zero.

The remaining attempts still matter: $1/x$ fails at zero, and the final seeded mutation does not beat the incumbent. The final selection summarizes only part of that history.
:::

## What would the winner leave out? {#s05}

::: {.question}
**ASK THE CLASS**

:::: {.prompt}
An agent evaluates five candidate equations. If we only save the winning equation, what information could we lose?
::::

Think of one thing you would need to investigate the run.
:::

::: {.answer}
**ANSWER — the missing evidence**

- Attempted equations and their scores.
- Input data, configuration, and code.
- Failed candidates and partial results.
- The decisions that led to the winner.

We need complementary records of the **experiment, execution, and result**.
:::

::: {.detail}
This is an open-ended question: several answers are useful. Saving the winner alone cannot reconstruct the complete workflow. Saving only a log also leaves gaps if its input hashes refer to missing snapshots. The next diagram shows the three records used together.
:::

## One experiment, three complementary records {#s06}

![](figures/experiment-records.svg){width=100%}

- **Manifest:** actual data/configuration, code hash, seed, runtime.
- **Steps:** each attempted equation, predictions, score, status.
- **Result:** selected candidate, attempted/failed counts, run links.

Also retain the saved **`agent.py`**. A hash cannot restore missing content.

::: {.detail}
The lines in the diagram associate records with the same run; they are not a pipeline that executes three files. A JSON file stores one structured object. A JSONL file stores one JSON object per line, so each candidate can be logged independently.

The manifest is written before evaluation and finalized afterward. It embeds the dataset, the descriptive prompt, model identifier `offline-rule-agent-v1`, seed 7, MSE metric, serial execution, a five-candidate budget, and retry limit zero. Temperature, top-p, and corpus snapshot are null because no live model or retrieval is used. Git commit/dirty state and the source snapshot identify the code actually executed.

Step records contain run/trace/candidate identifiers, the incumbent input, dataset/configuration hashes, predictions, score or null, status, exception, and timing. Each completed evaluation is flushed to the log. The result points to the winner and experiment. A completed run can include failed candidates.
:::
