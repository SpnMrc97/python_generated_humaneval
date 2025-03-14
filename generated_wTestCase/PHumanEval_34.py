def unique(l: list) -> list:
    """Return sorted unique elements in a list.
    
    Args:
        l (list): The list from which to extract unique elements.
        
    Returns:
        list: A sorted list of unique elements.
    
    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(unique)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)