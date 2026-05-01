import json
from pathlib import Path

rows = [json.loads(line) for line in Path("datasets/external/rag_eval_6k_sample.jsonl").read_text(encoding="utf-8").splitlines()]
print({"rows": len(rows), "avg_contexts": round(sum(r["num_contexts"] for r in rows) / len(rows), 2), "avg_overlap": round(sum(r["question_context_overlap"] for r in rows) / len(rows), 3)})
