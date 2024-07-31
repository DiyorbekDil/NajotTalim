from random import randint
from logging_file import log_decorator
from jsonManager import plane_manager
from typing import Union


class Plane:
    def __init__(self, name, capacity):
        self.id_num = randint(0, 1_000_000)
        self.name = name
        self.capacity = capacity


@log_decorator
def add_plane():
    name = input('Enter plane name: ')
    while True:
        try:
            capacity = int(input('Enter plane capacity: '))
            break
        except ValueError:
            print('Capacity must be a whole number!')

    plane = Plane(name, capacity)
    plane_manager.add(plane.__dict__)
    print('Added')


@log_decorator
def remove_plane():
    while True:
        try:
            id_num = int(input('Enter plane identical number: '))
            break
        except ValueError:
            print('Plane ID must be a whole number!')

    all_planes = plane_manager.read()
    idx = 0
    while idx < len(all_planes):
        if all_planes[idx]['id_num'] == id_num:
            del all_planes[idx]
            plane_manager.write(all_planes)
            print('Successfully removed')
            return
        idx += 1
    else:
        print('No such a plane!')
        return


@log_decorator
def show_planes():
    print('ID - Name - Capacity')
    all_planes = plane_manager.read()
    for plane in all_planes:
        print(f'{plane["id_num"]} - {plane["name"]} - {plane["capacity"]}')
    return


@log_decorator
def find_plane(name) -> Union[bool, dict]:
    all_planes = plane_manager.read()
    for plane in all_planes:
        if plane['name'] == name:
            return plane
    else:
        return False
