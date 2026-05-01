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

## Deeper Analysis

`examples/run_diagnostics.py` computes average recall, average faithfulness,
per-case retrieved evidence, and failure-source distribution.

## Experiment Artifacts

- Corpus: [`datasets/corpus.json`](datasets/corpus.json)
- QA cases: [`datasets/qa_cases.json`](datasets/qa_cases.json)
- Results: [`reports/rag_eval_results.csv`](reports/rag_eval_results.csv), [`reports/rag_eval_results.json`](reports/rag_eval_results.json)
- Analysis: [`reports/retrieval_failure_analysis.md`](reports/retrieval_failure_analysis.md)

## Retrieval Engine

In addition to the simple transparent retriever, the project includes a small
BM25-style index (`rag_eval_observatory.bm25`) and a dataset evaluation pipeline.
This gives the repository a realistic retrieval baseline without external services.

## Full RAG Dataset

The repository includes a 36-document corpus and 24 QA cases:
[`datasets/full_corpus.json`](datasets/full_corpus.json),
[`datasets/full_qa_cases.json`](datasets/full_qa_cases.json), and
[`reports/full_rag_analysis.md`](reports/full_rag_analysis.md).

## Retrieval Metrics

`rag_eval_observatory.metrics` computes hit rate, MRR, and nDCG for full retrieval
runs. Use `examples/run_full_pipeline.py` to regenerate `reports/full_pipeline_results.json`.

## Real Public Dataset Experiment

        `datasets/external/rag_eval_6k_sample.jsonl` contains a real sample from
        [aizip/Rag-Eval-Dataset-6k](https://huggingface.co/datasets/aizip/Rag-Eval-Dataset-6k).
        The report in `reports/real_rag_eval_6k_analysis.md` profiles answerability, difficulty,
        context count, and lexical overlap so the observatory can analyze retrieval conditions
        before generation.

## GPU-Backed Real Experiment

This repository now includes a reproducible GPU-backed experiment using `aizip/Rag-Eval-Dataset-6k`.
The smoke path runs on the local RTX 5090 Laptop GPU through the `Transformers` conda
environment and writes metrics, figures, and a markdown report.

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

Main report: `reports/rag_gpu_retrieval_benchmark.md`.

<!-- V2_RESEARCH_UPGRADE -->
## Publishable V2 Research Upgrade

This repository now includes a project-level V2 experiment suite:

- Reproducible matrix: `configs/experiment_matrix.yaml`
- Main runner: `scripts/run_matrix.py --device cuda --profile full`
- Failure analysis: `scripts/analyze_failures.py`
- Research report: `reports/rag_eval_observatory_v2_research_report.md`
- Experiment index: `reports/results/experiment_index.json`

The V2 artifacts include multiple experiments, ablations, figures, failure cases, and a discussion section while keeping raw caches and large checkpoints out of Git.

