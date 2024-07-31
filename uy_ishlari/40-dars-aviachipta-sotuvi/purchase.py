from logging_file import log_decorator
from jsonManager import booked_flights, flight_manager
from user import User
from flight import decrement_ticket


class Purchase:
    def __init__(self, passport_id, gmail, name, phone, flight_time, from_airport):
        self.name = name
        self.phone = phone
        self.passport_id = passport_id
        self.gmail = gmail
        self.flight_time = flight_time
        self.from_airport = from_airport


@log_decorator
def buy_ticket():
    from_air = input('Enter from airport name: ')
    to_air = input('Enter to airport name: ')
    flight_time = input('Enter flight time H:M dd/mm/yyyy: ')
    all_flights = flight_manager.read()
    idx = 0
    while idx < len(all_flights):
        if all_flights[idx]['from_airport']['name'] == from_air and\
                        all_flights[idx]['to_airport']['name'] == to_air\
                        and all_flights[idx]['flight_time'] == flight_time\
                        and all_flights[idx]['status'] == '0'\
                        and all_flights[idx]['ticket'] > 0:
            gmail = input('Enter your gmail: ')
            passport = input('Enter passport ID: ')
            active_user = User.active_user()
            purchase = Purchase(passport, gmail, active_user['name'],
                                active_user['phone'], flight_time, from_air)
            decrement_ticket(all_flights[idx])
            booked_flights.add(purchase.__dict__)
            flight_manager.write(all_flights)
            print('Success')
            return
        idx += 1
    else:
        print('No such a flight or there is no ticket left')
        return


@log_decorator
def my_booked_tickets():
    all_booked = booked_flights.read()
    active_user = User.active_user()
    flag = False
    print('Name - Flight time - from airport')
    for p in all_booked:
        if p['phone'] == active_user['phone']:
            print(f'{p["name"]} - {p["flight_time"]} - {p["from_airport"]}')
            flag = True
    if not flag:
        print('You have no purchase!')
