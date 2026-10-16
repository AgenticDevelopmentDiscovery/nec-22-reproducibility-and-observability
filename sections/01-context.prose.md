# Context

## Three questions about one agent run

An agent proposes an equation, calls a scoring tool, and uses the score to choose its next proposal.

| Question | Evidence |
| --- | --- |
| Can we repeat the result? | **Reproducibility:** preserved inputs and a stated comparison rule. |
| What actually happened? | **Observability:** recorded operations, outputs, and failures. |
| Where did the result come from? | **Provenance:** links to data, configuration, and parent candidates. |

Provenance describes how an artifact was produced; it does not prove that the artifact is correct. [@w3cprov]

## State what “same” means

For this tutorial, replay means **re-executing** the saved offline agent on the saved dataset and configuration. We compare candidate order, equations, predictions, scores, errors, and the selected result. New run IDs, timestamps, and durations are expected.

Replaying recorded model responses tests downstream behavior. Calling a live model again tests a different claim. A seed alone does not establish repeatability across software versions or platforms. [@pytorchrepro]

Our demo uses a small rule-based agent with no API calls. It isolates the recording and debugging method.
