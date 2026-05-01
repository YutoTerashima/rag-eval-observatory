from __future__ import annotations

"""Report metadata for the mature portfolio iteration."""

PROJECT_TITLE = 'RAG Eval Observatory'
RESEARCH_PROBLEM = 'Which retrieval failures are caused by indexing, lexical mismatch, reranking, or answerability confusion?'
DATASET_SUMMARY = 'RED6k full processed split with 5,978 QA cases and 21,827 context documents.'
TAKEAWAYS = ['Simple retrieval baselines struggle on RED6k; Recall@10 remains low enough that failure analysis is central.', 'Hybrid lexical+dense retrieval slightly improves MRR but does not solve evidence mismatch by itself.', 'The project now distinguishes retrieval misses from answer-generation risks.']
NEXT_EXPERIMENTS = ['Add sentence-transformer embeddings and a cross-encoder reranker when package/runtime allow.', 'Expand chunk-size and rerank-depth ablations.', 'Add a browser-friendly failure viewer for manual error review.']


def report_outline() -> list[str]:
    return [
        "Abstract",
        "Research question",
        "Dataset card",
        "Methods",
        "Experiment matrix",
        "Results",
        "Ablations",
        "Failure analysis",
        "Engineering notes",
        "Limitations",
        "Reproduction",
    ]


def maturity_claims() -> dict[str, object]:
    return {
        "title": PROJECT_TITLE,
        "problem": RESEARCH_PROBLEM,
        "dataset": DATASET_SUMMARY,
        "takeaways": TAKEAWAYS,
        "next_experiments": NEXT_EXPERIMENTS,
    }
