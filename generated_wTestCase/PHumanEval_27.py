def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
        
    Returns:
        str: The string with flipped case for each character.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return string.swapcase()

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(flip_case)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)