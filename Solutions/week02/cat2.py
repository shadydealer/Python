import sys

def cat2(arguments):
    with open(arguments) as file:
        return file.read()

def main():
    for i in range(1,len(sys.argv)):
        print(cat2(sys.argv[i]))

if __name__ == '__main__':
    main()
