from server import app, bcrypt, db
from server.models import Users
from flask import request, jsonify

@app.route('/')
def home():
    return '<h1>Home Page</h1>'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = Users(
        username = data['username'],
        email = data['email'],
        image_file = data['image_file'],
        password = hashed_password
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': f'Account created for {data["username"]}!'}), 201

@app.route('/login')
def login():
    return '<h1>Login Page</h1>'
