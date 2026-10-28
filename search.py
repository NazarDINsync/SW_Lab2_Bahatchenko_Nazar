"""Пошук по чанках: векторний (Gemini ембединги) і keyword (TF-IDF)"""

import json
import os

import numpy as np
from dotenv import load_dotenv
from google import genai
from google.genai import types
from sklearn.feature_extraction.text import TfidfVectorizer

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

chunks = json.load(open("chunks.json", encoding="utf-8"))
embeddings = np.load("embeddings.npy")

# TF-IDF по всіх чанках, для keyword-пошуку
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform([c["text"] for c in chunks])


def vector_search(query, n=3):
    # запит -> ембединг -> топ-N чанків за cosine similarity
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY"),
    )
    q = np.array(response.embeddings[0].values)
    q = q / np.linalg.norm(q)
    scores = embeddings.dot(q)  # вектори нормалізовані, тож це cosine
    return [chunks[i] for i in scores.argsort()[::-1][:n]]


def keyword_search(query, n=3):
    # звичайний пошук за словами (TF-IDF)
    scores = tfidf_matrix.dot(tfidf.transform([query]).T).toarray().ravel()
    return [chunks[i] for i in scores.argsort()[::-1][:n]]


def show(results, answer):
    for c in results:
        mark = "✔" if answer in c["text"] else " "  # ✔ - у чанку є відповідь
        print(" ", mark, c["source"], c["text"][:80].replace("\n", " "))


if __name__ == "__main__":
    # (запит, фраза з правильного чанку)
    queries = [
        # перефразований запит без спільних слів з текстом
        ("Which sibling pair makes retro-sounding tracks inspired by old television programmes from the seventies?", "public broadcasting"),
        # код, який ембединг не розуміє
        ("76:14", "76:14"),
        # звичайне питання
        ("Which label released Selected Ambient Works 85-92?", "Apollo Records"),
    ]
    for query, answer in queries:
        print("\n=== Запит:", query)
        print("Keyword:")
        show(keyword_search(query), answer)
        print("Векторний:")
        show(vector_search(query), answer)