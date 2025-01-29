import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv("../.env")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("PIXELA_TOKEN"),
    "username": "shatterstar",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

username = user_params["username"]

# create_user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(create_user_response.status_code)

graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
print(graph_endpoint)
graph_config={
    "id": "graph1",
    "name": "Graph 1",
    "unit": "H",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": os.getenv("PIXELA_TOKEN"),
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# response.raise_for_status()



today = datetime.datetime.now()
body_json = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.5"
}

# response = requests.post(graph_endpoint+"/graph1", json=body_json, headers=headers)
# print(response.text)
# response.raise_for_status()

update_json = {
    "quantity" : "12"
}

# update_response = requests.put(graph_endpoint+"/graph1/"+today.strftime("%Y%m%d"), json=update_json, headers=headers)


delete_response = requests.delete(graph_endpoint+"/graph1/"+today.strftime("%Y%m%d"), headers=headers)
print(delete_response.status_code)

print(today.strftime("%Y%m%d"))




