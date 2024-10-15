#!/usr/bin/env python3

from server import app, db
from server.models import Book

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database
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

    print("Seeding done!")