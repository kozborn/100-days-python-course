import os
import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv('../.env')

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_exercise = input("What exercises did you do today?\n")

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

body = {
    "query": user_exercise,
    "weight_kg": 88,
    "height_cm": 182,
    "age": 38,
}
# POST TO NUTRITIONIX
response = requests.post(ENDPOINT, headers=headers, json=body)
response.raise_for_status()
exercises_from_response = response.json()['exercises']
print(exercises_from_response)
# NUTRI_RESPONSE = {'exercises':
#                       [{'tag_id': 100,
#                         'user_input': 'walk',
#                         'duration_min': 12,
#                         'met': 3.5,
#                         'nf_calories': 61.6,
#                         'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg',
#                                   'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg', 'is_user_uploaded': False},
#                         'compendium_code': 17190, 'name': 'walking', 'description': None, 'benefits': None
#                     }]
#                   }


SHEETY_ENDPOINT = f"https://api.sheety.co/{os.getenv('SHEETY_ID')}/{os.getenv('SHEETY_APP_NAME')}"

# POST TO SHEETY
SHEETY_HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {os.getenv('SHEETY_TOKEN')}"
}

exercises = [{"date": dt.datetime.now().strftime("%d/%m/%Y"), "exercise": exercise['name'], "time": dt.datetime.now().strftime("%H:%M:%S"), "duration": exercise['duration_min'], "calories": exercise['nf_calories']} for exercise in exercises_from_response]

exercises_body = {
    "workout" : exercises[0],
}

sheety_upload_response = requests.post(SHEETY_ENDPOINT, headers=SHEETY_HEADERS, json=exercises_body)
sheety_upload_response.raise_for_status()
print(sheety_upload_response.json())


sheety_response = requests.get(SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
sheety_response.raise_for_status()
sheety_json = sheety_response.json()
print(sheety_json)










