#Here only B class call his constructor but not A class constructor because we have not used super() function in B class constructor
# class A:
#     def __init__(self):
#         print("Constructor of class A")
# class B(A):
#     def __init__(self):    
    
#         print("Constructor of class B")
# b=B()
class A:
    def __init__(self):
        print("Constructor of class A")
class B(A):
    def __init__(self): 
        super().__init__()    #This will call the constructor of class A   
    
        print("Constructor of class B")
b=B()
