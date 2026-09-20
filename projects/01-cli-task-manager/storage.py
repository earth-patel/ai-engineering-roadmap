import json
from pathlib import Path

from tasks import Task

DATA_FILE = Path("data/tasks.json")

tasks = []

def load_tasks():
  # We use the global keyword to indicate that we are referring to the global 'tasks' variable defined
  # outside of this function.
  global tasks

  # Create the data directory if it doesn't exist
  DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

  # Create JSON file if it doesn't exist
  if not DATA_FILE.exists():
    DATA_FILE.write_text("[]")
    tasks = []
    return

  try:
    data = json.loads(DATA_FILE.read_text())
    tasks = [
      Task(
        task_id=task_data["id"],
        title=task_data["title"],
        completed=task_data.get("completed", False)
      )
      for task_data in data
    ]
  except json.JSONDecodeError:
    print("Warning: tasks.json is invalid. Starting with an empty tasks.")
    tasks = []

def save_tasks():
  DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
  data = [
    {
      "id": task.id,
      "title": task.title,
      "completed": task.completed
    }
    for task in tasks
  ]
  DATA_FILE.write_text(json.dumps(data, indent=2))

def add_task(title):
  if tasks:
    task_id = max(task.id for task in tasks) + 1
  else:
    task_id = 1
  task = Task(
    task_id,
    title
  )
  tasks.append(task)
  save_tasks()
  return task

def get_tasks():
  return tasks

def complete_task(task_id):
  for task in tasks:
    if task.id == task_id:
      task.complete()
      save_tasks()
      return task
  return None

def delete_task(task_id):
  for task in tasks:
    if task.id == task_id:
      tasks.remove(task)
      save_tasks()
      return True
  return False

def search_task(keyword):
  keyword = keyword.lower()
  return [
    task
    for task in tasks
    if keyword in task.title.lower()
  ]