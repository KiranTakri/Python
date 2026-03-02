from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        print("Engine stopped.")
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started.")
car = Car()
car.start_engine()
car.stop_engine()
motorcycle = Motorcycle()
motorcycle.start_engine()
motorcycle.stop_engine()
