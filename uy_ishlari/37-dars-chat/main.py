from user import register, login


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
            return menu()
        else:
            return auth_menu()
    elif user_input == '3':
        return
    else:
        print('Unexpected character!')
        return auth_menu()


def menu():
    text = """
        1.Create chat
        2.Join the chat
        3.Delete chat
        4.Show my created chats
        5.Show my joined chats
        6.Back
        """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    elif user_input == '6':
        return auth_menu()
    else:
        print('Unexpected character!')
        return auth_menu()


def chat_menu():
    text = """
        1.Create message
        2.Show all messages
        3.Back
       """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        return menu()
    else:
        print('Unexpected character!')
        return auth_menu()


auth_menu()
