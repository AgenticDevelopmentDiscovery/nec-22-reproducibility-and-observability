# Content

## How it works: a trace is a tree of spans

The unit of observability is the **span**: one step of execution — an LLM
call, a tool call, a sub-agent invocation — recorded with its inputs, its
outputs, when it started and ended, and whatever metadata matters later (model
name, sampling parameters, token counts, the tool's arguments). A **trace** is
the tree those spans form for one agent run: a root span for the run as a
whole, with a child span for each step, nested to show which call happened
inside which.

![A trace for one support-agent run: a root span for the whole request, with child spans for the planning call, the doc-search tool call, and the drafting call. The tool-call span carries its own attributes — the query it sent and the raw response it got back — which is exactly the detail a final-answer-only log would discard.](figures/trace-tree.svg){#fig:trace width=85%}

This is the payoff of the tree structure: a bad final answer is one leaf of the
tree, but the tree also holds every intermediate step that led to it. Reading a
trace means walking from the root down, comparing each span's output against
what the next span used as input, until the mismatch appears.

## Reproducibility levers, and their real limits

Four things can be pinned or recorded to make a run re-creatable:

- **Model version.** Provider APIs update models behind a stable name; pin an
  exact snapshot identifier so "the same model" actually means the same model.
- **Sampling parameters.** Fix temperature and any seed the API accepts.
- **Prompt and tool versions.** Log which exact system prompt and tool
  definitions produced this run, the same way you would version application
  code.
- **Tool responses.** Record what a tool actually returned, so a re-run can
  replay that response instead of calling a live search index, API, or clock
  that may answer differently next time.

None of this guarantees bit-for-bit determinism.
Reproducibility here means enough of the run pinned that a fix 
can be tested under the *same conditions* that produced the failure 
— the same tool responses, the same prompt, a model that behaves the same
way in practice — not a guarantee of the identical output token for token.

## Using it: diagnosing a failure from a trace

A support agent searches internal docs, then drafts a reply. A user reports
that it confidently cited a refund policy that does not exist. The final
answer alone gives no way in. The trace does:

```text
span: agent run                                     4.2s
|- span: LLM call "plan"                             0.6s
|    output: {"action": "search_docs", "query": "refund"}
|- span: tool call "search_docs"                     0.5s
|    query sent:    "refund"
|    docs returned: [refund-policy-2019.md, returns-faq.md]
|    ! refund-policy-2019.md was deprecated 8 months ago
`- span: LLM call "draft reply"                      3.1s
     output: cites refund-policy-2019.md as current
```

Read top to bottom, the fault is not in the drafting call at all — the model
drafted a faithful summary of a document it was handed. The plan span's query
was too broad, the search span returned a stale document because nothing
scoped it to current policy, and the draft span had no way to know that. A
log of only the final answer would show a hallucination; the trace shows a
retrieval problem three steps upstream. That distinction is the entire reason
to look at the trace instead of the output: it tells you which span to fix —
here, the search step's query or its filtering — instead of leaving you to
suspect the model itself.

## Going further: replay as a regression test

Once a trace exists, it can do more than explain one run — the recorded tool
response turns into a fixture. Take the span attributes from the failing
trace above (the query, the stale document it returned) and replay the run
from that point with a fix applied: filter search results to current
documents before drafting. Re-running just the drafting span against the
corrected input confirms the fix without re-paying for the planning call or
depending on the live search index answering the same way twice. Stored this
way, a trace from a real failure becomes a cheap, targeted regression test —
the closest an agent gets to the deterministic unit test an ordinary function
would get for free.

## Pitfalls

**Logging what shouldn't be logged.** Spans capture raw inputs and outputs by
default, and agent inputs routinely include user messages, account details, or
API keys passed as tool arguments. A trace store is a new place secrets and
personal data can leak; redact before you record, not after.

**Instrumenting until no one reads it.** A span for every token or every retry
produces a trace too large to read during an actual incident. Instrument at
the grain a human will actually walk through — one span per LLM call and per
tool call is usually right — and add finer detail only where a real failure
has shown it is needed.

**Mistaking a clean trace for a correct one.** A trace shows what the agent
did and confirms it ran without errors; it says nothing about whether the
answer was right. The support-agent example above produced a trace with no
exceptions in it at all — every span succeeded. Whether the output was correct
is a question for evaluation, not for the trace.
