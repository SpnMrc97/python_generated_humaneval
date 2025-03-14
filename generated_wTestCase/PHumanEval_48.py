def is_palindrome(text: str) -> bool:
    """
    Checks if the given string is a palindrome.
    
    Args:
        text (str): The string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
        
    Examples:
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    # A palindrome reads the same forwards and backwards.
    # We can use slicing to reverse the string and compare with original.
    return text == text[::-1]

METADATA = {}


def check(candidate):
    assert candidate('') == True
    assert candidate('aba') == True
    assert candidate('aaaaa') == True
    assert candidate('zbcd') == False
    assert candidate('xywyx') == True
    assert candidate('xywyz') == False
    assert candidate('xywzx') == False


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(is_palindrome)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)