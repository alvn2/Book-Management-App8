from server import db
from server import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Bookclub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner = db.relationship('Users', backref='owned_bookclubs', lazy=True)
    books = db.relationship('Book', back_populates='book_club', lazy=True)

    def __repr__(self):
        return f"Bookclub('{self.name}', '{self.description}')"
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), nullable=False)
    book_author = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    book_club_id = db.Column(db.Integer, db.ForeignKey('bookclub.id'),default=None)
    book_club = db.relationship('Bookclub', back_populates='books', lazy=True)

    def __repr__(self):
        return f"Book('{self.book_title}', '{self.book_author}', '{self.description}')"

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user = db.relationship('Users', backref='comments', lazy=True)
    book = db.relationship('Book', backref='comments', lazy=True)

class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    bookclub_id = db.Column(db.Integer, db.ForeignKey('bookclub.id'), nullable=False)
    user = db.relationship('Users', backref='memberships', lazy=True)
    bookclub = db.relationship('Bookclub', backref='members', lazy=True)