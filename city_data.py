import codecs
import csv
import json
from urllib.request import urlopen


def get_city_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = base_url + city_name
    response = urlopen(url)

    data_json = json.loads(response.read())

    return data_json


def write_csv(data_json):
    with open('data.csv', 'w', encoding='utf-8') as file:
        csv_file = csv.writer(file)
        for item in data_json.values():
            csv_file.writerow([item])
        return {'msg': 'csv file updated successfully'}


if __name__ == '__main__':
    city = input("Enter the city name :\n")
    data = get_city_data(city)
    print(data)
    update = write_csv(data)
    print(update)
