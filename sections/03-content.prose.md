## How it works: a trace is a tree of spans

- The unit of observability is the **span**: one step of execution recorded with its inputs, its outputs, when it started and ended, and whatever metadata matters later (model name, sampling parameters, token counts, the tool's arguments).
- A **trace** is
the tree those spans form for one agent run: a root span for the run as a
whole, with a child span for each step, nested to show which call happened
inside which.

![A trace for one support-agent run: a root span for the whole request, with child spans for the planning call, the doc-search tool call, and the drafting call. The tool-call span carries its own attributes — the query it sent and the raw response it got back — which is exactly the detail a final-answer-only log would discard.](figures/trace-tree.svg){#fig:trace width=85%}

This is the payoff of the tree structure: a bad final answer is one leaf of the
tree, but the tree also holds every intermediate step that led to it. Reading a
trace means walking from the root down, comparing each span's output against
what the next span used as input, until the mismatch appears.

## Reproducibility levers, and their real limits

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

None of this guarantees bit-for-bit determinism.
Reproducibility here means enough of the run pinned that a fix 
can be tested under the *same conditions* that produced the failure 
— the same tool responses, the same prompt, a model that behaves the same
way in practice — not a guarantee of the identical output token for token.

# Demonstration

## Capture and inspect the original run

**Terminal:** run once, then inspect the three records.

```powershell
python demo/run.py run --out demo/runs/class-original
```

- `manifest.json`: five observations, seed 7, saved code/runtime.
- `steps.jsonl`: five attempts, including one error.
- `result.json`: `c003`, $x^2+1$, **MSE 0.0**.

Use a fresh directory. Run every demo command from the **repository root**.

::: {.detail}
The Python demo needs Python 3.10 or later and only the standard library. It does not need WSL, Pandoc, or just. Execute each command individually; do not concatenate the examples into one invocation.

Expected terminal output: `completed_with_errors: demo/runs/class-original/manifest.json`. This status records a completed search with one unsuccessful candidate; it is not a crash. The exit code is zero.

Open `demo/runs/class-original/manifest.json`, `steps.jsonl`, and `result.json`. The result reports `attempted: 5`, `failed: 1`, and `best.candidate_id: c003`. The exact serialized winner is `((x) * (x)) + 1`.

The demonstration directories were unused when this revision was prepared. If any exists before presenting, choose a new common suffix for all three paths and every reference; never overwrite or delete earlier run evidence.
:::

## Replay means evaluating again

**2. Replay:** reevaluate with preserved inputs and code.

```powershell
python demo/run.py replay `
  demo/runs/class-original/manifest.json `
  --out demo/runs/class-replay
```

**3. Compare:** check the original against the new execution.

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

## Compare the replayed outcomes

![](figures/replay-comparison.svg){width=100%}

`match: true` · `compared_steps: 5` · exit code **0**.

**Contract:** same experiment identity and ordered candidate outcomes. New run IDs and timing may differ.

::: {.detail}
The comparison checks dataset/configuration/code/runtime identity, ordered semantic step fields, and the result. It includes predictions, equations, errors, attempts, and candidate ancestry. Run/trace IDs, timestamps, durations, and result parent-run links describe the new execution and are excluded. Expected comparison: `match: true`, no differences, `compared_steps: 5`; exit code 0.

The displayed scores are a summary, not the entire comparison. In particular, the matching error is part of the evidence. Live model calls have additional variability; exact replay of this offline example does not guarantee identical live responses.
:::


## Pitfalls

**Logging what shouldn't be logged.** Spans capture raw inputs and outputs by
default, and agent inputs routinely include user messages, account details, or
API keys passed as tool arguments. A trace store is a new place secrets and
personal data can leak; redact before you record, not after.

**Instrumenting until no one reads it.** A span for every token or every retry
produces a trace too large to read during an actual incident. Instrument at
the grain a human will actually walk through and add finer detail only where
a real failure has shown it is needed.

**Mistaking a clean trace for a correct one.** A trace shows what the agent
did and confirms it ran without errors; it says nothing about whether the
answer was right. The support-agent example above produced a trace with no
exceptions in it at all — every span succeeded. Whether the output was correct
is a question for evaluation, not for the trace.
