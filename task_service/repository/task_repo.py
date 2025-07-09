from model.task_model import Task
from database.db import db

def create_task(data):
    task = Task(title=data["title"], description=data.get("description", ""))
    db.session.add(task)
    db.session.commit()
    return task

def get_all_tasks():
    return Task.query.all()

def get_task_by_id(task_id):
    return Task.query.get_or_404(task_id)

def update_task(task_id, data):
    task = Task.query.get_or_404(task_id)
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.completed = data.get("completed", task.completed)
    db.session.commit()
    return task

def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return True