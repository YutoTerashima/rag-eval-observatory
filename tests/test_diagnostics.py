from rag_eval_observatory.diagnostics import run_diagnostics


def test_diagnostics_include_failure_sources():
    data = run_diagnostics()
    assert "failure_sources" in data
    assert len(data["cases"]) >= 4
