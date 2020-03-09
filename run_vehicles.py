# import all the classes
from vehicle_class import *
from car_class import *
from plane_class import *
# create 2 vehicles instances

vehicle1 = Vehicle(5, 'Enough for a family')
vehicle2 = Vehicle(80, 'At least 80 bags')

# call methods and attributes to test
print('Vehicle 1')
print(vehicle1.accelerate())
print(vehicle1.breaking())
print('Passengers:', vehicle1.passengers)
print('Cargo:', vehicle1.cargo)
print(' ')
print("Vehicle 2")
print(vehicle2.accelerate())
print(vehicle2.breaking())
print('Passengers:', vehicle2.passengers)
print('Cargo:', vehicle2.cargo)
print(' ')
# create 2 car instances here
# make cars accelerate and make them break
# make car honk and park

car1 = Car(2, 'Very little', 'Ferrari', 180, 250)
car2 = Car(7, 'Enough for a family', 'Toyota Yarris', 140, 150)

print('Car 1')
print(car1.park())
print(car1.honk())
print(car1.accelerate())
print(car1.breaking())
print('Passengers:', car1.passengers)
print('Cargo:', car1.cargo)
print('Brand:', car1.brand)
print('Horsepower:', car1.horsepower, 'horses')
print('Max Speed:', car1.maxspeed, 'mph')
print(' ')
print('Car 2')
print(car2.park())
print(car2.honk())
print(car2.accelerate())
print(car2.breaking())
print('Passengers:', car2.passengers)
print('Cargo:', car2.cargo)
print('Brand:', car2.brand)
print('Horsepower:', car2.horsepower, 'horses')
print('Max Speed:', car2.maxspeed, 'mph')
print(' ')

# create 2 planes instances here
# make plane fly and land

plane1 = Plane(300, '300 peoples worth', 'Emirates', 'Long Haul')
plane2 = Plane(150, '150 peoples worth', 'EasyJet', 'Short Haul')

print('Plane 1')
print(plane1.takeoff())
print(plane1.touchdown())
print(plane1.accelerate())
print(plane1.breaking())
print('Passengers:', plane1.passengers)
print('Cargo:', plane1.cargo)
print('Airline:', plane1.airline)
print('Distance:', plane1.distance)
print(' ')
print('Plane 2')
print(plane2.takeoff())
print(plane2.touchdown())
print(plane2.accelerate())
print(plane2.breaking())
print('Passengers:', plane2.passengers)
print('Cargo:', plane2.cargo)
print('Airline:', plane2.airline)
print('Distance:', plane2.distance)