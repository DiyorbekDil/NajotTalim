# class FileHandler:
#     def read(self):
#         return 'This method handles all kinds of file!'
#
# class JsonHandler(FileHandler):
#     def read(self):
#         return 'This method handles only Json files!'
#
# class CSVHandler(FileHandler):
#     def read(self):
#         return 'This method handles only csv files!'
#
# class TXTHandler(FileHandler):
#     def read(self):
#         return 'This method handles only txt files!'
#
# all1 = FileHandler()
# print(all1.read())
# json1 = JsonHandler()
# print(json1.read())
# csv1 = CSVHandler()
# print(csv1.read())
# txt1 = TXTHandler()
# print(txt1.read())


# import json
# class DataFormatter:
#     def __init__(self, data):
#         self.data = data
#
#     def format(self):
#         return self.data
#
# class JsonFormatter(DataFormatter):
#     def __init__(self, data, file_name):
#         super().__init__(data)
#         self.file_name = file_name
#
#     def format(self):
#         with open(self.file_name, 'w', encoding='UTF-8') as file:
#             json.dump(self.data, fp=file)
#             return 'Success'
#
# class CSVFormatter(DataFormatter):
#     def __init__(self, data, file_name):
#         super().__init__(data)
#         self.file_name = file_name
#
#     def format(self):
#         with open(self.file_name, 'w', encoding='UTF-8') as file:
#             file.write(str(self.data))
#             return 'Success'
#
# class TxtFormatter(DataFormatter):
#     def __init__(self, data, file_name):
#         super().__init__(data)
#         self.file_name = file_name
#
#     def format(self):
#         with open(self.file_name, 'w', encoding='UTF-8') as file:
#             file.write(str(self.data))
#             return 'Success'
#
# data = {'ism':'diyor', 'yosh':20}
#
# dataf = DataFormatter(data)
# print(dataf.format())
#
# jsonf = JsonFormatter(data, 'data.json')
# print(jsonf.format())
#
# csvf = CSVFormatter(data, 'csvformatter.csv')
# print(csvf.format())
#
# txtf = TxtFormatter(data, 'txtf.txt')
# print(txtf.format())
import json
file_name = 'products.json'

def create_structure():
    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(obj=[], fp=file)
def read_file():
    with open(file_name, 'r', encoding='UTF-8') as file:
        return json.load(file)

def write_file(data):
    data = read_file()
    data.append(data)
    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(obj=data, fp=file, indent=4)

class Device:
    def __init__(self, name, price, typ='common'):
        self.name = name
        self.price = price
        self.typ = typ

    def add_to_file(self):
        data = {'type':self.typ, 'name':self.name, 'price':self.price}
        write_file(data)

    def get_total_price(self):
        pass

class Phone(Device):
    def __init__(self, name, price, memory, color, typ='phone'):
        super().__init__(name, price)
        self.typ = typ
        self.memory = memory
        self.color = color

    def add_to_file(self):
        data = {'type':self.typ, 'name':self.name, 'price':self.price, 'memory':self.memory, 'color':self.color}
        write_file(data)

    def get_total_price(self):
        pass

class Computer(Device):
    def __init__(self, name, price, year, made, typ='phone'):
        super().__init__(name, price)
        self.typ = typ
        self.year = year
        self.made = made

    def add_to_file(self):
        data = {'type':self.typ, 'name':self.name, 'price':self.price, 'made':self.made, 'year':self.year}
        write_file(data)

    def get_total_price(self):
        pass

create_structure()
dev1 = Device('tv', 120)
