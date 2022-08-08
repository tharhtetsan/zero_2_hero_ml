class Car:
    def __init__(self,license,epower, price):
        self.license = license
        self.engine_power = epower
        self.price = price
    
    def display(self):
        str_out = "This has "+str(self.engine_power,)+ " and cost : "+str(self.price)
        print(str_out)