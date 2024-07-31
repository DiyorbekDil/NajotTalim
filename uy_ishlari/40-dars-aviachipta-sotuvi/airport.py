from jsonManager import airport_manager
from logging_file import log_decorator
from typing import Union


class Airport:
    def __init__(self, name, country):
        self.name = name
        self.country = country


@log_decorator
def add_airport():
    name = input('Enter airport name: ')
    country = input('Enter airport country: ')
    airport = Airport(name, country)
    airport_manager.add(airport.__dict__)
    print('Added')


@log_decorator
def remove_airport():
    name = input('Enter airport name: ')
    country = input('Enter airport country: ')
    all_airports = airport_manager.read()
    idx = 0
    while idx < len(all_airports):
        if all_airports[idx]['name'] == name and all_airports[idx]['country'] == country:
            del all_airports[idx]
            airport_manager.write(all_airports)
            print('Successfully removed')
            return
        idx += 1
    else:
        print('No such a airport!')
        return


@log_decorator
def show_airports():
    print('Name - Country')
    all_airports = airport_manager.read()
    for airport in all_airports:
        print(f'{airport["name"]} - {airport["country"]}')
    return


@log_decorator
def find_airport(name) -> Union[bool, dict]:
    all_airports = airport_manager.read()
    for airport in all_airports:
        if airport['name'] == name:
            return airport
    else:
        return False

