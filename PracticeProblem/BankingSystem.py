# Banking System(Using abstraction in Module)
# Create a module name Bank.py
#Create an abstract class BankAccount
#Include :
"""Abstract method deposite(amount)
Normal method - show_message() -> prints "Transaction started
"""
#Implements
"""Deposite (amount) 
Create a normal method withdraw()"""
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance
    def show_message(self):
        print("Transaction started.")
    @abstractmethod
    def deposite(self, amount):
        pass
class SavingsAccount(BankAccount):
    def deposite(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")
S=SavingsAccount(1000)
S.show_message()
S.deposite(500)
S.withdraw(200)