import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import time


def demo_brute_force(graph):
    count_triangles = 0
    triangles = []
    for i in graph.nodes():
        for j in graph.nodes():
            for k in graph.nodes():
                if i > j and j > k:
                    if graph.has_edge(i, j) and graph.has_edge(j, k) and graph.has_edge(k, i):
                        count_triangles += 1
                if i != j and j != k and k != i:
                    triangles.append([k, j, i, count_triangles])
    return triangles


def animation_graph(G, algo):
    # Create Graph
    np.random.seed(int(time.time()))
    pos = nx.spring_layout(G)

    triangles = algo(G)

    # Build plot
    fig, ax = plt.subplots(figsize=(6, 4))
    labels = {}
    for i in G.nodes():
        labels[i] = i

    def update(num):
        global count
        path = triangles[num]
        ax.clear()

        # Background nodes
        nx.draw_networkx_edges(G, pos=pos, ax=ax, edge_color="gray")
        null_nodes = nx.draw_networkx_nodes(
            G, pos=pos, nodelist=set(G.nodes()) - set(path[:-1]), node_color="white",  ax=ax)
        null_nodes.set_edgecolor("black")

        # Query nodes
        query_nodes = nx.draw_networkx_nodes(
            G, pos=pos, nodelist=path[:-1], node_color="r", ax=ax)
        query_nodes.set_edgecolor("white")
        nx.draw_networkx_labels(
            G, pos=pos, labels=labels,  font_color="white", ax=ax)
        edgelist = []
        for n_a in path[:-1]:
            for n_b in path[:-1]:
                if n_b > n_a and G.has_edge(n_a, n_b):
                    edgelist.append([n_a, n_b])
        if num == 0:
            if path[-1] > 0:
                edge_color = "r"
            else:
                edge_color = "black"
        else:
            if triangles[num - 1][-1] < path[-1]:
                edge_color = "r"
            else:
                edge_color = "black"
        nx.draw_networkx_edges(G, pos=pos, edgelist=edgelist,
                               width=2, ax=ax, edge_color=edge_color)

        # Scale plot ax
        ax.set_title("Triangle counting: " +
                     str(path[-1]), fontweight="bold")
        ax.set_xticks([])
        ax.set_yticks([])

    ani = matplotlib.animation.FuncAnimation(
        fig, update, frames=len(triangles), interval=1000, repeat=True)
    plt.show()
