import math

def closest_integer(value):
    # Convert the input string to a float
    number = float(value)
    
    # Round away from zero
    if number > 0:
        return math.floor(number + 0.5)
    else:
        return math.ceil(number - 0.5)
