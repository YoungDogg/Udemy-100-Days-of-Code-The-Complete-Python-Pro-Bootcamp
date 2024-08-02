import asyncio
import random

'''
[x] question: what is different time.sleep() and asyncio.sleep()?
answer: 
time.sleep(): synchronous, blocking, if stops, other codes stop
asyncio.sleep(): asynchronous, non-blocking, if stops, other codes don't stop

[x] question: what is random.uniform()?
answer: generate random floating-point number
'''


async def fetch_data():
    print("Start fetching data...")
    # Simulate a network request
    await asyncio.sleep(random.uniform(0.5, 1.5))
    data = {"data": random.randint(1, 100)}
    print("Data fetched:", data)
    return data


async def process_data(data):
    print("Start processing data...")
    # Simulate data processing
    await asyncio.sleep(random.uniform(.5, 1.5))
    processed_data = {k: v * 2 for k, v in data.items()}
    print("Data processed:", processed_data)
    return processed_data


async def log_results(processed_data):
    print("Start logging results...")
    # Simulate logging
    await asyncio.sleep(random.uniform(0.5, 1.5))
    print("Results logged:", processed_data)


async def task_manager():
    while True:
        print("\nStarting new task cycle...\n")
        # Fetch data
        data = await fetch_data()
        # Process data
        processed_data = await process_data(data)
        # Log results
        await log_results(processed_data)

        # Sleep for a short period before starting the next cycle
        await asyncio.sleep(1)
