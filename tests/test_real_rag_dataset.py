import json
from pathlib import Path


def test_real_rag_sample_contains_context_features():
    rows = [json.loads(line) for line in Path("datasets/external/rag_eval_6k_sample.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(rows) >= 100
    assert all("question" in row and row["context_chars"] for row in rows)
    assert any(row["answerable"] is not None for row in rows)
