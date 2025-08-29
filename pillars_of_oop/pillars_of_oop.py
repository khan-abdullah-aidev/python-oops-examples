# encapsulation_example.py
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}, new balance: {self.__balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}, remaining balance: {self.__balance}"
        return "Invalid withdraw amount"

    def get_balance(self):
        return self.__balance


# polymorphism_example.py
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

# function showing polymorphism
def animal_sound(animal):
    print(animal.speak())


# abstraction_example.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started."


# inheritance_example.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_details(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}"
