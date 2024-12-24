import name


def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. Remove a specific task")
    print("3. Mark a task as completed")
    print("4. Display all tasks")
    print("5. Display completed tasks")
    print("6. Remove all tasks")
    print("7. Sort tasks alphabetically")
    print("8. Exit")

def add_task(task_list):
    task = input("Enter the task: ").strip()
    if task:
        task_list.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def remove_task(task_list):
    task = input("Enter the task to remove: ").strip()
    for t in task_list:
        if t["task"] == task:
            task_list.remove(t)
            print(f"Task '{task}' removed.")
            return
    print(f"Task '{task}' not found.")

def mark_completed(task_list):
    task = input("Enter the task to mark as completed: ").strip()
    for t in task_list:
        if t["task"] == task:
            t["completed"] = True
            print(f"Task '{task}' marked as completed.")
            return
    print(f"Task '{task}' not found.")

def display_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("\nAll Tasks:")
        for idx, t in enumerate(task_list, start=1):
            status = "Completed" if t["completed"] else "Pending"
            print(f"{idx}. {t['task']} - {status}")

def display_completed_tasks(task_list):
    completed_tasks = [t["task"] for t in task_list if t["completed"]]
    if not completed_tasks:
        print("No completed tasks.")
    else:
        print("\nCompleted Tasks:")
        for idx, task in enumerate(completed_tasks, start=1):
            print(f"{idx}. {task}")

def remove_all_tasks(task_list):
    task_list.clear()
    print("All tasks removed.")

def sort_tasks(task_list):
    task_list.sort(key=lambda t: t["task"].lower())
    print("Tasks sorted alphabetically.")

def main():
    task_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            remove_task(task_list)
        elif choice == "3":
            mark_completed(task_list)
        elif choice == "4":
            display_tasks(task_list)
        elif choice == "5":
            display_completed_tasks(task_list)
        elif choice == "6":
            remove_all_tasks(task_list)
        elif choice == "7":
            sort_tasks(task_list)
        elif choice == "8":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if name == "main":
    main()