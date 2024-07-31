from JSONManager import JsonManager

class Product(JsonManager):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.type = 'common'
        self.__sum = 0

    def convert_to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'type': self.type
        }

    def add_to_file(self):
        self.add_one_data(self.convert_to_dict())

    def calculate_total_price(self):
        products = self.read_json_file()
        for product in products:
            self.__sum += product['price']
        return self.__sum

    def show_data(self):
        products = self.read_json_file()
        for product in products:
            for key, value in product.items():
                print(f'{key} - {value}')
            print('')


class Electronics(Product):
    def __init__(self, name, price, made_in, year):
        super().__init__(name, price)
        self.made_in = made_in
        self.year = year
        self.type = 'electronics'
        self.__sum = 0

    def convert_to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'made_in': self.made_in,
            'year': self.year,
            'type': self.type
        }

    def add_to_file(self):
        self.add_one_data(self.convert_to_dict())

    def calculate_total_price(self):
        products = self.read_json_file()
        for product in products:
            if product['type'] == self.type:
                self.__sum += product['price']
        return self.__sum

    def show_data(self):
        products = self.read_json_file()
        for product in products:
            if product['type'] == self.type:
                for key, value in product.items():
                    print(f'{key} - {value}')
                print('')


class Book(Product):
    def __init__(self, name, price, pages):
        super().__init__(name, price)
        self.pages = pages
        self.type = 'book'
        self.__sum = 0

    def convert_to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'pages': self.pages,
            'type': self.type
        }

    def add_to_file(self):
        self.add_one_data(self.convert_to_dict())

    def calculate_total_price(self):
        products = self.read_json_file()
        for product in products:
            if product['type'] == self.type:
                self.__sum += product['price']
        return self.__sum

    def show_data(self):
        products = self.read_json_file()
        for product in products:
            if product['type'] == self.type:
                for key, value in product.items():
                    print(f'{key} - {value}')
                print('')


class Clothing(Product):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color
        self.type = 'clothing'
        self.__sum = 0

    def convert_to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'color': self.color,
            'type': self.type
        }

    def add_to_file(self):
        self.add_one_data(self.convert_to_dict())

    def calculate_total_price(self):
        products = self.read_json_file()
        for product in products:
            if product['type'] == self.type:
                self.__sum += product['price']
        return self.__sum

    def show_data(self):
        products = self.read_json_file()
        for product in products:
            if product['type'] == self.type:
                for key, value in product.items():
                    print(f'{key} - {value}')
                print('')

prod1 = Product(name='shkaf', price=500000)
prod1.add_to_file()

elect1 = Electronics('generator', 2_000_000, 2024, 2027)
elect1.add_to_file()

book1 = Book('fizika', 70_000, 450)
book1.add_to_file()

book2 = Book('matematika', 80_000, 400)
book2.add_to_file()

cloth1 = Clothing('kostyum-shim', 1_000_000, 'qora')
cloth1.add_to_file()

cloth2 = Clothing('trainers', 300_000, 'plain')
cloth2.add_to_file()

prod1.show_data()

print(prod1.calculate_total_price())
cloth2.show_data()
print(cloth2.calculate_total_price())
print(book2.calculate_total_price())