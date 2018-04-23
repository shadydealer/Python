
class Song:

    def __init__(self, *, title = None, artist = None, album = None, length=None):
        self.__title = title
        self.__artist = artist
        self.__album = album

        self.validate_length(length)
        self.__length = self.convert_length_to_int_list(length)

    def validate_length(self, length):
        data_as_str_list = length.split(':')
        self.__validate_length(data_as_str_list)

    def convert_length_to_int_list(self,length):
        
        length_as_str_list = length.split(':')
        result = self.__convert_length_to_int_list(length_as_str_list)
        result.reverse()
        return result

    def __convert_length_to_int_list(self, data):
        '''
        Converts the passed in str list to an int list.
        '''
        
        data_as_ints = []
    
        for time_unit in data:
            data_as_ints.append(int(time_unit))
    
        return data_as_ints

    def __validate_length(self, length):
        ''' Validates each time unit of the length list. '''
        
        length.reverse()

        if len(length) > 3:
            raise ValueError("Length must be hours:minutes:seconds.\n")
        try:
            length_as_ints = self.__convert_length_to_int_list(length)

        except TypeError:
            raise TypeError("Length values must be integers.\n")

        self.validate_minutes_or_seconds(length_as_ints[0])
        self.validate_minutes_or_seconds(length_as_ints[1])

        if len(length_as_ints) == 3:
            self.validate_hours(length_as_ints[2])

    def length(self,**kwargs):
        ''' Converts the length into one of the following time units:
                1) seconds
                2) minutes
                3) hours
            If no arguments were passed returns the string representation of self.__length
        '''
        
        if len(kwargs) == 0:
            return self.__length_str_repr()

        power_of_sixty = 1
        result = 0

        values = self.__extract_key(kwargs)

        if kwargs[values[0]] is True:

            for time_unit in range(values[1], len(self.__length)):
                result += power_of_sixty*self.__length[time_unit]
                power_of_sixty*=60

        return result

    def __length_str_repr(self):
        ''' Returns the string represention of self.__length. '''
        
        length_as_str = self.__convert_int_list_to_str(self.__length)
        length_as_str.reverse()
        length_str_repr = ':'.join(length_as_str)
        return length_str_repr

    def __extract_key(self, kwargs):
        ''' 
        Returns the a pair(key, begin), where key is the valid keyword
        and begin is where we should start iterating our __length list from.
        '''
        if len(kwargs) > 1:
            raise ValueError("Too many arguments. Chose only ONE of the following: seconds, minutes, hours.\n")

        key = None
        begin = 0
        
    
        if 'seconds' in kwargs:
                key = 'seconds'
        elif 'minutes' in kwargs:
            begin = 1
            key = 'minutes'
        elif 'hours' in kwargs:
            begin = 2
            key = 'hours'

        if key not in kwargs:
            raise ValueError("Arguments must be one of the following: seconds, minutes, hours.\n")

        return (key, begin)

    @staticmethod
    def validate_hours(hours):
        ''' Checks if the passed in integer is a valid hour time unit. '''
        
        if hours < 0:
            raise ValueError("Hours must be a positive integer.\n")

    @staticmethod
    def validate_minutes_or_seconds(time_unit):
        ''' Checks if the argument is a valid minutes/seconds time unit.'''
        
        if time_unit < 0 or time_unit > 59:
            raise ValueError("Minutes and seconds must be in the interval [0;59].\n")

    def __convert_int_list_to_str(self,int_list):
        result = []
        for integer in int_list:
            result.append(str(integer))
        return result

    def  __str__(self):
        length_str_repr = self.__length_str_repr()
        return f'{self.__artist} - {self.__title} from {self.__album} - {length_str_repr}.'

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return  {self._title == other.title and
                self.__artist == other.artist and
                self.alub == other.album and
                self.__length == other.length
                }