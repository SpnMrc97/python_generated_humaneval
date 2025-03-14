def correct_bracketing(brackets: str) -> bool:
    """Checks if every opening bracket "<" has a corresponding closing bracket ">".

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    balance = 0
    for char in brackets:
        if char == '<':
            balance += 1
        elif char == '>':
            balance -= 1
        # If balance goes negative, it means there's a closing bracket without a matching opening bracket
        if balance < 0:
            return False
    # In the end, balance should be zero for all brackets to be correctly matched
    return balance == 0

METADATA = {}


def check(candidate):
    assert candidate("<>")
    assert candidate("<<><>>")
    assert candidate("<><><<><>><>")
    assert candidate("<><><<<><><>><>><<><><<>>>")
    assert not candidate("<<<><>>>>")
    assert not candidate("><<>")
    assert not candidate("<")
    assert not candidate("<<<<")
    assert not candidate(">")
    assert not candidate("<<>")
    assert not candidate("<><><<><>><>><<>")
    assert not candidate("<><><<><>><>>><>")


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(correct_bracketing)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)