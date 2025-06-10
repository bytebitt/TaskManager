from typing import List
from colorama import Fore, init, Style
import json

init(autoreset=True)

FILENAME = 'user_tasks.json'


def load_tasks() -> List[dict[str, object]]:
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks() -> None:
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)


tasks: List[dict[str, object]] = load_tasks()


def add_task() -> None:
    """
    Prompts the user to enter a new task and adds it to the global task list.

    If the task already exists, the user is asked whether to add it anyway.

    Returns:
        None

    """

    task = input(f"{Fore.WHITE}Enter your task\n{Fore.BLUE}>>> ")

    if not any(t['title'] == task for t in tasks):
        tasks.append({"title": task, "done": False})
        save_tasks()
        print(f"{Fore.GREEN}\nTask Successfully Added\n")
    else:
        print(
            f"{Fore.YELLOW}This task is currently in the task list, add it anyway? (y/n)")

        answer = input(f"{Fore.BLUE}>>> ")

        if answer.lower() == 'y':
            tasks.append({"title": task, "done": False})
            save_tasks()
            print(f"\n{Fore.GREEN}Task Successfully Added\n")
        elif answer.lower() == 'n':
            print("...")


def mark_task() -> None:
    """
    Prompts the user to enter a task number and sets its 'done' status to True.

    If the task doesn't exist, the function shows an error warning.

    Returns:
        None
    """

    try:
        display_tasks()
        print('')
        task = int(
            input(f"{Fore.WHITE}Enter task number to mark it as completed\n{Fore.BLUE}>>> ")) - 1

        if 0 <= task < len(tasks):
            tasks[task]['done'] = True
            save_tasks()
            print(f"{Fore.GREEN}\nTask successfully Marked\n")
        else:
            print(f"{Fore.RED}\nTask doesn't exist in your tasks list\n")
    except ValueError:
        print(f"{Fore.RED}\nIncorrect input\n")


def delete_task() -> None:
    """
    Prompts the user to enter a task number and deletes the corresponding task from the global tasks list.

    Displays the current list of tasks before prompting.

    Handles invalid input (non-integer or out-of-range values) with error messages.

    Returns:
        None

    """

    try:
        display_tasks()
        print('')
        task = int(
            input(f"{Fore.WHITE}Enter task number to delete it\n{Fore.BLUE}>>> ")) - 1

        if 0 <= task < len(tasks):
            tasks.pop(task)
            save_tasks()
            print(f"{Fore.GREEN}\nTask successfully deleted\n")
        else:
            print(f"{Fore.RED}\nTask doesn't exist in your tasks list\n")
    except ValueError:
        print(f"{Fore.RED}\nIncorrect input.\n")


def display_tasks() -> None:
    """
    Displays all tasks in the global tasks list with their numbering.

    If a task's 'done' status is True, its title is shown with a strikethrough effect.

    If there are no tasks, prints a message indicating the list is empty.

    Returns:
        None
    """

    if tasks:
        for i, task in enumerate(tasks, start=1):
            title = task['title']
            if task['done'] == True:
                title = f"\x1b[9m{title}\x1b[0m"
            print(f"{i}. {title}")
    else:
        print("List is Empty")


def main():
    while True:
        print(f'{Fore.BLUE}-------- MENU --------')
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Display all Task")
        print("5. Clear Tasks List")
        print("6. Exit")

        choice = input(f"{Fore.BLUE}>>> {Fore.WHITE}")

        match choice:
            case '1':
                add_task()
            case '2':
                mark_task()
            case '3':
                delete_task()
            case '4':
                display_tasks()
            case '5':
                if tasks:
                    print(
                        f"{Fore.YELLOW}Are you sure you want delete all tasks? (y/n)")
                    confirmation = input(f"{Fore.BLUE}>>> {Fore.WHITE}")
                    if confirmation.lower() == 'y':
                        tasks.clear()
                        print(f"{Fore.GREEN}\nTasks successfully deleted\n")
                    else:
                        print("...")
                else:
                    print("List is Empty")
            case '6':
                break
            case _:
                print(f"{Fore.RED}\nIncorrect Input.\n")


if __name__ == '__main__':
    main()
