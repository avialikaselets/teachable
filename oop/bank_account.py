class BankAccount:

    def __init__(self, x_balance):
        self.__balance = x_balance

    def get_balance(self):
        return self.__balance

    def deposit_funds(self, x_amount):
        self.__balance += x_amount

    def withdraw_funds(self, x_amount):
        self.__balance -= x_amount
