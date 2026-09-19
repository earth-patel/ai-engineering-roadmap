def add(a, b):
  return a + b

result = add(5, 3)
print(result)  # Output: 8

def greet(name):
  print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

def greet_with_default(name="Guest"):
  print(f"Hello, {name}!")

greet_with_default()  # Output: Hello, Guest!

def get_user():
  return "Earth", 25

name, age = get_user()
print(name)  # Output: Earth
print(age)  # Output: 25

# *args: Useful when the number of arguments isn't fixed.
def add_all(*numbers):
  total = 0
  for number in numbers:
    total += number
  return total

print(add_all(1, 2, 3, 4))  # Output: 10

# **kwargs: Useful when you want to handle named arguments that you haven't defined in advance.
def create_user(**data):
  print(data)

create_user(name="Alice", age=30, city="New York")