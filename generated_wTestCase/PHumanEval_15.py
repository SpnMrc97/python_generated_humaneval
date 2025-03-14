def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive."""
    return ' '.join(str(i) for i in range(n + 1))

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(string_sequence)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)