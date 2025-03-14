def max_element(lst: list) -> int:
    """Return maximum element in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The maximum integer in the list.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("The list is empty and has no maximum element.")
    return max(lst)

METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(max_element)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)