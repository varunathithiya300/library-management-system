member_db = {}
books_db = {}

class book:
    def __init__(self, title: str, author: str, isbn: str):
        self.isbn = isbn
        self.title = title
        self.author = author

# b1 = book('Fluent Python', 'Luciano Ramalho', '978-1492056355')

class member:
    def __init__(self, firstname: str, lastname: str, dob: str, email: str):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.email = email

    def donate_book(self, title, author, isbn):
        if not books_db.get(title): # figure out a way to add a nested struct containing the book information to books_db
            books_db['title'] = title
            books_db['author'] = author
            books_db['isbn'] = isbn
            books_db['is_available'] = 'Yes'
        else:
            pass

    def borrow_book(self, title, author, isbn):
        pass


m1 = member('Varun', 'Athithiya', '02041994', 'shenbagarajvarun@gmail.com')
m1.donate_book('abc', 'varun', '123456789')
m1.donate_book('Fluent Python', 'Luciano Ramalho', '978-1492056355')


print(books_db)

# class borrower(member):
#     def __init__(self, firstname, lastname, dob, email):
#         super().__init__(firstname, lastname, dob, email)

# class lender(member):
#     def __init__(self, firstname, lastname, dob, email):
#         super().__init__(firstname, lastname, dob, email)