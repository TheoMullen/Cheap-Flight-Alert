import requests
import datetime as dt


class FlightSearch:
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.header = {"Content-Type": "application/json", "apikey": "XI40vBDeC4ijxpuCqDRWUctgR1JEqcbk"}
        self.from_date = dt.datetime.now() + dt.timedelta(days=7)
        self.to_date = dt.datetime.now() + dt.timedelta(days=28)

    def search(self, price, fly_from, fly_to):
        params = {
            "price_to": price,
            "fly_from": fly_from,
            "fly_to": fly_to,
            "dateFrom": self.from_date.strftime("%d/%m/%Y"),
            "dateTo": self.to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 2,
            "max_stopovers": 0,
        }

        response = requests.get(url=self.endpoint, params=params, headers=self.header)
        response.raise_for_status()
        data = response.json()["data"]
        if len(data) >= 1:
            return data[0]
