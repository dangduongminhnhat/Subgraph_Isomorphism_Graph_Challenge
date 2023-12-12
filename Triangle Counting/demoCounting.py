from triangleCounting import brute_force_counting, node_iterator_counting, matrix_muliplication_counting, forward_counting
import networkx as nx
import time
from animationCounting import animation_graph, demo_brute_force, draw_graph
import sys


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

    print("\n------")
    print("Algorithm is", algo.__name__)
    print("The number of triangles is", triangles)
    print("time to excute is", end - start, "(s)")
    print("------\n")


try:
    file_name = sys.argv[1]
    graph = generate_graph(f"../data/{file_name}.tsv")
except:
    graph = generate_graph("../data/dataA.tsv")

algorithm_experiment(graph, brute_force_counting)
algorithm_experiment(graph, node_iterator_counting)
algorithm_experiment(graph, matrix_muliplication_counting)
algorithm_experiment(graph, forward_counting)
