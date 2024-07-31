import json
def read_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        return json.load(file)

def write_to_file(file_name, data):
    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(obj=data, fp=file, indent=4)


class Teacher:
    file_name = "teachers.json"

    def create_json_structure(self):
        with open(self.file_name, mode='w', encoding='UTF-8') as file:
            json.dump([], fp=file)

    def add_to_file(self, full_name, phone_number, profession, age):
        data = read_from_file(self.file_name)
        data.append({'full_name':full_name, 'phone_number':phone_number, 'profession':profession, 'age':age})
        write_to_file(self.file_name, data)
        return 'Added'

    def get_info(self, phone_number):
        data = read_from_file(self.file_name)
        for r in data:
            if r['phone_number'] == phone_number:
                return "Teacher is " + r['full_name']
        return "No teacher found"

    def find_teacher(self, phone_number):
        data = read_from_file(self.file_name)
        for r in data:
            if r['phone_number'] == phone_number:
                return r
        return False

    def delete_teacher(self, teacher_phone_number):
        data = read_from_file(self.file_name)
        for r in range(len(data)):
            if data[r]['phone_number'] == teacher_phone_number:
                del data[r]
                write_to_file(self.file_name, data)
                return 'You are deleted from the list of teachers'
            else:
                return 'No such a teacher'



class Course:
    file_name = 'courses.json'

    def create_json_structure(self):
        with open(self.file_name, mode='w', encoding='UTF-8') as file:
            json.dump([], fp=file)

    def add_to_file(self, course_name, price, teacher_info):
        data = read_from_file(self.file_name)
        data.append({'course_name':course_name, 'price':price, 'teacher_info':teacher_info})
        write_to_file(self.file_name, data)
        return 'Added'

    def find_course(self, course_name):
        data = read_from_file(self.file_name)
        for r in data:
            if r['course_name'] == course_name:
                return r
        return False

    def delete_course(self, course_name):
        data = read_from_file(self.file_name)
        for r in range(len(data)):
            if data[r]['course_name'] == course_name:
                del data[r]
                write_to_file(self.file_name, data)
                return 'The course are deleted from the list of courses'
            else:
                return 'No such a course'



class Student:
    file_name = 'students.json'

    def create_json_structure(self):
        with open(self.file_name, mode='w', encoding='UTF-8') as file:
            json.dump([], fp=file)

    def register_to_course(self, name, email, phone, id, course_info):
        data = read_from_file(self.file_name)
        data.append({'student_name':name, 'email':email, 'phone':phone, 'id':id, 'course_info':course_info})
        write_to_file(self.file_name, data)
        return 'Added'

    def delete_from_course(self, student_name, course_name):
        data = read_from_file(self.file_name)
        for r in range(len(data)):
            if data[r]['student_name'] == student_name and data[r]['course_info']['course_name'] == course_name:
                del data[r]
                write_to_file(self.file_name, data)
                return 'You are deleted from the course'
            else:
                return 'No such a course or student'

    def find_nums_students(self, course_name):
        data = read_from_file(self.file_name)
        i = 0
        for r in data:
            if r['course_info']['course_name'] == course_name:
                i+=1
        if i != 0:
            return f'{i} student is studying this course'
        else:
            return f'{i} student is studying this course or no such a course!'



def show_menu():
    print("Welcome to menu!\n"
          f"Enter 1 if you are teacher\n"
          f"2 if you want to add a course to the platform\n"
          f"3 if you\'d like to sign up for a course\n"
          f"4 if you want to leave course\n"
          f"5 if you want to delete a course\n"
          f'6 if you want to delete a teacher\n'
          f'7 if you want to get number of students studying a particular course\n'
          f"Dial any other number to exit the platform")
    teacher = Teacher()
    teacher.create_json_structure()
    courses = Course()
    courses.create_json_structure()
    student = Student()
    student.create_json_structure()
    while True:
        user_input = int(input('Enter number: '))
        if user_input == 1:
            full_name = input("What is your full name: ")
            phone_number = int(input("Phone: "))
            profession = input("Profession: ")
            age = int(input("Age: "))
            result = teacher.add_to_file(full_name, phone_number, profession, age)
            print(result)
            print(teacher.get_info(phone_number))
        elif user_input == 2:
            course_name = input('What is the course name: ')
            price = int(input('What is the course price: '))
            teacher_phone_number = int(input('What is the course\'s teacher\'s phone number: '))
            teacher_info = teacher.find_teacher(teacher_phone_number)
            if teacher_info:
                result = courses.add_to_file(course_name, price, teacher_info)
                print(result)
            else:
                print('Given phone number is not available!')
        elif user_input == 3:
            name = input('Enter your name: ')
            email = input('Enter your email: ')
            phone = int(input('Enter your phone number: '))
            idv = int(input('Enter your id: '))
            chosen_course = input('Which course are you going to study? ')
            course_info = courses.find_course(chosen_course)
            if course_info:
                answer = student.register_to_course(name, email, phone, idv, course_info)
                print(answer)
            else:
                print('This course is not available!')
        elif user_input == 4:
            student_name = input('Enter your name: ')
            course_name = input('Enter the course name: ')
            result = student.delete_from_course(student_name, course_name)
            print(result)
        elif user_input == 5:
            course_name = input('Enter course name you want to delete: ')
            result = courses.delete_course(course_name)
            print(result)
        elif user_input == 6:
            t_phone = int(input('Enter teacher\'s phone number you want to delete from the list of teachers: '))
            outcome = teacher.delete_teacher(t_phone)
            print(outcome)
        elif user_input == 7:
            course_name = input('Enter a course name to get number of students studying this course: ')
            result = student.find_nums_students(course_name)
            print(result)
        else:
            break

show_menu()
