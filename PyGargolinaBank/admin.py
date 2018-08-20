from client import Client

class Admin(Client):
    def __init__(self, Name, Surname, HomeAdress, PassportNumber, Password, ID):
        Client.__init__(self, Name, Surname, HomeAdress, PassportNumber, Password, ID)
    
                                                                                                                                # In here passportNumber = Gargolina Number
    def __str__(self):                          # I am too lazy to write a whole new function just because one variable does differ in admin class from client class 
        return super().__str__() + "There was a mistake - Gargolina number was mentoined as passport number! Gargolina number is {}!".format(self.PassportNumber)
    
