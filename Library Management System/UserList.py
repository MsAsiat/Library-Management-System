import json
from Users import Users
import functions

#instanceUserList = UserList()
class UserList:
    def __init__(self):
        print('')        
 #-------(Add User- username, firstname, surname, housenumber, streetname, postcode, Email address, Date of birth)--------     
    def add_user(self):
        objUser = Users('','','','','','','','')
        objUser.set_username(functions.username())
        objUser.set_firstname(functions.firstname())
        objUser.set_surname(functions.surname())
        objUser.set_housenumber(int(input("Enter House Number: ")))
        objUser.set_streetname(input("Enter street name here: "))
        objUser.set_postcode(input("Enter postcode here: "))
        objUser.set_email(functions.validemail())
        objUser.set_dob(functions.grabDOB())
        addUserDictionary =json.dumps(objUser.__dict__, sort_keys=True)
        with open("data/UserList.json", "r") as openfile:
            UserDataset = json.load(openfile)
        UserDataset.append(addUserDictionary)
        UserDataset = str(UserDataset)
        UserDataset = UserDataset.replace("'{","{")
        UserDataset = UserDataset.replace("}'","}")
        UserDataset = UserDataset.replace("'","\"")
        with open("data/UserList.json", "w") as outfile:
            outfile.write (UserDataset)
        #with open("data/UserList.json", "a") as outfile:
        #    outfile.write (addUserDictionary)
        print("Firstname: ", objUser.get_firstname(), "was assigned", "User ID: ", objUser.get_user_ID(),  "and registered successfully!")

#------------------------------(Search User by username, firstname surname or Email)------------------
    def search_user(self):
        objUser = Users('','','','','','','','','')
        search_prompt = input("Type \n1 to Search by Username \n2 to Search by Firstname \n3 to Search by Surname \n4 to Search by Email Address \n")
        search_keyvalue = ""
        UserDataset = ""
        search_count = 0
        if search_prompt == "1":
            search_keyvalue = "_Users__username"         

        elif search_prompt == "2":
            search_keyvalue = "_Users__firstname" 

        elif search_prompt == "3":
            search_keyvalue = "_Users__surname" 

        elif search_prompt == "4":
            search_keyvalue = "_Users__email" 
        else:
            print ('Your choice is out of range')
            exit
        search_keyword = input("Enter the Search Keyword: ")
        with open("data/UserList.json", "r") as openfile:
            UserDataset = json.load(openfile)
        #print(userDataset)
        for keyval in UserDataset:
            if search_keyword.lower() == keyval [search_keyvalue].lower():
                search_count +=1
                print('\n\nSearch Result: \nUser(s) Found: \nUser ID: ',keyval['_Users__user_ID'],' | Firstname: ', keyval['_Users__firstname'],' | Surname: ', keyval['_Users__surname'],' | House#: ', keyval['_Users__housenumber'],' | Streetname: ', keyval['_Users__streetname'],' | Postcode: ', keyval['_Users__postcode'],' | Email: ', keyval['_Users__email'],' | DOB: ', keyval['_Users__dob'])
        if search_count == 0:
            print('\n\nSearch Result: \nNo User Found!')

#-------------(Remove a user from register by using their first name to search)--------------
# N/B currently not checking multiple user with same name
    def remove_user(self):
        objUser = Users('','','','','','','','')
        search_count = 0
        search_keyword = input("Type the Firstname of the user to be removed: \n")
        with open("data/UserList.json", "r") as openfile:
            userDataset = json.load(openfile)
        #print(userDataset)
        for keyval in userDataset:
            if search_keyword.lower() == keyval ['_Users__firstname'].lower():
                search_count +=1
                for idx, obj in enumerate(userDataset):
                    if obj['_Users__firstname'].lower() == search_keyword.lower():
                        userDataset.pop(idx)
                        userDataset = str(userDataset)
                        userDataset = userDataset.replace("'{","{")
                        userDataset = userDataset.replace("}'","}")
                        userDataset = userDataset.replace("'","\"")
            with open("data/UserList.json", "w") as outfile:
                outfile.write (str(userDataset))
        print('\n\nUser Removed: \nUser ID: ',keyval['_Users__user_ID'], ' | Username: ', keyval['_Users__username'], ' | Firstname: ', keyval['_Users__firstname'],' | Surname: ', keyval['_Users__surname'],' | House#: ', keyval['_Users__housenumber'],' | Streetname: ', keyval['_Users__streetname'],' | Postcode: ', keyval['_Users__postcode'],' | Email: ', keyval['_Users__email'],' | DOB: ', keyval['_Users__dob'])
        if search_count == 0:
            print('\n\nNo User Found!')

    def modify_user(self):
        search_count = 0
        objUser = Users('','','','','','','','')
        modify_user = input("Type the username of the person whose information is to be modified: \n")
        with open("data/UserList.json", "r") as openfile:
            userDataset = json.load(openfile)
        for keyval in userDataset:
            if modify_user.lower() == keyval ['_Users__username'].lower():
                search_count +=1
                if search_count >= 1:                     
                    print('\n\nUser(s) Found: \nUser ID: ',keyval['_Users__user_ID'], ' | Username: ', keyval['_Users__username'], ' | Firstname: ', keyval['_Users__firstname'],' | Surname: ', keyval['_Users__surname'],' | House#: ', keyval['_Users__housenumber'],' | Streetname: ', keyval['_Users__streetname'],' | Postcode: ', keyval['_Users__postcode'],' | Email: ', keyval['_Users__email'],' | DOB: ', keyval['_Users__dob'])
                    objUser.set_user_ID(int(keyval['_Users__user_ID']))
                    objUser.set_username(keyval['_Users__username'])
                    objUser.set_firstname(keyval['_Users__firstname'])
                    objUser.set_surname(keyval['_Users__surname'])
                    objUser.set_housenumber(keyval['_Users__housenumber'])
                    objUser.set_streetname(keyval['_Users__streetname'])
                    objUser.set_postcode(keyval['_Users__postcode'])
                    objUser.set_email(keyval['_Users__email'])
                    objUser.set_dob(keyval['_Users__dob'])
                    modify_prompt = input("\n\nType \n1 to Change the user's Firstname \n2 to Change the user's Surname \n3 to Change the user's house number \n4 to Change the user's street name \n5 to Change the user's postcode \n6 to Change the user's email address \n7 to Change the user's Date of birth \n")
                    if modify_prompt == "1":
                        objUser.set_firstname(input("\nEnter the new Firstname: ")) # upadte First name of user

                    elif modify_prompt == "2":
                        objUser.set_surname(input("\nEnter the new Surname: "))     # update surname of user

                    elif modify_prompt == "3":
                        objUser.set_housenumber(input("\nEnter the new house number: "))   # update house number of user

                    elif modify_prompt == "4":
                        objUser.set_streetname(input("\nEnter the new street name: "))     # update street name  of user
                    
                    elif modify_prompt == "5":
                        objUser.set_postcode(input("\nEnter the new postcode: "))          # update postcode of user

                    elif modify_prompt == "6":
                        objUser.set_email(input("\nEnter the new email address: "))        # update emai address of user

                    elif modify_prompt == "7":
                        objUser.set_dob(input("\nEnter the new date of birth: "))          # update date of birt of of user
                    else:
                        print ('\nYour choice is out of range')
                        exit
                    addBookDictionary =json.dumps(objUser.__dict__, sort_keys=True)  
                    for idx, obj in enumerate(userDataset):
                        if obj['_Users__username'].lower() == modify_user.lower():
                            userDataset.pop(idx)
                    userDataset.append(addBookDictionary)
                    userDataset = str(userDataset)
                    userDataset = userDataset.replace("'{","{")
                    userDataset = userDataset.replace("}'","}")
                    userDataset = userDataset.replace("'","\"")
                    with open("data/UserList.json", "w") as outfile:
                        outfile.write (userDataset)
                    print("The User with User ID: ", keyval['_Users__user_ID'], "has been modified successfully!")

        if search_count == 0:
            print('\n\nNo User Found!')

    def count_users(self):
        user_count = 0
        with open("data/UserList.json", "r") as openfile:
            userDataset = json.load(openfile)
            user_count = user_count + len(userDataset)
        print ("\n\nThe total number of users registered in the library is: ", user_count)


# Testing the methods
#instanceUserList = UserList()
#instanceUserList.add_user()
#instanceUserList.search_user()
#instanceUserList.remove_user()
#instanceUserList.modify_user()
#instanceUserList.count_users()


