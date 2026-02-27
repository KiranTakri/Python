class Father:
    def __init__(self):
        print("Constructor of Father class")

class Mother:
    def __init__(self):
        print("Constructor of Mother class")
class Son(Father,Mother):
    def __init__(self):
        super().__init__()  #This will call the constructor of Father class because it is the first parent class of Son class
        super().__init__()  #This will call the constructor of Mother class because it is the second parent class of Son class
        print("Constructor of Son class")
s=Son()
    