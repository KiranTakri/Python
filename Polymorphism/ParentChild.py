class Parent:
    def show(self):
        print("Parent name is Parent")
        print("Parent age is 50")
class Child(Parent):
    
    def show(self):
        super().show()
        print("Child name is Child")
        print("Child age is 20")
c=Child()
c.show()