class Course:
    def __init__(self, subject, price, period):
        self.subject = subject
        self.price = price
        self.period = period

    def __repr__(self):
        return f'{self.subject} - {self.price}'


class Student:
    def __init__(self, full_name, age, birthday, gender):
        self.full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.courses = []

    def __str__(self):
        return self.full_name.title()

    def __call__(self, *args):
        for course in args:
            if isinstance(course, Course):
                self.courses.append(course)

    def __len__(self):
        return len(self.courses)

    def __getitem__(self, item):
        try:
            return self.courses[item]
        except:
            print('List index out of range')

    def __setitem__(self, key, value: Course):
        try:
            if isinstance(value, Course):
                self.courses[key] = value
        except:
            print('List assignment index out of range')

    def __add__(self, other):
        if isinstance(other, Course) and (other not in self.courses):
            self.courses.append(other)
        new = Student(self.full_name, self.age, self.birthday, self.gender)
        new.courses = self.courses
        return new

    def __sub__(self, other):
        while other in self.courses:
            self.courses.remove(other)
        new = Student(self.full_name, self.age, self.birthday, self.gender)
        new.courses = self.courses
        return new

    def __truediv__(self, other):
        self.age /= other
        new = Student(self.full_name, self.age, self.birthday, self.gender)
        new.courses = self.courses
        return new

    def __mul__(self, other):
        self.age *= other
        new = Student(self.full_name, self.age, self.birthday, self.gender)
        new.courses = self.courses
        return new

    def __iadd__(self, other):
        if isinstance(other, Course) and (other not in self.courses):
            self.courses.append(other)
        return self

    def __isub__(self, other):
        while other in self.courses:
            self.courses.remove(other)
        return self

    def __itruediv__(self, other):
        self.age /= other
        return self

    def __imul__(self, other):
        self.age *= other
        return self

    def __pow__(self, power, modulo=None):
        return len(self.courses)**power



stu1 = Student('diyorbek isoqov', 20, '09.06.2004', 'male')

cr1 = Course('Dasturlash', 100, 6)
cr2 = Course('Fizika', 200, 12)
cr3 = Course('English', 200, 18)

print(dir(stu1))

stu1(cr1, cr2, cr1)
print(stu1.courses)

# print(stu1)
#
# print(len(stu1))
#
# print(stu1[1])
#
# stu1[0] = cr2
# print(stu1.courses)

# stu1 += cr3
# print(stu1.courses)
#
# stu1 -= cr1
# print(stu1.courses)
#
# stu1 *= 4
# print(stu1.age)
#
# stu1 /= 5
# print(stu1.age)

#print(stu1**3)

# new_obj = stu1 + cr3
# print(new_obj.courses)
#
# new_obj = stu1 - cr3
# print(new_obj.courses)
#
# new_obj = stu1/4
# print(new_obj.age)
#
# new_obj = stu1*12
# print(new_obj.age)
