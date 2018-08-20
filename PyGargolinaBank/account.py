class Account():
    def __init__(self, Currensy = "EUR", balance = 1000):
        self.Currensy = Currensy
        self.balance = balance

    def __str__(self):
        return("Account has {} {}!".format(self.balance, self.Currensy))

    @Currensy.setter
    def Currensy(self, value):
        isAllLetter = True
        value = str(value)
        if len(value) != 3:
            print("Currensy must contain 3 letters!")
        else:
            for h in value:
                if h.isalpha() == False:
                   isAllLetter = False

            if isAllLetter == False:
                print("Currensy must contain only letters!")
            else:
                value = value.upper()
                self.__Currensy = value


    


