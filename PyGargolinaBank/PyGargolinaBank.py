import sqlite3
import sys
#from math import *
from Library2 import Library2
from Library1 import Library1
from CEO import CEO
from admin import Admin
from client import Client
#import random
#from decimal import Decimal as D

def UploadDataFromDatabase(Cursor, ListOfAdmins, ListOfClients, clientID, adminID):
    try:
        result = Cursor.execute("SELECT * FROM admins;")
        for row in result:
            newAdmin = Admin(row[1], row[2], row[3], row[4], row[5], row[0])
            adminID = row[0]
            ListOfAdmins.append(newAdmin)

        result2 = Cursor.execute("SELECT * FROM clients;")
        for row in result2:
            newClient = Client(row[1], row[2], row[3], row[4], row[5], row[0])
            clientID = row[0]
            ListOfClients.append(newClient)

    except sqlite3.OperationalError:
        print("Table hasn't been created!")

def main():

    GargolinaDB = sqlite3.connect('Gargolina.db')
    Cursor = GargolinaDB.cursor()

    GargolinaDB.execute("CREATE TABLE IF NOT EXISTS admins(id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL, surname TEXT NOT NULL, homeAdress TEXT NOT NULL, GargolinaNumber TEXT NOT NULL, password TEXT NOT NULL);")
    GargolinaDB.commit()

    GargolinaDB.execute("CREATE TABLE IF NOT EXISTS clients(id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL, surname TEXT NOT NULL, homeAdress TEXT NOT NULL, passportNumber TEXT NOT NULL, password TEXT NOT NULL);")
    GargolinaDB.commit()

    adminCode = 666             #password for enabling register as admin
    clientID = 1000             #there shouldn't be more than 1000 admins
    adminID = 10                #there will be only 1 CEO account, so adminID should be bigger than 1

    UploadDataFromDatabase(Cursor, ListOfAdmins,ListOfClients, clientID, adminID)
    print(adminID)
    print(clientID)         # Temporary code - should disappear at the end of making this program

    CEOaccount = CEO()
    ListOfAdmins = []
    ListOfClients = []

    print("Hello! You have entered in a Gargolina bank!")
    while adminID != 0:                                                 # Just making it as never ending loop with only one way out
        choice = input("Choose between Log In(write L) or Sign up(write S) below this message!    ")
        if choice == 'L':
            Library2.LogIn(ListOfAdmins, ListOfClients, CEOaccount)
        elif choice == 'S':
            clientID = Library1.SignUp(clientID)
        elif choice == 'AS':
            try:
                controlCode = int(input("Enter admin code for registrating as administrator:   "))
                if controlCode != adminCode:
                    print("Access Denied for registrating as admin!")
                else:
                    adminID = Library1.AdminSignUp(adminID)
            except ValueError:
                print("There should be inputed a code that contains ONLY DIGITS!")
            except:
                print("An unknown error occured!")
        else:
            print("Input undefined!")



        willContinue = input("Do you want to continue? Write 'NO' to go out!    ")
        if willContinue == "NO":
            print("Bye, bye!")
            break
       
main()