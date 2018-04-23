def chain(iterableOne, iterableTwo):
    yield from iterableOne
    yield from iterableTwo

def main():
    print(list(chain([1,2,3], {'k':1})))

if __name__ == '__main__':
    main()
