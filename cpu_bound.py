import time
import multiprocessing
import os

import logging
import sys

logging.basicConfig(
        level = logging.INFO,
        format = "[%(asctime)s] - [%(levelname)s] - [Process %(process)d, Thread %(thread)d] - %(message)s", 
        datefmt = "%Y-%m-%d %H:%M:%S",
        handlers = [
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('log/multiprocessing_log.txt')
        ]
    )

logger = logging.getLogger('log output')

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
        
        logger.info(f'Processing number {number}')
        if is_prime(number):
            primes.append(number)
    return primes

def multiprocessing_find_primes(prime_range:list, number_of_processors:int):

    chunk_size = (prime_range[1] - prime_range[0] + 1) // number_of_processors

    with multiprocessing.Pool(processes=number_of_processors) as pool:
        results = pool.starmap(find_primes, [
            (prime_range[0] + i * chunk_size, prime_range[0] + (i + 1) * chunk_size - 1)
            for i in range(number_of_processors)
        ])
    
    primes = [prime for sublist in results for prime in sublist]
    
if __name__ == "__main__":
    num_processes = 3
    prime_range = (1, 10100000)
    

    start_time = time.time()
    find_primes(1, 10100000)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")