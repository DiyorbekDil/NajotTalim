from abc import ABC, abstractmethod
import os, json


class JsonManager:
    file_name = 'reports.json'

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


class Shape(ABC, JsonManager):
    @abstractmethod
    def get_area(self):
        raise NotImplementedError('You must implement get_area method!')

    @abstractmethod
    def get_perimeter(self):
        raise NotImplementedError('You must implement get_perimeter method!')


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.type = 'rectangle'

    def calculate_area(self):
        return {
            'type': self.type,
            'height': self.height,
            'width': self.width,
            'area': self.height*self.width
        }

    def get_area(self):
        print(f'The rectangle\'s area -> {self.calculate_area()["area"]}')

    def calculate_perimeter(self):
        return {
            'type': self.type,
            'height': self.height,
            'width': self.width,
            'perimeter': 2 * (self.height + self.width)
        }

    def get_perimeter(self):
        print(f'The rectangle\'s perimeter -> {self.calculate_perimeter()["perimeter"]}')

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14
        self.type = 'circle'

    def calculate_area(self):
        return {
            'type': self.type,
            'radius': self.radius,
            'pi': self.pi,
            'area': self.pi*(self.radius**2)
        }

    def get_area(self):
        print(f'The circle\'s area -> {self.calculate_area()["area"]}')

    def calculate_perimeter(self):
        return {
            'type': self.type,
            'radius': self.radius,
            'pi': self.pi,
            'perimeter': 2*self.pi*self.radius
        }

    def get_perimeter(self):
        print(f'The circle\'s perimeter -> {self.calculate_perimeter()["perimeter"]}')

def menu():
    jm = JsonManager()
    print(f'Enter 1 if you want to calculate area of a circle\n'
          f'2 if you want to calculate perimeter of a circle\n'
          f'3 if you want to calculate area of a rectangle\n'
          f'4 if you want to calculate perimeter of a rectangle\n'
          f'5 if you want to see all the calculations you did\n'
          f'any other number to leave the program\n')
    while True:
        user_input = int(input('Enter a number: '))
        if user_input == 1:
            radius = float(input('Enter radius of a circle: '))
            c1 = Circle(radius)
            c1.add(c1.calculate_area())
            c1.get_area()
        elif user_input == 2:
            radius = float(input('Enter radius of a circle: '))
            c1 = Circle(radius)
            c1.add(c1.calculate_perimeter())
            c1.get_perimeter()
        elif user_input == 3:
            h = float(input('Enter height of a rectangle: '))
            w = float(input('Enter width of a rectangle: '))
            r1 = Rectangle(h, w)
            r1.add(r1.calculate_area())
            r1.get_area()
        elif user_input == 4:
            h = float(input('Enter height of a rectangle: '))
            w = float(input('Enter width of a rectangle: '))
            r1 = Rectangle(h, w)
            r1.add(r1.calculate_perimeter())
            r1.get_perimeter()
        elif user_input == 5:
            for i in jm.read():
                for key, value in i.items():
                    print(f'{key} -> {value}')
                print('')
        else:
            break

#menu()
import datetime as dt
print(type(dt.date.today()))

