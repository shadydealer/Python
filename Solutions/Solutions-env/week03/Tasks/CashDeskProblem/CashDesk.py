from BillBatch import Bill, BillBatch

class CashDesk():

    drawer = {}

    def __take_bill(self, money):
        if money in self.drawer:
            self.drawer.update({money: self.drawer[money] + 1})
        else:
            self.drawer.update({money: 1})
        
    def take_money(self, money):
        if type(money) is Bill:
            self.__take_bill(money)
        elif type(money) is BillBatch:
            for bill in money:
                self.__take_bill(bill)
        else:
            raise TypeError(' \'money\' keyword must be'
                            f' assigned a value of type:{type(Bill)} or {type(BillBatch)}')
    
    def __init__(self, money = None):
        if money is None:
            return 
        self.take_money(money)
    
    def total(self):
        amount = 0
        for bill in self.drawer:
            amount += bill.amount * self.drawer[bill]
        return amount

    def __repr__(self):
        return str(self.drawer)

    def inspect(self):
        for bill in self.drawer:
            print(f'{bill.amount}$ bills - {self.drawer[bill]}')
