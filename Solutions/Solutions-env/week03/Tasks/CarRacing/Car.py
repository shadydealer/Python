
class Car():
    brand = ""
    model = ""
    maxSpeed = 0

    def __init__(self, brand = "", model="", maxSpeed = 0):
        if type(brand) is not str:
            raise TypeError(f'Brand must be of type {type(str)}.\n')
        if type(model) is not str:
            raise TypeError(f'Model must be of type {type(str)}.\n')
        if type(maxSpeed) is not int:
            raise TypeError(f'Speed must be of type {type(int)}.\n')
        if maxSpeed < 0:
            raise ValueError('Speed value must be a positive integer.\n')
        
        self.brand = brand
        self.model = model
        self.maxSpeed = maxSpeed

    def __int__(self):
        return self.maxSpeed
    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}, max speed: {self.maxSpeed}'
    def __repr__(self):
        return str(self)