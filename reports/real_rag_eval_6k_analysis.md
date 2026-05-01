# Real Dataset Analysis: Rag-Eval-Dataset-6k

Source: [aizip/Rag-Eval-Dataset-6k](https://huggingface.co/datasets/aizip/Rag-Eval-Dataset-6k)

This experiment profiles 120 real RAG evaluation cases with questions,
answerability labels, difficulty annotations, and retrieved contexts.

- Difficulty counts: {'medium': 60, 'hard': 47, 'easy': 13}
- Answerable counts: {'True': 113, 'False': 7}
- Average contexts per case: 3.758
- Average question/context lexical overlap: 0.625

Interpretation: the dataset is useful for separating retrieval failures from generation
failures because answerability, context volume, and lexical overlap can be compared before
calling any generator.
