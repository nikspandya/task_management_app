import enum
from datetime import datetime
from api import db


class TaskPriority(enum.Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


class Folder(db.Model):
    """
    db model class for folders
    folder class has relationship with task using backref
    """
    __tablename__ = 'folder'
    id = db.Column(db.Integer, primary_key=True)
    folder_name = db.Column(db.String(20), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='folder')


class Task(db.Model):
    """
    db model class for tasks
    """
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=False, nullable=False)
    task_description = db.Column(db.String(2000), unique=False, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    priority = db.Column(db.Enum(TaskPriority), nullable=False)
    task_participant = db.Column(db.PickleType, nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))
