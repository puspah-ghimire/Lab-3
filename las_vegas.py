import random
import matplotlib.pyplot as plt
import numpy as np
import time

# check if a configuration is valid
def is_valid(board, n):
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                return False  # Same column
            if abs(board[i] - board[j]) == j - i:
                return False  # Same diagonal
    return True

def visualize_board(board, n):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, n, 1))
    ax.set_yticks(np.arange(0, n, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    for i in range(n):
        for j in range(n):
            color = 'white' if (i + j) % 2 == 0 else 'black'
            ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor=color, edgecolor='black'))
            if board[i] == j:
                ax.text(j + 0.5, i + 0.5, 'Q', ha='center', va='center', fontsize=20, color='red')

    plt.xlim(0, n)
    plt.ylim(0, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()
    plt.show()

# print the board
def print_board(board, n):
    for i in range(n):
        row = ['.' for _ in range(n)]  
        row[board[i]] = 'Q'
        print(" ".join(row)) 
    print("\n")

# Las Vegas algorithm
def las_vegas_nqueens(n):
    start_time = time.time()
    
    while True:
        # Randomly place queens (one per row)
        board = random.sample(range(n), n)  # Randomly permutes columns for each row
        
        print("Current configuration:")
        print_board(board, n)
        
        # Check if the current configuration is valid
        if is_valid(board, n):
            end_time = time.time()
            total_time = end_time - start_time
            print("Valid Configuration Found using Las Vegas Algorithm.")
            visualize_board(board, n)
            return total_time
        else:
            print("Invalid Configuration, retrying...\n")
            continue


n = int(input("Enter the number of queens: "))

elapsed_time = las_vegas_nqueens(n)
print(f"\nTime taken to find a valid solution: {elapsed_time:.6f} seconds")
