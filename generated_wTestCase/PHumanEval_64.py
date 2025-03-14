def vowels_count(s: str) -> int:
    """Returns the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel
    only when it is at the end of the string.
    
    Args:
        s (str): The input string.
        
    Returns:
        int: The number of vowels in the string.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = s.lower()  # Convert the string to lowercase to handle case insensitivity
    count = sum(1 for char in s if char in vowels)
    
    # Check if 'y' is at the end and add to count if it's there
    if s.endswith('y'):
        count += 1
    
    return count

def check(candidate):

    # Check some simple cases
    assert candidate("abcde") == 2, "Test 1"
    assert candidate("Alone") == 3, "Test 2"
    assert candidate("key") == 2, "Test 3"
    assert candidate("bye") == 1, "Test 4"
    assert candidate("keY") == 2, "Test 5"
    assert candidate("bYe") == 1, "Test 6"
    assert candidate("ACEDY") == 3, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(vowels_count)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)