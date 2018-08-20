from account import Account

class Client():
    def __init__(self, Name = "", Surname = "", HomeAdress = "", PassportNumber = "", Password = "", ID = -1): 
        self.Name = Name                    # object can be created with random values
        self.Surname = Surname
        self.HomeAdress = HomeAdress
        self.PassportNumber = PassportNumber
        self.Password = Password
        self.ID = ID 
        self.myAccount = Account()

    def __str__(self):
        return("{} name is {} {} and your home adress is {} and your passport number is {} and your password is {} ! To Log in your bank account you should remember your ID - {} and your password!"
        .format(type(self).__name__, self.Name, self.Surname, self.HomeAdress, self.PassportNumber, self.Password, self.ID))

    


    
