
from Car import Car
from Driver import Driver
from Race import Race

def main():
    c1 = Car(brand = "opel", model = "astra", maxSpeed = 22)
    c2 = Car()
    print(int(c1))
    print(c2)

    d1 = Driver()
    d2 = Driver("Ivan", c1)
    print(d1)
    print(d2)

    r1 = Race()
if __name__ == '__main__':
    main()
    