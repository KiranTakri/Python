class emp:
    def __init__(self,id,name,age,BankAccount):
        self.id=id
        self.name=name
        self.age=age
        self.BankAccount=BankAccount
    def Idshow1(self):
        print("ID:",self.id)
    def Nameshow1(self):
        print("Name:",self.name)
    def Ageshow1(self):
        print("Age:",self.age)
    def __BankAccountshow1(self):
        print("Bank Account:",self.BankAccount)
class info(emp):
    def display(self):
        self.Idshow1()
        self.Nameshow1()
        self.Ageshow1()
    def display1(self):
        self.__BankAccountshow1()
# e=emp(101,"Kiran",25,1234567890)
# e.Ageshow1()
# e.Idshow1()
# e.Nameshow1()
# e.__BankAccountshow1()
Info1=info(101,"Kiran",25,1234567890)   
Info1.display()
Info1.display1()