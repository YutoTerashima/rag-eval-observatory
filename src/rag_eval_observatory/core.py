from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    doc_id: str
    text: str


@dataclass(frozen=True)
class RagResult:
    question: str
    answer: str
    retrieved_ids: list[str]
    context_precision: float
    context_recall: float
    faithfulness: float
    failure_source: str


CORPUS = [
    Document("agent-traces", "Trace grading inspects messages, tool calls, and final answers."),
    Document("rag-metrics", "Context precision and context recall describe retrieval quality."),
    Document("kendo", "Isshin furan means focused attention without distraction."),
]


def retrieve(question: str, corpus: list[Document] = CORPUS, k: int = 2) -> list[Document]:
    terms = {term.strip("?.!,").lower() for term in question.split() if len(term) > 3}
    scored = []
    for doc in corpus:
        score = sum(term in doc.text.lower() for term in terms)
        scored.append((score, doc))
    return [doc for score, doc in sorted(scored, key=lambda item: item[0], reverse=True)[:k] if score > 0]


def answer(question: str, docs: list[Document]) -> str:
    if not docs:
        return "I do not have enough retrieved evidence to answer."
    return docs[0].text


def evaluate(question: str, expected_doc: str) -> RagResult:
    docs = retrieve(question)
    response = answer(question, docs)
    retrieved_ids = [doc.doc_id for doc in docs]
    precision = 1.0 if expected_doc in retrieved_ids and retrieved_ids else 0.0
    recall = 1.0 if expected_doc in retrieved_ids else 0.0
    faithfulness = 1.0 if any(response == doc.text for doc in docs) else 0.0
    if recall == 0:
        source = "retrieval"
    elif faithfulness == 0:
        source = "generation"
    else:
        source = "no_failure"
    return RagResult(question, response, retrieved_ids, precision, recall, faithfulness, source)
