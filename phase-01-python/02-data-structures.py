# List
users = ["Earth", "John", "Sarah"]
print(users[0])  # Accessing the first element
print(users)
users.append("Mike")  # Adding a new element
print(users)
users.remove("John")  # Removing an element
print(users)
print(len(users))
for user in users:
  print(user)

# Tuple: A tuple is similar to a list, but it is immutable (cannot be changed after creation).
coordinates = (10.0, 20.0)
print(coordinates[0])  # Accessing the first element
# coordinates[0] = 15.0  # This will raise an error because tuples are immutable

# Set: A set stores unique values.
skills = {"Python", "Java", "C++", "Python"}  # Duplicate "Python" will be ignored
print(skills)
# Useful for things like:
skills1 = {"Python", "React", "AI"}
skills2 = {"Java", "Python", "AI"}
common = skills1.intersection(skills2)  # Finding common skills
print(common)

# Dictionary: A dictionary stores key-value pairs.
user = {
  "id": 1,
  "name": "Alice",
  "age": 30,
  "role": "developer",
}
print(user)
print(user["name"])  # Accessing a value by key
user["age"] = 31  # Updating a value
print(user["age"])
user["city"] = "New York"  # Adding a new key-value pair
print(user)
del user["city"]  # Removing a key-value pair
print(user)

for key, value in user.items():
  print(f"{key}: {value}")

# List of Dictionaries: A list can contain dictionaries, which is useful for storing multiple records.
users = [
  {"id": 1, "name": "Earth"},
  {"id": 2, "name": "John"},
  {"id": 3, "name": "Sarah"},
]
for user in users:
  if user["id"] == 2:
    print(user)

# List Comprehension: A concise way to create lists.
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
  squares.append(number ** 2)
print(squares)

# Using list comprehension
squares = [number ** 2 for number in numbers]
print(squares)