# Presenter notes — 15 minutes

The rendered material is in `sections/*.prose.md`. These cues support the shared document/deck/site and do not render as extra slides. Keep a terminal and the three original-run files open beside the presentation.

## Before presenting

- Run the tests in `demo/README.md` and rehearse all five commands.
- Confirm the three destination directories are unused, or choose fresh names throughout.
- Build with `just build` in a configured toolchain. Inspect the PDF slide pages for clipped commands or crowded tables.
- Keep previously generated run folders available as a fallback if the terminal fails; label them as saved evidence, not a live run.
- No API keys or internet access are needed for the demo.

## 0:00–2:00 — Context

Define reproducibility, observability, and provenance through their three questions. Explain the propose-evaluate loop before introducing file formats.

Say explicitly: “This demo re-executes an offline rule-based agent. It does not prove that a hosted model returns the same text twice.” Establish that timing and execution IDs will differ, while ordered outcomes must match.

## 2:00–4:00 — Motivation

Use the unchanged equation with a changed score as the puzzle. Ask the audience to name possible causes, then show the map of moving inputs. Mention that corpus snapshots must preserve content, not only a search query or a hash.

Connect fitness scores to C2 and candidate genealogy to the capstone. Avoid suggesting this repository imports the actual course harness.

## 4:00–6:00 — Capture and scoring

Explain the manifest, step log, and result file. Point to the saved source, dataset, hashes, runtime, and explicit null model settings.

Run the original experiment. Show that the first three scores are 13.8, 1.0, and 0.0. Explain that the incumbent affects later proposals; the final mutation uses the recorded seed.

## 6:00–8:00 — Replay

Run replay and compare. Highlight `match: true` and five compared steps. Show that the new manifest has a different run ID and a parent-run link to the original.

Ask: “Would copying yesterday's scores into a new file test the scoring code?” Answer: no; this replay recomputes them from preserved inputs.

## 8:00–10:00 — Deliberate divergence

Run `corrupt`, then compare the original and changed runs. The nonzero comparison exit is expected. Point to row 0's target changing from 5 to 6, the dataset hash difference, and the first score changing from 13.8 to 16.8.

The first equation and predictions are unchanged. The trace places the discrepancy at evaluation input; the manifest's explicit intervention supplies the cause. Do not describe the hash alone as a causal explanation.

## 10:00–12:00 — Failures and lineage

Open candidate `c004` in the step log. It keeps two predictions, the zero-division exception, row index 2, and a null score. Point out the attempted/failed totals in the result. Explain why silently dropping it would misrepresent reliability.

Follow `c003` → `c002` → `c001`. Contrast candidate ancestry with operation nesting, then show the parent-run link. Briefly explain how actual timeouts and retries would require additional records; this demo implements neither.

## 12:00–13:00 — Transfer

Show where a live proposer would replace the rule-based policy. The required boundaries are the visible model request/response, tool inputs/outputs, and retrieved content. A trace is a record of observable execution, not hidden model reasoning.

## 13:00–15:00 — Check understanding

Ask the exit question: the same winner survives, but an early score changes. Under this tutorial's contract, replay fails. Then ask the audience to identify one missing input in their own agent runs.

Close with the three references and the next experiment: instrument the actual course agent and measure which reproducibility claim it can support.
