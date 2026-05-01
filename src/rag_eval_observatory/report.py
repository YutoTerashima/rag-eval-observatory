from __future__ import annotations

from .core import evaluate


CASES = [
    ("What does trace grading inspect?", "agent-traces"),
    ("What describes retrieval quality?", "rag-metrics"),
    ("What does isshin furan mean?", "kendo"),
]


def run_report() -> str:
    rows = []
    for question, expected in CASES:
        result = evaluate(question, expected)
        rows.append(
            f"| {question} | {','.join(result.retrieved_ids)} | {result.context_recall:.2f} | {result.faithfulness:.2f} | {result.failure_source} |"
        )
    return "\n".join(
        [
            "# RAG Evaluation Report",
            "",
            "| Question | Retrieved | Recall | Faithfulness | Failure Source |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "The mock observatory is intentionally small so each metric can be inspected by hand.",
        ]
    )
