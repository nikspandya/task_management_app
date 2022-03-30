from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
__author__ = 'nikspandya2@gmail.com'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init db
db = SQLAlchemy(app)

from api import routes
