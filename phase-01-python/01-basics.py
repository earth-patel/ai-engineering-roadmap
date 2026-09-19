name = "Earth"
age = 25
is_developer = True
salary = 10000.00
user = None

print(type(name))
print(type(age))
print(type(is_developer))
print(type(salary))
print(type(user))

if age >= 18:
  print("Adult")
elif age >= 13:
  print("Teenager")
else:
  print("Minor")

users = ["Alice", "Bob", "Charlie"]
for user in users:
  print(user)

for number in range(5):
  print(number)

count = 1
while count <= 5:
  print(count)
  count += 1

for number in range(10):
  if number == 6:
    break
  print(number)

for number in range(5):
  if number == 2:
    continue
  print(number)