import sys

def sum_file(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            for number in line.split():
                sum +=int(number)
    return sum

def main():
    print(sum_file(sys.argv[1]))


if __name__ == '__main__' :
    main()