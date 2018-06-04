from Car import Car
from Driver import Driver

class Race():
    drivers = []
    crashChances = []
    
    def __init__(self, drivers = [], crashChances = []):
        if type(drivers) is not list:
            raise TypeError(f'Drivers must be of type {type(list)}\n')
        for driver in drivers:
            if type(driver) is not Driver:
                raise TypeError(f'Each element in the drivers list must be of type {type(driver)}\n')
        if type(crashChances) is not list:
            raise TypeError(f'CrashChances must be of type {type(list)}\n')
        for crashChance in crashChances:
            if type(crashChance) is not float:
                raise TypeError(f'Each element in the crashChances list must be of type {type(float)}\n')
            if crashChance < 0 or crashChance > 1:
                raise ValueError('Crash Chance must be in the interval [0;1].\n')

        self.drivers = drivers
        self.crashChances = crashChances

    def __str__(self):
        return f'Drivers: {str(self.drivers)}\n Crash Chances: {str(self.crashChances)}\n'
    def __repr__(self):
        return str(self)
