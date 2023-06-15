import requests
import json


url = 'https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies'


def connect_url(url: str):
    res = requests.get(url)
    if res.status_code != 200:
        return 'The URL is not valid'
    return res


def wrt_json(response):
    data = response.json()
    with open('film.json', 'w') as handle:
        json.dump(data, handle)


def read_data(file: json):
    with open(f'{file}.json', 'r') as read_it:
        data = json.load(read_it)
    for item in data:
        print(item.get('Title')+'\t'+item.get('Year'))
        print()


def post():
    url = 'https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies'
    data = {"id": 1, "Title": "About Eli",
            "Year": "1992", "Runtime": "120 min"}
    response = requests.post(url=url, json=data)
    if response.status_code == 201:
        print('POST request successful!')
    else:
        print('Unsuccessful Error', response.status_code)


a = connect_url(
    'https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies')
b = wrt_json(a)
c = read_data('film')
post()
