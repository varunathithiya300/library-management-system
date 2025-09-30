class book:
    books_db = {}

    def __init__(self, title: str, author: str, isbn: str):
        self.isbn = isbn
        self.title = title
        self.author = author

    def add_books(self, title, author, isbn):
        if not book.books_db.get(self.title): # figure out a way to add a nested struct containing the book information to books_db
            book.books_db['title'] = title
            book.books_df['author'] = author
            book.books_db['isbn'] = isbn

b1 = book('Fluent Python', 'Luciano Ramalho', '978-1492056355')

class member:
    member_db = {}

    def __init__(self, firstname: str, lastname: str, dob: str, email: str):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.email = email

class library:
    def __init__(self):
        pass



""" 
1. when a book object is created, the book should be automatically added to the object with default value as available
2. Member class should 
"""