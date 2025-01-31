import itertools
import random

# calculate the total distance of a given path
def total_distance(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    # Add distance from the last city back to the first city
    distance += graph[path[-1]][path[0]]
    return distance

# solve TSP using brute force
def brute_force_tsp(graph):
    n = len(graph)
    cities = list(range(n))
    best_distance = float('inf')
    best_path = []
    
    # Generate all permutations of cities (excluding the starting city, as it's a cycle)
    for path in itertools.permutations(cities):
        # Calculate the total distance for this path
        current_distance = total_distance(graph, path)
        
        # Update the best path and distance if this is better
        if current_distance < best_distance:
            best_distance = current_distance
            best_path = path
            
    return best_distance, best_path

if __name__ == "__main__":
    n = int(input("Enter the number of cities: "))
    
    # Generate a random distance matrix for the cities
    graph = [[0 if i == j else random.randint(1, 100) for j in range(n)] for i in range(n)]
    
    # Display the generated graph (distance matrix)
    print("Generated Distance Matrix (Graph):")
    for row in graph:
        print(row)
    
    best_distance, best_path = brute_force_tsp(graph)
    
    print(f"Shortest distance: {best_distance}")
    print(f"Best path (city order): {best_path}")
