# Conclusion

## Before you call a result reproducible

You can now capture an experiment, re-execute it, compare candidate outcomes, find an input-induced divergence, and retain failures alongside successful equations.

For the next agent run, check:

- Are the actual inputs and code available, as well as their hashes?
- Is “same result” defined, and does the comparison enforce it?
- Can every attempted candidate and the winning artifact be traced?

**Exit question:** The winner is unchanged, but an early candidate's score differs. Is replay successful? **No under our contract:** the ordered evaluation outcomes must also match.

## Extend one boundary at a time

Start with OpenTelemetry's traces documentation to map local operations into nested spans. [@oteltraces] Then use the W3C provenance overview to distinguish artifacts, producing activities, and responsible agents. [@w3cprov]

Read PyTorch's reproducibility notes for a concrete account of runtime and platform limits, even if your eventual agent uses another backend. [@pytorchrepro]

The next experiment is replacing the offline proposer with your course agent while keeping the manifest and comparison contract. Whether that system supports exact re-execution, recorded-response replay, or only distributional agreement remains an empirical question.
