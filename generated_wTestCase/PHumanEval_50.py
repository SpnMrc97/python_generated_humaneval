def encode_shift(s: str) -> str:
    """
    Returns the encoded string by shifting every character by 5 positions in the alphabet.
    """
    return "".join(
        [chr(((ord(ch) + 5 - ord('a')) % 26) + ord('a')) for ch in s]
    )


def decode_shift(s: str) -> str:
    """
    Takes as input a string encoded with the encode_shift function.
    Returns the decoded string by reversing the shift.
    """
    return "".join(
        [chr(((ord(ch) - 5 - ord('a')) % 26) + ord('a')) for ch in s]
    )


METADATA = {}


def check(candidate):
    from random import randint, choice
    import copy
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        test_str = ''.join(choice(letters) for i in range(randint(10, 20)))  # Usa test_str al posto di 'str'
        encoded_str = encode_shift(test_str)
        assert candidate(copy.deepcopy(encoded_str)) == test_str


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(decode_shift)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)