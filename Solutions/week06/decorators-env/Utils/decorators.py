from functools import  wraps
import datetime
import time

def accepts(*types):
    def accepter(func):
        def check_arguments(*args):
            if len(types) != len(args):
                raise ValueError("Number of arguments in the decorator\
                                 and in the called function do not match.\n")

            for curr_type, curr_argument in zip(types, args):
                if type(curr_argument) is not curr_type:
                    raise TypeError(f'Argument {curr_argument}'
                                    f' is of type {type(curr_argument)}'
                                    f' expected type {curr_type}.\n')
            return func(*args)
        return check_arguments
    return accepter

def encrypt(shift):
    def accepter(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pre_cipher = func(*args, **kwargs)
            
            def ceiser_cipher(string):
                post_cipher = ''

                base = 256

                for char in string:
                    char_in_ascii = ord(char)
                    if char_in_ascii >= ord('A') and char_in_ascii <= ord('Z'):
                        char_in_ascii += shift
                        base = ord('Z')
                    elif char_in_ascii >= ord('a') and char_in_ascii <=ord('z'):
                        char_in_ascii += shift
                        base = ord('z')

                    post_cipher += chr(char_in_ascii % base)
                return post_cipher
            
            return ceiser_cipher(pre_cipher)

        return wrapper

    return accepter

def log(file_name):
    def accepter(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        with open(file_name, 'a') as file:
            file.write(f'{func.__name__} was called {datetime.datetime.now()}\n')

        return wrapper
    return accepter

def performance(file_name):
    def accepter(func):
        def wrapper(*args, **kwargs):
            def timer():
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                return (start - end)
            return timer
            
            with open(file_name, 'a') as file:
                file.write(f'{func.__name__} was called and took {wrapper()} seconds to complete.\n')

        return wrapper
    return accepter