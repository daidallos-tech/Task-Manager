import json
from pathlib import Path

class Task:
    def __init__(self, title, description, status) -> None:
        if len(title) > 25:
            raise ValueError("Title of your task cannot be more than 25 symbols!")
        
        if not title.strip():
            raise ValueError("Title cannot be empty")
        
        if not description.strip():
            raise ValueError(f"Description cannot be empty")
        
        self.title = title
        self.description = description
        self.status = status
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }
        
            
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, task_object):
        self.tasks.append(task_object)
        print(f"Your '{task_object.title}' task was successfully created and added to your list!")
        print()
    
    def show_tasks(self, mode='all'):
        if mode == 'done':
            filtered_tasks = [task for task in self.tasks if task.status == 'done']
        elif mode == 'in':
            filtered_tasks = [task for task in self.tasks if task.status == 'in']
        else:
            filtered_tasks = self.tasks
        
        if not filtered_tasks:
            print("You don't have any tasks")
            return
        
        for idx, task in enumerate(filtered_tasks, 1):
            print(f"{idx}. {task.title} — {task.description} [{task.status}]")
    
    def delete_task(self, number: int):
        task_index = number - 1

        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task.title}' was deleted!")
            self.save_task()
        else:
            print("Incorrect number of task!Try again!")
    
    def save_task(self):
        file_path = Path("data/database.json")

        task_to_save = [task.to_dict() for task in self.tasks]

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(task_to_save, file, ensure_ascii=False, indent=4)
        print("Your data was saved!")


    def load_tasks(self):
        file_path = Path("data/database.json")

        if file_path.exists():
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    loaded_list = json.load(file)
                    self.tasks = []
                    for task_data in loaded_list:
                        task_obj = Task(**task_data)
                        self.tasks.append(task_obj)
                print("Data loaded successfully!")
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Error: {e}. Try again!")
        else:
            print("Database not found")
        
