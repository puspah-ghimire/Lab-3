import random
from itertools import combinations

def brute_force_knapsack(weights, values, max_weight):
    n = len(weights)
    best_value = 0
    best_combination = []

    # Generate all possible combinations of items
    for r in range(1, n + 1):
        for combo in combinations(range(n), r):
            total_weight = sum(weights[i] for i in combo)
            total_value = sum(values[i] for i in combo)
            
            # Check if this combination fits within the weight limit and is better than the previous best
            if total_weight <= max_weight and total_value > best_value:
                best_value = total_value
                best_combination = combo

    return best_value, best_combination

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    
    # Generate random values and weights for each item
    values = [random.randint(50, 1000) for _ in range(n)]
    weights = [random.randint(5, 50) for _ in range(n)]
    
    max_weight = int(input("Enter the maximum weight the knapsack can carry: "))
    
    best_value, best_combination = brute_force_knapsack(weights, values, max_weight)
    
    # Output the result
    print(f"Best Value: {best_value}")
    print(f"Best Combination of Items: {best_combination}")
    print(f"Items in Best Combination (weights, values): "
          + str([(weights[i], values[i]) for i in best_combination]))
