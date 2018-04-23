def compress(iterable, mask):
    for element in zip(iterable,mask):
        if element[1]:
            yield element[0]

def main():
    print(list(compress(["Ivo", "Rado", "Panda"], [False, True, False])))
    pass

if __name__ == '__main__':
    main()