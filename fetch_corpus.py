"""Завантажує тексти статей з англійської Wikipedia у corpus/*.txt"""

import os
import requests

# назви статей, які беремо з Wikipedia
TITLES = [
    "Aphex Twin",
    "Boards of Canada",
    "Richie Hawtin",
    "Warp (record label)",
    "Mute Records",
    "Techno",
    "Ambient music",
    "Detroit techno",
    "Intelligent dance music",
    "Selected Ambient Works 85–92",
]

API = "https://en.wikipedia.org/w/api.php"
HEADERS = {"User-Agent": "sw-lab2-student/1.0 (bahatchenko.nazar@gmail.com)"}

os.makedirs("corpus", exist_ok=True)
total = 0

for title in TITLES:
    # просимо в API чистий текст статті (без розмітки), redirects - йти за перенаправленням
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": 1,
        "redirects": 1,
        "titles": title,
    }
    r = requests.get(API, params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    page = next(iter(r.json()["query"]["pages"].values()))
    text = page["extract"]

    # зберігаємо в файл, пробіли в назві міняємо на _
    filename = "corpus/" + title.replace(" ", "_").replace("(", "").replace(")", "") + ".txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    words = len(text.split())
    total += words
    print(f"{filename}: {words} слів")

print(f"Разом: {total} слів")
# перевірка, що слів не менше 6000 (вимога лабораторної)
assert total >= 6000, "замало тексту"
