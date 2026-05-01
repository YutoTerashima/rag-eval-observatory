from __future__ import annotations

import json
from pathlib import Path

from .bm25 import BM25Index


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_dataset(corpus_path: Path, cases_path: Path, k: int = 3) -> list[dict[str, object]]:
    corpus = {item["doc_id"]: item["text"] for item in load_json(corpus_path)}
    cases = load_json(cases_path)
    index = BM25Index(corpus)
    rows = []
    for case in cases:
        retrieved = index.search(case["question"], k=k)
        ids = [doc_id for doc_id, _ in retrieved]
        hit = case["gold_doc"] in ids
        rows.append(
            {
                "case_id": case["case_id"],
                "gold_doc": case["gold_doc"],
                "retrieved": ids,
                "scores": dict(retrieved),
                "hit_at_k": hit,
                "rank": ids.index(case["gold_doc"]) + 1 if hit else None,
            }
        )
    return rows
