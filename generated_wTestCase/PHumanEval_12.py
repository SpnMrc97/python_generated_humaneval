from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """Returns the longest string from a list of strings. If there are multiple strings of the
    same maximum length, the first one encountered is returned. If the input list is empty, 
    return None.
    
    Args:
        strings (List[str]): A list of strings to evaluate.
        
    Returns:
        Optional[str]: The longest string, or None if the list is empty.
    
    Examples:
        >>> longest([])
        None
        
        >>> longest(['a', 'b', 'c'])
        'a'
        
        >>> longest(['a', 'bb', 'ccc'])
        'ccc'
    """
    if not strings:
        return None
    
    return max(strings, key=len)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == None
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(longest)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)