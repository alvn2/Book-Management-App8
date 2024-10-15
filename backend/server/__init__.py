from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_club.db'
db = SQLAlchemy(app)

from  server import models

with app.app_context():
    db.create_all()

from server import routes