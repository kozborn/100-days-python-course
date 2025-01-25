import requests
import time
from datetime import datetime
MY_LAT = 49.951005
MY_LNG = 19.867640

iss_endpoint = "http://api.open-notify.org/iss-now.json"
sunset_endpoint = "http://api.sunrise-sunset.org/json"
params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

def check_ISS_position_and_time():
    iss_response = requests.get(iss_endpoint)
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    print(iss_data)
    if iss_data['message'] == 'success':
        print(iss_data['iss_position'])
    else:
        print(iss_data['message'])

    sunset_response = requests.get(sunset_endpoint, params=params)
    sunset_response.raise_for_status()
    sunset_data = sunset_response.json()

    sunrise = datetime.fromisoformat(sunset_data['results']['sunrise'])
    sunset = datetime.fromisoformat(sunset_data['results']['sunset'])

    time_now = datetime.now()

    # IS ISS close to my position
    iss_lat = float(iss_data['iss_position']['latitude'])
    iss_lng = float(iss_data['iss_position']['longitude'])

    if iss_lat - 5 > MY_LAT < iss_lat + 5 and iss_lng - 5 > MY_LNG < iss_lng + 5:
        print("On position")
        if sunrise.hour > time_now.hour < sunset.hour:
            print("Go outside and look for ISS")
    else:
        print(f"Wrong position ({(iss_lng, iss_lat)}) - {(MY_LNG, MY_LAT)}")

while True:
    check_ISS_position_and_time()
    time.sleep(60)