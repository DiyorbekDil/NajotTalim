import os
import json
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


class Team:
    """
    This is the class of Team
    where:
    name - name of a team
    captain - name of captain of a team
    members - names of members of a team
    """
    def __init__(self, name, captain, members: list, phone):
        self.name = name
        self.captain = captain
        self.members = members
        self.phone = phone
        self.time = dt.datetime.now().strftime("%d-%m-%Y")


admin_name = 'admin'  # username for admin
admin_password = 'password'  # password for admin

# This is JsonManager object to manage 'teams.json' file
# in which is kept information about teams
teams_manager = JsonManager('teams.json')


def apply_hackathon():
    # This function belongs to main_menu()
    try:
        num = int(input('Enter number of members in your team: '))
    except ValueError:
        print('Please, enter a whole number!')
        return apply_hackathon()
    if num < 3:
        print('There must be at least 3 people with captain in a team')
        return main_menu()
    else:
        captain = input('Enter captain name: ')
        members = []
        i = 1
        while i <= (num-1):
            member = input(f'Member-{i}: ')
            members.append(member)
            i += 1
        name = input('Enter the name of your team: ')
        phone = int(input('Enter your phone number: '))
        team = Team(name, captain, members, phone)
        teams_manager.add(team.__dict__)
        print('Success!')
        return main_menu()


def sign_in():
    # This function belongs to main_menu()
    login = input('Enter your username: ')
    password = input('Enter your password: ')
    if login == admin_name and password == admin_password:
        return admin_menu()
    else:
        print('No such a user')
        return main_menu()


def main_menu():
    text = '''
    1.Apply for hackathon
    2.Sign in
    3.Exit
    '''

    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        apply_hackathon()
    elif user_input == '2':
        sign_in()
    elif user_input == '3':
        return
    else:
        main_menu()


def show_teams():
    # This function belongs to admin_menu()
    print(f'Team name - captain name - phone number')
    teams = teams_manager.read()
    for team in teams:
        print(f'{team["name"]} - {team["captain"]} - {team["phone"]}')


def delete_team():
    # This function belongs to admin_menu()
    name = input('Enter the name of a team: ')
    try:
        phone = int(input('Enter team\'s phone number: '))
    except ValueError:
        print('Please, enter a whole number!')
        return delete_team()
    teams = teams_manager.read()
    flag = False
    idx = 0
    while idx < len(teams):
        if teams[idx]["name"] == name and teams[idx]["phone"] == phone:
            del teams[idx]
            flag = True
            break
        idx += 1
    if flag:
        teams_manager.write(teams)
        print('The team is deleted')
    else:
        print('No such a team')


def admin_menu():
    text = '''
    1.Show all teams
    2.Delete a team
    3.Back
    '''

    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        show_teams()
        admin_menu()
    elif user_input == '2':
        delete_team()
        admin_menu()
    elif user_input == '3':
        main_menu()
    else:
        admin_menu()


if __name__ == "__main__":
    main_menu()

