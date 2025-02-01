#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
import os
from flight_search import FlightSearch
from data_manager import DataManager
from dotenv import load_dotenv
import requests
from pprint import pprint


dm = DataManager()
print(dm.sheet_data)
fs = FlightSearch()

sheet_data = [fs.search(flight) for flight in dm.sheet_data if len(str(flight['iataCode']).strip()) == 0]

dm.update_data(sheet_data)


