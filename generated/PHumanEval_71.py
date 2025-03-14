import math

def triangle_area(a, b, c):
    """
    Calculate the area of a triangle based on the lengths of its sides.
    
    :param a: Length of the first side of the triangle
    :param b: Length of the second side of the triangle
    :param c: Length of the third side of the triangle
    :return: The area of the triangle rounded to 2 decimal places if valid, otherwise -1
    """
    # Check for valid triangle using the triangle inequality theorem
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2)
    else:
        return -1
