import time

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
    start_time = time.time()
    primes = find_primes(1, 10100000)
    end_time = time.time()

    print(f"Prime numbers in the range {prime_range}:")
    print(f"Execution time: {end_time - start_time} seconds")