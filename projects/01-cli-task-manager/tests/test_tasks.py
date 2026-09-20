from tasks import Task

def test_create_task():
  task = Task(1, "Test Task")

  assert task.id == 1
  assert task.title == "Test Task"
  assert task.completed is False

def test_complete_task():
  task = Task(1, "Test Task")
  task.complete()

  assert task.completed is True

def test_task_string():
  task = Task(1, "Test Task")
  task_str = str(task)

  assert task_str == "1. Test Task - Pending"

def test_completed_task_string():
  task = Task(1, "Test Task")
  task.complete()
  task_str = str(task)

  assert task_str == "1. Test Task - Completed"