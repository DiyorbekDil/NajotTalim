import hashlib
from typing import Union
from jsonManager import user_manager
from logging_file import log_decorator


admin_name = '00'
admin_password = '00'


class User:
    def __init__(self, name, password, phone):
        self.name = name
        self.password = password
        self.phone = phone
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


@log_decorator
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
    user = User(full_name, password, phone)
    if not user.confirm_password(confirm_password):
        print('Passwords don\'t match')
        return register()
    user.password = User.hash_password(user.password)
    user_manager.add(user.__dict__)
    print('You have successfully registered on the site')
    return True


@log_decorator
def login() -> int:
    # This function belongs to auth_menu()
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    if name == admin_name and password == admin_password:
        return 1
    password = User.hash_password(password)
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['name'] == name and all_users[idx]['password'] == password:
            all_users[idx]['active'] = True
            user_manager.write(all_users)
            return 2
        idx += 1
    else:
        return 3


@log_decorator
def logout():
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['active'] is True:
            all_users[idx]['active'] = False
            user_manager.write(all_users)
            return
        idx += 1
