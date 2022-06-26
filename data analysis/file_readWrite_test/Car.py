from sqlite3 import Row


class Car:
    def __init__(self,license):
        self.license = license
        self.enginePower = 0
        self.fileName= "mycars.txt"
        self.carName = ""
        self.numberOfCar = self.checkNoCars()

    def setEnginePower(self,enginePower):
        self.enginePower= enginePower
    
    def setCarName(self,carName):
        self.carName =carName

    def WriteTofile(self):
        write_str = self.license+"\t"+str(self.carName)+"\n"
        
        with open(self.fileName,"a") as fileWrite:
            fileWrite.writelines(write_str)


    def checkNoCars(self):
        with open(self.fileName, "r") as file:
            rows = file.readlines()
        return len(rows)
