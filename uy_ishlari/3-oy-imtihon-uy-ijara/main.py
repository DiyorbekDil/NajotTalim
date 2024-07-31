from user import logout, login, register
from house import give_rent, my_houses, delete_house, see_all
from house import search_by_rooms, search_by_city
from request import leave_request, see_requests

"""
auth_menu - ro'yxatdan o'tish va tizimga kirish uchun
oluvchi va beruvchi bir xil tartibda ro'yxatdan o'tadi
main_menu - qolgan barcha operatsiyalar bajariladi
"""


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
        if login():
            return main_menu()
        else:
            return auth_menu()
    elif user_input == '3':
        return
    else:
        print('Unexpected character!')
        return auth_menu()


def main_menu():
    text = '''
    1.See all the houses for rent - ijaraga olish
    2.Search by number of rooms
    3.Search by name of city
    4.Leave a request for a house for rent
    *******    ******     *****
    5.Rent a house - ijaraga berish
    6.See the list of houses that you have rented out
    7.Delete a house that you have rented out
    8.See a list of those who have expressed interest
    ****    *****    **********
    9.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        see_all()
        main_menu()
    elif user_input == '2':
        search_by_rooms()
        main_menu()
    elif user_input == '3':
        search_by_city()
        main_menu()
    elif user_input == '4':
        leave_request()
        main_menu()
    elif user_input == '5':
        if give_rent():
            return main_menu()
    elif user_input == '6':
        my_houses()
        main_menu()
    elif user_input == '7':
        delete_house()
        main_menu()
    elif user_input == '8':
        see_requests()
        main_menu()
    elif user_input == '9':
        logout()
        auth_menu()
    else:
        print('Unexpected character!')
        return main_menu()


auth_menu()
