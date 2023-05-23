#Mycode

import requests
import json
import time

start_time = time.time()

for comic_id in range(1, 201):
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    response = requests.get(url)
    if response.status_code == 200:
        #status_code gives the status of the response i.e whether connection is OK(200), Not found(404), Unauthorized(401), Forbidden(403)
        file_data = response.json() #Stores all the data in json file
        filename = f"comic{comic_id}.json"
        with open(filename, 'w') as file: #Opening the file to write
            json.dump(file_data, file) #Dumping all the data of json file
        print(f"Downloaded - comic_id = {comic_id}")
    else:
        print(f"Download Failed - comic_id = {comic_id}")

end_time = time.time()
time_taken = end_time-start_time
#Printing the execution time
print("Execution Time = ", time_taken)

#Execution Time =  102.30453109741211
