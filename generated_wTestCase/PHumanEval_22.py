from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """Filter a given list of any Python values to return only integers.
    
    Args:
        values (List[Any]): A list containing any type of Python values.
        
    Returns:
        List[int]: A list containing only the integer values from the input list.
        
    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([4, {}, [], 23.2, 9, 'adasd']) == [4, 9]
    assert candidate([3, 'c', 3, 3, 'a', 'b']) == [3, 3, 3]


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(filter_integers)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)