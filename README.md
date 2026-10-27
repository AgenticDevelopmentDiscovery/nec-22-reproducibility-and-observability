# Tutorial 22 — Reproducibility, Logging & Observability for Agent Runs

A 15-minute ENGR 689 tutorial with a runnable offline symbolic-regression agent. Capture a manifest, replay candidate evaluations, locate an input-induced divergence, and preserve failed candidates and equation ancestry.

## Read or present

- [Topic and learning objectives](topic.md)
- [Context](sections/01-context.prose.md)
- [Workflow, MSE, and experiment records](sections/02-motivation.prose.md)
- [Worked example](sections/03-content.prose.md)
- [Conclusion and further reading](sections/04-conclusion.prose.md)
- [15-minute presenter notes](presenter-notes.md)
- [Demo commands and expected results](demo/README.md)
- [Observed verification results](demo/verification.md)
- [Refinement assessment and teaching decisions](docs/refinement-review.md)
- [Final command-slide review](docs/finalization-review.md)

Each section's `.concepts.md` companion records claims, decisions, and open questions. The prose is shared by the document, presentation, and website; each `##` heading becomes a slide. Bibliography entries live in `references.bib`.

The revised lesson has four **ASK THE CLASS** moments: correct answers (S01), missing evidence (S05), changed MSE (S09), and failed candidates (S11). In the slide PDF, advance one page to reveal each answer. The document and website include both the question and solution, plus detailed explanations.

## Run the demo

Python 3.10 or later, standard library only. From the repository root:

```sh
python demo/run.py run --out demo/runs/class-original
```

Then execute the remaining four commands **individually** from [demo/README.md](demo/README.md) or the [presenter guide](presenter-notes.md). All commands use the repository root as their working directory.

The first comparison matches all five candidate steps. The second detects the intentional change at step 1 and returns exit code 1. Each run keeps the failed `1 / x` candidate and its partial predictions.

Use fresh output directories when repeating the demo. For Windows interpreter paths and the precise replay contract, see [demo/README.md](demo/README.md).

```sh
python -m unittest discover -s demo -v
```

## Build the three outputs

The build uses `just`, Pandoc, XeLaTeX, and a POSIX shell. These are now installed in this computer's **Ubuntu-20.04 WSL environment**. From a PowerShell terminal in this repository, rebuild with:

```powershell
wsl -d Ubuntu-20.04 -- just build
```

Open `output/document.pdf` or `output/slides.pdf` in Windows Explorer after building. The tools are installed inside WSL; typing `just` directly in PowerShell will not invoke them. The Python demo remains independent of the document toolchain.

For installation on another computer, follow the platform instructions below.

On macOS:

```sh
brew install pandoc just librsvg
brew install --cask mactex-no-gui
```

On Debian/Ubuntu, install [just](https://just.systems/man/en/pre-built-binaries.html) and a current [Pandoc](https://pandoc.org/installing.html) release. Ubuntu 20.04's Pandoc package is too old for this build's `--citeproc` option. Install the TeX dependencies with:

```sh
sudo apt-get install -y texlive-xetex texlive-latex-extra \
  texlive-fonts-recommended lmodern librsvg2-bin
```

The slide metadata uses the Metropolis Beamer theme. Confirm it is installed with the TeX packages.

| Command | Output |
| --- | --- |
| `just doc` | `output/document.pdf` |
| `just slides` | `output/slides.pdf` |
| `just site` | `_site/index.html`, with both PDFs linked |
| `just build` | All three |
| `just serve` | Website preview at localhost:8000 |

The revised deck has **17 instructional frames**, including two short command frames, with four additional answer-reveal pages. All five live commands are visible: original execution on S07, replay/comparison on S08, and controlled change/comparison on S10. The result diagrams follow on S08-results and S10-results. It omits standalone section-divider pages while retaining the Metropolis theme. See [verification](demo/verification.md) for the final PDF page counts and inspection results. Inspect the slides again after future edits; the build itself does not reject overfull frames.

Installed versions: `just 1.58.0`, `pandoc 3.11`, and XeLaTeX from TeX Live 2019 (Ubuntu 20.04). The Metropolis theme currently uses fallback fonts because its optional Fira fonts are absent; the PDFs render successfully.

## Review and publishing

### Editing the shared manuscript

Keep the existing `##` heading-to-slide structure. The source IDs `s01`–`s15`, `s08-results`, and `s10-results` match the presenter guide. `filters/tutorial.lua` provides three small output differences:

- `.question` and `.answer` divisions occupy overlays 1 and 2 in Beamer. The article and website retain both in order.
- `.detail` divisions provide supplementary explanations and calculations in the article and website, and are omitted from the slides. The five demo commands stay outside these divisions.
- PowerShell command blocks wrap in the article using `fvextra`, so long paths remain readable without reducing the font size. Longer slide commands use PowerShell continuation lines; the presenter guide also keeps one-line copies.

The `.prompt` division enlarges and bolds a projected question. Add or revise content in the paired source files, not the generated PDFs or `_site/`. Five editable SVG diagrams live in `figures/`. Inspection PNGs are stored outside the repository in the temporary directory.

[CLAUDE.md](CLAUDE.md) describes the document's critique process. A review round produces a docket in `rounds/`; editing follows separately. Past rounds are preserved. No review round has been run for this draft.

Website publishing is a separate explicit action. The existing GitHub Pages workflow builds the committed version on demand through `just deploy`; it is not automatically triggered by a push. Tutorial source changes are maintained on `Elias.dev`; pushing that branch does not merge into `main` or deploy the site. Generated PDFs, website files, and demonstration runs are ignored and rebuilt locally.

## Framework origin

The repository uses the nel-course document template, derived from nel-operator: one manuscript with paired prose/concept files, an independent reviewer panel, and accumulated critique history.
