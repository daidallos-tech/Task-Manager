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
        
            
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task_object):
        self.tasks.append(task_object)
        print(f"Your '{task_object.title}' task was successfully created and added to your list!")
    
    def show_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task.title} — {task.description} [{task.status}]")