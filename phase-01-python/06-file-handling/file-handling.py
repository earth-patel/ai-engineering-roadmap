with open("notes.txt", "r") as file:
  content = file.read()

print(content)
# Output:
# Learn Python
# Learn FastAPI
# Learn AI

with open("notes.txt", "w") as file:
  file.write("This is a new note.")

with open("notes.txt", "r") as file:
  content = file.read()

print(content)
# Output:
# This is a new note.

# JSON file handling
import json

user = {
  "name": "John Doe",
  "age": 30,
}

# Convert Python → JSON
json_data = json.dumps(user)
print(json_data)

# Convert JSON → Python
python_data = json.loads(json_data)
print(python_data)

# CSV file handling
import csv

with open("data.csv", "r") as file:
  reader = csv.DictReader(file)

  for row in reader:
    print(row)