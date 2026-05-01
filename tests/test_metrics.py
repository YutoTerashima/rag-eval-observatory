from rag_eval_observatory.metrics import aggregate_retrieval


def test_aggregate_retrieval():
    metrics = aggregate_retrieval([{"retrieved": ["a", "b"], "gold_doc": "b", "hit_at_k": True}])
    assert metrics["hit_rate"] == 1.0
    assert metrics["mrr"] == 0.5
