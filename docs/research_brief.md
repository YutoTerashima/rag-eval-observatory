# Research Brief

## Problem

RAG failures are often collapsed into one vague label: "the answer was wrong." That is
not actionable. The system needs to say whether retrieval, grounding, or generation
failed.

## Method

The observatory separates:

- retrieval quality via context recall and context precision
- answer grounding via faithfulness
- failure assignment via a simple failure-source label

## What the Mock Demo Proves

The evidence path is inspectable end to end. Each answer can be traced to the retrieved
document that supported it.

## Limitations

- Lexical retrieval is used for transparency.
- Faithfulness is exact and deterministic.
- The corpus is intentionally tiny.

## Next Experiments

- Add embedding retrieval.
- Add reranker diagnostics.
- Add model-judged faithfulness with human spot checks.
