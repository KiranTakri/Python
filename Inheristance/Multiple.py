class Dog:
    def show():
        print("Dog class")
class Cat(Dog):
    def display():
        print("Cat class")
class Cow(Cat):
    def shows():
        print("Cow Class")
c=Cow
c.shows()
c.display()
c.show()