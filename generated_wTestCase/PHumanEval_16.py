def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of. """
    return len(set(string.lower()))

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('abcde') == 5
    assert candidate('abcde' + 'cade' + 'CADE') == 5
    assert candidate('aaaaAAAAaaaa') == 1
    assert candidate('Jerry jERRY JeRRRY') == 5


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(count_distinct_characters)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)