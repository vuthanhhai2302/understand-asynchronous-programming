import time
import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

if __name__ == "__main__":
    num_processes = 4
    prime_range = (1, 10100000)
    chunk_size = (prime_range[1] - prime_range[0] + 1) // num_processes

    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(find_primes, [
            (prime_range[0] + i * chunk_size, prime_range[0] + (i + 1) * chunk_size - 1, i, num_processes)
            for i in range(num_processes)
        ])
    
    primes = [prime for sublist in results for prime in sublist]
    
    end_time = time.time()

    print(f"Prime numbers in the range {prime_range}:")
    print(f"Execution time: {end_time - start_time} seconds")