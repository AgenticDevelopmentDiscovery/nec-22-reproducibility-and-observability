# figures/

Drop figures here and reference them from a `.prose.md` section:

```markdown
![A caption that teaches on its own.](figures/my-figure.svg){#fig:mine width=70%}
```

Paths are written **relative to the repository root**, not to the section file —
that is where pandoc runs from.

## Format

**Prefer SVG or PDF.** Both are vector, so they stay sharp in the document, on a
projector, and on a high-DPI screen. Use PNG for screenshots and photographs,
nothing else.

> **SVG in the PDF outputs needs `rsvg-convert`.** The website uses SVG directly,
> but pandoc has to convert it to PDF for LaTeX. If `just doc` fails with
> *"check that rsvg-convert is in path"*, install it:
> `brew install librsvg` (macOS) or `apt-get install librsvg2-bin` (Debian).
> CI already has it. A PDF figure needs no converter at all, but will not display
> on the website — so SVG plus librsvg is usually the better trade.

## What the panel looks for

The `visual` reviewer does not count figures. It asks whether each one makes a
relationship visible that the prose leaves abstract, and it will tell you to
delete any figure that merely decorates.

## Tutorial figures

The five editable SVG assets use a restrained teal/gray palette and large labels. They are embedded from the shared manuscript and copied into the website; each includes an accessible title and description.

| Asset | Teaching purpose |
| --- | --- |
| `agent-workflow.svg` | Save inputs/source before search; propose, evaluate, score, keep best, log, and repeat; finalize result/status afterward |
| `experiment-records.svg` | Three complementary records associated with one run, not file execution stages |
| `replay-comparison.svg` | All five recomputed candidate outcomes, including the matching failure |
| `controlled-divergence.svg` | One changed target, first score divergence, same winning equation |
| `equation-lineage.svg` | Verified parent-to-child chain, with notes about the other two attempts |

The numbers and ancestry correspond to seed 7 in the unchanged Python demo. If the experiment changes, verify these labels against actual records before editing them. Temporary PDF inspection PNGs belong outside the repository; they are not tutorial assets.
