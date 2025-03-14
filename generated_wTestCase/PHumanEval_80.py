def is_happy(s):
    """
    Check if the string s is happy.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is happy, False otherwise.
    """
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False

    return True

def check(candidate):

    # Check some simple cases
    assert candidate("a") == False , "a"
    assert candidate("aa") == False , "aa"
    assert candidate("abcd") == True , "abcd"
    assert candidate("aabb") == False , "aabb"
    assert candidate("adb") == True , "adb"
    assert candidate("xyy") == False , "xyy"
    assert candidate("iopaxpoi") == True , "iopaxpoi"
    assert candidate("iopaxioi") == False , "iopaxioi"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(is_happy)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)