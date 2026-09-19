import requests

# GET: Commonly used to retrieve a data.
response = requests.get('https://jsonplaceholder.typicode.com/users')
print(response)  # <Response [200]>

# POST: Commonly used to create a new data.
user = {
  "name": "Earth",
  "email": "earth@example.com",
}
response = requests.post('https://jsonplaceholder.typicode.com/users', json=user)
# json=user - This tells the requests library to send the user data as JSON
print(response)  # <Response [201]>
print(response.json())  # {'name': 'Earth', 'email': 'earth@example.com', 'id': 11}

# PUT: Commonly used to replace an existing data.
user = {
  "name": "Earth",
  "email": "earth@example.com",
}
response = requests.put('https://jsonplaceholder.typicode.com/users/1', json=user)
print(response)  # <Response [200]>
print(response.json())  # {'name': 'Earth', 'email': 'earth@example.com', 'id': 1}

# PATCH: Commonly used to partially update an existing data.
data = {
  "email": "newemail@example.com",
}
response = requests.patch('https://jsonplaceholder.typicode.com/users/1', json=data)
print(response)  # <Response [200]>
print(response.json())  # {'name': 'Leanne Graham', 'email': 'newemail@example.com', ...}

# DELETE: Commonly used to delete an existing data.
response = requests.delete('https://jsonplaceholder.typicode.com/users/1')
print(response)  # <Response [200]>

# API headers: Headers are used to provide additional information about the request or response.
headers = {
  "Authorization": "Bearer your_token_here",
}
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url, headers=headers, timeout=5)  # timeout is optional, but recommended

# FastAPI: FastAPI is used to create APIs in Python.
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
  return {"message": "Hello, World!"}