# RAG GPU Retrieval Benchmark

BM25-style lexical retrieval versus GPU dense hashing retrieval on real RAG cases.

## Dataset

- Source: `aizip/Rag-Eval-Dataset-6k`
- Config: `default`
- Split: `train`

## Reproducibility

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

## Generated Artifacts

- Result JSON: `results/retrieval_failures.json`
- Result JSON: `results/retrieval_metrics.json`
- Result CSV: `results/retrieval_metrics.csv`
- Figure: `figures/retrieval_metrics.png`

## Result Snapshot

```json
[
  {
    "question": "What was the outcome of the legal proceedings involving the individual charged in Oklahoma?",
    "gold_context_preview": "Matloff v. Wallace, 2021 OK CR 21, ¶15, 497 P. 3d 686, 689 (reaffirming recognition of the Cherokee, Choctaw, and Chickasaw Reservations); Grayson v. State, 2021 OK CR 8, ¶10, 485 P. 3d 250, 254 (Seminole Reservation). In light of McGirt an",
    "top_context_preview": "Supp. 1110, 1121 (DC 1976) (federal courts had pre-statehood jurisdiction); Clinton 960-962. The Oklahoma Enabling Act and the commitments it demanded in the new Oklahoma Constitution sought to maintain this status quo. Recognizing the poin",
    "rank": 415
  },
  {
    "question": "How does the jurisdiction apply in cases involving crimes committed by non-Indians against Indians in certain areas?",
    "gold_context_preview": "## Syllabus in connection with this case, at the time the opinion is issued. syllabus constitutes no part of the opinion of the Court but has been Decisions for the convenience of the reader. Co., NOTE: Where it is feasible, a syllabus (hea",
    "top_context_preview": "Under the Court's precedents, as we will explain, a State's jurisdiction in Indian country may be preempted (i) by federal law under ordinary principles of federal preemption, or (ii) when the exercise of state jurisdiction would unlawfully",
    "rank": 161
  },
  {
    "question": "Who can prosecute crimes in Indian country?",
    "gold_context_preview": "This case is the first time that the matter has been fully explored by this Court. Until the Court's decision in McGirt two years ago, this ------ ## Opinion of the Court question likewise did not matter much in Oklahoma. Most everyone in O",
    "top_context_preview": "Under the Court's precedents, as we will explain, a State's jurisdiction in Indian country may be preempted (i) by federal law under ordinary principles of federal preemption, or (ii) when the exercise of state jurisdiction would unlawfully",
    "rank": 48
  },
  {
    "question": "What's the deal with jurisdiction in Oklahoma?",
    "gold_context_preview": "Those questions are: (i) whether Indian country is part of a State or instead is separate and independent from a State; and (ii) if Indian country is part of a State, whether the State has concurrent jurisdiction with the Federal Government",
    "top_context_preview": "Supp. 1110, 1121 (DC 1976) (federal courts had pre-statehood jurisdiction); Clinton 960-962. The Oklahoma Enabling Act and the commitments it demanded in the new Oklahoma Constitution sought to maintain this status quo. Recognizing the poin",
    "rank": 272
  },
  {
    "question": "What's the deal with jurisdiction in Indian country?",
    "gold_context_preview": "Those holdings, too, contravene Castro-Huerta's argument regarding the General Crimes Act. grants the Federal Government exclusive jurisIn advancing his enclave argument, Castro-Huerta also tries to analogize the text of the General Crimes ",
   
```

## Failure Analysis

The experiment stores model disagreements, retrieval misses, or policy-risk examples in the result JSON/CSV files when available. These examples are intentionally kept as previews or structured metadata where the source data can contain unsafe or sensitive text.

## Limitations

- Smoke mode prioritizes reproducibility and runtime over leaderboard-scale performance.
- Raw datasets are downloaded to `data/raw/` and are not committed.
- Metrics should be interpreted as portfolio research baselines, not production claims.
