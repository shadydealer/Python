from Car import Car

class Driver():
    name = ""
    car = Car()
    def __init__(self,name = "", car = Car()):
        if type(name) is not str:
            raise TypeError(f'Name must be of type {type(str)}\n')
        if type(car) is not Car:
            raise TypeError(f'Car must of type {type(car)}\n')
        self.name = name
        self.car = car
    
    def __str__(self):
        return f'driver: {self.name}, Car: <{str(self.car)}>'
    def __repr__(self):
        return str(self)
