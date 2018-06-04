import pdb
import types
import collections

def deep_find(data, key):
    result = None

    for child in data:
        if type(data) is dict:
            if (isinstance(data[child], collections.Iterable) and
                type(data[child]) is not str):
            
                result = deep_find(data[child], key)
                break

            elif child == key:
                return data[child]
        
        elif (isinstance(data, collections.Iterable) and
             type(data) is not str):
            result = deep_find(child,key)
            break
            
    return result

def main():
    test_dict = {'1':
                    {
                    '2':[{
                        '3':{
                            '4':'GG',
                            '4.1':'Nope'
                            },
                        '3.1': 'haHAA',
                        '4.1':'b'
                        }]
                    }
                }
    print(deep_find(test_dict, '4.1'))

if __name__ == '__main__':
    main()