from car import Car

class BMW(Car):
    def __init__(self,license):
        self.license = license
        super().__init__(self.license, "v90",3000)
        
    def tax(self):
        tax = 8
        licenseCost = 2
        
        totalCost = (tax/100)*self.price + self.price
        totalCost = (licenseCost/100)*self.price +  totalCost
        return totalCost


class LightTruck(Car):
    def __init__(self,license):
        self.license = license
        super().__init__(self.license,"v50",1500)
    
    def tax(self):
        tax = 5
        
        totalCost = (tax/100)*self.price + self.price
        return totalCost