from Car import Car

class Crown(Car):
    def __init__(self,license):
        super().__init__(license)
        super().setCarName("Crown")
        #super().setEnginePower(80)