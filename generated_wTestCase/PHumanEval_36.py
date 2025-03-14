def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n
    which are divisible by 11 or 13.
    
    Parameters:
    n (int): The upper limit (exclusive) for checking numbers.
    
    Returns:
    int: Count of digit '7' in numbers divisible by 11 or 13.
    
    Examples:
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for num in range(n):
        if num % 11 == 0 or num % 13 == 0:
            count += str(num).count('7')
    return count

METADATA = {}


def check(candidate):
    assert candidate(50) == 0
    assert candidate(78) == 2
    assert candidate(79) == 3
    assert candidate(100) == 3
    assert candidate(200) == 6
    assert candidate(4000) == 192
    assert candidate(10000) == 639
    assert candidate(100000) == 8026


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(fizz_buzz)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)