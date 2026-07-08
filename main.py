import json

FILE_NAME = "tasks.json"


def show_menu():
    print("\n===== TO DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Mark Completed")
    print("6. Exit")


def get_user_input():
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']}")


def view_tasks(tasks):
    display_tasks(tasks)


def add_task(tasks):
    task = input("Enter your task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    for existing_task in tasks:
        if existing_task["title"].lower() == task.lower():
            print("Task already exists.")
            return

    tasks.append({
        "title": task,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully!")


def delete_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    display_tasks(tasks)

    while True:
        try:
            task_number = int(input("Which task do you want to delete? "))

            if task_number not in range(1, len(tasks) + 1):
                print("Invalid choice.")
                continue

            tasks.pop(task_number - 1)
            save_tasks(tasks)

            print("Task deleted successfully!")
            break

        except ValueError:
            print("Invalid choice.")


def edit_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    display_tasks(tasks)

    while True:
        try:
            task_number = int(input("Which task do you want to edit? "))

            if task_number not in range(1, len(tasks) + 1):
                print("Invalid choice.")
                continue

            new_title = input("Enter the new title: ").strip()

            if not new_title:
                print("Task title cannot be empty.")
                continue

            duplicate = any(
                task["title"].lower() == new_title.lower()
                for task in tasks
                if task != tasks[task_number - 1]
            )

            if duplicate:
                print("Task already exists.")
                continue

            tasks[task_number - 1]["title"] = new_title

            save_tasks(tasks)

            print("Task updated successfully!")
            break

        except ValueError:
            print("Invalid choice.")


def mark_completed(tasks):
    if not tasks:
        print("No tasks found.")
        return

    display_tasks(tasks)

    while True:
        try:
            task_number = int(input("Which task do you want to mark as completed? "))

            if task_number not in range(1, len(tasks) + 1):
                print("Invalid choice.")
                continue

            if tasks[task_number - 1]["completed"]:
                print("Task already completed!")
                return

            tasks[task_number - 1]["completed"] = True

            save_tasks(tasks)

            print("Task marked as completed!")
            break

        except ValueError:
            print("Invalid choice.")


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def main():
    tasks = load_tasks()

    while True:
        show_menu()

        user_input = get_user_input()

        if user_input == 1:
            view_tasks(tasks)

        elif user_input == 2:
            add_task(tasks)

        elif user_input == 3:
            delete_task(tasks)

        elif user_input == 4:
            edit_task(tasks)

        elif user_input == 5:
            mark_completed(tasks)

        elif user_input == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()