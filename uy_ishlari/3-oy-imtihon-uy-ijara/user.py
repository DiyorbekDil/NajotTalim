import hashlib
from typing import Union
from darsdagi_amaliyot.filemanager import user_manager


class User:
    def __init__(self, name, phone, password):
        self.name = name
        self.phone = phone
        self.password = password
        self.active = False

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
            if all_users[idx]['active'] is True:
                return all_users[idx]
            idx += 1


def register() -> Union[object, bool]:
    # This function belongs to auth_menu()
    full_name = input('Enter your name: ')
    try:
        phone = int(input('Enter your phone number: '))
    except ValueError:
        print('Please, enter numbers!')
        return register()
    password = input('Enter your password: ')
    confirm_password = input('Re-enter your password: ')

    user = User(full_name, phone, password)
    if not user.confirm_password(confirm_password):
        print('Passwords don\'t match')
        return register()
    user.password = User.hash_password(user.password)
    user_manager.add(user.__dict__)
    print('You have successfully registered on the site')
    return True


def login() -> Union[object, bool]:
    # This function belongs to auth_menu()
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    password = User.hash_password(password)
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['name'] == name and all_users[idx]['password'] == password:
            all_users[idx]['active'] = True
            user_manager.write(all_users)
            return True
        idx += 1
    print('No such a user, try again!')
    return False


def logout():
    # This function belongs to main_menu()
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['active'] is True:
            all_users[idx]['active'] = False
            user_manager.write(all_users)
        idx += 1
