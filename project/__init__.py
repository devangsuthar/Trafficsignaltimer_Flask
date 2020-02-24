from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'test'

app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_RECORD_QUERIES'] = True

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/pythondb'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)

print("---in project---")

import project.com.controller
