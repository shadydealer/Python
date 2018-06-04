import datetime
import time

class Performance:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_handler = None
        self.timer = None
        
    def __time__(self):
        return time.time()

    def __log__(self):
        currDateTime = datetime.datetime.now()
        self.file_handler.write('Date ' + str(currDateTime) + 
                                '. Execution time: ' + str(self.timer) + '\n')

    def __enter__(self):
        self.timer = self.__time__()
        self.file_handler = open(self.file_name, 'a')
        return self.timer

    def __exit__(self, exc_type, exc_value, traceback):
        self.timer = self.__time__() - self.timer
        self.__log__()
        self.file_handler.close()
        return True