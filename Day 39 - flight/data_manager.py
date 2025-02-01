import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = f"https://api.sheety.co/{os.getenv('SHEETY_ID')}/{os.getenv('SHEETY_FLIGHT_APP_NAME')}"
        self.headers = {"Authorization": f"Bearer {os.getenv('SHEETY_FLIGHT_TOKEN')}"}
        data = requests.get(self.url, headers=self.headers)
        data.raise_for_status()
        self.sheet_data = data.json()['prices']


    def update_single_row(self, flight):
        print(flight)
        data = requests.put(f"{self.url}/{flight['id']}", headers=self.headers, json={"price": flight})
        data.raise_for_status()

    def update_data(self, data):
        for row in data:
            print(row)
            data = requests.put(f"{self.url}/{row['id']}", headers=self.headers, json={"price": row})
            data.raise_for_status()



