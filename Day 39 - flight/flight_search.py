import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv("../.env")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flights = []
        self.url = "https://test.api.amadeus.com/v1/"

        self.token = ""

        auth_response = requests.post(
            headers= {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            url=self.url + "security/oauth2/token",
            data={"grant_type": "client_credentials", "client_id": os.getenv("AMADEUS_API_KEY"), "client_secret": os.getenv("AMADEUS_API_SECRET")}
        )

        auth_response.raise_for_status()
        print("Auth Response:", auth_response.json())
        self.token = auth_response.json()["access_token"]


    def search(self, flight):
        try:
            headers = {
                "Authorization": "Bearer " + self.token,
            }
            params = {
               "subType": "AIRPORT",
                "keyword": flight['city']
            }
            city_search = requests.get(url=self.url + "reference-data/locations", params=params, headers=headers)
            city_search.raise_for_status()

            pprint(city_search.json()['data'])
        except requests.exceptions.HTTPError as err:
            iataCode = err.response.status_code
        else:
            iataCode = city_search.json()['data'][0]['iataCode'] if len(city_search.json()['data']) > 0 else "Not found"
        flight['iataCode'] = iataCode
        return flight







