'''
Magic Methods = Dunder Methods (double underscore) __init__, __str__, __eq__
They are automatically called by many of Python's built-in operations
They allow dvelopers to define or customize the behaviour of objects
'''

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

book1 = Book("The Hobbit", "J.R.R", 310)
book2 = Book("The Harry Potter","J.k Rowling",223)
book3 = Book("The lion","C.S. Lewis",172)
book4 = Book("The Hobbit", "J.R.R", 310)

print(book1) #This return the object value
print(book1 == book4) #still this return false even it correct
#To customize the above behaviour we can use that __str__ method. Instead of returning memory adrees we will customize this

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by '{self.author}"
    
    def __eq__(self,other): #self is first book and the other is other book
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self,other):
        return self.num_pages < other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __conatins__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key ==  "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key} not found"

book1 = Book("The Hobbit", "J.R.R", 310)
book2 = Book("The Harry Potter","J.k Rowling",223)
book3 = Book("The lion","C.S. Lewis",172)
book4 = Book("The Hobbit", "J.R.R", 310)

print(book1)
print(book1 == book2)
print(book1==book4)
print(book2 < book1)
print("Hobbit" in book1)
