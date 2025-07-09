from repository import task_repo
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from kafka_event.kafka_producer.producer import publish_event

def add_task_controller(data):
    task = task_repo.create_task(data)
    publish_event("task_created", task.to_dict())
    return task

def update_task_controller(task_id, data):
    task = task_repo.update_task(task_id, data)
    publish_event("task_updated", task.to_dict())
    return task

def delete_task_controller(task_id):
    task = task_repo.get_task_by_id(task_id)
    task_repo.delete_task(task_id)
    publish_event("task_deleted", task.to_dict())
    return True

def get_tasks():
    return task_repo.get_all_tasks()
