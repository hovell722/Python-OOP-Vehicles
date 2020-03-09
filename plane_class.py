from vehicle_class import *


class Plane(Vehicle):

    def __init__(self, passengers, cargo, airline, distance):
        super().__init__(passengers, cargo)
        self.airline = airline
        self.distance = distance

    def takeoff(self):
        return 'NNNNNEEEEEEEEOOOOOOOOWWWWWWWW'

    def touchdown(self):
        return 'CLAP CLAP CLAP CLAP'