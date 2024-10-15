from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_club.db'
db = SQLAlchemy(app)
bcrypt =  Bcrypt(app)
migrate = Migrate(app)

from  server import models

with app.app_context():
    db.create_all()

from server import routes