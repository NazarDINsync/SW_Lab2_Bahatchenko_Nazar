"""GraphRAG: резюме спільнот графа через Gemini -> community_summaries.json"""

import json
import os
import time

import community as community_louvain
from dotenv import load_dotenv
from google import genai

from build_graph import build_graph

MODEL = "gemini-3.8-flash"
MIN_SIZE = 5  # резюме робимо тільки для спільнот від 5 вузлів

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def ask(prompt):
    return client.models.generate_content(model=MODEL, contents=prompt).text


def summarize_communities():
    graph = build_graph()
    partition = community_louvain.best_partition(graph.to_undirected(), random_state=1)

    summaries = {}
    for c in sorted(set(partition.values())):
        nodes = [n for n in graph if partition[n] == c]
        if len(nodes) < MIN_SIZE:
            continue
        # зв'язки всередині спільноти, по одному в рядку
        facts = [
            f"{graph.nodes[s]['label']} --{d['relation']}--> {graph.nodes[o]['label']}"
            for s, o, d in graph.edges(data=True) if s in nodes and o in nodes
        ]
        prompt = (
            "Below are facts about electronic music from one community of a knowledge graph.\n"
            "Write a short summary (3-4 sentences) of what this community is about: "
            "name the main entities and how they are connected.\n\n" + "\n".join(facts)
        )
        print("спільнота", c, "вузлів:", len(nodes))
        summaries[c] = {"entities": [graph.nodes[n]["label"] for n in nodes], "summary": ask(prompt)}
        time.sleep(6)  # ліміти безкоштовного API
    return summaries


if __name__ == "__main__":
    summaries = summarize_communities()
    with open("community_summaries.json", "w", encoding="utf-8") as f:
        json.dump(summaries, f, ensure_ascii=False, indent=2)
    print("Збережено резюме:", len(summaries))
