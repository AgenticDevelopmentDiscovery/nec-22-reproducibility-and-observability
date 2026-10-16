# Motivation

## A winning equation is not enough evidence

Suppose yesterday's winner was $x^2+1$ with mean squared error zero. Today its score is $0.2$. Did the agent change, the scoring tool change, or one target value change?

A final score cannot distinguish those explanations. The saved dataset and per-candidate trace can: our demo changes one target from 5 to 6, and the first candidate's score changes from 13.8 to 16.8.

For the course, these records connect reproducible repositories (C1), auditable fitness scores (C2), recorded retrieval context (C3), and visible failures (C4).

## Find the moving inputs

| Source of variation | Preserve or control |
| --- | --- |
| Model sampling | Model version, decoding settings, seed if supported, request and response |
| Tools and retrieval | Arguments, results, retrieved content and order, corpus snapshot |
| Code and data | Code snapshot/commit, dependencies, dataset, hashes |
| Concurrency and time | Ordering, environment, deadlines, time-dependent inputs |

The demo removes external services and executes serially. Real runs need records at every boundary that can change. A hash detects changed content; it cannot recover missing content.
