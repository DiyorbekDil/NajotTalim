import os, json
import hashlib
import datetime as dt

class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def check_existence(self):
        return os.path.exists(self.file_name)

    def read(self):
        if self.check_existence():
            if os.path.getsize(self.file_name) != 0:
                with open(self.file_name, 'r') as file:
                    data = json.load(file)
                    return data
            return []
        return []

    def write(self, all_data):
        with open(self.file_name, mode='w') as file:
            json.dump(all_data, file, indent=4)
            return "Data is added"

    def add(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        return self.write(all_data)



class Car:
    def __init__(self, model, trademark, price, color):
        self.model = model
        self.trademark = trademark
        self.price = price
        self.color = color



class Customer:
    def __init__(self, full_name, phone, password):
        self.full_name = full_name
        self.phone = phone
        self.password = password
        self.is_login = False

    def confirm_password(self, confirm_password):
        return self.password == confirm_password

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()



class Application:
    def __init__(self, full_name, phone, model):
        self.full_name = full_name
        self.phone = phone
        self.model = model
        self.time = dt.datetime.now().strftime("%d-%m-%Y")

    def info(self):
        return f'{self.full_name} - {self.model} - {self.time}'



cars_manager = JsonManager('cars.json')
customers_manager = JsonManager('customers.json')
applications_manager = JsonManager('applications.json')

admin_name = 'admin'
admin_password = 'admin'

def register():
    full_name = input('Enter your full name: ')
    phone = int(input('Enter your phone number: '))
    password = input('Enter your password: ')
    confirm_password = input('Re-enter your password ')

    customer = Customer(full_name, phone, password)
    if not customer.confirm_password(confirm_password):
        print('Passwords don\'t match')
        return register()
    customer.password = Customer.hash_password(customer.password)
    customers_manager.add(customer.__dict__)
    print('You have successfully registered on the site')
    return show_auth_menu()

def login():
    full_name = input('Enter your full name: ')
    password = input('Enter your password: ')
    if full_name == admin_name and password == admin_password:
        admin_menu()
    else:
        password = Customer.hash_password(password)
        all_customers = customers_manager.read()
        idx = 0
        while idx < len(all_customers):
            if all_customers[idx]['full_name'] == full_name and all_customers[idx]['password'] == password:
                all_customers[idx]['is_login'] = True
                customers_manager.write(all_customers)
                application_menu()
            idx += 1
        print('No such a user, try again!')
        return show_auth_menu()


def apply_purchase():
    model = input('Car model: ')
    price = int(input('Price: '))
    for car in cars_manager.read():
        if car['model'] == model and car['price'] == price:
            for customer in customers_manager.read():
                if customer['is_login']:
                    break
            application = Application(customer['full_name'], customer['phone'], model)
            applications_manager.add(application.__dict__)
            print("Application info: ", application.info())
            return application_menu()
    else:
        print('No such a car')
        return application_menu()


def find_application(phone):
    all_appl = applications_manager.read()
    data = []
    for appl in all_appl:
        if appl['phone'] == phone:
            data.append(appl)
    return data

def my_applications():
    for customer in customers_manager.read():
        if customer['is_login']:
            break
    for appl in find_application(customer['phone']):
        print(f'\n{appl["full_name"]} - {appl["model"]} - {appl["time"]}')
    return application_menu()
def show_cars():
    for car in cars_manager.read():
        print(f'\n{car["model"]} - {car["trademark"]} - {car["price"]}')

def log_out():
    all_customers = customers_manager.read()
    idx = 0
    while idx < len(all_customers):
        if all_customers[idx]['is_login']:
            all_customers[idx]['is_login'] = False
            customers_manager.write(all_customers)
            break
        idx += 1
def add_car():
    model = input('Car model: ')
    trademark = input('Car trademark: ')
    price = int(input('Price: '))
    color = input('Color: ')
    car = Car(model, trademark, price, color)
    cars_manager.add(car.__dict__)
    print("Added")
    admin_menu()

def delete_car():
    model = input('Car model: ')
    price = int(input('Price: '))
    all_cars = cars_manager.read()
    new_cars = []
    for car in all_cars:
        if car['model'] == model and car['price'] == price:
            continue
        new_cars.append(car)
    cars_manager.write(new_cars)
    admin_menu()

def admin_menu():
    text = '''
    1.Add car
    2.Delete car
    3.Show all cars
    4.Exit
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        add_car()
    elif user_input == '2':
        delete_car()
    elif user_input == '3':
        show_cars()
        admin_menu()
    elif user_input == '4':
        print('Have a nice mood!')
        return
    else:
        admin_menu()

def application_menu():
    text = '''
    1.Apply for purchase
    2.My applications
    3.Show all cars
    4.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        apply_purchase()
    elif user_input == '2':
        my_applications()
    elif user_input == '3':
        show_cars()
        application_menu()
    elif user_input == '4':
        log_out()
        show_auth_menu()
    else:
        application_menu()

def show_auth_menu():
    text = '''
    1.Register
    2.Login
    3.Exit
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        register()
    elif user_input == '2':
        login()
    elif user_input == '3':
        print('Have a nice mood!')
        return
    else:
        show_auth_menu()

show_auth_menu()