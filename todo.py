def show_menu():
    print("\n=== To-Do App ===")
    print("1) Add task")
    print("2) View tasks")
    print("3) Delete task")
    print("4) Quit")


def add_task(tasks):
    task = input("Enter a task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append(task)
    print(f'Added: "{task}"')


def view_tasks(tasks):
    if not tasks:
        print("No tasks to view.")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)

    try:
        choice = input("Enter the task number to delete: ").strip()
        num = int(choice)

        if num < 1 or num > len(tasks):
            print("That task does not exist.")
        else:
            removed = tasks.pop(num - 1)
            print(f'Deleted: "{removed}"')

    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        pass
    finally:
        pass


def get_choice():
    try:
        choice = int(input("Choose an option (1-4): ").strip())
        return choice
    except ValueError:
        return None


def main():
    tasks = []
    print("Welcome to the To-Do List App!")

    while True:
        show_menu()
        choice = get_choice()

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()