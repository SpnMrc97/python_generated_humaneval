def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The number to find the largest divisor for.
        
    Returns:
        int: The largest divisor of n that is smaller than n.
        
    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
    return 1  # If no divisor is found, return 1

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(largest_divisor)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)