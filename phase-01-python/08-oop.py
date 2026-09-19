# Classes and Objects
class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    return f"Hello {self.name}"

user = User("Alice", 30)
print(user)   # Output: <__main__.User object at 0x...>
print(user.age)   # Output: 30
print(user.greet())   # Output: Hello Alice

# Dataclasses
from dataclasses import dataclass

@dataclass
class Product:
  name: str
  price: float
  quantity: int
  country: str = "USA"  # Default value for country

product = Product("Laptop", 999.99, 5)
print(product)          # Output: Product(name='Laptop', price=999.99, quantity=5)
print(product.name)      # Output: Laptop

# Inheritance
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def introduce(self):
    print(f"Hi, my name is {self.name}")

class Employee(Person):
  def work(self):
    print(f"{self.name} is working.")
# Employee inherits from Person, so it has the same attributes and methods

employee = Employee("Bob", 25)
employee.introduce()   # Output: Hi, my name is Bob
employee.work()        # Output: Bob is working.

# Composition
class Engine:
  def start(self):
    print("Engine started.")

class Car:
  def __init__(self):
    self.engine = Engine()  # Car has an Engine

car = Car()
car.engine.start()   # Output: Engine started.

# Inheritance -> IS-A relationship example: Employee IS-A Person
# Composition -> HAS-A relationship example: Car HAS-A Engine