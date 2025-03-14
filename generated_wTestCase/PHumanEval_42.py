def incr_list(l: list) -> list:
    """Return list with elements incremented by 1.
    
    Args:
        l (list): A list of integers.

    Returns:
        list: A new list with each element incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

METADATA = {}


def check(candidate):
    assert candidate([]) == []
    assert candidate([3, 2, 1]) == [4, 3, 2]
    assert candidate([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124]


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(incr_list)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)