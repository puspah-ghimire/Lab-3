import itertools
import random

# check if a given path forms a Hamiltonian cycle
def is_hamiltonian_cycle(graph, path):
    # Check if all the vertices are visited and the last vertex connects to the first
    for i in range(len(path) - 1):
        if graph[path[i]][path[i + 1]] == 0:  # No edge between consecutive vertices
            return False
    # Check if the last vertex connects back to the first vertex
    if graph[path[-1]][path[0]] == 0:
        return False
    return True

# find a Hamiltonian cycle using brute force
def brute_force_hamiltonian_cycle(graph):
    n = len(graph)
    vertices = list(range(n))
    best_path = None
    
    # Generate all permutations of the vertices (excluding the first vertex)
    for path in itertools.permutations(vertices):
        if is_hamiltonian_cycle(graph, path):
            best_path = path
            break  # Return the first valid Hamiltonian cycle found
    
    return best_path

if __name__ == "__main__":
    n = int(input("Enter the number of vertices in the graph: "))
    
    # Generate a random adjacency matrix 
    graph = [[0 if i == j else random.choice([0, 1]) for j in range(n)] for i in range(n)]
    
    print("Generated Adjacency Matrix (Graph):")
    for row in graph:
        print(row)
    
    # find a cycle
    cycle = brute_force_hamiltonian_cycle(graph)
    
    if cycle:
        print(f"Hamiltonian cycle found: {cycle}")
    else:
        print("No Hamiltonian cycle found.")
