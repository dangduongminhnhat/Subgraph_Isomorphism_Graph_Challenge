import networkx as nx
import matplotlib.pyplot as plt

def k_truss(graph, k_max):
    G = graph.copy()

    for edge in list(G.edges()):
        u, v = edge
        sup_e = len(set(G.neighbors(u)) & set(G.neighbors(v)))

        while sup_e < k_max - 2:
            W = set(G.neighbors(u)) & set(G.neighbors(v))
            for w in W:
                edge_u_w = (u, w)
                edge_v_w = (v, w)

                if edge_u_w in G.edges():
                    G[edge_u_w]['sup'] -= 1
                    if G[edge_u_w]['sup'] == 0:
                        G.remove_edge(*edge_u_w)

                if edge_v_w in G.edges():
                    G[edge_v_w]['sup'] -= 1
                    if G[edge_v_w]['sup'] == 0:
                        G.remove_edge(*edge_v_w)

            G.remove_edge(*edge)


    return G

# def k_truss_improved(graph, k):
#     # Compute support for each edge and sort them in ascending order of their support.
#     supports = {(u, v): 0 for u, v in graph.edges}
#     for u, v in graph.edges:
#         supports[(u, v)] = len(set(graph.neighbors(u)).intersection(set(graph.neighbors(v))))

#     sorted_edges = sorted(graph.edges, key=lambda x: supports[x])

#     while sorted_edges:
#         e = sorted_edges[0]

#         if supports[e] <= k - 2:
#             # Decrement the support of all other edges that form a triangle with e.
#             u, v = e
#             common_neighbors = set(graph.neighbors(u)).intersection(set(graph.neighbors(v)))

#             for w in common_neighbors:
#                 if (u, w) in supports:
#                     supports[(u, w)] -= 1

#                 if (v, w) in supports:
#                     supports[(v, w)] -= 1

#             # Update positions of affected edges.
#             sorted_edges.sort(key=lambda x: supports[x])

#             # Check if the edge exists in the graph before removing it.
#             if graph.has_edge(*e):
#                 graph.remove_edge(*e)

#         else:
#             break

#         k += 1

#     return graph

edges = [(1,2), (1,3), (1,4), (1,9),
                  (2,3), (2,4), (2,5), (2,6), (2,9),
                  (3,4), (3,9), (3,10),
                  (4,9),
                  (5,6), (5,7), (5,8), (5,9),
                  (6,7), (6,8), (6,9),
                  (7,8), (7,9), (7,12),
                  (8,9),
                  (9,10), (9,11), (9,12),
                  (11,12), (11,13), (11,14)]

# edges = [(1,4), (1,16), (1,18),
#          (2,7), (2,21),
#          (3,10), (3,18), (3,21),
#          (4,8), (4,10), (4,17), (4,18), (4,21),
#          (5,10), (5,13), (5,18), (5,19),
#          (6,21),
#          (7,11), (7,14), (7,17), (7,18), (7,21),
#          (8,10), (8,18), (8,21),
#          (9,18),
#          (10,15), (10,16), (10,18), (10,19),
#          (12,17), (12,21),
#          (13,18),
#          (14,18), (14,21),
#          (15,18), (15,19), (15,20),
#          (16,18),
#          (17,21),
#          (18,19), (18,20), (18,21),
#          (20,21)]

G = nx.Graph(edges)

# Plot the original graph
plt.subplot(151)
nx.draw(G, with_labels=True, font_weight='bold')
plt.title('Original Graph')

# k_truss_3 = nx.algorithms.k_truss(G, 3)
# k_truss_4 = nx.algorithms.k_truss(G, 4)
# k_truss_5 = nx.algorithms.k_truss(G, 5)
# k_truss_6 = nx.algorithms.k_truss(G, 6)

k_truss_3 = k_truss(G, 3)
k_truss_4 = k_truss(G, 4)
k_truss_5 = k_truss(G, 5)
k_truss_6 = k_truss(G, 6)

# k_truss_3 = k_truss_improved(G, 3)
# k_truss_4 = k_truss_improved(G, 4)
# k_truss_5 = k_truss_improved(G, 5)
# k_truss_6 = k_truss_improved(G, 6)

# Plot the k-truss decomposition
plt.subplot(152)
nx.draw(k_truss_3, with_labels=True, font_weight='bold')
plt.title('k-Truss Decomposition (k = 3)')

plt.subplot(153)
nx.draw(k_truss_4, with_labels=True, font_weight='bold')
plt.title('k = 4')

plt.subplot(154)
nx.draw(k_truss_5, with_labels=True, font_weight='bold')
plt.title('k = 5')

plt.subplot(155)
nx.draw(k_truss_6, with_labels=True, font_weight='bold')
plt.title('k = 6')

plt.subplots_adjust(wspace=0.1)
plt.show()
