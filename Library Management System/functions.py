import re

#                                                              LIBRARY USERS' INPUT VALIDATION                                                     

def getDate():
    import datetime
    now=datetime.datetime.now
    #print("Date: ",now().date())
    return str(now().date())
#----------------------------------------------------------------------------------

def getTime():
    import datetime
    now=datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())



#                                                               BOOK LIST FUNCTIONS
#-----------------------------------------------------------------------------------------
#           A function to prompt user to input proper book author's name
#------------------------------------------------------------------------------------------
pattern = re.compile('[a-zA-Z ]+')
def authorname():
    while True:
        name = input("Enter Author's Name: ").strip()
        if pattern.fullmatch(name):
            return name
        print("Invalid name format!\nPlease input alphabet from A-Z with spaces only")

#------------------------------------------------------------------------------------------
#           A function to prompt user to input proper publisher name 
#------------------------------------------------------------------------------------------
pattern = re.compile('[a-zA-Z ]+')
def publisher():
    while True:
        name = input("Enter the publisher of this book: ").strip()
        if pattern.fullmatch(name):
            return name
        print("Invalid name format!\nPlease input alphabet from A-Z with spaces only")

#------------------------------------------------------------------------------------------
#           A function to input a proper publication date
#------------------------------------------------------------------------------------------
def grabpub_date():
    while(True):
        date = input("Please enter date of publication: [mm/dd/yy] ")
        if( len(date) == 8 and date[2] == "/"):
            return date
        else:
            print("Incorrect date format!\nEnter date as: [mm/dd/yy] ")

#------------------------------------------------------------------------------------------
#       A function to ensure that valid integer value is entered for book quantity
#------------------------------------------------------------------------------------------
def get_qty():
    bookqty = input("Please enter the quantity in stock: ").lower()
    if (bookqty.isdigit()):
        return bookqty
    else:
        print("Invalid input!\nEnter an integer value")
        return get_qty()


#                                                           USERS LIST FUNCTIONS

#------------------------------------------------------------------------------------------------------------------------
# A function to prompt user to create strong username with combination of numbers, letters and special character
#------------------------------------------------------------------------------------------------------------------------
def username():
    while(True):
        username = input ("Please enter a username: ")
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', username):
            return username
        else:
            print("Username must not be less than 8 characters include numbers, letters and symbols")


#-----------------------------------------------------------------------------------
# A function to prompt user to input proper name
#-----------------------------------------------------------------------------------

def firstname():
    while(True):
        name = input("Enter first name: ")
        if name.isalpha() == True:
            return name
        else:
            print("Invalid name! Please input alphabet from A-Z only")


def surname():
    while(True):
        name = input("Enter surname: ")
        if name.isalpha() == True:
            return name
        else:
            print("Invalid name! Please input alphabet from A-Z only")

#------------------------------------------------------------------------------------------------------------------------------------
# A function to prompt user to input proper date of birth
#------------------------------------------------------------------------------------------------------------------------------------
def grabDOB():
    while(True):
        date = input("Please enter a user's DOB: [mm/dd/yy] ")
        if( len(date) == 8 and date[2] == "/"):
            return date
        else:
            print("Incorrect date format!\nEnter date as: [mm/dd/yy] ")


#------------------------------------------------------------------------------------------------------------------------------------
# A function to prompt user to input proper email addresss
#------------------------------------------------------------------------------------------------------------------------------------
def validemail():
    while(True):
        email = input ("Please type in an email address ")
        if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
            return email
        else:
            print("Your email address must have '@' and '.' in it. Please write your email address again")
