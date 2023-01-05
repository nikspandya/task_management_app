from datetime import datetime
from api import db


class Project(db.Model):
    """
    db model class for project
    project class has relationship with task using backref
    """

    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(20), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    tasks = db.relationship("Task", backref="project")


class Task(db.Model):
    """
    db model class for tasks
    """

    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=False, nullable=False)
    task_description = db.Column(db.String(2000), unique=False, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    project_name = db.Column(db.Integer, db.ForeignKey("project.project_name"))
