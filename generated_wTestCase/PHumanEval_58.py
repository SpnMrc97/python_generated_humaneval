def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists.

    Args:
        l1 (list): First list of elements.
        l2 (list): Second list of elements.

    Returns:
        list: Sorted list of unique common elements.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]

        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert both lists to sets to find the intersection, which gives common elements
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of two sets
    common_elements = set1.intersection(set2)
    
    # Return the sorted list of common elements
    return sorted(common_elements)

METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(common)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)