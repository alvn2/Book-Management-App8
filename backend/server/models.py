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
    owner = db.relationship('Users', backref='owner', lazy=True)
    books = db.relationship('Book', backref='bookclub', lazy=True)

    def __repr__(self):
        return f"Bookclub('{self.name}', '{self.description}')"
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), nullable=False)
    book_author = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    book_club_id = db.Column(db.Integer, db.ForeignKey('bookclub.id'), nullable=False)
    book_club = db.relationship('Bookclub', backref='books', lazy=True)

    def __repr__(self):
        return f"Book('{self.book_title}', '{self.book_author}', '{self.description}')"