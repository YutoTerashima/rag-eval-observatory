from __future__ import annotations

import math
import re
from collections import Counter


TOKEN = re.compile(r"[a-zA-Z][a-zA-Z0-9_-]+")


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower() for match in TOKEN.finditer(text)]


class BM25Index:
    def __init__(self, docs: dict[str, str], k1: float = 1.5, b: float = 0.75) -> None:
        self.docs = docs
        self.k1 = k1
        self.b = b
        self.tokens = {doc_id: tokenize(text) for doc_id, text in docs.items()}
        self.lengths = {doc_id: len(tokens) for doc_id, tokens in self.tokens.items()}
        self.avg_len = sum(self.lengths.values()) / max(1, len(self.lengths))
        self.df: Counter[str] = Counter()
        for tokens in self.tokens.values():
            self.df.update(set(tokens))

    def score(self, query: str, doc_id: str) -> float:
        q_terms = tokenize(query)
        freqs = Counter(self.tokens[doc_id])
        score = 0.0
        for term in q_terms:
            if term not in self.df:
                continue
            idf = math.log(1 + (len(self.docs) - self.df[term] + 0.5) / (self.df[term] + 0.5))
            tf = freqs[term]
            denom = tf + self.k1 * (1 - self.b + self.b * self.lengths[doc_id] / self.avg_len)
            score += idf * ((tf * (self.k1 + 1)) / denom) if denom else 0.0
        return score

    def search(self, query: str, k: int = 3) -> list[tuple[str, float]]:
        scored = [(doc_id, self.score(query, doc_id)) for doc_id in self.docs]
        return [(doc_id, round(score, 4)) for doc_id, score in sorted(scored, key=lambda item: item[1], reverse=True)[:k] if score > 0]
