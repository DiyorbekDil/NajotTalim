from random import randint
from fileManager import subject_manager


class Subject:
    def __init__(self, name, period):
        self.name = name
        self.period = period
        self.iden_num = randint(0, 100_000)


def create_subject():
    name = input('Enter subject name: ')
    try:
        period = int(input('Subject period (# of terms): '))
    except ValueError:
        print('Period must be a whole number')
        return create_subject()
    subject = Subject(name, period)
    subject_manager.add(subject.__dict__)
    print('Added')


def del_subject():
    name = input('Enter subject name: ')
    all_subjects = subject_manager.read()
    flag = True
    new = []
    for subject in all_subjects:
        if subject['name'] == name:
            flag = False
            continue
        new.append(subject)
    subject_manager.write(new)
    if flag:
        print('Not such a subject')
    else:
        print('Deleted!')


def show_subjects():
    all_subjects = subject_manager.read()
    print('Name - Identity number - Period')
    for subject in all_subjects:
        print(f'{subject["name"]} - {subject["iden_num"]} - {subject["period"]}')


def find_subject(name):
    all_subjects = subject_manager.read()
    for subject in all_subjects:
        if subject['name'] == name:
            return True
    else:
        return False
