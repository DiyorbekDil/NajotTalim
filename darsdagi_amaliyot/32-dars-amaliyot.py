import hashlib
#
# password = 'diyor'
#
# print(hashlib.sha256(password.encode()).hexdigest())

import os, json


class JsonManager:
    file_name = 'reports.json'

    def check_existence(self):
        return os.path.exists(self.file_name)

    def read(self):
        if self.check_existence():
            if os.path.getsize(self.file_name) != 0:
                with open(self.file_name, 'r') as file:
                    data = json.load(file)
                    return data
            return []
        return []

    def write(self, all_data):
        with open(self.file_name, mode='w') as file:
            json.dump(all_data, file, indent=4)
            return "Data is added"

    def add(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        return self.write(all_data)

class User(JsonManager):
    def __init__(self, username, password, id):
        self.username = username
        self.password = password
        self.id = id

    def convert_dict(self):
        return {
            'username': self.username,
            'password': hashlib.sha256(self.password.encode()).hexdigest(),
            'id': self.id
        }

    def register(self):
        data = self.convert_dict()
        self.add(data)

    def login(self, id, password):
        for user in self.read():
            if user['id'] == id and user['password'] == hashlib.sha256(password.encode()).hexdigest():
                return 'You are welcome'
        return 'No such a user'

def menu():
    while True:
        admin = User('admin', 'admin', 'admin')
        user_input = int(input('Enter a number: '))
        if user_input == 1:
            user_name = input('user_name ')
            password = input('password ')
            id = input('id ')
            new = User(user_name, password, id)
            new.register()



