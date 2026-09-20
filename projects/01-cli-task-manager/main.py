from storage import (
  load_tasks,
  add_task,
  get_tasks,
  complete_task,
  delete_task,
  search_task,
)

def show_menu():
  print("\nTask Manager")
  print("1. Add task")
  print("2. List tasks")
  print("3. Search tasks")
  print("4. Complete task")
  print("5. Delete task")
  print("6. Exit")

def main():
  # Load saved tasks from the JSON
  load_tasks()

  while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
      title = input("Task title: ")
      task = add_task(title)
      print(f"Created: {task}")

    elif choice == "2":
      tasks = get_tasks()
      if not tasks:
        print("No tasks found.")
        continue
      for task in tasks:
        print(task)

    elif choice == "3":
      keyword = input("Search tasks: ")
      results = search_task(keyword)
      if not results:
        print("No tasks found.")
        continue
      for task in results:
        print(task)

    elif choice == "4":
      task_id = int(input("Task ID: "))
      task = complete_task(task_id)
      if task:
        print("Task completed!")
      else:
        print("Task not found.")

    elif choice == "5":
      task_id = int(input("Task ID: "))
      deleted = delete_task(task_id)
      if deleted:
        print("Task deleted!")
      else:
        print("Task not found.")

    elif choice == "6":
      print("Exiting...")
      break

    else:
      print("Invalid option.")

if __name__ == "__main__":
  main()