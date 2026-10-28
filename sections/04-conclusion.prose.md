# Applications and conclusion

## Reproducibility levers, and their limits {#s13}

- **Model:** record the exact version and sampling settings.
- **Prompt and tools:** version the instructions, code, and definitions.
- **External evidence:** preserve actual tool responses and retrieved content.
- **Comparison:** define equivalence before testing a repeated run.

**A seed alone is not a reproducibility guarantee.** [@pytorchrepro]

::: {.detail}
Sources of variation include sampling, changing tool outputs, retrieval over a changing corpus, scheduling, time, and runtime versions. Preserve the actual snapshots as well as their hashes. Capture the rendered prompt and retrieval order; hidden model reasoning is neither required nor generally available.

The four levers are model version, sampling parameters, prompt/tool versions, and recorded tool responses. A stable model alias need not identify an unchanged implementation; use an exact version where the provider supports it. Record temperature and any accepted seed, without treating either as a promise of identical tokens. Version the system prompt and tool definitions alongside application code. A recorded tool response prevents a changed search index, service, or clock from silently changing the conditions of a downstream test. These controls improve comparability; they do not guarantee bit-for-bit determinism across every runtime or service.

Replaying saved model responses tests downstream behavior. Calling the live model again tests a different claim. For distributional agreement, choose a metric, tolerance, and repeated-run protocol before running the experiment. One matching execution is not statistical evidence.

The offline demo is intentionally smaller than a production framework. Real systems need appropriate access controls/redaction, retention policies, start/end events for interrupted work, recovery, and explicit retry/timeout policies. These are extensions, not features claimed by the example.
:::

## Three pitfalls of instrumentation {#s-pitfalls}

- **Sensitive data:** redact secrets and unnecessary personal data before storage.
- **Too much instrumentation:** record meaningful operations; add detail where needed.
- **False confidence:** successful execution or replay does not establish a correct answer.

Scale tracing depth, access controls, and retention to the investigation.

::: {.detail}
These pitfalls apply to both the trace store and the surrounding workflow. Raw messages, account details, or tool arguments may contain sensitive information. Instrumentation does not have to capture everything: select useful fields, redact before recording, control who can read the records, and retain only what is needed. Redaction also changes what can be replayed, so document that limitation.

A trace with a span for every tiny operation can become expensive and hard to investigate. Begin at meaningful model/tool/evaluation boundaries, preserve errors and relevant inputs, and add finer detail when it resolves a concrete uncertainty. Even simple workflows can benefit from versioned inputs and evaluated outputs; full tracing is a proportional design choice.

A span marked successful says that its operation completed under the recorded status rules. It does not prove that the content it produced is correct. A wrong support reply may have no exceptions at all, while our useful completed search intentionally records a failed candidate. Matching replay proves agreement under its contract, not scientific validity or physical correctness.
:::

## Where would you use these records? {#s14}

| AI coding agents | Engineering simulations |
| --- | --- |
| Tool calls and code revisions | Input files and material properties |
| Test outcomes and failed attempts | Boundary conditions; solver settings |
| Execution/revision history | Software versions and outputs |

**Coding:** Which edit broke the tests?

**Simulation:** Did the result change because of the physics inputs or solver settings?

Reproducibility supports **verification and validation**; it does not establish correctness by itself.

::: {.detail}
A coding-agent trace can associate a tool call with a code diff, test command, and failed attempt, making an unexpected edit easier to investigate. A simulation run can connect an output artifact to the input deck, material model, boundary conditions, mesh, solver configuration, software version, and evaluation result. Repeating a simulation also requires its relevant software and numerical environment. Verification asks whether the implementation solves the intended equations correctly; validation asks whether the model adequately represents the physical system for its intended use. Reproducible evidence supports those checks but cannot replace them.

These examples transfer the same recording principles; they do not imply our offline search implements a production coding or simulation platform. The course connections remain C1 (reproducible repositories), C2 (auditable fitness), C3 (retrieval context), and C4 (visible failures).

The same principles extend to robotics, medical AI, and other systems with multi-step execution, where domain-specific validation is also necessary.
:::

## Keep the evidence, not just the winner {#s15}

Before claiming reproducibility:

1. Preserve inputs, configuration, and source code.
2. Record intermediate evaluations, failures, and results.
3. Replay and compare the recorded behavior.
4. Use the evidence to investigate unexpected differences.

**The final answer shows what was produced. The records let us investigate how, repeat the execution, and explain differences.**

A consistent run can still be wrong. **Verify the result.**

::: {.detail}
Optional closing check: if two runs share the same winning equation, were the runs identical? No. Their data, intermediate scores, failures, or execution histories can differ. In our controlled example, both runs selected $x^2+1$, yet the first candidate's score and the winner's score changed.

For further reading, start with OpenTelemetry's observability primer and traces documentation, then W3C's provenance overview, and finally the PyTorch reproducibility notes for a concrete discussion of runtime limits. [@otelprimer; @oteltraces; @w3cprov; @pytorchrepro]
:::
