class Category():
    
    def __init__(self, category, amount):
        if type(category) is not str:
            raise TypeError(f'Category must be of type {type(str)}\n')
        if type(amount) is not float:
            raise TypeError(f'Amount must be of type {type(float)}\n')
        self.__category = category
        self.__amount = amount

    def __str__(self):
        return f'{self.__amount}, {self.__category}'
    def __hash__(self):
        return self.__category
    def __int__(self):
        return self.__amount

class Income(Category):
    def __init__(self, category, amount):
        super().__init__(category, amount)
    
    def __str__(self):
        return f'{super().__str__()}, New Income'

    def __repr__(self):
        return str(self)

class Expense(Category):
    def __init__(self, category, amount):
        super().__init__(category, amount)
    
    def __str__(self):
        return f'{super().__str__()}, New Expense'
    
    def __repr__(self):
        return str(self)

