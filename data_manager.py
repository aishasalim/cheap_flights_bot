import requests
import datetime

class DataManager:
    def __init__(self, kiwi_endpoint, kiwi_token, list_of_destinations=None):
        self.data_kiwi = None
        self.kiwi_endpoint = kiwi_endpoint
        self.kiwi_token = kiwi_token
        self.list_of_destinations = list_of_destinations

        self.date_from = datetime.datetime.now().strftime("%d/%m/%Y")
        self.date_to = datetime.datetime.now() + datetime.timedelta(30)
        self.return_from = datetime.datetime.now() + datetime.timedelta(10)
        self.return_to = self.date_to + datetime.timedelta(10)

    def retrieve_iata_code(self, city_name):
        print(city_name)

    def get_info_kiwi(self, fly_to):
        header = {
            "apikey": self.kiwi_token
        }

        body = {
            "fly_from": "IAH",
            "fly_to": fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to.strftime("%d/%m/%Y"),
            "return_from": self.return_from.strftime("%d/%m/%Y"),
            "return_to": self.return_to.strftime("%d/%m/%Y"),
            "adults": 1,
            "children": 0,
            "selected_cabins": "M",
            "curr": "USD",
            "max_sector_stopovers": 1,
            "nights_in_dst_from": 7,
        }
        respond = requests.get(self.kiwi_endpoint, params=body, headers=header)
        self.data_kiwi = respond.json()
