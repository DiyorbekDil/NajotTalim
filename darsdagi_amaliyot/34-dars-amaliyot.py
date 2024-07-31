class User:
    def __init__(self, name, phone, password):
        self.name = name
        self.phone = phone
        self.password = password


def sign_up():
    pass


def sign_in():
    pass


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


def ui():
    text = """
    1.Show all books
    """