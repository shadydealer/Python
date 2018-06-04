import sys
from random import randint

def generate_random_numbers(filename, n):
    n = int(n)
    with open(filename,'w+') as file:
        for i in range (n):
            file.write(str(randint(1,1000)) + " ")

def main():
    generate_random_numbers(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()