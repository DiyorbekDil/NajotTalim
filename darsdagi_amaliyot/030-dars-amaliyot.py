from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def age(self):
#         raise NotImplementedError('Not implemented')
#
#     @abstractmethod
#     def sound(self):
#         raise NotImplementedError('Not implemented')
#
# class Cat(Animal):
#     def age(self):
#         return 102
#
#     def sound(self):
#         return 'Miow'
#
#     def name(self):
#         return 'Bo\'rsiq'
#
# a1 = Cat()
# print(a1.sound())
# print(a1.name())
import os, json
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


class Course(ABC, JsonManager):
    def __init__(self, name, price, teacher):
        super().__init__(file_name="courses.json")
        self.name = name
        self.price = price
        self.teacher = teacher

    def parent_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "teacher": self.teacher,
            "users": []
        }

    @classmethod
    def register(self):
        raise NotImplementedError('Not implemented')

    @classmethod
    def cancel_register(self):
        raise NotImplementedError('Not implemented')

    @classmethod
    def show_users(self):
        raise NotImplementedError('Not implemented')

class Math(Course):
    def __init__(self, name, price, teacher, time):
        super().__init__(name, price, teacher)
        self.file_name = 'math.json'
        self.time = time

    def dict(self):
        data = self.parent_dict()
        data["time"] = self.time
        return data

    def add_to_file(self):
        return self.add(self.dict())

    def register(self):
        pass

    def cancel_register(self):
        pass

    def show_users(self):
        pass

class Dance(Course):
    def __init__(self, name, price, teacher, age):
        super().__init__(name, price, teacher)
        self.file_name = 'music.json'
        self.age = age

    def dict(self):
        data = self.parent_dict()
        data["age"] = self.age
        return data

    def add_to_file(self):
        return self.add(self.dict())

    def register(self):
        pass

    def cancel_register(self):
        pass

    def show_users(self):
        pass


class Music(Course):
    def __init__(self, name, price, teacher, type_music):
        super().__init__(name, price, teacher)
        self.type_music = type_music
        self.file_name = 'music.json'

    def dict(self):
        data = self.parent_dict()
        data["type_of_music"] = self.type_of_music
        return data

    def add_to_file(self):
        return self.add(self.dict())

    def register(self):
        pass

    def cancel_register(self):
        pass

    def show_users(self):
        pass