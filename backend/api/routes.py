import logging
from flask import jsonify, request
from api import app, db
from api.models import Project, Task


@app.route("/", methods=["GET"])
def default_route():
    return jsonify({"message": "Welcome to task management app"}), 200


# Project endpoits
@app.route("/projects", methods=["GET"])
def get_all_projects():
    """
    Get request to this endpoint gives list of existing Projects
    """
    project_list = []
    all_projects = Project.query.all()
    for project in all_projects:
        projects = {
            "project_id": project.id,
            "project_name": project.project_name,
            "date_created": project.date_created,
        }
        project_list.append(projects)
    return jsonify({"All_projects:": project_list}), 200


@app.route("/project", methods=["POST"])
def add_project():
    try:
        project_name = request.json.get("project_name", "")
        if project_name != "":
            new_project = Project(project_name=project_name)
            db.session.add(new_project)
            db.session.commit()
            return (
                jsonify(project_name + " is created successfully"),
                200,
            )
        else:
            return jsonify({"message": "Please provide valid project name"}), 500
    except Exception:
        logging.exception("Could not create project due to following error:")
        return (
            jsonify({"message": "Project adding error, project may alrady exist!"}),
            500,
        )


@app.route("/project/<id>", methods=["DELETE"])
def delete_project(id):
    try:
        project = Project.query.get(id)
        tasks = Task.query.filter_by(project_name=project.project_name)
        logging.info(tasks)
        for task in tasks:
            db.session.delete(task)
        db.session.delete(project)
        db.session.commit()
        return (
            jsonify(project.project_name + " is deleted successfully"),
            200,
        )
    except Exception:
        logging.exception("Could not delete requested project due to following error:")
        return jsonify({"message": "Project delete error"}), 500


# Task endpoints
@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    """
    Get request to this endpoint gives list of existing Tasks
    """
    task_list = []
    all_task = Task.query.all()
    for task in all_task:
        tasks = {
            "task_id": task.id,
            "task_name": task.task_name,
            "project_name": task.project_name,
            "date_created": task.date_created,
        }
        task_list.append(tasks)
    return jsonify({"All_task:": task_list}), 200


@app.route("/task", methods=["POST"])
def add_task():
    try:
        task_name = request.json.get("task_name", "")
        task_description = request.json.get("task_description", "")
        project_name = request.json.get("project_name", "")

        if project_name:
            new_task = Task(
                task_name=task_name,
                task_description=task_description,
                project_name=project_name,
            )
            db.session.add(new_task)
            db.session.commit()
            return (
                jsonify(task_name + " is created in the " + project_name),
                200,
            )
        else:
            return jsonify({"message": "Please provide valid project name"}), 500
    except Exception:
        logging.exception("Could not create task due to following error:")
        return jsonify({"message": "Task adding error, task may alrady exsist!"}), 500


@app.route("/task/<id>", methods=["PUT"])
def update_task(id):
    try:
        task = Task.query.get(id)
        task_name = request.json.get("task_name", "")
        task_description = request.json.get("task_description", "")
        project_name = request.json.get("project_name", "")

        task.task_name = task_name
        task.task_description = task_description
        task.project_name = project_name
        db.session.commit()
        return jsonify(task_name + " is updated successfully"), 200
    except Exception:
        logging.exception("Could not update task due to following error:")
        return jsonify({"message": "Update task error"}), 500


@app.route("/task/<id>", methods=["DELETE"])
def delete_task(id):
    try:
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify(task.task_name + " is deleted successfully"), 200
    except Exception:
        logging.exception("Could not delete task due to following error:")
        return jsonify({"message": "Delete task error"}), 500
