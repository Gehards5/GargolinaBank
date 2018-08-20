class CEO(object):
    def __init__(self, name = 'Someone', surname = 'Unknown', ID = 1, password = "ThisIsNotWhatYouThink!ThisIsMchMuchWorse@"):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.password = password

    def __str__(self):
        return ("{} name is {} {} and your password is {} ! To Log in your bank account you should remember your ID - {} and your password!"
        .format(type(self).__name__, self.Name, self.Surname, self.Password, self.ID))
