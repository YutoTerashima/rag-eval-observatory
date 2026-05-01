from rag_eval_observatory.core import evaluate


if __name__ == "__main__":
    result = evaluate("What does trace grading inspect?", "agent-traces")
    print(f"question={result.question}")
    print(
        f"precision={result.context_precision:.2f} "
        f"recall={result.context_recall:.2f} "
        f"faithfulness={result.faithfulness:.2f} "
        f"source={result.failure_source}"
    )
