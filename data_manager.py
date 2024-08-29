import json
import csv
from models import Task

class DataExporter:
    @staticmethod
    def export_json(file_path, tasks, notes):
        data = {
            'tasks': {date: [f"{task.time} - {task.description}" for task in tasks] 
                      for date, tasks in tasks.items()},
            'notes': notes
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def export_csv(file_path, tasks):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Time', 'Task'])
            for date, task_list in tasks.items():
                for task in task_list:
                    writer.writerow([date, task.time, task.description])

class DataImporter:
    @staticmethod
    def import_json(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        tasks = {date: [Task(date, task.split(' - ')[0], task.split(' - ')[1]) 
                        for task in tasks] 
                 for date, tasks in data['tasks'].items()}
        notes = data['notes']
        return tasks, notes

    @staticmethod
    def import_csv(file_path):
        tasks = {}
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            for row in reader:
                date, time, description = row
                if date not in tasks:
                    tasks[date] = []
                tasks[date].append(Task(date, time, description))
        return tasks