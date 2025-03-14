def multiply(a, b):
    """
    Takes two integers and returns the product of their unit digits.
    
    :param a: First integer
    :param b: Second integer
    :return: Product of the unit digits of a and b
    """
    # Get the absolute value of the unit digits
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    
    # Return the product of the unit digits
    return unit_digit_a * unit_digit_b
