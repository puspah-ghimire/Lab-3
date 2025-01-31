import matplotlib.pyplot as plt
import numpy as np
import time
import random
from multiprocessing import Pool, cpu_count

def sequential_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sequential_quicksort(left) + middle + sequential_quicksort(right)

def parallel_partition(data):
    """Helper function to sort chunks of data in parallel"""
    return sequential_quicksort(data)

def parallel_quicksort(arr, num_processes=None):
    if num_processes is None:
        num_processes = cpu_count()
        
    # If array is small, use sequential sort
    if len(arr) < 100000:
        return sequential_quicksort(arr)
    
    # Split data into chunks for parallel processing
    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    
    # Sort chunks in parallel
    with Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(parallel_partition, chunks)
    
    # Merge sorted chunks
    return merge_sorted_arrays(sorted_chunks)

def merge_sorted_arrays(arrays):
    """Merge multiple sorted arrays into a single sorted array"""
    result = []
    # Create a list of indices to track current position in each array
    indices = [0] * len(arrays)
    
    while True:
        min_val = float('inf')
        min_idx = -1
        
        # Find the smallest value among current positions
        for i in range(len(arrays)):
            if indices[i] < len(arrays[i]) and arrays[i][indices[i]] < min_val:
                min_val = arrays[i][indices[i]]
                min_idx = i
        
        if min_idx == -1:  # All arrays are exhausted
            break
            
        result.append(min_val)
        indices[min_idx] += 1
    
    return result

def measure_sorting_time(sort_func, arr, **kwargs):
    start_time = time.time()
    sorted_arr = sort_func(arr.copy(), **kwargs)
    return time.time() - start_time

def plot_complexity_comparison():
    # Test different input sizes
    sizes = np.linspace(500000, 10000000, 5, dtype=int)
    parallel_times = []
    sequential_times = []
    num_processes = cpu_count()
    
    print(f"Using {num_processes} CPU cores in parallel")
    
    # Measure actual execution times
    for size in sizes:
        print(f"Size of input: {size}")
        # Generate random array
        arr = random.sample(range(1, size * 10), size)
        
        # Measure times for both algorithms
        parallel_time = measure_sorting_time(
            parallel_quicksort, 
            arr, 
            num_processes=num_processes
        )
        sequential_time = measure_sorting_time(
            sequential_quicksort, 
            arr
        )
        
        print(f"Sequential: {sequential_time:.4f}s, Parallel: {parallel_time:.4f}s")
        
        parallel_times.append(parallel_time)
        sequential_times.append(sequential_time)
    
    # Plotting
    plt.figure(figsize=(12, 8))
    
    # Plot actual times
    plt.plot(sizes, sequential_times, 'b-', 
             label=f'Sequential Quicksort', marker='o')
    plt.plot(sizes, parallel_times, 'r-', 
             label=f'Parallel Quicksort ({num_processes} processes)', marker='o')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sequential vs. Parallel Quicksort Performance')
    plt.legend()
    plt.grid(True)
    
    # Add speedup text
    avg_speedup = np.mean([s/p for s, p in zip(sequential_times, parallel_times)])
    plt.text(0.02, 0.98, f'Average Speedup: {avg_speedup:.2f}x',
             transform=plt.gca().transAxes, 
             bbox=dict(facecolor='white', alpha=0.8))
    
    plt.show()

if __name__ == "__main__":
    plot_complexity_comparison()