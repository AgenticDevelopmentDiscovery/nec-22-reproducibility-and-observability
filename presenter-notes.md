# Presenter notes — 15-minute classroom guide

## Setup before classmates arrive

Stay in the repository root for **every command**, including commands beginning with `python demo/run.py`. Do not switch into `demo/`:

`nec-22-reproducibility-and-observability/` (the folder containing `justfile` and `demo/`)

Use Python 3.10 or later. The demo uses the standard library only: no API, WSL, Pandoc, or just is needed to run it. Those build tools are only for preparing the document/slides/site.

If `python` is not configured, replace only that executable in each command with your working interpreter. On this computer, the PowerShell prefix is:

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
```

For example, the full original-run invocation is:

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" demo/run.py run --out demo/runs/class-original
```

Use the same interpreter throughout. This is an alternative to the command below, not an extra run.

- Open the PDF in a PDF viewer, not the source-code editor. Advance **one PDF page at a time**. Each of the four questions has a second page revealing its answer.
- Keep a terminal at the repository root and a JSON-capable editor beside the slides.
- Confirm `demo/runs/class-original`, `class-replay`, and `class-changed` do not exist. If any exists, choose a fresh common suffix (for example `class2-original`, `class2-replay`, `class2-changed`) and replace all three names consistently in this guide before starting. Preserve earlier evidence; optional disposal of practice runs is described below.
- Run the tests during preparation: `python -m unittest discover -s demo -v`.
- Execute each demo command **individually**, waiting for its output. Do not paste all five commands as one command.
- Have this guide open for copying one-line commands. All five commands also appear in the slides; PowerShell backticks wrap the longer ones at argument boundaries. A backtick must be the last character on its line, with no trailing spaces. Each block is one command.
- If a live command fails unexpectedly, use the separately labeled verification records described in `demo/verification.md`. Tell the class they are saved evidence rather than a live execution.

## Timing and navigation

Stable IDs S01–S15 match the `#s01`–`#s15` source headings and website anchors. S08-results and S10-results hold the diagrams after their command frames. A PDF page is not the same as an instructional slide: a question/reveal uses two pages of one frame. The footer counts frames, so its number stays the same during a question's answer reveal.

The verified 23-page PDF navigation is: Q1 pages 2–3, Q2 pages 7–8, Q3 pages 13–14, and Q4 pages 17–18. The first page of each pair asks; the next reveals. Commands 1, 2–3, and 4–5 are on pages 10, 11, and 15. Results follow on pages 12 and 16. Title is page 1, closing takeaway page 22, and references page 23.

| Time | Slide ID | Teaching purpose |
| --- | --- | --- |
| 0:00–0:20 | Title | Introduce the investigation |
| 0:20–2:00 | S01 | Correct output versus evidence; Q1 |
| 2:00–2:40 | S02 | Distinguish the four concepts |
| 2:40–3:20 | S03 | Propose/evaluate/select workflow |
| 3:20–4:05 | S04 | Dataset and MSE |
| 4:05–4:35 | S05 | What the winner omits; Q2 |
| 4:35–5:00 | S06 | Three complementary records |
| 5:00–6:30 | S07 | Original execution and inspection |
| 6:30–7:40 | S08 | Show and run replay and comparison commands |
| 7:40–8:00 | S08-results | Interpret five matching evaluations |
| 8:00–9:00 | S09 | Predict MSE; Q3 |
| 9:00–10:30 | S10 | Show and run modification and comparison commands |
| 10:30–11:00 | S10-results | Interpret the first divergence |
| 11:00–12:05 | S11 | Preserve a failed attempt; Q4 |
| 12:05–13:00 | S12 | Candidate/run/span relationships |
| 13:00–13:35 | S13 | Transfer to live agents |
| 13:35–14:20 | S14 | Coding and engineering applications |
| 14:20–15:00 | S15 | Close with the evidence checklist |

This schedule includes about 80 seconds for student responses. It is a pacing estimate, **not a completed timed rehearsal**. The highest overrun risks are navigating JSON files and extending discussion. Collect one or two responses, point to preselected fields, and skip the optional closing question if behind. References are available after the closing slide; do not read them aloud.

## Optional cleanup of disposable practice outputs

Using fresh output names is the safest way to rehearse again while preserving evidence. Alternatively, **only if all three named directories contain disposable practice outputs**, you may explicitly choose to remove them before class. Confirm that your terminal is at this repository's root and inspect the directories first. The following PowerShell command permanently removes only these three directories and their contents:

```powershell
Remove-Item -Recurse -Force demo/runs/class-original, demo/runs/class-replay, demo/runs/class-changed
```

Do not run it on records you want to keep. Do not delete the entire `demo` directory. This cleanup is documentation only: it is never run by the demo or build, and it was not executed during this refinement. Existing outputs must not be deleted or overwritten without your explicit choice.

## Title — 0:00–0:20

**Point:** This is an investigation of a run, not a claim about the power of a search algorithm.

**Say:** “An agent can return a convincing answer while leaving us unsure what actually happened. We'll run a small equation search, repeat it, and then change one input to see what its records tell us.”

## S01 — A correct answer is only the beginning — 0:20–2:00

Introduce the missing-intermediate-actions problem. **Do not advance to the answer page yet.**

**Ask Q1:** “If an AI agent produces the correct final answer, do we still need to know how it got there?” Let students choose A, B, or C; wait **15–20 seconds**.

**Expected:** B; someone may reasonably prioritize only the result for a low-stakes one-off task. Acknowledge that context, then focus on experiments we need to audit or repeat.

**Reveal:** Advance one page. “For these experiments, B is the strongest answer. A correct output doesn't tell us whether the inputs were right, whether failed attempts were hidden, or whether we could repeat the run.”

**Transition:** “Let's separate four ideas that help answer those questions.”

## S02 — Four ideas, four different jobs — 2:00–2:40

**Point:** Logging produces records; observability is what connected evidence lets us investigate.

**Say:** “Logging records an event. Observability lets us connect events to a run and its inputs so we can investigate behavior. Reproducibility asks whether we can repeat the execution under a defined comparison rule. Provenance tells us where a result came from.”

Use one contrast: “Candidate failed” versus “candidate c004, in this run, failed at this input.” Avoid suggesting more logs automatically produce observability.

## S03 — Propose, evaluate, select — 2:40–3:20

**Point:** Explain the diagram before file formats.

**Say:** “Symbolic regression searches for an equation that fits data. The proposer suggests an equation, the harness evaluates it, and MSE determines whether it becomes our incumbent—the best valid equation so far.”

Follow the arrows, including feedback. “This proposer follows fixed rules plus a seeded mutation. It isn't calling an LLM. That makes the recording method easier to see.”

## S04 — What does a better fit mean? — 3:20–4:05

**Point:** MSE measures fit to five recorded observations.

**Say:** “For each input, compare the equation's prediction with the observed target, square the difference, and average over five points. Lower is better. Our first three equations score 13.8, 1.0, and zero.”

Point to $x^2+1$. “Zero means it fits these points exactly. It doesn't establish accuracy on unseen data.”

**Calculation backup, not spoken by default:** For $x$, residuals are $[-7,-3,-1,-1,-3]$; squares sum to 69, so MSE is 13.8. For $x^2$, five residuals of minus one give MSE 1.0.

## S05 — What would the winner leave out? — 4:05–4:35

**Ask Q2 before the demo:** “An agent evaluates five candidate equations. If we only save the winning equation, what information could we lose?” Keep the answer page hidden. Wait **15–20 seconds**, taking one or two responses.

**Expected:** Inputs/configuration, attempted equations, failures, scores, or the sequence of decisions.

**Reveal:** Advance one page. “All of those matter. We need the experiment, the execution history, and the result together.”

## S06 — One experiment, three complementary records — 4:35–5:00

**Point:** Three kinds of evidence share a run ID.

**Say:** “The manifest records the experiment's inputs and settings; steps.jsonl records each evaluation; result.json records the selection and counts. These lines mean the files belong to the same run—not that the files are three computational stages.”

Explain JSONL in one sentence: “It's one JSON object per line, one per candidate here.” Point to the saved source: “Hashes identify content; the snapshots let us recover it.”

## S07 — Capture and inspect the original run — 5:00–6:30

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

## S08 — Replay means evaluating again — 6:30–7:40

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

## S08-results — Compare the replayed outcomes — 7:40–8:00

**Point:** Interpret the successful comparison using the two rows of the diagram.

**Say:** “All five records match, including the failed evaluation. New run IDs and durations are expected and excluded; the equations, predictions, scores, and error outcomes are not.”

**Return to the question-only page of S09. Do not run the modification yet.**

## S09 — Predict the effect of changing one target — 8:00–9:00

**Ask Q3:** “At x equals minus two, the equation predicts five. If the observed target becomes six, what happens to MSE?” Keep the reveal hidden for **20–25 seconds**.

**Expected:** B, it increases.

**Reveal:** Advance one page. “One residual now has magnitude one. Its square is one, and there are still five observations: one divided by five is 0.2. We replaced one target; we didn't add a sixth point.”

**Follow-up:** “Does a higher MSE necessarily mean a different equation wins?” Take one quick response. “Not necessarily. The winner depends on the other candidates' scores too. Let's check this run.”

**Advance to S10, point to command 4, and switch to the terminal.**

## S10 — Change one observation, then compare — 9:00–10:30

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

## S10-results — Locate the first divergence — 10:30–11:00

**Point:** Use the side-by-side diagram to distinguish a shared winning equation from equivalent executions.

**Say:** “Even before the winner, the very first score differs. Predictions for x stayed the same; the recorded target changed. The report locates the divergence, and the manifest's recorded intervention explains the cause.”

**Math backup:** The first candidate's first squared residual changes from 49 to 64. Its mean increases by 15/5 = 3. The changed $x^2$ scores 1.6 and the final offset candidate scores 0.8, both worse than 0.2.

## S11 — What should happen to a failed candidate? — 11:00–12:05

**Ask Q4 before inspecting the failure:** “The agent tries one over x, but our dataset includes zero. What should happen to the failed attempt?” Wait **15–20 seconds** on the question page.

**Expected:** B, preserve the cause and partial results.

**Reveal:** Advance once, then **switch to the editor** at the fourth line of `demo/runs/class-original/steps.jsonl` (search `c004`).

**Show:** Equation `1 / x`; `status: error`; `score: null`; partial predictions `[-0.5, -1.0]`; exception `ZeroDivisionError`; `row_index: 2`; candidate/run IDs and input hashes.

**Say:** “The first two predictions succeeded. At the third input—row index two—we divide by zero. Keeping the partial output and exception lets us locate that failure. Zero would mean a perfect fit, so the missing score must stay null.”

**Return to S12.** Mention that retry limit is zero; do not claim a timeout implementation.

## S12 — Trace the winner to its origin — 12:05–13:00

**Point:** Ancestry and operation nesting answer different questions.

**Say:** “The winner c003 comes from c002, which comes from c001. These arrows are parent to child; the records store the reverse lookup as parent_candidate_id.”

Keep the SVG visible. If the editor is already open, briefly point to `c002.parent_candidate_id: c001` and `c003.parent_candidate_id: c002`.

“Run ancestry tells us which run was replayed or modified. Span nesting tells us which run contained the evaluation. Here evaluations are sibling operations even when their equations have parent-child relationships.”

The diagram includes a note about c005 and independent c004 so students do not mistake a three-node winner chain for all five attempts.

## S13 — Carry the evidence into a live agent — 13:00–13:35

**Say:** “For a live agent, record the visible requests and responses, tool calls, retrieved content, and environment. Define what counts as the same result before comparing. A seed alone doesn't control every external dependency.”

Distinguish recorded-response replay from another live model call. Mention that a distributional claim requires repeated runs and a chosen metric/tolerance; do not introduce a statistical methods lecture.

## S14 — Where would you use these records? — 13:35–14:20

**Say:** “For a coding agent, link tool calls and code revisions to tests and failed attempts: which edit broke the tests? For a simulation agent, preserve material properties, input files, model versions, solver settings, and results: did the inputs or solver change?”

“These are the same questions as our toy search, but a production system also needs retention, access control, and interrupted-run handling.”

## S15 — Keep the evidence, not just the winner — 14:20–15:00

Point to the three checks: preserve inputs/code, compare execution outcomes, keep failures and origins.

**Optional, only if ahead:** “Same winner: same run?” Expected answer: no; today's dataset modification is the counterexample. No extra slide or long discussion.

**Closing statement:** “The answer tells us what the agent produced. The records help us investigate how it got there, repeat the execution, and explain why another run differs.”

Leave references available after the final slide for questions. Do not spend the last minute reading URLs.
