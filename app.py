from datetime import datetime

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
        self.history.append((datetime.now(), "DEPOSIT", amount))

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.history.append((datetime.now(), "WITHDRAW", amount))

    @property
    def balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.owner}: {self.__balance}$"
