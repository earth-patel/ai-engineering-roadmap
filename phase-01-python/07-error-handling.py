try:
  number = int(input("Enter a number: "))
except ValueError:
  print("Please enter a valid number.")

# Multiple exceptions
try:
  number = int(input("Enter a number: "))
  result = 100 / number
except ValueError:
  print("Invalid number.")
except ZeroDivisionError:
  print("Cannot divide by zero.")

# Finally block
try:
  print("Working...")
except Exception:
  print("Something went wrong.")
finally:
  print("Finished.")

# Raising exceptions
def withdraw(balance, amount):
  if amount > balance:
    raise ValueError("Insufficient funds.")
  return balance

withdraw(100, 150)  # This will raise a ValueError