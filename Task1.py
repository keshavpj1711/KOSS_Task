# Mycode
import asyncio
import time
import aiohttp


async def download_page(el):
    url = f"https://reqres.in/api/users?page{el}"  # The 'f' at the start of the URL string in the code snippet represents an f-string (formatted string literal)
    # Since we are changing el to an element in arr[]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(f"Download Complete - page {el}")
            return data


async def main():
    arr = [1, 2, 3]
    tasks = [download_page(el) for el in arr]

    # To measure the time of execution
    start = time.time()
    await asyncio.gather(tasks[0], tasks[1], tasks[2])  # This part of the code is whose execution time is calculated
    time_taken = time.time() - start

    print('Time Taken:', time_taken)


asyncio.run(main())

# Output may not be consistent as sometimes it may be Downloaded 1 then 2 and 3 or 3, 2 and 1 or 3, 1 and 2
# This is because it depends on the latency of the webpage and how quickly a fucntion is accessible
