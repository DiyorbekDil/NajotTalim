from user import login, logout
from admin import add_teacher, del_teacher, show_teachers
from admin import add_student, del_student, show_students
from group import add_student_group, del_group, create_group, show_groups
from subject import create_subject, del_subject, show_subjects
from lesson import add_lesson, show_lessons
from teacher import show_actual_lessons, show_ended_lessons, grade_students
from student import show_actual_student_lessons, show_my_grades, show_my_grades_by_subject


def auth_menu():
    text = """
    1.Log-in
    2.Exit
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        result = login()
        if result == 1:
            return admin_menu()
        elif result == 2:
            return teacher_menu()
        elif result == 3:
            return student_menu()
        else:
            print('No such a user!')
            return auth_menu()
    elif user_input == '2':
        return
    else:
        print('Unexpected character!')
        return auth_menu()


def admin_menu():
    text = '''
    1.Subject (CRUD)
    2.Teacher (CRUD)
    3.Group (CRUD)
    4.Student (CRUD)
    5.Add lesson
    6.Show lessons table
    7.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        return manage_subjects()
    elif user_input == '2':
        return manage_teachers()
    elif user_input == '3':
        return manage_groups()
    elif user_input == '4':
        return manage_students()
    elif user_input == '5':
        add_lesson()
        admin_menu()
    elif user_input == '6':
        show_lessons()
        admin_menu()
    elif user_input == '7':
        return auth_menu()
    else:
        print('Unexpected character!')
        return admin_menu()


def teacher_menu():
    # Will be launched soon
    text = '''
    1.Show my actual lessons
    2.Start lesson and grade students
    3.Show my ended lessons
    4.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        show_actual_lessons()
        teacher_menu()
    elif user_input == '2':
        grade_students()
        teacher_menu()
    elif user_input == '3':
        show_ended_lessons()
        teacher_menu()
    elif user_input == '4':
        logout()
        auth_menu()
    else:
        print('Unexpected character!')
        return manage_subjects()


def student_menu():
    # this function will be launched soon
    text = '''
    1.Show my actual lessons
    2.Show my grades
    3.Show my grade by subject
    4.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        show_actual_student_lessons()
        student_menu()
    elif user_input == '2':
        show_my_grades()
        student_menu()
    elif user_input == '3':
        show_my_grades_by_subject()
        student_menu()
    elif user_input == '4':
        logout()
        auth_menu()
    else:
        print('Unexpected character!')
        return manage_subjects()


def manage_subjects():
    # This function belongs to admin_menu()
    text = '''
        1.Create subject
        2.Delete subject
        3.Show all subjects
        4.Back
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        create_subject()
        manage_subjects()
    elif user_input == '2':
        del_subject()
        manage_subjects()
    elif user_input == '3':
        show_subjects()
        manage_subjects()
    elif user_input == '4':
        return admin_menu()
    else:
        print('Unexpected character!')
        return manage_subjects()


def manage_teachers():
    # This function belongs to admin_menu()
    text = '''
        1.Create teacher
        2.Delete teacher
        3.Show all teachers
        4.Back
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        add_teacher()
        manage_teachers()
    elif user_input == '2':
        del_teacher()
        manage_teachers()
    elif user_input == '3':
        show_teachers()
        manage_teachers()
    elif user_input == '4':
        return admin_menu()
    else:
        print('Unexpected character!')
        return manage_teachers()


def manage_groups():
    # This function belongs to admin_menu()
    text = '''
        1.Create group
        2.Delete group
        3.Show all groups
        4.Add a student to a group
        5.Back
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        create_group()
        manage_groups()
    elif user_input == '2':
        del_group()
        manage_groups()
    elif user_input == '3':
        show_groups()
        manage_groups()
    elif user_input == '4':
        add_student_group()
        manage_groups()
    elif user_input == '5':
        return admin_menu()
    else:
        print('Unexpected character!')
        return manage_groups()


def manage_students():
    # This function belongs to admin_menu()
    text = '''
        1.Create student
        2.Delete student
        3.Show all students
        4.Back
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        add_student()
        manage_students()
    elif user_input == '2':
        del_student()
        manage_students()
    elif user_input == '3':
        show_students()
        manage_students()
    elif user_input == '4':
        return admin_menu()
    else:
        print('Unexpected character!')
        return manage_students()


auth_menu()
