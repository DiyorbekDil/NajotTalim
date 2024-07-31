import os
import json
class JsonManager:
    file_name = 'products.json'

    def check_existence(self):
        return os.path.exists(self.file_name)

    def create_json_file(self):
        if not self.check_existence():
            with open(self.file_name, 'x', encoding='UTF-8'):
                return 'File is created'
        return 'File exists'

    def read_json_file(self):
        if self.check_existence():
            if os.path.getsize(self.file_name) != 0:
                with open(self.file_name, 'r', encoding='UTF-8') as file:
                    return json.load(file)
            return []
        return []

    def write_json_file(self, data):
        with open(self.file_name, 'w', encoding='UTF-8') as file:
            json.dump(obj=data, fp=file, indent=4)
            return 'Data is added'

    def add_one_data(self, data: dict):
        all_data = self.read_json_file()
        all_data.append(data)
        self.write_json_file(all_data)

    def add_more_data(self, data: list):
        if self.check_existence():
            all_data = self.read_json_file()
            for d in data:
                all_data.append(d)
            return self.write_json_file(all_data)
        return 'File does not exist'