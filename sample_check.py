"""Бере 20 випадкових фактів з facts.json для ручної перевірки -> verification.md"""

import json
import random

facts = json.load(open("facts.json", encoding="utf-8"))

random.seed(42)  # щоб вибірка щоразу була та сама
sample = random.sample(facts, 20)

lines = [
    "# Ручна перевірка 20 фактів",
    "",
    "Вибірка: `random.seed(42)`, 20 з %d фактів (`sample_check.py`)." % len(facts),
    "",
    "| # | Факт | Цитата з тексту | Є в тексті | Вердикт | Помилка |",
    "|---|---|---|---|---|---|",
]

for n, f in enumerate(sample, 1):
    fact = f"{f['subject']} ({f['subject_type']}) -{f['predicate']}-> {f['object']} ({f['object_type']})"
    # чи цитата дослівно є в оригінальній статті
    text = open("corpus/" + f["source"], encoding="utf-8").read()
    in_text = "так" if f["evidence"] in text else "ні"
    lines.append(f"| {n} | {fact} | {f['evidence']} ({f['source']}) | {in_text} |  |  |")

with open("verification.md", "w", encoding="utf-8") as out:
    out.write("\n".join(lines) + "\n")

print("Записано verification.md")
