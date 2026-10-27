"""Витягує факти з corpus/*.txt за допомогою Gemini і зберігає в facts.json"""

import glob
import json
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from schema import FactList

MODEL = "gemini-3.8-flash"
CHUNK_SIZE = 3000  # символів у одному шматку тексту

PROMPT = """Extract facts about electronic music from the text below.
Only extract facts that are explicitly stated in the text, do not guess.
For each fact put a short exact quote from the text into 'evidence'.

Text:
"""

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

facts = []

for path in sorted(glob.glob("corpus/*.txt")):
    text = open(path, encoding="utf-8").read()

    # ділимо текст на шматки по CHUNK_SIZE символів
    for i in range(0, len(text), CHUNK_SIZE):
        print(path, i)
        try:
            # structured output: модель повертає JSON за схемою FactList
            response = client.models.generate_content(
                model=MODEL,
                contents=PROMPT + text[i:i + CHUNK_SIZE],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=FactList,
                ),
            )
        except Exception as e:
            print("помилка:", e)  # пропускаємо шматок, якщо API видало помилку
            continue

        for fact in response.parsed.facts:
            row = fact.model_dump()
            row["source"] = os.path.basename(path)
            facts.append(row)
        time.sleep(6)  # ліміти безкоштовного API

with open("facts.json", "w", encoding="utf-8") as f:
    json.dump(facts, f, ensure_ascii=False, indent=2)

print("Разом фактів:", len(facts))
