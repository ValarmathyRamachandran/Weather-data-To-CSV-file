import csv
import json
import requests
import time

city_list = ['Mumbai',
             'Kolkata',
             'Delhi',
             'Chennai',
             'Bangalore',
             'Hyderabad',
             'Kolkata',
             'Pune',
             'Lucknow',
             'Kanpur',
             'Indore',
             'Patna',
             'Chandigarh',
             'Shimla',
             'Thiruvananthapuram',
             'Bhopal',
             'Mumbai',
             'Srinagar',
             'Shillong',
             'Jaipur',
             'Mumbai',
             'Kolkata',
             'Delhi',
             'Chennai',
             'Bangalore',
             'Hyderabad',
             'Kolkata',
             'Pune',
             'Lucknow',
             'Kanpur',
             'Indore',
             'Patna',
             'Chandigarh',
             'Shimla',
             'Thiruvananthapuram',
             'Bhopal',
             'Mumbai',
             'Srinagar',
             'Shillong',
             'Jaipur'

             ]


# header = ['name', 'longitude', 'latitude', 'temperature', 'temp_max', 'temp_min']


def get_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = base_url + city_name
    response = requests.get(url)

    text = response.text
    json_data = {"record": json.loads(text)}
    write_data(json_data)


def write_data(json_data):
    with open('multiple_data.csv', 'a', newline="", encoding='utf-8') as file:
        csv_file = csv.writer(file)
        # csv_file.writerow(header)
        for data in json_data.values():
            csv_file.writerow([data['name'], data['coord']['lon'], data['coord']['lat'], data['main']['temp'],
                               data['main']['temp_max'], data['main']['temp_min']])


def main(cities):
    for city in cities:
        get_data(city)


if __name__ == '__main__':
    start_time = time.strftime('%X')
    main(city_list)
    end_time = time.strftime('%X')
    print(start_time, end_time)
