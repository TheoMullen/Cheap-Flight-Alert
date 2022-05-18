import os
from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ.get("API_KEY")
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.phone_number = os.environ.get("PHONE_NUMBER")
        self.my_number = os.environ.get("MY_NUMBER")

    def send(self, message):
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(body=message, from_=self.phone_number, to=self.my_number)
