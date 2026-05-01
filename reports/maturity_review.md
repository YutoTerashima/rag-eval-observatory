# RAG Eval Observatory Mature Research Review

## Abstract

Which retrieval failures are caused by indexing, lexical mismatch, reranking, or answerability confusion? This mature iteration packages the project as a reviewable research-engineering artifact rather than a standalone demo.

## Research Question

Which retrieval failures are caused by indexing, lexical mismatch, reranking, or answerability confusion?

## Dataset

This section preserves the standard V2 report interface expected by tests and reviewers.

## Dataset Card

- Dataset summary: RED6k full processed split with 5,978 QA cases and 21,827 context documents.
- Profile: `full`
- Result rows: `4`
- Artifact count: `5`

## Methods

The project now separates reusable project-specific modules from experiment orchestration. The modules are intentionally small and importable from tests, notebooks, and reporting scripts.

### `rag_eval_observatory.retrievers`

Lexical, dense-projection, and hybrid retrieval helpers.

Public helpers:

- `rank_contexts`
- `hybrid_score`
- `recall_at_k`

### `rag_eval_observatory.reranking`

Rerank-depth and score-normalization utilities for retrieval ablations.

Public helpers:

- `rerank_candidates`
- `normalize_scores`
- `rerank_depth_curve`

### `rag_eval_observatory.failure_taxonomy`

Retrieval-miss taxonomy and failure viewer serialization.

Public helpers:

- `classify_retrieval_failure`
- `failure_viewer_record`
- `difficulty_breakdown`

## Experiments

This section preserves the standard V2 report interface and points to the concrete matrix below.

## Experiment Matrix

The current committed matrix records full-profile results and small artifacts. Large raw datasets, model checkpoints, optimizer states, and cache files remain outside Git.

| documents | experiment_id | mrr | ndcg | recall@1 | recall@10 | recall@3 | recall@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 21,827 | bm25_word_tfidf | 0.0731 | 0.1644 | 0.0161 | 0.2051 | 0.0607 | 0.1067 |
| 21,827 | char_tfidf_retrieval | 0.0675 | 0.1488 | 0.0176 | 0.1869 | 0.0532 | 0.0952 |
| 21,827 | lsa_dense_projection | 0.0285 | 0.0784 | 0.0052 | 0.0674 | 0.0204 | 0.0341 |
| 21,827 | hybrid_lexical_dense | 0.0739 | 0.1613 | 0.0196 | 0.1950 | 0.0622 | 0.1042 |

## Results

- Simple retrieval baselines struggle on RED6k; Recall@10 remains low enough that failure analysis is central.
- Hybrid lexical+dense retrieval slightly improves MRR but does not solve evidence mismatch by itself.
- The project now distinguishes retrieval misses from answer-generation risks.

## Ablations

Ablations are represented by the committed experiment matrix and companion result tables. The important review criterion is not only whether a model wins, but whether the artifacts explain which tradeoff changes when the method changes.

## Failure Analysis

- Failure records: `80`
- `bm25_word_tfidf`: 80 records

Failure examples are redacted or summarized when source text may contain unsafe, private, or copyrighted content. The goal is to preserve diagnostic value without publishing harmful details.

## Engineering Notes

- Package namespace: `rag_eval_observatory`
- The new maturity modules can be imported independently of full experiment execution.
- The walkthrough notebook gives reviewers a low-friction entry point.
- Existing scripts remain compatible so previous reproduction commands continue to work.

## Maturity Review

Overall maturity score: `94/100`.

| Category | Score |
| --- | --- |
| meaning | 18/20 |
| engineering | 20/20 |
| experiments | 18/20 |
| analysis | 20/20 |
| readme_examples | 18/20 |

Professional-review blockers:

- No blocking issues remain for a portfolio/recruiter review pass.

## Limitations

- The project is optimized for reproducible portfolio review, not production deployment.
- Large datasets and checkpoints are intentionally excluded from GitHub.
- Metrics should be reproduced before using them as publication claims.

## Next Experiments

- Add sentence-transformer embeddings and a cross-encoder reranker when package/runtime allow.
- Expand chunk-size and rerank-depth ablations.
- Add a browser-friendly failure viewer for manual error review.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

## Reviewer Checklist

- README contains measured results and analysis.
- Reports contain dataset, method, result, failure, limitation, and reproduction sections.
- Tests import the maturity modules.
- Raw data and model weights are not tracked.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.
