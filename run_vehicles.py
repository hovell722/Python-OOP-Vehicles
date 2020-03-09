# import all the classes
from vehicle_class import *
from car_class import *
from plane_class import *
# create 2 vehicles instances

vehicle1 = Vehicle(5, 'Enough for a family')
vehicle2 = Vehicle(80, 'At least 80 bags')

# call methods and attributes to test

print(vehicle1.accelerate())
print(vehicle1.breaking())
print(vehicle2.accelerate())
print(vehicle2.breaking())

# create 2 car instances here
# make cars accelerate and make them break
# make car honk and park

car1 = Car(2, 'Very little', 'Ferrari', 180, 250)
car2 = Car(7, 'Enough for a family', 'Toyota Yarris', 140, 150)

print(car1.park())
print(car1.honk())
print(car2.park())
print(car2.honk())


# create 2 planes instances here
# make plane fly and land

plane1 = Plane(300, '300 peoples worth', 'Emirates', 'Long Haul')
plane2 = Plane(150, '150 peoples worth', 'EasyJet', 'Short Haul')

print(plane1.takeoff())
print(plane1.touchdown())
print(plane2.takeoff())
print(plane2.touchdown())