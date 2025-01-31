import time
import matplotlib.pyplot as plt

# Normal Fibonacci function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Fibonacci with memoization
def fib_memo(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = result
    return result

# Performance comparison
n_values = [4, 6, 8, 10, 12, 14]  # Test cases
normal_times = []
memo_times = []
normal_fibs = []
memo_fibs = []

for n in n_values:
    # Measure time for normal Fibonacci
    start = time.time()
    normal_fib = fibonacci(n)
    end = time.time()
    normal_times.append(end - start)
    normal_fibs.append(normal_fib)

    # Measure time for Fibonacci with memoization (clear memo for each n)
    start = time.time()
    memo_fib = fib_memo(n, {})  # Pass an empty dictionary each time
    end = time.time()
    memo_times.append(end - start)
    memo_fibs.append(memo_fib)

    print(f"n = {n}: F(n) = {normal_fib} | t = {normal_times[-1]:.6f}s || MF(n)= {memo_fib} | t = {memo_times[-1]:.6f}s")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, normal_times, label="Normal Fibonacci", marker="o")
plt.plot(n_values, memo_times, label="Memoized Fibonacci", marker="o")
plt.xlabel("n (Fibonacci Index)")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison: Normal vs Memoized Fibonacci")
plt.legend()
plt.grid()
plt.show()
