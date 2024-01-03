import numpy as np

# Input: Unoriented incidence matrix E and integer k
E = np.array([[1, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0 ,1],
              [0 ,1 ,1 ,0 ,1 ,0],
              [0 ,0 ,1 ,1 ,0 ,1],
              [0 ,0 ,0 ,1 ,1 ,0]])
k = 3

# Output: Incidence matrix of k-truss subgraph Ek
def k_truss(E, k):
    # Initialization
    d = np.sum(E, axis=1)  # Sum of each row of E
    A = E.T @ E  # Product of transpose of E with E
    np.fill_diagonal(A, 0)  # Set diagonal elements to 0
    R = E @ A  # Support matrix of E
    s = np.sum(R, axis=1)  # Number of triangles containing each edge
    x = np.where(s < 2 * (k - 2))[0]  # Indices of edges to be removed

    # Loop until no more edges can be removed
    while len(x) > 0:
        Ex = E[x, :]  # Submatrix of E corresponding to x
        E = np.delete(E, x, axis=0)  # Remove rows from E
        dx = np.sum(Ex, axis=1)  # Sum of each row of Ex
        R = np.delete(R, x, axis=0)  # Remove rows from R
        R = R - Ex.T @ Ex + np.diag(dx)  # Update R using the formula in Algorithm 4
        s = np.sum(R, axis=1)  # Update s
        x = np.where(s < 2 * (k - 2))[0]  # Update x

    # Retain only edges that are part of the k-truss subgraph
    truss_edges = np.sum(R == 2, axis=1) >= k - 2
    E = E[truss_edges]

    # Return the final incidence matrix of k-truss subgraph
    return E

# Print the result
print(k_truss(E, k))
indices = np.where(k_truss(E, k) == 1)

# Zip these indices together to get the edges
edges = list(zip(indices[0], indices[1]))

print(edges)
