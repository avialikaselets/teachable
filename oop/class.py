#!/usr/bin/python3


class BankAccount:

    def __init__(self,
                 x_first_name,
                 x_last_name,
                 x_account_number,
                 x_deposit_amount):
        self.__first_name = x_first_name
        self.__last_name = x_last_name
        self.__account_number = x_account_number
        self.__deposit_amount = x_deposit_amount

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_account_number(self):
        return self.__account_number

    def get_deposit_amount(self):
        return self.__deposit_amount

    def set_first_name(self, x_first_name):
        self.__first_name = x_first_name

    def set_last_name(self, x_last_name):
        self.__last_name = x_last_name

    def set_account_number(self, x_account_number):
        self.__account_number = x_account_number

    def set_deposit_amount(self, x_deposit_amount):
        self.__deposit_amount = x_deposit_amount


def main():
    clients = []

    for i in range(3):
        print("Input data for customer", i+1)
        first_name = input("Specify first name: ")
        last_name = input("Specify last name: ")
        account_number = input("Specify account number: ")
        deposit_amount = input("Specify deposit amount: ")
        clients.append(BankAccount(first_name, last_name, account_number,
                                   deposit_amount))
        print("\n")

    for client in clients:
        print("First name: ", client.get_first_name(), "\n"
              "Last name: ", client.get_last_name(), "\n"
              "Account number: ", client.get_account_number(), "\n"
              "Deposit amount: ", client.get_deposit_amount())

    clients[1].set_first_name("Jerry")

    for client in clients:
        print("First name: ", client.get_first_name(), "\n"
              "Last name: ", client.get_last_name(), "\n"
              "Account number: ", client.get_account_number(), "\n"
              "Deposit amount: ", client.get_deposit_amount())


main()
# Atom+GitHub Test 8
