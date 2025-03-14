def string_xor(a: str, b: str) -> str:
    """Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
    a (str): First binary string.
    b (str): Second binary string.
    
    Returns:
    str: Result of XOR operation on input strings.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings are of the same length
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Perform XOR operation and build result string
    result = ''.join('1' if char_a != char_b else '0' for char_a, char_b in zip(a, b))
    
    return result

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(string_xor)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)