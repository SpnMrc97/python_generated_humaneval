def strlen(string: str) -> int:
    """Return the length of the given string.

    Args:
        string (str): The string whose length is to be calculated.

    Returns:
        int: The length of the string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(strlen)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)