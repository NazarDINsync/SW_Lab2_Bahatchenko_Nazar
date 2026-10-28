"""Будує граф знань з facts.json (networkx), знаходить спільноти (louvain) і малює graph.png"""

import json

import community as community_louvain
import matplotlib.pyplot as plt
import networkx as nx

# одна сутність під різними іменами (помилка моделі, див. verification.md)
ALIASES = {
    "james": "aphex twin",
    "warp records": "warp",
    "apollo": "apollo records",
    "rephlex": "rephlex records",
    "hawtin": "richie hawtin",
    "sandison brothers": "boards of canada",
    "ambient": "ambient music",
}


def node_id(name):
    # прибираємо невидимі символи, регістр, і замінюємо відомі аліаси
    key = name.replace("‍", "").strip().lower()
    return ALIASES.get(key, key)


def build_graph():
    graph = nx.DiGraph()
    for f in json.load(open("facts.json", encoding="utf-8")):
        s, o = node_id(f["subject"]), node_id(f["object"])
        graph.add_node(s, label=f["subject"], type=f["subject_type"])
        graph.add_node(o, label=f["object"], type=f["object_type"])
        graph.add_edge(s, o, relation=f["predicate"])
    return graph


if __name__ == "__main__":
    graph = build_graph()
    # спільноти шукаємо на неорієнтованому графі
    partition = community_louvain.best_partition(graph.to_undirected())
    print("вузлів:", graph.number_of_nodes(), "ребер:", graph.number_of_edges())
    sizes = sorted([list(partition.values()).count(c) for c in set(partition.values())], reverse=True)
    print("спільнот:", len(sizes), "розміри:", sizes)

    # малюємо: колір = спільнота, підписи тільки у великих вузлів
    pos = nx.spring_layout(graph, seed=1, k=0.4)
    plt.figure(figsize=(18, 14))
    nx.draw_networkx_edges(graph, pos, alpha=0.2, arrows=False)
    nx.draw_networkx_nodes(
        graph, pos, node_size=[40 + 40 * graph.degree(n) for n in graph],
        node_color=[partition[n] for n in graph], cmap=plt.cm.tab20,
    )
    labels = {n: graph.nodes[n]["label"] for n in graph if graph.degree(n) >= 4}
    nx.draw_networkx_labels(graph, pos, labels, font_size=8)
    plt.axis("off")
    plt.savefig("graph.png", dpi=120, bbox_inches="tight")
    print("Збережено graph.png")
