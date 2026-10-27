# Лабораторна робота №02. LLM-екстракція, векторний пошук та GraphRAG

**Студент:** Назар Багатченко
**Тема:** музика (електронна музика, виконавці, лейбли, жанри)

## 1. Предметна область, джерела і питання

**Предметна область:** електронна музика (техно, ambient, IDM), виконавці та лейбли.

**Корпус:** 9 статей англійської Wikipedia, разом ~32 000 слів (ліцензія CC BY-SA). Завантажуються скриптом `fetch_corpus.py` у папку `corpus/`.

| Стаття | Слів |
|---|---|
| [Aphex Twin](https://en.wikipedia.org/wiki/Aphex_Twin) | 5228 |
| [Boards of Canada](https://en.wikipedia.org/wiki/Boards_of_Canada) | 2785 |
| [Richie Hawtin](https://en.wikipedia.org/wiki/Richie_Hawtin) | 1660 |
| [Warp (record label)](https://en.wikipedia.org/wiki/Warp_(record_label)) | 2811 |
| [Techno](https://en.wikipedia.org/wiki/Techno) | 9907 |
| [Ambient music](https://en.wikipedia.org/wiki/Ambient_music) | 3785 |
| [Detroit techno](https://en.wikipedia.org/wiki/Detroit_techno) | 2258 |
| [Intelligent dance music](https://en.wikipedia.org/wiki/Intelligent_dance_music) | 1884 |
| [Selected Ambient Works 85–92](https://en.wikipedia.org/wiki/Selected_Ambient_Works_85%E2%80%9392) | 1680 |

**Питання до тексту:** 5 питань (3 прості, 2 на синтез з кількох документів), див. `questions.md`.

## 2. LLM-екстракція

TODO

## 3. Векторний пошук

TODO

## 4. Граф знань і GraphRAG

TODO

## 5. Помилки та їх виправлення

TODO

## 6. Висновки

TODO

## Запуск

```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # вписати свій GEMINI_API_KEY з aistudio.google.com
```
