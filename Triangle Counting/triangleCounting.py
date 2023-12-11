import networkx as nx


def brute_force_counting(graph):
    count_triangles = 0
    for i in graph.nodes():
        for j in graph.nodes():
            for k in graph.nodes():
                if i != j and j != k and k != i:
                    if graph.has_edge(i, j) and graph.has_edge(j, k) and graph.has_edge(k, i):
                        count_triangles += 1
    return count_triangles // 6
