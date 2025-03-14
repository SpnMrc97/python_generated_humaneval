def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_multiply_prime(a):
    """Returns True if the given number is the multiplication of exactly 3 prime numbers, False otherwise."""
    if a < 2:
        return False

    primes = [i for i in range(2, a) if is_prime(i)]
    
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False

def check(candidate):

    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(3 * 5 * 7) == True
    assert candidate(3 * 6 * 7) == False
    assert candidate(9 * 9 * 9) == False
    assert candidate(11 * 9 * 9) == False
    assert candidate(11 * 13 * 7) == True


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(is_multiply_prime)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)