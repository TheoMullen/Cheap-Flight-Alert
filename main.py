from flight_search import FlightSearch
from notification_manager import NotificationManager
from data_manager import DataManager
from message import Message


data_manager = DataManager()
data = data_manager.get_data()
choice_list = data["prices"]


flight_search = FlightSearch()
notification_manager = NotificationManager()
data_manager = DataManager()


search_results = [flight_search.search(choice["lowestPrice"], "LON", choice["iataCode"]) for choice in choice_list]
flight_list = list(filter(None, search_results))


for flight in flight_list:
    message = Message(flight).write()
    notification_manager.send(message)
