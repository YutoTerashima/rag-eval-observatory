import json
from pathlib import Path

from rag_eval_observatory.metrics import aggregate_retrieval
from rag_eval_observatory.pipeline import evaluate_dataset


if __name__ == "__main__":
    rows = evaluate_dataset(Path("datasets/full_corpus.json"), Path("datasets/full_qa_cases.json"))
    metrics = aggregate_retrieval(rows)
    Path("reports/full_pipeline_results.json").write_text(json.dumps({"metrics": metrics, "rows": rows}, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2))
