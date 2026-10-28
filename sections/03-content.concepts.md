# Demonstration — spine

## Claims

- Replay recomputes candidates and scores under validated inputs/code/runtime.
- All five semantic records must match, including failed attempts.
- Replacing one existing target raises the same winner's MSE to 0.2.
- The first divergence is step 1: dataset hash and MSE 13.8 versus 16.8.
- Failed c004 retains partial predictions, exception, failed row, and identifiers.
- Candidate ancestry, run ancestry, and span nesting are distinct relationships.

## Decisions

- Preserve demo/run.py and its unit tests without changes.
- Run all classroom commands individually from the repository root using fresh class-* directories.
- Verify separately under verification-* paths so classroom names remain available.
- Q3 precedes modification; its answer explains 1/5 without revealing the first-divergence result early.
- Q4 precedes failure inspection; show the actual c004 record after discussion.
- Use comparison/lineage SVGs instead of long paragraphs.
- Verify c001 -> c002 -> c003 against records; mention losing c005 and independent c004.
- Display all five commands in the deck; split S08 and S10 into command/result frames without changing the lesson's time budget.
- Use executable PowerShell continuations at argument boundaries; keep one-line copies in presenter notes.
- Retain detailed calculations and schema explanations in .detail blocks.
- Distinguish four CLI operations from the internal loop; compare is used twice and reads recorded outcomes.
- Define divergence and lineage in place; distinguish first difference from cause and equation parentage from span nesting.

## Open questions

- Further content edits require renewed overlay and slide-fit inspection.
- Production crash recovery and timeout policy remain separate implementations.

## Not doing

- Replacing or deleting old runs; retries/timeouts; live LLM calls; a production tracing backend.
