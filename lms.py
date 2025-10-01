member_db = {}
books_db = {}

class book:
    def __init__(self, title: str, author: str, isbn: str):
        self.isbn = isbn
        self.title = title
        self.author = author

class member:
    def __init__(self, firstname: str, lastname: str, dob: str, email: str):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.email = email
    
    def register_member(self):
        if not member_db.get(self.firstname):
            member_db[self.firstname] = {'firstname':self.firstname, 'lastname':self.lastname, 'dob':self.dob, 'email':self.email}

    def donate_book(self, title, author, isbn):
        if not books_db.get(title): # figure out a way to add a nested struct containing the book information to books_db
            books_db[title] = {'author':author, 'isbn':isbn, 'is_available':'y'}
        else:
            pass

    def borrow_book(self, book_title):
        """ 
        Approach
        Ideally we should be able to borrow a book based on any of the title or author or both
        This method should access the books_db and check the is_available flag for each book and return a suitable response.
        If the book is available the book should be assigned to the user, else the system should show the date earliest and the latest available date of the book.
        Whenever a book is borrowed, is_available = 'N'
        We should also maintain a mapping of which book is with which member
        """
        if books_db.get(book_title)['is_available'] == 'y':
            books_db.get(book_title).update(is_available = 'n')
        else:
            print(f'{book_title} is not available at the moment.')
        

m1 = member('Varun', 'Athithiya', '02041994', 'shenbagarajvarun@gmail.com')
m1.register_member()

m2 = member('Kirtana', 'Shenbagaraj', '31122001', 'kirtanasraj@gmail.com')
m2.register_member()

m1.donate_book('abc', 'varun', '123456789')
m1.donate_book('Fluent Python', 'Luciano Ramalho', '978-1492056355')
m1.donate_book('Data Mining', 'Jiawei Han and Micheline Kamber', '978-8131205358')

# for k,v  in books_db.items():
#     print(k, v)

# for k,v  in member_db.items():
#     print(k, v)


m1.borrow_book('Fluent Python')
m2.borrow_book('Fluent Python')

