from Car import Car

class LightTruck(Car):
    def __init__(self,license):
        super().__init__(license)
        super().setCarName("LightTruck")
