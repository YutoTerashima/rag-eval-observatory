from rag_eval_observatory.report import run_report


def test_report_has_metric_columns():
    report = run_report()
    assert "Faithfulness" in report
    assert "Failure Source" in report
