import asyncio
import time

async def fetchData(id, delay):
    print("Data fetching...id: ", id)
    await asyncio.sleep(delay)
    print("Data fetched.id: ", id)
    return {"id: ": id, "data": "some datas"}


async def main():
    task1 = asyncio.create_task(fetchData(1, 2))
    task2 = asyncio.create_task(fetchData(2, 3))
    task3 = asyncio.create_task(fetchData(3, 1))

    result1 = await task1
    print(f"The data that fetched:{result1}")

    result2 = await task2
    print(f"The data that fetched:{result2}")
   
    result3 = await task3
    print(f"The data that fetched:{result3}")

t = time.time()
asyncio.run(main())
print(time.time() - t)