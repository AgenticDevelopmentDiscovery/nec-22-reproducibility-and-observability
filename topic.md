# Tutorial 22 - reproducibility, logging, and observability

## In one sentence

Preserve an agent experiment, repeat it, compare its behavior, and use connected evidence to investigate where results and failures came from.

## Why it belongs in ENGR 689

Model sampling, changing tool responses, and multi-step execution complicate debugging. Deterministic software can be easier to replay under controlled conditions, but neither ordinary programs nor agents are universally deterministic. The final answer does not identify the inputs, intermediate errors, or changes that produced it.

The combined tutorial retains Russell Oplinger's explanation of these difficulties, trace/span relationships, reproducibility controls, and instrumentation pitfalls. Elias Lynch's offline symbolic-regression demonstration gives those ideas an executable, inspectable example.

## What students can do afterward

- Distinguish logging, observability, reproducibility, and provenance.
- Explain the Python propose/evaluate/select/record loop, MSE, and incumbent decisions.
- Capture five attempts, including a failure, and four complementary evidence files.
- Replay an experiment and compare all five candidate outcomes.
- Predict and locate controlled divergence even with the same winning equation.
- Distinguish candidate ancestry, run ancestry, and span containment.
- Describe model/prompt/tool versioning and saved responses without claiming a seed guarantees determinism.
- Apply proportionate recording to coding agents and engineering simulations; distinguish repeatability from correctness and validation.

## Scope and shape

The 15-minute session has 22 instructional frames, four separate answer reveals, a title, and references: 28 PDF pages. Sequence: motivation/definitions; workflow/records; original/replay; prediction/divergence; failure/ancestry; trace relationships; live-agent limits, pitfalls, applications, and conclusion.

All five commands appear on slides and as copyable single lines in presenter notes. The paired source feeds the article, Beamer deck, and website. Longer explanations belong in detail blocks and notes, not overflowing slides.

In scope: saved input/code/configuration/runtime, local logs, comparison criteria, errors, trace interpretation, and reproducibility limits. The support-agent trace is illustrative; the executed experiment is the offline search.

Out of scope: hosted LLM demo, production telemetry export, monitoring infrastructure, training reproducibility, general symbolic regression, or a complete V&V course. A matching trace does not establish scientific validity.

## Delivery limits

The schedule is an estimate, not a timed rehearsal. Live file navigation and discussion are the main risks. Pre-open the named fields, preserve audience pauses and all commands, and omit optional backup explanations when behind.
