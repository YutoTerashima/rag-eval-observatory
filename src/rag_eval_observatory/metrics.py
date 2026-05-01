from __future__ import annotations

import math


def reciprocal_rank(retrieved: list[str], gold: str) -> float:
    return 1.0 / (retrieved.index(gold) + 1) if gold in retrieved else 0.0


def dcg(retrieved: list[str], gold: str) -> float:
    if gold not in retrieved:
        return 0.0
    rank = retrieved.index(gold) + 1
    return 1 / math.log2(rank + 1)


def aggregate_retrieval(rows: list[dict]) -> dict[str, float]:
    total = len(rows)
    if total == 0:
        return {"hit_rate": 0.0, "mrr": 0.0, "ndcg": 0.0}
    hit_rate = sum(bool(row["hit_at_k"]) for row in rows) / total
    mrr = sum(reciprocal_rank(row["retrieved"], row["gold_doc"]) for row in rows) / total
    ndcg = sum(dcg(row["retrieved"], row["gold_doc"]) for row in rows) / total
    return {"hit_rate": round(hit_rate, 3), "mrr": round(mrr, 3), "ndcg": round(ndcg, 3)}
