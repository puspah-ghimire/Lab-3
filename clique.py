import itertools
import random

# check if a subset of vertices forms a clique
def is_clique(graph, vertices):
    for u, v in itertools.combinations(vertices, 2):
        if graph[u][v] == 0:  # No edge between u and v
            return False
    return True

# find all cliques of size k
def find_cliques(graph, k):
    n = len(graph)
    cliques = []
    
    # Generate all combinations of vertices of size k
    for vertices in itertools.combinations(range(n), k):
        if is_clique(graph, vertices):
            cliques.append(vertices)
    
    return cliques

# find the maximum clique in the graph
def find_max_clique(graph):
    n = len(graph)
    
    # Start by checking cliques from the largest possible size down to 1
    for k in range(n, 0, -1):
        cliques = find_cliques(graph, k)
        if cliques:  # If we found cliques of size k
            return cliques[0]  # Return the first found clique (any clique of this size)
    
    return None

if __name__ == "__main__":
    n = int(input("Enter the number of vertices in the graph: "))
    
    # Generate a random adjacency matrix for the graph
    graph = [[0] * n for _ in range(n)]
    
    # Randomly add edges between vertices (with probability 0.5)
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.5:  # 50% chance to add an edge
                graph[i][j] = 1
                graph[j][i] = 1  # Since the graph is undirected
    
    print("Generated Graph (Adjacency Matrix):")
    for row in graph:
        print(row)
    
    # size of the clique to find
    k = int(input("Enter the size of the clique to find: "))
    
    # find cliques of size k
    cliques = find_cliques(graph, k)
    
    print(f"Cliques of size {k}:")
    if cliques:
        for clique in cliques:
            print(clique)
    else:
        print("No cliques found.")
    
    # Find the maximum clique
    max_clique = find_max_clique(graph)
    print("\nMaximum Clique:")
    if max_clique:
        print(max_clique)
    else:
        print("No maximum clique found.")
