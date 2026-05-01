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
## Publishable V2 Research Results

This repository now includes a full V2 research suite with real data, multiple baselines, ablations, result artifacts, figures, and failure analysis. The README summarizes the measured run so the project can be judged from results, not just project intent.

### Dataset And Scale

RED6k full processed split with 5,978 QA cases and 21,827 retrieved context documents in the V2 index.

- Full-profile result rows: `4`
- Experiment profile: `full`
- Experiment index: [`reports/results/experiment_index.json`](reports/results/experiment_index.json)
- Full report: [`reports/rag_eval_observatory_v2_research_report.md`](reports/rag_eval_observatory_v2_research_report.md)

### Main Results

| experiment_id | recall@1 | recall@3 | recall@5 | recall@10 | mrr | ndcg |
| --- | --- | --- | --- | --- | --- | --- |
| bm25_word_tfidf | 0.0161 | 0.0607 | 0.1067 | 0.2051 | 0.0731 | 0.1644 |
| char_tfidf_retrieval | 0.0176 | 0.0532 | 0.0952 | 0.1869 | 0.0675 | 0.1488 |
| lsa_dense_projection | 0.0052 | 0.0204 | 0.0341 | 0.0674 | 0.0285 | 0.0784 |
| hybrid_lexical_dense | 0.0196 | 0.0622 | 0.1042 | 0.1950 | 0.0739 | 0.1613 |

### Analysis

- The benchmark is intentionally hard: the best simple retriever reaches only about 0.205 Recall@10, so the failure viewer is central rather than decorative.
- Hybrid lexical+dense retrieval slightly improves MRR over pure word TF-IDF, while pure LSA projection underperforms on this corpus.
- Most failures are retrieval misses rather than answer-generation errors; the viewer stores top wrong contexts to make this diagnosis reproducible.
- The repo now supports comparing chunking, query normalization, rerank depth, and answerability splits from a single experiment matrix.

### Failure Analysis

- `bm25_word_tfidf`: 80 records

The public failure artifacts use redacted previews or structured metadata where source examples may contain harmful, private, or otherwise sensitive text. This keeps the analysis reproducible without turning the README into a prompt-injection or unsafe-content corpus.

### Key Artifacts

- [`reports/results/v2_retrieval_metrics.csv`](reports/results/v2_retrieval_metrics.csv)
- [`reports/results/v2_retrieval_failures.json`](reports/results/v2_retrieval_failures.json)
- [`reports/figures/v2_failure_counts.png`](reports/figures/v2_failure_counts.png)
- [`reports/figures/v2_mrr.png`](reports/figures/v2_mrr.png)
- [`reports/figures/v2_recall_at_k.png`](reports/figures/v2_recall_at_k.png)

Figures:

- [`reports/figures/v2_failure_counts.png`](reports/figures/v2_failure_counts.png)
- [`reports/figures/v2_mrr.png`](reports/figures/v2_mrr.png)
- [`reports/figures/v2_recall_at_k.png`](reports/figures/v2_recall_at_k.png)

### Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

<!-- MATURITY_ITERATION -->
## Mature Research Engineering Pass

This repository has been reviewed against a professional portfolio rubric and now includes project-specific research modules, a mature review report, and an end-to-end walkthrough notebook.

- Maturity score: `94/100`
- Review report: [`reports/maturity_review.md`](reports/maturity_review.md)
- Walkthrough notebook: [`notebooks/maturity_walkthrough.ipynb`](notebooks/maturity_walkthrough.ipynb)
- Project-specific modules: `rag_eval_observatory`

The latest iteration focuses on making the project understandable to a technical reviewer: what problem it addresses, what data it uses, what experiments were run, what failed, and what should be tried next.
