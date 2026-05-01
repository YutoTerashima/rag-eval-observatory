# RAG Eval Observatory

A small observability and evaluation lab for RAG systems. It separates retrieval,
answer generation, and evaluation so failures can be traced to the right layer.

## Quick Start

```bash
pip install -e ".[dev]"
python examples/run_rag_eval.py
pytest
```

## Metrics

- **Context precision:** how much retrieved context is useful
- **Context recall:** whether expected evidence was retrieved
- **Faithfulness:** whether the answer stays grounded in retrieved text
- **Failure source:** retrieval, generation, or no failure

## Example Output

```text
question=What does trace grading inspect?
precision=1.00 recall=1.00 faithfulness=1.00 source=no_failure
```

## Research Brief

See [`docs/research_brief.md`](docs/research_brief.md) for the problem framing,
metric design, limitations, and next experiments.

## Portfolio Notes

This project shows evaluation taste: failures are assigned to retrieval, generation, or grounding rather than treated as one opaque score.
