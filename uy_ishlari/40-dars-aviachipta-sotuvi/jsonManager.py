import os
import json
from logging_file import log_decorator


class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name

    @log_decorator
    def check_existence(self):
        return os.path.exists(self.file_name)

    @log_decorator
    def read(self):
        if self.check_existence():
            if os.path.getsize(self.file_name) != 0:
                with open(self.file_name, 'r') as file:
                    data = json.load(file)
                    return data
            return []
        return []

    @log_decorator
    def write(self, all_data):
        with open(self.file_name, mode='w') as file:
            json.dump(all_data, file, indent=4)
            return "Data is added"

    @log_decorator
    def add(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        return self.write(all_data)


user_manager = JsonManager('./jsonFiles/users.json')
plane_manager = JsonManager('./jsonFiles/planes.json')
airport_manager = JsonManager('./jsonFiles/airports.json')
flight_manager = JsonManager('./jsonFiles/flights.json')
booked_flights = JsonManager('./jsonFiles/purchases.json')

