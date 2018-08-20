from client import Client
from admin import Admin
import sqlite3
import sys

class Library1:

    @staticmethod
    def SignUp(ID):

        GargolinaDB = sqlite3.connect('Gargolina.db')
        Cursor = GargolinaDB.cursor()

        try:
            Name, Surname = input("Please enter your first name and your last name: ").split()
        except ValueError:                                              # if they fail to input Name and Surname correct
                print("You must input at least 2 words with space between them!")
                return ID
        HomeAdress = input("Please enter your home adress: ")

        PassportNumber = input("Please enter your passport number(in bottom of your passport ID): ")

        isCorrect = False
        while isCorrect == False:

            print("It is time to set your password. Your password must be at least 15 characters long, must contain a symbol(not digit or letter)! ")

            password1 = input("Enter your password: ") # up there are 2 conditions - 15 characters and at least 1 symbol
            isSymbolInPassword = 0

            for n in password1:
                if n.isalnum() == False:                                # if char in string isn't number and string - getting ready for checking 2. condition
                    isSymbolInPassword += 1

            if len(password1) < 15:                                     # checking for first condition
                print("Password is too short! ")

            elif isSymbolInPassword < 1:                                # checking for second condition 
                print("Password contains too less symbols! ")

            else:
                password2 = input("Repeat your password: ")
                if password2 != password1:
                    print("Sorry! You should repeat your password input because you don't remember your password!")
                else:
                    ID += 1
                    newClient = Client(Name, Surname, HomeAdress, PassportNumber, password1, ID)
                    print(newClient)

                    GargolinaDB.execute("INSERT INTO clients(id, name, surname, homeAdress, passportNumber, password) VALUES({}, '{}', '{}', '{}', '{}', '{}');".format(ID, Name, Surname, HomeAdress, PassportNumber, password1))
                    GargolinaDB.commit()

                    return ID

    @staticmethod
    def AdminSignUp(ID):

        GargolinaDB = sqlite3.connect('Gargolina.db')
        Cursor = GargolinaDB.cursor()

        try:
            Name, Surname = input("Please enter your first name and your last name: ").split()

        except ValueError:                                              # if they fail to input Name and Surname correct
                print("You must input at least 2 words with space between them!")
                return ID

        HomeAdress = "Not required"
        GargolinaNumber = input("Please enter your Gargolina card number: ")

        isCorrect = False
        while isCorrect == False:

            print("It is time to set your password. Your password must be at least 15 characters long, must contain a symbol(not digit or letter)! ")
            password = input("Enter your password: ")                   # up there are 2 conditions - 15 characters and at least 1 symbol
            isSymbolInPassword = 0

            for n in password:
                if n.isalnum() == False:                                # if char in string isn't number and string - getting ready for checking 2. condition
                    isSymbolInPassword += 1

            if len(password) < 15:                                      # checking for first condition
                print("Password is too short! ")

            elif isSymbolInPassword < 1:                                # checking for second condition 
                print("Password contains too less symbols! ")

            else:
                password2 = input("Repeat your password: ")             # repeat password - temporary variable for password control 
                if password2 != password:
                    print("Sorry! You should repeat your password input because you don't remember your password!")

                else:
                    ID += 1
                    newAdmin = Admin(Name, Surname, HomeAdress, GargolinaNumber, password, ID)
                    print(newAdmin)

                    GargolinaDB.execute("INSERT INTO admins(id, name, surname, homeAdress, GargolinaNumber, password) VALUES({}, '{}', '{}', '{}', '{}', '{}');".format(ID, Name, Surname, HomeAdress, GargolinaNumber, password))
                    GargolinaDB.commit()
                    return ID
                