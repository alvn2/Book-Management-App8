from server import app, bcrypt, db
from server.models import Users
from flask import request, jsonify

@app.route('/')
def home():
    return '<h1>Home Page</h1>'

@app.route('/register', methods=['POST'])
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

@app.route('/login')
def login():
    data = request.get_json()

    user = Users.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.passwor,data['password']):
        return jsonify({'message': f'user {user.username} found'})
    else:
        return jsonify({'message': f'Login failed, please check username or password'})
    
    
