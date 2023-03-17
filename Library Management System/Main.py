from BookList import BookList
from UserList import UserList
from Loans import Loans


print("\t\t\t\t\t\t\t-----------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t♦♦♦♦♦♦♦ WELCOME TO THE CETM73 ASSIGNMENT2 LIBRARY MANANEGEMENT SYSTEM ♦♦♦♦♦♦♦\n")
print("\t\t\t\t\t\t\t-----------------------------------------------------------------------------")

def start():
    response = input("Do you want to access the library? (yes or no): ")
    response = response.upper()

    if response == "YES":                     
        return True                                   
    else:                                             
        return False
    
class Main:

    def __init__(self):
        objBookList = BookList()
        objUserList = UserList()
        objLoan = Loans()
        prompt = input("Select the option that correspond to what you want to do. \n1 to Add a Book \n2 to Search for a Book \n3 to Remove a Book \n4 to Modify a Book \n5 for Book Count  \n6 to Add a User \n7 to Search for a User \n8 to Remove a User \n9 to Modify a User \n10 for User Count  \n11 to Loan a Book  \n12 to Return a Book  \n13 to List User Loaned Book(s)  \n14 to List Overdue Loaned Book(s) \nQ to Quit\n\n")

        if prompt == "1":
            print("\nAdd a Book\n")
            objBookList.add_book()        

        elif prompt == "2":
            print("\nSearch for a Book\n")
            objBookList.search_book()

        elif prompt == "3":
            print("\nRemove a Book\n")
            objBookList.remove_book()

        elif prompt == "4":
            print("\nModify a Book\n")
            objBookList.modify_book()
        
        elif prompt == "5":
            print("\nGenerate Book Count\n")
            objBookList.inventory_book()

        elif prompt == "6":
            print("\nAdd a User\n")
            objUserList.add_user()

        elif prompt == "7":
            print("\nSearch for a User\n")
            objUserList.search_user()

        elif prompt == "8":
            print("\nRemove a User\n")
            objUserList.remove_user()

        elif prompt == "9":
            print("\nModify a User\n")
            objUserList.modify_user()

        elif prompt == "10":
            print("\nGenerate User Count\n")
            objUserList.count_users()

        elif prompt == "11":
            print("\nIssue a Book on Loan\n")
            objLoan.loan_book()

        elif prompt == "12":
            print("\nReturn a Loaned Book\n")
            objLoan.return_book()

        elif prompt == "13":
            print("\nUser Loaned Book Count\n")
            objLoan.loan_count()

        elif prompt == "14":
            print("\nList Overdue Loaned\n")
            objLoan.overdue_count()

        elif prompt == "Q":
            exit()
        else:
            print ('\nYour choice is out of range. Try again! \n')

while start():
    Main()
    print('')
