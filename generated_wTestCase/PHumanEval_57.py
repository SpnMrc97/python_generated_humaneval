def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of comparable elements.

    Returns:
        bool: True if the list is monotonic, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    if not l:
        return True

    increasing = decreasing = True

    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            decreasing = False
        elif l[i] < l[i - 1]:
            increasing = False

    return increasing or decreasing

METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([4, 1, 1, 0]) == True
    assert candidate([1, 2, 3, 2, 5, 60]) == False
    assert candidate([1, 2, 3, 4, 5, 60]) == True
    assert candidate([9, 9, 9, 9]) == True


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(monotonic)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)