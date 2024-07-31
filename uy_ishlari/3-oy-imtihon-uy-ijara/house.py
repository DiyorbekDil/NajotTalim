from darsdagi_amaliyot.filemanager import house_manager
from user import User
from random import randint as rn


class House:
    def __init__(self, city, rooms, rental, owner_phone):
        self.city = city
        self.rooms = rooms
        self.rental = rental
        self.owner_phone = owner_phone
        self.iden_num = rn(0, 10_000)

    @staticmethod
    def have_house():
        houses = house_manager.read()
        active = User.active_user()
        for house in houses:
            if house['owner_phone'] == active['phone']:
                return True
        else:
            return False


def give_rent():
    # This function belongs to main_menu()
    city = input('Enter house city: ')
    try:
        rooms = int(input('Enter house rooms: '))
        rental = int(input('Enter house rental per month $: '))
    except ValueError:
        print('Their values must be number!')
        return give_rent()
    owner = User.active_user()
    house = House(city, rooms, rental, owner['phone'])
    house_manager.add(house.__dict__)
    print("Successfully added!")
    return True


def my_houses():
    # This function belongs to main_menu()
    if House.have_house():
        print("City - Rooms - Rental - Identity #")
        owner = User.active_user()
        houses = house_manager.read()
        for house in houses:
            if house['owner_phone'] == owner['phone']:
                print(f"{house['city']} - {house['rooms']} - "
                      f"{house['rental']} - {house['iden_num']}")
    else:
        print('You have no house yet!')


def delete_house():
    # This function belongs to main_menu()
    if House.have_house():
        try:
            idn = int(input('Enter house identity number: '))
        except ValueError:
            print('It must be a whole number!')
            return delete_house()
        owner = User.active_user()
        houses = house_manager.read()
        flag = False
        new_houses = []
        for house in houses:
            if house['owner_phone'] == owner['phone'] and house['iden_num'] == idn:
                flag = True
            else:
                new_houses.append(house)
        house_manager.write(new_houses)
        if flag:
            print('Successfully deleted')
        else:
            print('You have no such a house!')
    else:
        print('You have no house yet!')


def see_all():
    # This function belongs to main_menu()
    print("City - Rooms - Rental - Owner phone # - Identity #")
    houses = house_manager.read()
    for house in houses:
        print(f"{house['city']} - {house['rooms']} - {house['rental']}"
              f" - {house['owner_phone']} - {house['iden_num']}")


def search_by_rooms():
    # This function belongs to main_menu()
    try:
        num = int(input('Enter number of rooms>>> '))
    except ValueError:
        print('It must be a number!')
        return search_by_rooms()
    houses = house_manager.read()
    flag = False
    print("City - Rooms - Rental - Owner phone # - Identity #")
    for house in houses:
        if house['rooms'] == num:
            flag = True
            print(f"{house['city']} - {house['rooms']} - {house['rental']}"
                  f" - {house['owner_phone']} - {house['iden_num']}")
    if not flag:
        print('Not found, sorry!')


def get_all_cities():
    houses = house_manager.read()
    cities = []
    for house in houses:
        cities.append(house['city'])
    return set(cities)


def search_by_city():
    # This function belongs to main_menu()
    cities = get_all_cities()
    for city in cities:
        print(city, end=' ')
    print('')
    city = input('Choose one above: ')
    if city in cities:
        houses = house_manager.read()
        print("City - Rooms - Rental - Owner phone # - Identity #")
        for house in houses:
            if house['city'] == city:
                print(f"{house['city']} - {house['rooms']} - {house['rental']}"
                      f" - {house['owner_phone']} - {house['iden_num']}")
    else:
        print('Wrong choice!')
        return search_by_city()
