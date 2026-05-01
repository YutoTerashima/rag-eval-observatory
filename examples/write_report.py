from pathlib import Path

from rag_eval_observatory.report import run_report


if __name__ == "__main__":
    out = Path("reports/rag_eval_report.md")
    out.write_text(run_report(), encoding="utf-8")
    print(out)
