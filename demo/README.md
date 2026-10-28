# Reproducible equation-search demo

This is a Python-standard-library demo: no packages, credentials, or network calls are needed. Use Python 3.10 or later. The five-candidate, rule-based agent adapts its proposals to its incumbent score; it is an offline teaching stand-in for an LLM proposer.

## What the Python program does

A candidate is an equation proposed for evaluation. The incumbent is the best valid equation found so far. `run()` saves the initial manifest and source snapshot, then repeats proposal, prediction, MSE calculation or error capture, incumbent selection, and step logging. It stops at the five-attempt budget, saves the result, and finalizes status. An invalid or worse candidate never replaces the incumbent.

With seed 7, the attempts are `x` (13.8), `x²` (1.0), `x² + 1` (0.0), `1/x` (error), and `x² + 2` (1.0). The last proposal adds a seeded offset of +1 to incumbent `x² + 1`; c003 remains the winner. The seed initializes a repeatable pseudorandom sequence, and the proposer follows programmed rules rather than making LLM calls.

The command-line interface selects what to do with the experiment:

| Operation | Purpose |
| --- | --- |
| `run` | Start a new search and save its evidence |
| `replay` | Validate the saved manifest, source identity, and required runtime; repeat using saved data/settings |
| `compare` | Check two sets of recorded outcomes, including failures and result, while excluding expected ID/timing differences |
| `corrupt` | Record a deliberate target change and execute a new run, preserving the original |

There are four operations but five demonstration commands because comparison is used twice. The shell launches Python; the search logic is inside `demo/run.py`.

## Run the complete experiment

Execute each command **individually from the repository root**. Each output directory must be new. These classroom names are reserved for presentation; validation uses separately named runs. No WSL, Pandoc, or just is required for this Python demo.

```powershell
python demo/run.py run --out demo/runs/class-original
```

```powershell
python demo/run.py replay demo/runs/class-original/manifest.json --out demo/runs/class-replay
```

```powershell
python demo/run.py compare demo/runs/class-original demo/runs/class-replay
```

```powershell
python demo/run.py corrupt demo/runs/class-original/manifest.json --out demo/runs/class-changed
```

```powershell
python demo/run.py compare demo/runs/class-original demo/runs/class-changed
```

On macOS/Linux, use `python3` if that is your Python command. On Windows, use `py -3` if configured. If neither command finds the interpreter, invoke the installed executable; for this workspace:

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" demo/run.py run --out demo/runs/class-original
```

Use the same interpreter for all five commands. To repeat the presentation, choose a new set of directory names and adjust every command consistently; the script refuses to replace earlier evidence.

The [presenter guide](../presenter-notes.md) provides the timing, spoken explanations, question/reveal cues, expected output, and exact files to display for every action.

## Expected observations

| Observation | Expected value |
| --- | --- |
| Original winner | `c003`, equation `((x) * (x)) + 1`, MSE `0.0` |
| Candidates | 5 attempted, 1 failed |
| Normal replay comparison | `match: true`, `compared_steps: 5`, exit code 0 |
| Changed input | First row's target changes from 5 to 6 |
| Perturbation comparison | `match: false`, first difference at step 1, exit code 1 |
| First changed score | 13.8 becomes 16.8; predictions remain unchanged |
| Winner's changed score | 0.0 becomes 0.2 |
| Failed candidate | `c004`, `1 / x`, `ZeroDivisionError` at row index 2 |

Exit code 2 means invalid input or an execution/setup error. The expected difference uses exit code 1 so shell automation can distinguish equality from divergence. Candidate failure is data: a run that finishes recording it returns 0 and reports `completed_with_errors`.

## Inspect the evidence

Each directory contains:

- `manifest.json`: full dataset, full configuration, their SHA-256 hashes, Python/platform identity, Git commit and dirty flag, source hash, run ancestry, and completion status.
- `agent.py`: exact bytes of the source that executed the experiment. This matters when the Git tree is dirty; a commit alone would not capture the code actually run.
- `steps.jsonl`: one JSON object per attempted candidate, including equation, incumbent input, dataset/config hashes, predictions, score or null, status, exception, attempt number, timing, and parent candidate.
- `result.json`: winner, attempted/failed counts, run ancestry, and dataset/config hashes.

The prompt is descriptive configuration for the offline rule-based proposer; no model is called. Temperature/top-p and corpus snapshot are null because they do not apply. The seed controls the final offset mutation. The tiny arithmetic interpreter accepts numeric constants, `x`, and arithmetic; it never executes an equation with Python `eval`.

The parent span `run` corresponds to the run lifecycle in the manifest. Candidate spans are siblings; candidate-parent links separately describe mutation ancestry. This is a local educational schema, not an OpenTelemetry exporter.

## What the comparison enforces

Replay validates dataset/config hashes, the saved source hash, the executing source hash, and exact Python version before creating a new directory. Configuration options other than the seed are fixed for this teaching agent. Keep the recorded runtime available; recording its name does not install it.

The comparator checks dataset/config/code/runtime identity, all ordered semantic step fields, and the result. It excludes run/trace IDs, timestamps, durations, and the result's parent-run link because those identify a new execution. It includes candidate IDs, ancestry, errors, predictions, scores, and attempt count.

`corrupt` first validates the source, then deliberately changes a copied dataset and records the intervention in a new manifest. It does not bypass validation or alter the original. Manually editing a dataset while keeping its old hash is rejected.

If the repository code later changes, run the recorded source with its recorded Python version:

```sh
python demo/runs/class-original/agent.py replay demo/runs/class-original/manifest.json --out demo/runs/from-snapshot
```

## Tests and boundaries

```sh
python -m unittest discover -s demo -v
```

Tests verify exact replay, the expected winner, retained partial failure output, lineage, the changed-input divergence, refusal to overwrite, rejection of a stale input hash, and detection of a missing step or changed result.

This demo does not implement wall-clock timeouts, retries, live model requests, retrieval, or distributed tracing. It demonstrates a real failed evaluation instead. In production, log timeout status/deadline and each retry as a separate attempt. Completed-step flushing is not crash-proof: a killed process may leave an unfinished attempt with no completed record. Add start/end events, atomic finalization, and recovery when those guarantees are required.

Exact replay here does not establish live-model determinism, cross-platform bitwise equality, or scientific validity. Hashes detect accidental changes against recorded expectations; they are not signatures or protection against someone rewriting the whole record.
