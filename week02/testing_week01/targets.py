import math

INPUT_NOT_NUMBER = "Input was not a number."

def sum_of_digits(number):
    
    if type(number) is not int:
        raise ValueError(INPUT_NOT_NUMBER)
    
    number = abs(int(number))

    _sum = 0
    while number > 0:
        _sum += number%10
        number //=10

    return _sum


def to_digits(number):
    
    if type(number) is not int:
        raise ValueError(INPUT_NOT_NUMBER)
    
    result  = []

    while number > 0:
        result.append((number)%10)    
        number//=10

    result.reverse()
    return result

def to_number(sequence):
    number = 0

    for digit in sequence:
        number += digit
        number *=10    
    number //=10

    return number

def fact_digits(number):
    
    if type(number) is not int:
        raise ValueError(INPUT_NOT_NUMBER)

    _sum = 0
    while number > 0 :
        _sum += math.factorial((number %10))
        number //=10
    return _sum

def nth_fibonacci(number):
    if number == 1 or number == 2:
        return 1
    
    return nth_fibonacci(number -1) + nth_fibonacci(number-2)

#number = input()
#sum_of_digits(number)
#print(to_digits(20))

def fib_list(number):
    if type(number) is not int or number <= 0:
        raise ValueError(INPUT_NOT_NUMBER)
    
    result = [nth_fibonacci(i) for i in range(1,number +1)]
    return result

#print([nth_fibonacci(i) for i in range(1,11)])