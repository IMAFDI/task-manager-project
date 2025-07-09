from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from controller import task_controller

task_bp = Blueprint("task_bp", __name__)

@task_bp.route("/", methods=["GET"])
def index():
    tasks = task_controller.get_tasks()
    return render_template("index.html", tasks=tasks)

@task_bp.route("/add-task", methods=["POST"])
def add_task_form():
    data = {
        "title": request.form["title"],
        "description": request.form.get("description", "")
    }
    task_controller.add_task_controller(data)
    return redirect(url_for("task_bp.index"))

@task_bp.route("/update-task/<int:task_id>", methods=["POST"])
def update_task_form(task_id):
    new_status = request.form.get("completed") == "True"
    task_controller.update_task_controller(task_id, {"completed": new_status})
    return redirect(url_for("task_bp.index"))

@task_bp.route("/delete-task/<int:task_id>", methods=["POST"])
def delete_task_form(task_id):
    task_controller.delete_task_controller(task_id)
    return redirect(url_for("task_bp.index"))
