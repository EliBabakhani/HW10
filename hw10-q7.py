import requests
import json

# class FindCity:
#     def __init__(self, city) -> None:
#         self.city=city
#     def __enter__(self):
#         get_API=requests.get("https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}")

#     def __exit__(self):
#         pass

api_key = "Your_API_Key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input('enter the name of city: ')
complete_url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(f'{city}: {current_temperature}')


else:
    print(" City Not Found ")


# # def get_weather(city:str)->tuple:
# get_API = requests.get(
#     "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}")
# response = print(get_API.status_code)
# # get_API=requests.get('https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}')
# # a=json.dumps(get_API)
# g = []
# for record in response.json():
#     g.append((record[name_city], record[temp]))
# for i in g:
#     if i[0] == 'city':
#         print(f'{name_city}:{temp}')
