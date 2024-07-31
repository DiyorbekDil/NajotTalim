from fileManager import user_manager
from user import User
from teacher import Teacher
from student import Student


def add_teacher():
    name = input('Teacher name: ')
    password = User.hash_password(input('Password: '))
    subject = input('Subject: ')
    try:
        phone = int(input("Phone: "))
        experience = int(input('Experience: '))
    except ValueError:
        print('Phone and experience must be a whole number!')
        return add_teacher()
    teacher = Teacher(name, password, phone, subject, experience)
    user_manager.add(teacher.__dict__)
    print('Successfully added!')


def del_teacher():
    name = input('Teacher name: ')
    try:
        phone = int(input("Phone: "))
    except ValueError:
        print('Phone number must be a whole number!')
        return del_teacher()
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['name'] == name and all_users[idx]['phone'] == phone:
            del all_users[idx]
            user_manager.write(all_users)
            print('Deleted')
            return
        idx += 1
    else:
        print('No such a teacher')
        return


def show_teachers():
    all_users = user_manager.read()
    print('Name - Phone - Subject')
    for user in all_users:
        if user['kind'] == 'teacher':
            print(f'{user["name"]} - {user["phone"]} - {user["subject"]}')


def add_student():
    name = input('Student name: ')
    password = User.hash_password(input('Password: '))
    specialty = input('Specialty: ')
    try:
        phone = int(input("Phone: "))
        stage = int(input('Stage: '))
    except ValueError:
        print('Phone and stage must be a whole number!')
        return add_student()
    student = Student(name, password, phone, specialty, stage)
    user_manager.add(student.__dict__)
    print('Successfully added!')


def del_student():
    name = input('Student name: ')
    try:
        phone = int(input("Phone: "))
    except ValueError:
        print('Phone number must be a whole number!')
        return del_student()
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['name'] == name and all_users[idx]['phone'] == phone:
            del all_users[idx]
            user_manager.write(all_users)
            print('Deleted')
            return
        idx += 1
    else:
        print('No such a student')
        return


def show_students():
    all_users = user_manager.read()
    print('Name - Phone - Specialty')
    for user in all_users:
        if user['kind'] == 'student':
            print(f'{user["name"]} - {user["phone"]} - {user["specialty"]}')
