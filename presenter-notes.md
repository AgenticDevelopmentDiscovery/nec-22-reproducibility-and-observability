# Presenter notes — 15-minute classroom guide

## Setup before classmates arrive

The command examples use the Python demo from `Elias.dev`. This slide-focused revision does not add or change that implementation; have it available in `demo/` before a live presentation.

Stay in the repository root for **every command**, including commands beginning with `python demo/run.py`. Do not switch into `demo/`:

`nec-22-reproducibility-and-observability/` (the folder containing `justfile` and `demo/`)

Use Python 3.10 or later. The demo uses the standard library only: no API, WSL, Pandoc, or just is needed to run it. Those build tools are only for preparing the document/slides/site.

Use a working Python 3.10+ interpreter consistently for all five commands. If needed, replace only the `python` executable with its installed path.

- Open the PDF in a PDF viewer, not the source-code editor. Advance **one PDF page at a time**. Each of the four questions has a second page revealing its answer.
- Keep a terminal at the repository root and a JSON-capable editor beside the slides.
- Confirm `demo/runs/class-original`, `class-replay`, and `class-changed` do not exist. If any exists, choose a fresh common suffix (for example `class2-original`, `class2-replay`, `class2-changed`) and replace all three names consistently in this guide before starting. Preserve earlier evidence; optional disposal of practice runs is described below.
- Run the tests during preparation: `python -m unittest discover -s demo -v`.
- Execute each demo command **individually**, waiting for its output. Do not paste all five commands as one command.
- Have this guide open for copying one-line commands. All five commands also appear in the slides; PowerShell backticks wrap the longer ones at argument boundaries. A backtick must be the last character on its line, with no trailing spaces. Each block is one command.
- If a live command fails unexpectedly, explain the interruption and use the explicitly labeled expected-result diagrams on the slides. Do not present a diagram or saved output as a successful live execution.

## Timing and navigation

Stable IDs match manuscript headings and website anchors. The deck has 22 instructional frames; four question/reveal overlays occupy two PDF pages each. The footer counts frames, so it repeats on each answer reveal.

The 28-page navigation is: title 1; Q1 2-3; motivation 4; definitions 5-6; workflow 7; MSE 8; candidates 9; Q2 10-11; files 12; command 1 on 13; commands 2-3 on 14; replay results 15; Q3 16-17; commands 4-5 on 18; divergence results 19; Q4 20-21; ancestry 22; trace 23; reproducibility levers 24; pitfalls 25; applications 26; conclusion 27; references 28.

| Time | Slide ID | Teaching purpose |
| --- | --- | --- |
| 0:00–0:15 | Title | Introduce the investigation |
| 0:15–1:00 | S01 | Correct output versus evidence; Q1 |
| 1:00–1:45 | S-why | Model, tool, and multi-step variability |
| 1:45–2:15 | S02 | Logging and observability |
| 2:15–2:45 | S02-repeat | Reproducibility and provenance |
| 2:45–3:20 | S03 | Python search and recording lifecycle |
| 3:20–3:45 | S04 | Dataset and MSE |
| 3:45–4:15 | S04-attempts | Five attempts and incumbent decisions |
| 4:15–4:45 | S05 | What the winner omits; Q2 |
| 4:45–5:15 | S06 | Four complementary files |
| 5:15–6:30 | S07 | Original run and selected JSON fields |
| 6:30–7:25 | S08 | Replay and compare |
| 7:25–7:45 | S08-results | Interpret five matching evaluations |
| 7:45–8:45 | S09 | Predict MSE; Q3 |
| 8:45–10:15 | S10 | Modify and compare |
| 10:15–10:45 | S10-results | Interpret divergence |
| 10:45–11:45 | S11 | Preserve failure; Q4 |
| 11:45–12:15 | S12 | Candidate and run ancestry |
| 12:15–12:45 | S-trace | Trace and span containment |
| 12:45–13:15 | S13 | Reproducibility levers and limits |
| 13:15–13:40 | S-pitfalls | Privacy, useful detail, and correctness |
| 13:40–14:20 | S14 | Coding, simulation, and V&V |
| 14:20–15:00 | S15 | Close with the evidence checklist |

This schedule totals 15 minutes, including about 80 seconds for student responses. It is an estimate, not a completed timed rehearsal. Setup and definitions occupy 5:15; original/replay 2:30; prediction/divergence 3:00; failure/provenance 2:00; applications and closing guidance 2:15. The integration trades some introductory commentary for Russell's technical context. Live file navigation is the main overrun risk: pre-open the three JSON files, show only the named fields, and skip optional backup explanations. Do not cut the five commands or audience response time. References are available afterward, not a speaking segment.

For every slide without an explicit terminal/editor cue below, stay in the PDF. The only planned audience pauses are Q1-Q4; do not add extra questions during the short explanation frames.

## Optional cleanup of disposable practice outputs

Use fresh output names to rehearse again while preserving evidence. For disposable practice outputs only, first inspect the three exact directories and their resolved paths under this repository's `demo/runs/`. Never select the entire `demo` or `runs` directory.

This command only previews removal; `-WhatIf` does not delete anything:

```powershell
Remove-Item -LiteralPath demo/runs/class-original, demo/runs/class-replay, demo/runs/class-changed -Recurse -WhatIf
```

Remove `-WhatIf` only after you personally verify that all three paths are correct and contain disposable practice data you explicitly want deleted. Otherwise retain them and choose new names. No cleanup command was executed during integration; neither the demo nor the build performs it.

## Title — 0:00–0:15

**Point:** This is an investigation of a run, not a claim about the power of a search algorithm.

**Say:** “An agent can return a convincing answer while leaving us unsure what actually happened. We'll run a small equation search, repeat it, and then change one input to see what its records tell us.”

## S01 — A correct answer is only the beginning — 0:15–1:00

Introduce the missing-intermediate-actions problem. **Do not advance to the answer page yet.**

**Ask Q1:** “If an AI agent produces the correct final answer, do we still need to know how it got there?” Let students choose A, B, or C; wait **15–20 seconds**.

**Expected:** B; someone may reasonably prioritize only the result for a low-stakes one-off task. Acknowledge that context, then focus on experiments we need to audit or repeat.

**Reveal:** Advance one page. “For these experiments, B is the strongest answer. A correct output doesn't tell us whether the inputs were right, whether failed attempts were hidden, or whether we could repeat the run.”

**Transition:** “Let's separate four ideas that help answer those questions.”

## S-why - Why agent failures are difficult to debug - 1:00–1:45

**Point:** Preserve Russell's three sources of uncertainty without claiming all software is deterministic.

**Say:** "A model can sample a different response, a tool can return new evidence, and the visible mistake may be downstream of the real problem. A final answer cannot tell us which happened. Deterministic code is easier to replay when its conditions are controlled, but neither ordinary software nor agents are universally deterministic."

**Backup:** A support agent citing a nonexistent policy may have searched badly or misread a useful response. Trace those boundaries before assigning blame. Scale instrumentation to chain length and stakes. This absorbs the repeated 'What goes wrong without it' material; do not read an extra motivation passage.

## S02 — Logging records; observability investigates — 1:45–2:15

**Point:** Logging produces records; observability is what connected evidence lets us investigate.

**Terms:** Logging records events, inputs, outputs, scores, errors, and metadata. Observability is the ability to investigate internal behavior using connected evidence.

**Say:** “Logging saves what happened—for example, equation c004 failed with division by zero. Observability lets us connect that failure to the equation, input, and run so we can investigate it. Lots of disconnected log lines would not answer those questions.”

**Optional definitions:** A trace connects related execution operations; a span records one operation; metrics summarize quantities such as failure counts. Return to trace/span relationships at S12 and S-trace.

## S02-repeat — Reproducibility verifies; provenance explains origins — 2:15–2:45

**Terms:** Reproducibility repeats an experiment using preserved inputs/code/settings and appropriate execution conditions, then verifies agreed outcomes. The comparison contract is that agreement. Provenance records a result's origin and history.

**Say:** “Reproducibility checks a new execution: do all five evaluations match our rules? New timestamps are allowed. Provenance looks backward: which inputs and code produced the winner, and which earlier equations led to it?”

**Spoken summary:** “Logging records what happened. Observability helps us investigate it. Reproducibility helps us repeat and verify it. Provenance explains where results came from.”

## S03 — How Does Our Python Agent Work? — 2:45–3:20

**Point:** Explain the actual Python loop and when it records evidence.

**Terms:** Symbolic regression searches for an equation fitting observations. A candidate is a proposed equation; the incumbent is the best valid one found so far. Evaluation produces predictions and a score or failure. A rule-based agent follows programmed proposal and selection rules.

**Say:** “We search for an equation that fits five observations. Python saves the inputs and source, then proposes, evaluates, keeps the best valid equation, and logs every attempt. That best equation feeds the next proposal. After five attempts it saves the winner and final status.”

**Optional implementation detail:** Seed 7 initializes a repeatable pseudorandom sequence for the final offset. The candidate budget is the maximum number of attempts: five. Execution is serial, with no retries or external API. Deterministic means the same relevant behavior under controlled inputs/code/runtime; it does not mean identical IDs or timestamps. `proposal()` chooses the equation, `evaluate()` computes its values, and `run()` scores, selects, and records. The input manifest is written before the loop, steps are flushed during it, and result/status are finalized afterward.

## S04 — What does a better fit mean? — 3:20–3:45

**Point:** MSE measures fit to five recorded observations.

**Say:** “MSE is the average squared difference between predictions and observations. For each of these five inputs, subtract the observed target from the prediction, square that difference, and average. Lower means a better fit.”

Point to the equation. “Zero means a perfect fit to these points; it doesn't guarantee accuracy on unseen data.”

**Calculation backup, not spoken by default:** For $x$, residuals are $[-7,-3,-1,-1,-3]$; squares sum to 69, so MSE is 13.8. For $x^2$, five residuals of minus one give MSE 1.0.

## S04-attempts — Five attempts; keep the best valid equation — 3:45–4:15

**Point:** The algorithm retains the best valid candidate, not the latest attempt.

**Say:** “x becomes the first incumbent. Squaring it reduces MSE from 13.8 to 1. Adding one reaches zero, so c003 becomes best. The reciprocal fails and cannot replace it. Seed 7 chooses a final offset of plus one: x squared plus two scores one and also loses. We finish all five attempts, but keep c003.”

Point down the incumbent column. The exact winning source expression is `((x) * (x)) + 1`; c005 is `(((x) * (x)) + 1) + (1)`. Save detailed failure fields for Q4. No terminal switch yet.

## S05 — What would the winner leave out? — 4:15–4:45

**Ask Q2 before the demo:** “An agent evaluates five candidate equations. If we only save the winning equation, what information could we lose?” Keep the answer page hidden. Wait **15–20 seconds**, taking one or two responses.

**Expected:** Inputs/configuration, attempted equations, failures, scores, or the sequence of decisions.

**Reveal:** Advance one page. “All of those matter. We need the experiment, the execution history, and the result together.”

## S06 — One experiment, four complementary files — 4:45–5:15

**Point:** Four files preserve the setup, source, execution history, and result.

**Say:** “The manifest records the experiment's inputs and settings; steps.jsonl records each evaluation; result.json records the selection and counts. These lines mean the files belong to the same run—not that the files are three computational stages.”

**Terms:** A manifest describes inputs, settings, code identity, runtime, and run status. JSONL means one JSON record per line. A hash is a computed fingerprint for checking content.

Explain JSONL in one sentence: “It's one JSON object per line, one per candidate here.” Point to the saved source: “Hashes identify content; agent.py preserves the actual source.” The three JSON records and source snapshot belong to one run; they are not sequential algorithm stages. Say: "Manifest is the setup, agent.py is the code, steps is the execution history, and result is the final outcome."

## S07 — Capture and inspect the original run — 5:15–6:30

**Brief recap (10 seconds):** "Python proposes five equations, retains the best valid score, and records every attempt. Now we will inspect those records."

**CLI distinction:** `run`, `replay`, and `corrupt` execute searches; `compare` reads existing evidence. Five commands use four operations because we compare twice. Start command 1 by **5:25**; keep file inspection to the listed fields.

**Show command 1 on S07, then switch to the terminal.** Stay at the repository root.

**Command 1 — original execution**

```powershell
python demo/run.py run --out demo/runs/class-original
```

**Does:** Runs the five-candidate search and saves a manifest, source snapshot, completed-step records, and result in a new directory.

**Expected terminal output:**

```text
completed_with_errors: demo/runs/class-original/manifest.json
```

Exit code: **0**. The run completed and retained a failed candidate.

**Show in the editor, in this order:**

1. `demo/runs/class-original/manifest.json`: `dataset`, `config.seed`, `config.model_id`, `code_sha256`, and `runtime`. The five targets are 5, 2, 1, 2, 5.
2. `demo/runs/class-original/steps.jsonl`: point to `candidate_id`, `equation`, `score`, and `status`. Preview the first three scores: 13.8, 1.0, 0.0. Save the detailed error discussion for Q4.
3. `demo/runs/class-original/result.json`: `attempted: 5`, `failed: 1`, and `best` with candidate `c003`, equation `((x) * (x)) + 1`, score 0.0.

**Concept:** Recorded configuration, logged execution, and selected output provide complementary evidence.

**Say:** “The winner is one line of the story. These files also preserve what we asked the agent to do and what each attempt produced. Completed with errors means a failed candidate is visible; it doesn't mean the program crashed.”

**Return to S08.**

## S08 — Replay means evaluating again — 6:30–7:25

**Point:** The comparison includes intermediate outcomes, not only the winner.

Point to command 2 on S08, then **switch back to the terminal**. Keep the comparison diagram for the next frame, after executing both commands.

**Command 2 — replay**

```powershell
python demo/run.py replay demo/runs/class-original/manifest.json --out demo/runs/class-replay
```

**Does:** Validates the recorded inputs/code/runtime and re-executes the policy on the saved dataset and configuration.

**Expected output:**

```text
completed_with_errors: demo/runs/class-replay/manifest.json
```

Exit code: **0**. Show `demo/runs/class-replay/manifest.json` if time permits: it has a new `run_id` and a `parent_run_id` pointing to the original.

**Concept and spoken explanation:** “This recomputes predictions and scores. Copying old scores would not test the scoring code.”

**Return briefly to S08 to point to command 3, then switch to the terminal.**

**Command 3 — compare, executed separately**

```powershell
python demo/run.py compare demo/runs/class-original demo/runs/class-replay
```

**Does:** Compares experiment identity, ordered candidate outcomes, and the result under the replay contract.

**Expected terminal result:**

```json
{
  "match": true,
  "manifest_changes": [],
  "first_step_difference": null,
  "result_changes": [],
  "compared_steps": 5
}
```

Exit code: **0**. Show this terminal result; it is the shortest useful evidence.

**Return to S08-results.**

## S08-results — Compare the replayed outcomes — 7:25–7:45

**Point:** Interpret the successful comparison using the two rows of the diagram.

**Say:** “All five records match, including the failed evaluation. New run IDs and durations are expected and excluded; the equations, predictions, scores, and error outcomes are not.”

**Return to the question-only page of S09. Do not run the modification yet.**

## S09 — Predict the effect of changing one target — 7:45–8:45

**Ask Q3:** “At x equals minus two, the equation predicts five. If the observed target becomes six, what happens to MSE?” Keep the reveal hidden for **20–25 seconds**.

**Expected:** B, it increases.

**Reveal:** Advance one page. “One residual now has magnitude one. Its square is one, and there are still five observations: one divided by five is 0.2. We replaced one target; we didn't add a sixth point.”

**Follow-up:** “Does a higher MSE necessarily mean a different equation wins?” Take one quick response. “Not necessarily. The winner depends on the other candidates' scores too. Let's check this run.”

**Advance to S10, point to command 4, and switch to the terminal.**

## S10 — Change one observation, then compare — 8:45–10:15

**Command 4 — deliberate input modification**

```powershell
python demo/run.py corrupt demo/runs/class-original/manifest.json --out demo/runs/class-changed
```

**Does:** Validates the original and creates a new run with only the first target changed from 5 to 6. It records the intervention and new dataset hash; it does not modify the original files.

**Expected output:**

```text
completed_with_errors: demo/runs/class-changed/manifest.json
```

Exit code: **0**.

**Show:** `demo/runs/class-changed/manifest.json`, particularly `change`, `dataset[0]`, and `dataset_hash`. Then show `demo/runs/class-changed/result.json`: `best.candidate_id: c003`, same equation, score **0.2**.

**Concept and spoken explanation:** “The prediction is confirmed: the same equation now scores 0.2. It still beats this run's alternatives, so it remains the winner.”

**Return briefly to S10 to point to command 5, then switch to the terminal.**

**Command 5 — compare the changed run, separately**

```powershell
python demo/run.py compare demo/runs/class-original demo/runs/class-changed
```

**Does:** Finds the first differing candidate record and also compares manifest/result fields.

**Expected result:** `match: false`; `first_step_difference.step: 1`; changes to `inputs.dataset_hash` and `score` from **13.8 to 16.8**; `result_changes` includes `best.score` from **0.0 to 0.2**. `compared_steps: 1` means the step scan stopped at its first mismatch.

Exit code **1 is intentional and expected**. If needed, `$LASTEXITCODE` immediately after the command displays it in PowerShell. It signals “different runs,” not an unexpected crash.

**Show:** The terminal's `first_step_difference`, then return to S10-results.

## S10-results — Locate the first divergence — 10:15–10:45

**Point:** Use the side-by-side diagram to distinguish a shared winning equation from equivalent executions.

**Term:** Divergence is a detected difference under the comparison contract. A changed hash identifies different content; it does not alone establish why the content changed.

**Say:** “Even before the winner, the very first score differs. Predictions for x stayed the same; the recorded target changed. The report locates the divergence, and the manifest's recorded intervention explains the cause.”

**Math backup:** The first candidate's first squared residual changes from 49 to 64. Its mean increases by 15/5 = 3. The changed $x^2$ scores 1.6 and the final offset candidate scores 0.8, both worse than 0.2.

## S11 — What should happen to a failed candidate? — 10:45–11:45

**Ask Q4 before inspecting the failure:** “The agent tries one over x, but our dataset includes zero. What should happen to the failed attempt?” Wait **15–20 seconds** on the question page.

**Expected:** B, preserve the cause and partial results.

**Reveal:** Advance once, then **switch to the editor** at the fourth line of `demo/runs/class-original/steps.jsonl` (search `c004`).

**Show:** Equation `1 / x`; `status: error`; `score: null`; partial predictions `[-0.5, -1.0]`; exception `ZeroDivisionError`; `row_index: 2`; candidate/run IDs and input hashes.

**Say:** “The first two predictions succeeded. At the third input—row index two—we divide by zero. Keeping the partial output and exception lets us locate that failure. Zero would mean a perfect fit, so the missing score must stay null.”

**Return to S12.** Mention that retry limit is zero; do not claim a timeout implementation.

## S12 — Trace the winner to its origin — 11:45–12:15

**Point:** Ancestry and operation nesting answer different questions.

**Terms:** Lineage links results to parent candidates or source runs. A trace connects operations in one execution; a span records a unit of work, here one candidate evaluation. These evaluations are sibling spans under the run, even where their equations have parent-child relationships. The demo has a local educational schema, not an OpenTelemetry exporter.

**Say:** “The winner c003 comes from c002, which comes from c001. These arrows are parent to child; the records store the reverse lookup as parent_candidate_id.”

Keep the SVG visible. If the editor is already open, briefly point to `c002.parent_candidate_id: c001` and `c003.parent_candidate_id: c002`.

“Run ancestry tells us which run was replayed or modified. Span nesting tells us which run contained the evaluation. Here evaluations are sibling operations even when their equations have parent-child relationships.”

The diagram includes a note about c005 and independent c004 so students do not mistake a three-node winner chain for all five attempts.

## S-trace - A trace connects the steps of an agent run - 12:15–12:45

**Point:** A trace groups operations; parent spans describe containment.

**Say:** "This support request has planning, search, and drafting spans. Inspect what the search returned before blaming the final reply. The dashed box lists attributes of the search span, not another operation. Our equation ancestry arrows answer a different question: which equation produced which candidate?"

**Backup:** Record useful inputs/outputs, status, timing, model/settings, and tool arguments. If retrieved evidence is irrelevant, investigate retrieval; if useful evidence became a false claim, inspect drafting. This is an illustrative support-agent trace, not a run produced by our Python demo. A successful span can contain a wrong answer. Return to slides throughout; no new command or audience pause.

## S13 — Reproducibility levers, and their limits — 12:45–13:15

**Say:** “For a live agent, record the visible requests and responses, tool calls, retrieved content, and environment. Define what counts as the same result before comparing. A seed alone doesn't control every external dependency.”

Name model version and sampling settings, prompt/tool versions, and actual tool responses. A stable model alias or a seed is not a complete guarantee. Distinguish recorded-response replay from another live model call. Mention that a distributional claim requires repeated runs and a chosen metric/tolerance; do not introduce a statistical methods lecture.

## S-pitfalls - Three pitfalls of instrumentation - 13:15–13:40

**Point:** Preserve Russell's three instrumentation pitfalls.

**Say:** "Do not store secrets or unnecessary personal data. Record meaningful operations instead of an unreadable stream of tiny events. Finally, a successful trace or matching replay does not prove a correct answer. Evaluate correctness separately."

**Backup:** Redact before storage; restrict access and retention. Redaction may limit exact replay. Recording depth should serve a real investigation. Never replay external side effects automatically. These are design limits, not features implemented by this offline example.

## S14 — Where would you use these records? — 13:40–14:20

**Say:** “For a coding agent, link tool calls and code revisions to tests and failed attempts: which edit broke the tests? For a simulation agent, preserve material properties, input files, model versions, solver settings, and results: did the inputs or solver change?”

“Include boundary conditions and software versions in the simulation record. Reproducibility supports verification and validation, but repeating a result does not prove the equations were implemented correctly or that they represent the physical system adequately.”

## S15 — Keep the evidence, not just the winner — 14:20–15:00

Point to the four checks: preserve inputs/code, record evaluations and failures, replay and compare, investigate differences. Preserve Russell's closing reminder: a consistent workflow can still be wrong; verify the result.

**Optional, only if ahead:** “Same winner: same run?” Expected answer: no; today's dataset modification is the counterexample. No extra slide or long discussion.

**Closing statement:** “The answer tells us what the agent produced. The records help us investigate how it got there, repeat the execution, and explain why another run differs.”

Leave references available after the final slide for questions. Do not spend the last minute reading URLs.

## Optional short explanations for questions afterward

| Distinction | Natural explanation |
| --- | --- |
| Logging / observability | Logging saves events; connected evidence lets us investigate them. |
| Reproducibility / identical output | Matching winners is one observation; reproducibility verifies the required execution outcomes. IDs and times may differ. |
| Provenance / candidate ancestry | Candidate parents are one part of provenance, alongside input, code, configuration, and run origins. |
| Rule-based / LLM agent | This Python proposer follows programmed rules and a seeded offset; it makes no model call. |
| Manifest / evaluation log | The manifest describes the experiment; the log records each attempted evaluation. |
| Replay / copied results | Replay recalculates predictions and scores; copying them would not test execution. |

These are backup explanations, not additional timed presentation segments.
