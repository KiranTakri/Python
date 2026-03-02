class Animal:
    def Sound(self):
        pass
class Dog(Animal):
    def Sound(self):
        print("Dog is barking")
class Cat (Animal):
    def Sound(self):
        print("Cat is meowing")
c=Cat()
c.Sound()
d=Dog()
d.Sound()
                
            

