import csv
import json
from urllib.request import urlopen

header = ['name', 'longitude', 'latitude', 'temperature']




def get_city_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = base_url + city_name
    response = urlopen(url)

    data_json = {"records": json.loads(response.read())}

    return data_json
    print(data_json)


def write_csv(data_json):
    with open('citydata.csv', 'w', encoding='utf-8', newline='') as file:
        csv_file = csv.writer(file)
        csv_file.writerow(header)

        for item in data_json.values():
            csv_file.writerows([item['name'], item['coord']['lon'], item['coord']['lat'],
                                item['main']['temp']])

        return {'msg': 'csv file updated successfully'}


if __name__ == '__main__':
    city = input("Enter the city name :\n")
    data = get_city_data(city)

    write_csv(data)
