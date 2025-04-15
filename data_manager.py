import requests
import os


SHEETY_ENDPOINT = "https://api.sheety.co"
SHEETY_USERNAME = os.environ['SHEETY_USERNAME']
SHEETY_BEARER_TOKEN = os.environ['SHEETY_BEARER_TOKEN']

project_url = f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/flightDeals"
headers = {
            "Authentication": f"Bearer {SHEETY_BEARER_TOKEN}",
            "Content-Type": "application/json"
        }


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}

    def get_location_data(self):
        response = requests.get(
            url=f"{project_url}/prices",
            headers=headers
        )
        response.raise_for_status()
        self.data = response.json()['prices']
        return self.data

    def update_city_codes(self):
        for location in self.data:
            new_data = {
                "price": {
                    "iataCode": location['iataCode']
                }
            }

            response = requests.put(
                url=f"{project_url}/prices/{location['id']}",
                headers=headers,
                json=new_data
            )
            response.raise_for_status()
            print(response.text)