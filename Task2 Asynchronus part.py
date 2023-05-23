#Mycode

import time
import aiohttp
import asyncio
import json

async def download_page(comic_id):
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            file_data = await response.json()  # Stores all the data in json file
            filename = f"comic{comic_id}.json"
            with open(filename, 'w') as file:  # Opening the file to write
                json.dump(file_data, file)  # Dumping all the data of json file
            print(f"Downloaded - comic_id = {comic_id}")

async def main():
    # To measure execution of time
    start_time = time.time()
    tasks = [download_page(i) for i in range(1,201)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    time_taken = end_time-start_time

    print("Execution Time = ", time_taken)

asyncio.run(main())

#Execution Time =  0.6216354370117188
