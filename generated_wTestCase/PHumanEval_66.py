def digitSum(s: str) -> int:
    """
    Calculate the sum of ASCII values of uppercase characters in the input string.

    Parameters:
    s (str): The input string.

    Returns:
    int: Sum of ASCII values of uppercase characters in the string.
    """
    return sum(ord(char) for char in s if char.isupper())

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("") == 0, "Error"
    assert candidate("abAB") == 131, "Error"
    assert candidate("abcCd") == 67, "Error"
    assert candidate("helloE") == 69, "Error"
    assert candidate("woArBld") == 131, "Error"
    assert candidate("aAaaaXa") == 153, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(" How are yOu?") == 151, "Error"
    assert candidate("You arE Very Smart") == 327, "Error"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(digitSum)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)