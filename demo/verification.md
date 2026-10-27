# Demo verification

Verified on 2026-10-27 with Windows Python 3.12.10 using the standard library. These are observed results, not simulated output. The demo implementation and tests were not changed during this refinement.

## Automated checks

`python -m unittest discover -s demo -v`: **4 tests passed**.

- Re-execution matches, selects the zero-error winner, and preserves failed partial predictions and lineage.
- A changed target causes the first score difference at step 1: 13.8 versus 16.8.
- A stale dataset hash and attempts to overwrite a run are rejected.
- A missing step and an altered winner score are detected by comparison.

## Executed demonstration

Finalization verification runs were generated individually under `demo/runs/finalize-20261027-144035-original`, `demo/runs/finalize-20261027-144035-replay`, and `demo/runs/finalize-20261027-144035-changed`. The longer commands were executed using the same PowerShell continuation syntax shown in the slides, with fresh validation paths and the installed Python executable. Run directories are ignored local artifacts. Hash checks confirm all 24 files in the previous original/replay/changed and verify-20261027-* runs remain unchanged. The `class-original`, `class-replay`, and `class-changed` paths remain unused for the presentation. No practice cleanup was executed.

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

## Rendering status

After installing the toolchain in Ubuntu-20.04 WSL, `wsl -d Ubuntu-20.04 -- just build` completed successfully and generated:

- `output/document.pdf`: 10 pages.
- `output/slides.pdf`: 23 pages: title, 17 instructional frames, four additional answer-reveal pages, and references.
- `_site/index.html`, stylesheet, and copies of both PDFs.

All 23 final slide pages were visually inspected, with additional full-size checks of command pages 10, 11, and 15. All five commands are visible in order, without shrinking the existing font. Four questions appear on pages 2, 7, 13, and 17; each answer is on the following page. Extracted text confirms no answer on the question page and no changed numerical scores before the MSE prediction reveal. No clipping, overlap, missing citations, or unexpected blank frames was observed. Footer numbers advance consistently from 1 to 19, repeating only for the four answer reveals. All 10 document pages were previewed.

HTML checks confirm all five commands and 17 anchors, along with five identical SVG copies and identical downloadable PDF copies. The prior refinement included a Chrome layout check; this finalization verified the rebuilt HTML structurally rather than repeating a browser interaction test.

The original baseline had a 6-page document and 22-page slide PDF; the intermediate refinement had 10 and 21 pages. Finalization adds two short command frames, retaining the 15-minute schedule. Temporary inspection PNGs are outside the repository, with none in `output/`. See `docs/refinement-review.md` for the earlier assessment and `docs/finalization-review.md` for this finalization. The guide has not undergone a timed speaking rehearsal.

Versions: just 1.58.0, Pandoc 3.11, XeTeX 0.999991 from TeX Live 2019/Debian. The optional Fira fonts are absent, so Metropolis emits font lookup messages and uses fallback fonts. These messages do not prevent successful PDF generation.
