def modp(n: int, p: int) -> int:
    """Return 2^n modulo p."""
    return pow(2, n, p)

METADATA = {}


def check(candidate):
    assert candidate(3, 5) == 3
    assert candidate(1101, 101) == 2
    assert candidate(0, 101) == 1
    assert candidate(3, 11) == 8
    assert candidate(100, 101) == 1
    assert candidate(30, 5) == 4
    assert candidate(31, 5) == 3


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(modp)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)