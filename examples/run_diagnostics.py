import json
from pathlib import Path

from rag_eval_observatory.diagnostics import run_diagnostics


if __name__ == "__main__":
    data = run_diagnostics()
    out = Path("reports/diagnostics.json")
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps(data, indent=2))
