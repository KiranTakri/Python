class WelcomeDrinks:
    def menu(self):
        print("This is the welcome drinks menu")
class Starter:
    def menu(self):
        print("This is the starter menu")
class MainCourse:
    def menu(self):
        print("This is the main course menu")
class Dessert:
    def menu(self):
        print("This is the dessert menu")
def MainMenu(Resturant):
    Resturant.menu()
MainMenu(WelcomeDrinks())
MainMenu(Starter()) 
MainMenu(MainCourse())
MainMenu(Dessert())
