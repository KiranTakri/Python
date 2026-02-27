class BankAccount:
    def account_type(self):
        print("This is a Bank Account")

class CurrentAccount(BankAccount):
    def account_type(self):
        print("This is a Current Account")


class SavingAccount(BankAccount):
    def account_type(self):
        print("This is a Saving Account")

class FixedDeposit(BankAccount):
    def account_type(self):
        print("This is a Fixed Deposit Account")


c1 = [CurrentAccount(), SavingAccount(), FixedDeposit()]
for account in c1:
    account.account_type()