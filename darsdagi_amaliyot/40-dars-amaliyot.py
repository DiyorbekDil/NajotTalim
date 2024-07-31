import logging
from filemanager import file_manager


class FunctionExecutionError(Exception):
    def __init__(self, message, *args):
        super().__init__(*args)
        self.message = message

    def __str__(self):
        return self.message


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='logs.log')

logger = logging.getLogger(__name__)


def log_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            message = f"Function: {func.__name__}: args: {args} kwargs: {kwargs} result: {result}"
            logger.info(message)

            return result
        except Exception as e:
            message = f"Function: {func.__name__}: {e}"
            logger.exception(message)
            raise FunctionExecutionError(message=message)

    return wrapper

@log_decorator
def nomsiz():
    text="""
    1.Register
    2.show
    3.exit
    """
    user_input = input('Enter a number: ')
    if user_input == '1':
        name = input('Enter your name: ')
        age = int(input('Enter your age: '))
        file_manager.add({'name': name, 'age': age})
        return nomsiz
    elif user_input == '2':
        alll = file_manager.read()
        print('Name - Age')
        for i in alll:
            print(f'{i["name"]} - {i["age"]}')
        return nomsiz()
    elif user_input == '3':
        return
    else:
        return nomsiz()

nomsiz()

