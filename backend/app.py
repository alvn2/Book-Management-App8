from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_club.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(20), nullable=False)

@app.route('/')
def home():
    return '<h1>Home Page</h1>'

@app.route('/register')
def register():
    return '<h1>Register Page</h1>'

@app.route('/login')
def login():
    return '<h1>Login Page</h1>'

if __name__ == '__main__':
    app.run(debug=True)