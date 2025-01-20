# class is designed for Object-oriented Programming (OOP)
# class is a user-difined type
# Key Features of Python Classes:
# 1. Encapsulation: Bundling data and methods together.
# 2. Inheritance: Deriving new classes from existing ones.
# 3. Polymorphism: Using methods in different ways (e.g., overriding describe).
# 4. Abstraction: Hiding implementation details (using abstract classes).

# 1. Encapsulation Example
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. Remaining balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self):
        return self.__balance

# Creating a bank account
account = BankAccount(12345, 1000)
account.deposit(500)
account.withdraw(300)
print(f"Final balance: ${account.get_balance()}")

# 2. Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Using the classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

# 3. Polymorphism Example
class Shape:
    def area(self):
        pass  # Abstract method

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Calculating areas
shapes = [Rectangle(10, 5), Circle(7)]
for shape in shapes:
    print(f"Area: {shape.area()}")

# 4. Abstraction Example
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started.")

# Using the classes
vehicles = [Car(), Motorcycle()]
for vehicle in vehicles:
    vehicle.start_engine()

