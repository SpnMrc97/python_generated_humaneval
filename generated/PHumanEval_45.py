def triangle_area(a, h):
    """
    Calculate the area of a triangle given the base and height.

    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("The base and height must be positive numbers.")
    
    area = (a * h) / 2
    return area
