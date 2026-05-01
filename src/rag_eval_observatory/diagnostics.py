from __future__ import annotations

from collections import Counter

from .core import RagResult, evaluate


CASES = [
    ("What does trace grading inspect?", "agent-traces"),
    ("What describes retrieval quality?", "rag-metrics"),
    ("What does isshin furan mean?", "kendo"),
    ("What is the deployment SLA?", "nonexistent"),
]


def diagnose_case(question: str, expected_doc: str) -> dict[str, object]:
    result = evaluate(question, expected_doc)
    return {
        "question": result.question,
        "retrieved_ids": result.retrieved_ids,
        "answer": result.answer,
        "context_precision": result.context_precision,
        "context_recall": result.context_recall,
        "faithfulness": result.faithfulness,
        "failure_source": "missing_gold" if expected_doc == "nonexistent" and not result.retrieved_ids else result.failure_source,
    }


def run_diagnostics() -> dict[str, object]:
    rows = [diagnose_case(question, expected) for question, expected in CASES]
    sources = Counter(row["failure_source"] for row in rows)
    avg_recall = sum(float(row["context_recall"]) for row in rows) / len(rows)
    avg_faithfulness = sum(float(row["faithfulness"]) for row in rows) / len(rows)
    return {
        "average_context_recall": round(avg_recall, 3),
        "average_faithfulness": round(avg_faithfulness, 3),
        "failure_sources": dict(sorted(sources.items())),
        "cases": rows,
    }
