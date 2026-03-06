class Bank:
    def __init__(self,_account_number,acoount_holder_namr,balance):
        self._account_number=_account_number
        self.account_holder_name=acoount_holder_namr
        self.balance=balance
    def show1(self):
        print("Account Number:", self._account_number)
    def show2(self):
        print("Account Holder Name:", self.account_holder_name)
    def __show3(self):
        print("Balance:", self.balance)
class info(Bank):
    def display(self):
        self.show1()
        self.show2()
        self.__show3()
info1=info(1234567890,"Kiran",10000)
info1.show1()
info1.show2()
info1._Bank__show3()
info1.display()

