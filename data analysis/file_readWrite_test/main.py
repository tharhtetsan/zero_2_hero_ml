from LightTruck import LightTruck 
from Crown import Crown


car_licenses = []

fileName= "mycars.txt"
def checkNoCars():
        with open(fileName, "r") as file:
            rows = file.readlines()
            for currentRow in rows:
                carData = currentRow.split("\t")
                license_id =carData[0]
                car_licenses.append(license_id)
checkNoCars()







count = int(input("Enter number of cars : "))

for i in range(1,count+1+len(car_licenses),1):
    license_id = "000"+str(i)

    
    if (license_id in car_licenses):
        continue
    else:
        
        out_str = "Enter car type for "+license_id+" (0 or 1): "
        carType = int(input(out_str))
        
        carObj = None
        if carType == 0:
            carObj= Crown(license_id)
            carObj.WriteTofile()
        elif carType ==1:
            carObj= LightTruck(license_id)
            carObj.WriteTofile()
        else:
            print("****Please choose only available****")
        
