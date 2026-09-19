from calculator import add, subtract

def test_add():
  assert add(2, 3) == 5

def test_subtract():
  assert subtract(5, 3) == 2

# To run the tests, run the following command in your terminal:
# pytest
# pytest will find the files that has test_*.py or *_test.py and
# run the functions that start with test_ in those files.