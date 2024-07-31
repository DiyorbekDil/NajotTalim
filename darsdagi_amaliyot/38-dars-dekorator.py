from datetime import datetime as dt


def my_decorator(func):
    def wrapper():
        tic = dt.now()
        func()
        toc = dt.now()
        print('Time: ', toc-tic)

    return wrapper()


@my_decorator
def ask():
    phone = input('Phone: ')
    name = input('Name: ')
    print(phone, name)


ask()


