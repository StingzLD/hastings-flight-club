import requests
import os

SHEETY_ENDPOINT = "https://api.sheety.co"
SHEETY_USERNAME = os.environ['SHEETY_USERNAME']
SHEETY_BEARER_TOKEN = os.environ['SHEETY_BEARER_TOKEN']


def add_user(first_name, last_name, email):
    url = f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/flightDeals/users"
    
    headers = {
        "Authentication": f"Bearer {SHEETY_BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    
    user_info = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=user_info
    )
    response.raise_for_status()
    print(response.text)
