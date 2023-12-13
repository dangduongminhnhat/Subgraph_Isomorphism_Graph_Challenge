import networkx as nx
import numpy as np


def brute_force_counting(graph):
    count_triangles = 0
    operations = 0
    for i in graph.nodes():
        for j in graph.nodes():
            for k in graph.nodes():
                operations += 1
                if i > j and j > k:
                    if graph.has_edge(i, j) and graph.has_edge(j, k) and graph.has_edge(k, i):
                        count_triangles += 1
    return count_triangles, operations


def node_iterator_counting(graph):
    count_triangles = 0
    operations = 0
    for i in graph.nodes():
        adj = list(graph.neighbors(i))
        for j in adj:
            for k in adj:
                operations += 1
                if j > k and i > j and graph.has_edge(j, k):
                    count_triangles += 1
    return count_triangles, operations


def matrix_muliplication_counting(graph):
    matrix = nx.to_numpy_array(graph, dtype=int)
    matrix = np.asmatrix(matrix)

    A = matrix.dot(matrix)
    count_triangles = 0
    operations = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            operations += 1
            count_triangles += matrix[i, j] * A[i, j]
    return count_triangles // 6, operations


def forward_counting(graph):
    count_triangles = 0
    operations = 0
    A = {}
    for v in graph.nodes():
        A[v] = set()
    for s in range(graph.number_of_nodes()):
        try:
            for t in graph.neighbors(s):
                if s < t:
                    for v in (A[s] & A[t]):
                        operations += 1
                        count_triangles += 1
                    A[t].add(s)
        except:
            continue
    return count_triangles, operations
