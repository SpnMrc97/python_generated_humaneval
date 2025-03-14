def solve(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.

    Parameters:
        N (int): A non-negative integer (0 ≤ N ≤ 10000).

    Returns:
        str: The binary representation of the sum of the digits of N.
    """
    # Calculate the sum of the digits of N
    digit_sum = sum(int(digit) for digit in str(N))
    
    # Convert the sum to binary and return the binary string (excluding the '0b' prefix)
    return bin(digit_sum)[2:]

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1000) == "1", "Error"
    assert candidate(150) == "110", "Error"
    assert candidate(147) == "1100", "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(333) == "1001", "Error"
    assert candidate(963) == "10010", "Error"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(solve)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)