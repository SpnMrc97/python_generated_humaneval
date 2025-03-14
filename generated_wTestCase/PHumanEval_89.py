def encrypt(s):
    """Encrypts the input string by rotating each alphabet character
    down by four places.
    
    Args:
        s (str): The input string to be encrypted.
        
    Returns:
        str: The encrypted string with each character rotated.
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
            result.append(new_char)
        else:
            # If the character is not a lowercase letter, it remains unchanged
            result.append(char)
    return ''.join(result)

def check(candidate):

    # Check some simple cases
    assert candidate('hi') == 'lm', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('asdfghjkl') == 'ewhjklnop', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('gf') == 'kj', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('et') == 'ix', "This prints if this assert fails 1 (good for debugging!)"

    assert candidate('faewfawefaewg')=='jeiajeaijeiak', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('hellomyfriend')=='lippsqcjvmirh', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh')=='hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', "This prints if this assert fails 3 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate('a')=='e', "This prints if this assert fails 2 (also good for debugging!)"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(encrypt)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)