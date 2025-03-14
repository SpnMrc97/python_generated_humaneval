def add(x: int, y: int) -> int:
    """
    Add two numbers x and y.

    Parameters:
    x (int): The first number to add.
    y (int): The second number to add.

    Returns:
    int: The sum of x and y.

    Examples:
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

METADATA = {}


def check(candidate):
    import random

    assert candidate(0, 1) == 1
    assert candidate(1, 0) == 1
    assert candidate(2, 3) == 5
    assert candidate(5, 7) == 12
    assert candidate(7, 5) == 12

    for i in range(100):
        x, y = random.randint(0, 1000), random.randint(0, 1000)
        assert candidate(x, y) == x + y


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(add)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)