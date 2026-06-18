from my_project.models.task import Task, TaskManager


manager = TaskManager()
def main_logic():
    while True:
        print("=== TASK MANAGER ===")
        user_input = input("Enter your choice\n1 - Create task\n2 - See task(s)\n3 - Delete task\n4 - Exit\nEnter: ")

        if user_input == "1":
            title_input = input("Enter a title of your task: ")
            description_input = input("Enter a description of your task: ")
            status_input = input("Enter a status of your task: ")

            try:
                new_task = Task(title=title_input, description=description_input, status=status_input)
                manager.add_task(new_task)
                manager.save_task()
                continue
            except ValueError as e:
                print(f"Error: {e}. Try again!")
        elif user_input == "2":
            print("=== CURRENT TASK ===")
            manager.show_tasks()
        elif user_input =="3":
            print("=== CURRENT TASK ===")
            manager.show_tasks()
            delete_input = int(input("Enter a number of task you want to delete: "))
            manager.delete_task(delete_input)
        elif user_input == "4":
            print("Close app...")
            break
        else:
            print("Invalid choice. Try again!")

