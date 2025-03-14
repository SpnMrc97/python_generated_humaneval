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

def check(candidate):

    # Check some simple cases
    assert candidate(1) == True, "First test error: " + str(candidate(1))
    assert candidate(2) == False, "Second test error: " + str(candidate(2))
    assert candidate(-1) == True, "Third test error: " + str(candidate(-1))
    assert candidate(64) == True, "Fourth test error: " + str(candidate(64))
    assert candidate(180) == False, "Fifth test error: " + str(candidate(180))
    assert candidate(1000) == True, "Sixth test error: " + str(candidate(1000))


    # Check some edge cases that are easy to work out by hand.
    assert candidate(0) == True, "1st edge test error: " + str(candidate(0))
    assert candidate(1729) == False, "2nd edge test error: " + str(candidate(1728))


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(iscube)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)