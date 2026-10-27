# Tutorial 22 command-slide finalization — 2026-10-27

## Starting point and scope

The authoritative repository is `AgenticDevelopmentDiscovery/nec-22-reproducibility-and-observability`, on `Elias.dev` at `12f61513e28299329652f09442a87a23f810f8bb`. Local main, origin/main, and the live remote main were `9e065f8b6be2cacff03a41fdbfa1696d653346f6`. The preexisting uncommitted manuscript, concepts, diagrams, filter, notes, and build refinements belong to this tutorial task and are included. No unrelated modifications were found. A patch, untracked source copies, PDF snapshots, and prior-run hash inventory were saved outside the repository before editing.

Read the current manuscript/concept pairs, proposal, notes, demo implementation/tests/documentation, bibliography, framework instructions, build configuration, and site templates. Visually inspected all 21 current slide pages before editing. Confirmed the highest-priority issue: only command 1 was projected; commands 2–5 were inside `.detail` blocks excluded from Beamer.

This is an implementation and visual self-review, not a formal `/round` or independent reviewer panel. Existing review history and the earlier `refinement-review.md` remain intact.

## Changes and navigation

| PDF page | Stable ID | Action or evidence |
| --- | --- | --- |
| 10 | S07 | Command 1: original execution; explicit manifest/step/result filenames |
| 11 | S08 | Commands 2 and 3: replay, then compare; executable PowerShell continuations |
| 12 | S08-results | Five matching outcomes, comparison contract, expected exit code 0 |
| 13–14 | S09 | MSE prediction and separate calculation reveal |
| 15 | S10 | Commands 4 and 5: replace one target, then compare |
| 16 | S10-results | First divergence; unchanged winner; expected mismatch exit code 1 |
| 17–18 | S11 | Failed-candidate question, reveal, then actual log inspection |

Q1 remains on pages 2–3 and Q2 on pages 7–8, both before the demo. All four question/answer pairs are preserved. The deck grows from 21 to 23 PDF pages: 17 instructional frames, title, references, and four additional answer pages. Commands and result diagrams now have separate frames at the existing font size. All five diagrams, mathematical results, and the Metropolis theme are retained.

Presenter notes have matching page/ID navigation, explicit slide/terminal transitions for every command, one-line copies, expected results, and the same 15-minute budget. Optional removal of the three disposable classroom directories is documented with a warning and fresh-name alternative; no cleanup was executed. README/topic/concepts describe the revised single-source arrangement.

## Observed validation

- Four existing Python tests passed on Windows Python 3.12.10. No implementation or test changes.
- Five individually executed commands in fresh `finalize-20261027-144035-*` directories returned 0, 0, 0, 0, 1. PowerShell continuation syntax executed successfully.
- Replay matched all five records. Controlled change first diverged at step 1, MSE 13.8 → 16.8. Winner c003 remained at changed MSE 0.2 with five observations. Partial failure output and all five parent-candidate links were checked against the generated logs.
- `wsl -d Ubuntu-20.04 -- just build` completed successfully: 10-page document, 23-page slides, and local website.
- Visually inspected all 23 slide pages and all 10 document pages; command pages also inspected at full size. No unresolved clipping, overlap, blank frames, unreadable commands, incorrect math, or missing citations was observed.
- PDF text checks found all five exact commands after normalizing continuation formatting, four hidden answers followed by reveals, no premature changed scores, and consistent frame numbering. HTML contains all five commands and 17 anchors; the website's PDFs and five SVGs match their source artifacts.
- All 24 preexisting experiment files retain their hashes. Classroom paths remain unused. No output PNGs or temporary artifacts belong in the commit; generated PDFs/site/runs follow the existing ignore rules.

The estimated duration remains 15 minutes, including roughly 80 seconds for responses. No timed speaking rehearsal was performed. File navigation and extended discussion remain the pacing risks. Optional Fira fonts are absent, so the successful build uses readable fallback fonts. WSL also prints its preexisting configuration warning; it did not block the build.

## Release scope

The user authorized committing and pushing the validated source changes to `origin/Elias.dev`. The commit includes the prior refinements and this command-slide fix, plus all source dependencies needed to rebuild. It excludes ignored generated outputs and practice evidence. No merge, pull request, tag, or website deployment is part of this task. The existing Pages workflow is manual-only and is not triggered by this branch push.
