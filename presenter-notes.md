# Presenter notes - requested slide replacement

## Sequence

- PDF pages 1-11: Russell's opening slides, in their original order.
- Pages 12-26: Elias's demo, from "How Does Our Python Agent Work?" through the failed-candidate answer reveal.
- Page 27: Russell's original conclusion. It is the last page.

| PDF pages | Source ID | Content |
| --- | --- | --- |
| 1 | Title | Shared title and authors |
| 2-3 | R01-R02 | Correct-answer question and separate answer |
| 4-5 | R03-R04 | Debugging difficulties and missing evidence |
| 6-7 | R05-R06 | Observability and reproducibility |
| 8-9 | R07-R08 | Missing-evidence recap; when to instrument |
| 10-11 | R09-R10 | Trace/span tree; reproducibility levers |
| 12 | S03 | Python agent workflow |
| 13 | S04 | Dataset and MSE |
| 14 | S04-attempts | Five candidates and incumbent decisions |
| 15-16 | S05 | Winner-only question and answer |
| 17 | S06 | Experiment records |
| 18 | S07 | Command 1: original run |
| 19 | S08 | Commands 2-3: replay and compare |
| 20 | S08-results | Matching outcomes |
| 21-22 | S09 | MSE prediction and answer |
| 23 | S10 | Commands 4-5: change and compare |
| 24 | S10-results | First divergence |
| 25-26 | S11 | Failed-candidate question and answer |
| 27 | R-conclusion | Russell's conclusion |

## Pacing and setup

Allow approximately 5 minutes for Russell's introduction, 2 minutes for the Python workflow/records, 2.5 minutes for original/replay, 3 minutes for prediction/divergence, 1.5 minutes for the failed candidate, and 1 minute for the conclusion: 15 minutes. This is an estimate, not a timed rehearsal. Keep the repeated missing-evidence slide brief. Full introductory explanations remain in manuscript detail blocks where they would overflow a slide.

Stay in the PDF until S07. Have the terminal and named JSON files ready at the repository root. Use Python 3.10+ and fresh directories if presenting live. The command examples require the demo implementation from Elias.dev; it is not changed by this slide-only revision. No demo commands were executed for this replacement.

Advance question and answer pages separately. Pause for 15-20 seconds at Q1, Q2, and Q4, and 20-25 seconds at Q3. Do not show the answer first. Run each command separately if delivering live; the PowerShell backtick must be the last character on its line. The commands below are single-line versions for copying.

## Russell opening cues

- R01-R02: Ask whether a correct answer is sufficient; reveal why execution evidence matters.
- R03-R04: Sampling, changing tools, and multi-step chains make the final output insufficient for debugging. Ordinary software is not universally deterministic.
- R05-R06: Contrast investigating a recorded run with reproducing the conditions of a run.
- R07-R08: Briefly recap missing evidence; instrumentation effort should scale with complexity and stakes. The longer trace-first heuristic is backup discussion, not a universal rule to wait for a second failure.
- R09: A span records one operation; a trace connects them. The attribute annotation belongs to the search span, not a separate nested operation. Inspect evidence passed between steps.
- R10: Record model/settings, prompt/tool versions, and tool responses. These controls do not guarantee identical tokens across all environments.

## S03 — How Does Our Python Agent Work?

**Point:** Explain the actual Python loop and when it records evidence.

**Terms:** Symbolic regression searches for an equation fitting observations. A candidate is a proposed equation; the incumbent is the best valid one found so far. Evaluation produces predictions and a score or failure. A rule-based agent follows programmed proposal and selection rules.

**Say:** “We search for an equation that fits five observations. Python saves the inputs and source, then proposes, evaluates, keeps the best valid equation, and logs every attempt. That best equation feeds the next proposal. After five attempts it saves the winner and final status.”

**Optional implementation detail:** Seed 7 initializes a repeatable pseudorandom sequence for the final offset. The candidate budget is the maximum number of attempts: five. Execution is serial, with no retries or external API. Deterministic means the same relevant behavior under controlled inputs/code/runtime; it does not mean identical IDs or timestamps. `proposal()` chooses the equation, `evaluate()` computes its values, and `run()` scores, selects, and records. The input manifest is written before the loop, steps are flushed during it, and result/status are finalized afterward.

## S04 — What does a better fit mean?

**Point:** MSE measures fit to five recorded observations.

**Say:** “MSE is the average squared difference between predictions and observations. For each of these five inputs, subtract the observed target from the prediction, square that difference, and average. Lower means a better fit.”

Point to the equation. “Zero means a perfect fit to these points; it doesn't guarantee accuracy on unseen data.”

**Calculation backup, not spoken by default:** For $x$, residuals are $[-7,-3,-1,-1,-3]$; squares sum to 69, so MSE is 13.8. For $x^2$, five residuals of minus one give MSE 1.0.

## S04-attempts — Five attempts; keep the best valid equation

**Point:** The algorithm retains the best valid candidate, not the latest attempt.

**Say:** “x becomes the first incumbent. Squaring it reduces MSE from 13.8 to 1. Adding one reaches zero, so c003 becomes best. The reciprocal fails and cannot replace it. Seed 7 chooses a final offset of plus one: x squared plus two scores one and also loses. We finish all five attempts, but keep c003.”

Point down the incumbent column. The exact winning source expression is `((x) * (x)) + 1`; c005 is `(((x) * (x)) + 1) + (1)`. Save detailed failure fields for Q4. No terminal switch yet.

## S05 — What would the winner leave out?

**Ask Q2 before the demo:** “An agent evaluates five candidate equations. If we only save the winning equation, what information could we lose?” Keep the answer page hidden. Wait **15–20 seconds**, taking one or two responses.

**Expected:** Inputs/configuration, attempted equations, failures, scores, or the sequence of decisions.

**Reveal:** Advance one page. “All of those matter. We need the experiment, the execution history, and the result together.”

## S06 — One experiment, three complementary records

**Point:** Four files preserve the setup, source, execution history, and result.

**Say:** “The manifest records the experiment's inputs and settings; steps.jsonl records each evaluation; result.json records the selection and counts. These lines mean the files belong to the same run—not that the files are three computational stages.”

**Terms:** A manifest describes inputs, settings, code identity, runtime, and run status. JSONL means one JSON record per line. A hash is a computed fingerprint for checking content.

Explain JSONL in one sentence: “It's one JSON object per line, one per candidate here.” Point to the saved source: “Hashes identify content; agent.py preserves the actual source.” The three JSON records and source snapshot belong to one run; they are not sequential algorithm stages. Say: "Manifest is the setup, agent.py is the code, steps is the execution history, and result is the final outcome."

## S07 — Capture and inspect the original run

**Brief recap (10 seconds):** "Python proposes five equations, retains the best valid score, and records every attempt. Now we will inspect those records."

**CLI distinction:** `run`, `replay`, and `corrupt` execute searches; `compare` reads existing evidence. Five commands use four operations because we compare twice. Keep file inspection to the listed fields.

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

## S08 — Replay means evaluating again

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

## S08-results — Compare the replayed outcomes

**Point:** Interpret the successful comparison using the two rows of the diagram.

**Say:** “All five records match, including the failed evaluation. New run IDs and durations are expected and excluded; the equations, predictions, scores, and error outcomes are not.”

**Return to the question-only page of S09. Do not run the modification yet.**

## S09 — Predict the effect of changing one target

**Ask Q3:** “At x equals minus two, the equation predicts five. If the observed target becomes six, what happens to MSE?” Keep the reveal hidden for **20–25 seconds**.

**Expected:** B, it increases.

**Reveal:** Advance one page. “One residual now has magnitude one. Its square is one, and there are still five observations: one divided by five is 0.2. We replaced one target; we didn't add a sixth point.”

**Follow-up:** “Does a higher MSE necessarily mean a different equation wins?” Take one quick response. “Not necessarily. The winner depends on the other candidates' scores too. Let's check this run.”

**Advance to S10, point to command 4, and switch to the terminal.**

## S10 — Change one observation, then compare

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

## S10-results — Locate the first divergence

**Point:** Use the side-by-side diagram to distinguish a shared winning equation from equivalent executions.

**Term:** Divergence is a detected difference under the comparison contract. A changed hash identifies different content; it does not alone establish why the content changed.

**Say:** “Even before the winner, the very first score differs. Predictions for x stayed the same; the recorded target changed. The report locates the divergence, and the manifest's recorded intervention explains the cause.”

**Math backup:** The first candidate's first squared residual changes from 49 to 64. Its mean increases by 15/5 = 3. The changed $x^2$ scores 1.6 and the final offset candidate scores 0.8, both worse than 0.2.

## S11 — What should happen to a failed candidate?

**Ask Q4 before inspecting the failure:** “The agent tries one over x, but our dataset includes zero. What should happen to the failed attempt?” Wait **15–20 seconds** on the question page.

**Expected:** B, preserve the cause and partial results.

**Reveal:** Advance once, then **switch to the editor** at the fourth line of `demo/runs/class-original/steps.jsonl` (search `c004`).

**Show:** Equation `1 / x`; `status: error`; `score: null`; partial predictions `[-0.5, -1.0]`; exception `ZeroDivisionError`; `row_index: 2`; candidate/run IDs and input hashes.

**Say:** “The first two predictions succeeded. At the third input—row index two—we divide by zero. Keeping the partial output and exception lets us locate that failure. Zero would mean a perfect fit, so the missing score must stay null.”

**Return to Russell's conclusion on page 27.** Mention that retry limit is zero; do not claim a timeout implementation.


## R-conclusion - page 27

Keep Russell's conclusion visible. His two points are to log meaningful traces/spans and to verify correctness independently: a clean trace and consistent output do not prove the answer is right. No additional closing, application, or reference slide follows it.
