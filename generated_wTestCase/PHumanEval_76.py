def is_simple_power(x, n):
    """Returns True if x is a simple power of n, otherwise False."""
    if x == 1:
        # Any number to the power of 0 is 1, hence 1 is a power of any number n (except n=0).
        return True
    if n < 2:
        # If n is less than 2, it cannot be a base for powers other than 1 when x=1.
        return False

    power = 1
    while power < x:
        power *= n
    return power == x

def check(candidate):

    # Check some simple cases
    assert candidate(16, 2)== True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(143214, 16)== False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(4, 2)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(9, 3)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(16, 4)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(24, 2)==False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(128, 4)==False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(12, 6)==False, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1)==True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(1, 12)==True, "This prints if this assert fails 2 (also good for debugging!)"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(is_simple_power)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)