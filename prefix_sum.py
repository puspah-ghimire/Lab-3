import matplotlib.pyplot as plt
import numpy as np
import time
import random
from multiprocessing import Pool, cpu_count

def sequential_prefix_sum(arr):
    """Sequential implementation of prefix sum."""
    result = np.zeros(len(arr), dtype=int)
    result[0] = arr[0]
    for i in range(1, len(arr)):
        result[i] = result[i - 1] + arr[i]
    return result

def parallel_prefix_sum(arr, num_processes=None):
    """Parallel implementation of prefix sum using multiprocessing."""
    if num_processes is None:
        num_processes = cpu_count()

    # If array is small, use sequential prefix sum
    if len(arr) < 100000:
        return sequential_prefix_sum(arr)

    # Divide the array into chunks
    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with Pool(processes=num_processes) as pool:
        partial_sums = pool.map(sequential_prefix_sum, chunks)

    # Adjust each chunk's result based on the previous chunk's sum
    for i in range(1, len(partial_sums)):
        partial_sums[i] += partial_sums[i - 1][-1]

    # Merge the chunks into a single array
    result = np.concatenate(partial_sums)
    return result

def measure_prefix_sum_time(prefix_sum_func, arr, **kwargs):
    start_time = time.time()
    result = prefix_sum_func(arr.copy(), **kwargs)
    return time.time() - start_time

def plot_complexity_comparison():
    # Test different input sizes
    sizes = np.linspace(5000000, 20000000, 5, dtype=int)
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
        parallel_time = measure_prefix_sum_time(
            parallel_prefix_sum, 
            arr, 
            num_processes=num_processes
        )
        sequential_time = measure_prefix_sum_time(
            sequential_prefix_sum, 
            arr
        )
        
        print(f"Sequential: {sequential_time:.4f}s, Parallel: {parallel_time:.4f}s")
        
        parallel_times.append(parallel_time)
        sequential_times.append(sequential_time)
    
    # Plotting
    plt.figure(figsize=(12, 8))
    
    # Plot actual times
    plt.plot(sizes, sequential_times, 'b-', 
             label=f'Sequential Prefix Sum', marker='o')
    plt.plot(sizes, parallel_times, 'r-', 
             label=f'Parallel Prefix Sum ({num_processes} processes)', marker='o')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sequential vs. Parallel Prefix Sum Performance')
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
