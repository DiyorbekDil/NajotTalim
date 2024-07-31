from user import register, login, logout
from logging_file import log_decorator
from plane import add_plane, remove_plane, show_planes
from airport import add_airport, remove_airport, show_airports
from flight import add_flight, show_flights, search_flights_by
from purchase import buy_ticket, my_booked_tickets


"""
user - Diyor
parol - 1234
"""


@log_decorator
def template(name):
    text = (f"\n1.Add a {name}\n"
            f"2.Remove a {name}\n"
            f"3.Show all {name}\'s\n"
            f"4.Back admin menu\n")

    print(text)


@log_decorator
def auth_menu():
    print("""
    1.Register
    2.Login
    3.Exit
    """)
    user_input = input('Enter a number: ')

    if user_input == '1':
        register()
        auth_menu()
    elif user_input == '2':
        outcome = login()
        if outcome == 1:
            return admin_menu()
        elif outcome == 2:
            return user_menu()
        else:
            print('No such a user!')
            return auth_menu()
    elif user_input == '3':
        return
    else:
        print('Unexpected character!')
        return auth_menu()


@log_decorator
def admin_menu():
    text = '''
    1.Plane (CRUD)
    2.Airport (CRUD)
    3.Add flight
    4.Show all flights
    5.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        admin_plane_manager()
    elif user_input == '2':
        admin_airport_manager()
    elif user_input == '3':
        add_flight()
        admin_menu()
    elif user_input == '4':
        show_flights()
        admin_menu()
    elif user_input == '5':
        auth_menu()
    else:
        print('Unexpected character!')
        return admin_menu()


@log_decorator
def admin_plane_manager():
    template('plane')

    user_input = input('Enter a number: ')
    if user_input == '1':
        add_plane()
        admin_plane_manager()
    elif user_input == '2':
        remove_plane()
        admin_plane_manager()
    elif user_input == '3':
        show_planes()
        admin_plane_manager()
    elif user_input == '4':
        return admin_menu()
    else:
        print('Unexpected character!')
        return admin_menu()


@log_decorator
def admin_airport_manager():
    template('airport')

    user_input = input('Enter a number: ')
    if user_input == '1':
        add_airport()
        admin_airport_manager()
    elif user_input == '2':
        remove_airport()
        admin_airport_manager()
    elif user_input == '3':
        show_airports()
        admin_airport_manager()
    elif user_input == '4':
        return admin_menu()
    else:
        print('Unexpected character!')
        return admin_menu()


@log_decorator
def user_menu():
    text = """
    1.Search flights
    2.All the available flights
    3.Buy ticket
    4.My booked flights
    5.Log-out
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        search_flights_by()
        user_menu()
    elif user_input == '2':
        show_flights()
        user_menu()
    elif user_input == '3':
        buy_ticket()
        user_menu()
    elif user_input == '4':
        my_booked_tickets()
        user_menu()
    elif user_input == '5':
        logout()
        auth_menu()
    else:
        print('Unexpected character!')
        return admin_menu()


auth_menu()
