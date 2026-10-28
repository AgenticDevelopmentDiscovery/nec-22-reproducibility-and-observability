## What goes wrong without it
 
 Without a trace, the output is the entire evidence: one cannot
see what the agent searched for, what the search actually returned, or which
part of the returned text the model misread. 

- One can only re-run the agent on a similar-sounding question and hope to hit the same failure, which a non-deterministic model may simply not reproduce for you.
- Without a stored trace to compare against, there is no way to check whether a change made a class of failure more or less common — only an impression, formed from whichever cases happened to be
noticed. 

An agent operating without observability is a system whose only debugging signal is what a user happened to report, and whose only evidence for whether a change helped is how the team feels about it afterward.

## When to reach for it

The cost of instrumenting and pinning a run is not free, so it should scale with what is at stake.

- A single-call, stateless agent (a one-shot summarizer with no tools) has little to gain: a bad output is trivial to inspect directly. 

The case for full tracing and reproducibility strengthens sharply once:

- An agent chains multiple tool calls, once its failures are reported by users rather than caught in testing
- Its decisions carry enough weight — financial, medical, safety-relevant — that someone must be able to answer "why did it do that" after the fact. 

Between those extremes, a reasonable default is to trace first and treat pinned, replayable reproduction as something you add once a class of failure has actually shown up twice.
