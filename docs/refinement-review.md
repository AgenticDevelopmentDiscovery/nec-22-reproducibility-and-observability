# Tutorial 22 refinement review — 2026-10-27

## Baseline assessment, before editing

Authoritative working tree: `C:/Users/ejlyn/ENGR689/nec-22-reproducibility-and-observability/nec-22-reproducibility-and-observability`. Branch: `Elias.dev`, initially clean at `12f6151`. Local main and origin/main: `9e065f8`; no branch operations are part of this refinement.

Read the paired manuscript, topic, presenter notes, demo documentation, Python implementation/tests, references, project protocol, metadata, build recipes, website template/style, and deployment configuration. Inspected all 22 pages of the existing slide PDF as rendered previews. The existing document has 6 pages. There are 15 substantive instructional frames, one title, five section dividers, and one references frame.

This is an editorial assessment and implementation check, not a formal `/round` panel or a claimed independent multi-reviewer synthesis. Historical review records are untouched.

| Finding | Refinement decision |
| --- | --- |
| Definitions arrive before a concrete reason to care; logging is not separately defined. | Open with a short agent-output puzzle and Q1, then define all four terms. |
| Files and configuration precede the search problem. | Explain the rule-based propose/evaluate/select loop and MSE before Q2 and the records. |
| Replay contract appears in both the opening and replay slides. | Explain it once at replay; keep runtime detail in the document and notes. |
| Baseline pages 4, 16, 17, and 20 rely on long paragraphs. | Replace repeated explanations with diagrams, short bullets, and applications. |
| Pages 7, 9, 10, and 15 are visually crowded near the footer. | Reduce projected text; retain detail in the same manuscript through `.detail` blocks. |
| The early motivation gives away both changed scores. | Save numerical divergence results until after the MSE prediction question. |
| MSE is given without explaining the observations or unseen-data limitation. | Define symbolic regression, show the five data pairs and score progression, and explain what zero MSE does and does not mean. |
| Final interaction exposes its answer on the same page. | Four question/reveal overlays: two before the demo, two within it. |
| Command working directories differ between slides and notes. | Standardize all demonstration commands on the repository root and fresh `class-*` paths. |
| Lineage appears as prose, with run ancestry and span nesting introduced together. | Draw the actual candidate chain and explain the other two relationships separately. |
| Live-agent transfer lacks concrete engineering examples. | Add one concise coding/simulation applications frame. |

## Design constraints

- Preserve the existing offline Python implementation, tests, results, and previous run directories.
- Keep 15 instructional frames; four overlays add answer pages, not new topics.
- Preserve Metropolis; remove automatic section-divider pages to avoid unnecessary navigation.
- Add one small format-aware Lua filter; use native Beamer `onlyenv` overlays. The article and website keep question, answer, and detail in order.
- Keep SVG diagrams editable, use the same assets in all three outputs, and store inspection PNGs outside the repository in the temporary directory.
- Budget 15 minutes including about 80 seconds of audience response time. This is a schedule, not a claimed timed rehearsal.

## Validation and final student-perspective assessment

The final assessment below is an editorial self-review from a new student's perspective, not an independent panel review. It was performed after rendering and checking the revised outputs.

| Student question | Where the final tutorial answers it |
| --- | --- |
| What is reproducibility for? | S01–S02 separate a correct output from repeatable execution under an explicit contract. |
| Why record intermediate actions? | S05 asks what the winner omits; S06 assigns complementary roles to the three records. |
| What does observability add beyond logging? | S02 distinguishes recorded events from evidence used to investigate behavior; S10 demonstrates an investigation. |
| What is needed to replay? | S07–S08 identify the manifest, snapshotted code, inputs, configuration, and runtime constraints; replay actually reevaluates. |
| How are differences detected? | S08 compares five candidate records; S10 identifies the first changed hash and score at step 1. |
| Why can the winner stay the same? | S09–S10 distinguish a changed score from changed ranking: c003 remains best at MSE 0.2. |
| Why preserve failures? | S11 retains the exception, failed row, identifiers, and partial predictions instead of inventing a valid score. |
| How does provenance help debugging? | S12 separates candidate ancestry, run ancestry, and execution spans, using verified candidate parents. |
| Where does this apply? | S13–S14 transfer the evidence pattern to live agents, coding tools, and engineering simulations without claiming production readiness. |

The final inspection prompted two further refinements: explicit lettered bullet options and larger question prompts for projection, and wrapped article commands at normal font size. Detailed prose and full commands remain in the article/website and presenter guide rather than crowding the slides.

## Final evidence

- Four Python unit tests passed. Five individually executed CLI commands produced expected exit codes 0, 0, 0, 0, 1; the final mismatch is intentional. See `demo/verification.md`.
- `wsl -d Ubuntu-20.04 -- just build` succeeded: 10-page document, 21-page slide PDF, and local website. The baseline was 6 document pages and 22 slide pages. Both decks have 15 instructional frames; four answer overlays replace five baseline section dividers.
- All 21 final slide pages were visually inspected. Question and reveal pages are readable, diagrams and mathematics render correctly, and no clipping or overlap was observed. All article pages were previewed; command-heavy pages 5–7 received additional full-size inspection after wrapping was fixed.
- Automated extraction confirms four question pages (2, 7, 12, 15), each without its answer, followed by its reveal. Changed scores are absent before the prediction reveal. All 15 website anchors, five SVG copies, and identical downloadable PDF copies were checked. A Chrome screenshot confirmed readable local website layout; no deployment occurred.
- Hash checks confirm the Python implementation, tests, and all 12 files in the previous original/replay/changed runs are unchanged. Classroom `class-*` directories remain unused. Inspection PNGs are outside the repository; none are in `output/`.
- Workspace remains on `Elias.dev`. Local main and origin/main remain at `9e065f8b6be2cacff03a41fdbfa1696d653346f6`. No commit, push, merge, tag, or publication was performed.

## Remaining limits and rehearsal recommendation

The guide allocates exactly 15 minutes, including about 80 seconds of audience response time. This is an estimate, not a timed rehearsal. Practice file navigation and collect only one or two answers per prompt; these are the most likely sources of overruns. Use one-page PDF advancement to reveal answers, and keep the notes open for commands. Optional Fira fonts are unavailable; the successful build uses readable fallback fonts. The offline replay guarantees apply to this recorded comparison contract, not arbitrary live-model or external-service behavior.
