def main():
    tasks = []

    def addTask():
        task = input("Please enter a task: ")
        tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def updateTasks():
        if not tasks:
            print("There are no tasks currently.")
        else:
            print("Current Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")

    def deleteTask():
        try:
            taskToDelete = int(input("Enter the # to delete: "))
            if 0 <= taskToDelete < len(tasks):
                removed_task = tasks.pop(taskToDelete)
                print(f"Task '{removed_task}' has been removed.")
            else:
                print(f"Task #{taskToDelete} was not found.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        print("\nWelcome to the To-Do List app")
        print("1. Add Task")
        print("2. Update Tasks")
        print("3. Delete Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            updateTasks()
        elif choice == "3":
            deleteTask()
        elif choice == "4":
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid input. Please try again.")
        print("THANK YOU!")

if __name__ == "__main__":
    main()

            
