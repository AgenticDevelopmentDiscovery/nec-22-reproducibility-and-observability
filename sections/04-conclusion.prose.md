# Applications and conclusion

## Carry the evidence into a live agent {#s13}

- Save visible model requests/responses and tool inputs/outputs.
- Preserve model/settings, code, environment, and retrieved content.
- Define what “same” means **before** comparing runs.
- If exact re-execution is unavailable, evaluate repeated-run behavior.

**A seed alone is not a reproducibility guarantee.** [@pytorchrepro]

::: {.detail}
Sources of variation include sampling, changing tool outputs, retrieval over a changing corpus, scheduling, time, and runtime versions. Preserve the actual snapshots as well as their hashes. Capture the rendered prompt and retrieval order; hidden model reasoning is neither required nor generally available.

Replaying saved model responses tests downstream behavior. Calling the live model again tests a different claim. For distributional agreement, choose a metric, tolerance, and repeated-run protocol before running the experiment. One matching execution is not statistical evidence.

The offline demo is intentionally smaller than a production framework. Real systems need appropriate access controls/redaction, retention policies, start/end events for interrupted work, recovery, and explicit retry/timeout policies. These are extensions, not features claimed by the example.
:::

## Where would you use these records? {#s14}

| AI coding agents | Engineering simulations |
| --- | --- |
| Tool calls and code revisions | Input files and material properties |
| Test outcomes and failed attempts | Solver settings and model versions |
| Execution/revision history | Evaluation outcomes and run history |

**Coding:** Which edit broke the tests?

**Simulation:** Did the result change because of the physics inputs or solver settings?

::: {.detail}
A coding-agent trace can associate a tool call with a code diff, test command, and failed attempt, making an unexpected edit easier to investigate. A simulation run can connect an output artifact to the input deck, material model, mesh, solver configuration, software version, and evaluation result. Repeating a simulation also requires its relevant software and numerical environment.

These examples transfer the same recording principles; they do not imply our offline search implements a production coding or simulation platform. The course connections remain C1 (reproducible repositories), C2 (auditable fitness), C3 (retrieval context), and C4 (visible failures).

The same principles extend to robotics, medical AI, and other systems with multi-step execution, where domain-specific validation is also necessary.
:::

## Keep the evidence, not just the winner {#s15}

Before claiming reproducibility:

1. Preserve the actual inputs, configuration, and code.
2. Re-execute and compare intermediate outcomes as well as the result.
3. Keep failures and links to each artifact's origin.

**The final answer shows what was produced. The records let us investigate how, repeat the execution, and explain differences.**

::: {.detail}
Optional closing check: if two runs share the same winning equation, were the runs identical? No. Their data, intermediate scores, failures, or execution histories can differ. In our controlled example, both runs selected $x^2+1$, yet the first candidate's score and the winner's score changed.

For further reading, start with OpenTelemetry's observability primer and traces documentation, then W3C's provenance overview, and finally the PyTorch reproducibility notes for a concrete discussion of runtime limits. [@otelprimer; @oteltraces; @w3cprov; @pytorchrepro]
:::
