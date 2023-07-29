import requests
import datetime

class DataManager:
    def __init__(self, sheets_endpoint, kiwi_endpoint, kiwi_token):
        self.kiwi_endpoint = kiwi_endpoint
        self.kiwi_token = kiwi_token

        self.sheets_respond = requests.get(url=sheets_endpoint)
        self.sheets_data = self.sheets_respond.json()
        self.sheet_list = self.sheets_data["values"]

        self.date_from = datetime.datetime.now().strftime("%d/%m/%Y")
        self.date_to = datetime.datetime.now() + datetime.timedelta(30)
        self.return_from = datetime.datetime.now() + datetime.timedelta(10)
        self.return_to = self.date_to + datetime.timedelta(10)

    def get_info_kiwi(self, fly_to):
        self.header = {
            "apikey": self.kiwi_token
        }

        self.body = {
            "fly_from": "IAH",
            "fly_to": fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to.strftime("%d/%m/%Y"),
            "return_from": self.return_from.strftime("%d/%m/%Y"),
            "return_to": self.return_to.strftime("%d/%m/%Y"),
            "adults": 1,
            "selected_cabins": "M",
            "curr": "USD",
            "max_sector_stopovers": 1
        }
        respond = requests.get(self.kiwi_endpoint, params=self.body, headers=self.header)
        self.data_kiwi = respond.json()
