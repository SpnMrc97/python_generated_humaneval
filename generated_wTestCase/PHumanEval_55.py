def fib(n: int) -> int:
    """Return the n-th Fibonacci number."""
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    
    return b

METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(fib)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)