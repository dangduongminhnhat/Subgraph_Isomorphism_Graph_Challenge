import time
import pandas as pd
from collections import defaultdict
from heapq import heapify, heappop, heapreplace

def read_graph(file_path):
    df = pd.read_csv(file_path, sep='\t', header=None)
    graph = defaultdict(set)
    for _, row in df.iterrows():
        u, v = row[0], row[1]
        graph[u].add(v)
        graph[v].add(u)
    return graph

def truss_decomposition(graph):
    k = 3
    support = {}
    for u in graph:
        for v in graph[u]:
            support[(u, v)] = len(graph[u].intersection(graph[v]))

    while True:
        edges_to_remove = [(u, v) for (u, v), sup in support.items() if sup < k - 2]
        if not edges_to_remove:
            break

        for u, v in edges_to_remove:
            common_neighbors = graph[u].intersection(graph[v])
            for w in common_neighbors:
                support[(u, w)] -= 1
                support[(w, u)] -= 1
                support[(v, w)] -= 1
                support[(w, v)] -= 1
            del support[(u, v)]
            del support[(v, u)]
            graph[u].remove(v)
            graph[v].remove(u)

        k += 1

    return graph, k

def improved_truss_decomposition(graph):
    k = 3
    phi = defaultdict(set)
    support = {}
    edge_list = []
    for u in graph:
        for v in graph[u]:
            sup = len(graph[u].intersection(graph[v]))
            support[(u, v)] = sup
            edge_list.append((sup, (u, v)))

    heapify(edge_list)
    while edge_list:
        sup, (u, v) = edge_list[0]
        if sup > k - 2:
            break

        if len(graph[u]) > len(graph[v]):
            u, v = v, u

        for w in graph[u]:
            if w in graph[v]:
                for edge in [(u, w), (w, u), (v, w), (w, v)]:
                    if edge in support:
                        if support[edge] == sup + 1:
                            heapreplace(edge_list, (sup, edge))
                        else:
                            edge_list.remove((support[edge], edge))
                            heapify(edge_list)
                        support[edge] -= 1

        phi[k].add((u, v))
        del support[(u, v)]
        del support[(v, u)]
        graph[u].remove(v)
        graph[v].remove(u)
        heappop(edge_list)

        if not edge_list:
            k += 1

    return phi, k

# def main():
#     for i in range(1, 11):
#         file_path = f'../data/data{i*100}.tsv'
#         graph = read_graph(file_path)
#         start_time = time.time()
#         truss, k_max = truss_decomposition(graph)
#         end_time = time.time()
#         print(f'Truss decomposition of {file_path} completed in {end_time - start_time} seconds.')

def main():
    for i in range(1, 11):
        file_path = f'../data/data{i*100}.tsv'
        graph = read_graph(file_path)
        start_time = time.time()
        phi, k_max = improved_truss_decomposition(graph)
        end_time = time.time()
        print(f'Improved truss decomposition of {file_path} completed in {end_time - start_time} seconds.')

if __name__ == '__main__':
    main()
