# import my vehicle class

from vehicle_class import *

# define car class here and make it inherit the vehicle

# Characteristics:
# brand
# horsepower
# max speed

# Methods:
# park
# honk

class Car(Vehicle):

    def __init__(self, passengers, cargo, brand, horsepower, maxspeed):
        super().__init__(passengers, cargo)
        self.brand = brand
        self.horsepower = horsepower
        self.maxspeed = maxspeed

    def park(self):
        return 'DING DING DING'

    def honk(self):
        return 'BEEP BEEP'