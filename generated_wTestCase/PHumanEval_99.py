def closest_integer(value):
    """
    Convert a string representing a number to the closest integer according to specified rounding rules.

    Args:
    value (str): A string representation of a numeric value.

    Returns:
    int: The closest integer, rounding away from zero if equidistant.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    """
    number = float(value)
    if number > 0:
        return int(number + 0.5)
    else:
        return int(number - 0.5)

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(closest_integer)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)