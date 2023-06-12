import requests
import json


url = 'https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies'


def connect_url(url: str):
    res = requests.get(url)
    if res.status_code != 200:
        return 'The URL is not valid'
    return res


def wrt_json(response):
    var = json.loads(response.text)

# print(var)
    with open('film.json', 'w') as handle:
        json.dump(var, handle)


def read_data(file: json):
    with open(f'{file}.json', 'r') as read_it:
        data = json.load(read_it)
    for item in data:
        print(item.get('Title')+'\t'+item.get('Year'))
        print()

def post():
    name=input('enter film\'s name')
    r=requests.post(url,json{'Tittle':f'{name}'})
    r.json()

def get_input():

# for reccord in response.json():
#     print(reccord['name'])

a = connect_url(
    'https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies')
print(a)
b = wrt_json(a)
c = read_data('film')
