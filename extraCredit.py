"""
Kobe Dawes
I pledge my honor that I have abided by the stevens honor system. Kobe Dawes
"""
from datetime import date

today = date.today()


class Computer:

    def __init__(self, make, model, FOU, year):
        self.make = make
        self.model = model
        self.FOU = FOU
        self.year = year

    def age(self):
        d3 = today.strftime("%m/%d/%Y")
        curent = d3[-4:]
        diff = int(curent) - int(self.year)
        return diff


    def __str__(self):
        return f"{self.make}, {self.model}, {self.FOU}, {self.year}"
    def __repr__(self):
        return f"{self.make}, {self.model}, {self.FOU}, {self.year}"


'''my = Computer('Apple','Macbook Air', 'High', 2017)
print(my)
print(my.age())'''

box = list(range(10))
def square(l):
    for x in range(len(l)):
        l[x] = x**2
    return l
print(square(box))

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f'{self.title, self.author, self.price}'
    
    def __str__(self):
        return f'{self.title, self.author, self.price}'
    

class Inventory:
    def __init__(self, name, address, stock):
        self.name = name
        self.address = address
        self.stock = stock

    def addBook(self, book):
        stock = {}
        stock.update({"title":book.title, 'author': book.author, 'price': book.price})

    def __str__(self):
        return f"{self.name}, {self.address}, {self.stock}"
    def __repr__(self):
        return f"{self.name}, {self.address}, {self.stock}"


