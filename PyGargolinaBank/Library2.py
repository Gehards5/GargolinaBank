from client import Client
from admin import Admin
from CEO import CEO
from Library3 import Library3

class Library2():
    
    @staticmethod
    def PasswordCheck(YourList, idInput):
        ifIdExists = False
        for OBJ in YourList: # Function has recieved List, so here it checks every object's ID
                if idInput == OBJ.ID:
                        attemptsLeft = 3
                        ifIdExists = True
                        while attemptsLeft >= 0: 
                            password = input("Enter your password: ")
                            if OBJ.Password == password:
                                print("Log in succeeded!")
                                return True
                            elif attemptsLeft == 0:
                                print("You have used all your attempts! Access Denied!")
                                return False
                            else:
                                attemptsLeft -= 1
                                print("You have left " + attemptsLeft + " attempts!")

        if ifIdExists == False:
            print("This ID doesn't exist!")
            return False

    @staticmethod
    def LogIn(ListOfAdmins, ListOfClients, CEOaccount):
            try:  
                idInput = int(input("Please enter your ID: "))
                if idInput > 1000:                              # Clients ID
                    result = Library2.PasswordCheck(ListOfClients, idInput)
                    if result == True:
                        Library2.clientsAccount(ListOfClients, ME)
                elif idInput > 10:                              # Admins ID
                    result = Library2.PasswordCheck(ListOfAdmins, idInput)
                    if result == True:
                        print("There should be admin's account!")
                else:                                           # CEO ID
                    if CEOaccount.ID == idInput:
                        passworD = input("Enter your password: ")
                        if CEOaccount.password == passworD:
                            print("There should be CEO's account!")
                        else:
                            print("Access Denied!")
            except ValueError:
                print("You must input ONLY DIGITS!")

    @staticmethod
    def clientsAccount(ListOfClients, ME):
        needRepeat = True
        while needRepeat == True:
            print
            ('''You have entered in your account!
                You have man options what to do:
                1. Send money to some account in this bank  (Enter 1)
                2. Take credit                              (Enter 2)
                3. Invest money and get back more           (Enter 3)
                4. Look at your history                     (Enter 4) 
            
                ''')
            try:
                choice = int(input("Enter 1, 2 or 3 to your choice"))
                if choice == 1:
                    Library3.sendMoney(ListOfClients, ME)
                elif choice == 2:
                    print("Take Credit")
                elif choice == 3:
                    print("Invest money")
                else:
                    raise ValueError            # Just prints out unique error message

                choice = input('Do you want log out? (Enter YES to go out) ')
                if choice == 'YES':
                    print('Logging out')
                    needRepeat = False
                
            except ValueError:
                print("You must input ONLY ONE DIGIT from 1 to 3!")

   
            