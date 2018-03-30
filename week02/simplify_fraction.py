def gcd(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot mod with zero.")
    t = 0
    while b != 0:
        t = b
        b = a% b
        a = t
    return a

def simplify_fraction(fraction):
    if fraction[1] == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")

    greatest_common_divider = gcd(fraction[0], fraction[1])
    result_nom = fraction[0] // greatest_common_divider
    result_denom = fraction[1] //  greatest_common_divider

    return (result_nom, result_denom)

def read_input():
    
    is_number = False
    
    fraction = ""

    while not is_number:
        fraction = input()
        try:
            fraction = tuple(map(int, fraction.split()))
            is_number = True
        except ValueError:
            print("Please enter two numbers.")
    
    return fraction

#fraction = read_input()