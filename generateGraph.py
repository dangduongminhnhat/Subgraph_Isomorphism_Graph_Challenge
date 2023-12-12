import time
import sys
import networkx as nx
import random


def generate_graph(file_name, n, m):
    file = open("data/" + file_name + ".tsv", "w")
    seed = int(time.time())

    graph = nx.gnm_random_graph(n, m, seed=seed)
    for e in graph.edges():
        file.write(str(e[0]) + "\t" + str(e[1]) + "\t" + "1" + "\n")
    file.close()


random.seed(int(time.time()))
if len(sys.argv) == 1:
    file_name = "default"
else:
    file_name = sys.argv[1]
try:
    n = int(sys.argv[2])
except:
    n = random.randint(5, 10)
m = random.randint(n + 1, n * (n - 1) // 2)

generate_graph(file_name, n, m)
