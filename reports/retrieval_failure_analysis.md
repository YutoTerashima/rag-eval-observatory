# Retrieval Failure Analysis

The evaluation uses a small but concrete corpus and six QA cases. One case has no
gold document on purpose, which tests whether the system can distinguish missing
evidence from ordinary retrieval failure.

## Results

| case_id | gold_doc | retrieved | precision | recall | faithfulness | failure_source |
| --- | --- | --- | --- | --- | --- | --- |
| Q001 | D002 | D002,D003,D005 | 0.333 | 1.0 | 1.0 | no_failure |
| Q002 | D003 | D003,D002,D005 | 0.333 | 1.0 | 1.0 | no_failure |
| Q003 | D007 | D007,D001,D008 | 0.333 | 1.0 | 1.0 | no_failure |
| Q004 | D008 | D008,D001,D007 | 0.333 | 1.0 | 1.0 | no_failure |
| Q005 | D006 | D006 | 1.0 | 1.0 | 1.0 | no_failure |
| Q006 | D999 |  | 0.0 | 0.0 | 0.0 | missing_gold |

## Aggregate

- Mean recall: 0.833
- Mean precision: 0.389
- Mean faithfulness: 0.833

## Interpretation

This report makes the failure source explicit. In real RAG systems, this distinction
determines whether to improve indexing, retrieval, reranking, answer generation, or
data coverage.
