# import the random class to generate random numbers for the Book ID
import random 

# Create the class Books with getter and setter methods for title, author, year, publisher, qty, pub_Date, book_ID. 
# Generate 6 Digits Random Book ID Number
class Books:
    
    def __init__(self, title, author, year, publisher, qty, pub_Date, book_ID = random.randint(100000,999999)):
        self.__book_ID = book_ID
        self.__title = title
        self.__author = author
        self.__year = year
        self.__publisher = publisher
        self.__qty = qty
        self.__pub_Date = pub_Date

# Setter Method for Book ID
    def set_book_ID(self, book_ID):
        self.__book_ID = book_ID

# Getter Method for Book ID
    def get_book_ID(self):
        return self.__book_ID

# Getter Method for Book Title
    def get_title(self):
        return self.__title

# Setter Method for Book Title
    def set_title(self, title):
        self.__title = title

# Getter Method for Book Author
    def get_author(self):
        return self.__author

# Setter Method for Book Author
    def set_author(self, author):
        self.__author = author

# Getter Method for Book Year
    def get_year(self):
        return self.__year

# Setter Method for Book Year
    def set_year(self, year):
        self.__year = year

# Getter Method for Book Publisher
    def get_publisher(self):
        return self.__publisher

# Setter Method for Book Publisher
    def set_publisher(self, publisher):
        self.__publisher = publisher

# Getter Method for Book Copies
    def get_qty(self):
        return self.__qty

# Setter Method for Book Copies
    def set_qty(self, qty):
        self.__qty = qty

# Getter Method for Book Publsihed Date
    def get_pub_Date(self):
        return self.__pub_Date

# Setter Method for Book Publsihed Date
    def set_pub_Date(self, pub_Date):
        self.__pub_Date = pub_Date


# Testing the setter and getter methods
# obj = Books('','','','','','')
# obj.set_year('2001')
# print("The year is: ", obj.get_year())