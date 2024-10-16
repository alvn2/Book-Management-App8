from server import app, db

from server.models import Book, Users, Bookclub

with app.app_context():

    print("Deleting data...")
    Book.query.delete()

    print("Creating book list...")
    book1 = Book(
        book_title="The Great Gatsby", book_author="F. Scott Fitzgerald", 
        description="The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan.")
    book2 = Book(
        book_title="To Kill a Mockingbird", book_author="Harper Lee", 
        description="The story of a young boy growing up in the South during the 1930s who learns about   the evils of racism and the importance of standing up for what is right.")
    book3 = Book(
        book_title="1984", book_author="George Orwell", 
        description="The story of Winston Smith, a bold individual who decides to rebel against the oppressive government of Oceania.")
    book4 = Book(
        book_title="Pride and Prejudice", book_author="Jane Austen", 
        description="The story of Elizabeth Bennet, a strong-willed kind lady who must navigate the social norms of her time.")
    book5 = Book(
        book_title="The Catcher in the Rye", book_author="J.D. Salinger", 
        description="The story of Holden Caulfield and his journey through New York City after being expelled from his prep school.")
    
    books = [book1, book2, book3, book4, book5]
  
    print("Creating books...")

   

    print("Creating book list...")
    db.session.add_all(books)
    db.session.commit() 

    print("Deleting data...")
    Users.query.delete()
    
    print ("Creating user list...")
    user1 = Users(username="admin", email="admin@book-list.com", password="testing", image_file="default.png")
    user2 = Users(username="user", email="second@gmail.com", password="testing", image_file="default.png")
    user3 = Users(username="user2", email="third@gmail.com", password="testing", image_file="default.png")
    user4 = Users(username="user3", email="fourth@gmail.com", password="testing", image_file="default.png")
    user5 = Users(username="user4", email="fifth@gmail.com", password="testing", image_file="default.png")

    users = [user1, user2, user3, user4, user5]

    print("Creating users...")
    db.session.add_all(users)
    db.session.commit()

    print("Deleting data...")
    Bookclub.query.delete()

    print("Creating bookclubs...")
    bookclub1 = Bookclub(
        name="Bookclub 1", description="A bookclub for the classics.", owner_id=1)
    bookclub2 = Bookclub(
        name="Bookclub 2", description="A bookclub for the modern reader.", owner_id=2)
    bookclub3 = Bookclub(
        name="Bookclub 3", description="A bookclub for the adventurous reader.", owner_id=3)
    bookclub4 = Bookclub(
        name="Bookclub 4", description="A bookclub for the romantic at heart.", owner_id=4)
    bookclub5 = Bookclub(
        name="Bookclub 5", description="A bookclub for the mystery lover.", owner_id=5)
    
    bookclubs = [bookclub1, bookclub2, bookclub3, bookclub4, bookclub5]

    print("Creating bookclubs...")
    db.session.add_all(bookclubs)
    db.session.commit()


    print("Seeding done!")

if __name__ == '__main__':
    app.run(debug=True)