def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
    
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in text if char not in vowels)

METADATA = {}


def check(candidate):
    assert candidate('') == ''
    assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert candidate('fedcba') == 'fdcb'
    assert candidate('eeeee') == ''
    assert candidate('acBAA') == 'cB'
    assert candidate('EcBOO') == 'cB'
    assert candidate('ybcd') == 'ybcd'


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(remove_vowels)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)