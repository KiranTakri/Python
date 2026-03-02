class dog:
    def sound(self):
        print("dogs bark ")
class cat:
    def sound(self):
        print("cats meow")
def show_sound(animal):
    animal.sound()
show_sound(dog())
show_sound(cat())
        