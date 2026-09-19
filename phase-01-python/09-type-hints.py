# Without type hints
def add(a, b):
  return a + b

# With type hints
def add(a: int, b: int) -> int:
  return a + b

# List
def get_names() -> list[str]:
  return ["Alice", "Bob", "Charlie"]

# Dictionary
def get_user() -> dict[str, str]:
  return {"name": "Earth"}

# Optional
def find_user(user_id: int) -> dict | None:
  if user_id == 1:
    return {"name": "Earth"}
  else:
    return None