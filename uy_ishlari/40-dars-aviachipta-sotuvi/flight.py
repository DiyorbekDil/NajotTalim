from jsonManager import flight_manager
from logging_file import log_decorator
from plane import find_plane
from airport import find_airport


class Flight:
    def __init__(self, plane, from_airport, to_airport, flight_time, landing_time,
                 ticket, price, status='0'):
        self.plane = plane
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.flight_time = flight_time
        self.landing_time = landing_time
        self.status = status
        self.ticket = ticket
        self.price = price


@log_decorator
def add_flight():
    while True:
        try:
            ticket = int(input('Enter flight number of tickets available: '))
            price = int(input('Enter flight price of a ticket: '))
            break
        except ValueError:
            print('They must be a whole number!')

    name_plane = find_plane(input('Enter name of plane: '))
    from_air = find_airport(input('Enter from airport name: '))
    to_air = find_airport(input('Enter to airport name: '))
    if name_plane and from_air and to_air:
        flight_time = input('Enter flight time H:M dd/mm/yyyy: ')
        landing_time = input('Enter landing time H:M dd/mm/yyyy: ')
        status = input('Enter flight status 0 for actual/ 1 for ended:  ')
        flight = Flight(name_plane, from_air, to_air, flight_time, landing_time, ticket, price, status)
        flight_manager.add(flight.__dict__)
        print('Added')
        return
    print('You entered plane or airport name wrong, try again!')
    return add_flight


@log_decorator
def show_flights():
    all_flights = flight_manager.read()
    print('Plane - From - To - Tickets - Status - Flight time')
    for flight in all_flights:
        print(f'{flight["plane"]["name"]} - {flight["from_airport"]["name"]}'
              f' - {flight["to_airport"]["name"]} - {flight["ticket"]} - {flight["status"]}'
              f' - {flight["flight_time"]}')
        return


@log_decorator
def return_desired_flights(from_air, to_air):
    all_flights = (flight_manager.read())
    desired_flights = []
    for flight in all_flights:
        if flight["from_airport"]["name"] == from_air and flight["to_airport"]["name"] == to_air and \
                flight['status'] == '0':
            desired_flights.append(flight)
    return desired_flights


@log_decorator
def search_flights_by():
    from_air = input('Enter from airport: ')
    to_air = input('Enter to airport: ')
    all_flights = (flight_manager.read())
    desired_flights = return_desired_flights(from_air, to_air)
    if not desired_flights:
        print('Not found!')
        return
    else:
        print('Plane - From - To - Tickets - Ticket price - Flight time')
        for flight in all_flights:
            print(f'{flight["plane"]["name"]} - {flight["from_airport"]["name"]}'
                  f' - {flight["to_airport"]["name"]} - {flight["ticket"]} - {flight["price"]}'
                  f' - {flight["flight_time"]}')
            return


@log_decorator
def decrement_ticket(flight: dict):
    flight['ticket'] -= 1
    return flight

