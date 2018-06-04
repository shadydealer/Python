from Bill import Bill

class BillBatch():
    
    wallet = []

    def __init__(self, batch):
        if type(batch) is not list:
            raise TypeError(f'Batch must be of type {type(list)}')
        if not all(type(bill) is Bill for bill in batch):
            raise TypeError(f'Batch elements must of type {type(Bill)}')
        self.wallet = batch

    def __len__(self):
        return len(self.wallet)
    
    def __getitem__(self, index):
        if type(index) is not int:
            raise TypeError(f'Key should be of type {type(int)}')
        if index >= len(self.wallet) or index < 0:
            raise IndexError(f'Key should be in interval [0;{len(self.wallet)})')
        return self.wallet[index]

    def total(self):
        totalAmount = 0
        for bill in self.wallet:
            totalAmount+= bill.amount
        return totalAmount

    def __repr__(self):
        return str(self.wallet)