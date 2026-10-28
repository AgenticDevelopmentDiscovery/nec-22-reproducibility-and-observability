# Context

## Observability

**Observability** is instrumenting an agent's execution so that after a run
finishes, one can see what it actually did.

- Every call to a language model, every call to a tool, every intermediate plan, retry, or sub-agent hand-off, each timestamped and carrying its inputs, outputs, and metadata. 

In practice this record takes the shape of a *trace* — a tree of *spans*, one per step, nested to show which call happened inside which. 

Observability answers "what happened here?" after the fact.

## Reproducibility
**Reproducibility** is the
 ability to re-create a run, or enough of one, that a fix
can be tested against the same conditions that produced a failure

- Pinning the model version, fixing the sampling parameters, recording tool responses so they can be replayed instead of called live again, and versioning the prompts that
drove the run.

Reproducibility answers "can I make that happen again on purpose?" so a
proposed fix can be checked rather than guessed at.

## Where it came from

Both ideas are older than agents. Observability is borrowed directly from
distributed systems: once an application became a graph of services calling
each other over a network, a single log file was no longer enough to explain a
failure, and engineers built traces that follow one request across every
service it touched. Reproducibility echoes a concern from computational
science, where a result is only as trustworthy as the pipeline's ability to
produce it again from the same inputs. AI agents inherited both problems at
once, and made them harder: an agent's "services" are calls to a model that
*samples* its output rather than computing it deterministically, its "network"
includes tools whose results can change between calls, and a wrong final
answer is frequently the visible symptom of a wrong decision several steps
upstream — exactly the situation distributed tracing was built to untangle.

## What this tutorial covers

This tutorial builds the mental model of a trace as a tree of spans, then walks
through the concrete levers for making an agent run reproducible and their real
limits, then works a single example: diagnosing a multi-step agent's failure
from its trace instead of from its final output alone. It closes with the
pitfalls that make instrumentation backfire — logging sensitive data into a
trace, instrumenting so heavily that no one reads the result, and mistaking a
trace that looks clean for a trace that is correct.

It does not cover production monitoring and alerting infrastructure, model
*training* reproducibility, or how to score whether an agent's output was
actually right — that last question needs an evaluation framework, and a trace
only tells you what the agent did, not whether it should have.
