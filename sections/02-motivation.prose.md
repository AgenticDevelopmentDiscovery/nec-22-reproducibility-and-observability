# The experiment

## How Does Our Python Agent Work? {#s03}

**Symbolic regression:** search for an equation that fits observed data.

![](figures/agent-workflow.svg){width=100%}

- **Candidate:** a proposed equation. **Incumbent:** best valid one so far.
- Programmed rules; five serial attempts; no retries or external API.

::: {.detail}
`demo/run.py` is a Python program implementing a simplified **rule-based agent**: programmed rules propose equations and respond to evaluation outcomes. PowerShell launches the program; the search is implemented in Python, not in a Bash script or a hosted LLM. **Deterministic execution** means the same relevant behavior when inputs, code, and necessary execution conditions are controlled; run IDs and timing can still change.

Initialization uses the five data pairs shown next, seed 7, MSE scoring, serial execution, no retries, and a **candidate budget** of five—the maximum number of attempts. A **random seed** is the initial value for a repeatable pseudorandom sequence. Here it controls the final nonzero offset; it does not make live model calls reproducible.

Before evaluation, `run()` creates the output directory, saves the executing source as `agent.py`, and writes `manifest.json`—the experiment's input/configuration record—with status `running`. The incumbent begins empty. Each iteration calls `proposal()` using the current incumbent and seeded generator. **Evaluation** tests an equation: `evaluate()` computes predictions; `run()` computes their MSE or retains the error and any partial predictions.

A valid candidate replaces the incumbent only if its MSE is strictly lower, or if no incumbent exists. The program then writes and flushes that attempt's equation, predictions, score, status, error, identifiers, ancestry, and timing to `steps.jsonl`. It continues through all five attempts, even after reaching zero error. It saves `result.json` after the search and finalizes the manifest's status. Recording therefore occurs before, during, and after the search.

The rule-based sequence isolates instrumentation from hosted-model variability. It is not a general symbolic-regression solver or a demonstration of scientific discovery. In the course, the scoring harness illustrates auditable fitness evaluation (C2); it does not import a separately supplied C2 implementation.
:::

## What does a better fit mean? {#s04}

$x=[-2,-1,0,1,2]$; observed $y=[5,2,1,2,5]$.

**Mean squared error (MSE):** average squared difference between a prediction and its observed target.

$$\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(\hat y_i-y_i)^2,\qquad n=5.$$

$\hat y_i$ is the prediction; $y_i$ is the observation.

**Lower is better on these observations.** Zero error here does not guarantee accuracy on unseen data.

::: {.detail}
Here $\hat y_i$ is a predicted value and $y_i$ is an observed target. Squaring makes both positive and negative residuals contribute nonnegative error; averaging keeps the score per observation.

For $x$, predictions are $[-2,-1,0,1,2]$. Residuals are $[-7,-3,-1,-1,-3]$, so squared errors sum to $49+9+1+1+9=69$ and MSE is $69/5=13.8$. For $x^2$, each prediction is one below its target, giving MSE $5/5=1.0$. For $x^2+1$, every residual is zero.

The next table follows the incumbent through every attempt, including a failure and a worse proposal.
:::

## Five attempts; keep the best valid equation {#s04-attempts}

| ID | Equation | Outcome | Incumbent after attempt |
| --- | --- | --- | --- |
| c001 | $x$ | MSE 13.8 | c001: first valid |
| c002 | $x^2$ | MSE 1.0 | c002: improves |
| **c003** | $x^2+1$ | **MSE 0.0** | **c003: improves** |
| c004 | $1/x$ | ZeroDivisionError | c003: keep |
| c005 | $x^2+2$ | MSE 1.0 | c003: keep |

Seed 7 gives a final offset of **+1**: $(x^2+1)+1=x^2+2$.

The winner is **c003**, not the most recent attempt.

::: {.detail}
The rules first propose $x$, then square the incumbent, then add 1 to the incumbent. These three valid candidates successively become the best result. The fourth rule proposes $1/x$ independently; its failure cannot replace the incumbent. The final rule adds an offset chosen from `[-2, -1, 1, 2]` to the current best equation. In the verified seed-7 execution, that offset is +1. Candidate c005 is therefore a child of c003, scores 1.0, and loses to c003's 0.0. Selection retains the best valid candidate found so far, not the last proposed equation.
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

## One experiment, four complementary files {#s06}

![](figures/experiment-records.svg){width=100%}

- **Manifest:** record of inputs, settings, code identity, and runtime.
- **Steps (JSONL):** one JSON record per line, one per attempt.
- **Result:** winner, score, attempted/failed counts, and run links.

**`agent.py`:** saved source code. A **hash** fingerprints its content.

::: {.detail}
The lines in the diagram associate records with the same run; they are not a pipeline that executes three files. A JSON file stores one structured object. A JSONL file stores one JSON object per line, so each candidate can be logged independently.

The manifest is written before evaluation and finalized afterward. It embeds the dataset, the descriptive prompt, model identifier `offline-rule-agent-v1`, seed 7, MSE metric, serial execution, a five-candidate budget, and retry limit zero. It also records dataset/configuration/source hashes, Python runtime, run ID, source `parent_run_id` when applicable, and execution status. Temperature, top-p, and corpus snapshot are null because no live model or retrieval is used. Git commit/dirty state and the source snapshot identify the code actually executed.

Step records contain run/trace/candidate identifiers, the incumbent input, dataset/configuration hashes, predictions, score or null, status, exception, and timing. Each completed evaluation is flushed to the log. The result points to the winner and experiment. A completed run can include failed candidates.
:::
