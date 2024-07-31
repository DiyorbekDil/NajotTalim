class Car:
    def __init__(self, name, price, color, year, horse_power):
        self.name = name
        self.price = price
        self.color = color
        self.year = year
        self.horse_power = horse_power

    def __repr__(self):
        return f'{self.name} - {self.price}'


class Factory:
    def __init__(self, open_year, name):
        self.name = name
        self.open_year = open_year
        self.cars = []

    def __call__(self, *args):
        for arg in args:
            if isinstance(arg, Car):
                self.cars.append(arg)

kia = Factory(1999, 'KIA')
gm = Factory(1900, 'GM')

car1 = Car('Malibu', 20000, 'red', 2024, 200)
car2 = Car('k4', 20000, 'black', 2020, 189)
car3 = Car('k5', 45000, 'yellow', 2024, 250)
kia(car2, car3)
gm(car1)
print(kia.cars)
print(gm.cars)