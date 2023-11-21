import requests
import threading
import concurrent.futures
import asyncio
import aiohttp
import time

import os
import logging
import sys


logging.basicConfig(
        level = logging.INFO,
        format = "[%(asctime)s] - [%(levelname)s] - [Process %(process)d, Thread %(thread)d] - %(message)s", 
        datefmt = "%Y-%m-%d %H:%M:%S",
        handlers = [
            logging.StreamHandler(sys.stdout)
        ]
    )

logger = logging.getLogger('log output')

 
DELAY_FACTOR = 2

# Get response from API using 
def get_character_data(character_index: int):
    logger.info(f'Ingesting character number {character_index}')
    response = requests.get(f'https://rickandmortyapi.com/api/character/{character_index}')
    
    if response.status_code == 200:
        logger.info(f"Ingested successfully character number {character_index}")
    else:
        logger.error(f"Ingestion failed character number {character_index}!")

    time.sleep(DELAY_FACTOR)
    return response

# Synchronous programming
def synchronous_api_call(number_of_apis: int):
    for i in range(1, number_of_apis + 1):
        response = get_character_data(i)

# multi-threading
def threading_api_call(number_of_apis: int):
    # Create and start multiple threads
    threads = []
    for i in range(1, number_of_apis + 1):
        thread = threading.Thread(target=get_character_data, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Thread-pool 
def thread_pool_api_call(number_of_apis: int, number_of_threads: int):
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        # Use list comprehension to submit API requests to the thread pool
        results = [executor.submit(get_character_data, i) for i in range(1, number_of_apis + 1)]

        # Retrieve results from the submitted tasks
        for future in concurrent.futures.as_completed(results):
            result = future.result()

# AsyncIO
async def asyncio_get_character_data(character_index: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://rickandmortyapi.com/api/character/{character_index}') as response:
            
            if response.status == 200:
                logger.info(f'Ingesting character number {character_index} ')
                data = await response.json()
                await asyncio.sleep(DELAY_FACTOR)

                logger.info(f"Ingested successfully character number {character_index}")
                return data
            else:
                logger.error(f"Ingestion failed character number {character_index}!")

async def main():
    list_of_characters = range(1, 11)

    tasks = [asyncio_get_character_data(index) for index in list_of_characters]

    results = await asyncio.gather(*tasks)



if __name__ == "__main__":
    start_time = time.time()

    synchronous_api_call(10) # running the synchronous function
    # threading_api_call(10) # running the multi-threading function
    # thread_pool_api_call(10, 3) # running the thread-pool function
    # asyncio.run(main()) # running the async io function
    total_execution_time = time.time() - start_time 
    print(f"Execution time: {total_execution_time} seconds")