import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return[]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, title):
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        print(f'{task["id"]}. {status} {task["title"]}')

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            return True
    return False

tasks = load_tasks()

while True:
    print("Todo menu")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter a new task: ")
        add_task(tasks, title)
        print("Task added.")

    elif choice == "2":
        print("Current tasks: ")
        list_tasks(tasks)

    elif choice == "3":
        print("Current tasks: ")
        list_tasks(tasks)
        task_id = int(input("Enter task ID to mark complete: "))
        updated = complete_task(tasks, task_id)
        if updated:
            print("Task updated.")
        else:
            print("Task ID not found.")

    elif choice == "4":
        print("Goodbye!")
        break;

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")