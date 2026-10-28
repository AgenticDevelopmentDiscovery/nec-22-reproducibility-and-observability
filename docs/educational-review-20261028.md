# Tutorial 22 educational refinement — 2026-10-28

## Inspection and scope

Authoritative working tree: `C:/Users/ejlyn/ENGR689/nec-22-reproducibility-and-observability/nec-22-reproducibility-and-observability`. Repository: `AgenticDevelopmentDiscovery/nec-22-reproducibility-and-observability`. Started clean on `Elias.dev` at `930d515dc0ea2ba1bbe73016b970f69bd5000ad4`; the live remote matched. Local/remote main were `9e065f8b6be2cacff03a41fdbfa1696d653346f6`.

Read the existing paired manuscript, topic, presenter guide, Python implementation/tests, demo documentation, framework instructions, build/filter/metadata, figures, references, and prior review records. Visually inspected the actual 23-page slide PDF before editing. Saved baseline PDFs and a hash inventory of all 36 existing experiment files outside the repository. No obsolete template copy or new repository was used.

This is an implementation and educational self-review, not an independent panel or formal `/round`. Historical review documents are unchanged. The existing four questions, five commands, Metropolis theme, shared-source filter, and Python implementation are preserved.

## Findings and changes

| Stable ID / final PDF page | Refinement |
| --- | --- |
| S02 / 4 | Logging and observability now each have a definition, tutorial example, and investigative purpose. |
| S02-repeat / 5 (added) | Reproducibility and provenance distinguish repeat/verify from origin/history; expected ID/timing differences are explicit. |
| S03 / 6 | Retitled “How Does Our Python Agent Work?”; expanded the existing diagram with initialization, logging, incumbent feedback, and finalization. |
| S04 / 7 | Defines MSE in words and identifies prediction/observation symbols; retains the generalization limit. |
| S04-attempts / 8 (added) | Shows all five outcomes and incumbent decisions; explains c005's seeded +1 offset and why c003 still wins. |
| S06 / 11 | Defines manifest, JSONL, and hash in context; connects the fingerprint to the saved source. |
| S07 / 12 | Labels the run operation and distinguishes the four CLI operations from the internal search in detailed prose. |
| S08 / 13; S08-results / 14 | Clarifies validation/reexecution, saved-record comparison, and comparison criteria. |
| S10 / 17; S10-results / 18 | Clarifies the non-destructive target intervention, defines divergence, and distinguishes the detected difference from its recorded cause. |
| S12 / 21 | Defines lineage, trace, and span while preserving equation/run ancestry distinctions. |

Only two instructional frames were added: 17 → 19, and 23 → 25 physical PDF pages. The document grows from 10 to 12 pages to retain detailed terminology and implementation explanations. Candidate, incumbent, symbolic regression, evaluation, deterministic execution, rule-based agent, seed, budget, replay, comparison contract, divergence, hash, lineage, trace/span, and JSONL are explained where relevant in slides, manuscript, or notes; no glossary-slide sequence was added.

## Implementation cross-check

`run()` saves the initial manifest and `agent.py` before the loop. `proposal()` uses programmed rules and the current best candidate; `evaluate()` computes predictions; `run()` computes MSE or retains errors/partial predictions. Only a valid, strictly better result replaces the incumbent (or the first valid result when none exists). Every attempt is written and flushed. After five attempts, the program saves the result and finalizes manifest status.

Fresh logs confirm scores 13.8, 1.0, 0.0, null/error, and 1.0; incumbent inputs empty, c001, c002, c003, c003; and parents null, c001, c002, null, c003. Seed 7 selects offset +1 for c005, yielding x² + 2. The winner remains c003. The source and tests are unchanged.

## Student-perspective self-review

- Definitions explain why evidence is useful, not just list fields. Logging is the recording activity; observability uses connected evidence to investigate behavior.
- Reproducibility checks a repeated execution under explicit criteria. Provenance records where results came from; ancestry is only one part of it.
- Workflow and candidate progression make the agent's programmed feedback loop visible. MSE and selection are explained before live commands.
- Records have complementary roles; their association diagram is retained. Saving source content is distinct from recording its fingerprint.
- Replay recalculates; compare reads recorded outcomes. A modified target explains differing scores even when predictions and winning equation remain unchanged.
- Failed attempts retain partial evidence and cannot win. Candidate parents and span parents describe different relationships.
- Existing coding-agent and simulation examples remain the practical transfer point.

## Validation and limits

Four existing unit tests passed on Windows Python 3.12.10. Five separate CLI commands in fresh `education-20261028-*` paths returned expected exit codes 0, 0, 0, 0, 1. Replay matched all five records; changed input first diverged at step 1, with the same winner at MSE 0.2. All 36 preexisting experiment files retain their hashes; classroom paths remain unused; no cleanup occurred.

The final `wsl -d Ubuntu-20.04 -- just build` succeeded for the document, slides, and website. All 25 slide pages and 12 document pages were visually inspected. The initial workflow had two labels extending beyond their boxes; shorter labels fixed this without shrinking type. Final affected pages were reinspected and all other slide images are identical to the inspected first build. No unresolved formatting defects were observed.

Extracted PDF checks verify all five commands on pages 12/13/17 and four hidden questions with next-page reveals at 2–3, 9–10, 15–16, and 19–20. Commands and question/answer source blocks are unchanged. Frame numbering, 19 matching source/notes/HTML IDs, website PDF/SVG copies, and the 15-minute timing table were checked. Inspection PNGs remain outside the repository. Generated outputs are ignored under the existing conventions.

Presenter notes include a 35-second Python recap immediately before execution, short term definitions, optional distinction explanations, and revised navigation. Live original/replay and prediction/divergence each retain three minutes. The schedule totals 15 minutes including roughly 80 seconds of audience response time; no timed speaking rehearsal was performed. The expanded preparation block and live file navigation are the likely overrun points. Shorter opening/closing commentary and skipping optional explanations preserve the core demonstration time.

Optional Fira fonts remain absent; readable fallback fonts render successfully. WSL's existing configuration warning does not block the build. No new dependencies, formal review artifacts, Python changes, merge, pull request, tag, or deployment are required. The validated source changes are authorized for a normal commit/push to `Elias.dev`.
