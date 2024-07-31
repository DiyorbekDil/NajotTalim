from JsonManager import JsonManager

users_manager = JsonManager('users.json')


class User:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.is_login = False



