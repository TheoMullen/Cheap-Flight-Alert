from flight_search import FlightSearch
from notification_manager import NotificationManager
from data_manager import DataManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


# data_manager = DataManager()
# data = data_manager.get_data()
# preferred_flights = data["prices"]
choice_list = [
    {
      "city": "Paris",
      "iataCode": "PAR",
      "lowestPrice": 50,
      "id": 2
    },
    {
      "city": "Nice",
      "iataCode": "NCE",
      "lowestPrice": 60,
      "id": 3
    },
    {
      "city": "Madrid",
      "iataCode": "MAD",
      "lowestPrice": 60,
      "id": 4
    },
    {
      "city": "Barcelona",
      "iataCode": "BCN",
      "lowestPrice": 80,
      "id": 5
    },
    {
      "city": "Vienna",
      "iataCode": "VIE",
      "lowestPrice": 60,
      "id": 6
    },
    {
      "city": "Brussels",
      "iataCode": "BRU",
      "lowestPrice": 50,
      "id": 7
    },
    {
      "city": "Milan",
      "iataCode": "MIL",
      "lowestPrice": 70,
      "id": 8
    },
    {
      "city": "Rome",
      "iataCode": "ROM",
      "lowestPrice": 70,
      "id": 9
    },
    {
      "city": "Florence",
      "iataCode": "FLR",
      "lowestPrice": 60,
      "id": 10
    },
    {
      "city": "Venice",
      "iataCode": "VCE",
      "lowestPrice": 80,
      "id": 11
    },
    {
      "city": "Dubrovnik",
      "iataCode": "DBV",
      "lowestPrice": 70,
      "id": 12
    },
    {
      "city": "Istanbul",
      "iataCode": "IST",
      "lowestPrice": 70,
      "id": 13
    },
    {
      "city": "Bologna",
      "iataCode": "BLQ",
      "lowestPrice": 60,
      "id": 14
    },
    {
      "city": "Naples",
      "iataCode": "NAP",
      "lowestPrice": 70,
      "id": 15
    }
  ]


flight_search = FlightSearch()

for _ in choice_list:
    flight_search.search(fly_from="LON", fly_to=_["iataCode"], price=_["lowestPrice"], date_from=, date_to=)