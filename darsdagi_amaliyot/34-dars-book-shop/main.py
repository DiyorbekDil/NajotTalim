from JsonManager import JsonManager


def auth_menu():
    text = """
    1.Sign up
    2.Sign in
    3.Exit
    """

    user_input = input()
    if user_input == '1':
        sign_up()
    elif user_input == '2':
        sign_in()
    elif user_input == '3':
        return
    else:
        return auth_menu()

