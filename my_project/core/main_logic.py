from my_project.models.task import Task, TaskManager


manager = TaskManager()
def main_logic():
    while True:
        print("=== TASK MANAGER ===")
        user_input = input("Enter your choice\n1 - Create task\n2 - See task(s)\n3 - Delete task\n4 - Update task's status\n5 - Exit\nEnter: ")

        if user_input == "1":
            print()
            title_input = input("Enter a title of your task: ")
            description_input = input("Enter a description of your task: ")
            #status_input = input("Enter a status of your task: ")
            print()

            try:
                new_task = Task(title=title_input, description=description_input)
                manager.add_task(new_task)
                manager.save_task()
                continue
            except ValueError as e:
                print(f"Error: {e}. Try again!")
            print()
        
        elif user_input == "2":
            print()
            tasks_filter = input("Enter a choice 1 - show all tasks, 2 - show tasks in process, 3 - show done tasks\nEnter: ")
            if tasks_filter == "1":
                print()
                print("=== ALL TASKS ===")
                manager.show_tasks(mode='all')
            elif tasks_filter == "2":
                print()
                print("=== TASKS IN PROCESS ===")
                manager.show_tasks(mode='in')
            elif tasks_filter == "3":
                print()
                print("=== DONE TASKS ===")
                manager.show_tasks(mode='done')
            else:
                print("Invalid choice! Try again!")
            print()
        
        elif user_input =="3":
            print()
            print("=== CURRENT TASKS ===")
            try:
                manager.show_tasks()
                delete_input = int(input("Enter a number of task you want to delete: "))
                manager.delete_task(delete_input)
            except ValueError:
                print("Your input has to be a number! Try again!")
            print()
        elif user_input == "4":
            print()
            print("=== CURRENT TASKS ===")
            try:
                manager.show_tasks()
                update_input = int(input("Enter a number of task you want to update: "))
                manager.update_status(update_input)
            except ValueError:
                print("Your input has to be a number! Try again!")
            print()
        elif user_input == "5":
            print()
            print("Close app...")
            print()
            break
        else:
            print()
            print("Invalid choice. Try again!")
            print()

