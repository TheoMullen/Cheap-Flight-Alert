import requests


class DataManager:
    def __init__(self):
        self.get_endpoint = "https://api.sheety.co/70c97a5071378f2b544128a5d45670fa/flightDetails/prices"
        self.post_endpoint = "https://api.sheety.co/70c97a5071378f2b544128a5d45670fa/flightDetails/prices"
        self.put_endpoint = "https://api.sheety.co/70c97a5071378f2b544128a5d45670fa/flightDetails/prices"
        self.delete_endpoint = "https://api.sheety.co/70c97a5071378f2b544128a5d45670fa/flightDetails/prices"


    def get_data(self):
        response = requests.get(url=self.get_endpoint)
        response.raise_for_status()
        print(response.text)


    def add_row(self, city, price):
        params = {"price": {"city": city, "lowestPrice": price}}
        response = requests.post(url=self.post_endpoint, json=params)
        response.raise_for_status()
        print(response.text)


    def edit_row(self, city, price, id):
        params = {"price": {"city": city, "lowestPrice": price}}
        response = requests.put(url=f"{self.put_endpoint}/{id}", json=params)
        response.raise_for_status()
        print(response.text)


    def delete_row(self, id):
        response = requests.delete(url=f"{self.delete_endpoint}/{id}")
        response.raise_for_status()
        print(response.text)


d = DataManager()
d.get_data()