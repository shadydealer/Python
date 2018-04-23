from contextlib import contextmanager

@contextmanager
def performance(file_name):
    file_handler = open(file_name,'a')
    
    yield 

    file_handler.close()