tasks = []


def menu_list():
    print("\n --- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


def view_tasks(task_list):
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\nYour Tasks: ")
        for i in range(len(tasks)):
            print(str(i+1) + ". " + tasks[i])

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    view_tasks()
    if len(tasks) == 0:
        return

    try:
        num = int(input("Enter task number to remove:  "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print("Removed: ", removed)
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

while True:
    menu_list()
    choice = input("Choose an option (1-4):  ")

    if choice == "1":
        view_tasks()
    elif choice ==  "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break 
    else:
        print("Invalid choice, try again.")        