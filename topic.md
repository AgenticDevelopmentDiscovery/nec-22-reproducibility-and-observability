# Topic

## In one sentence

Make a symbolic-regression agent run replayable and inspectable by saving its inputs, recording every candidate evaluation, and tracing the winning equation to its origin.

## What it is

A 15-minute tutorial on reproducibility, structured logging, tracing, and artifact lineage for agent runs. A run manifest records the experiment; a step log records execution; a result links the selected equation to both. An offline rule-based agent makes the example runnable without credentials or a hosted service.

## Why it belongs in this course

Agentic search combines proposal generation with tool-based evaluation, so an unexplained fitness score is insufficient evidence. This tutorial connects the reproducible-repository goal (C1), evaluation harness (C2), captured retrieval context (C3), and reliability goal (C4). The same records support the capstone's genealogy of candidate equations.

## What the reader will be able to do

- Identify uncontrolled inputs in a model/tool/retrieval loop.
- Capture a manifest containing configuration, dataset snapshot, hashes, code, and runtime identity.
- Re-execute the included agent and compare ordered candidate outcomes.
- Locate the first divergent evaluation after a deliberate dataset change.
- Preserve an invalid candidate, its partial output, and its exception in the audit trail.
- Follow parent-candidate and parent-run links from an equation to its origins.

## Scope

**In scope**

- Exact behavioral replay in a controlled offline example; limits of applying that claim to live models.
- A serial, five-candidate search scored by mean squared error.
- JSON manifests, JSONL step records, lineage, and first-divergence comparison.
- Errors and retry policy; logging timeouts as a production extension.

**Out of scope**

- Hosted-model integration and tracing dashboards: credentials and service setup would dominate the session.
- Full evolutionary optimization and scientific discovery: the small search teaches instrumentation, not search quality.
- Bitwise reproducibility across arbitrary platforms and statistical equivalence testing: these need separate protocols.
- Production crash recovery, sensitive-data storage, and distributed scheduling implementations.

## Shape

- Context: 2 minutes, definitions and the replay contract.
- Motivation: 2 minutes, a concrete misleading-score example and the nondeterminism map.
- Content: 9 minutes, capture, execute, replay, perturb, inspect failures, and connect lineage.
- Conclusion: 2 minutes, transfer checklist, exit question, and further reading.
- Keep each level-two heading short enough for one slide. Put operational detail in demo/README.md and presenter cues in presenter-notes.md.

## Open questions

- Author names have not been supplied; omit author metadata until known.
- The course harness interface has not been supplied; the runnable MSE harness is a stand-in, not a claimed C2 integration.
- A live model's repeatability and a real timeout policy must be evaluated when those components are selected.
