# define vehicle class here

# Characteristics:
# Number of passengers
# Size of cargo

# Methods:
# Accelerate
# Break

class Vehicle():

    def __init__(self, passengers, cargo):
        self.passengers = passengers
        self.cargo = cargo

    def accelerate(self):
        return 'VROOOOOOOOM'

    def breaking(self):
        return 'SKRRRRT'


