def any_int(x, y, z):
    # Check if all numbers are integers
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False

    # Check if one number is equal to the sum of the other two
    return x == y + z or y == x + z or z == x + y
