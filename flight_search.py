import requests
import os


TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.environ['TEQUILA_API_KEY']


class FlightData:
    # This class is responsible for structuring the flight data
    def __init__(self,
                 price,
                 origin_city,
                 origin_airport,
                 destination_city,
                 destination_airport,
                 depart_date,
                 return_date,
                 airline,
                 operating_carrier
                 ):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.depart_date = depart_date
        self.return_date = return_date
        self.airline = airline
        self.operating_carrier = operating_carrier


class FlightSearch:
    # This class is responsible for talking to the Flight Search API
    def __init__(self):
        self.endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        self.headers = {
            "apikey": TEQUILA_API_KEY,
            "accept": "application/json"
        }

    def get_city_code(self, city_name):
        params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": 10,
            "active_only": "true"
        }

        response = requests.get(url=self.endpoint,
                                headers=self.headers,
                                params=params
                                )

        for location in response.json()['locations']:
            if location['name'] == city_name:
                return location['code']

    def check_flights(self,
                      origin_city_code,
                      destination_city_code,
                      depart_date,
                      return_date):
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": depart_date,
            "date_to": return_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                headers=self.headers,
                                params=params
                                )

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airport=data['route'][0]['flyTo'],
            depart_date=data['route'][0]['local_departure'].split('T')[0],
            return_date=data['route'][1]['local_departure'].split('T')[0],
            airline=data['route'][0]['airline'],
            operating_carrier=data['route'][0]['operating_carrier']
        )

        return flight_data