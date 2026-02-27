class A:
    def __init__(self):
        print("Constructor of class A")
class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of class B") 
class C(B):
    def __init__(self):
        super().__init__()
        print("Constructor of class C")
c=C()
