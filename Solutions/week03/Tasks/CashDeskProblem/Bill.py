
class Bill():
    
    amount = 0

    def __init__(self, amount):
        if type(amount) is not int:
            raise TypeError("Bill amount HAS to be of integral type.\n")
        if amount < 0:
            raise ValueError("Bill amount cannot be negative.\n")
        
        self.amount = amount

    def __str__(self):
        return f'A {self.amount}$ bill'
    
    def __int__(self):
        return self.amount
    
    def __repr__(self):
        return f'A {self.amount}$ bill'

    def __eq__(self, other):
        if type(other) is not Bill:
            raise TypeError(f'Cannot compare {type(self)} to {type(other)}.\n')
        return self.amount == other.amount

    def __hash__(self):
        return self.amount
