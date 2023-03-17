import json
import datetime
from tkinter import TRUE
from Users import Users
from Books import Books
from BookList import BookList
from UserList import UserList
import functions


class Loans:
    def __init__(self):
        print('')  

# Loan out a book and store the record (Book Title, Username, Loan Date, Expected Return Date, Is Returned?, Actual Return Date) in Loan.json
    def loan_book(self):
        time = datetime.datetime.now()
        book_title = ""
        username = ""
        loan_date ="%s/%s/%s" % (time.day, time.month, time.year)
        return_date = datetime.datetime.now() + datetime.timedelta(days = 7)
        return_date = "%s/%s/%s" % (return_date.day, return_date.month, return_date.year)
        book_title = input("\nEnter the Book Title: ")
        if(self.confirm_book(book_title)): # Check if the book exist
            username = input("\nEnter the Username: ")
            if(self.confirm_user(username)): # check if the user exist
                addLoanDictionary = {"_Books__title": book_title, "_Users__username": username, "_Loan__loan_date": loan_date, "_Loan__return_date": return_date, "_Loan__returned": "No", "_Loan__returned_date": "01/01/1900"}
                addLoanDictionary =json.dumps(addLoanDictionary, sort_keys=True)
                with open("data/Loan.json", "r") as openfile:
                    loanDataset = json.load(openfile)
                loanDataset.append(addLoanDictionary)
                loanDataset = str(loanDataset)
                loanDataset = loanDataset.replace("'{","{")
                loanDataset = loanDataset.replace("}'","}")
                loanDataset = loanDataset.replace("'","\"")
                with open("data/Loan.json", "w") as outfile:
                    outfile.write (loanDataset)
                print("Book with Book Title ", book_title, " has been issued to ",username," today ",loan_date," and to be retuned in 7 days on ",return_date)
            else:
                print("\n\n Username does not exist!")
        else:
            print("\n\n Book does not exist!")

# Return a Loan Book and update the record in Loan.json
    def return_book(self):
        time = datetime.datetime.now()
        search_count = 0
        book_title = ""
        username = ""
        returned_date = "%s/%s/%s" % (time.day, time.month, time.year)
        book_title = input("\nEnter the Book Title: ")
        username = input("\nEnter the Username: ")
        with open("data/Loan.json", "r") as openfile:
            loanDataset = json.load(openfile)
        for keyval in loanDataset:
            if book_title.lower() == keyval ['_Books__title'].lower() and username.lower() == keyval ['_Users__username'].lower():
                search_count +=1
                addLoanDictionary = {"_Books__title": book_title, "_Users__username": username, "_Loan__loan_date": keyval ['_Loan__loan_date'], "_Loan__return_date": keyval ['_Loan__return_date'], "_Loan__returned": "Yes", "_Loan__returned_date": returned_date}
                for idx, obj in enumerate(loanDataset):
                    if obj['_Books__title'].lower() == book_title.lower() and obj['_Users__username'].lower() == username.lower():
                        loanDataset.pop(idx)
                    loanDataset.append(addLoanDictionary)
                    loanDataset = str(loanDataset)
                    loanDataset = loanDataset.replace("'{","{")
                    loanDataset = loanDataset.replace("}'","}")
                    loanDataset = loanDataset.replace("'","\"")
                    with open("data/Loan.json", "w") as outfile:
                        outfile.write (loanDataset)
                    print('\n\nThe Book with Book Title: ', keyval['_Books__title'] ,' loaned to ', keyval['_Users__username'],' on ', keyval ['_Loan__loan_date'],' has been marked returned successfully!')    
        if search_count == 0:
            print("We could not find a match for the Loaned Book and Username")
        

# Count the number of Loaned Books per User from Loan.json with username filter
    def loan_count(self):
        search_count = 0
        username = ""
        username = input("\nEnter the Username: ")
        with open("data/Loan.json", "r") as openfile:
            loanDataset = json.load(openfile)
        for keyval in loanDataset:
            if keyval ['_Users__username'].lower() == username.lower() and keyval ['_Loan__returned'] == 'No': # Check the loaned books with the username with return status still No
                search_count +=1
        print("\n\n",username, " has ",search_count," book(s) on loan")
        if search_count == 0:
            print("\n\n",username, " do not have any book on loan")

# List all the overdue Loaned Books from Loan.json
    def overdue_count(self):
        objUser = Users('username', 'firstname', 'surname', 'housenumber', 'streetname', 'postcode', 'email', 'dob')
        time = datetime.datetime.now()
        today= "%s/%s/%s" % (time.day, time.month, time.year)
        search_count = 0
        with open("data/Loan.json", "r") as openfile:
            loanDataset = json.load(openfile)
        with open("data/UserList.json", "r") as openfile:
            UserDataset = json.load(openfile)
        for keyval in loanDataset:
            if  keyval ['_Loan__return_date'] <= today and keyval ['_Loan__returned'] == 'No': # Check if the expected return date has past and return status is still No
                search_count +=1
                for ukeyval in UserDataset:
                    if keyval ['_Users__username'].lower() == ukeyval ['_Users__username'].lower():
                        objUser.set_firstname(ukeyval ['_Users__firstname'])
                print("\n\n Book Title: ", keyval ['_Books__title']," | Due Date: ", keyval ['_Loan__return_date'], " | Username: ", keyval ['_Users__username']," | First Name: ", objUser.get_firstname())
        if search_count == 0:
            print("\n\nNo record found")

# Check if the entered book name exist in BookList.json (bookDatabase)
    def confirm_book(self,search_keyword):
        bookDataset = ""
        search_count = 0
        with open("data/BookList.json", "r") as openfile:
            bookDataset = json.load(openfile)
        for keyval in bookDataset:
            if search_keyword.lower() == keyval ['_Books__title'].lower():
                search_count +=1
        if search_count == 0:
            return False
            
        else:
            return True

# Check if the entered username exist in UserList.json (userDatabase)
    def confirm_user(self,search_keyword):
        userDataset = ""
        search_count = 0
        with open("data/UserList.json", "r") as openfile:
            userDataset = json.load(openfile)
        for keyval in userDataset:
            if search_keyword.lower() == keyval ['_Users__username'].lower():
                search_count +=1
        if search_count == 0:
            return False
            
        else:
            return True


#Testing the methods
#instanceLoan = Loans()
#instanceLoan.loan_book()
#instanceLoan.return_book()
#instanceLoan.overdue_count()
#instanceLoan.overdue_count()
