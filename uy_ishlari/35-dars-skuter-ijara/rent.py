from fileManager import rent_manager
from datetime import datetime as dt
from datetime import timedelta
from scooter import Scooter
from user import User


class Rent:
    def __init__(self, user: dict, scooter: dict):
        self.user = user
        self.scooter = scooter
        self.time = dt.now().strftime("%d/%m/%Y, %H:%M")


def rent_scooter():
    try:
        identity = int(input('Enter scooter identity number >>> '))
    except ValueError:
        print('It must be number!')
        return rent_scooter()
    scooter = Scooter.find_scooter(identity)
    if scooter is False:
        print('No such a scooter')
    else:
        user = User.active_user()
        rent = Rent(user, scooter)
        rent_manager.add(rent.__dict__)
        print('Rent successfully!')


def return_scooter():
    user = User.active_user()
    rents = rent_manager.read()
    idx = 0
    while idx < len(rents):
        if rents[idx]['user']['password'] == user['password']:
            cost = rents[idx]['scooter']['cost_per_min']
            time = dt.strptime(rents[idx]['time'], "%d/%m/%Y, %H:%M")
            now = dt.strptime(dt.now().strftime("%d/%m/%Y, %H:%M"), "%d/%m/%Y, %H:%M")
            diff = now - time
            diff_min = diff.seconds/60
            total_cost = diff_min*cost
            print('Cost>>>', total_cost)
            del rents[idx]
            rent_manager.write(rents)
            return
        idx += 1
    else:
        print('You have no scooter!')


