import requests
import pywhatkit

ENDPOINT_1 = f"https://api.openweathermap.org/data/2.5/weather?lat=49.95&lon=19.86&appid={API_KEY}"
ENDPOINT_2 = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "q": "Krakow,PL",
    "appid": API_KEY,
    'units': 'metric',
    'cnt': 4

}

response = requests.get(ENDPOINT_2, params=params)
response.raise_for_status()

weather_data = response.json()

hour_data_list = [w['weather'] for w in weather_data["list"]]

should_take_umbrella = False

for hour_data in hour_data_list:
    for weather in hour_data:
        if int(weather['id']) < 700:
            should_take_umbrella = True
            break

if should_take_umbrella:
    print("You should take an umbrella")
else:
    print("You don't need an umbrella")




