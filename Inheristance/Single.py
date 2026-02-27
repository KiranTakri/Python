class Parent:
    def show():
        print("Parent class")
class Child(Parent):
    def display():
        print("Child class")
c=Child
c.display()
c.show()