import hashlib
from jsonManager import user_manager


class User:
    def __init__(self, full_name, phone, password):
        self.full_name = full_name
        self.phone = phone
        self.password = password
        self.is_login = False

    def confirm_password(self, confirm_password):
        return self.password == confirm_password

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def active_user():
        all_users = user_manager.read()
        idx = 0
        while idx < len(all_users):
            if all_users[idx]['is_login'] is True:
                return all_users[idx]
            idx += 1
