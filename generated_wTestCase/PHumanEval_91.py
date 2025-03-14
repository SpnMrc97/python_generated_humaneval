def is_bored(S):
    """
    Count the number of sentences that start with the word 'I'.
    Sentences are delimited by '.', '?' or '!'.
    
    Parameters:
    S (str): A string containing multiple sentences.
    
    Returns:
    int: The count of sentences starting with 'I'.
    
    Examples:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Split the string into sentences based on delimiters: '.', '?', '!'
    sentences = [sentence.strip() for sentence in re.split(r'[.!?]', S)]
    
    # Count how many sentences start with the word 'I'
    boredom_count = sum(1 for sentence in sentences if sentence.startswith('I'))
    
    return boredom_count

def check(candidate):

    # Check some simple cases
    assert candidate("Hello world") == 0, "Test 1"
    assert candidate("Is the sky blue?") == 0, "Test 2"
    assert candidate("I love It !") == 1, "Test 3"
    assert candidate("bIt") == 0, "Test 4"
    assert candidate("I feel good today. I will be productive. will kill It") == 2, "Test 5"
    assert candidate("You and I are going for a walk") == 0, "Test 6"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(is_bored)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)