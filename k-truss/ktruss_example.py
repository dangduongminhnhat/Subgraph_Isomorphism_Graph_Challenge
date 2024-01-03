import networkx as nx
import matplotlib.pyplot as plt

def k_truss(graph, k):
    k_truss = nx.Graph()
    temp_graph = graph.copy()

    while True:
        # Find all edges that belong to at least k-2 triangles
        edges = []
        for edge in temp_graph.edges():
            if belongs_to_k_2_triangles(temp_graph, edge, k):
                edges.append(edge)

        # If no edges were found, stop
        if not edges:
            break

        # Remove the edges from the graph
        for edge in edges:
            temp_graph.remove_edge(*edge)

        # Add the edges to the k-truss subgraph
        k_truss.add_edges_from(edges)

    return k_truss

def belongs_to_k_2_triangles(graph, edge, k):
    triangle_count = 0
    for neighbor in set(graph.neighbors(edge[0])) & set(graph.neighbors(edge[1])):
        common_neighbors = set(graph.neighbors(neighbor)) - {edge[0], edge[1]}
        for node in common_neighbors:
            if graph.has_edge(edge[0], node) and graph.has_edge(edge[1], node):
                triangle_count += 1

    return triangle_count >= k - 2

# Algorithm 2 Improved Truss Decomposition
# Input: G = (VG, EG)
# Output: the k-class, Φk, for 2 ≤ k ≤ kmax
# 1. k ← 2, Φk ← ∅;
# 2. compute sup(e) for each edge e ∈ EG;
# 3. sort all the edges in ascending order of their support;
# 4. while(∃e such that sup(e) ≤ (k − 2))
# 5. let e = (u, v) be the edge with the lowest support;
# 6. assume, w.l.o.g., deg(u) ≤ deg(v);
# 7. for each w ∈ nb(u) do
# 8. if((v, w) ∈ EG)
# 9. sup((u, w)) ← (sup((u, w)) − 1),
# sup((v, w)) ← (sup((v, w)) − 1);
# 10. reorder (u, w) and (v, w) according to
# their new support;
# 11. Φk ← (Φk ∪ {e});
# 12. remove e from G;
# 13. if(not all edges in G are removed)
# 14. k ← (k + 1);
# 15. goto Step 4;
# 16. return Φj , for 2 ≤ j ≤ k;
def k_truss_improved(graph, k):
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

# k_truss_3 = k_truss(G, 3)
# k_truss_4 = k_truss(G, 4)
# k_truss_5 = k_truss(G, 5)
# k_truss_6 = k_truss(G, 6)

k_truss_3 = k_truss_improved(G, 3)
k_truss_4 = k_truss_improved(G, 4)
k_truss_5 = k_truss_improved(G, 5)
k_truss_6 = k_truss_improved(G, 6)

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
