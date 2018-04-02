from Bill import Bill
from BillBatch import BillBatch
from CashDesk import CashDesk

def main():
    #a = Bill(20)
    #print(a)
    #print(repr(a))
    #b = Bill(30)
    #a == 2
    #print(a==b)
    
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total()) # 390
    desk.inspect()
    #print(phatStack.total())
if __name__ == '__main__':
    main()
