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

    def borrow_book(self, title, author, isbn):
        """ 
        whenever a members borrows a book, the is_available flag must be changed to 'N'
        We should also maintain a mapping of which book is with which member
        """
        pass


m1 = member('Varun', 'Athithiya', '02041994', 'shenbagarajvarun@gmail.com')
m1.register_member()

m2 = member('Kirtana', 'Shenbagaraj', '31122001', 'kirtanasraj@gmail.com')
m2.register_member()

m1.donate_book('abc', 'varun', '123456789')
m1.donate_book('Fluent Python', 'Luciano Ramalho', '978-1492056355')
m1.donate_book('Data Mining', 'Jiawei Han and Micheline Kamber', '978-8131205358')

for k,v  in books_db.items():
    print(k, v)

for k,v  in member_db.items():
    print(k, v)