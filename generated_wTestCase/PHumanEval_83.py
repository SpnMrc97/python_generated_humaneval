def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n == 1:
        # For a single-digit number, the only valid number is 1
        return 1

    # Total n-digit numbers: 9 * 10^(n-1)
    total_n_digit_numbers = 9 * (10 ** (n - 1))

    # Numbers starting with 1: 10^(n-1)
    start_with_1 = 10 ** (n - 1)

    # Numbers ending with 1: 9 * 10^(n-2)
    end_with_1 = 9 * (10 ** (n - 2))

    # Numbers starting and ending with 1: 10^(n-2)
    both_start_and_end_with_1 = 10 ** (n - 2)

    # Use the principle of inclusion-exclusion
    return start_with_1 + end_with_1 - both_start_and_end_with_1

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(starts_one_ends)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)