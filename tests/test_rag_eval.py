from rag_eval_observatory.core import evaluate


def test_rag_eval_success_case():
    result = evaluate("What does trace grading inspect?", "agent-traces")
    assert result.context_recall == 1.0
    assert result.faithfulness == 1.0
    assert result.failure_source == "no_failure"
