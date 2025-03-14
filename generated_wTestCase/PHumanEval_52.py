def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of integers.
        t (int): The threshold integer.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(x < t for x in l)

METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10], 100)
    assert not candidate([1, 20, 4, 10], 5)
    assert candidate([1, 20, 4, 10], 21)
    assert candidate([1, 20, 4, 10], 22)
    assert candidate([1, 8, 4, 10], 11)
    assert not candidate([1, 8, 4, 10], 10)


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(below_threshold)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)