from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    

class Car(Vehicle):
    def move(self):
        return "The car is driving."
        
class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is pedaling."

class Boat(Vehicle):
    def move(self):
        return "The boat is sailing."

def start_vehicle(vehicle: Vehicle):
    print(vehicle.move())


# Test your implementation
car = Car()
bicycle = Bicycle()
boat = Boat()

start_vehicle(car)
start_vehicle(bicycle)
start_vehicle(boat)