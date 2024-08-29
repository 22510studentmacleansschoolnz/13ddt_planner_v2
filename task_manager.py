import json
import os
from models import Task

class TaskManager:
    def __init__(self, username):
        self.username = username
        self.tasks = self.load_tasks()

    def load_tasks(self):
        filename = f'{self.username}_tasks.json'
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                task_data = json.load(f)
                return {date: [Task(date, task.split(' - ')[0], task.split(' - ')[1]) 
                               for task in tasks] 
                        for date, tasks in task_data.items()}
        return {}

    def save_tasks(self):
        task_data = {date: [f"{task.time} - {task.description}" for task in tasks] 
                     for date, tasks in self.tasks.items()}
        with open(f'{self.username}_tasks.json', 'w') as f:
            json.dump(task_data, f)

    def add_task(self, task):
        if task.date not in self.tasks:
            self.tasks[task.date] = []
        self.tasks[task.date].append(task)
        self.save_tasks()

    def remove_task(self, task):
        if task.date in self.tasks:
            self.tasks[task.date] = [t for t in self.tasks[task.date] if t.description != task.description]
            if not self.tasks[task.date]:
                del self.tasks[task.date]
            self.save_tasks()

    def modify_task(self, old_task, new_task):
        self.remove_task(old_task)
        self.add_task(new_task)