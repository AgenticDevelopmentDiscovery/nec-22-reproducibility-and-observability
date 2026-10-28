# Motivation

## Why it matters for agentic development

Ordinary programs are deterministic: the same input produces the same output,
so a stack trace or a debugger reliably points at the cause of a failure. 

An agent breaks that guarantee in three ways at once:

- The model *samples* its output, so asking it the same question twice can give two different answers even with nothing else changed. 
- A tool it calls — a web search, a retrieval index, another service — can return a different result on the next call regardless of what the agent does.
- The agent's real output is the product of a *chain* of such calls, so the step that actually went wrong is often several steps upstream of the one where the wrong answer became visible.

Observability and reproducibility exist to answer exactly the question a stack trace answers for ordinary code, for a system where that trick no longer works.

## What goes wrong without it

Consider an agent that answers a support question by searching internal docs,
then drafting a reply. A user reports that it confidently cited a policy that
does not exist. Without a trace, that report is the entire evidence: you cannot
see what the agent searched for, what the search actually returned, or which
part of the returned text the model misread — you can only re-run the agent on
a similar-sounding question and hope to hit the same failure, which a
non-deterministic model may simply not reproduce for you. Multiply this by
every prompt tweak or tool swap made afterward, and a second problem appears:
each change is a guess. Without a stored trace to compare against, there is no
way to check whether last week's change made this class of failure more or
less common — only an impression, formed from whichever cases happened to be
noticed. An agent operating without observability is a system whose only
debugging signal is what a user happened to report, and whose only evidence
for whether a change helped is how the team feels about it afterward.

## When to reach for it

The cost of instrumenting and pinning a run is not free — it adds logging
volume, storage, and engineering effort — so it should scale with what is at
stake. A single-call, stateless agent (a one-shot summarizer with no tools) has
little to gain: there is no chain to localize a fault within, and a bad output
is trivial to inspect directly. The case for full tracing and reproducibility
strengthens sharply once an agent chains multiple tool calls, once its
failures are reported by users rather than caught in testing, or once its
decisions carry enough weight — financial, medical, safety-relevant — that
someone must be able to answer "why did it do that" after the fact. Between
those extremes, a reasonable default is to trace first and treat pinned,
replayable reproduction as something you add once a class of failure has
actually shown up twice.
