from triangleCounting import brute_force_counting
import networkx as nx
import time


def generate_graph(file_name):
    file = open(file_name, "r")
    gr = nx.Graph()
    line = file.readline()
    while line:
        arr = line[:-1].split("\t")
        gr.add_edge(int(arr[0]), int(arr[1]))
        line = file.readline()
    print("Graph's data: " + file_name)
    print("Number of nodes: " + str(gr.number_of_nodes()))
    print("Number of edges: " + str(gr.number_of_edges()))
    return gr


def algorithm_experiment(graph, algo):
    start = time.time()
    triangles = algo(graph)
    end = time.time()
    return (triangles, start, end)


graph = generate_graph("../data/test.tsv")
print(algorithm_experiment(graph, brute_force_counting))
