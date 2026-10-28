"""Відповідь на «глобальне» питання двома способами: GraphRAG і звичайний vector-RAG -> answers.md"""

import json

from graphrag import ask
from search import vector_search

# питання 5 з questions.md (вимагає синтезу з кількох статей)
QUESTION = (
    "How did electronic music develop from Detroit techno and Brian Eno to IDM, "
    "and which artists and labels connect these genres?"
)
TOP_N = 5


def graphrag_answer(question):
    # map-reduce: резюме всіх спільнот (map вже зроблено в graphrag.py) -> один фінальний запит (reduce)
    summaries = json.load(open("community_summaries.json", encoding="utf-8"))
    text = "\n\n".join(f"Community {c}: {v['summary']}" for c, v in summaries.items())
    return ask(
        "Answer the question using only the community summaries below.\n\n"
        f"Question: {question}\n\nSummaries:\n{text}"
    )


def vector_rag_answer(question):
    # топ-N чанків за запитом напряму в LLM, без графа
    chunks = vector_search(question, TOP_N)
    text = "\n\n".join(c["text"] for c in chunks)
    return ask(
        "Answer the question using only the text fragments below.\n\n"
        f"Question: {question}\n\nFragments:\n{text}"
    ), [c["source"] for c in chunks]


if __name__ == "__main__":
    graph_answer = graphrag_answer(QUESTION)
    vector_answer, sources = vector_rag_answer(QUESTION)

    with open("answers.md", "w", encoding="utf-8") as f:
        f.write(f"# Питання\n\n{QUESTION}\n\n")
        f.write(f"## Відповідь GraphRAG\n\n{graph_answer}\n\n")
        f.write(f"## Відповідь vector-RAG (топ-{TOP_N} чанків: {', '.join(sources)})\n\n{vector_answer}\n")
    print("Записано answers.md")
