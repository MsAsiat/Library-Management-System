import json
from Books import Books
import functions

#instanceBookList = BookList()
class BookList:
    def __init__(self):
        print('')      
#1 -----------------------------------------(Function to add Book)-------------------------------------------------------
    def add_book(self):
        objBook = Books('','','','','','')
        objBook.set_title(input("Enter the Book Title: "))
        objBook.set_author(functions.authorname())
        objBook.set_year(input("Enter the Book Year: "))
        objBook.set_publisher(functions.publisher())
        objBook.set_qty(functions.get_qty())
        objBook.set_pub_Date(functions.grabpub_date())
#-----------------------------------------(addBookDictionary)-------------------------------------------------------
        addBookDictionary =json.dumps(objBook.__dict__, sort_keys=True)
        with open("data/BookList.json", "r") as openfile:
            bookDataset = json.load(openfile)
        bookDataset.append(addBookDictionary)
        bookDataset = str(bookDataset)
        bookDataset = bookDataset.replace("'{","{")
        bookDataset = bookDataset.replace("}'","}")
        bookDataset = bookDataset.replace("'","\"")
        with open("data/BookList.json", "w") as outfile:
            outfile.write (bookDataset)
        print("Book ID: ", objBook.get_book_ID(), " added successfully!")

#2 -----------------------------------------(Search BooK from the Database)-------------------------------------------
#                        (Search User by title, name of author, publisher or date of Publication)
    def search_book(self):
        objBook = Books('','','','','','')
        search_prompt = input("Type \n1 to Search by Book Title \n2 to Search by Book Author \n3 to Search by Book Publisher \n4 to Search by Publication Date \n")
        search_keyvalue = ""
        bookDataset = ""
        search_count = 0
        if search_prompt == "1":
            search_keyvalue = "_Books__title"         #---Search BooK by the title

        elif search_prompt == "2":
            search_keyvalue = "_Books__author"          #---Search BooK by the name of author

        elif search_prompt == "3":
            search_keyvalue = "_Books__publisher"       #---Search BooK by the name of publisher

        elif search_prompt == "4":
            search_keyvalue = "_Books__pub_Date"         #---Search BooK by the date of publication
        else:
            print ('Your choice is out of range')
            exit
        search_keyword = input("Enter the Search Keyword: ")
        with open("data/BookList.json", "r") as openfile:
            bookDataset = json.load(openfile)
        for keyval in bookDataset:
            if search_keyword.lower() == keyval [search_keyvalue].lower():
                search_count +=1
 #--------------(If the search keyword, information entered correspond - print book detals from file)---------------------
                print('\n\nSearch Result: \nBook(s) Found: \nBook ID: ',keyval['_Books__book_ID'],' | Book Title: ', keyval['_Books__title'],' | Book Author: ', keyval['_Books__author'],' | Book Publisher: ', keyval['_Books__publisher'],' | Book Publication Date: ', keyval['_Books__pub_Date'],' | No. of Copies: ', keyval['_Books__qty'])
        if search_count == 0:
            print('\n\nSearch Result: \nNo Book Found!')  #------------(information entered does not correspond - No Book Found!)---------------------



#3 ------------------------------(Remove a book from the file by supplying the title )------------------
    def remove_book(self):
        objBook = Books('','','','','','')
        search_count = 0
        search_keyword = input("Type the Title of the Book to remove: \n")
        with open("data/BookList.json", "r") as openfile:
            bookDataset = json.load(openfile)
        for keyval in bookDataset:
            if search_keyword.lower() == keyval ['_Books__title'].lower():
                search_count +=1
                for idx, obj in enumerate(bookDataset):
                    if obj['_Books__title'].lower() == search_keyword.lower():
#--------------------(If a book with the title is in the bookDataset then it will be removed-------------
                        bookDataset.pop(idx)
                        bookDataset = str(bookDataset)
                        bookDataset = bookDataset.replace("'{","{")
                        bookDataset = bookDataset.replace("}'","}")
                        bookDataset = bookDataset.replace("'","\"")
            with open("data/BookList.json", "w") as outfile:
                outfile.write (str(bookDataset))
#--------------------(Book database is updated and details of book remove is printed-------------
        print('\n\nBook Removed: \nBook ID: ',keyval['_Books__book_ID'],' | Book Title: ', keyval['_Books__title'],' | Book Author: ', keyval['_Books__author'],' | Book Publisher: ', keyval['_Books__publisher'],' | Book Publication Date: ', keyval['_Books__pub_Date'],' | No. of Copies: ', keyval['_Books__qty'])
        if search_count == 0:
            print('\n\nNo Book Found!') #------(If no book with the title is in the bookDataset no book will be removed---------




#4 -----(Modify Book details - title and/or author, publicationdate, publisher, quantity )------------------
    def modify_book(self):
        search_count = 0
        objBook = Books('','','','','','')
        modify_title = input("Type the Title of the Book to modify: \n")
        with open("data/BookList.json", "r") as openfile:
            bookDataset = json.load(openfile)
        for keyval in bookDataset:
            if modify_title.lower() == keyval ['_Books__title'].lower():
                search_count +=1
                if search_count >= 1:
                    print('\n\nBook Found: \nBook ID: ',keyval['_Books__book_ID'],' | Book Title: ', keyval['_Books__title'],' | Book Author: ', keyval['_Books__author'],' | Book Publisher: ', keyval['_Books__publisher'],' | Book Publication Date: ', keyval['_Books__pub_Date'],' | No. of Copies: ', keyval['_Books__qty'])
                    objBook.set_book_ID(int(keyval['_Books__book_ID']))
                    objBook.set_title(keyval['_Books__title'])
                    objBook.set_author(keyval['_Books__author'])
                    objBook.set_year(keyval['_Books__pub_Date'])
                    objBook.set_publisher(keyval['_Books__publisher'])
                    objBook.set_qty(keyval['_Books__qty'])
                    objBook.set_pub_Date(keyval['_Books__pub_Date'])
                    modify_prompt = input("\n\nType \n1 to Change the Book Title \n2 to Change the Book Author \n3 to Change the Book Publisher \n4 to Change the Book Quantity \n")
                    if modify_prompt == "1":
                        objBook.set_title(input("\nEnter the new Book Title: "))

                    elif modify_prompt == "2":
                        objBook.set_author(input("\nEnter the new Book Author: "))

                    elif modify_prompt == "3":
                        objBook.set_publisher(input("\nEnter the new Book Publisher: "))

                    elif modify_prompt == "4":
                        objBook.set_qty(input("\nEnter the new No. of Book Copies: "))
                    else:
                        print ('\nYour choice is out of range')
                        exit
                    addBookDictionary =json.dumps(objBook.__dict__, sort_keys=True)  
                    for idx, obj in enumerate(bookDataset):
                        if obj['_Books__title'].lower() == modify_title.lower():
                            bookDataset.pop(idx)
                    bookDataset.append(addBookDictionary)
                    bookDataset = str(bookDataset)
                    bookDataset = bookDataset.replace("'{","{")
                    bookDataset = bookDataset.replace("}'","}")
                    bookDataset = bookDataset.replace("'","\"")
                    with open("data/BookList.json", "w") as outfile:
                        outfile.write (bookDataset)
                    print("The Book with Book ID: ", keyval['_Books__book_ID'], "has been modified successfully!")
        if search_count == 0:
            print('\n\nNo Book Found!') #-----------(If no book with the title entered in Book database )-----------


#5 ----------(Take stock of book in the BookDatabe - How many books are there? )-----------
    def inventory_book(self):
        objBook = Books('','','','','','')
        book_count = 0
        with open("data/BookList.json", "r") as openfile:
            bookDataset = json.load(openfile)
        #print(bookDataset)
        for keyval in bookDataset:
            book_count += int(keyval['_Books__qty'])
        print ("\n\nThe total number of books stored in the collection is: ", book_count)


# Testing the methods
#instanceBookList = BookList()
#instanceBookList.add_book()
#instanceBookList.search_book()
#instanceBookList.remove_book()
#instanceBookList.modify_book()
#instanceBookList.inventory_book()