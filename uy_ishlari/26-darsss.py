import os
import json
class Concert:
    def __init__(self, author, date, total_tickets, price, place, file_name):
        self.author = author
        self.date = date
        self.total_tickets = total_tickets
        self.price = price
        self.place = place
        self.file_name = file_name

    def get_price(self):
        return self.price

    def get_full_info(self):
        return (f'{self.author.title()} {self.date} sanasida {self.place}da konsert beradi. '
                f'Chipta narxi:{self.price}$, qolgan chiptalar:{self.total_tickets} dona!')

    def buy_ticket(self, full_name, phone_number, quantity):
        if os.path.exists(self.file_name):
            if self.available_tickets() == 0:
                return f'{full_name.title()} kechirasiz, chiptalarimiz tugadi!'
            elif quantity>self.available_tickets():
                return f'{full_name.title()} bizda o\'zi {self.available_tickets()} dona chipta qoldi!'
            else:
                temp = self.read_data()
                temp['full_name'].append(full_name)
                temp['phone_number'].append(phone_number)
                temp['quantity'].append(quantity)
                self.write_data(temp)
                return f'{full_name.title()} savdoyingiz uchun tashakkur!'
        else:
            return 'Qaydlar fayli mavjud emas!!!'
    def create_json_file(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, mode='w', encoding='UTF-8') as file:
                json.dump({'full_name':[], 'phone_number':[], 'quantity':[]}, fp=file)
            return 'Fayl muvaffaqiyatli yaratildi'
        else:
            return 'Bunday fayl allaqachon mavjud!'

    def available_tickets(self):
        return self.total_tickets - self.sold_tickets()
    def sold_tickets(self):
        temp = self.read_data()
        return sum(temp['quantity'])
    def read_data(self):
        with open(self.file_name, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def write_data(self, obj):
        with open(self.file_name, 'w', encoding='UTF-8') as file:
            json.dump(obj=obj, fp=file)

obj = Concert('botir qodirov','13-08-2024', 500,50,
                                       'Xalqlar do\'stligi','savdo.json')
print(obj.get_full_info())
print(obj.create_json_file())
print(obj.buy_ticket('diyor', 998971234567, 56))
print(obj.buy_ticket('diyorbek', 998978234567, 444))
print(obj.buy_ticket('otabek', 98978234567, 44))
print(obj.sold_tickets())
print(obj.available_tickets())