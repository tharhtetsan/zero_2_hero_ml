from cars_types.carTypes import *



car1 = BMW("v001")
car2 = LightTruck("L001")

cars = []
cars.append(car1)
cars.append(car2)

totalCost = 0 
for car in cars:
    car.display()
    totalCost = car.tax()+totalCost
print("Total Cost :",totalCost)