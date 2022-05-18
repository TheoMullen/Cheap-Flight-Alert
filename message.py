class Message:
    def __init__(self, data):
        self.data = data

    def write(self):
        foreign_city = self.data["cityTo"]
        price = self.data["price"]
        route_1 = self.data["routes"][0]
        route_2 = self.data["routes"][1]
        dep_date = self.data["route"][0]["local_departure"][0:10]
        ret_date = self.data["route"][1]["local_departure"][0:10]
        dep_time = self.data["route"][0]["local_departure"][11:16]
        ret_time = self.data["route"][1]["local_departure"][11:16]
        link = self.data["deep_link"]

        message = f"""
        Return Flight: {foreign_city}
        Price: £{price}
        
        From: {route_1[0]} To: {route_1[1]}
        Depart: {dep_time} {dep_date}
        From: {route_2[0]} To: {route_2[1]}
        Return: {ret_time} {ret_date}
        
        Link: {link}
        """

        return message
