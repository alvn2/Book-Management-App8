from server import app, bcrypt, db
from server.models import Users, Bookclub
from flask import request, jsonify
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    return '<h1>Home Page</h1>'

@app.route('/register', methods=['POST', 'GET'])
def register():
    data = request.get_json()

    if Users.query.filter_by(email=data['email']).first():
        return jsonify({'errors': {'email': 'Email already registered. please choose a different one'}}), 400

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

@app.route('/login', methods=['POST', 'GET'])
def login():
    data = request.get_json()

    user = Users.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': f'User {user.username} logged in successfully!'}), 200
    else:
        return jsonify({'message': 'Login failed, please check your email or password.'}), 401
    
@app.route('/logout')
def logout():
    logout_user()
    return jsonify({'message': 'User logged out successfully!'}), 200

@app.route('/New-bookclub', methods=['POST', 'GET'])
@login_required
def add_bookclub():
    data = request.get_json()

    bookclub = Bookclub(
        name = data['name'],
        description = data['description'],
        owner_id = current_user.id
    )
    db.session.add(bookclub)
    db.session.commit()
    return jsonify({'message': f'Bookclub {data["name"]} added successfully!'}), 201