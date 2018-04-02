import sys

def cat(arguments):
    file = open(arguments, 'r')
    content = file.read()
    file.close()
    return content


def main():
    print(cat(sys.argv[1]))

if __name__ == '__main__' :
    main()
