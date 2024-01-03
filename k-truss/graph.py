import matplotlib.pyplot as plt

# Assuming these are your arrays
traditional_runtime = [0.03124237, 0.25039864, 1.70855998, 4.52847242, 2.73959541, 18.95525885, 32.22745109, 36.30973411, 43.25523806, 153.11755323]
improved_runtime = [0.01573610, 0.14004827, 1.15944910, 3.02403760, 1.92820740, 12.73270917, 27.39556718, 26.39463478, 35.44532919, 94.47124028]
graph_data = ['data100.tsv', 'data200.tsv', 'data300.tsv', 'data400.tsv', 'data500.tsv', 'data600.tsv', 'data700.tsv', 'data800.tsv', 'data900.tsv', 'data1000.tsv']

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(graph_data, traditional_runtime, label='Traditional')
plt.plot(graph_data, improved_runtime, label='Improved')
plt.xlabel('Graph’s data')
plt.ylabel('Runtime (s)')
plt.title('Runtimes of the different algorithms')
plt.legend()
plt.show()
