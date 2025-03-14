def hex_key(num):
    """Counts the number of prime hexadecimal digits in a given hexadecimal number string."""
    # Define the set of prime hexadecimal digits
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    
    # Initialize a counter for prime digits
    prime_count = 0

    # Iterate over each character in the input string
    for char in num:
        # Increment the counter if the character is in the set of prime digits
        if char in prime_hex_digits:
            prime_count += 1
    
    return prime_count

def check(candidate):

    # Check some simple cases
    assert candidate("AB") == 1, "First test error: " + str(candidate("AB"))      
    assert candidate("1077E") == 2, "Second test error: " + str(candidate("1077E"))  
    assert candidate("ABED1A33") == 4, "Third test error: " + str(candidate("ABED1A33"))      
    assert candidate("2020") == 2, "Fourth test error: " + str(candidate("2020"))  
    assert candidate("123456789ABCDEF0") == 6, "Fifth test error: " + str(candidate("123456789ABCDEF0"))      
    assert candidate("112233445566778899AABBCCDDEEFF00") == 12, "Sixth test error: " + str(candidate("112233445566778899AABBCCDDEEFF00"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate([]) == 0


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(hex_key)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)