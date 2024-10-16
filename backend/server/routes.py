from server import app, bcrypt, db
from server.models import Users, Bookclub, Book, Comments, Membership
from flask import request, jsonify
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@login_required
def home():
    return jsonify({'message': f'{current_user.username}!'}), 200

@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return jsonify({'message': 'User already logged in!'}), 200
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
    return jsonify({'message': f'User {data["username"]} registered successfully!'}), 201

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return jsonify({'message': 'User already logged in!'}), 200
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

@app.route('/bookclubs')
@login_required
def get_bookclubs():
    bookclubs = Bookclub.query.all()
    bookcluns_list = []
    for bookclub in bookclubs:
        bookclub_dict = {
            'name': bookclub.name,
            'description': bookclub.description,
            'owner': bookclub.owner.username
        }
        bookcluns_list.append(bookclub_dict)
    return jsonify(bookcluns_list), 200

@app.route('/bookclub/<int:id>')
@login_required
def get_bookclub(id):
    bookclub = Bookclub.query.get_or_404(id)   
    bookclub_dict = {
        'name': bookclub.name,
        'description': bookclub.description,
        'owner': bookclub.owner.username
        }
    return jsonify(bookclub_dict), 200

@app.route('/bookclub/<int:id>/join', methods=['POST', 'GET'])
@login_required
def join_bookclub(id):
    existing_membership = Membership.query.filter_by(user_id=current_user.id, bookclub_id=id).first()
    if existing_membership:
        return jsonify({'message': 'You are already a member of this bookclub!'}), 200

    new_membership = Membership(user_id=current_user.id, bookclub_id=id)
    db.session.add(new_membership)
    db.session.commit()
    return jsonify({'message': 'You have successfully joined the book club!'}), 201

@app.route('/add-book/', methods=['POST', 'GET'])
@login_required
def add_book():
    data = request.get_json()

    book = Book(
        book_title = data['book_title'],
        book_author = data['book_author'],
        description = data['description'],
        book_club_id = data['book_club_id']
        )
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': f'Book {data["book_title"]} added successfully!'}), 201

@app.route('/books')
@login_required
def get_books():
    books = Book.query.all()
    books_list = []
    for book in books:
        book_dict = {
            'book_title': book.book_title,
            'book_author': book.book_author,
            'description': book.description,
            'book_club_id': book.book_club_id
            }
        books_list.append(book_dict)
    return jsonify(books_list), 200

@app.route('/book/<int:id>')
@login_required
def get_book(id):
    book = Book.query.get_or_404(id)  
    book_dict = {
        'book_title': book.book_title,
        'book_author': book.book_author,
        'description': book.description,
        'book_club': book.book_club_id
        }
    return jsonify(book_dict), 200

@app.route('/delete-book/<int:id>', methods=['DELETE'])
@login_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    comments = book.comments  
    for comment in comments:
        db.session.delete(comment)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': f'Book "{book.book_title}" deleted successfully!'}), 200

@app.route('/add-comment/', methods=['POST', 'GET'])
@login_required
def add_comment():
    data = request.get_json()
    comment = Comments(user_id = current_user.id,book_id = data['book_id'], content = data['content'])
    db.session.add(comment)
    db.session.commit()
    return jsonify({'message': 'Comment added successfully!'}), 201

@app.route('/comments')
def get_comments():
    comments = Comments.query.all()  
    comments_list = []
    for comment in comments:
        comment_dict = {
            'user': comment.user.username,
            'book': comment.book.book_title,
            'content': comment.content
            }
        comments_list.append(comment_dict)
    return jsonify(comments_list), 200

@app.route('/comment/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_comment(id):
    comment = Comments.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment deleted successfully!'}), 200