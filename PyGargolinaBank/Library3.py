from client import Client
from admin import Admin
from CEO import CEO
import sqlite3
import sys

class Library3():
    
    @staticmethod
    def sendMoney(ListOfClients, ME):
        TargetID = input('Please enter ID of account where you want to send money:  ')
        idExists = False
        for client in ListOfClients:
            if client.ID  == TargetID:
                idExists = True
                try:
                    TransferAmmount = int(input("Enter your transfer ammoount:  "))
                    if ME.myAccount.balance < TransferAmmount:
                        print("You don't have enough money!")
                    else:
                        client.myAccount.balance += TransferAmmount
                        ME.myAccount.balance -= TransferAmmount


                except ValueError:
                    print("You must input ONLY DIGITS!")

    @staticmethod
    def TakeCredit(ME):
        credit = input("How much money you want to borrow: ")
        Me.myAccount.balance += credit
        Currensy1 = ME.myAccount.Currensy
        print("You took {} {} credit. Now you have {} {} in your account!".format(credit, Currensy1, ME.myAccount.balance, Currensy1))
        print("For your credit you will have 7% cost of total ammount!")
        credit = float(credit)       
        credit *= 1.07
        Me.myAccount.balance -= credit
        print("You returned credit! Now you have {} {} in your account!".format(ME.myAccount.balance, Currensy1))

    @staticmethod
    def InvestMoney(ME):
        investment = input("How much money you want to invest: ")
        Me.myAccount.balance -= investment
        Currensy1 = ME.myAccount.Currensy
        print("You took {} {} investment. Now you have {} {} in your account!".format(investment, Currensy1, ME.myAccount.balance, Currensy1))
        print("For your investment you will have 2% earn of total ammount!")
        investment = float(credit)       
        investment *= 1.02
        Me.myAccount.balance += investment
        print("You returned credit! Now you have {} {} in your account!".format(ME.myAccount.balance, Currensy1))





