# RAG Eval Observatory V2 Research Report

## Abstract

This V2 upgrade turns the repository into a reproducible project-level experiment suite. The run records the dataset, device, experiment matrix, metrics, figures, failure analysis, and reproduction commands in committed small artifacts.

## Dataset

- Source path: `data/processed/rag_cases.jsonl`
- Profile: `full`
- Runtime: `48.477` seconds
- Device: `cuda` / `NVIDIA GeForce RTX 5090 Laptop GPU`

## Methods

Experiments declared in `configs/experiment_matrix.yaml`:

- `bm25_word_tfidf`: `tfidf_word`
- `char_tfidf_retrieval`: `tfidf_char`
- `lsa_dense_projection`: `lsa_dense`
- `hybrid_lexical_dense`: `hybrid`

## Experiments

The matrix produced `4` result rows. Best observed `recall@5`: `0.1067` from `bm25_word_tfidf`.

## Results

Key artifacts:

- `reports\results\v2_retrieval_metrics.csv`
- `reports\results\v2_retrieval_failures.json`
- `reports\figures\v2_failure_counts.png`
- `reports\figures\v2_mrr.png`
- `reports\figures\v2_recall_at_k.png`

## Ablations

Configured ablations: top_k, query_normalization, rerank_depth, answerability_split. The generated ablation files quantify threshold, perturbation, architecture, retrieval, or metric sensitivity depending on the project.

## Failure Analysis

Failure records: `80`.

Top clusters:

- `bm25_word_tfidf`: 80

## Discussion

RAG failures usually look like generation failures, but the root cause is often retrieval miss or answerability confusion. V2 separates retrieval recall from answerability-aware diagnostics.

## Limitations

- Full raw caches, model weights, and optimizer states are intentionally excluded from GitHub.
- Results are designed for reproducible portfolio research; they are not production safety, medical, or compliance guarantees.
- Some V2 experiments use compact local artifacts to keep the repository lightweight.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```
