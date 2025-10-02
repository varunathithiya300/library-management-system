from datetime import datetime, timedelta
from dataclasses import dataclass
import time

book_donation_date = datetime.now().strftime("%Y-%m-%d")
member_db = {}
books_db = {}


class book:
    def __init__(self, title: str, author: str, isbn: str, donated_date: datetime.date) -> object:
        """ 
        The library can have up to 5 copies of the same book to cater to any demand. (not implemented yet)  
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.donated_date = donated_date

class member():
    def __init__(self, firstname: str, lastname: str, dob: str, email: str):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.email = email
        self.doj = datetime.now().strftime("%Y-%m-%d")
        self.dor = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")
    
    def register_member(self):
        if not member_db.get(self.firstname):
            member_db[self.firstname] = {'firstname':self.firstname, 'lastname':self.lastname, 'dob':self.dob, 'email':self.email, 'doj': self.doj, 'dor': self.dor}

    def donate_book(self, title, author, isbn, donated_date):
        if books_db.get(title): # figure out a way to add a nested struct containing the book information to books_db
            print(f'{title} already available. Please donate a different book. Thank you. Keep contributing :)')
        else:
            books_db[title] = {'author':author, 'isbn':isbn, 'is_available':'y', 'donated_date': donated_date}

    def borrow_book(self, book_title):
        """ 
        Approach
        Ideally we should be able to borrow a book based on any of the title or author or both
        This method should access the books_db and check the is_available flag for each book and return a suitable response.
        If the book is available the book should be assigned to the user, else the system should show the date earliest and the latest available date of the book.
        Whenever a book is borrowed, is_available = 'N'
        We should also maintain a mapping of which book is with which member
        We should have a field for when a book is borrowed
        """
        if books_db.get(book_title)['is_available'] == 'y':
            books_db.get(book_title).update(is_available = 'n')
        else:
            print(f'{book_title} is not available at the moment.')

""" 
@dataclass                
class library_rules(frozenset=True):
    min_duration = min_duration
    max_duration = max_duration
    max_allowed_books = 3
    renewal = 180
    pass 
"""

m1 = member('Varun', 'Athithiya', '02041994', 'shenbagarajvarun@gmail.com')
m1.register_member()

m2 = member('Kirtana', 'Shenbagaraj', '31122001', 'kirtanasraj@gmail.com')
m2.register_member()

m1.donate_book('Designing Data-Intensive Applications', 'Martin Kleppmann', '978-9352135240', book_donation_date)
m1.donate_book('Fluent Python', 'Luciano Ramalho', '978-1492056355', book_donation_date)
m1.donate_book('Data Mining', 'Jiawei Han and Micheline Kamber', '978-8131205358', book_donation_date)
m2.donate_book('Database Internals: A Deep Dive Into How Distributed Data Systems Work', 'Alex Petrov', '978-9352139071', book_donation_date )

# m1.borrow_book('Fluent Python')
# m2.borrow_book('Fluent Python')
# m2.borrow_book('Data Mining')
# m1.borrow_book('Data Mining')
# print(member_db)

def show_book_db():
    print()
    for book, details in books_db.items():
        print(book, '-', details)
        print()

if __name__ == "__main__":
    show_book_db()