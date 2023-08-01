import pyshorteners


def shorten_flight_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)


class FlightSearch:
    def __init__(self, data_manager, list_of_destinations=None):
        self.data_manager = data_manager
        self.list_of_destinations = list_of_destinations

    def flight_search(self, fly_to_iata_code):
        self.data_manager.get_info_kiwi(fly_to_iata_code)
        # Check if the response from the API is not empty and contains the required data
        if self.data_manager.data_kiwi['data']:
            cost = int(self.data_manager.data_kiwi['data'][0]["price"])
            link = self.data_manager.data_kiwi['data'][0]["deep_link"]
            return {"cost": cost, "link": link}
        else:
            return None

    def format_flights(self):
        results = []
        for destination in self.list_of_destinations[1:]:  # Skip the first element if it's a header
            if len(destination) < 2:
                print(f"Warning: destination {destination} does not have enough elements")
                continue  # Skip to the next iteration

            fly_to_city_name = destination[0]
            fly_to_iata_code = destination[1]

            flight_info = self.flight_search(fly_to_iata_code)

            if flight_info:
                shortened_flight_link = shorten_flight_url(flight_info['link'])
                result_message = (f"Check out flight from {self.data_manager.data_kiwi['data'][0]['cityFrom']} to "
                                  f"{fly_to_city_name} {fly_to_iata_code}\n"
                                  f"<b>COST:</b> ${flight_info['cost']}\n"
                                  f"<b>LINK:</b> {shortened_flight_link}")
                results.append(result_message)
        return results


