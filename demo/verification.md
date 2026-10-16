# Demo verification

Verified locally with Windows Python 3.12 using the standard library. These are observed results, not simulated output.

## Automated checks

`python -m unittest discover -s demo -v`: **4 tests passed**.

- Re-execution matches, selects the zero-error winner, and preserves failed partial predictions and lineage.
- A changed target causes the first score difference at step 1: 13.8 versus 16.8.
- A stale dataset hash and attempts to overwrite a run are rejected.
- A missing step and an altered winner score are detected by comparison.

## Executed demonstration

The original, replay, and changed runs were generated under `demo/runs/`, which is ignored by Git because runs are regenerable local artifacts.

| Check | Observed |
| --- | --- |
| Original and replay | `match: true`; 5 steps compared |
| Original and changed | `match: false`; first difference at step 1 |
| Changed fields at first divergence | `inputs.dataset_hash`, `score` |
| Original winner | `c003`, MSE 0.0 |
| Changed winner | `c003`, MSE 0.2 |
| Failures in each run | One division by zero, retained in the step log |

`compare` returned 0 for matching runs and 1 for the intentional divergence. Both are expected outcomes. See `README.md` in this directory for reproduction commands.

## Rendering status

After installing the toolchain in Ubuntu-20.04 WSL, `wsl -d Ubuntu-20.04 -- just build` completed successfully and generated:

- `output/document.pdf`: 6 pages.
- `output/slides.pdf`: 22 pages, including title, section dividers, and references.
- `_site/index.html`, stylesheet, and copies of both PDFs.

Slide previews were visually inspected. The clipped three-file overview was shortened, and the configuration excerpt was tightened; both revised slides were checked after rebuilding. The document's first page was also inspected. Website generation was verified; browser interaction was not tested.

Versions: just 1.58.0, Pandoc 3.11, XeTeX 0.999991 from TeX Live 2019/Debian. The optional Fira fonts are absent, so Metropolis emits font lookup messages and uses fallback fonts. These messages do not prevent successful PDF generation.
