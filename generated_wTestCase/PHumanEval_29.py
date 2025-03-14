from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
        prefix (str): The prefix to filter strings by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(filter_by_prefix)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)