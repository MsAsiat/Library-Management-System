import random
# Create the class Users with getter and setter methods for username, firstname, surname, housenumber, streetname, postcode, email, dob. 

class Users:
    
    def __init__(self, username, firstname, surname, housenumber, streetname, postcode, email, dob, user_ID = random.randint(1,9999)):
        self.__user_ID = user_ID
        self.__username= username
        self.__firstname = firstname
        self.__surname = surname
        self.__housenumber = housenumber
        self.__streetname = streetname
        self.__postcode = postcode
        self.__email = email
        self.__dob = dob



# Getter Method for User ID
    def get_user_ID(self):
        return self.__user_ID

# Setter Method for User ID
    def set_user_ID(self, user_ID):
        self.__user_ID = user_ID

# Getter Method for Username
    def get_username(self):
        return self.__username

# Setter Method for Username
    def set_username(self, username):
        self.__username = username

# Getter Method for First Name
    def get_firstname(self):
        return self.__firstname

# Setter Method for First Name
    def set_firstname(self, firstname):
        self.__firstname = firstname

# Getter Method for Surname
    def get_surname(self):
        return self.__surname

# Setter Method for Surname
    def set_surname(self, surname):
        self.__surname = surname

# Getter Method for House Number      
    def get_housenumber(self):
        return self.__housenumber

# Setter Method for House Number
    def set_housenumber(self, housenumber):
        self.__housenumber = housenumber

# Getter Method for Street Name
    def get_streetname(self):
        return self.__streetname

# Setter Method for Street Name
    def set_streetname(self, streetname):
        self.__streetname = streetname

# Getter Method for Postcode
    def get_postcode(self):
        return self.__postcode

# Setter Method for Postcode
    def set_postcode(self, postcode):
        self.__postcode = postcode

# Getter Method for Email Address
    def get_email(self):
        return self.__email

# Setter Method for Email Address
    def set_email(self, email):
        self.__email = email

# Getter Method for Date of Birth
    def get_dob(self):
        return self.__dob

# Setter Method for Date of Birth
    def set_dob(self, dob):
        self.__dob = dob