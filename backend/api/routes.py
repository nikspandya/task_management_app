import logging
from flask import jsonify, request
from api import app, db
from api.models import Folder, Task, TaskPriority


@app.route('/', methods=['GET'])
def default_route():
    return jsonify({'message': 'Welcome to task management app'}), 200

# Folder route controllers


@app.route('/folder', methods=['POST'])
def add_folder():
    folder_name = request.json.get('folder_name', '')
    if folder_name != '':
        new_folder = Folder(folder_name=folder_name)
        db.session.add(new_folder)
        db.session.commit()
        return jsonify("folder_name: " + folder_name + " is created successfully"), 200
    else:
        return jsonify({'message': 'Please provide folder name'}), 500


@app.route('/folder/<id>', methods=['PUT'])
def update_folder(id):
    try:
        folder = Folder.query.get(id)
        folder_name = request.json['folder_name']
        folder.folder_name = folder_name
        db.session.commit()
        return jsonify("folder: " + str(folder.id) + " is updated successfully"), 200
    except Exception:
        logging.exception(
            "Could not update requested folder due to following error:")
        return jsonify({'message': "Folder update error"}), 500


@app.route('/folder/<id>', methods=['DELETE'])
def delete_folder(id):
    try:
        folder = Folder.query.get(id)
        tasks = Task.query.filter_by(folder_id=folder.id)
        for task in tasks:
            db.session.delete(task)
        db.session.delete(folder)
        db.session.commit()
        return jsonify("folder: " + str(folder.id) + " is deleted successfully"), 200
    except Exception:
        logging.exception(
            "Could not delete requested folder due to following error:")
        return jsonify({'message': "Folder delete error"}), 500

# Task route controllers


@app.route('/task', methods=['POST'])
def add_task():
    task_name = request.json.get('task_name', '')
    task_description = request.json.get('task_description', '')
    folder_id = request.json.get('folder_id', '')
    task_priority = request.json.get('task_priority', '')
    task_participant = request.json.get('task_participant', '')
    if task_priority == 'medium':
        priority = TaskPriority.MEDIUM
    elif task_priority == 'high':
        priority = TaskPriority.HIGH
    else:
        priority = TaskPriority.LOW

    new_task = Task(task_name=task_name, task_description=task_description,
                    priority=priority, task_participant=task_participant, folder_id=folder_id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify(task_name + " is created in the folder (id): " + str(folder_id)), 200


@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    try:
        task = Task.query.get(id)
        task_name = request.json.get('task_name', '')
        task_description = request.json.get('task_description', '')
        folder_id = request.json.get('folder_id', '')
        task_priority = request.json.get('task_priority', '')
        task_participant = request.json.get('task_participant', '')
        if task_priority == 'medium':
            priority = TaskPriority.MEDIUM
        elif task_priority == 'high':
            priority = TaskPriority.HIGH
        else:
            priority = TaskPriority.LOW

        task.priority = priority
        task.task_name = task_name
        task.task_description = task_description
        task.task_participant = task_participant
        task.folder_id = folder_id
        db.session.commit()
        return jsonify("task(id): " + str(task.id) + " is updated successfully"), 200
    except Exception:
        logging.exception(
            "Could not update task due to following error:")
        return jsonify({'message': "Update task error"}), 500


@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    try:
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify("task: " + str(task.id) + " is deleted"), 200
    except Exception:
        logging.exception(
            "Could not delete task due to following error:")
        return jsonify({'message': "Delete task error"}), 500


@app.route('/task', methods=['GET'])
def get_all_tasks():
    task_list = []
    all_task = Task.query.all()
    for task in all_task:
        tasks = ({'task_id': task.id, 'task_name': task.task_name,
                  'priority': task.priority.value, 'task_participants': task.task_participant, 'folder_id': task.folder_id, 'date_created': task.date_created})
        task_list.append(tasks)
    return jsonify({"all_task:": task_list}), 200
