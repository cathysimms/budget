from abc import ABC, abstractmethod

class Budget(ABC):
    def __init__(self, name, balance = 0):
        self.cat_name = name
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, amount, category):
        self.withdraw(amount)
        category.deposit(amount)

class Category(Budget):
    def __init__(self, name, balance=0):
        super().__init__(name, balance)

food = Category("food", 100)
clothing = Category("clothing", 20)
print(food.getBalance())
food.deposit(10)
print(food.balance)
food.transfer(100, clothing)
print(food.balance)
print(clothing.balance)
