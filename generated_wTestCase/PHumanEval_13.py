def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(greatest_common_divisor)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)