#!/usr/bin/python3
from bank_account import BankAccount
from savings_account import SavingsAccount

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
    account_01 = BankAccount(500)
    print(account_01.get_balance())

    savings_account_01 = SavingsAccount(300)
    print(savings_account_01.get_balance())


main()
