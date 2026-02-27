class Bank:
    def Customerdetails(self):
        print("Bank class")


class Savingaccoun(Bank):
    def Savingaccountdetails(self):
        print("Saving account class")


class Currentaccount(Bank):
    def Currentaccountdetails(self):
        print("Current account class")
s=Savingaccoun()
s.Customerdetails()
s.Savingaccountdetails()
c=Currentaccount()
c.Customerdetails() 
c.Currentaccountdetails()