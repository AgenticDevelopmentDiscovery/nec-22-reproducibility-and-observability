# Topic

## In one sentence

Make a symbolic-regression agent run replayable and inspectable by saving its inputs, recording every candidate evaluation, and tracing the winning equation to its origin.

## What it is

A 15-minute tutorial on reproducibility, structured logging, observability, and artifact lineage for agent runs. A run manifest records the experiment; a step log records execution; a result links the selected equation to both. An offline rule-based agent makes the example runnable without credentials or a hosted service. Four prediction/discussion moments turn the example into an investigation students can follow.

## Why it belongs in this course

Agentic search combines proposal generation with tool-based evaluation, so an unexplained fitness score is insufficient evidence. This tutorial connects the reproducible-repository goal (C1), evaluation harness (C2), captured retrieval context (C3), and reliability goal (C4). The same records support the capstone's genealogy of candidate equations.

## What the reader will be able to do

- Identify uncontrolled inputs in a model/tool/retrieval loop.
- Distinguish logging from observability, reproducibility, and provenance.
- Capture a manifest containing configuration, dataset snapshot, hashes, code, and runtime identity.
- Re-execute the included agent and compare ordered candidate outcomes.
- Locate the first divergent evaluation after a deliberate dataset change.
- Explain why changing a target can increase MSE without changing the winning equation.
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

- Introduction and Q1: 2 minutes; missing evidence before technical terms.
- Concepts, workflow, MSE, Q2, and artifacts: 3 minutes.
- Original execution and replay: 3 minutes.
- MSE prediction (Q3) and controlled divergence: 3 minutes.
- Failed-candidate question (Q4) and provenance: 2 minutes.
- Live-agent transfer, coding/simulation applications, and conclusion: 2 minutes.
- Preserve four source pairs and 17 substantive headings, including two short command frames. The second pair prepares the experiment; the first pair opens with motivation.
- Four question/answer overlays; suppress section-divider pages to keep navigation short.
- `.detail` blocks keep supplementary calculations and schema explanations in the document/website. All five commands appear in the slides. A small Lua filter handles output differences.
- Stable S01–S15 IDs, plus S08-results and S10-results, connect the manuscript to complete presenter notes. Keep all demo commands at the repository root.

## Open questions

- Author names have not been supplied; omit author metadata until known.
- The course harness interface has not been supplied; the runnable MSE harness is a stand-in, not a claimed C2 integration.
- A live model's repeatability and a real timeout policy must be evaluated when those components are selected.
- The 15-minute schedule includes discussion but still needs a real presenter rehearsal.
