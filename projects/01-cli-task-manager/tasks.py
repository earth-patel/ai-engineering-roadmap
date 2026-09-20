class Task:
  def __init__(self, task_id, title, completed=False):
    self.id = task_id
    self.title = title
    self.completed = completed

  def complete(self):
    self.completed = True

  def __str__(self):
    status = "Completed" if self.completed else "Pending"
    return f"{self.id}. {self.title} - {status}"