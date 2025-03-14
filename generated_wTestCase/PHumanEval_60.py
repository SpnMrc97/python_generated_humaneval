def sum_to_n(n: int) -> int:
    """Calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the range to sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
    """
    return n * (n + 1) // 2

METADATA = {}


def check(candidate):
    assert candidate(1) == 1
    assert candidate(6) == 21
    assert candidate(11) == 66
    assert candidate(30) == 465
    assert candidate(100) == 5050


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(sum_to_n)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)