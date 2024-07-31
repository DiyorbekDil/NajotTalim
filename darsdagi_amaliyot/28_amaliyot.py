# class Bank:
#     def __init__(self, owner, deposit):
#         self.owner = owner
#         self.__deposit = deposit
#
#     def show_deposit(self):
#         return self.__deposit
#
#     def add_money(self, amount):
#         if amount>0:
#             self.__deposit+=amount
#             return 'Added'
#         else:
#             return "Please, enter positive number!"
#
#     def subtract_money(self, amount):
#         if amount>0 and (self.__deposit - amount)<=0:
#             return "You don\'t have enough money in your account number"
#         elif amount<0:
#             return "Please, enter positive number!"
#         else:
#             self.__deposit-=amount
#             return 'Get your money'
#
# dep1 = Bank('diyor', 1000)
# print(dep1.show_deposit())
# print(dep1.subtract_money(1200))
# print(dep1.add_money(344))
# print(dep1.show_deposit())
# print(dep1.subtract_money(200))
# print(dep1.show_deposit())

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book_name):
        if book_name in self.__books:
            return 'We have this book'
        else:
            self.__books.append(book_name)
            return 'Added'

    def get_book(self, book_name):
        if book_name in self.__books:
            self.__books.remove(book_name)
            return 'Enjoy reading the book'
        else:
            return 'We have no such a book'

    def show_books(self):
        print("Books:", end=' ')
        for b in self.__books:
            print(b, end=' ')
        print('')

lib1 = Library()
lib1.add_book('Fizika')
lib1.add_book('Python')
lib1.add_book('Matematika')
lib1.show_books()
print(lib1.get_book('Fizika'))
lib1.show_books()
print(lib1.get_book('Fizika asoslari'))
