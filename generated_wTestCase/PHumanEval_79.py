def decimal_to_binary(decimal):
    """
    Converts a decimal number to its binary representation and wraps the binary
    string with 'db' at the beginning and end.

    Args:
        decimal (int): The decimal number to convert.

    Returns:
        str: The binary representation of the decimal number with 'db' at the
             start and end.
    """
    # Convert the decimal number to binary and remove the '0b' prefix
    binary_representation = bin(decimal)[2:]
    
    # Format with 'db' at the beginning and end
    result = f"db{binary_representation}db"
    
    return result

def check(candidate):

    # Check some simple cases
    assert candidate(0) == "db0db"
    assert candidate(32) == "db100000db"
    assert candidate(103) == "db1100111db"
    assert candidate(15) == "db1111db", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(decimal_to_binary)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)