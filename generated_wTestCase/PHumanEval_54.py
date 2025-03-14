def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    
    :param s0: First string to compare
    :param s1: Second string to compare
    :return: True if both strings contain the same characters, False otherwise
    """
    # Convert both strings to sets of characters and compare
    return set(s0) == set(s1)

METADATA = {}


def check(candidate):
    assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert candidate('abcd', 'dddddddabc') == True
    assert candidate('dddddddabc', 'abcd') == True
    assert candidate('eabcd', 'dddddddabc') == False
    assert candidate('abcd', 'dddddddabcf') == False
    assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert candidate('aabb', 'aaccc') == False


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(same_chars)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)