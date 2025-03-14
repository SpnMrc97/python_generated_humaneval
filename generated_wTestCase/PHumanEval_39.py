from math import isqrt

def is_prime(num: int) -> bool:
    """Return True if the number is prime, else False."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n: int) -> int:
    """
    Return the n-th number that is both a Fibonacci number and prime.
    """
    fib1, fib2 = 1, 1
    count = 0
    
    while True:
        if is_prime(fib1):
            count += 1
            if count == n:
                return fib1

METADATA = {}


def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89
    assert candidate(6) == 233
    assert candidate(7) == 1597
    assert candidate(8) == 28657
    assert candidate(9) == 514229
    assert candidate(10) == 433494437


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(prime_fib)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)