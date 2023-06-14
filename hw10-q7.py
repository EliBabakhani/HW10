import requests
def main():
    try:
        url='http://api.openweathermap.org/data/2.5/weather'
        appid="be19eafe21e4b6ff9c6d4947d75ff19c"
        city = input("Enter the city name: ")
        para={"q":city, "appid":appid}

        response=requests.get(url,para)
        if response.status_code==200:
            data=response.json()
            temperature=data["main"]["temp"]

        print(f"The temperature in {city} is {temperature}°C.")
    except:
        print("Failed to retrieve weather information. Try again!")
        return main()
if __name__=="__main__":
    main()