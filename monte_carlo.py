import random
import time
import matplotlib.pyplot as plt

# Fermat's Primality Test
def fermat_test(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:  # a^(n-1) % n
            return False
    return True

# Miller-Rabin Primality Test
def miller_rabin_test(n, k):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as d * 2^r
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    def check_composite(a):
        # a^d % n
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        if check_composite(a):
            return False
    return True

# Monte Carlo simulation for primality test using both methods
def monte_carlo_primality_test(n, k):
    fermat_result = fermat_test(n, k)
    miller_rabin_result = miller_rabin_test(n, k)
    
    return fermat_result, miller_rabin_result

def main():
    n_values = [120, 137, 237, 471, 561]  # numbers to test
    k = 20  # Number of iterations for each test
    fermat_times = []
    miller_rabin_times = []
    
    for n in n_values:
        # Measure time for Fermat's test
        start_time = time.time()
        fermat_result, _ = monte_carlo_primality_test(n, k)
        fermat_times.append(time.time() - start_time)
        
        # Measure time for Miller-Rabin test
        start_time = time.time()
        _, miller_rabin_result = monte_carlo_primality_test(n, k)
        miller_rabin_times.append(time.time() - start_time)
        
        print(f"Testing n = {n}:")
        print(f"  Fermat's Test: {'Prime' if fermat_result else 'Composite'}")
        print(f"  Miller-Rabin Test: {'Prime' if miller_rabin_result else 'Composite'}")
    
    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, fermat_times, label="Fermat's Test", marker='o')
    plt.plot(n_values, miller_rabin_times, label="Miller-Rabin Test", marker='o')
    
    plt.xlabel('Value of n')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Time Taken by Fermat and Miller-Rabin Tests')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
