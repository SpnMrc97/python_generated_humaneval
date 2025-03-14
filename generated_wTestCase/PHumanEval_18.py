def how_many_times(string: str, substring: str) -> int:
    """ 
    Find how many times a given substring can be found in the original string, counting overlapping cases.
    
    Args:
        string (str): The string to search within.
        substring (str): The substring to search for.
        
    Returns:
        int: The number of times the substring appears in the string, including overlaps.
    
    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if not string or not substring:
        return 0
    
    count = start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1  # Move one character forward to allow overlapping matches
    
    return count

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('', 'x') == 0
    assert candidate('xyxyxyx', 'x') == 4
    assert candidate('cacacacac', 'cac') == 4
    assert candidate('john doe', 'john') == 1


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(how_many_times)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)