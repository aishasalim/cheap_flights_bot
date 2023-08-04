import requests
import datetime

class DataManager:
    def __init__(self, kiwi_endpoint, kiwi_token, list_of_destinations=None):
        self.data_kiwi = None
        self.kiwi_endpoint = kiwi_endpoint
        self.kiwi_token = kiwi_token
        self.list_of_destinations = list_of_destinations
        self.selected_iata_code = None

        self.date_from = datetime.datetime.now().strftime("%d/%m/%Y")
        self.date_to = datetime.datetime.now() + datetime.timedelta(30)
        self.return_from = datetime.datetime.now() + datetime.timedelta(10)
        self.return_to = self.date_to + datetime.timedelta(10)

    def retrieve_iata_code(self, city_name):
        iata_codes = []
        with open('GlobalAirportDatabase.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if city_name.lower() in parts[3].lower() and parts[1] != 'N/A' and parts[2] != 'N/A':
                    iata_codes.append((parts[2], parts[1]))
        print(iata_codes)
        return iata_codes

    def set_selected_iata_code(self, iata_code):
        self.selected_iata_code = iata_code
        print(f"this is from data manager {iata_code}")

    def get_info_kiwi(self, fly_to):
        header = {
            "apikey": self.kiwi_token
        }

        body = {
            "fly_from": self.selected_iata_code,
            "fly_to": fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to.strftime("%d/%m/%Y"),
            "return_from": self.return_from.strftime("%d/%m/%Y"),
            "return_to": self.return_to.strftime("%d/%m/%Y"),
            "adults": 1,
            "children": 0,
            "selected_cabins": "M",
            "curr": "USD"
        }
        print(body)
        respond = requests.get(self.kiwi_endpoint, params=body, headers=header)
        self.data_kiwi = respond.json()
