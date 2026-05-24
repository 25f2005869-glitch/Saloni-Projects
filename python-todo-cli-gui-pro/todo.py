# To-Do List CLI App

from task_storage import load_tasks, save_tasks

# Load tasks from file (auto-migrates legacy plain-text lines)
tasks = load_tasks()

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    # Add Task
    if choice == "1":
        title = input("Enter new task: ")
        tasks.append({"title": title, "status": "Pending", "category": "Work"})
        save_tasks(tasks)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['title']} [{t['status']}] ({t['category']})")
        else:
            print("No tasks found.")

    # Delete Task
    elif choice == "3":
        if tasks:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['title']} [{t['status']}] ({t['category']})")

            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Task '{removed['title']}' deleted.")
            except:
                print("Invalid task number.")
        else:
            print("No tasks to delete.")

    # Exit
    elif choice == "4":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice. Try again.")
