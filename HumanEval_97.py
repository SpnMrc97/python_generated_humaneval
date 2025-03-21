def multiply(a, b):
    # Get the unit digit of `a`
    unit_digit_a = abs(a) % 10
    
    # Get the unit digit of `b`
    unit_digit_b = abs(b) % 10
    
    # Return the product of the unit digits
    return unit_digit_a * unit_digit_b
