from user import register, login, logout
from scooter import add_scooter, delete, show_scooters
from rent import rent_scooter, return_scooter


def auth_menu():
    text = """
    1.Register
    2.Log-in
    3.Exit
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        if register():
            return auth_menu()
    elif user_input == '2':
        t = login()
        if t == 1:
            return main_menu()
        elif t == 2:
            return auth_menu()
        else:
            return admin_menu()
    elif user_input == '3':
        return
    else:
        print('Unexpected character!')
        return auth_menu()


def admin_menu():
    text = '''
    1.Add a scooter
    2.Delete a scooter
    3.Show all scooters
    4.Back
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        add_scooter()
        admin_menu()
    elif user_input == '2':
        delete()
        admin_menu()
    elif user_input == '3':
        show_scooters()
        admin_menu()
    elif user_input == '4':
        return auth_menu()
    else:
        print('Unexpected character!')
        return admin_menu()


def main_menu():
    text = '''
    1.Show all scooters
    2.Rent a scooter
    3.Return a scooter
    4.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        show_scooters()
        main_menu()
    elif user_input == '2':
        rent_scooter()
        main_menu()
    elif user_input == '3':
        return_scooter()
        main_menu()
    elif user_input == '4':
        logout()
        return auth_menu()
    else:
        print('Unexpected character!')
        return main_menu()


auth_menu()

