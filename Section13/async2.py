import asyncio

async def fetchData(delay):
    print("Data fetching...")
    await asyncio.sleep(delay)
    print("Data fetched.")
    return {"data": "some datas"}


async def main():
    print("start")
    task = await fetchData(2)
    print(f"The data that fetched: {task}")
    print("end")

asyncio.run(main())
