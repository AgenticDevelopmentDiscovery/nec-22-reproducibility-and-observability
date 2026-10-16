# Content

## Three files connect the experiment to its result

| File in each run directory | Job |
| --- | --- |
| `manifest.json` | Inputs, configuration, code/runtime identity, run ancestry |
| `steps.jsonl` | One record per candidate, in execution order |
| `result.json` | Winner, counts, and experiment links |

The saved `agent.py` preserves the source. Write the manifest before execution; flush each step after evaluation. Completion does not mean every candidate succeeded.

Trace IDs group operations; parent span IDs describe nesting. Our local schema follows this distinction. [@oteltraces]

## Record the replay contract

The manifest embeds the five data rows and the full configuration, including:

```json
{
  "model_id": "offline-rule-agent-v1",
  "seed": 7,
  "temperature": null, "top_p": null,
  "metric": "mean_squared_error",
  "retry_limit": 0, "candidate_budget": 5
}
```

Null decoding settings mean “not applicable.” The full file also records the prompt, input/source hashes, Git state, and Python version. The seed controls the final exploratory mutation.

## The agent proposes; the harness scores

Our five points are $x=(-2,-1,0,1,2)$ and $y=(5,2,1,2,5)$. The harness computes

$$\mathrm{MSE}=\frac{1}{5}\sum_{i=1}^{5}(\hat y_i-y_i)^2.$$

The agent starts with $x$, squares its incumbent, then adds 1 to the best equation so far. It also tries $1/x$ and a seeded offset mutation. Each valid improvement becomes the incumbent.

Expected scores: $x$: 13.8; $x^2$: 1.0; $x^2+1$: 0.0. The invalid division remains a recorded attempt. This is a tiny adaptive search, not a demonstration of discovery quality.

## Capture the first run

From the repository root, with Python 3.10 or later, enter the demo directory:

```text
cd demo
python run.py run --out runs/original
```

Open `runs/original/manifest.json`, `steps.jsonl`, and `result.json`. Keep this working directory for the next two slides.

The result should report **five attempted candidates, one failed candidate, and a winner with MSE 0.0**. Candidate `c003` represents $x^2+1$ and names `c002` as its parent.

Run directories must be new: the script refuses to overwrite evidence. Platform-specific launch instructions are in `demo/README.md`.

## Re-execute and compare behavior

```text
python run.py replay runs/original/manifest.json --out runs/replay
python run.py compare runs/original runs/replay
```

The comparison should report `"match": true` and `"compared_steps": 5`. It compares configuration, data, code/runtime identity, step outcomes, and results while excluding execution IDs and timing.

Replay first validates the input hashes, source snapshot, executing code, and Python version. It regenerates proposals and recomputes scores; it does not copy the old scores.

## Change one input and find the first divergence

```text
python run.py corrupt runs/original/manifest.json --out runs/changed
python run.py compare runs/original runs/changed
```

`corrupt` creates a new experiment: row 0's target changes from 5 to 6, its dataset hash changes, and the manifest records that intervention. The original remains intact.

The comparison reports **step 1**, a changed `inputs.dataset_hash`, and score **13.8 → 16.8**. Predictions for $x$ are unchanged. That evidence locates the divergence at evaluation input, before later proposals can react. Exit code 1 means a detected difference.

## Preserve the failed candidate

At candidate `c004`, evaluating $1/x$ reaches $x=0$. Its record contains:

```json
{
  "status": "error", "score": null,
  "predictions": [-0.5, -1.0],
  "error": {
    "type": "ZeroDivisionError",
    "message": "division by zero", "row_index": 2
  }
}
```

Partial predictions survive; the incomplete score cannot win. There are no retries in this demo. A production timeout should likewise record its deadline, status, and partial results; every retry needs a separate attempt record.

## Trace the winner to its origin

The result identifies `c003`; that step identifies parent `c002`; `c002` identifies parent `c001`. These links describe **candidate ancestry**. The replay manifest's `parent_run_id` instead identifies the source **run**.

Trace nesting answers which operation contained an evaluation; ancestry answers which equation was mutated. Those relationships need different fields.

Dataset/configuration hashes and the source snapshot connect this genealogy to its experiment. In a larger evolutionary search, preserving these links makes a surprising winner inspectable. It still needs independent evaluation to establish scientific value.

## Transfer the method to a live agent

Wrap the proposal call and scoring tool with the same recording boundaries. Save the rendered request, visible response, tool arguments/results, and retrieved chunks; record model and environment identity. Hidden model reasoning is not required.

If identical live outputs cannot be guaranteed, define a metric, tolerance, and repeated-run protocol before comparing distributions. Do not present one matching run as statistical evidence.

Two practical limits: completed-step logs cannot fully explain a process killed mid-step; production systems need start/end events and recovery. Real inputs also need controlled storage and redaction, with any replay gaps documented.
