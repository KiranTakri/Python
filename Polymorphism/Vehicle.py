class Vehicle:
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car is starting")
class Bike(Vehicle):
    def start(self):
        print("Bike is starting")
class Bus(Vehicle):
    def start(self):
        print("Bus is starting")
v=[Car(),Bike(),Bus()]
for i in v:
    i.start()