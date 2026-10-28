# Topic

## In one sentence

Reproducibility and observability are the discipline and tooling for making an
AI agent's run re-creatable and its decision trail inspectable, so a failure can
be diagnosed after the fact instead of only guessed at.

## What it is

**Observability** means instrumenting an agent's execution — every LLM call,
every tool call, every intermediate plan or retry — so the run can be inspected
after it finishes: what was sent, what came back, how long it took, and how each
step fed the next. In practice this takes the shape of a *trace*: a tree of
timestamped *spans*, one per step, each carrying its inputs, outputs, and
metadata. **Reproducibility** is the related but separate ability to re-create a
run, or enough of one, that a fix can be tested against the same conditions that
produced the failure — by pinning the model version, fixing sampling parameters,
recording and replaying tool responses, and versioning the prompts that drove
the run. Observability tells you what happened; reproducibility lets you make it
happen again on purpose.

## Why it belongs in this course

A traditional program fails the same way every time you feed it the same input,
so a stack trace and a debugger are usually enough. An agent does not offer that
guarantee: the model samples its output, a retrieved document or search result
can differ between calls, and a multi-step plan means the visible failure is
often several steps downstream of the actual cause. A student who has only
built single-call chatbots has not yet met this problem; the moment an agent
chains three or four tool calls together, "print the output and look at it"
stops being a debugging strategy, because the wrong output does not say which
step went wrong. Without observability, a bug a user hits once is a bug you
cannot reproduce, inspect, or fix with confidence. Without reproducibility,
changing a prompt or swapping a tool is a guess you cannot check, because there
is no comparable run to check it against. Both problems are specific to
agents — they follow directly from chaining a stochastic model into a multi-step
system — not from programming in general.

## What the reader will be able to do

- Instrument an agent's LLM calls and tool calls as a trace of spans, so a run
  can be inspected after it finishes.
- Read a trace to localize the step that caused a multi-step agent's failure,
  rather than guessing from the final output alone.
- Apply the concrete levers for making an agent run reproducible — model and
  prompt versioning, fixed sampling parameters, and recording tool responses for
  replay — and state honestly which ones do and do not guarantee determinism.
- Recognize the pitfalls that make traces useless in practice: logging secrets
  or user data into them, instrumenting so heavily that no one reads the
  result, and mistaking a clean-looking trace for a correct one.

## Scope

**In scope**

- The trace/span mental model for agent execution, and how it descends from
  distributed-systems observability.
- The concrete levers for reproducibility (versioning, seeding, record-and-replay)
  and their real limits.
- A worked example of diagnosing a multi-step agent failure from a trace.
- The practical pitfalls of instrumenting agents: overhead, sensitive data, and
  false confidence from a trace that "looks fine."

**Out of scope**

- Production monitoring, alerting, and on-call infrastructure — a real concern,
  but a systems-operations topic rather than an agent-development one.
- Model *training* reproducibility (data versioning, checkpoint management) —
  a different discipline that happens before an agent is ever deployed.
- Evaluation frameworks and scoring rubrics for agent correctness — related, but
  a trace shows what happened, not whether it was right; that judgment is a
  separate topic.

## Shape

`03-content` carries the weight: the trace/span mental model, the reproducibility
levers (with their real limits stated plainly), a worked debugging example built
from a single multi-step agent failure, and the pitfalls. The worked example is
the one figure this tutorial needs — a small trace tree showing where a
malformed tool call hides behind a plausible final answer.

## Open questions

- How much of the reproducibility-levers material should name specific vendor
  tools (OpenTelemetry's GenAI conventions, a given tracing product) versus
  staying at the level of the underlying pattern, given how quickly that
  tooling is still moving.
- Whether the worked example should be a single continuous case reused across
  §§ Content, or a fresh case for the "going further" replay discussion — a
  single thread is easier to follow, but a second case exercises the pattern on
  something new.
