class Father:
    def __init__(self):
        print("Constructor of Father class")
class Son1(Father):
    def __init__(self):
        super().__init__()  #This will call the constructor of Father class
        print("Constructor of Son1 class")
class Son2(Father):
    def __init__(self):
        super().__init__()  #This will call the constructor of Father class
        print("Constructor of Son2 class")
s1=Son1()
s2=Son2()

   