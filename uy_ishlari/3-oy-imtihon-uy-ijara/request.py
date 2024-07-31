from darsdagi_amaliyot.filemanager import house_manager, request_manager
from user import User
from house import House


class Request:
    def __init__(self, name, phone, house_info: dict):
        self.name = name
        self.phone = phone
        self.house_info = house_info


def leave_request():
    # This function belongs to main_menu()
    try:
        owner_phone = int(input('Enter house\'s owner\'s phone number: '))
        idn = int(input('Enter house identity number: '))
    except ValueError:
        print('Please, enter whole number!')
        return leave_request()
    houses = house_manager.read()
    for house in houses:
        if house['iden_num'] == idn and house['owner_phone'] == owner_phone:
            active = User.active_user()
            request = Request(active['name'], active['phone'], house)
            request_manager.add(request.__dict__)
            print('Successfully left!')
            return
    else:
        print('No such a house!')
        return


def see_requests():
    # This function belongs to main_menu()
    if House.have_house():
        active = User.active_user()
        requests = request_manager.read()
        flag = False
        print('Who? - Phone # - Where your house? - House identity #')
        for request in requests:
            if request['house_info']['owner_phone'] == active['phone']:
                print(f'{request["name"]} - {request["phone"]} - '
                      f'{request["house_info"]["city"]} - {request["house_info"]["iden_num"]}')
                flag = True
        if not flag:
            print('Not yet!')
    else:
        print('You have no house yet!')
