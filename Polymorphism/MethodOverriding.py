class Animal:
    def make_sound(self):
        
        print("Animal makes a sound")
class Dog(Animal):
    
    def make_sound(self):
        super().make_sound()
        print("Dog barks")
class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

A=Cat()
A.make_sound()
d1=Dog()
d1.make_sound()