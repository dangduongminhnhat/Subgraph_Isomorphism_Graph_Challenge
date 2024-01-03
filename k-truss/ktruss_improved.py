import networkx as nx
import matplotlib.pyplot as plt

def truss_decomposition(graph, k):
    # Compute support for each edge and sort them in ascending order of their support.
    supports = {(u, v): 0 for u, v in graph.edges}
    for u, v in graph.edges:
        supports[(u, v)] = len(set(graph.neighbors(u)).intersection(set(graph.neighbors(v))))

    sorted_edges = sorted(graph.edges, key=lambda x: supports[x])

    while sorted_edges:
        e = sorted_edges[0]

        if supports[e] <= k - 2:
            # Decrement the support of all other edges that form a triangle with e.
            u, v = e
            common_neighbors = set(graph.neighbors(u)).intersection(set(graph.neighbors(v)))

            for w in common_neighbors:
                if (u, w) in supports:
                    supports[(u, w)] -= 1

                if (v, w) in supports:
                    supports[(v, w)] -= 1

            # Update positions of affected edges.
            sorted_edges.sort(key=lambda x: supports[x])

            # Check if the edge exists in the graph before removing it.
            if graph.has_edge(*e):
                graph.remove_edge(*e)

        else:
            break

        k += 1

    return graph

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 4), (1, 16), (1, 18),
                  (2, 7), (2, 21),
                  (3, 10), (3, 18), (3, 21),
                  (4, 8), (4, 10), (4, 17), (4, 18), (4, 21),
                  (5, 10), (5, 13), (5, 18), (5, 19),
                  (6, 21),
                  (7, 11), (7, 14), (7, 17), (7, 18), (7, 21),
                  (8, 10), (8, 18), (8, 21),
                  (9, 18),
                  (10, 15), (10, 16), (10, 18), (10, 19),
                  (12, 17), (12, 21),
                  (13, 18),
                  (14, 18), (14, 21),
                  (15, 18), (15, 19), (15, 20),
                  (16, 18),
                  (17, 21),
                  (18, 19), (18, 20), (18, 21),
                  (20, 21)])

# Plot the original graph
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.title('Original Graph')

# Set an initial k value
initial_k = 3

# Perform truss decomposition
k_truss_graph = truss_decomposition(G.copy(), initial_k)

# Plot the k-truss decomposition
plt.subplot(122)
nx.draw(k_truss_graph, with_labels=True, font_weight='bold')
plt.title(f'k-Truss Decomposition (k={initial_k})')

plt.show()
