def any_int(x, y, z):
    """
    Takes three numbers and returns True if one of the numbers is equal to the sum of the other two
    and all numbers are integers. Returns False in any other cases.

    Examples:
    any_int(5, 2, 7) ➞ True
    any_int(3, 2, 2) ➞ False
    any_int(3, -2, 1) ➞ True
    any_int(3.6, -2.2, 2) ➞ False
    """
    
    # Check if all inputs are integers
    if all(isinstance(i, int) for i in (x, y, z)):
        # Check if any one of the numbers is equal to the sum of the other two
        if x == y + z or y == x + z or z == x + y:
            return True
    return False
