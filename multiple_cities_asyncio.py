import csv
import json
import time
import asyncio
import requests

city_list = ['Chennai' for i in range(40)]


async def get_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = base_url + city_name
    response = requests.get(url)
    json_data = {"record": json.loads(response.text)}
    await update_data(json_data)


async def update_data(json_data):
    with open('async_data.csv', 'a', newline="") as file:
        csv_file = csv.writer(file)
        for data in json_data.values():
            csv_file.writerow([data['name'], data['coord']['lon'], data['coord']['lat'], data['main']['temp'],
                               data['main']['temp_max'], data['main']['temp_min']])


async def main(cities):
    for city in cities:
        task = asyncio.create_task(get_data(city))
        await task


if __name__ == '__main__':
    start_time = time.strftime('%X')
    print('started at', start_time)
    asyncio.run(main(city_list))
    end_time = time.strftime('%X')
    print('finished at', end_time)
