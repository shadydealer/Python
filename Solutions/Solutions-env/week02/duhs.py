import sys
from os import listdir
from os.path import isfile, getsize

def dir_size_bytes(directory):
    _sum = 0
    for entity in listdir(directory):
        full_path = directory + '/' +entity
        print(full_path)
        _sum += getsize(full_path) if isfile(full_path) else dir_size_bytes(full_path)
    return _sum

def switch(x):
    return  {
        'B':0,
        'KB':1,
        'MB':2,
        'GB':3
    }.get(x,3)

def main():
    size = dir_size_bytes(sys.argv[1])
    
    print(size, end = '')
    
    counter = 0
    while size > 1024:
        counter +=1
        size /=1024
    print(switch(counter))

if __name__ == '__main__':
    main()