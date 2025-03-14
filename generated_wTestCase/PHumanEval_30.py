def get_positive(l: list) -> list:
    """
    Return only positive numbers in the list.

    Args:
        l (list): A list of integers.

    Returns:
        list: A list containing only the positive integers from the input list.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]

METADATA = {}


def check(candidate):
    assert candidate([-1, -2, 4, 5, 6]) == [4, 5, 6]
    assert candidate([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1]
    assert candidate([-1, -2]) == []
    assert candidate([]) == []


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(get_positive)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)