import matplotlib.pyplot as plt
import numpy as np
import time
import random
from multiprocessing import Pool, cpu_count

# Sequential Merge Sort
def sequential_mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sequential_mergesort(arr[:mid])
    right = sequential_mergesort(arr[mid:])
    return merge_sorted_arrays([left, right])

# Parallel Merge Sort helper function
def parallel_mergesort(arr):
    """Helper function to sort chunks of data in parallel"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge_sorted_arrays([parallel_mergesort(left), parallel_mergesort(right)])

# Parallel Merge Sort with multiprocessing
def parallel_merge_sort(arr, num_processes=None):
    if num_processes is None:
        num_processes = cpu_count()
    
    # Split data into chunks for parallel processing
    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    
    # Sort chunks in parallel
    with Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(parallel_mergesort, chunks)
    
    # Merge sorted chunks
    return merge_sorted_arrays(sorted_chunks)

# Merge sorted arrays into one
def merge_sorted_arrays(arrays):
    """Merge multiple sorted arrays into a single sorted array"""
    result = []
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

# Measure sorting time for performance comparison
def measure_sorting_time(sort_func, arr, **kwargs):
    start_time = time.time()
    sorted_arr = sort_func(arr.copy(), **kwargs)
    return time.time() - start_time

# Plot complexity comparison
def plot_complexity_comparison():
    # Test different input sizes
    sizes = np.linspace(100000, 1000000, 5, dtype=int)
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
            parallel_merge_sort, 
            arr, 
            num_processes=num_processes
        )
        sequential_time = measure_sorting_time(
            sequential_mergesort, 
            arr
        )
        
        print(f"Sequential: {sequential_time:.4f}s, Parallel: {parallel_time:.4f}s")
        
        parallel_times.append(parallel_time)
        sequential_times.append(sequential_time)
    
    plt.figure(figsize=(12, 8))
    plt.plot(sizes, sequential_times, 'b-', 
             label=f'Sequential Merge Sort', marker='o')
    plt.plot(sizes, parallel_times, 'r-', 
             label=f'Parallel Merge Sort ({num_processes} processes)', marker='o')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sequential vs. Parallel Merge Sort Performance')
    plt.legend()
    plt.grid(True)

    avg_speedup = np.mean([s/p for s, p in zip(sequential_times, parallel_times)])
    plt.text(0.02, 0.98, f'Average Speedup: {avg_speedup:.2f}x',
             transform=plt.gca().transAxes, 
             bbox=dict(facecolor='white', alpha=0.8))
    
    plt.show()

if __name__ == "__main__":
    plot_complexity_comparison()
