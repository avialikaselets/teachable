from bank_account import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, x_balance):
        BankAccount.__init__(self, x_balance)
