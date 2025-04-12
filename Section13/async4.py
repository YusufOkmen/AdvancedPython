import asyncio
import time

async def fetchData(id, delay):
    print("Data fetching...id: ", id)
    await asyncio.sleep(delay)
    print("Data fetched.id: ", id)
    return {"id: ": id, "data": "some datas"}


async def main():
    results = await asyncio.gather(fetchData(1, 2), fetchData(2, 3), fetchData(3, 1))

    for result in results:
        print(result)

t = time.time()
asyncio.run(main())
print(time.time() - t)