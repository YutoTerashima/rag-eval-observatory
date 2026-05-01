from pathlib import Path

from rag_eval_observatory.pipeline import evaluate_dataset


def test_bm25_pipeline_retrieves_gold_docs():
    rows = evaluate_dataset(Path("datasets/corpus.json"), Path("datasets/qa_cases.json"))
    assert any(row["case_id"] == "Q001" and row["hit_at_k"] for row in rows)
