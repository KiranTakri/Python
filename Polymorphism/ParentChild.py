class Parent:
    def show(self):
        print("Parent name is Parent")
        print("Parent age is 50")
class Child1(Parent):
    
    def show(self):
        super().show()
        print("Child name is Child1")
        print("Child age is 20")

class Child2(Parent):
    def show(self):
        super().show()
        print("Child name is Child2")
        print("Child age is 24")
c=Child1()
c.show()
c=Child2()
c.show()