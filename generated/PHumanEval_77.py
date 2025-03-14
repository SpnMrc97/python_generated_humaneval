def iscube(a):
    """
    Determine if the provided integer is a perfect cube.

    Parameters:
    a (int): The integer to check if it is a perfect cube.

    Returns:
    bool: True if 'a' is a perfect cube, False otherwise.
    """
    if a < 0:
        # For negative numbers, make the number positive and check
        # then return True if it is a perfect cube.
        cube_root = int(round(abs(a) ** (1/3)))
        return cube_root ** 3 == abs(a)
    else:
        # For non-negative numbers, directly check if it is a perfect cube.
        cube_root = int(round(a ** (1/3)))
        return cube_root ** 3 == a
