#!/usr/bin/python3
# from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

'''
class BankAccount:

    def __init__(self, x_deposit_amount):
        self.__deposit_amount = x_deposit_amount

    def get_deposit_amount(self):
        return self.__deposit_amount

    def deposit_funds(self, x_amount):
        self.__deposit_amount += x_amount

    def withdraw_funds(self, x_amount):
        self.__deposit_amount -= x_amount


class SavingsAccount(BankAccount):

    def __init__(self, x_deposit_amount):
        BankAccount.__init__(self, x_deposit_amount)
'''


def main():
    savings_account_01 = SavingsAccount(100)
    print("Saving account balance: $", savings_account_01.get_balance(),
          sep="")

    checking_account_01 = CheckingAccount(500)
    print("Checking account balance: $", checking_account_01.get_balance(),
          sep="")

    print("")

    print("Making deposit into checking account for 75$...")
    checking_account_01.deposit_funds(75)
    print("New checking account balance: $", checking_account_01.get_balance(),
          sep="")

    print("")

    print("Making deposit into savings account for 300$...")
    savings_account_01.deposit_funds(300)
    print("New savings account balance: $", savings_account_01.get_balance(),
          sep="")

    print("")


main()
