from typing import List

def concatenate(strings: List[str]) -> str:
    """Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string resulting from the concatenation of the input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['x', 'y', 'z']) == 'xyz'
    assert candidate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(concatenate)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)