from user import User
from typing import Union
from fileManager import user_manager, lesson_manager, group_manager
from datetime import datetime as dt


class Teacher(User):
    def __init__(self, name, password, phone, subject, experience):
        super().__init__(name, password, phone)
        self.subject = subject
        self.experience = experience
        self.kind = 'teacher'


def find_teacher(name):
    all_users = user_manager.read()
    for user in all_users:
        if user['name'] == name and user['kind'] == 'teacher':
            return True
    else:
        return False


def find_lessons():
    active = User.active_user()['name']
    lessons = lesson_manager.read()
    temp = []
    for lesson in lessons:
        if lesson['teacher'] == active:
            temp.append(lesson)
    return temp


def show_actual_lessons():
    current = dt.now().strftime("%H:%M %d/%m/%Y")
    now_datetime = dt.strptime(current, "%H:%M %d/%m/%Y")
    temp = find_lessons()
    flag = False
    if temp:
        for lesson in temp:
            lesson_date = dt.strptime(lesson['start_time'], "%H:%M %d/%m/%Y")
            if lesson_date > now_datetime:
                print(f'{lesson["group"]} - {lesson["subject"]} - {lesson["start_time"]}')
                flag = True
        if not flag:
            print('You do not have any actual lesson')
    else:
        print('You do not have any lesson')


def show_ended_lessons():
    current = dt.now().strftime("%H:%M %d/%m/%Y")
    now_datetime = dt.strptime(current, "%H:%M %d/%m/%Y")
    temp = find_lessons()
    flag = False
    if temp:
        for lesson in temp:
            lesson_date = dt.strptime(lesson['end_time'], "%H:%M %d/%m/%Y")
            if lesson_date < now_datetime:
                print(f'{lesson["group"]} - {lesson["subject"]} - {lesson["start_time"]}')
                flag = True
        if not flag:
            print('You do not have any ended lesson')
    else:
        print('You do not have any lesson')


def return_students(group) -> Union[list, bool]:
    groups = group_manager.read()
    for grou in groups:
        if grou['name'] == group:
            return grou['students']
    return False


def grade_students():
    group = input('Enter group name: ')
    start_time = input('Enter lesson\'s start time: ')
    students = return_students(group)
    lessons = lesson_manager.read()
    if students:
        idx = 0
        while idx < len(lessons):
            if lessons[idx]['group'] == group and lessons[idx]['start_time'] == start_time:
                for student in students:
                    grade = input(f'Grade {student["name"]}>>> ')
                    pair = {"student_name": student["name"],
                            "student_grade": grade}
                    lessons[idx]['grades'].append(pair)
            idx += 1
        lesson_manager.write(lessons)
        print('Added!')
    else:
        print('No such a group or lesson!')



