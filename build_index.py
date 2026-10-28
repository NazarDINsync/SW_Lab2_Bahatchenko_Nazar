"""Ділить corpus/*.txt на чанки, рахує ембединги через Gemini -> chunks.json + embeddings.npy"""

import glob
import json
import os
import time

import numpy as np
from dotenv import load_dotenv
from google import genai
from google.genai import types

EMBED_MODEL = "gemini-embedding-001"
CHUNK_SIZE = 1000
OVERLAP = 200      # overlap, щоб факт на межі чанків не розрізався
BATCH = 50         # скільки чанків відправляємо в одному запиті

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# ділимо кожну статтю на чанки з кроком CHUNK_SIZE - OVERLAP
chunks = []
for path in sorted(glob.glob("corpus/*.txt")):
    text = open(path, encoding="utf-8").read()
    for i in range(0, len(text), CHUNK_SIZE - OVERLAP):
        piece = text[i:i + CHUNK_SIZE]
        if len(piece.strip()) > 100:  # дуже короткі хвости пропускаємо
            chunks.append({"source": os.path.basename(path), "text": piece})
print("Чанків:", len(chunks))

# ембединги: по BATCH чанків за запит
vectors = []
for i in range(0, len(chunks), BATCH):
    batch = [c["text"] for c in chunks[i:i + BATCH]]
    response = client.models.embed_content(
        model=EMBED_MODEL,
        contents=batch,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT"),
    )
    vectors += [e.values for e in response.embeddings]
    print("ембединги:", len(vectors), "з", len(chunks))
    time.sleep(10)  # ліміти безкоштовного API

# нормалізуємо, щоб cosine similarity = звичайний скалярний добуток
embeddings = np.array(vectors, dtype="float32")
embeddings /= np.linalg.norm(embeddings, axis=1, keepdims=True)

np.save("embeddings.npy", embeddings)
with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

print("Збережено:", embeddings.shape)
