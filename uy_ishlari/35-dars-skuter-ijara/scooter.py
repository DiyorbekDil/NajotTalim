from fileManager import scooter_manager
from random import randint as rn


class Scooter:
    def __init__(self, charge, location, cost_per_min):
        self.charge = charge
        self.location = location
        self.cost_per_min = cost_per_min
        self.iden_num = rn(0, 1_000_0)

    @staticmethod
    def find_scooter(identity_number):
        all_ = scooter_manager.read()
        idx = 0
        while idx < len(all_):
            if all_[idx]['iden_num'] == identity_number:
                return all_[idx]
            idx += 1
        return False


def show_scooters():
    data = scooter_manager.read()
    print("Charge - location - cost per a minute - id")
    for scooter in data:
        print(f'{scooter["charge"]} - {scooter["location"]} - '
              f'{scooter["cost_per_min"]} - {scooter["iden_num"]}')


def add_scooter():
    try:
        charge = int(input('Enter scooter charge (km) >>> '))
        cost = int(input('Enter scooter cost per minute >>> '))
    except ValueError:
        print('Their values must be number!')
        return add_scooter()
    location = input('Enter scooter location >>> ')
    scooter = Scooter(charge, location, cost)
    scooter_manager.add(scooter.__dict__)
    print('Added')


def delete():
    idenum = int(input('Enter scooter identity number >>> '))
    all_scooters = scooter_manager.read()
    idx = 0
    while idx < len(all_scooters):
        if all_scooters[idx]['iden_num'] == idenum:
            del all_scooters[idx]
            scooter_manager.write(all_scooters)
            print('Deleted successfully!')
            return
        idx += 1
    print('No such a scooter')
    return

