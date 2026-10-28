# Demo verification

Verified on 2026-10-28 with Windows Python 3.12.10 using the standard library. These are observed results, not simulated output. The demo implementation and tests were not changed during this refinement.

## Automated checks

`python -m unittest discover -s demo -v`: **4 tests passed**.

- Re-execution matches, selects the zero-error winner, and preserves failed partial predictions and lineage.
- A changed target causes the first score difference at step 1: 13.8 versus 16.8.
- A stale dataset hash and attempts to overwrite a run are rejected.
- A missing step and an altered winner score are detected by comparison.

## Executed demonstration

Educational-refinement verification runs were generated individually under `demo/runs/education-20261028-original`, `demo/runs/education-20261028-replay`, and `demo/runs/education-20261028-changed`, using fresh paths and the installed Python executable. Run directories are ignored local artifacts. Hash checks confirm all 36 files in the nine preexisting run directories remain unchanged, including the earlier verification/finalization runs. The `class-original`, `class-replay`, and `class-changed` paths remain unused for the presentation. No practice cleanup was executed.

| Check | Observed |
| --- | --- |
| Original and replay | `match: true`; 5 steps compared |
| Original and changed | `match: false`; first difference at step 1 |
| Changed fields at first divergence | `inputs.dataset_hash`, `score` |
| Original winner | `c003`, MSE 0.0 |
| Changed winner | `c003`, MSE 0.2 |
| Failures in each run | One division by zero, retained in the step log |

`compare` returned 0 for matching runs and 1 for the intentional divergence. Both are expected outcomes. See `README.md` in this directory for reproduction commands.

The five commands (run, replay, matching compare, corrupt, changed compare) returned 0, 0, 0, 0, 1 respectively. The changed run still has five observations. Candidate c001 changes from MSE 13.8 to 16.8. Candidate c004 preserves `ZeroDivisionError`, failed row index 2, and partial predictions `[-0.5, -1.0]`. Verified parent links are c001 → c002 → c003; c005 descends from c003 and c004 has no parent.

The five original outcomes are 13.8, 1.0, 0.0, error/null, and 1.0. Recorded incumbent inputs are empty, c001, c002, c003, and c003. Candidate c005 is exactly `(((x) * (x)) + 1) + (1)`: the seed-7 offset is +1, producing x² + 2. The final selected candidate is c003, confirming that the algorithm retains the best valid candidate rather than the last attempt.

## Rendering status

After installing the toolchain in Ubuntu-20.04 WSL, `wsl -d Ubuntu-20.04 -- just build` completed successfully and generated:

- `output/document.pdf`: 12 pages.
- `output/slides.pdf`: 25 pages: title, 19 instructional frames, four additional answer-reveal pages, and references.
- `_site/index.html`, stylesheet, and copies of both PDFs.

All 25 slide pages were visually inspected. Two overflowing workflow labels in the first build were shortened at the same font size, followed by a successful rebuild and full-size reinspection. The final images differ from the inspected first build only on the corrected workflow and shortened artifact-summary pages. All five commands remain visible on pages 12, 13, and 17. Four questions appear on pages 2, 9, 15, and 19; each answer is on the following page. Extracted text confirms no answer on the question page and no changed numerical scores before the MSE prediction reveal. No unresolved clipping, overlap, missing citations, or unexpected blank frames was observed. Footer numbers advance from 1 to 21, repeating only for the four answer reveals. All 12 final document pages were previewed.

HTML checks confirm all five commands and 19 anchors, along with five identical SVG copies and identical downloadable PDF copies. Source checks confirm all five command blocks and all four question/answer pairs are unchanged from the preceding commit. Presenter IDs and the continuous 15-minute timing table match the source. The prior refinement included a Chrome layout check; this refinement verified the rebuilt HTML structurally rather than repeating a browser interaction test.

The immediately preceding version had a 10-page document and 23-page slide PDF. This refinement adds two instructional frames for paired definitions and five-candidate progression while preserving the commands and interactions. Temporary inspection PNGs are outside the repository, with none in `output/`. Historical assessments remain in `docs/refinement-review.md` and `docs/finalization-review.md`; the current self-review is `docs/educational-review-20261028.md`. The 15-minute guide has not undergone a timed speaking rehearsal.

Versions: just 1.58.0, Pandoc 3.11, XeTeX 0.999991 from TeX Live 2019/Debian. The optional Fira fonts are absent, so Metropolis emits font lookup messages and uses fallback fonts. These messages do not prevent successful PDF generation.
