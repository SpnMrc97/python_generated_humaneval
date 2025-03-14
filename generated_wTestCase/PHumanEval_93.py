def encode(message):
    """
    Encodes the given message by swapping the case of all letters
    and replacing all vowels with the letter that appears 2 places
    ahead of that vowel in the English alphabet.

    Parameters:
    message (str): The input string containing only letters.

    Returns:
    str: The encoded message.
    """
    # Define a mapping for vowels to their replacements
    vowel_mapping = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    
    encoded_message = []

    for char in message:
        if char in vowel_mapping:
            # Replace vowel with its corresponding mapped character
            encoded_message.append(vowel_mapping[char])
        else:
            # Swap case of the character
            encoded_message.append(char.swapcase())

    return ''.join(encoded_message)

def check(candidate):
    # Check some simple cases
    assert candidate('TEST') == 'tGst'
    assert candidate('YES') == 'yGs'


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(encode)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)