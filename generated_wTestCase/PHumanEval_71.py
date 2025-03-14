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

def check(candidate):

    # Check some simple cases
    assert candidate(3, 4, 5) == 6.00, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1, 2, 10) == -1
    assert candidate(4, 8, 5) == 8.18
    assert candidate(2, 2, 2) == 1.73
    assert candidate(1, 2, 3) == -1
    assert candidate(10, 5, 7) == 16.25
    assert candidate(2, 6, 3) == -1

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1, 1) == 0.43, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(2, 2, 10) == -1


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(triangle_area)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)