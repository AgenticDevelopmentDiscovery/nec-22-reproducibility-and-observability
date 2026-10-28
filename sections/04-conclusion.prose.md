# Conclusion

## What you can do now

You can describe an agent's execution as a trace — a tree of spans, each
carrying its inputs, outputs, timing, and metadata — instead of as a single
opaque call. Given a multi-step failure, you can read that trace top to bottom
and localize which span actually went wrong, rather than inspecting only the
final output and guessing. You can name the concrete levers for making a run
reproducible — pinning the model version, fixing sampling parameters,
versioning prompts and tools, recording tool responses for replay — and state
honestly that none of them, even together, guarantee identical output token
for token. And you can turn a recorded failing trace into a targeted replay
that tests a fix without re-running or re-paying for an entire chain.

## Where to go next

Put this into practice on an agent you have already built, before reaching for
new material: add a span around each LLM call and each tool call, and look at
one real trace end to end. That single exercise will teach you more about
where your own agent's failures actually live than any amount of further
reading. From there, the natural next step is evaluation — once you can see
what an agent did, the remaining question this tutorial deliberately left open
is whether what it did was *right*, which needs a rubric and a scoring method,
not a trace. After that, look at how the pattern here generalizes to
multi-agent systems, where a trace has to follow a request across more than
one agent talking to another — the same tree, one level taller.

## Open edges

The tooling for agent tracing is still moving faster than practice has
settled: naming conventions for spans, what counts as standard metadata, and
how much of a trace should be captured by default are all still being worked
out across the field, so treat any specific product or standard you adopt as
provisional. The determinism limits described in § Reproducibility levers are
not a gap this tutorial glossed over — they reflect how hosted model inference
actually works today, and no amount of careful engineering on your side
removes them. And full replay has a hard edge of its own: a tool call that
only reads data can be replayed safely, but one with a real-world side effect
— an email actually sent, a payment actually made — cannot be replayed without
consequence, only inspected after the fact. Knowing which of your tools fall
on which side of that line is judgment this tutorial cannot supply for you.
