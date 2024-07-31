from jsonManager import user_manager, attach_manager
from users import User
from attachments import Attachment


def main_menu():
    text = """
    1.Leave an attachment (ilova - zayavka)
    2.Remove an attachment
    3.Possible barters
    4.My attachments
    5.Log-out
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        leave_attach()
    elif user_input == '2':
        remove_attach()
        main_menu()
    elif user_input == '3':
        possible_barter()
        main_menu()
    elif user_input == '4':
        my_attachments()
    elif user_input == '5':
        logout()
        auth_menu()
    else:
        print('Unexpected character!')
        return main_menu()


def leave_attach():
    # This function belongs to main_menu()
    give = input('Enter a book name you want to give instead: ')
    get = input('Enter a book name you want to read: ')
    if give.isspace() or get.isspace() or give == '' or get == '':
        print('Please, enter the names of books!')
        return leave_attach()
    active_user = User.active_user()
    attach = Attachment(active_user['full_name'], active_user['phone'], get, give)
    attach_manager.add(attach.__dict__)
    print('Success!')
    return main_menu()


def remove_attach():
    # This function belongs to main_menu()
    give = input('Enter a book name you want to give instead: ')
    get = input('Enter a book name you want to read: ')
    user = User.active_user()
    data = attach_manager.read()
    flag = False
    idx = 0
    while idx < len(data):
        if data[idx]['phone'] == user['phone'] and data[idx]['get'] == get and data[idx]['give'] == give:
            del data[idx]
            flag = True
            break
        idx += 1
    attach_manager.write(data)
    if flag:
        print('Successfully removed!')
    else:
        print('You do not have such a attachment!')


def possible_barter():
    # This function belongs to main_menu()
    all_attach = attach_manager.read()
    active = User.active_user()
    my_attach = Attachment.find_attach(active['phone'])
    temp = []
    if not my_attach:
        print('You do not have any attachments!')
        return main_menu()
    else:
        for attach in my_attach:
            for oth in all_attach:
                if oth['phone'] != attach['phone']:
                    if oth['give'] == attach['get'] and oth['get'] == attach['give']:
                        temp.append(oth)
    if len(temp) != 0:
        for i in temp:
            print(f'You will give: {i["get"]} <-> get: {i["give"]} >>> Phone: {i["phone"]}')
    else:
        print('Not found!')


def my_attachments():
    active = User.active_user()
    my_attach = Attachment.find_attach(active['phone'])
    for i in my_attach:
        print(f'Get: {i["get"]} <-> Give: {i["give"]}')
    return main_menu()


def logout():
    # This function belongs to main_menu()
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['is_login'] is True:
            all_users[idx]['is_login'] = False
            user_manager.write(all_users)
        idx += 1


def auth_menu():
    text = """
    1.Register
    2.Log-in
    3.Exit
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        register()
    elif user_input == '2':
        login()
    elif user_input == '3':
        return
    else:
        print('Unexpected character!')
        return auth_menu()


def register():
    # This function belongs to auth_menu()
    full_name = input('Enter your full name: ')
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
    return auth_menu()


def login():
    # This function belongs to auth_menu
    full_name = input('Enter your full name: ')
    password = input('Enter your password: ')
    password = User.hash_password(password)
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['full_name'] == full_name and all_users[idx]['password'] == password:
            all_users[idx]['is_login'] = True
            user_manager.write(all_users)
            return main_menu()
        idx += 1
    print('No such a user, try again!')
    return auth_menu()


auth_menu()
