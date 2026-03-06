from abc import ABC, abstractmethod
class Resturant(ABC):
    @abstractmethod
    def order(self):
        pass
    def receive_order(self):
        print("Order received.")
class Veg(Resturant):
    def order(self):
        print("Veg order placed.")
class NonVeg(Resturant):
     def order(self):
         print("Non-Veg order placed.")
class SeaFood(Resturant):
    def order(self):
        print("Seafood order placed.")
class FastFood(Resturant):
    def order(self):
        print("Fast Food order placed.")
veg = Veg()
veg.order()
veg.receive_order()
nonveg = NonVeg()
nonveg.order()
nonveg.receive_order()
seafood = SeaFood()
seafood.order()
seafood.receive_order()
fastfood = FastFood()
fastfood.order()
fastfood.receive_order()
