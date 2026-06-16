from task import Task, TaskManager


manager = TaskManager()
def main_logic():
    while True:
        print("=== TASK MANAGER ===")
        user_input = input("Enter your choice\n1 - Create task\n2 - See task(s)\n3 - Exit\nEnter: ")

        if user_input == "1":
            title_input = input("Enter a title of your task: ")
            description_input = input("Enter a description of your task: ")
            status_input = input("Enter a status of your task: ")

            try:
                new_task = Task(title=title_input, description=description_input, status=status_input)
                manager.add_task(new_task)
                continue
            except ValueError as e:
                print(f"Error: {e}. Try again!")
        elif user_input == "2":
            manager.show_tasks()
        elif user_input =="3":
            print("Close app...")
            break
        else:
            print("Invalid choice. Try again!")

