def cycle(iterable):
    while True:
        yield from iterable

def main():
    endless = cycle(range(0,10))
    for item in endless:
        print(item)

if __name__ == '__main__':
    main()
