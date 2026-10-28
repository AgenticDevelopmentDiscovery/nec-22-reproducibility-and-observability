# Demonstration

## Capture and inspect the original run {#s07}

**1. Run:** execute a new five-candidate search and save its evidence.

```powershell
python demo/run.py run --out demo/runs/class-original
```

- `manifest.json`: five observations, seed 7, saved code/runtime.
- `steps.jsonl`: five attempts, including one error.
- `result.json`: `c003`, $x^2+1$, **MSE 0.0**.

Use a fresh directory. Run every demo command from the **repository root**.

::: {.detail}
The Python demo needs Python 3.10 or later and only the standard library. It does not need WSL, Pandoc, or just. Execute each command individually; do not concatenate the examples into one invocation.

The command-line interface selects an operation; it is distinct from the search loop inside the program. `run` starts a new search, `replay` validates and repeats a saved experiment, `corrupt` validates and reruns with one recorded target change, and `compare` examines existing records without performing a new search. There are four operations but five demonstration commands because we compare twice.

Expected terminal output: `completed_with_errors: demo/runs/class-original/manifest.json`. This status records a completed search with one unsuccessful candidate; it is not a crash. The exit code is zero.

Open `demo/runs/class-original/manifest.json`, `steps.jsonl`, and `result.json`. The result reports `attempted: 5`, `failed: 1`, and `best.candidate_id: c003`. The exact serialized winner is `((x) * (x)) + 1`.

The demonstration directories were unused when this revision was prepared. If any exists before presenting, choose a new common suffix for all three paths and every reference; never overwrite or delete earlier run evidence.
:::

## Replay means evaluating again {#s08}

**2. Replay:** validate, then reexecute with saved inputs and code.

```powershell
python demo/run.py replay `
  demo/runs/class-original/manifest.json `
  --out demo/runs/class-replay
```

**3. Compare:** check recorded evaluations, failures, and result.

```powershell
python demo/run.py compare `
  demo/runs/class-original `
  demo/runs/class-replay
```

**PowerShell, repository root.** A backtick continues one command; run each block separately.

::: {.detail}
The backtick must be the final character on its line, with no trailing spaces. The presenter notes also provide each command on one line for copying. A continuation is formatting, not an extra command.

Replay first validates dataset/configuration hashes, saved and executing source hashes, completed source-run status, and exact Python version. It regenerates candidates and recomputes their scores instead of copying old scores. The new manifest links to the source through `parent_run_id`.
:::

## Compare the replayed outcomes {#s08-results}

![](figures/replay-comparison.svg){width=100%}

`match: true` · `compared_steps: 5` · exit code **0**.

**Comparison contract:** criteria for equivalent outcomes—same experiment identity and ordered evaluations. New run IDs and timing may differ.

::: {.detail}
The comparison checks dataset/configuration/code/runtime identity, ordered semantic step fields, and the result. It includes predictions, equations, errors, attempts, and candidate ancestry. Run/trace IDs, timestamps, durations, and result parent-run links describe the new execution and are excluded. Expected comparison: `match: true`, no differences, `compared_steps: 5`; exit code 0.

The displayed scores are a summary, not the entire comparison. In particular, the matching error is part of the evidence. Live model calls have additional variability; exact replay of this offline example does not guarantee identical live responses.
:::

## Predict the effect of changing one target {#s09}

::: {.question}
**ASK THE CLASS**

The winner $x^2+1$ has MSE 0.0 on five observations.

:::: {.prompt}
At $x=-2$, change the observed $y$ from 5 to 6. Keep the equation fixed. What happens to MSE?
::::

- **A.** It remains 0.0.
- **B.** It increases.
- **C.** It decreases.
- **D.** The equation becomes mathematically invalid.
:::

::: {.answer}
**ANSWER — B: MSE increases**

Prediction: 5. New observation: 6. Error magnitude: 1.

$$\mathrm{MSE}=\frac{(5-6)^2+0+0+0+0}{5}=0.2.$$

We changed one target; there are **still five observations**.

**Follow-up:** Must a higher MSE change the winning equation? Let's check.
:::

::: {.detail}
A score is relative to the observations used to compute it. The equation is still mathematically valid. Only its agreement with the recorded dataset changed. The next run confirms whether this equation remains best among this agent's attempts; a higher score alone does not determine the ranking.
:::

## Change one observation, then compare {#s10}

**4. Corrupt:** record target 5 → 6 and rerun; keep the original.

```powershell
python demo/run.py corrupt `
  demo/runs/class-original/manifest.json `
  --out demo/runs/class-changed
```

**5. Compare:** locate the first difference from the original.

```powershell
python demo/run.py compare `
  demo/runs/class-original `
  demo/runs/class-changed
```

**Still five observations; same candidate equations.** Run each block separately from the repository root.

::: {.detail}
Despite its command name, `corrupt` creates a deliberate, recorded experiment. It validates the source manifest, changes only `dataset[0].y` from 5 to 6 in a new run, updates the dataset hash, and records the intervention in `change`. The original files remain intact.
:::

## Locate the first divergence {#s10-results}

![](figures/controlled-divergence.svg){width=100%}

**Divergence:** a difference under our comparison criteria. First difference: step 1, input fingerprint and score.

The recorded target change explains it. Same winner; exit code **1 is the expected mismatch**, not a crash.

::: {.detail}
The first difference is candidate `c001` at step 1: `inputs.dataset_hash` changes and MSE moves from 13.8 to 16.8. The $x$ predictions stay unchanged. The changed target makes its first squared residual 64 instead of 49, increasing the mean by $15/5=3$.

The winner remains `c003`, $x^2+1$, but its MSE increases from 0.0 to 0.2. In this changed run $x^2$ scores 1.6 and the final offset candidate scores 0.8, so neither displaces it. The first-divergence report locates the affected evaluation; the explicitly recorded intervention identifies the cause. A changed hash by itself is not a causal explanation.

Exit code 1 is the comparator's intended signal for unequal runs. Exit code 2 instead indicates invalid input or setup/execution error.
:::

## What should happen to a failed candidate? {#s11}

::: {.question}
**ASK THE CLASS**

:::: {.prompt}
Our agent evaluates $f(x)=1/x$, but the dataset includes $x=0$. What should it do when evaluation fails?
::::

- **A.** Delete the failed candidate entirely.
- **B.** Record the failure, cause, and available partial results.
- **C.** Silently assign an MSE of zero.
- **D.** Stop all future experiments permanently.
:::

::: {.answer}
**ANSWER — B: preserve the attempt**

`c004`: $1/x$; `ZeroDivisionError` at row index **2** ($x=0$).

```json
{
  "status": "error", "score": null,
  "predictions": [-0.5, -1.0]
}
```

Show the full record in `steps.jsonl`. The failed attempt remains visible and cannot win.
:::

::: {.detail}
The first two inputs, $-2$ and $-1$, produce predictions $-0.5$ and $-1.0$. Evaluation then fails at the third input; row indices start at zero. The recorded exception is `{"type": "ZeroDivisionError", "message": "division by zero", "row_index": 2}`.

The full record retains `candidate_id: c004`, `equation: 1 / x`, `parent_candidate_id: null`, run/trace/span IDs, input hashes, timing, and attempt number 1. These fields connect the failure to the particular experiment. A null score means no valid complete MSE was computed; assigning zero would falsely reward a failure.

There are no retries or implemented timeouts in this example. A production system should record each retry separately and record timeout status, deadline, and any partial results. Completed-step logging alone cannot recover an operation killed before its final record.
:::

## Trace the winner to its origin {#s12}

**Lineage:** links to parent candidates or source runs.

![](figures/equation-lineage.svg){width=100%}

- **Candidate ancestry:** which equation was mutated?
- **Run ancestry:** which recorded run was replayed or modified?
- **Trace:** connected operations in a run; **span:** one unit of work.

Equation parentage does not imply nested spans. [@w3cprov; @oteltraces]

::: {.detail}
The arrows run from parent to child. The actual records show `c002.parent_candidate_id = c001` and `c003.parent_candidate_id = c002`. The final `c005` is another child of `c003`; it loses. Candidate `c004` is an independent reciprocal proposal with no candidate parent.

Run ancestry is different: the replay and changed manifests both identify the original run through `parent_run_id`. In the local trace schema, candidate operations are siblings with `parent_span_id: run`; mutation ancestry does not make one evaluation a nested span inside another.

The demo uses a local educational trace schema, not an OpenTelemetry exporter. Input/configuration hashes and the saved source connect the result to its experiment. Provenance helps investigate a surprising winner but does not establish its scientific validity.
:::
