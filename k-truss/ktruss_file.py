import networkx as nx
import matplotlib.pyplot as plt

def read_edges_from_file(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) == 2:
                edges.append((int(data[0]), int(data[1])))
            else:
                print(f"Invalid line: {line}")
    return edges

# Specify the path to your file
file_path = '../data/lastfm_asia_edges.csv'
edges = read_edges_from_file(file_path)

G = nx.Graph(edges)

# Plot the original graph with nodes and labels hidden
plt.subplot(191)
nx.draw(G, with_labels=False, font_weight='bold', node_size=1)
plt.title('G')

k_truss_10 = nx.algorithms.k_truss(G, 10)
k_truss_12 = nx.algorithms.k_truss(G, 12)
k_truss_14 = nx.algorithms.k_truss(G, 14)
k_truss_15 = nx.algorithms.k_truss(G, 15)
k_truss_16 = nx.algorithms.k_truss(G, 16)
# k_truss_20 = nx.algorithms.k_truss(G, 20)
# k_truss_70 = nx.algorithms.k_truss(G, 70)

# Plot the k-truss decomposition with nodes and labels hidden
plt.subplot(192)
nx.draw(k_truss_10, with_labels=False, font_weight='bold', node_size=1)
plt.title('10-truss')

plt.subplot(193)
nx.draw(k_truss_12, with_labels=False, font_weight='bold', node_size=1)
plt.title('12-truss')

plt.subplot(194)
nx.draw(k_truss_14, with_labels=False, font_weight='bold', node_size=1)
plt.title('14-truss')

plt.subplot(195)
nx.draw(k_truss_15, with_labels=False, font_weight='bold', node_size=1)
plt.title('15-truss')

plt.subplot(196)
nx.draw(k_truss_16, with_labels=False, font_weight='bold', node_size=1)
plt.title('16-truss')

# plt.subplot(197)
# nx.draw(k_truss_20, with_labels=False, font_weight='bold', node_size=1)
# plt.title('20-truss')

# plt.subplot(198)
# nx.draw(k_truss_70, with_labels=False, font_weight='bold', node_size=1)
# plt.title('70-truss')


plt.subplots_adjust(wspace=0.1)
plt.show()
